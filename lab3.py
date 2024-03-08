#zadanie 1

list = [i+1 for i in range(10)]

list_a = list[0:5]
list_b = list[5:10]

concat_list = list_a + list_b

# zadanie 2

concat_list.insert(0, 0)
copy_list = concat_list.copy()
copy_list.sort(reverse=True)
print(copy_list)


# zadanie 3
string = input()
sorted(set(string.lower()))


# zadanie 4

miesiace = {
    1: 'styczen',
    2: 'luty',
    3: 'marzec',
    4: 'kwiecien',
    5: 'maj', 
    6: 'czerwiec',
    7: 'lipiec',
    8: 'sierpien',
    9: 'wrzesien',
    10: 'pazdziernik',
    11: 'listopad', 
    12: 'grudzien'
}

# zadanie 5

miesiace_ang = {
    1: 'january',
    2: 'february',
    3: 'march',
    4: 'april',
    5: 'may', 
    6: 'june',
    7: 'july',
    8: 'august',
    9: 'september',
    10: 'october',
    11: 'november', 
    12: 'december'
}

months = {
    'pl': miesiace,
    'en':miesiace_ang
}


# zadanie 6
string = 'Marianna'
value = 1
dict = dict.fromkeys(set([*string]), value)

# zadanie 7

import string
str = input()
cnt = 0
for i in str:
    if i in string.ascii_lowercase:
        cnt += 1
    elif i in string.digits:
        cnt += 1
result = cnt/len(str)
print(result)
