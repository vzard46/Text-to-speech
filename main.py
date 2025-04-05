from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

import pyttsx3
import random


# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 140)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

default_text = "Welcome to the Interactive Text-to-Speech App!"

class TextToSpeechApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.background_color = (1, 0.9, 0, 1)  # A slightly softer yellow

        layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Create label without animation
        self.label = Label(text="Enter your text", size_hint=(1, 0.2), color=(0, 0, 0, 1),
                           font_size=250, bold=True)
        self.label.pos_hint = {'top': 1}  # Align the label to the top
        layout.add_widget(self.label)

        # Create the TextInput widget without animation
        self.text_input = TextInput(hint_text="Type something", size_hint=(1, 1.5), multiline=False,
                                    background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))
        self.text_input.pos_hint = {'center_x': 0.5}
        layout.add_widget(self.text_input)

        # GridLayout for buttons (only Speak button now)
        button_layout = GridLayout(cols=1, spacing=10, size_hint=(None, None), width=200, height=100)
        button_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.3}

        # Speak button
        self.speak_button = Button(text="Speak", size_hint=(1, None), height=50,
                                    background_color=(1, 1, 1, 1), font_size=18, color=(0, 0, 0, 1))
        self.speak_button.bind(on_press=self.speak)
        button_layout.add_widget(self.speak_button)

        layout.add_widget(button_layout)

        self.root = layout
        self.speak_on_start()

        return self.root

    def speak_on_start(self):
        # Speak out the default text when the app starts
        engine.say(default_text)
        engine.runAndWait()

    def speak(self, instance):
        text = self.text_input.text
        if text:
            # Speak out the text entered by the user
            engine.say(text)
            engine.runAndWait()
        else:
            # Give feedback if text is empty
            engine.say("Please enter some text first!")
            engine.runAndWait()

    def focus_on_text_input(self, instance):
        # Focus on the text input when the button is clicked
        self.text_input.focus = True

if __name__ == "__main__":
    TextToSpeechApp().run()
