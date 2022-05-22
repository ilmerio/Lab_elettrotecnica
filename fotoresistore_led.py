# importo le librerie
import serial
import time


def main():
    # apro la comunicazione seriale con la scheda
    arduino = serial.Serial("COM3", 9600)
    time.sleep(1)
    print("PRONTO A RICEVERE DATI")
    # ciclo con cui gestisco i dati letti dalla board esco premendo ctrl+c
    while True:
        # leggo e pulisco la stringa
        data = arduino.readline().decode("ascii").rstrip()
        # converto la stringa appena ricevuta in float
        tensione = float(data)
        # stampo la tensione i capi del fotoresistore
        print("V ", tensione, end=", ")
        # calcolo la il valore di resistivo del fotoresistore
        fotoresistore = (tensione * 1000) / (5 - tensione)
        # stampo il valore del fotoresistore
        print("R %.3f ," % fotoresistore)
        # se il valore supera una certa soglia invio il comndo per accendere il led alla scheda arduino
        # questo valore deve essere impostato in base alla luce ambientale, si potrebbe creare una parte di programma dove far inserire i dati all'utente
        if fotoresistore > 2000:
            led = 'a'
        else:
            led = 's'
        modo = led.encode()
        arduino.write(modo)

    # chiudo la comunicazione seriale
    arduino.close()

main()
