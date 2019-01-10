from PySide2.QtCore import *
from PySide2.QtWidgets import *
import arrow
import workdays

# GUI:
app = QApplication([])

labelTitle = QLabel()
label = QLabel()
label2 = QLabel()
label3 = QLabel()

labelTitle.setText("But how long EXACTLY is left? :P")
label.setText("Initial text")
label2.setText("Initial text")
label3.setText("Initial text")

layout = QVBoxLayout()
layout.addWidget(labelTitle)
layout.addWidget(label)
layout.addWidget(label2)
layout.addWidget(label3)

window = QWidget()
window.setWindowTitle("Count Down App")
window.setLayout(layout)
window.show()


def display_new_messages():

    now = arrow.now()
    end = arrow.get('2019-01-31 00:00:00', 'YYYY-MM-DD HH:mm:ss')
    calc = now - end
    label.setText("Exact time left including weekends: " + str(calc))

    # TODO: add a description label
    label2.setText("Total working days left: " + str(workdays.networkdays(now, end)))

    totalHrsLeft = workdays.networkdays(now, end) * 7.5
    label3.setText("Total working Hrs left: " + str(totalHrsLeft))


# def countDownDispaly():



# Signals:
timer = QTimer()
timer.timeout.connect(display_new_messages)
timer.start(1000)

app.exec_()