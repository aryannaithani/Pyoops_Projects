from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time
from filestack import Client
import webbrowser
import pyperclip

Builder.load_file('interface.kv')

class Webcam(Screen):

    def toggle_video(self):
        self.ids.camera.play = not self.ids.camera.play
        if self.ids.camera.play:
            self.ids.toggle_button.text = 'Stop Video'
        else:
            self.ids.toggle_button.text = 'Start Video'
            self.ids.camera.texture = None

    def capture_image(self):
        file_name = f'{time.strftime('%Y%m%d_%H%M%S')}.png'
        self.ids.camera.export_to_png(file_name)
        self.manager.current = 'file_operations'
        self.manager.current_screen.ids.img.source = file_name


class FileOperations(Screen):

    def create_link(self):
        client = Client('AxG9Oi03qTq6UJue2O5npz')
        link = client.upload(filepath=self.manager.current_screen.ids.img.source)
        self.manager.current_screen.ids.img_label.text = link.url
        return link.url

    def copy_to_clipboard(self):
        pyperclip.copy(self.create_link())

    def open_in_browser(self):
        webbrowser.open(self.create_link())


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
