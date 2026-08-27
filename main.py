import sys
from pathlib import Path
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Gdk, Adw

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        # Create a Builder
        builder = Gtk.Builder()
        builder.add_from_file(str(Path(__file__).with_name("lionhead2048.ui")))

        # Obtain the button widget and connect it to a function
        button = builder.get_object("button1")
        button.connect("clicked", self.hello)

        btnUp = builder.get_object("btnUp")
        btnUp.connect("clicked", self.up)

        btnDown = builder.get_object("btnDown")
        btnDown.connect("clicked", self.down)

        btnLeft = builder.get_object("btnLeft")
        btnLeft.connect("clicked", self.left)

        btnRight = builder.get_object("btnRight")
        btnRight.connect("clicked", self.right)

        # Keys
        window = builder.get_object("main_window")
        event_controller = Gtk.EventControllerKey()
        event_controller.connect("key-pressed", self.event_key_pressed_cb)
        # event_controller.connect("key-released", self.event_key_released_cb)
        window.add_controller(event_controller)

        # Obtain and show the main window
        self.win = builder.get_object("main_window")
        self.win.set_application(self)  # Application will close once it no longer has active windows attached to it
        self.win.present()

    def hello(self, button):
        print("World has now been changed!!!")

    def left(self, button):
        print("Left")

    def right(self, button):
        print("Right")

    def up(self, button):
        print("Up")

    def down(self, button):
        print("Down")

    def event_key_pressed_cb (self, event_controller, keyval, keycode, state):
        #print(f"Key pressed: {keyval} {keycode}")
        match keyval:
            case Gdk.KEY_Up:
                print("Up")
            case Gdk.KEY_Left:
                print("Left")
            case Gdk.KEY_Right:
                print("Right")
            case Gdk.KEY_Down:
                print("Down")

    # def event_key_released_cb (self, event_controller, keyval, keycode, state):
    #     print("Key released")

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
