# lionhead2048
Python and GTK4 practice by implementing the game 2048.

A version of 2048 that lets you think about either lions or rabbits depending on your preference.

## Packages

In order to install packages, it is better to run `scripts/boostrap` then `pipenv install`.

### About venv

I ran this command in case I want to use venv later.
```
pipenv install --site-packages
```

## Documentation

- Python Wrapper Tutorial: https://pygobject.gnome.org/tutorials/index.html
- Draw Are Tutorial: https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.DrawingArea.html
- API Reference: https://gnome.pages.gitlab.gnome.org/gtk/gtk4/index.html

## Intellisense

As a self reminder, if you want to enable python intellisense, you need
- a "python-envs.defaultEnvManager" entry in .vscode/settings.json.
- type "pipenv --venv" in a terminal to see a venv path, and type "Python: Select Interpreter" in the command palette to select that same path.

## Possible Improvements

- Display a label on the left-hand side when the user reaches 2048 or any higher number.
- When we use arrow keys on the keyboard, prevent buttons in the desktop form from being highlighted.
- React to Desktop Environment changes between light and dark mode. Change the piece colors accordingly.
- Clean up the UI a bit. Make the arrow buttons smaller. Add some boarders between the game field and the buttons.
- Add an "Are You Sure?" question before creating a new game.
- Add animation when the pieces move