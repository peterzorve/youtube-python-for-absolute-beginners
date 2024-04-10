# Next, let us look at another method. Here, we will just shuffle the text. 

def encryption_shuffle(text):
    text_length = len(str(text))
    first_part, second_part = "", "" # After shuffling, we want to split it into two parts. Just adding a bit of complexity to the code
    for i in range(text_length):
        if i % 2 == 0: 
            first_part = first_part + text[i]
        else: 
            second_part = second_part + text[i]
    shuffle_text = first_part.lower()[::-1] + "y.yo.b##" + second_part.lower()[::-1] # I added "y.yo.b##" in between to be able to identify the first part from the second part during decryption
                                                                                     # [::-1] allows me to reverse each part. It adds complexity to the encryption
    return shuffle_text


# Now let us decrypt the previous the text 
def decryption_shuffle(text):
    if "y.yo.b##" in text: 
        text = text.split("y.yo.b##") # I am using this to split the encryted file into to 
        first_part = text[0][::-1]
        second_part = text[1][::-1]
        decrypted_text = ""
        for i in range(len(second_part)):
            decrypted_text = decrypted_text + first_part[i] + second_part[i]

        # There is the possibility that the length of the first_part will be one more than that 
        # of the second part if the length of original text is an odd number. 
        # This will end up removing the last letter in the first_part. 
        # Let's fix that 

        if len(first_part) != second_part: 
            decrypted_text = decrypted_text + first_part[-1]
        return decrypted_text
    else: 
        return None
     

def caesar_cipher_encryption(text, shift_number): 
    text = str(text).lower() # Convert everything to lowercase
    base = ord("a")
    result = ""
    for character in text: 
        if character.isalpha():
            new_ord = ord(character) + shift_number     # This shifts the each character by shift_number
            new_ord = (new_ord - base) % 26 + base
            new_character = chr(new_ord) 
            result = result + new_character
        else: 
            result = result + character
    # print(result)    
            
    return result 


def caesar_cipher_decryption(text, shift_number): 
    shift_number = -abs(shift_number)
    text = str(text).lower() # Convert everything to lowercase
    base = ord("a")
    result = ""
    for character in text: 
        if character.isalpha():
            new_ord = ord(character) + shift_number     # This shifts the each character by shift_number
            new_ord = (new_ord - base) % 26 + base
            new_character = chr(new_ord) 
            result = result + new_character
        else: 
            result = result + character  
            
    return result 


