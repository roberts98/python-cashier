from Window import Window
from Cashier import Cashier

controller = Cashier()
view = Window(controller)
controller.setView(view)
view.start()