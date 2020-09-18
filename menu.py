import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import similar_movies
import similar_results


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu.ui", self)
        # Define button events
        self.option_1.mousePressEvent = self.movies_by_title
        self.l_option_1.mousePressEvent = self.movies_by_title
        #self.option_2.mousePressEvent = self.test

    # Methods to call on icon click
    def movies_by_title(self, event):
        self.close()
        similar_movies_page = similar_movies.Similar()
        similar_movies_page.exec_()


    #def test(self, event):
    #    self.close()
    #    show_similar_results_page = similar_results.SimilarResults()
    #    show_similar_results_page.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Menu()
    GUI.show()
    app.exec_()
