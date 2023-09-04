import flet as ft
import threading
import time
import json
import random
from components.single.circular_loading import CircularLoading


class Option(ft.UserControl):

    def __init__(self, option_text):
        super().__init__()
        self.option_text = option_text

    def build(self):
        return ft.Container(
            bgcolor=ft.colors.GREY_50,
            margin=ft.Margin(2, 10, 2, 10),
            padding=ft.Padding(20, 15, 15, 10),
            clip_behavior='ANTI_ALIAS_WITH_SAVE_LAYER',
            content=ft.ResponsiveRow([
                ft.Radio(value=self.option_text, col=0.9),
                ft.Text(self.option_text, max_lines=6, no_wrap=False, overflow='CLIP', col=11)
            ])
        )

class QuizQuestionWidget(ft.UserControl):

    def did_mount(self):
        print('\nQuiz Widget Successfully mounted\n')

    def will_unmount(self):
        print('\nQuiz Widget To be Unmounted\n')
        self.thread_stopper.set()
        

        
    def __init__(self, question_data,user_answers, on_next_click):
        super().__init__()
        self.question_data = question_data
        self.on_next_click = on_next_click
        self.timer_thread = None
        self.remaining_time = 60  # in seconds

        # the user_answers is an object hence we will be able to track the user selection through here and it will reflect in the outside world where it was passed from
        self.user_answers = user_answers
        #auto-setting the user selection to none
        self.user_answers[question_data['id']] = {
            "question" : question_data['question'],
            "answer" : None 
        }

    def build(self):
        question_number = f"Question {self.question_data['number']} / {self.question_data['total']}"

        question_text = ft.Text(self.question_data['question'], size=20, weight=ft.FontWeight.BOLD)

        options = []
        for option in self.question_data['options']:
            option_widget = Option(option)
            options.append(option_widget)

        options_column =  ft.RadioGroup(content=ft.Column(options), on_change=self.handle_option_change)

        next_text = "Submit" if self.question_data['number'] == self.question_data['total'] else "Next"
        next_button = ft.ElevatedButton(next_text, on_click=lambda e : self.move_to_next_question())

        column_content_holder = ft.Column(
            [
                ft.Text(question_number, size=14, italic=True, color=ft.colors.LIGHT_BLUE_ACCENT_400),
                question_text,
                options_column,
                next_button
            ]
        )

        # Show the remaining time using a Text widget
        self.remaining_time_tf = ft.Text(f"Remaining Time: {self.remaining_time} seconds", size=16)
        
        self.start_timer()
        self.container = ft.Container(
            border_radius=10,
            margin=ft.Margin(20, 30, 20, 30),
            padding=20,
            bgcolor="#44CCCCCC",
            blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors.BLUE_GREY_300,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            content=ft.Column([
                self.remaining_time_tf,
                column_content_holder
            ])
        )
        return self.container

    def handle_option_change(self, e):
        # setting the user answer
        self.user_answers[self.question_data['id']]['answer'] = e.control.value
        

    def start_timer(self):
        if self.timer_thread is None or not self.timer_thread.is_alive():
            self.timer_thread = threading.Thread(target=self.run_timer)
            self.thread_stopper = threading.Event()
            self.timer_thread.start()

    def run_timer(self):
        while self.remaining_time > 0:
            time.sleep(1)
            self.remaining_time -= 1

            print(f'REMAINING TIME :  {self.remaining_time}')

            # Update the UI with the remaining time
            if self.remaining_time < 30 :
                self.remaining_time_tf.color = 'red'
            self.remaining_time_tf.value = f"Remaining Time: {self.remaining_time} seconds"
            
            #stopping the thread using event object monitoring
            if self.thread_stopper.is_set():
                print('Stopping Thread with event')
                break

            if self.remaining_time == 0:
                self.move_to_next_question()
                break

            #Update the Text widget
            try:
                self.update()
            except Exception as e :
                print(e)
        print('while loop stooped')

    def move_to_next_question(self):
        self.on_next_click()
        self.thread_stopper.set()
        

