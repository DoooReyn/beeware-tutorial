"""
BMFont Toolbox
"""
import os
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def get_default_path():
    return os.path.abspath(os.path.join(os.environ.get("HOMEPATH"), "Pictures"))


class BMFontToolbox(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        textfield = toga.TextInput(
            initial=get_default_path(),
            placeholder="Choose pictures folder",
            readonly=True,
            style=Pack(padding=(4, 4, 0, 4), flex=1)
        )
        button = toga.Button(
            "Choose",
            style=Pack(padding=(4, 4, 4, 0)),
            on_press=self.on_select_texture_dir
        )
        box = toga.Box(style=Pack(direction=ROW))
        box.add(textfield)
        box.add(button)

        main_box.add(box)

        self.textfield = textfield
        self.folder_button = button

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def on_select_texture_dir(self, widget):
        try:
            where = get_default_path()
            folder = self.main_window.select_folder_dialog(
                title="Choose pictures folder",
                initial_directory=where,
                multiselect=False)
            if folder and len(folder) > 0:
                self.textfield.value = folder[0]
            print(folder)
        except ValueError as e:
            print(e)


def main():
    return BMFontToolbox()
