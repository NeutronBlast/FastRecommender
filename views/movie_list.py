from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from views import movie_list_results
import menu


class MovieList(QDialog):
    def __init__(self):
        super(MovieList, self).__init__()
        uic.loadUi("gui/titles.ui", self)
        self.back_button.mousePressEvent = self.back_to_main
        self.search_button.mousePressEvent = self.show_movie_list

    def back_to_main(self, event):
        self.close()
        menu_page = menu.Menu()
        menu_page.show()

    def show_movie_list(self, event):
        self.hide()
        show_sorted_page = movie_list_results.SortedList(self.title_textbox.toPlainText())
        show_sorted_page.exec_()