# a widget to display user quiz test score 
class ScoreCardWidget(ft.UserControl):
    def __init__(self,quiz_name,user_score_percentage,score_card_text,correct_count,total_count):
        super().__init__()
        self.user_score_percentage = user_score_percentage
        self.quiz_name = quiz_name
        self.score_card_text = score_card_text
        self.correct_count = correct_count
        self.total_question_count = total_count

    def build(self):
        correct_count_color = "red" if self.user_score_percentage < 45 else "#19444e"
        score_card = ft.Container(
            margin=ft.margin.symmetric(30,10),padding=20,alignment=ft.alignment.center,
            bgcolor="#cbbbe8", width=300,height=300,
            border_radius=20,
            blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=4,
                color=ft.colors.BLUE_GREY_300,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            content=ft.Column(
                [
                    ft.Text(
                        spans =[
                            ft.TextSpan(
                                self.quiz_name,
                                ft.TextStyle(
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    foreground=ft.Paint(
                                        gradient=ft.PaintLinearGradient(
                                            (0, 20), (150, 20), [ft.colors.PINK, "#006400"]
                                        )
                                    ),
                                    shadow=ft.BoxShadow(
                                        spread_radius=0,
                                        blur_radius=1,
                                        color="#343743",
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.INNER,
                                    )
                                ),
                            ),
                        ]
                    ),
                    ft.Container(
                        shape=ft.BoxShape.CIRCLE,border_radius=40,padding=30,
                        blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
                        border = ft.border.all(4, 'white'),
                        
                        content=ft.Text(
                            spans =[
                                ft.TextSpan(
                                    f'{self.user_score_percentage:.2f}%',
                                    ft.TextStyle(
                                        size=20,
                                        weight=ft.FontWeight.W_600,
                                        foreground=ft.Paint(
                                            gradient=ft.PaintLinearGradient(
                                                (0, 20), (150, 20), ["#0021400","#19444e"]
                                            )
                                        ),
                                        shadow=ft.BoxShadow(
                                            spread_radius=0,
                                            blur_radius=1,
                                            color="#343743",
                                            offset=ft.Offset(0, 0),
                                            blur_style=ft.ShadowBlurStyle.INNER,
                                        )
                                    ),
                                ),
                            ]
                        )
                    ),
                    ft.Text("Score : ", size=20,
                        spans = [
                            ft.TextSpan(
                                self.correct_count, 
                                ft.TextStyle(
                                    size = 23, weight=ft.FontWeight.BOLD,
                                    color = correct_count_color 
                                )
                            ),
                            ft.TextSpan(
                                " out of ",ft.TextStyle(italic=True)
                            ),
                            ft.TextSpan(
                                self.total_question_count, 
                                ft.TextStyle(
                                    size = 23, weight=ft.FontWeight.BOLD,
                                    color = "#006400" 
                                )
                            )
                        ]
                    ),
                    ft.Text(self.score_card_text, size=21, color=correct_count_color,weight=ft.FontWeight.BOLD,italic=True),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,)
            )
        return score_card



class QuizView(ft.UserControl):

    def __init__(self,question_to_load,amount_to_load):
        super().__init__()
        self.answer_bank = {}
        self.questions = []
        self.loadQuestions(question_to_load, amount_to_load)
        self.quiz_name = question_to_load
        self.user_answers = {}
       
    def did_mount(self):
        print('\nQuiz Component Mounted to Page Successfully\n')

    def will_unmount(self):
        print('\nQuiz Component About To Be Removed from Page\n')
        
    # loading multiple questions from json files    
    def loadQuestions(self,question_to_load,amounts):
        with open(f'./questions/{question_to_load}.json') as json_questions :
            questions = random.sample(json.load(json_questions),amounts)
            question_length = len(questions)
            for index,question in enumerate(questions):
                index = index + 1
                question['id'] = f'qt{index}'
                question['total'] = question_length
                question['number'] = index

                # mapping question id to answer for ease of score calculation
                self.answer_bank[question['id']] = question['answer']
                # storing questions so as to create quiz component
                self.questions.append(question)

        # reverse question so that the first question would be set for popping
        self.questions.reverse()

    def handleNextQuestion(self):

        #focused on using height of 600 here so as to enable quiz to be scrollable if they overlapp
        if self.main_column.height != 600:
            self.main_column.height = 600
            
        if self.questions :
            #pop out question from 
            current_question = self.questions.pop()
            question_widget = QuizQuestionWidget(current_question, self.user_answers,self.handleNextQuestion)
            self.main_column.controls = [question_widget]
            
        else :
            self.main_column.controls = [CircularLoading("Compiling Quiz Result")]
            self.update()
            print('sleeping time')
            #time.sleep(10)
            # Create the card to display user score
            result_calculation = self.calculateUserScorePercentage()
            user_score_percentage  = result_calculation['percentage']
            score_card_text = self.getScoreCardText(user_score_percentage)

            score_card = ft.Row([
                ScoreCardWidget(self.quiz_name,user_score_percentage,score_card_text,result_calculation['total_correct'],result_calculation['total_question'])
                ],scroll="AUTO",alignment=ft.MainAxisAlignment.CENTER
            )
            self.main_column.controls.pop()
            self.main_column.controls.append(score_card) 
            self.main_column.controls.extend(self.markUserSubmissions())
            self.main_column.height = 625
        
        self.update()

    def build(self):
        self.main_column = ft.Column([ft.ElevatedButton("Start Quiz",on_click=lambda e : self.handleNextQuestion())],scroll="AUTO");
        return self.main_column


    def markUserSubmissions(self):
        # control after being added to page now has access to page as it property 
        #print(self.main_column.controls[0].page)
        #container = ft.Column
        cols = []
        count = 1

        for key in self.answer_bank :

            question = ft.Column([ft.Text(spans=[ft.TextSpan(f'Question {count}',ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE,color='#3D84EF'))]),ft.Text(self.user_answers[key]["question"], size=23,font_family="RobotoSlab",weight=ft.FontWeight.W_200,col=10)],col=12)
            
            user_selection = ft.Text(spans=[
                    ft.TextSpan('selected :', ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE,color='#7420D2')#9986D2
                    ),
                    ft.TextSpan(f' {self.user_answers[key]["answer"]}',ft.TextStyle(size=21,font_family="RobotoSlab",weight=ft.FontWeight.W_600))
                ],col=12)

            result = ft.Text(col=12)
            gotten = self.answer_bank[key] == self.user_answers[key]['answer']
            result.value = "Correct" if gotten else 'Wrong'
            if not gotten:
                user_selection.color = "red"
                result.color ="red"

            cols.append(ft.Container(
                bgcolor=ft.colors.GREY_50,
                margin=ft.Margin(2, 10, 2, 10),
                padding=ft.Padding(20, 15, 15, 10),
                clip_behavior='ANTI_ALIAS_WITH_SAVE_LAYER',
                content=ft.ResponsiveRow([
                    question,
                    user_selection,
                    result
                ])
            ))
            
            count += 1

        return cols

    def calculateUserScorePercentage(self):
        correct_count = sum(
            1
            for key in self.user_answers
            if self.user_answers[key]["answer"] == self.answer_bank[key]
        )
        total_questions = len(self.answer_bank)
        return {
            "percentage":(correct_count / total_questions) * 100,
            "total_correct" : correct_count,
            "total_question":total_questions
        }

    def getScoreCardText(self, user_score_percentage):
        if user_score_percentage >= 80:
            return "Excellent!"
        elif user_score_percentage >= 50:
            return "Passed!"
        else:
            return "Not Cleared."


if __name__ == '__main__':

    def main(page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.scroll = 'AUTO'
        page.vertical_alignment = 'START'
        page.add(QuizView('oop', 5))
        
    ft.app(target=main)
