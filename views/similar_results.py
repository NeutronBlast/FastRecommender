from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon
from recommender import extract_movie_titles, get_movies_from_tastedive
from views import similar_movies


class SimilarResult(QDialog):
    def __init__(self, title, limit):
        super(SimilarResult, self).__init__()
        uic.loadUi("gui/similar_results.ui", self)
        self.setWindowTitle('FastRecommender | '+title)
        self.setWindowIcon(QIcon('./gui/design/movie.png'))
        self.title.setText('Similar movies to: '+title)
        self.back_button.mousePressEvent = self.back_to_form
        self.set_list(title, int(limit))

    def back_to_form(self, event):
        self.close()
        similar_movies_page = similar_movies.Similar()
        similar_movies_page.exec_()

    def set_list(self, title, limit):
        titles = extract_movie_titles(get_movies_from_tastedive(title, limit)['Similar']['Results'])

        # Add items to the list
        for item in titles:
            self.movie_list.addItem(item)

