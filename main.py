import sys
import requests

from PyQt5.QtWidgets import QApplication , QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


from PyQt5.QtCore import Qt



class WheaterApp(QWidget):
    def __init__(self):
        super().__init__()


        self.city_label = QLabel("Enter city name:" , self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)

        self.temerature_label = QLabel("24℃", self)
        self.emoji_label = QLabel("🌡️", self)
        self.description_label = QLabel("Sunny", self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Weather App")



        vbox = QVBoxLayout()


        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temerature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)


        self.setLayout(vbox)


        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temerature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WheaterApp()
    weather_app.show()
    sys.exit(app.exec_())