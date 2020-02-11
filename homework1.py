import re

my_text = """Wyobraz sobie, ze ten tekst zawiera numer
KODU 94-348 twojej karty do bankomatu, a ty wlasnie go
zapomniales. Jak szybko go odnalezc 62-879?"""

def check_postal_code(text):
    path = r'\d\d\-\d\d\d'
    postal_code_list = re.findall(path, text)
    return postal_code_list


print(check_postal_code(my_text))


# version 2
# path = r'\d\d\-\d\d\d'
# match = re.search(path, my_text)
#
# if match:
#     number = match.group()
#     print(number)


# version 3
# def check_postal_code(text):
#     postal_code_list = []
#     path = r'\d\d\-\d\d\d'
#     match = re.search(path, text)
#     for code in text:
#         if match:
#             number = match.group()
#             postal_code_list.append(number)
#     return postal_code_list
#
#
# print(check_postal_code(my_text))





