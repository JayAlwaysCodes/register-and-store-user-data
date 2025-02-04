import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

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
        submit_button = Button(text='Register', font_size=18, on_press=self.register)



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

    def register(self, instance):
        #collect user details
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirmPassword_input.text

        #validation 
        if name.strip() == '' or email.strip() == '' or password.strip =='' or confirm_password.strip=='':
            message = "Please fill in all fields"
        elif password != confirm_password:
            message = "Enter a match password"

        else:
            filename = name + '.txt'
            with open(filename, 'w') as file:
                file.write('Full Name: {}\n'.format(name))
                file.write('Email Address: {}\n'.format(name))
                file.write('Password: {}\n'.format(password))
            message = "Details Saved Succesfully!\nFull Name: {}\nEmail Address: {}".format(name, email)

        #notification
        popup = Popup(title = "Registration Status", content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()



if __name__ == '__main__':
    RegistrationApp().run()