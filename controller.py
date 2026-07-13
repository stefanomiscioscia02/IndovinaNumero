from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def reset(self, e):
        self._model.reset() #resetto lo stato del gioco lato modello
        self._view._txtT.value = self._model.T
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(
            ft.Text("Inzia il gioco! Indovina a quale numero sto pensando.")
        )
        self._view.update()

    def play(self, e):
        pass

    def getNmax(self):
        return self._model.Nmax

    def getTmax(self):
        return self._model.Tmax

    def getTentativi(self):
        return self._model.T


