#condiciones
texto = "Este es el texto de Federico"
mayusculas = texto.upper()
caracterMayus = texto[2].upper()
minusculas = texto.lower()
separarTexto = texto.split()
SeparadorCondicionado = texto.split("t")
buscarCaracter = texto.find("s")    #cuando find no encuentre el objeto, droppea -1
reemplazarTexto = texto.replace("Federico","todos")
print(texto)

#Metodo join
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])

print(e)
