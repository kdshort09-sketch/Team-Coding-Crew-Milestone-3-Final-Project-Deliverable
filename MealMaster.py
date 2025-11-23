from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem

Window.size = (400, 700)


# SCREEN classes

class LoginScreen(MDScreen):
    def login_user(self):
        username = self.ids.username.text
        password = self.ids.password.text
        if username and password:
            self.manager.current = "dashboard"

class DashboardScreen(MDScreen):
    pass

class RecipesScreen(MDScreen):
    pass

class PantryScreen(MDScreen):
    pass

class SettingsScreen(MDScreen):
    pass

class AddRecipeScreen(MDScreen):
    pass


# MAIN
class MealMasterApp(MDApp):
    dialog = None

    def build(self):
        self.title = "MealMaster"
        return Builder.load_file("MealMasterLayout.kv")

    
    # LANGUAGE BUTTON
    
    def show_language_popup(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Select Language",
                type="simple",
                items=[
                    OneLineListItem(text="English", on_release=lambda x: self.set_language("English")),
                    OneLineListItem(text="Spanish", on_release=lambda x: self.set_language("Spanish")),
                    OneLineListItem(text="French", on_release=lambda x: self.set_language("French")),
                ],
            )
        self.dialog.open()

    def set_language(self, lang):
        print(f"Language selected: {lang}")
        self.dialog.dismiss()
        self.dialog = None

    
    # NOTIFICATION TOGGLE
    
    def toggle_notifications(self, value):
        if value:
            print("Notifications Enabled")
        else:
            print("Notifications Disabled")


if __name__ == "__main__":
    MealMasterApp().run()
