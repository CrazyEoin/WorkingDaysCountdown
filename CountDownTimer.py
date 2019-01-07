from PySide2.QtCore import *
from PySide2.QtWidgets import *
import arrow

# GUI:
app = QApplication([])
text_area = QTextEdit()
label = QLabel()
label.setText("Initial text")

# self.title = 'This is my title'
# self.left = 400
# self.top = 400
# self.width = 300
# self.height = 200

layout = QVBoxLayout()
layout.addWidget(text_area)
layout.addWidget(label)

window = QWidget()
window.setLayout(layout)
window.show()


def display_new_messages():
    # d1 = arrow.get('2012-06-05 16:20:03', 'YYYY-MM-DD HH:mm:ss')
    # d2 = arrow.get(1504384602)
    # text_area.append('d1: '+str(d1))
    # text_area.append('d2: ' + str(d2))

    now = arrow.now()
    end = arrow.get('2019-01-31 00:00:00', 'YYYY-MM-DD HH:mm:ss')
    calc = now - end
    text_area.append(str(calc))
    label.setText(str(calc))


# def countDownDispaly():



# Signals:
timer = QTimer()
timer.timeout.connect(display_new_messages)
timer.start(1000)

app.exec_()