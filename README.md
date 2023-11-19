## Установка через py2app

- Если нет setup.py
    ```bash
    py2applet --make-setup YandexMusicApp
    ```
- Выполнить сборку app
    ```bash
    python3.11 setup.py py2app -A
    ```

## MacOS

### Nuitka

```bash
 python3.11 -m nuitka --macos-create-app-bundle --macos-app-icon=logo.png --standalone --onefile --enable-plugin=pyqt5 --output-dir=YandexMusicAppBuild YandexMusicApp.py
```

### py2app

```bash
python3.11 setup.py py2app --dist-dir=YandexMusicAppBuild
```