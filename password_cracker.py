import hashlib

def crack_sha1_hash(hash, use_salts = False):

    with open('top-10000-passwords.txt', 'r') as passwords:
        for passwordPlain in passwords:
            passwordPlain = passwordPlain.strip()
            if use_salts:
                with open('known-salts.txt', 'r') as salts:
                    for salt in salts:
                        salt = salt.strip()
                        passwordPlainSalted1 = f"{salt}{passwordPlain}"
                        passwordPlainSalted2 = f"{passwordPlain}{salt}"
                        passwordHashed1 = hashlib.sha1(passwordPlainSalted1.encode()).hexdigest()
                        passwordHashed2 = hashlib.sha1(passwordPlainSalted2.encode()).hexdigest()
                        if passwordHashed1 == hash or passwordHashed2 == hash:
                            #print(f"FOUND FOR {passwordPlain}")
                            return passwordPlain
            else:
                passwordHashed = hashlib.sha1(passwordPlain.encode()).hexdigest()
                if passwordHashed == hash:
                    #print(f"FOUND FOR {passwordPlain}")
                    return passwordPlain
            
    return "PASSWORD NOT IN DATABASE"