def readImage(filepath):
    with open(filepath, "r") as image:
        imageType = image.readline().strip()
        assert imageType == "P2", "Não é P2"
        
        line = image.readline().strip()
        
        width, height = map(int, line.split())
        grayscaleBits = int(image.readline().strip())
        
        pixels = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(image.readline().strip())
            pixels.append(row)
        
    return pixels, grayscaleBits, width, height

def convertBits(pixels, limiar, width, height):
    convertedPixelsFixed = []
    convertedPixelsDynamic = []
    for y in range(height):
        fixedRow = []
        for x in range(width):
            chosenPixel = pixels[y][x]
            newPixel = 255
            if int(chosenPixel) <= limiar:
                newPixel = 0
            fixedRow.append(newPixel)
        convertedPixelsFixed.append(fixedRow)
    
    return convertedPixelsFixed, convertedPixelsDynamic


def saveIMG(filename, pixels, width, height):
    with open(filename, "w") as newImage:
        newImage.write("P2\n")
        newImage.write(str(width) + " " + str(height) + "\n")
        newImage.write(str(255) + "\n")
        
        for row in pixels:
            newImage.write(" ".join(map(str, row)) + "\n")
            
originalIMG = "Entrada_EscalaCinza.pgm"

pixels, bits, width, height = readImage(originalIMG)
limiar = 40
convertedPixelsFixed, convertedPixelsDynamic = convertBits(pixels, limiar, width, height)

output = "binary.pbm"

saveIMG(output, convertedPixelsFixed, width, height)