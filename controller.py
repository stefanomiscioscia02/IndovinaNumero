from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNmax(self):
        self._model.Nmax

    def getTmax(self):
        self._model.Tmax

    def getTentativi(self):
        self._model.T
