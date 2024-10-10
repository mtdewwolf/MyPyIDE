# main.py

import sys
import traceback
from PyQt5.QtWidgets import QApplication, QMessageBox
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Global exception handler
    def handle_exception(exc_type, exc_value, exc_traceback):
        error_message = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        # Log the error to a file (implement logging if necessary)
        print(error_message)

        # Show error message to the user
        QMessageBox.critical(
            window,
            'An unexpected error occurred',
            'An unexpected error occurred. Please check the logs for more details.'
        )
        # Optionally, you can exit the application or continue running

    # Install the exception hook
    sys.excepthook = handle_exception

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
