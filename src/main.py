import sys
from pathlib import Path
from typing import cast
import gi
import cairo
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Gdk, Adw  # pyright: ignore[reportMissingModuleSource]
from powers_of_two import TILE_COLORS
from board2048 import Board2048, BOARD_SIZE
from piece_maker import PieceMaker

# gi.repository will never have a real *.py file for pylance to find.
# So I plan to add the above ignore statement, anywhere that I import gi.repository

SIZE = 30
Y_OFFSET = 15

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)
        piece_maker = PieceMaker()
        self.game_board = Board2048(piece_maker)

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
        return min(self.drawing_area.get_content_width(), self.drawing_area.get_content_height()) / 4

    def hello(self, button: Gtk.Button):
        print("World has now been changed!!!")

    def left(self, button: Gtk.Button):
        self.game_board.move_left()
        self.drawing_area.queue_draw()

    def right(self, button: Gtk.Button):
        self.game_board.move_right()
        self.drawing_area.queue_draw()

    def up(self, button: Gtk.Button):
        self.game_board.move_up()
        self.drawing_area.queue_draw()

    def down(self, button: Gtk.Button):
        self.game_board.move_down()
        self.drawing_area.queue_draw()

    def event_key_pressed_cb (self, event_controller: Gtk.EventControllerKey, keyval: int, keycode: int, state: Gdk.ModifierType):
        #print(f"Key pressed: {keyval} {keycode}")
        match keyval:
            case Gdk.KEY_Up:
                self.game_board.move_up()
            case Gdk.KEY_Left:
                self.game_board.move_left()
            case Gdk.KEY_Right:
                self.game_board.move_right()
            case Gdk.KEY_Down:
                self.game_board.move_down()
            case _:
                return
        self.drawing_area.queue_draw()

    def draw_play_piece(self, ctx: cairo.Context, position_x: int, position_y: int, exponent: int):
        box_size = self.play_piece_size()
        font_size = box_size / 4
                
        ctx.save()
        box_color = TILE_COLORS[exponent]
        ctx.set_source_rgb(box_color[0], box_color[1], box_color[2])
        ctx.rectangle(box_size * position_x, box_size * position_y, box_size, box_size)
        ctx.fill()
        ctx.restore()

        if exponent==0:
            return

        play_value = 2**exponent
        text_color: tuple[float, float, float] = (0.8, 0.8, 0.8)
        ctx.save()
        ctx.set_source_rgb(text_color[0], text_color[1], text_color[2])
        ctx.move_to(box_size * position_x + 2, box_size * position_y + (box_size * 0.6))
        ctx.set_font_size(font_size)
        ctx.show_text(f"{play_value}")
        ctx.restore()

    def draw(self, da: Gtk.DrawingArea, ctx: cairo.Context, width: int, height: int):
        powers = self.game_board.get_powers()
        for row in powers:
            print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
        print(f"")

        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                self.draw_play_piece(ctx, c, r, powers[r][c])


app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
