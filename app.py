import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        head_lable = Label(text="User Registration App", font_size=26, bold=True, height=40)

        #adding input lables and fields

        name_lable = Label(text="Full Name:", font_size=18)
        self.name_input = TextInput(multiline=False, font_size=18)

        email_lable = Label(text="Email Address:", font_size=18)
        self.email_input = TextInput(multiline=False, font_size=18)

        password_lable = Label(text="Password:", font_size=18)
        self.password_input = TextInput(multiline=False, font_size=18, password=True)

        confirmPassword_lable = Label(text="Confrim Password:", font_size=18)
        self.confirmPassword_input = TextInput(multiline=False, font_size=18, password=True)

        #submit button
        submit_button = Button(text='Register', font_size=18)



        layout.add_widget(head_lable)
        layout.add_widget(name_lable)
        layout.add_widget(self.name_input)
        layout.add_widget(email_lable)
        layout.add_widget(self.email_input)
        layout.add_widget(password_lable)
        layout.add_widget(self.password_input)
        layout.add_widget(confirmPassword_lable)
        layout.add_widget(self.confirmPassword_input)
        layout.add_widget(submit_button)
        return layout


if __name__ == '__main__':
    RegistrationApp().run()