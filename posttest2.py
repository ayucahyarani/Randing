import os
os.system("cls")

def partisi(l, bwh, ats) :
    pivot = l[bwh]
    batas = bwh + 1
    for q in range (bwh + 1, ats) :
        if l[q] < pivot :
            l[batas], l[q] = l[q], l[batas]
            batas += 1
    l[batas - 1], l[bwh] = l[bwh], l[batas - 1]
    return batas

def quicksort(l, bwh, ats) :
    if ats <= bwh :
        return
    r = partisi(l, bwh, ats)
    quicksort(l, bwh, r-1)
    quicksort(l, r, ats)
    return l

def searching(isi, x, n) :
    fibo2 = 0
    fibo1 = 1
    fibo = fibo2 + fibo1
    while (fibo < n):
        fibo2 = fibo1
        fibo2 = fibo
        fibo = fibo2 + fibo1
    offset = -1
    while (fibo > 1) :
        i = min(offset + fibo2, n-1)
        if (isi[i] < x) :
            fibo = fibo1
            fibo1 = fibo2
            fibo2 = fibo - fibo1
            offset = i
        elif (isi[i] > x) :
            fibo = fibo2
            fibo1 = fibo1 - fibo2
            fibo2 = fibo - fibo1
        else :
            return i
    if (fibo1 and isi[n-1] == x) :
        return n-1
    return -1

def search() :
    print("\nKetika ingin mencari huruf 'zaki' maka hasilnya : ")
    for q in range(len(data2)):
        if type(data2[q]) == list :
            isi = searching(data[q], "zaki", len(data[q]))
            print("Zaki berada di array index ke -", q, "kolom", isi)
        else :
            if data2[q] == x :
                print("zaki berada di array index ke -", q)

data = ["daiva", "zaki", ["wahyu", "zaki"], "shafa", ["zaki", "aji", "wahyu"], "zaki"]
data2 = []
data3 = {}
x = "zaki"

def sorting() :
    print("Sebelum di urutkan = ", data)
    for i in range(len(data)) :
        if type(data[i]) != str :
            data3[i] = data[i]
        else : 
            data2.append(data[i])
            quicksort(data2, 0, len(data2))
    
    for j in data3 :
        quicksort(data3[j], 0, len(data3[j])) 
        data2.insert(j, data3[j])
    print("\nSetelah di urutkan = ", data2)

sorting()
search()