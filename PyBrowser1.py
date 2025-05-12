import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QStatusBar
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.navigation_bar = QToolBar('Navigation Toolbar')
        self.addToolBar(self.navigation_bar)

        back_button = QAction("Back", self)
        back_button.triggered.connect(self.browser.back)
        self.navigation_bar.addAction(back_button)

        refresh_button = QAction("Refresh", self)
        refresh_button.triggered.connect(self.browser.reload)
        self.navigation_bar.addAction(refresh_button)

        next_button = QAction("Next", self)
        next_button.triggered.connect(self.browser.forward)
        self.navigation_bar.addAction(next_button)

        home_button = QAction("Home", self)
        home_button.triggered.connect(self.go_to_home)
        self.navigation_bar.addAction(home_button)

        self.URLBar = QLineEdit()
        self.URLBar.returnPressed.connect(lambda: self.go_to_URL(QUrl(self.URLBar.text())))
        self.navigation_bar.addWidget(self.URLBar)

        self.show()

    def go_to_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    def go_to_URL(self, url: QUrl):
        if url.scheme() == '':
            url.setScheme('https://')
        self.browser.setUrl(url)

app = QApplication(sys.argv)
window = Window()
app.exec_()
