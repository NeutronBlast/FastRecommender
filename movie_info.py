import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
import menu
import info_results
import similar_results


class Info(QDialog):
    def __init__(self):
        super(Info, self).__init__()
        uic.loadUi("gui/info.ui", self)
        self.back_button.mousePressEvent = self.back_to_main
        self.search_button.mousePressEvent = self.show_info_results

    def back_to_main(self, event):
        self.close()
        menu_page = menu.Menu()
        menu_page.show()

    def show_info_results(self, event):
        self.hide()
        show_info_result_page = info_results.InfoResult(self.title_textbox.toPlainText())
        show_info_result_page.exec_()