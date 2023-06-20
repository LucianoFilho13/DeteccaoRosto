# importe a biblioteca opencv 
import cv2

# Defina um objeto VideoCapture
vid = cv2.VideoCapture(0)

det = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
   
    # Capture o vídeo quadro a quadro
    ret, frame = vid.read()
    vidBW = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) #Escurecer a foto

    scale = det.detectMultiScale(vidBW)

    for (x,y,w,h) in scale:
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,215,0),2)

    # Exiba o quadro resultante
    cv2.imshow("Web cam", frame)
      
    # Saia da tela ao pressionar a barra de espaço
    if cv2.waitKey(25) == 32:
        break
  
# Após o loop, libere o objeto capturado
vid.release()

# Destrua todas as telas
cv2.destroyAllWindows()