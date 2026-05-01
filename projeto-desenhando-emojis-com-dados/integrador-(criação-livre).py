for chave in playlist.keys():

    for imagem in playlist[chave]:

        imagem["pixels"].pop()

        novos_pixels = []

        for pixel in imagem["pixels"]:
            novo_pixel = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])

            novos_pixels.append(novo_pixel)

        novos_pixels.insert(0, (128, 128, 128))

        imagem.update({"pixels": novos_pixels})
