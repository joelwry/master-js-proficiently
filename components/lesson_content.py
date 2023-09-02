import flet as ft
from utilities.helper import copyToClipboard, extract_code_section,schemeOfWork, sectionalSummary,readSectionStringContent

ct1 = "shades-of-purple"
ct2 = "monokai-sublime"
ct3 = "zenburn"
ct4 = "codepen-embed"
ct5 = "brown-paper"


class LessonView():

    def __init__(self, file_path, route_path):

        self.readFileContent(file_path)
        self.markdown = ft.Markdown(
            self.code,
            extension_set="gitHubWeb",
            code_theme=ct1,
            expand=False,
            selectable=True,
            on_tap_link=self.mdCopyActionCode,
            code_style=ft.TextStyle(font_family="Roboto Mono"))

        self.float_button = ft.FloatingActionButton(
            icon=ft.icons.TIMER,
            on_click=self.questionLink,
            bgcolor="#cbbbe8",#ft.colors.AMBER_300,
            shape=ft.RoundedRectangleBorder(
                radius=ft.BorderRadius(60, 60, 60, 60)),
            width=100,
            text="Quiz",
            mini=True)

        col = ft.Column([self.markdown], height=600, scroll="AUTO")
        self.row = ft.ResponsiveRow(
            [
                ft.Column([
                    
                ],col=0.5),
                ft.Column([col],col=11),
            ],
            height=800,
            expand=True
        )
        self.view = ft.View(
            controls=[self.row],
            floating_action_button=self.float_button)

    def mdCopyActionCode(self, e):
        code_extracted = extract_code_section(self.code,
                                              e.data)  # Fix: Added self.code
        print(f'Code Extracted: {code_extracted}')
        copyToClipboard(code_extracted)  # Fix: Used the function directly
        print('Code successfully copied')

    def questionLink(self, e):
        quiz_name = e.control.tooltip
        lesson_active_index = e.control.data
        if quiz_name : 
            page = self.markdown.page
            page.go(f'/quiz/{quiz_name}/{lesson_active_index}')
        else :
            self.view.page.snack_bar = ft.SnackBar(ft.Text("No quiz for this lesson"),duration=2000)
            self.view.page.snack_bar.open = True
            self.view.page.update()
            print('No quiz to load yet')

    def readFileContent(self, file_path):
        try:
            with open(file_path, "r") as fp:
                self.code = fp.read()
        except Exception as e:
            print('Error occurred while reading the file')
            self.code = "### No Lesson Available"  # Fix: Corrected formatting and added space

    def updateMarkDownContent(self,file_path):
        self.readFileContent(file_path)
        self.markdown.value = self.code


