"""4.2. Разработать фрагмент программы с использованием библиотеки pyqrcode, позволяющей создавать изображение QR-кода на основе переданной в программу текстовой строки."""

import pyqrcode

code = pyqrcode.create("QR code from Igor Kozyrkov")
code.svg("QR-code.svg", scale=2, background="white")

"""4.3. Реализовать модификацию изображения генерируемого QR-кода: раскрасить фрагменты изображения в несколько случайно определяемых цветов."""

code.svg("Red_QR-code.svg", scale=2, module_color="red", background="black")
code.svg("Yellow-Blue_QR-code.svg", scale=2, module_color="yellow", background="blue")
