import sys
import random

from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("UI.ui", self)  # загрузка файла

        self.paint_now = False  # контроль рисования
        self.yellowButton.clicked.connect(self.draw_circle)  # линкуем кнопку с функцией

    def paintEvent(self, event):
        # отключаем рисование до нажатия кнопки
        if self.paint_now:
            painter = QPainter(self)
            painter.setBrush(QBrush(QColor(255, 255, 0)))

            # создаем сколько-то окружностей
            for _ in range(random.randint(5, 50)):
                # для каждой окружности генерируем случайные значения
                x = random.randint(0, 1200)
                y = random.randint(0, 800)
                radius = random.randint(10, 100)

                # рисуем окружность
                painter.drawEllipse(x, y, radius, radius)

        self.paint_now = False

    def draw_circle(self):
        # задаем параметр рисования и обновляем виджет
        self.paint_now = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
