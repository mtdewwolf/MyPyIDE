# core/settings.py

from PyQt5.QtCore import QSettings

class SettingsManager:
    def __init__(self):
        self.settings = QSettings('MyCompany', 'MyPyIDE')

    def set_value(self, key, value):
        self.settings.setValue(key, value)

    def get_value(self, key, default=None):
        return self.settings.value(key, default)
