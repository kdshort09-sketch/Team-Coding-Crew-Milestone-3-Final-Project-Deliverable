# Changes from original version:
# - Added function to change Daily Recipe to random recipe on startup, used in .kv file
# - Added function to save recipes in .json file, used in .kv file
# - Added comments to .kv and .py files
#
# P.S. - Sorry this took so long, needed to upgrade my laptop after the D key broke.

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivy.storage.jsonstore import JsonStore
import random

store = JsonStore("Recipes.json")

Window.size = (400, 700)

# SCREEN classes

class LoginScreen(MDScreen):
    def login_user(self):
        username = self.ids.username.text
        password = self.ids.password.text
        if username and password:
            self.manager.current = "dashboard"

class DashboardScreen(MDScreen):
    # Chooses a random recipe from Recipes.json. If there aren't any, it lists the placeholder text.
    # Chosen recipe persists until the app is reloaded.
    def dayRecipe(self):
        all_recipes = list(store.keys())
        if not all_recipes:
            return ("Title of Recipe\nDescription...")
        else:
            daily_recipe = random.choice(all_recipes)
            daily_recipe_steps = store.get(daily_recipe)
            return (f"{daily_recipe}\n{daily_recipe_steps['dish_steps']}")
            # You need to do this wack workaround to get the newline (\n) to work:
            # recipe = store.get(recipe name)
            # print(recipe['dish_steps'])
            #
            # recipe name should be retrieved through external means, mainly using store.keys()
    pass

class RecipesScreen(MDScreen):
    # TODO:
    # Add function/kivy stuff to list saved recipes. Actually viewing the recipes is outside current scope.
    # Maybe via popup/modal?
    pass

class PantryScreen(MDScreen):
    pass

class SettingsScreen(MDScreen):
    pass

class AddRecipeScreen(MDScreen):
    # The big difference. To prevent recipes from replacing each other, the name of each recipe is the index key.
    # Somewhat unintuitive, but it functions, and doesn't override already saved recipes.
    def saveRecipe(self):
        store.put(self.ids.recipe_title.text , dish_steps = self.ids.recipe_steps.text)
        print("Saving Recipe")

    # A method to adding pantry ingredients to recipes and linking them together should be done.
    # Maybe a popup to add ingredients to a separate database?

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
