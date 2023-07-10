# importe a biblioteca opencv 
import cv2
import numpy as np
#Carregando o arquivo do classificador
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
# Defina um objeto VideoCapture
vid = cv2.VideoCapture("walking.avi")

while(True):
   
    # Capture o vídeo quadro a quadro
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Detectar rostos
    #1.1 -> fator de escala (aumenta a precisão)
    #5 -> características de detecção do rosto (de 0 a 4)
    body = body_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in body:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
       color = frame[y:y+h,x:x+w]
       #acessar o arquivo e escrever nele
       cv2.imwrite("corpo.png",color)

    # Exiba o quadro resultante
    cv2.imshow("Frame", frame)
      
    # Saia da tela ao pressionar a barra de espaço
    if cv2.waitKey(25) == 32:
        break
  
# Após o loop, libere o objeto capturado
vid.release()

# Destrua todas as telas
cv2.destroyAllWindows()