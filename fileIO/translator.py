from translate import Translator

translator = Translator(to_lang = 'fr')

try:
    with open ('test_translate.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        # print(translation)
        with open('./translated.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileExistsError as err:
    print('Please check the file path')