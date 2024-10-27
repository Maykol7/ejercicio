print("HOLA, BIENVENIDO/A A MI DICCIONARIO")

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobacion",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agreviso o enojado"
            }

for i in range(5):
    word = input("\nEscribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(word, "significa: ", meme_dict [word])
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print("Lo siento, no tenemos esta palabra por ahora")
