diccionario_de_memes = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador, siniestro",
            "AGGRO": "Ponerse agresivo/enojado",
            }

palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
#DECIR EL SIGNIFICADO DE LAS PALABRAS.
if palabra in diccionario_de_memes.keys():
    print(diccionario_de_memes[palabra])
else:
    print('Esta palabra no existe.')
