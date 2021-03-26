import AnalizadorSemantico

analizador = AnalizadorSemantico.AnalizadorSemantico() #definimos el metodo principal que hara toda la ejecucion

analizador._imprimirArchivo()#impresion del archivo
print()
analizador.crear_tabla()
analizador._errorAsignacion()#errores detectados
analizador._errorDeCuerpoFunciones()
print()


