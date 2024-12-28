
# def re_list(lst):
#     return lst[::-1]
# list2 = [1,2,3,4,5]
# list = re_list(list2)
# print(list2)

# def change(lst):
#     lst[0],lst[-1] =  lst[-1], lst[0]
#     return lst
# print(change([9,8,7,6,5]))


# def to_list(g):
#     return list(g)
# print(to_list(9,8,7,6,5))


# def useless(a):
#     return max(a)/len(a)
# print(useless([9,8,7,6,5]))


# def list_sort(lst):
#     for i in range(len(lst)-1):
#         for b in range(len(lst)-1):
#             if abs(lst[b]) < abs(lst[b+1]):
#                 f = lst[b]
#                 l = lst[b+1]
#                 lst[b] = l
#                 lst[b+1] = f
#     return lst
# print(list_sort([9,8,7,6,5,-57,4653,47,43,]))


# def all_eq(lst):
#     a = lst[0]
#     for i in lst:
#         if len(i) > len(a):
#            a = i
#     for i, y in enumerate(lst):
#         if len(y) < len(a):
#             add = len(a) - len(y)
#             for y in range(add):
#                 lst[i] += "_"
#     return lst
# print(all_eq(["kekv","kekv4","kekvvv","kekv4536"]))

# def to_float(num):
#     if num != int(num):
#         return "Невозможно преобразовать"
#     return float(num)
# print(to_float(55))
# def gh(a,b,c,d):
#     return round((a*b*c*d)/4, 5)
# print(gh(1.45,5,7,8.957))
# def kvk(a,b):
#     if a*b%1 == 0:
#         return int(a*b)
#     return a*b
# print(kvk(1.4,2))
# def find_r(r):
#     return ((3*r)/(4*3.14))**(1/3)
# print(find_r(523.33))
# def dislike_6(a):
#     if a == 6:
#         return "Только не 6"
#     return True
# print(dislike_6(5))
# print(dislike_6(6))
# def help_bool(letter):
#     letter = letter.upper()
#     if letter == "к":
#         return "Коммутативность — свойство бинарной операции «», заключающееся в возможности перестановки аргументов: для любых элементов."
#     elif letter == "а":
#         return "Ассоциати́вность — свойство бинарной операции, заключающееся в возможности осуществлять последовательное применение формулы в произвольном порядке к элементам."
#     elif letter == "д":
#         return "Дистрибути́вность — свойство согласованности двух бинарных операций, определённых на одном и том же множестве."
#     elif letter == "м":
#         return "правило де Мо́ргана — логические правила, связывающие пары логических операций при помощи логического отрицания."
#     else:
#         return "к - коммутативность\nа - ассоциативность\nд - дистрибутивность\nм - правило де Моргана"
# print(help_bool("м"))
# def to_dict(lst):
#     ju = {}
#     for i in lst:
#         ju[i] = i
#     return ju
# print(to_dict(["f","otr"]))


# my_dict = {"first_one": "we can do it"}
# def biggest_dict(**kwargs):
#     global my_dict
#     my_dict.update(**kwargs)
#     return my_dict
# print(biggest_dict(car="honda", kekv4="kekv3"))