# works for lesson view
def appBar(view, updateMarkDownFunction,index_from_quiz=None):

    header_title = ft.Text("JAVASCRIPT TUTORIALS",size="30")
    LEFT_ICON_BTN = ft.IconButton(ft.icons.ARROW_LEFT)
    RIGHT_ICON_BTN = ft.IconButton(ft.icons.ARROW_RIGHT)
    
    
    ACTIVE_MENU_ITEM = None
    # setting the state of active menu item index which is to be as a result of the first lesson to be served to the user
    ACTIVE_MENU_ITEM_INDEX = 1
    POPMENU_REF :dict = {}

    # passing the quiz question data to load through the quiz floatbtn tooltip
    def setFloatingBtnQuestionLink(quiz_name):
        float_btn = view.floating_action_button
        float_btn.tooltip = quiz_name

        # adding a data attribute representing the current state of mark down
        float_btn.data = ACTIVE_MENU_ITEM_INDEX
        print(f'quiz question to load : {float_btn.tooltip}')
        print(f'quiz question ref id : {float_btn.data}')

    def activateMenuIndexAndMenuItem() -> str or None :
        nonlocal ACTIVE_MENU_ITEM, ACTIVE_MENU_ITEM_INDEX
        quiz_file_name = None
        for key in POPMENU_REF:
            if ACTIVE_MENU_ITEM == POPMENU_REF[key]['control']:
                # store the key 
                ACTIVE_MENU_ITEM_INDEX = key
                quiz_file_name = POPMENU_REF[key]["question"]
        return quiz_file_name

    def getActiveMenuCheckedINDEX() -> None:
        quiz_file_name = activateMenuIndexAndMenuItem()
        setFloatingBtnQuestionLink(quiz_file_name)
    
    # this function helps to put clicked menu item in a check state while removing previously checked state
    def menuItemChecked(e):
        nonlocal ACTIVE_MENU_ITEM
        if e :
            if ACTIVE_MENU_ITEM == None :
                ACTIVE_MENU_ITEM = e.control
                ACTIVE_MENU_ITEM.checked = True
            else:
                ACTIVE_MENU_ITEM.checked = None
                ACTIVE_MENU_ITEM = e.control
                ACTIVE_MENU_ITEM.checked = True
        else :
            # use the active menu item index that has been updated to change the control
            if ACTIVE_MENU_ITEM :
                ACTIVE_MENU_ITEM.checked = None
            ACTIVE_MENU_ITEM = POPMENU_REF[ACTIVE_MENU_ITEM_INDEX]['control']
            ACTIVE_MENU_ITEM.checked = True
        
        # storing/UPDATING the checked POPUPMENU ITEM INDEX
        getActiveMenuCheckedINDEX()

    # update state and markdown based on current index and topic. to be used when we coming back from quiz page
    def updateBasedOnActiveIndex(active_index):
        nonlocal ACTIVE_MENU_ITEM_INDEX,ACTIVE_MENU_ITEM
        ACTIVE_MENU_ITEM_INDEX = int(active_index)
        ACTIVE_MENU_ITEM = POPMENU_REF[ACTIVE_MENU_ITEM_INDEX]['control']
        ACTIVE_MENU_ITEM.checked = True
        quiz_file_name = activateMenuIndexAndMenuItem()
        setFloatingBtnQuestionLink(quiz_file_name)
        updateMarkDownFunction(f'./mdfiles/{quiz_file_name}.md')
        #view.update()


    # screen resize 
    # work on this function in a more global file such as main page etc
    def resizeHeaderBar(e):
        if e.control.width < 400:
            header_title.size = "15"
        else :
            header_title.size = "30"
        e.control.update()


    # EVENT LISTENER THAT ENABLES MARKDOWN TO BE UPDATED
    def updateMarkDown(e,file_name):
        updateMarkDownFunction(f'./mdfiles/{file_name}')
        menuItemChecked(e)
        view.page.update()
        #need to be removed FROM here
        view.page.on_resize = resizeHeaderBar 

    
    schemes = schemeOfWork()
    section_summary = sectionalSummary()
    pop_up_items : list = []

    # creating pop menu item buttons
    count = 0
    for key in schemes :
        pop_menu_section = ft.PopupMenuItem(
                content = ft.Text(f"Section {key}",size = 20,
                            weight= ft.FontWeight.BOLD
                        ),
                on_click = lambda e, file_name =section_summary[key]['file_name']:updateMarkDown(e,file_name)
                )
        count += 1

        pop_up_items.extend([
            pop_menu_section,
            ft.PopupMenuItem(), #Divider
        ])

        # storing the popmenu item which is the section phase into the POPMENUREF 
        POPMENU_REF[count] = {
            "control" : pop_menu_section,
            "file_name": section_summary[key]['file_name'],
            "question" : None
        }

        for index,data in enumerate(schemes[key]):
            pop_menu_btn = ft.PopupMenuItem(text=data['topic'], on_click = lambda e, file_name =data['file_name']:updateMarkDown(e,file_name))
            pop_up_items.append(pop_menu_btn)
            
            count += 1
            # storing the popmenu item which is the section phase into the POPMENUREF 
            POPMENU_REF[count] = {
                "control" : pop_menu_btn,
                "file_name": data['file_name'],
                "question" : data['question_name']
            }

        pop_up_items.append(ft.PopupMenuItem())


    def onLeftIconClick(e):
        nonlocal ACTIVE_MENU_ITEM_INDEX
        if ACTIVE_MENU_ITEM_INDEX > 1:
            ACTIVE_MENU_ITEM_INDEX -= 1
        file_name = POPMENU_REF[ACTIVE_MENU_ITEM_INDEX]['file_name']
        updateMarkDown(None, file_name)

    def onRightIconClick(e):
        nonlocal ACTIVE_MENU_ITEM_INDEX
        if ACTIVE_MENU_ITEM_INDEX < POPMENU_REF.__len__():
            ACTIVE_MENU_ITEM_INDEX += 1
        file_name = POPMENU_REF[ACTIVE_MENU_ITEM_INDEX]['file_name']
        updateMarkDown(None, file_name)

    # Assign event listeners to the icon buttons
    LEFT_ICON_BTN.on_click = onLeftIconClick
    RIGHT_ICON_BTN.on_click = onRightIconClick

    #COLORS : PRIMARY_CONTAINER,AMBER_100
    view.appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU),
        leading_width=70,
        title=header_title,
        center_title=False,
        bgcolor=ft.colors.GREY_200,
        toolbar_height=74.0,
        actions=[
            LEFT_ICON_BTN,
            RIGHT_ICON_BTN,
            ft.PopupMenuButton(
                items = pop_up_items
            ),
        ])

    
    if index_from_quiz:
        updateBasedOnActiveIndex(index_from_quiz)


