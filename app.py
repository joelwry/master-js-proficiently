import flet as ft
#from utilities import helper
from components.lesson_content import LessonView,lessonAppBar,introPage,createfloatingButton,createGeneralAppBar
from components.lesson_quiz import QuizView
	

def main(page: ft.Page):
    page.horizontal_alignment ="CENTER"
    page.scroll = 'AUTO'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 414

    def lessonRoute(topic_index = None) -> None:
        print(f'Topic Index : {topic_index}')
        component1 = LessonView("./mdfiles/section1.md","/")
        if not topic_index: 
           lessonAppBar(component1.view,component1.updateMarkDownContent)
        else :
           lessonAppBar(component1.view,component1.updateMarkDownContent,topic_index)

        page.views.append(component1.view)  
        page.vertical_alignment ="CENTER"

        page.update()

    def route_change(e):
        print('Present Route accessed ' + page.route)
        page.views.clear()

        page.views.append(
            ft.View(
                "/",
                [
                    createGeneralAppBar('Modern Javascript Tutor'),
                    ft.ElevatedButton("Start Lesson", on_click=lambda _: page.go("/lesson")),
                    
                    createfloatingButton('code',ft.icons.CODE_OUTLINED),
                    introPage(page),

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        if page.route =="/":
            page.horizontal_alignment ="CENTER"
            page.update()
            return
        
        if page.route == "/lesson":
            lessonRoute()
            return

        elif ft.TemplateRoute(page.route).match("/lesson/:index"):
            print(f'Present Route : {page.route}')
            router = ft.TemplateRoute(page.route)
            if router.match('/lesson/:index'):
                lessonRoute(router.index)

        else :
            router = ft.TemplateRoute(page.route)
            if router.match("/quiz/:id/:index"):
                print("ID:", router.id)
                print("ACTIVE INDEX:", router.index)
                quiz_id = router.id

                # this function will be assigned to an event listener so as to enable the user go back to lessons
                def backToLesson(e):
                    page.go(f"/lesson/{router.index}")

                page.views.append(
                    ft.View(
                        f"/quiz/{quiz_id}",
                        controls=[
                            createGeneralAppBar('Quiz'),
                            QuizView(quiz_id, 5),
                            createfloatingButton('Lesson',ft.icons.BOOK,backToLesson),
                        ],
                        #scroll=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        vertical_alignment= ft.MainAxisAlignment.CENTER,
                        #padding= ft.padding.symmetric(10,40)
                    )
                )
                
                page.vertical_alignment = 'START'
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


ft.app(target=main)

