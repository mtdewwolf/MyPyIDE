# ui/main_window.py

from PyQt5.QtWidgets import (
    QMainWindow, QMenuBar, QMenu, QAction, QFileDialog, QStatusBar, QMessageBox
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from ui.editor import CodeEditor
from core.settings import SettingsManager
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize Settings Manager
        self.settings = SettingsManager()

        # Initialize the UI
        self.init_ui()

    def init_ui(self):
        # Set window properties
        self.setWindowTitle('MyPyIDE')
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon('resources/icons/app_icon.png'))

        # Initialize components
        self.editor = CodeEditor()
        self.setCentralWidget(self.editor)
        self.current_file = None

        # Initialize menu, status bar, and docks
        self.init_menu()
        self.init_status_bar()
        self.init_dock_widgets()

    def init_menu(self):
        menubar = self.menuBar()

        # File Menu
        file_menu = menubar.addMenu('File')

        # New File Action
        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        # Open File Action
        open_action = QAction('Open...', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Save File Action
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        # Save As Action
        save_as_action = QAction('Save As...', self)
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(save_as_action)

        # Exit Action
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Edit Menu (Placeholder for future actions)
        edit_menu = menubar.addMenu('Edit')

        # View Menu (Placeholder for future actions)
        view_menu = menubar.addMenu('View')

        # Help Menu
        help_menu = menubar.addMenu('Help')
        about_action = QAction('About', self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def init_status_bar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('Ready')

    def init_dock_widgets(self):
        # Placeholder for future dock widgets (e.g., Project Explorer)
        pass

    def new_file(self):
        # Check for unsaved changes
        if self.maybe_save():
            self.editor.clear()
            self.current_file = None
            self.status_bar.showMessage('New file created')

    def open_file(self):
        if self.maybe_save():
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(
                self, 'Open File', '', 'Python Files (*.py);;All Files (*)', options=options
            )
            if file_name:
                try:
                    with open(file_name, 'r', encoding='utf-8') as file:
                        content = file.read()
                    self.editor.setText(content)
                    self.current_file = file_name
                    self.status_bar.showMessage(f'Opened file: {os.path.basename(file_name)}')
                except Exception as e:
                    QMessageBox.warning(self, 'Error', f'Could not open file: {e}')

    def save_file(self):
        if self.current_file:
            return self._save_to_path(self.current_file)
        else:
            return self.save_file_as()

    def save_file_as(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, 'Save File As', '', 'Python Files (*.py);;All Files (*)', options=options
        )
        if file_name:
            return self._save_to_path(file_name)
        return False

    def _save_to_path(self, path):
        try:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(self.editor.text())
            self.current_file = path
            self.status_bar.showMessage(f'Saved file: {os.path.basename(path)}')
            return True
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Could not save file: {e}')
            return False

    def maybe_save(self):
        if self.editor.isModified():
            ret = QMessageBox.warning(
                self, 'Unsaved Changes',
                'The document has been modified.\nDo you want to save your changes?',
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
            )
            if ret == QMessageBox.Save:
                return self.save_file()
            elif ret == QMessageBox.Cancel:
                return False
        return True

    def closeEvent(self, event):
        if self.maybe_save():
            event.accept()
        else:
            event.ignore()

    def about(self):
        QMessageBox.about(
            self, 'About MyPyIDE',
            '<b>MyPyIDE</b> is a Python IDE built with PyQt.'
        )
