# ui/editor.py

from PyQt5.Qsci import QsciScintilla, QsciLexerPython
from PyQt5.QtGui import QFont

class CodeEditor(QsciScintilla):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_editor()

    def init_editor(self):
        # Set the font
        font = QFont('Consolas', 12)
        self.setFont(font)
        self.setMarginsFont(font)

        # Line numbers
        self.setMarginsFont(font)
        self.setMarginType(0, QsciScintilla.NumberMargin)
        self.setMarginWidth(0, '0000')
        self.setMarginsForegroundColor(Qt.black)
        self.setMarginsBackgroundColor(Qt.lightGray)

        # Lexer (Syntax Highlighting)
        lexer = QsciLexerPython()
        lexer.setDefaultFont(font)
        self.setLexer(lexer)

        # Brace matching
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # Auto-indentation
        self.setAutoIndent(True)

        # Current line highlighting
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(Qt.lightGray)

        # Enable UTF-8 encoding
        self.setUtf8(True)

        # Tab width
        self.setTabWidth(4)

        # Disable unsafe APIs
        self.setEolMode(QsciScintilla.EolUnix)
        self.setAutoCompletionSource(QsciScintilla.AcsNone)

    def isModified(self):
        return self.isModified()
