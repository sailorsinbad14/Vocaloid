def detectLanguage(lang):
    language=''
    if(lang == 'ja'):
       language = 'JAPANESE'
    elif(lang =='zh'):
        language = 'CHINESE'
    elif(lang == 'en-US'):
        language = 'ENGLISH'
    else:
       language = "Cannot recognize this language..."
    print('LANGUAGE: ' + language)