from flet import UserControl, Text, Container, Stack, ProgressRing,Margin,ResponsiveRow,TextThemeStyle,FontWeight,alignment,padding
from time import sleep
 
class CircularLoading(UserControl):

    def __init__(self,text_initial_value):
        super().__init__()
        self.pre_initial_value = text_initial_value
    
    def build(self):
        self.progress_control = ProgressRing(width=220, height=220, stroke_width = 10, color="#7BC3F1",tooltip='calculating',col=6,) #bgcolor='#cbbbe8',)

        self.text_control = Text("0%", left=100,top=100,weight=FontWeight.W_900,style=TextThemeStyle.HEADLINE_LARGE, text_align='center')
        stacked = Stack([self.progress_control,self.text_control])
        container = Container(
            margin=Margin(10, 10, 10, 10),
            padding=padding.all(30),
            clip_behavior='ANTI_ALIAS_WITH_SAVE_LAYER',
            alignment = alignment.center,
            content = stacked,
            col = 12
        )
        
        return ResponsiveRow([Text(f"{self.pre_initial_value}...", style="headlineSmall",col=12,text_align='center'),container])

    def will_unmount(self):
        print('UNMOUNTING CIRCULAR PROGRESS BAR')

        self.page_ref.on_resize.unsubscribe(self.evt)
        print('Successfully unsubscribed from event')
        print(f'Counts of handler : {self.page_ref.on_resize.count()}')
        #self.page_ref.update()

    def did_mount(self):    
        print('\nCircular Progress Bar Successfully mounted\n')
        self.page_ref = self.progress_control.page

        def screenSizeChanged(e):
            if self.page_ref.window_width <= 400 :
                self.progress_control.width = 100
                self.progress_control.height = 100
                self.progress_control.stroke_width = 2
                self.text_control.style = "headlineSmall"
                self.text_control.size = 10
                self.text_control.left = 45
                self.text_control.top = 45
            else :
                self.progress_control.width = 180
                self.progress_control.height = 180
                self.progress_control.stroke_width = 5
                self.text_control.style = "headlineSmall"
                self.text_control.left = 85
                self.text_control.top = 85
                self.text_control.size = 15

            if len(self.text_control.value) > 5 :         
                self.text_control.style = "bodySmall"
                self.text_control.left = 45
                self.text_control.top = 85

                if self.page_ref.window_width <= 300:
                    self.text_control.left = 3
                    self.text_control.top = 40
                    self.text_control.size = 8
                if self.page_ref.window_width > 300:
                    self.text_control.top = 50
                    self.text_control.size = 10

            self.page_ref.update()

        # setting a class variable to have a ref to eventhandler so we can unsubscribe from it as @ when needed
        self.evt = screenSizeChanged
        self.page_ref.on_resize = self.evt
        self.animateCircularValue(self.progress_control,self.text_control)
        
        self.update()
            
    def animateCircularValue(self,progress_ring : ProgressRing, text : Text):
        #page = progress_ring.page
        for i in range(0, 101):
            result =  i * 0.01
            progress_ring.value = result
            text.value = f'{i}%'
            sleep(0.1)
            self.update()

        text.value = "COMPILED"
        self.update()


