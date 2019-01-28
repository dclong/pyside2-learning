#!/usr/bin/python3
# https://build-system.fman.io/python-qt-tutorial

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from requests import Session

name = 'Ben Du' 
chat_url = 'https://build-system.fman.io/chat'
server = Session()

# GUI:
app = QApplication([])
text_area = QTextEdit()
text_area.setFocusPolicy(Qt.NoFocus)
message = QLineEdit()
layout = QVBoxLayout()
layout.addWidget(text_area)
layout.addWidget(message)
window = QWidget()
window.setLayout(layout)
window.show()

# Event handlers:
def display_new_messages():
    new_message = server.get(chat_url).text
    if new_message:
        text_area.append(new_message)

def send_message():
    server.post(chat_url, {'name': name, 'message': message.text()})
    message.clear()

# Signals:
message.returnPressed.connect(send_message)
timer = QTimer()
timer.timeout.connect(display_new_messages)
timer.start(1000)

app.exec_()