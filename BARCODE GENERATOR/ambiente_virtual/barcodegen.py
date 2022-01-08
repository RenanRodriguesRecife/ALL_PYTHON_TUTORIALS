#pip install python-barcode
#pip install Pillow

from barcode import EAN13
from barcode.writer import ImageWriter #para salvar em png

numero = "123456784432"



codigo_barra = EAN13(numero, writer=ImageWriter())#para salvar em png
codigo_barra.save("codigo_barra")