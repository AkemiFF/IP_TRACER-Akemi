import sys
import requests
import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'IP Finder'
        self.left = 200
        self.top = 200
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.my_ip_button = QPushButton('My IP', self)
        self.my_ip_button.clicked.connect(self.my_ip_action)

        self.ip_label = QLabel('Enter IP address:')
        self.ip_input = QLineEdit(self)
        self.trace_ip_button = QPushButton('Trace IP', self)
        self.trace_ip_button.clicked.connect(self.trace_ip_action)

        self.exit_button = QPushButton('Exit', self)
        self.exit_button.clicked.connect(self.exit_action)

        vbox = QVBoxLayout()
        vbox.addWidget(self.my_ip_button)

        hbox = QHBoxLayout()
        hbox.addWidget(self.ip_label)
        hbox.addWidget(self.ip_input)
        hbox.addWidget(self.trace_ip_button)
        vbox.addLayout(hbox)

        vbox.addWidget(self.exit_button)

        self.setLayout(vbox)

        self.show()

    def my_ip_action(self):
        response = requests.get('https://api64.ipify.org?format=json').json()
        QMessageBox.information(self, 'My IP', response['ip'])

    def trace_ip_action(self):
        the_ip = self.ip_input.text()
        if the_ip:
            try:
                lookup = 'https://ipapi.co'
                response = requests.get(f'{lookup}/{the_ip}/json/').json()
                location_data = {
                    "ip": the_ip,
                    "org": response.get("org"),
                    "hostname": response.get("hostname"),
                    "version": response.get("version"),
                    "city": response.get("city"),
                    "country": response.get("country"),
                    "country_code": response.get("country_code"),
                    "country_name": response.get("country_name"),
                    "country_code_iso3": response.get("country_code_iso3"),
                    "country_capital": response.get("country_capital"),
                    "country_tld": response.get("country_tld"),
                    "country_area": response.get("country_area"),
                    "country_population": response.get("country_population"),
                    "region": response.get("region"),
                    "region_code": response.get("region_code"),
                    "continent_code": response.get("continent_code"),
                    "in_europe": response.get("in_eu"),
                    "postal": response.get("postal"),
                    "latitude": response.get("latitude"),
                    "longitude": response.get("longitude"),
                    "timezone": response.get("timezone"),
                    "utc_offset": response.get("utc_offset"),
                    "country_calling_code": response.get("country_calling_code"),
                    "currency": response.get("currency"),
                    "currency_name": response.get("currency_name"),
                    "languages": response.get("languages"),
                }
                QMessageBox.information(
                    self, 'Trace IP', json.dumps(location_data, indent=4))
                with open('results.txt', 'w') as file:
                    file.write(json.dumps(location_data, indent=4))
                QMessageBox.information(
                    self, 'Trace IP', 'Session data recorded in results.txt')
            except requests.exceptions.RequestException:
                QMessageBox.warning(
                    self, 'Trace IP', 'Could not retrieve data for this IP')
        else:
            QMessageBox.warning(self, 'Trace IP', 'Please enter an IP address')

        def exit_action(self):
            QApplication.quit()
