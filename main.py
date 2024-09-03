import sys

from typing import Union, Optional

from operator import add, sub, mul, truediv

from PySide6.QtWidgets import QApplication, QMainWindow

from calc1 import Ui_mainWindow

from PySide6.QtGui import QFontDatabase

import calcres_rc

operations = {
    '+': add,
    '-': sub,
    'x': mul,
    '/': truediv
}

error_zero_div = 'Division by'
error_undefined = 'Resualt is undefined'

default_font_size = 16
default_line_font_size = 40


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.entry_max_len = self.ui.lineEdit1.maxLength()
        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

        #digits
        self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))
        #actions
        self.ui.btn_C.clicked.connect(self.clear_all)
        self.ui.btn_CE.clicked.connect(self.clear_entry)
        self.ui.btn_dot.clicked.connect(self.add_point)
        self.ui.btn_negative.clicked.connect(self.negate)
        self.ui.btn_undo.clicked.connect(self.backspace)
        #math
        self.ui.btn_equal.clicked.connect(self.calculate)
        self.ui.btn_plus.clicked.connect(lambda: self.add_temp('+'))
        self.ui.btn_minus.clicked.connect(lambda: self.add_temp('-'))
        self.ui.btn_x.clicked.connect(lambda: self.add_temp('x'))
        self.ui.btn_p.clicked.connect(lambda: self.add_temp('/'))

    def add_digit(self, btn_text: str) -> None:
        self.remove_error()
        self.clear_temp_if_equality()

        if self.ui.lineEdit1.text() == '0':
            self.ui.lineEdit1.setText(btn_text)
        else:
            self.ui.lineEdit1.setText(self.ui.lineEdit1.text() + btn_text)

        self.adjust_entry_font_size()

    def backspace(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()

        entry = self.ui.lineEdit1.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.ui.lineEdit1.setText('0')
            else:
                self.ui.lineEdit1.setText(entry[:-1])
        else:
            self.ui.lineEdit1.setText('0')

        self.adjust_entry_font_size()

    def clear_all(self) -> None:
        self.remove_error()
        self.ui.lineEdit1.setText('0')
        self.ui.label1.clear()
        self.adjust_entry_font_size()

    def clear_entry(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()

        self.ui.lineEdit1.setText('0')
        self.adjust_entry_font_size()

    def clear_temp_if_equality(self) -> None:
        if self.get_math_sign() == '=':
            self.ui.label1.clear()

    def add_point(self) -> None:

        self.clear_temp_if_equality()

        if '.' not in self.ui.lineEdit1.text():
            self.ui.lineEdit1.setText(self.ui.lineEdit1.text() + '.')

        self.adjust_entry_font_size()

    def negate(self):

        self.clear_temp_if_equality()

        entry = self.ui.lineEdit1.text()

        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]

        if len(entry) == self.entry_max_len + 1 and '-' in entry:
            self.ui.lineEdit1.setMaxLength(self.entry_max_len + 1)
        else:
            self.ui.lineEdit1.setMaxLength(self.entry_max_len)

        self.ui.lineEdit1.setText(entry)

        self.adjust_entry_font_size()

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def add_temp(self, math_sign: str):
        if not self.ui.label1.text() or self.get_math_sign() == '=':
            self.ui.label1.setText(self.remove_trailing_zeros(self.ui.lineEdit1.text()) + f' {math_sign} ')
            self.ui.lineEdit1.setText('0')
        self.adjust_entry_font_size()
        self.adjust_temp_font_size()

    def get_entry_num(self) -> Union[int, float]:
        entry = self.ui.lineEdit1.text().strip('.')

        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.label1.text():
            temp = self.ui.label1.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> Optional[str]:
        if self.ui.label1.text():
            return self.ui.label1.text().strip('.').split()[-1]

    def get_line_edit_text_width(self):
        return self.ui.lineEdit1.fontMetrics().boundingRect(self.ui.lineEdit1.text()).width()

    def get_temp_text_width(self):
        return self.ui.label1.fontMetrics().boundingRect(self.ui.label1.text()).width()

    def calculate(self) -> Optional[str]:
        entry = self.ui.lineEdit1.text()
        temp = self.ui.label1.text()

        if temp:
            try:
                resualt = self.remove_trailing_zeros(
                    str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num()))
                )
                self.ui.label1.setText(temp + self.remove_trailing_zeros(entry) + ' =')
                self.ui.lineEdit1.setText(resualt)
                return resualt
            except KeyError:
                pass

            except ZeroDivisionError:
                if self.get_temp_num() == 0:
                    self.show_err(error_undefined)
                else:
                    self.show_err(error_zero_div)
        self.adjust_entry_font_size()
        self.adjust_temp_font_size()

    def math_operation(self, math_sign: str):
        temp = self.ui.label1.text()

        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math_sign() != math_sign:
                if self.get_math_sign() == '=':
                    self.add_temp(math_sign)
                else:
                    self.ui.label1.setText(temp[:-2] + f'{math_sign} ')
            else:
                self.ui.label1.setText(self.calculate() + f' {math_sign}')

        self.adjust_temp_font_size()

    def show_err(self, text: str) -> None:
        self.ui.lineEdit1.setMaxLength(len(text))
        self.ui.lineEdit1.setText(text)
        self.disable_buttons(True)
        self.adjust_entry_font_size()

    def remove_error(self) -> None:
        if self.ui.lineEdit1.text() in (error_undefined, error_zero_div):
            self.ui.lineEdit1.setMaxLength(self.entry_max_len)
            self.ui.lineEdit1.setText('0')
            self.disable_buttons(False)
            self.adjust_entry_font_size()

    def disable_buttons(self, disable: bool) -> None:
        self.ui.btn_equal.setDisabled(disable)
        self.ui.btn_plus.setDisabled(disable)
        self.ui.btn_dot.setDisabled(disable)
        self.ui.btn_minus.setDisabled(disable)
        self.ui.btn_x.setDisabled(disable)
        self.ui.btn_p.setDisabled(disable)
        self.ui.btn_negative.setDisabled(disable)

        color = 'color: #666;' if disable else 'color: white;'
        self.change_buttons_color(color)

    def change_buttons_color(self, css_color: str):
        self.ui.btn_equal.setStyleSheet(css_color)
        self.ui.btn_plus.setStyleSheet(css_color)
        self.ui.btn_dot.setStyleSheet(css_color)
        self.ui.btn_minus.setStyleSheet(css_color)
        self.ui.btn_x.setStyleSheet(css_color)
        self.ui.btn_p.setStyleSheet(css_color)
        self.ui.btn_negative.setStyleSheet(css_color)

    def adjust_entry_font_size(self) -> None:
        font_size = default_line_font_size
        while self.get_line_edit_text_width() > self.ui.lineEdit1.width() - 15:
            font_size -= 1

            if font_size < 2:
                break

            self.ui.lineEdit1.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')
        font_size = 1
        while self.get_line_edit_text_width() < self.ui.lineEdit1.width() - 60:
            font_size += 1

            if font_size > default_line_font_size:
                break

            self.ui.lineEdit1.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

    def adjust_temp_font_size(self) -> None:
        font_size = default_font_size
        while self.get_temp_text_width() > self.ui.label1.width() - 10:
            font_size -= 1
            self.ui.label1.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')
        font_size = 1
        while self.get_temp_text_width() < self.ui.label1.width() - 60:
            font_size += 1

            if font_size > default_font_size:
                break

            self.ui.label1.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

    def resizeEvent(self, event) -> None:
        self.adjust_entry_font_size()
        self.adjust_temp_font_size()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
