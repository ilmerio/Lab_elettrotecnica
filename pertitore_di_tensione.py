# importo le librerie
import serial
import time


def main():
    # apro la comunicazione seriale con la scheda
    arduino = serial.Serial("COM3", 9600)
    time.sleep(1)
    print("PRONTO A RICEVERE DATI")
    data = []

    # ciclo con cui creo la lista dei dati da elaborare esco premendo ctrl+c
    while True:
        # leggo e pulisco la stringa
        data.append(arduino.readline().decode("utf-8").rstrip())
        # converto la stringa appena ricevuta in float
        volt = float(data[-1])
        # stampo la tensione i capi del potenziometro
        print("V ", volt, end=", ")
        r = (volt * 1000) / (5 - volt)
        # stampo il valore della resistenza del potenziometro, ogni volta che si modifica il valore del potenziometro si può vedere il variare della tensione
        print("R %.3f ," % r)

    # chiudo la comunicazione seriale
    arduino.close()


main()