# from collections import Counter
# def count_it(sequence):
#     b = Counter(sequence).most_common(3)
#     b= dict(b)
#     new_dict = {}
#     for key, value in b.items():
#         new_dict[int(key)] = value
#     return new_dict
# print(count_it("354637829"))
# a= {"bird": "red", "car": "honda", "plane": "broller", "kekv3": "kekv4", "pipel": "god"}
# first = list(a.values())[0]
# second = list(a.values())[-1]
# a[list(dct.keys())[0]] = second
# a[list(dct.keys())[-1]] = first
# del(a[list(a.keys())[1]])
# a["new_key"] = "new_value"
# print(a)
# def search_substr(subst,st):
#     if subst.lower() in st.lower():
#         return "Есть контакт!"
#     else:
#         return "Мимо!"
# print(search_substr("kv", "kekv3"))
# def first_last(letter, st):
#     a = (st.find(letter), st.rfind(letter))
#     return a
# print(first_last("kek","kekv3"))
# def top3(st):
#     a = Counter(st.replace(' ', '')).most_common(3)
#     return ', '.join([f'{letter} - {i}' for letter, i in a])
# print(top3("jgjvbbjnbrnn,fhjdkcdkjkcihc"))
# def camel(st):
#     st = st.lower()
#     st = list(st)
#     q = []
#     b = []
#     for i in range(len(st)):
#         if st[i] == "," or st[i] == "." or st[i] == "!" or st[i] == " " or st[i] == ":" or st[i] == "-":
#             q.append(i)
#             b.append(st[i])
#             st[i] = "#"
#     st = "".join(st).replace("#","")
#     st = list(st)
#     for i in range(len(st)):
#         if i % 2 == 0:
#             st[i] = st[i].upper()
#     st = "".join(st)
#     for i in range(len(q)):
#         st = st[:q[i]] + b[i] + st[q[i]:]
#     return st
# print(camel("hallo world"))
# def shortener(st):
#     while "(" in st or ")" in st:
#         a = st.rfind("(")
#         b = st.find(")", a)
#         st = st.replace(st[a:b + 1], "")
#     return st
# print(shortener("ke(vv(kekv)kvk)k3(v)k((v)kv)kke)"))
# def cleaned_str(st):
#     a= []
#     for s in st:
#         if s != '@':
#             ca.append(s)
#         elif s == '@' and a:
#             a.pop()
#     return ''.join(a)
# print(cleaned_str("kekekekekevv33"))


# # /////////////////////////////////////////////////////
# # /////////////////////////////////////////////////////
# /////////////////////////////////////////////////////



# def a_b (a,b):
#     ab= []
#     for i in range(len(a)):
#         tr = (a[i], b[i])
#         ab.append(tr)
#     return ab
# print(a_b([7,9,6],[6,9,7]))


# def hello(lst):
#     for i in range(len(lst)):
#         print("Привет {lst[i]}")
# hello(["Roma", "Ars", "kekv3"])


# def double(st):
#     for i in range(len(st)):
#         if st[i].lower() == st[i+1].lower():return True
#     return 0
# print(double("kammenn"))

# def without_space(a):
#     a= list(a)
#     if a[0] == " ":
#         a[0] = ""
#     if a[-1] == " ":
#         a[-1] = ""
#     a.append("0")
#     for i in range(len(aa)-1):
#         if a[i] == " " and a[i] == a[i+1]:
#             a[i] = ""
#         if a[i] == " " and a[i+1] == "." or a[i+1] == "," or a[i+1] == ":" or a[i+1] == "!":
#             a[i] = ""
#     a.pop()
#     return "".join(a)
# print(without_space(" hallow world   ,   were space? . "))


# def m(a, b):
#     return round(3.14*(b**2)*a*1000,2)
# print(m(0.87,0.08))


# def s(a):
#     a = a.split(", ")
#     b = 1
#     for i in range(len(a)):
#         b *= int(a[i])
#     return b
# print(s("9, 8, 7"))


# def v(a):
#     b = 0
#     for i in range(a):
#         x = int(input(f"Введите длину коробки {i+1} "))
#         y = int(input(f"Введите ширину коробки {i + 1} "))
#         z = int(input(f"Введите высоту коробки {i + 1} "))
#         b += x*y*z
#     return b
# print(v(3))



# def length(a,b):
#     return round(abs(((b["x"] - a["x"])**2 + (b["y"] - a["y"])**2)**0.5), 3)
# print(length({"x": 9, "y": 5},{"x": 7, "y": 4}))


# def language(a):
#     a = a.replace("е", "3")
#     a = a.replace("Е", "3")
#     a = a.replace("а", "4")
#     a = a.replace("А", "4")
#     return a
# print(language("wooo kekv3"))


