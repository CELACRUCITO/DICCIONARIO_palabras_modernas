meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso que da pena ajena",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "una forma de reir en chats",
            "TOY JOYA": "una forma de decir que estas bien",
            "CREEPY": "algo aterrador o perturbador",
            "BOOMER": "persona que se aferra al pasado",
            "CHAMBA": "una forma de decir trabajo",
            "PAPU": "forma de decir amigo",
            "TROLL": "persona que hace bromas pesadas en internet"
            }
            
print("hola, bienvenido a la aplicacion de diccionario de palabras modernas.")



for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict:
        print("el significado de ",word," es: ",meme_dict[word])

    else:
        print("lo sentimos no tenemos esta palabra")
