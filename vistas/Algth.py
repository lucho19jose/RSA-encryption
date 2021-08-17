import random


def mcd(a, b):
    '''Calcula el maximo comun divisor de dos numeros a y b'''
    while a:
        a, b = b % a, a
    return b


def modinv(n, phi):
    '''calcula el inverso del modulo s de dos numeros n y phi'''
    def egcd(n, b):
        if n == 0:
            return (b, 0, 1)
        g, y, x = egcd(b % n, n)
        return (g, x - (b//n) * y, y)
    g, x, y = egcd(n, phi)
    if g != 1:
        raise Exception('No hay inverso del módulo')
    return x % phi


def rabinMiller(num):
    '''Comprueba si un numero num es probablemente primo'''
    if num % 2 == 0:
        return False
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    for pruebas in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)

        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v**2) % num
    return True


def generaClaves(tamano=1024):
    '''devuelve una tupla con un par de claves privada y  clave publica ((n,e),(n,d)) utilizando primos del orde nde 2**tamano
    debe generar dos archivos uno de clave publica u otro de privado
    '''
    p = getPrimo(tamano)
    q = getPrimo(tamano)
    n = p*q
    phi = (p-1)*(q-1)

    e = 2
    while(True):
        # e = getPrimo(tamano)   es coprimo con phi   mcd(n,phi) = 1
        if mcd(e, phi) == 1:
            break
        e += 1

    # d es el inverso del modulo de n y phi cumple que n.s mod phi = 1
    d = modinv(e, phi)

    clavePublica = (n, e)
    clavePrivada = (n, d)
    Pk = open("PublicKey.txt", "w+")
    Pk.write(convertTuplein(clavePublica))
    Pk.close()
    PrK = open("PrivateKey.txt", "w+")
    PrK.write(convertTuplein(clavePrivada))
    PrK.close()
    return (clavePublica, clavePrivada)


def cifra(textoClaro, clavePublica, textoCifrado=""):
    '''lee un archivo de texto textoClaro y lo cifra con la clavePublica del receptor, formando bloques de n bytes y lo guarda en textoCifrado'''
    n, key = clavePublica
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [str(pow(ord(char), int(key), int(n))) for char in textoClaro]
    print(cipher)
    Pk = open("cipher.txt", "w+", encoding="utf8")
    Pk.write(" ".join(cipher))  # ...
    Pk.close()
    # Return the array of bytes
    return cipher


def descifra(textoCifrado, clavePrivada, textoClaro=""):
    '''lee un archivo de texto textoCifrado y lo descifra con la clavePrivada del receptor, formando bloques de n bytes y lo guarda en textoClaro'''
    # Unpack the key into its components
    n, key = clavePrivada
    n = int(n)
    key = int(key)
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr(pow(int(char), key, n)) for char in textoCifrado]
    # Return the array of bytes as a string
    decryptedFile = open("Decrypter.txt", "w+", encoding="utf8")
    decryptedFile.write(" ".join(plain))  # ...
    decryptedFile.close()
    return ''.join(plain)


def getPrimo(tam):
    while(True):
        num = random.randint(2**tam, 2**(tam+1))
        if(rabinMiller(num)):
            return num


def convertTuplein(tup):
    string = ''.join(str(tup))
    return string


def convertTupleout(tup):
    intTup = int(tup)
    return intTup


##### ESTA PARTE ES SOLO UN EJEMPLO DE COMO FUNCIONA EL ALGORITMO  ###########
""" claves = generaClaves(2048) """