# def up(lst):
#     a = []
#     for i in range(len(lst)):
#         a.append(sum(lst[:i]) + lst[i])
#     return a
# print(up([9,8,7,6,5,4,3,2,1]))


# def up_down(lst):
#     return "Возрастает" if lst[0] < lst[-1] else "Убывает"
# print(up_down([1,2,3,4,5]))


# def med(lst):
#     lst.sort()
#     a = len(lst)
#     if a % 2 == 0:
#         return (lst[a//2] + lst[a//2-1]) / 2
#     else:
#         return lst[a//2]
# print(med([3,4,4,5,6,4,7,1]))


# def device():
#     a = {1: "А", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I",
#           10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S",
#           20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
#     st = input("print world use only number ")
#     st = st.split(" ")
#     for i in range(len(st)):
#         st[i] = a[len(st[i])]
#     return "".join(st)
# print(device())


# def remake(st):
#     st = list(st)
#     for i in range(len(st)):
#         if st[i] == st[i].lower():
#             st[i] = st[i].upper()
#         else:
#             st[i] = st[i].lower()
#     st = st[::-1]
#     return "".join(st)
# print(remake(".Kekv3, keKV4, kEkV5"))

# def i_am_not_have_enemi(lst, enem):
#     for i in range(len(enem)):
#         if enem[i] in lst:
#             lst.remove(enem[i])
#     return lst
# print(i_am_not_have_enemi(["grisha", "ivan", "semen", "nikita", "kekv666", "ilya"], ["semen", "kekv666"]))




# # /////////////////////////////////////////////////////
# # /////////////////////////////////////////////////////
# /////////////////////////////////////////////////////




# def rock_paper_shears(a1, a2):
#     if a1 == "Камень" and a2 == "Ножницы": return "Первый игрок выйграл"
#     elif a1 == "Ножницы" and a2 == "Бумага": return "Первый игрок выйграл"
#     elif a1 == "Бумага" and a2 == "Камень": return "Первый игрок выйграл"
#     elif a1 == a2: return "Ничья"
#     else: return "Второй игрок выйграл"
# print(rock_paper_shears("ножницы", "камень"))


# def can_or_not(a):
#     if len(a) % 3 == 0: return "gud"
#     return "not gud"
# print(can_or_not(["kvk3", "kvk3", "kvk3", "kvk3", "kvk3"]))


# def do_not_shout(st):
#    st = list(st)
#    a = []
#    r = []
#    for i in range(len(st)):
#        if st[i] == "!" or st[i] == "?":
#            for y in range(len(st)-i):
#                if st[y+i] != "?" or st[y+i] != "?":
#                    break
#            a.append(i)
#    for i in range(len(a)-1):
#        if a[i] + 1 != a[i+1]:
#            a[i] = 0
#            r.append(i)
#    a = a[r[-1]+1:]
#    st = "".join(st)
#    if ("?" in st[a[0]:] and not "!" in st[a[0]:]) or ("!" in st[a[0]:] and not "?" in st[a[0]:]):
#        if st[a[0]:].find("?") > st[a[0]:].find("!"):
#            st = st[:a[0]] + "?"
#        elif st[a[0]:].find("?") < st[a[0]:].fiand("!"):
#            st = st[:a[0]] + "!"
#    if "?" in st[a[0]:] and "!" in st[a[0]:]:
#        if st[a[0]:].fiand("?") < st[a[0]:].find("!"):
#            st = st[:a[0]] + "?!"
#        elif st[a[0]:].find("?") > st[a[0]:].find("!"):
#            st = st[:a[0]] + "!?"
#    return st
# print(do_not_shout("hal?lo ??!world?!!!!"))

# def med(lst):
#     if sum(lst) > 21:
#         return True
#     else:
#         False
# print(med[98, 97])

