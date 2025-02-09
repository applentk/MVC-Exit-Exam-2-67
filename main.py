from Controller.Controller import Controller
from View.View import View

controller = Controller()
view = View(controller)

is_running = True

while is_running:
    view.clear_output_screen()

    view.read_new_animal()
    view.display_stats()

    is_running = view.check_continue()