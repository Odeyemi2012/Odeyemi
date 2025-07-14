from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CalculatorLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.text_input = TextInput(multiline=False, font_size=30)
        self.add_widget(self.text_input)

        buttons_layout = BoxLayout(orientation='vertical')
        buttons_row1 = BoxLayout()
        buttons_row1.add_widget(Button(text='7', on_press=lambda x: self.append_text('7')))
        buttons_row1.add_widget(Button(text='8', on_press=lambda x: self.append_text('8')))
        buttons_row1.add_widget(Button(text='9', on_press=lambda x: self.append_text('9')))
        buttons_row1.add_widget(Button(text='/', on_press=lambda x: self.append_text('/')))
        buttons_layout.add_widget(buttons_row1)

        buttons_row2 = BoxLayout()
        buttons_row2.add_widget(Button(text='4', on_press=lambda x: self.append_text('4')))
        buttons_row2.add_widget(Button(text='5', on_press=lambda x: self.append_text('5')))
        buttons_row2.add_widget(Button(text='6', on_press=lambda x: self.append_text('6')))
        buttons_row2.add_widget(Button(text='*', on_press=lambda x: self.append_text('*')))
        buttons_layout.add_widget(buttons_row2)

        buttons_row3 = BoxLayout()
        buttons_row3.add_widget(Button(text='1', on_press=lambda x: self.append_text('1')))
        buttons_row3.add_widget(Button(text='2', on_press=lambda x: self.append_text('2')))
        buttons_row3.add_widget(Button(text='3', on_press=lambda x: self.append_text('3')))
        buttons_row3.add_widget(Button(text='-', on_press=lambda x: self.append_text('-')))
        buttons_layout.add_widget(buttons_row3)

        buttons_row4 = BoxLayout()
        buttons_row4.add_widget(Button(text='0', on_press=lambda x: self.append_text('0')))
        buttons_row4.add_widget(Button(text='.', on_press=lambda x: self.append_text('.')))
        buttons_row4.add_widget(Button(text='=', on_press=self.calculate))
        buttons_row4.add_widget(Button(text='+', on_press=lambda x: self.append_text('+')))
        buttons_layout.add_widget(buttons_row4)

        self.add_widget(buttons_layout)

    def append_text(self, text):
        self.text_input.text += text

    def calculate(self, instance):
        try:
            result = eval(self.text_input.text)
            self.text_input.text = str(result)
        except Exception as e:
            self.text_input.text = 'Error'

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run()