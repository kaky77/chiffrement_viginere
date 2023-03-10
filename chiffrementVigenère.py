
def encryp_vigenaire(text,key):
    indice_key = 0
    encrypt_text = ""
    # parcourons le texte 
    for i in range(0,len(text)):
        if 'A'<= text[i]<='Z':
            # decalage puis sommation de l'indice de caractère du text avec la key 
            # l'indice est compris de 0 - 25 d'où le calcul du modulo
            encrypt_text += chr((((ord(text[i])-ord('A')) + (ord(key[indice_key])-ord('A')))%26)+ord('A'))
            #incrémentons l'indice de la key sans qu'il ne depasse la taille de la key
            indice_key = (indice_key + 1)% len(key)
        else:
            encrypt_text += text[i]
    return encrypt_text

def decryp_vigenaire(text,key):
    indice_key = 0
    encrypt_text = ""
    # parcourons le texte 
    for i in range(0,len(text)):
        if 'A'<= text[i]<='Z':
            # decalage puis sommation de l'indice de caractère du text avec la key 
            # l'indice est compris de 0 - 25 d'où le calcul du modulo
            encrypt_text += chr((((ord(text[i])-ord('A')) - (ord(key[indice_key])-ord('A')))%26)+ord('A'))
            #incrémentons l'indice de la key sans qu'il ne depasse la taille de la key
            indice_key = (indice_key + 1)% len(key)
        else:
            encrypt_text += text[i]
    return encrypt_text


#-----------------Main-------------
var1 = encryp_vigenaire('BONJOUR A TOUS','MAISON')
with open("text-chiffrer.txt", "w+") as text_file:
    text_file.write(var1)

var2 = decryp_vigenaire(var1,'MAISON')
with open("text-Clair.txt", "w+") as text_file:
    text_file.write(var2)