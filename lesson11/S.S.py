# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# smb = ["{", "}", ",", "!", "?", " ", "."]
# sh_end = False
# while not sh_end:
#     txt = input("Введите слово: ")
#     txt = list(txt)
#     shift = int(input("Введите сдвиг: "))
#
#
#     cp_txt = ""
#     for ltr in txt:
#         if ltr == "":
#             cp_txt += ltr
#         else:
#             pst = alphabet.index(ltr)
#             if pst + shift > len(alphabet):
#                 nw_pst = pst + shift - len(alphabet)
#             elif pst + shift <0:
#                 nw_pst = pst + shift + len(alphabet)
#             else:
#                 nw_pst = pst + shift
#             cp_txt += alphabet[nw_pst]
#     print(cp_txt)






