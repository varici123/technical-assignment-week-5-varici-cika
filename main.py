import dht11
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = []
    for i in range(5):
        x.append(dht11.ambil())
        time.sleep(0.2)
    
    print(x)
    plt.plot(x)
    plt.show()

#menentukan bilagnan ganjil apa genap
def ganjilGenap(suhu):
    if suhu % 2 == 0:
        return "genap"
    else :
        return "Ganjil"

while True:
    hm = dht11.ambil()
    
    #mecetak hasil
    print("%0.0f*C, adalah suhu dalam bilangan"%(hm), ganjilGenap(hm))
