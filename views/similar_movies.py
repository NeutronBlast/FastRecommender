from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from views import menu, similar_results
import search_params


class Similar(QDialog):
    def __init__(self):
        super(Similar, self).__init__()
        uic.loadUi("gui/similar.ui", self)
        self.back_button.mousePressEvent = self.back_to_main
        self.search_button.mousePressEvent = self.show_similar_results
        self.error_limit.setHidden(True)

    def back_to_main(self, event):
        self.close()
        menu_page = menu.Menu()
        menu_page.show()

    def show_similar_results(self, event):
        # Validate limit input
        params = search_params.Parameter(self.title_textbox.toPlainText(), self.limit_textbox.toPlainText())
        if params.limit_int():
            self.hide()
            show_similar_results_page = similar_results.SimilarResult(self.title_textbox.toPlainText(),
                                                                      self.limit_textbox.toPlainText())
            show_similar_results_page.exec_()
        else:
            self.error_limit.setHidden(False)
