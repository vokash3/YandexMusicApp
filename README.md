# YandexMusicApp (WebView Unofficial)

<img src="//yastatic.net/s3/home/services/pinned/music_new.2.png" width="100" height="100">

## О проекте

Обычное приложение на Python 3, использующее PyWebEngine и PyQT5 для открытия веб версии Яндекс Музыки.
Создавал для себя, так как десктопных программ Я.Музыки для macOS и Linux нет, публичное API так и не было предоставлено, а зачастую не совсем удобно в рабочем профиле браузера открывать дополнительные вкладки с личным аккаунтом.
# Подготовка к установке

**_ПРЕДУПРЕЖДЕНИЕ_**

_Все команды желательно выполнять в терминале (не в терминалах IDE!), чтобы избежать проблем с зависимостями!_

Требуется наличие **[Python3](https://www.python.org/)** в системе и инструментов разработчика (gcc, XCode CommandLine Tools)

Сборка и работоспособность протестированы:
- на macOS Sonoma 14.1.1 arm64 (Apple Silicon), Python 3.11.0, [Homebrew 4.1.20, CLTools 14.3.1.0.1...](https://brew.sh/)
- на Linux Mint 21.2 x86_64, Python 3.10.12, [GCC 11.4.0](https://losst.pro/ustanovka-gcc-v-ubuntu-16-04)

## Подготовка

1) Выполнить клонирование этого проекта (должен быть установлен git):
    ```bash
    git clone https://github.com/vokash3/YandexMusicApp
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
    python3 -m nuitka --enable-plugin=pyqt5 --output-dir=YandexMusicAppBuild YandexMusicApp.py
    ```

будет создан исполняемый YandexMusicApp.bin файл в поддиректории YandexMusicAppBuild этого проекта.

___

## Сборка для Ubuntu и подобных

**ОДИН ВАРИАНТ**

### Сборка через [Nuitka](https://github.com/Nuitka/Nuitka)

- Выполнить установку дополнительного пакета через apt (apt-get) (актуально на Ubuntu):
    ```bash
    sudo apt-get install python3-pyqt5.qtwebengine
    ```

- Выполнить сборку исполняемого bin файла:

    ```bash
    python3 -m nuitka --enable-plugin=pyqt5 --output-dir=YandexMusicAppBuild YandexMusicApp.py
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