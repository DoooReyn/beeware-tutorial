"""
BMFont Toolbox
"""
import os
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def get_default_path():
    return os.path.abspath(os.path.join(os.environ.get("HOMEPATH"), "Pictures"))


def get_output_path():
    return os.path.abspath(os.path.join(os.environ.get("HOMEPATH"), "Documents"))


class BMFontToolbox(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.setup_ui()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def setup_ui(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.create_original_box()
        self.create_output_box()
        self.create_list_box()
        self.create_picture_list_box()
        self.create_output_list_box()

    def create_list_box(self):
        pass

    def create_picture_list_box(self):
        pass

    def create_output_list_box(self):
        pass

    def create_original_box(self):
        label = toga.Label(
            "选择图集目录",
            style=Pack(padding=(4, 4, 0, 4))
        )

        self.original_textfield = toga.TextInput(
            initial=get_default_path(),
            readonly=True,
            style=Pack(padding=(4, 4, 0, 4), flex=1)
        )

        self.original_button = toga.Button(
            "打开",
            style=Pack(padding=(4, 4, 4, 0)),
            on_press=self.on_select_texture_dir
        )

        box = toga.Box(style=Pack(direction=ROW))
        box.add(label)
        box.add(self.original_textfield)
        box.add(self.original_button)
        self.main_box.add(box)

    def create_output_box(self):
        label = toga.Label(
            "选择输出目录",
            style=Pack(padding=(4, 4, 0, 4))
        )

        self.output_textfield = toga.TextInput(
            initial=get_output_path(),
            readonly=True,
            style=Pack(padding=(4, 4, 0, 4), flex=1)
        )

        self.output_button = toga.Button(
            "打开",
            style=Pack(padding=(4, 4, 4, 0)),
            on_press=self.on_select_output_dir
        )

        box = toga.Box(style=Pack(direction=ROW))
        box.add(label)
        box.add(self.output_textfield)
        box.add(self.output_button)
        self.main_box.add(box)

    def on_select_texture_dir(self, widget):
        try:
            where = get_default_path()
            folder = self.main_window.select_folder_dialog(
                title="选择图集目录",
                initial_directory=where,
                multiselect=False
            )
            if folder and len(folder) > 0:
                self.original_textfield.value = folder[0]
        except ValueError:
            pass

    def on_select_output_dir(self, widget):
        try:
            where = get_output_path()
            folder = self.main_window.select_folder_dialog(
                title="选择输出目录",
                initial_directory=where,
                multiselect=False
            )
            if folder and len(folder) > 0:
                self.output_textfield.value = folder[0]
        except ValueError:
            pass


def main():
    return BMFontToolbox()
