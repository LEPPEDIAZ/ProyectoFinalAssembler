Código de Prueba: (Python)
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida
GPIO.setup(27, GPIO.OUT) ## GPIO 27 como salida
GPIO.setup(18, GPIO.OUT) ## GPIO 18 como salida
GPIO.setup(22, GPIO.OUT) ## GPIO 22 como salida
print "Bienvenido al programa"
print "Velocidad 1 = rapida"
print "Velocidad 2 = media"
print "Velocidad 3 = lenta"
ciclo = False
while ciclo == False:
    resp = raw_input("Escoja una velocidad para la secuencia (de 1 a 3): ")
    if resp == "1":
       loop=10
       while loop != 0:
           GPIO.output(17,True)
           GPIO.output(18,False)
           GPIO.output(22,False)
           GPIO.output(27,True)
           time.sleep(0.05)
           GPIO.output(17,True)
           GPIO.output(18,True)
           GPIO.output(22,False)
           GPIO.output(27,False)
           time.sleep(0.05)
           GPIO.output(17,False)
           GPIO.output(18,True)
           GPIO.output(22,True)
           GPIO.output(27,False)
           time.sleep(0.05)
           GPIO.output(17,False)
           GPIO.output(18,False)
           GPIO.output(22,True)
           GPIO.output(27,True)
           time.sleep(0.05)
           loop = loop -1
      
    if resp == "2":
       loop=10
       while loop != 0:
           GPIO.output(17,True)
           GPIO.output(18,False)
           GPIO.output(22,False)
           GPIO.output(27,True)
           time.sleep(0.25)
           GPIO.output(17,True)
           GPIO.output(18,True)
           GPIO.output(22,False)
           GPIO.output(27,False)
           time.sleep(0.25)
           GPIO.output(17,False)
           GPIO.output(18,True)
           GPIO.output(22,True)
           GPIO.output(27,False)
           time.sleep(0.25)
           GPIO.output(17,False)
           GPIO.output(18,False)
           GPIO.output(22,True)
           GPIO.output(27,True)
           time.sleep(0.25)
           loop = loop -1
           
    if resp == "3":
       loop=10
       while loop != 0:
           GPIO.output(17,True)
           GPIO.output(18,False)
           GPIO.output(22,False)
           GPIO.output(27,True)
           time.sleep(0.75)
           GPIO.output(17,True)
           GPIO.output(18,True)
           GPIO.output(22,False)
           GPIO.output(27,False)
           time.sleep(0.75)
           GPIO.output(17,False)
           GPIO.output(18,True)
           GPIO.output(22,True)
           GPIO.output(27,False)
           time.sleep(0.75)
           GPIO.output(17,False)
           GPIO.output(18,False)
           GPIO.output(22,True)
           GPIO.output(27,True)
           time.sleep(0.75)
           loop = loop -1
    resp2 = raw_input("Desea probar otra velocidad?(n/s): ")
    if resp2 == "n":
       ciclo=True
           
