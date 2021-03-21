
#mencari pola ke - 1
#[0,0] = 0          
#[1,1] = 1          +1
#[2,2] = 4          +3
#[3,3] = 5          +1
#[4,4] = 8          +3
#[5,5] = 9          +1
#[6,6] = 12         +3

#mencari pola ke - 2
#[2,0] = 2          
#[3,1] = 3         +1
#[4,2] = 6         +3
#[5,3] = 7         +1
#[6,4] = 10        +3
#[7,5] = 11        +1 

def steponNumber(pola):
    hasil = []
    for i in range(len(pola)): #memisah nilai x dan y
        x = pola[i][0]
        y = pola[i][1]
        if x == y: #untuk pola ke -1
            tambah = 2
            sum = 0
            for i in range(0,x):
                sum += tambah
            hasil.append(sum)
        if y + 2 == x: #untuk pola ke -2
            tambah = 3
            sum = 0
            for i in range(2,x):
                sum += tambah
            hasil.append(sum)
    if y != x or y + 2 != x:
        b = 'No Number'
        hasil.append(b)
    return hasil


pola = [[4,2],[6,6],[3,4]]
print(steponNumber(pola))