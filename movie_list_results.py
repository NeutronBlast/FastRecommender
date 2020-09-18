import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from recommender import get_sorted_recommendations
import movie_list


class SortedList(QDialog):
    def __init__(self, title):
        super(SortedList, self).__init__()
        uic.loadUi("gui/titles_results.ui", self)
        self.back_button.mousePressEvent = self.back_to_form
        unsorted_list = title.strip().split(',')
        sorted_list = get_sorted_recommendations(unsorted_list)

        self.tableWidget.setRowCount(len(sorted_list))
        for index, row in enumerate(sorted_list):
            self.tableWidget.setItem(index, 0, QTableWidgetItem(row['title']))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(row['rating'])))

    def back_to_form(self, event):
        self.close()
        list_form_page = movie_list.MovieList()
        list_form_page.exec_()
