import nltk
nltk.download('words')

english_words = nltk.corpus.words.words()

def encrypt(str, key):
    """
    Input:
         text to be encrypted
         key of the caesar cypher
    Output: Encrypted text
    """
    
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted = ''
    str = str.lower()
    for char in str:
        if char == " " :
              encrypted += " "
              continue
        if char == "," or char == "." or char == "#" or char == ";" or char == "&":
           continue
        index = alphabet.index(char)
        shifted_text = (index + key) % 26
        encrypted += alphabet[shifted_text]

    return encrypted


def decrypt(encrypted_text, key):
    """
    Input:
         text to be deccrypted
         key of the caesar cypher
    Output: deccrypted text
    """
    return encrypt(encrypted_text, -1*key)


def hack(sentence):
    """
    try to get the decrypted text 
    with the correct key
    """
    word_arr = []
    count_arr = []
    key_arr=[]
    round = 0
    while round < 27 :
        decrypt_text = decrypt (sentence,round)
        counter = 0
        words = decrypt_text.split()
        text=""
        for word in words:
            if word in english_words or word.lower() in english_words or word.upper() in english_words:
                counter += 1
            text += word
            text += " "
        word_arr.append(text[:-1])
        count_arr.append(counter)
        key_arr.append(round)
        m = max(count_arr)
        maxIndex = count_arr.index(m)
        round +=1
        
        
    return  word_arr[maxIndex] ,'key : '+ str(key_arr[maxIndex])



print(encrypt("home sweet home",2))
print(hack("jqog uyggv jqog"))
print(encrypt("my name is aya",5))