# def plus_in_str(st):
#     a = 0
#     b = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#     c = []
#     for i in range(len(st)):
#         if st[i] in b:
#             c.append(st[i])
#         else:
#            c.append("0")
#     c = "".join(c)
#     c = c.split("0")
#     for i in range(len(c)):
#         if c[i] == "":
#             c[i] = "0"
#     for i in range(len(c)):
#         a += int(c[i])
#     return a
# print(plus_in_str("Kekvkekvkke343kdk"))

# def l(st):
#     a = st.replace("+", "")
#     b = 0
#     for i in range(1, len(st)-1):
#         if st[i] != "+" and st[i-1] == "+" and st[i+1] == "+":
#             b += 1
#     if len(a) == b:
#         return True 
#     else: False
# print(l("+k+v+kev+kk++v++"))


# def to_24(a):
#     if "pm" in a:
#         a = a.replace(" pm", "")a
#         time = a.split(":")
#         a = a.split(":")
#         if int(time[0]) + 12 == 24:
#             b = "00"
#         else:
#             b = str(int(time[0]) + 12)
#         a[0] = b
#         return ":".join(a)
#     else:
#         a = a.replace("am", "")
#     return a
# print(to_24("12:34 pm"))


# def check_pass(p):
#     a = 0
#     b = False
#     v = False
#     q = False
#     if len(p) >= 8:
#         a += 1
#     if "@" in p or "_" in p or "*" in p or "&" in p or "#" in p:
#        a += 1
#     for item in p:
#         try:
#             if int(item) in range(0,10):b = True
#         except ValueError:
#             if item == item.upper(): q = True
#             v = True
#     if b: a += 1
#     if v: a += 1
#     if q: a += 1
#     return f"{a} балла"
# print(check_pass("kekv_v45"))


# def from_int_to_str(integer):
#     a = len(str(integer))
#     nums = {"1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять", "6": "шесть", "7": "семь", "8": "восемь", "9": "девять",
#             "10": "десять", "11": "одиннадцать", "12": "двенадцать", "13": "тринадцать", "14": "четырнадцать", "15": "пятнадцать", "16": "шестнадцать", "17": "семнадцать", "18": "восемнадцать", "19": "девятнадцать",
#             "20": "двадцать", "30": "тридцать", "40": "сорок", "50": "пятьдесят", "60": "шестьдесят", "70": "семьдесят", "80": "восемьдесят", "90": "девяносто",
#             "100": "сто", "200": "двести", "300": "триста", "400": "четыреста", "500": "пятьсот", "600": "шестьсот", "700": "семьсот", "800": "восемьсот", "900": "девятьсот"}
#     b= ""
#     if str(integer) in nums:
#         return nums[str(integer)]
#     if integer == 0:
#         return "0"
#     if len(str(integer)) == a:
#         b += f"{nums[str(int(str(integer)[0])*(10**(a - 1)))]} "
#         integer = int(integer) % (10**(a - 1))
#         if str(integer) in nums:
#             b += nums[str(integer)]
#         else:
#             b += f"{nums[str(int(str(integer)[0]) * 10)]} "
#             integer = int(integer) % 10
#             b += nums[str(integer)]
#     return b
# print(from_int_to_str(678))

# def luck(a):
#     f = 0
#     for i in range(10**(a-1), 10**a):
#         lst = []
#         for a in str(i):
#             lst.append(int(a))
#         if len(lst) % 2 != 0:
#             q = len(lst) // 2
#             if sum(lst[:q]) == sum(lst[q+1:]):
#                 f += 1
#         else:
#             q = len(lst) // 2
#             if sum(lst[:q]) == sum(lst[q:]):
#                 f += 1
#     return f
# print(luck(3))

#   ████████████████████████████████████████████████████████████  
# ██                                                            ██
# ██              ██████    ██      ██    ██████                ██
# ██              ██        ████    ██    ██    ██              ██
# ██              ██████    ██  ██  ██    ██    ██              ██
# ██              ██        ██    ████    ██    ██              ██
# ██              ██████    ██      ██    ██████                ██
# ██                                                            ██
#   ████████████████████████████████████████████████████████████  