def introPage(page:ft.Page):

    schemes = schemeOfWork()
    section_summary = sectionalSummary()

    widget = []
    count = 0
    for key in schemes :
        count += 1
        section_tile = ft.ListTile(
            title=ft.Text(f"Section {key}",size = 20,weight= ft.FontWeight.BOLD),
            subtitle=ft.Text(readSectionStringContent(section_summary[key]['file_name']),spans=[
                                ft.TextSpan(
                                "\n\nTopics",
                                ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                                )])
            )
        topics_btn = []      
        for index,data in enumerate(schemes[key]):
            count += 1
            topics_btn.append(ft.TextButton(data['topic'],on_click=lambda e,count_index = count: page.go(f"/lesson/{count_index}")))
        
        # used to set a margin bottom to our view page
        mg_bottom = 0 if count  < 25 else 45
        
        widget.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            section_tile,
                            ft.Column(topics_btn,
                                #alignment=ft.MainAxisAlignment.END,
                                horizontal_alignment= ft.CrossAxisAlignment.START
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        #height= 350,
                        scroll='AUTO'
                    ),
                    width=300,
                    padding=20,
                    height=500,
                ),
                margin=ft.margin.only(15,0,25,mg_bottom),
                elevation = 4,
                surface_tint_color ="#0000f3"
            )
        )

    return ft.Row(
        wrap=True,
        spacing=15,
        run_spacing=50,
        controls=widget,
        scroll = "AUTO",
        vertical_alignment = ft.CrossAxisAlignment.START,
        #width =page_width,
        expand=True,
        tight= True,
    )


def createfloatingButton(floating_text:str, clickAction=None) -> ft.FloatingActionButton:
    float_button = ft.FloatingActionButton(
        icon=ft.icons.CODE_OUTLINED,
        on_click=clickAction,
        bgcolor="#cbbbe8",##5B9CDE",
        shape=ft.RoundedRectangleBorder(
            radius=ft.BorderRadius(60, 60, 60, 60)),
        width=100,
        text=floating_text,
        mini=True
    )
    return float_button

def createGeneralAppBar(page_title : str) -> ft.AppBar :
    app_bar = ft.AppBar(title=ft.Text(page_title), bgcolor=ft.colors.SURFACE_VARIANT,toolbar_height=74.0,leading=ft.IconButton(ft.icons.MENU),
        leading_width=70)
    return app_bar