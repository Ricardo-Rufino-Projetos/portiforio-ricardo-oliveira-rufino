biblioteca_musical = {
    "Toques": [
        {"Alegre": ([440, 480], [520, 560])},
        {"Triste": ([200, 150], [100, 50])}
    ]
}

for chave, lista_musicas in biblioteca_musical.items():

    for musica in lista_musicas:
        for nome, matriz in musica.items():
            linha1, linha2 = matriz
            nova_matriz = []

            for i in range(len(linha1)):
                nova_linha = []

                nova_linha.append(linha1[i])
                nova_linha.append(linha2[i])

                nova_matriz.append(nova_linha)

            musica.update({nome: nova_matriz})

print(biblioteca_musical)

playlist = {
    "imagens": [
        {
            "nome": "Sol",
            "pixels": [(255, 255, 0), (255, 255, 0), (0, 0, 0)]
        },
        {
            "nome": "Noite",
            "pixels": [(0, 0, 0), (255, 255, 0), (0, 0, 0)]
        }
    ]
}