import matplotlib.pyplot as plt

emoji_data = {
    "nome": "Smile",
    "grade": [
        [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)],  # Linha 0
        [(255, 255, 0), (0, 0, 0), (255, 255, 0), (0, 0, 0), (255, 255, 0)],  # Linha 1 (Olhos)
        [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)],  # Linha 2
        [(255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0)],  # Linha 3 (Boca)
        [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)]  # Linha 4
    ]
}

new_emoji = {}

for chave, valor in emoji_data.items():
    if chave == "nome":
        new_emoji[chave] = valor
    elif chave == "grade":
        new_grade = []

        for linha in valor:
            nova_linha = []

            for pixel in linha:
                if pixel == (255, 255, 0):
                    novo_pixel = (pixel[0] // 2, pixel[1] // 2, pixel[2] // 2)
                else:
                    novo_pixel = pixel

                nova_linha.append(novo_pixel)

            new_grade.append(nova_linha)

            new_emoji[chave] = new_grade

print(new_emoji)

plt.imshow(new_emoji["grade"])
plt.show()
