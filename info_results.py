import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QImage, QPixmap
from recommender import get_movie_data, get_movie_rating
import movie_info
import requests

class InfoResult(QDialog):
    def __init__(self, title):
        super(InfoResult, self).__init__()
        uic.loadUi("gui/info_results.ui", self)
        self.title.setText('About '+title)
        self.back_button.mousePressEvent = self.back_to_form

        # Get info
        info = get_movie_data(title)

        # Fill
        self.genre.setText("Genre: "+info['Genre'])
        self.year.setText("Year: "+info['Year'])
        self.rating.setText("Rating: "+str(get_movie_rating(info)))
        self.plot.setWordWrap(True)
        self.plot.setText("Plot: "+info['Plot'])
        url = info['Poster']

        image = QImage()
        image.loadFromData(requests.get(url).content)

        self.poster.setPixmap(QPixmap(image))


    def back_to_form(self, event):
        self.close()
        info_form_page = movie_info.Info()
        info_form_page.exec_()