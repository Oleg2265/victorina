from PyQt5.QtWidgets import *
import random

app = QApplication([])

window = QWidget()
window.resize(500, 500)
lbl = QLabel("Вікторина")
lbl2 = QLabel("нажми на кнопку")
butterbrod = QPushButton("Стати молодцем")


main_line = QVBoxLayout()
main_line.addWidget(lbl)
main_line.addWidget(lbl2)


def banana():
    a = random.randint(1, 2)
    if a == 1:
        lbl2.setText(str("Ти молодець"))

    else:
        lbl2.setText(str("Ти не молодець >:("))
butterbrod.clicked.connect(banana)
main_line.addWidget(butterbrod)



window.setLayout((main_line))
window.show()

app.exec()