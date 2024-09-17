from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.textinput import TextInput


class IntegerTextInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        # Only allow numeric input (digits 0-9)
        if substring.isdigit():
            super().insert_text(substring, from_undo)
        # Optional: You can play a sound or show a message here if the input is invalid


class GridLayoutFood(GridLayout):
    my_text_1 = StringProperty("1")
    my_text_2 = StringProperty("1")
    my_text_3 = StringProperty("1")
    my_text_4 = StringProperty("1")

    count_enabled = BooleanProperty(False)

    def on_button_click_plus(self, text_property):
        current_value = getattr(self, text_property)
        new_value = str(int(current_value) + 1)
        setattr(self, text_property, new_value)

    def on_button_click_minus(self, text_property):
        current_value = getattr(self, text_property)
        new_value = str(int(current_value) - 1)
        setattr(self, text_property, new_value)

    def on_text_validate(self, text_property, text_input):
        # Update the corresponding my_text property with the value from TextInput
        new_value = text_input.text
        setattr(self, text_property, new_value)


class LafiApp(App):
    pass


if __name__ == '__main__':
    LafiApp().run()
