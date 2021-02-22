Alphabetic = {
         '0':'อ',
         'h':'า',
         'i':'ิ',
         'j':'ี',
         'k':'ุ',
         'l':'ู',
         'm':'เ',
         'n':'โ',
         'g':'ํ',
         'o':'ฺ',
    'A' : 'ก',
    'B' : 'ข',
    'C' : 'ค',
    'D' : 'ฆ',
    'E' : 'ง',
    'F' : 'จ',
    'G' : 'ฉ',
    'H' : 'ช',
    'I' : 'ฌ',
    'J' : 'ญ',
    'K' : 'ฏ',
    'L' : 'ฐ',
    'M' : 'ฑ',
    'N' : 'ฒ',
    'O' : 'ณ',
    'P' : 'ต',
    'Q' : 'ถ',
    'R' : 'ท',
    'S' : 'ธ',
    'T' : 'น',
    'U' : 'ป',
    'V' : 'ผ',
    'W' : 'พ',
    'X' : 'ภ',
    'Y' : 'ม',
    'Z' : 'ย',
    'a' : 'ร',
    'b' : 'ล',
    'c' : 'ว',
    'd' : 'ส',
    'e' : 'ห',
    'f' : 'ฬ'
}
#Alphabetic = Vowels + Consonants


def sortlistpalithai(word):

    def convertfunction(x):
        u = []
        for y in x:
            j = list(Alphabetic.keys())[list(Alphabetic.values()).index(y)]
            u.append(j)
        return u


    def convertcommand(x):
        j = []
        for i in range(0,len(x)):
            a = convertfunction(x[i])
            j.append(a)

        return j


    data = convertcommand(word)  #นำ keys ที่ระบุไว้ในตอนที่ทำ dictionary อักษรโดยทำการเปลี่ยนตัวอักษรเป็น keys
    d = ''
    def sortconvert(data):
        for y in range(1,len(data)):
            for z in range(0,len(data)-1):
                if y != z:
                    if data[y] > data[z]:
                        d = data[y]
                        data[y] = data[z]
                        data[z] = d
                        if True:
                            stud = True


        return data

    y = sortconvert(data)  #ทำการเรียงอักษรเบื้องต้น

    def sortreversed(y):
        i = []
        for a in range(0,len(y)):
            i.append(y[-1-a])
        return i


    z = sortreversed(y)  #จำเป็นต้องใช้คำสั่งนี้เพียงเพราะว่า การสลับโดยไม่ทำการเรียงจำทำให้เกิดข้อผิดพลาดมากกว่า

    def swappedinput(z): #this function is ทำงานโดยมีข้อผิดพลาดตรงที่เฉพาะเจาะจงต่อปริมาณของอักษร
        def swapped(z,a):
            for i in range(0,len(z)):
                if len(z[i]) == a:
                    for j in range(0,len(z[i])):
                        d = z[i]
                        k = j + 1
                        if j < a-1:
                            if d[a-2] == 'm' and d[a-1] != '0':
                                c = d[a-2]
                                d[a-2] = d[a-1]
                                d[a-1] = c

                            if d[a-2] == 'm' and d[a-1] != '0':
                                c = d[a-2]
                                d[a-2] = d[a-1]
                                d[a-1] = c
                                if d[a - 3] == 'm' and d[a - 2] != '0':
                                    c = d[a - 3]
                                    d[a - 3] = d[a - 2]
                                    d[a - 2] = c
                                    break
                            if d[j] == 'm' and d[k] != '0'or d[k] == '0':
                                c = d[j]
                                d[j] = d[k]
                                d[k] = c
                                break
                            if d[a - 2] == 'n' and d[a - 1] != '0':
                                c = d[a - 2]
                                d[a - 2] = d[a - 1]
                                d[a - 1] = c

                            if d[a - 2] == 'n' and d[a - 1] != '0':
                                c = d[a - 2]
                                d[a - 2] = d[a - 1]
                                d[a - 1] = c
                                if d[a - 3] == 'n' and d[a - 2] != '0':
                                    c = d[a - 3]
                                    d[a - 3] = d[a - 2]
                                    d[a - 2] = c
                                    break
                            if d[j] == 'n' and d[k] != '0' or d[k] == '0':
                                c = d[j]
                                d[j] = d[k]
                                d[k] = c
                                break
                elif a == 1:
                    break

            return z

        swapped(z,2)
        swapped(z,3)
        swapped(z,4)
        swapped(z,5)
        swapped(z,6)
        swapped(z,7)
        swapped(z,8)
        swapped(z,9)
        swapped(z,10)
        swapped(z,11)
        return z

    a = swappedinput(z)
    r = sortreversed(sortconvert(a))


    def swappedinputagain(r): #this function is swapped กลับไปตำแหน่งก่อนหน้าเพราะว่าต้องการจะเปลี่ยนกลับไปเป็นภาษาไทย
        def swapped(r,a):
            for i in range(0,len(r)):
                if len(r[i]) == a:
                    for j in range(0,len(r[i])):
                        d = r[i]
                        k = j + 1
                        if j < a-1:
                            if d[a-2] != '0' and d[a-1] == 'm':
                                c = d[a-2]
                                d[a-2] = d[a-1]
                                d[a-1] = c

                            if d[a-2] != '0' and d[a-1] == 'm':
                                c = d[a-2]
                                d[a-2] = d[a-1]
                                d[a-1] = c
                                if d[a - 3] != '0' and d[a - 2] == 'm':
                                    c = d[a - 3]
                                    d[a - 3] = d[a - 2]
                                    d[a - 2] = c
                                    break
                            if d[j] != '0' and d[k] == 'm'or d[j] == '0':
                                c = d[j]
                                d[j] = d[k]
                                d[k] = c
                                break
                            if d[a - 2] != '0' and d[a - 1] == 'n':
                                c = d[a - 2]
                                d[a - 2] = d[a - 1]
                                d[a - 1] = c

                            if d[a - 2] != '0' and d[a - 1] == 'n':
                                c = d[a - 2]
                                d[a - 2] = d[a - 1]
                                d[a - 1] = c
                                if d[a - 3] != '0' and d[a - 2] == 'n':
                                    c = d[a - 3]
                                    d[a - 3] = d[a - 2]
                                    d[a - 2] = c
                                    break
                            if d[j] != '0' and d[k] == 'n'or d[j] == '0':
                                c = d[j]
                                d[j] = d[k]
                                d[k] = c
                                break
                elif a == 1:
                    break

            return r
        swapped(r,2)
        swapped(r,3)
        swapped(r,4)
        swapped(r,5)
        swapped(r,6)
        swapped(r,7)
        swapped(r,8)
        swapped(r,9)
        swapped(r,10)
        swapped(r,11)

        return r

    bb = swappedinputagain(r)

    h = []
    g = []
    def converttovalues(bb):
        for i in range(0,len(bb)):
            d = bb[i]
            def tovalues(d):
                h = []
                d = bb[i]
                j = 0
                while j >= 0 and j < len(d):
                    w = Alphabetic[d[j]]
                    h.append(w)
                    j += 1
                return h

            g.append(tovalues(d))
        return g


    w = converttovalues(bb)
    goal = []
    def lstostring(w):
        out_str= ""
        for x in w:
            goal.append(out_str.join(x))
        return goal


    result = lstostring(w)
    return result

if __name__ == '__main__':
    word = ['โสภติ', 'สติ', 'หิริ', 'โค', 'โสโก', 'เหฏฺฐา', 'ปโรสตํ', 'โอตฺตปฺป', 'พฺยญฺชนํ', 'พยาธิ']
    print(word)
    word = sortlistpalithai(word)
    print(word)




