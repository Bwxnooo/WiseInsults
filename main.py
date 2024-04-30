# Import statements (if any)
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

noName = "no name given"
noSurname = "no surname given"
BothMissing = "none of them given"
BothCompiled = "morte a {} {}"

class MainLayout(BoxLayout):
    LabelText = StringProperty("Submit to show a creative insult.")

    def get_name_validated(self, widget):
        return widget.text

    def get_surname_validated(self, widget):
        return widget.text

    def alghoritm(self):
        name = self.get_name_validated(widget=self.ids.name_input)
        surname = self.get_surname_validated(widget=self.ids.surname_input)

        if name == "Name. (Optional)":
            self.LabelText = noName
        if surname == "Surname. (Optional)":
            self.LabelText = noSurname
        if name == "Name. (Optional)" and surname == "Surname. (Optional)":
            self.LabelText = BothMissing
        if name != "Name. (Optional)" and surname != "Surname. (Optional)":
            self.LabelText = BothCompiled.format(name, surname)

class SmartInsultsApp(App):
    def on_start(self):
        Window.size = (400, 600)

    def build(self):
        return MainLayout()

if __name__ == '__main__':
    SmartInsultsApp().run()
    Builder.load_file('SmartInsults.kv')
