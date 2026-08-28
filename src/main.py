import sys
from pathlib import Path
import gi
import cairo
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Gdk, Adw  # pyright: ignore[reportMissingModuleSource]

# gi.repository will never have a real *.py file for pylance to find.
# So I plan to add the above ignore statement, anywhere that I import gi.repository

SIZE = 30
Y_OFFSET = 15

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

        # Draw
        drawing_area = builder.get_object("drawArea")
        drawing_area.set_draw_func(self.draw)

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

    def event_key_pressed_cb (self, event_controller, keyval: int, keycode: int, state):
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

    def manual_square(self, ctx: cairo.Context):
        ctx.save()
        ctx.move_to(0, Y_OFFSET)
        ctx.rel_line_to(2 * SIZE, 0)
        ctx.rel_line_to(0, 2 * SIZE)
        ctx.rel_line_to(-2 * SIZE, 0)
        ctx.close_path()
        ctx.fill()
        ctx.restore()

    def square(self, ctx: cairo.Context):
        ctx.save()
        ctx.rectangle(SIZE * 1.5, Y_OFFSET + 10, SIZE, SIZE)
        ctx.close_path()
        ctx.fill()
        ctx.restore()

    def draw(self, da: Gtk.DrawingArea, ctx: cairo.Context, width: int, height: int):
        print(f"Width: {width}, Height: {height}")

        ctx.set_source_rgb(120, 120, 0)

        ctx.set_line_width(SIZE / 4)
        ctx.set_tolerance(0.1)

        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
        ctx.set_dash([SIZE / 4.0, SIZE / 4.0], 0)

        self.manual_square(ctx)

        ctx.set_source_rgb(0, 120, 120)
        self.square(ctx)


app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
