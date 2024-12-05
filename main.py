import sys
import random

from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow

from UI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.paint_now = False  # контроль рисования
        self.circlesButton.clicked.connect(self.draw_circle)  # линкуем кнопку с функцией

    def paintEvent(self, event):
        # отключаем рисование до нажатия кнопки
        if self.paint_now:
            painter = QPainter(self)

            # создаем сколько-то окружностей
            for _ in range(random.randint(5, 50)):
                # для каждой окружности генерируем случайные значения
                x = random.randint(0, 1200)
                y = random.randint(0, 800)
                radius = random.randint(10, 100)

                # генерируем случайный цвет для каждой окружности
                color = [random.randint(0, 255) for _ in range(3)]
                painter.setBrush(QBrush(QColor(*color)))

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
