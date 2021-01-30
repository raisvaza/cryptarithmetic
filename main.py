from itertools import permutations
import time

hurufPertama = []
hurufPertamaUnik = []
hurufSemua = []
hurufUnik = []
operand = [] # list berisi operand dan hasil
seluruhString = ""
permutasi = [0 for i in range(10)] # permutasi


# Input Text
f = open("E:/My-Programs/cryptarithmetic/data.txt","r")
for i in f:
    seluruhString = seluruhString + i
    if (i[0] != '-'):
        kata = ""
        hurufPertama.append(i[0])
        for j in i:
            if ((j != '\n') and (j != '-') and (j != '+')):
                hurufSemua.append(j)
                kata = kata + j
                #print(kata)
        operand.append(kata)

# Bikin Unik
for i in range(len(hurufSemua)):
    if hurufSemua[i] not in hurufUnik:
        hurufUnik.append(hurufSemua[i])

for i in range(len(hurufPertama)):
    if hurufPertama[i] not in hurufPertamaUnik:
        hurufPertamaUnik.append(hurufPertama[i])

korespondensi = [" " for i in range(len(hurufUnik))] # daftar huruf yang berkorespondensi dengan angka


indeks = len(hurufPertamaUnik)
for i in range(indeks):
    if hurufPertamaUnik[i] not in korespondensi:
        korespondensi[i] = hurufPertamaUnik[i]

i = 0
while (i < len(hurufUnik)):
    if hurufUnik[i] not in korespondensi:
        korespondensi[indeks] = hurufUnik[i]
        indeks = indeks + 1
    i = i + 1


permHurufPertama = 9
permHurufNonPertama = 10 - len(hurufPertamaUnik)

for i in range(len(hurufPertamaUnik)):
    permutasi[i] = permHurufPertama
    permHurufPertama = permHurufPertama - 1

for i in range(len(hurufPertamaUnik),len(korespondensi)):
    permutasi[i] = permHurufNonPertama
    permHurufNonPertama = permHurufNonPertama - 1

# Membuang 0 pada list permutasi

for i in range(len(permutasi)-len(korespondensi)):
    permutasi.remove(0)

# Percobaan Seluruh Permutasi
start = time.time()
print(start)

perm = permutations(permutasi)
for percobaanKeN in perm:
    operandConverted = []
    korespondensiConverted = [0 for i in range(len(korespondensi))]
    for item in operand:
        itemConverted = 0
        for huruf in item:
            for i in range(len(korespondensi)):
                if huruf == korespondensi[i]:
                    korespondensiConverted[i] = percobaanKeN[i]
                    itemConverted = itemConverted*10 + percobaanKeN[i]
        operandConverted.append(itemConverted)
    if (operandConverted[0] == 9567):
        print(operandConverted)
    jumlah = 0
    for i in range(len(operandConverted)-1):
        jumlah = jumlah + operandConverted[i]
    if (jumlah == operandConverted[len(operandConverted)-1]):
        for i in range(len(operand)):
            print(operand[i] + "                               " + operandConverted[i])
            if (i == len(operand) - 1):
                print("-------- +" + "                               "  + "-------- +")
        
        '''print(korespondensi)
        print(korespondensiConverted)'''
end = time.time()
print(end)
print(end - start)
