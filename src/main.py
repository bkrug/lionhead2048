import sys
from pathlib import Path
from typing import cast
import gi
import cairo
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Gdk, Adw  # pyright: ignore[reportMissingModuleSource]
from powers_of_two import TILE_COLORS

# gi.repository will never have a real *.py file for pylance to find.
# So I plan to add the above ignore statement, anywhere that I import gi.repository

SIZE = 30
Y_OFFSET = 15

class MyApp(Adw.Application):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app: Gtk.Application):
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
        window.add_controller(event_controller)

        # Draw
        self.drawing_area: Gtk.DrawingArea = cast(Gtk.DrawingArea, builder.get_object("drawArea"))
        self.drawing_area.set_draw_func(self.draw)

        # Obtain and show the main window
        self.win = builder.get_object("main_window")
        self.win.set_application(self)  # Application will close once it no longer has active windows attached to it
        self.win.present()

    def play_piece_size(self) -> int:
        return min(self.drawing_area.get_content_width(), self.drawing_area.get_content_height())

    def hello(self, button: Gtk.Button):
        print("World has now been changed!!!")

    def left(self, button: Gtk.Button):
        print("Left")

    def right(self, button: Gtk.Button):
        print("Right")

    def up(self, button: Gtk.Button):
        print("Up")

    def down(self, button: Gtk.Button):
        print("Down")

    def event_key_pressed_cb (self, event_controller: Gtk.EventControllerKey, keyval: int, keycode: int, state: Gdk.ModifierType):
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

    def text_msg(self, ctx: cairo.Context):
        #te = ctx.text_extents()
        ctx.select_font_face("Serif")
        ctx.set_font_size(14)
        ctx.move_to(0, Y_OFFSET*10)
        ctx.show_text("Abcdefg")

    def draw_number_box(self, ctx: cairo.Context, position_x: int, position_y: int, exponent: int):
        box_size = self.play_piece_size() / 4
        font_size = box_size / 4
                
        ctx.save()
        box_color = TILE_COLORS[exponent]
        ctx.set_source_rgb(box_color[0], box_color[1], box_color[2])
        ctx.rectangle(box_size * position_x, box_size * position_y, box_size, box_size)
        ctx.fill()
        ctx.restore()

        play_value = 2**exponent
        text_color: tuple[float, float, float] = (0.8, 0.8, 0.8)
        ctx.save()
        ctx.set_source_rgb(text_color[0], text_color[1], text_color[2])
        ctx.move_to(box_size * position_x + 2, box_size * position_y + (box_size * 0.6))
        ctx.set_font_size(font_size)
        ctx.show_text(f"{play_value}")
        ctx.restore()

    def draw(self, da: Gtk.DrawingArea, ctx: cairo.Context, width: int, height: int):
        ctx.set_line_width(SIZE / 4)
        ctx.set_tolerance(0.1)

        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
        ctx.set_dash([SIZE / 4.0, SIZE / 4.0], 0)

        self.draw_number_box(ctx, 0, 0, 1)
        self.draw_number_box(ctx, 1, 2, 2)
        self.draw_number_box(ctx, 3, 3, 8)


app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
