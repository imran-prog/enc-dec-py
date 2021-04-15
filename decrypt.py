# The Encryption Function
def cipher_encrypt(plain_text, key):

    encrypted = ""

    for c in plain_text:

        if c.isupper(): #check if it's an uppercase character

            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a') 

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_new = (int(c) + key) % 10

            encrypted += str(c_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted

# The Decryption Function
def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper(): 

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower(): 

            c_index = ord(c) - ord('a') 

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted

_text = " M eq Mqver Eofev. M pmziw mr Mwpeqefeh erh M aerx xs xs nsmr xli fmk kmerxw pmoi csy xs mrgviewi qc hexefewi sj orsapihki. M aerx xs ibgip amxl kviex kycw pmoi csy, erh qeoi qcwipj gsqjsvxefpi mr qeomrk qc hvieqw e viepmxc. M eq e Tcxlsr Hizipstiv erh ger hs qygl xlmrkw amxl mx pmoi Wgvetmrk, Aif erh Wsjxaevi hizipstqirx, QP, EM erh Hexe Wgmirgi. Fc xli aec M eq epws e Neze erh G/G++ hizipstiv fyx rsx sr qewxiv pizip cix. M ger gviexi Ettw, hs eyxsqexmsr sj Wcwxiq erh fymph Wqevx Ettpmergiw, erh ywmrk G++ M eq xvcmrk xs pievr hizipstmrk Wsjxaevi'w erh KYM'w. M wxevxih qc geviiv amxl Aif Hizipstqirx xlex'w alc, csy orsa alex M eq xvcmrk xs wec. Erh sri pewx xlmrk qc kviexiwx womppw sj epp mw xlex M eq kssh Tvsfpiq Wspziv erh kssh Wievgliv sj Mrxivrix almgl qeoiw qi alex M eq vmklx rsa. Sl xlmrk epws M eq epws kssh mr zivwmsr gsrxvsp wcwxiqw xss."

ciphertext = cipher_decrypt(_text, 4)

print(ciphertext)
