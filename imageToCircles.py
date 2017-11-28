import System
import rhinoscriptsyntax as rs

# Anzahl von vertikalen Spalten im Gitter
gridColumns = 190

# Gitterabstand in mm
gridGapSize = 3

# Maximale und Minimale groesse der Kreise als Durchmesser in mm
minCircleSize = 0.5
maxCircleSize = 3

# Helligkeitsfaktor; bei > 1 werde die Kreise groesser, bei < 1 kleiner
brightnessFactor = 1.2

def imageToCircles():
    filter = "Text file (*.jpg)|*.jpg|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open Image", filter)
    if not filename: return

    image = System.Drawing.Bitmap.FromFile(filename)
    image.RotateFlip(System.Drawing.RotateFlipType.RotateNoneFlipY)

    gridScale = image.Width / gridColumns
    
    outputX = 0
    outputY = 0
    
    imageX = 0
    imageY = 0

    rs.EnableRedraw(False)
    for imageX in range (0, image.Width, int(gridScale)):
        outputX = outputX+gridGapSize
        outputY = 0

        for imageY in range (0, image.Height, int(gridScale)):
            outputY = outputY + gridGapSize
            pixel = image.GetPixel(imageX, imageY)
            diameter = (pixel.GetBrightness()* gridGapSize)* brightnessFactor

            if (diameter > minCircleSize):
                if (diameter > maxCircleSize):
                    rs.AddCircle((outputX, outputY, 0), (maxCircleSize/2))
                else:
                    rs.AddCircle((outputX, outputY, 0), (diameter/2))
    rs.EnableRedraw(True)

if __name__ == "__main__":
    imageToCircles() # Call the function defined above