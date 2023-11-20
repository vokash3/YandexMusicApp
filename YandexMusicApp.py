import sys

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

login_url = 'https://passport.yandex.ru/auth?origin=music_button-header&retpath=https%3A%2F%2Fmusic.yandex.ru%2Fsettings%3Freqid%3D6724833517003451817471583178390582%26from-passport'
radio_url = 'https://music.yandex.ru/home'


class YandexMusicApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(radio_url))

        self.setCentralWidget(self.browser)
        self.setMinimumSize(768, 768)
        self.show()

        # Настройка меню
        navbar = QToolBar()
        self.addToolBar(navbar)

        actions = [
            ('Назад', self.browser.back),
            ('Вперёд', self.browser.forward),
            ('Обновить', self.browser.reload),
            ('Логин', self.navigate_login),
            ('Моя волна', self.navigate_radio),
        ]

        for text, slot in actions:
            action = QAction(text, self)
            action.triggered.connect(slot)
            navbar.addAction(action)

        navbar.addAction(self.create_info_button())

    def navigate_login(self):
        self.browser.setUrl(QUrl(login_url))

    def navigate_radio(self):
        self.browser.setUrl(QUrl(radio_url))

    def create_info_button(self) -> QAction:
        info_btn = QAction('Информация', self)
        info_btn.triggered.connect(self.show_info_dialog)
        return info_btn

    def show_info_dialog(self):
        info_dialog = InfoDialog(self)
        info_dialog.exec()


class InfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        data_path = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation)
        cache_path = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.CacheLocation)

        self.setWindowTitle("Информация")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        info_label = QLabel(f'<b>WebEngine хранит данные и кэш</b>:')
        data_label = QLabel(f'<u>Данные</u>: {data_path}')
        cache_label = QLabel(f'<u>Кэш</u>: {cache_path}')
        github_label = QLabel('<a href="https://github.com/vokash3/YandexMusicApp">GitHub проекта</a>')
        github_label.setOpenExternalLinks(True)

        layout.addWidget(info_label)
        layout.addWidget(data_label)
        layout.addWidget(cache_label)
        layout.addWidget(github_label)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

        self.setLayout(layout)

        data_path = None
        cache_path = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName("YandexMusicApp")
    window = YandexMusicApp()
    sys.exit(app.exec())
