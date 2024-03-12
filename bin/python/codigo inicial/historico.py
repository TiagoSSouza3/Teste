import boletins

historico_boletins = []
def mostrar_notas(boletin: list):
    try:
        if boletin[0] != None:
            print("---------------------------")
            print("Boletin")
            for index, nota in enumerate(boletin):
                print("Nota " + str(index + 1) + " = " + str(nota))
            media_formatada = str("{:.2f}".format(boletins.media(boletin)))
            print("Media final = " + media_formatada)
            print("---------------------------")
            boletin.append(media_formatada)
            historico_boletins.append(boletin)
            return
    except:
        print("Boletin vazio")