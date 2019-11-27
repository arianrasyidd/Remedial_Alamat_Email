def inputEmail():
    email = input('Input email: ')
    emailLower = email.lower()
    emailReplace = emailLower.replace('@','.')
    emailSplit = emailReplace.split('.')

    if len(emailSplit) != 3:
        return 'Hasil : EMAIL TIDAK VALID'

    else:
        namaUser = emailSplit[0]
        namaHosting = emailSplit[1]
        ekstensi = emailSplit[2]

        if ekstensi.isalpha() == False or len(ekstensi) > 5:
            return 'Hasil : EMAIL TIDAK VALID'    
        
        else:
            if namaHosting.isalnum() == True:
                if namaUser.isalnum() == True or '_' in namaUser or '-' in namaUser:
                    return 'Hasil : EMAIL VALID'
                else:
                    return 'Hasil : EMAIL TIDAK VALID'
            else:
                return 'Hasil : EMAIL TIDAK VALID'


print(inputEmail())