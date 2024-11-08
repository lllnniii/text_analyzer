import re
import io
from collections import Counter
import pandas as pd


class FileTxt():

    def __init__(self, file_path):
        self.file_path = file_path

    '''I have one method that  does everything(sorry)'''

    def read_file(self):
        try:
            with io.open(self.file_path, 'r', encoding='utf-8') as ffile:

                ref = ffile.read()

                chars_numb = len(ref)  # All chars (with spaces, etc.)

                words = re.findall(r'\b\w+\b', ref.lower())
                words_num = len(words)  # Number of all words
                sent = re.split(r'[.!?;\n]', ref)
                sentences_numb = len(sent) - 1  # Count all sentences.

                '''Then we need a dictionary with all the unique words'''
                word_uniq = Counter(words)

                '''the same with the alphabet'''

                letters_count = Counter()
                letters_count.update(ref.lower())

                '''Then i used pandas to save it as csv and do some graphs'''
                df1 = pd.DataFrame(list(word_uniq.items()), columns=['item', 'count'])
                df1['word_lenght'] = df1['item'].str.len()

                df2 = pd.DataFrame(list(letters_count.items()), columns=['letter', 'letter_count'])

                merged_df = pd.merge(df1, df2, left_index=True, right_index=True, how='left')
                merged_df.to_csv(r'files/unic_items.csv', index=False)

                return word_uniq, chars_numb, words_num, sentences_numb
                #merged_df['word_lenght'].mean()
        except FileNotFoundError:
            return 'такого файла нееет'

    def write_file(self):  # Rewrite txt
        try:
            with open(self.file_path, 'w') as ffile:
                a = ffile.write(input())
                return a
        except FileNotFoundError:
            return 'такого файла нееет'

    def add_in_file(self):
        try:
            with open(self.file_path, 'a+') as ffile:  # Add new sentences
                ffile.seek(0)
                data = ffile.read(100)
                if len(data) > 0:
                    ffile.write('\n')

            with open(self.file_path, 'r') as ffile:
                strings = ffile.readlines()

            strings.insert(int(input('Введите строку ')) - 1, input('ТЕКСТ ') + '\n')
            newlines = ''.join(strings)

            with open(self.file_path, 'w') as ffile:
                a = ffile.write(newlines)
                return a
        except FileNotFoundError:
            return 'такого файла нееет'

    def delete_data(self):  # Deletes the string
        try:
            with open(self.file_path, 'r') as ffile:
                strings = ffile.readlines()

            del strings[int(input('строка для удаления ')) - 1]
            newlines = ''.join(strings)

            with open(self.file_path, 'w') as ffile:
                a = ffile.write(newlines)
                return a
        except FileNotFoundError:
            return 'такого файла нееет'