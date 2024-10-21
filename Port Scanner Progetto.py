
import socket

print ("-------------------------- \n")
print ("|      Port Scanner      | \n")
print ("-------------------------- \n \n")

target = input("Inserire l'indirizzo IP da scannerizzare: \n")
portRange = input("Inserire il range di porte da controllare: \n (Esempio 5-200) \n")
    
lowport = int(portRange.split('-')[0])
highport = int(portRange.split('-')[1])

print ("Scannerizzando IP: ", target, " dalla porta ", lowport, " alla porta ", highport)

for port in range (lowport, highport):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if (status == 0):

        print("Porta ", port, " - APERTA  ***")
    else:
        print("Porta ", port, " - CHIUSA") 