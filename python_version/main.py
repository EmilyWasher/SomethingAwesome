# Make sure you activate the venv with venv\Scripts\activate
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

kivy.require("1.11.1")


class Reverse(Widget):
    pass


class HomePage(BoxLayout):
    pass


class CipherApp(App):
    def build(self):
        return HomePage()


if __name__ == "__main__":
    CipherApp().run()
