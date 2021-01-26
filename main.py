def ngedata(x):
    for i in range(len(x)):
        if x[i] not in listHuruf:
            listHuruf.append(x[i])


f = open("E:\My-Programs\cryptarithmetic\data.txt","r")
a = f.read(1)

op1 = ""
op2 = ""
hasil = ""

# Nyimpen operand 1
while (a != "\n"):
    op1 = op1 + a
    a = f.read(1)
a = f.read(1)

# Nyimpen operand 2
while(a != "+"):
    op2 = op2 + a
    a = f.read(1)
a = f.read(1)

# Nyimpen hasil
a = f.readline()
a = f.readline()
hasil = hasil + a

# Konversi ke list
op1List = list(op1)
op2List = list(op2)
hasilList = list(hasil)

# Ngedata ada huruf apa aja
listHuruf = []

ngedata(op1List)
ngedata(op2List)
ngedata(hasilList)
