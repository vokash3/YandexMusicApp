# YandexMusicApp (Unofficial)

___
_Linux_
![screen_linux](resources/static/screens/screen_linux.png)

_macOS_
![screen_mac](resources/static/screens/screen_mac.png)

## О проекте

Обычное приложение на Python 3, использующее PyWebEngine и PyQt5 для открытия веб
версии [Яндекс Музыки](https://music.yandex.ru/).

Создавал для себя, так как официальных версий Яндекс Музыки для macOS и Linux нет, а публичное API так и не было
предоставлено.

Зачастую не совсем удобно в рабочем профиле браузера открывать дополнительные вкладки с личным
аккаунтом для прослушивания треков из Яндекс Музыки. Это приложение решает такую проблему.

# Подготовка к сборке

**_ПРЕДУПРЕЖДЕНИЕ_**

_Все команды желательно выполнять в терминале (не в терминалах IDE!), чтобы избежать проблем с зависимостями!_

Требуется наличие **[Python3](https://www.python.org/)** в системе и инструментов разработчика (GCC, XCode CommandLine
Tools и т.п.)

Сборка и работоспособность протестированы:

- на macOS Sonoma 14.1.1 arm64 (Apple Silicon), Python
  3.11.0, [Homebrew 4.1.20](https://brew.sh/), [CLTools 14.3.1](https://developer.apple.com/download/all/?q=Command%20Line%20Tools)
- на Linux Mint 21.2 x86_64, Python 3.10.12, [GCC 11.4.0](https://losst.pro/ustanovka-gcc-v-ubuntu-16-04)

## Загрузка проекта

1) Скачать проект или выполнить клонирование (должен быть установлен git):
    ```bash
    git clone https://github.com/vokash3/YandexMusicApp.git
    ```
2) Перейти в директорию с проектом и выполнить установку зависимостей:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
3) Остаться в директории с проектом YandexMusicApp.

___

## Сборка для MacOS

**ДВА ВАРИАНТА**

### 1. Сборка через [py2app](https://github.com/ronaldoussoren/py2app/)

**_Особенность: приложение можно будет добавить в Программы_**

- Установить py2app:
    ```bash
    python3 -m pip install py2app
    ```

- **(Дополнительно) Если НЕТ** setup.py в директории проекта, выполнить его генерацию:
    ```bash
    py2applet --make-setup YandexMusicApp
    ```
- Выполнить сборку app пакета:
  ```bash
  python3 setup.py py2app --dist-dir=YandexMusicAppBuild
  ```

будет создан привычный YandexMusicApp.app пакет в поддиректории YandexMusicAppBuild этого проекта, который можно
переместить в Программы и запускать из Launchpad.

### 2. Сборка через [Nuitka](https://github.com/Nuitka/Nuitka)

- Выполнить сборку исполняемого bin файла:

    ```bash
    python3 -m nuitka --enable-plugin=pyqt5 --macos-create-app-bundle --macos-app-icon=icon.icns --output-dir=YandexMusicAppBuild YandexMusicApp.py
    ```

будет создан исполняемый YandexMusicApp файл в поддиректории YandexMusicAppBuild этого проекта.

___

## Сборка для Ubuntu и подобных

**ОДИН ВАРИАНТ**

### Сборка через [Nuitka](https://github.com/Nuitka/Nuitka)

- Установить инструменты разработки через apt (apt-get):
    ```bash
    sudo apt install build-essential
    ```
    ```bash
    sudo apt install python3.10-dev
    ```

- Выполнить установку дополнительного пакета через apt (apt-get) (актуально на Ubuntu):
    ```bash
    sudo apt-get install python3-pyqt5.qtwebengine
    ```

- Выполнить сборку исполняемого bin файла:

    ```bash
    python3 -m nuitka --enable-plugin=pyqt5 --linux-icon=icon.png --output-dir=YandexMusicAppBuild YandexMusicApp.py
    ```

будет создан исполняемый YandexMusicApp.bin файл в поддиректории YandexMusicAppBuild этого проекта.

___

# На этом всё 😉

___
___

### Дополнительно

#### Универсальный вариант (для linux и mac) через [pyinstaller](https://github.com/pyinstaller/pyinstaller)

_Этот способ не советую. Программа может не запуститься. Оставляю этот вариант для справки._

- Выполнить установку pyinstaller через pip:
    ```bash
    python3 -m pip install pyinstaller
    ```
- Запустить сборку проекта:
    ```bash
    pyinstaller --onefile YandexMusicApp.py
    ```

будет создан исполняемый YandexMusicApp файл в поддиректории dist этого проекта.

*
    * На macOS можно создать и app пакет:

      ```bash
      pyinstaller --noconsole -i icon.icns YandexMusicApp.py
      ```

___

#### Запуск через интерпретатор Python

- Просто запустить через python интерпретатор:
    ```bash
    python3 YandexMusicApp.py
    ```
