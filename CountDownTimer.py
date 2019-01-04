from PySide2.QtCore import *
from PySide2.QtWidgets import *

# GUI:
app = QApplication([])
text_area = QTextEdit()
# text_area.setFocusPolicy(Qt.NoFocus)
# message = QLineEdit()
layout = QVBoxLayout()
layout.addWidget(text_area)
# layout.addWidget(message)
window = QWidget()
window.setLayout(layout)
window.show()


def display_new_messages():
    text_area.append('test')


# Signals:
timer = QTimer()
timer.timeout.connect(display_new_messages)
timer.start(1000)

app.exec_()