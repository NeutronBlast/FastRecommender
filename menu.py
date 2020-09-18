import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import similar_movies
import movie_info
import movie_list


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu.ui", self)
        # Define button events
        self.option_1.mousePressEvent = self.movies_by_title
        self.l_option_1.mousePressEvent = self.movies_by_title
        self.option_2.mousePressEvent = self.movie_info
        self.l_option_2.mousePressEvent = self.movie_info
        self.option_3.mousePressEvent = self.movie_list
        self.l_option_3.mousePressEvent = self.movie_list
        self.exit.mousePressEvent = self.exit_program

    # Methods to call on icon click
    def movies_by_title(self, event):
        self.close()
        similar_movies_page = similar_movies.Similar()
        similar_movies_page.exec_()

    def movie_info(self, event):
        self.close()
        show_info_form = movie_info.Info()
        show_info_form.exec_()

    def movie_list(self, event):
        self.close()
        show_movie_list_form = movie_list.MovieList()
        show_movie_list_form.exec_()

    def exit_program(self, event):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Menu()
    GUI.show()
    app.exec_()
