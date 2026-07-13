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
        tentativoStr =  self._view._txtInTentativo.value
        try:
            tentativo = int(tentativoStr)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Errore, devi inserire un valore numerico"))
            return
        res = self._model.play(tentativo)
        if res == 0:
            """Ho vinto"""
            self._view._lvOut.controls.append(ft.Text(f"Ha vinto! Il numero corretto era: {tentativo}",
                                                  color="green"))
            self._view.update()
            return

        elif res == 2:
            """Non hai più vite per giocare. Vuoi iniziare una nuova partita?"""
            self._view._lvOut.controls.append(ft.Text(f"Ha perso! Il numero corretto era: {self._model.segreto}",
                                                      color="red"))
            self._view.update()
            return

        elif res == 1:
            """Il tentativo è più grande del valore """
            self._view._lvOut.controls.append(ft.Text(f"Hai perso una vita, Ritenta! Il numero che hai inserito è più grande di quello segreto"))
            self._view.update()
            return

        else:
            """Il tentativo è più piccolo del valore """
            self._view._lvOut.controls.append(ft.Text(f"Hai perso una vita, Ritenta! Il numero che hai inserito è più piccolo di quello segreto"))
            self._view.update()
            return


    def getNmax(self):
        return self._model.Nmax

    def getTmax(self):
        return self._model.Tmax

    def getTentativi(self):
        return self._model.T


