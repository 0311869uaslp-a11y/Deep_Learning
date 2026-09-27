#Instalamos la librería necesaria
#!pip install rembg

#Llamamos a la libreria instalada
from rembg import remove

#Path de imagen que tenemos en nuestro disco e imagen que vamos a obtener como resultado
input_path = "caballo.jpg"
output_path = "caballo_sinfondo.jpg"

#Leemos imagen input y Python procede a generarte una nueva imagen sin fondo en output
with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)