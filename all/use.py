from mmk import FileTxt
import pandas as pd
import matplotlib.pyplot as plt


def check_file(file_path):
    file_extension = file_path.split('.')[-1].lower()
    try:
        if file_extension == 'txt':
            return FileTxt(file_path)
    except FileNotFoundError:
        print("Файл не найден")

def results(a):
    try:
        # Write the results to a text file
        with open('files/results.txt', 'w') as result_file:
            word_uniq, chars_numb, words_num, sentences_numb = FileTxt(a).read_file()

            result_file.write(f"Total Characters: {chars_numb}\n")
            result_file.write(f"Total Words: {words_num}\n")
            result_file.write(f"Total Sentences: {sentences_numb}\n")
            result_file.write(f"Unique Words Lenght: {len(word_uniq)}\n")
            try:
                result_file.write(f"Average sentence length: {int(words_num) / int(sentences_numb)} \n")
            except ZeroDivisionError:
                result_file.write('предложений нет')

            dfr = pd.read_csv('files/unic_items.csv')

            result_file.write(f"Average word length: {round(dfr['word_lenght'].mean(), 2)}\n")


            result_file.write(f"Longest Word: {dfr.loc[dfr['word_lenght'].idxmax()]['item']}")
            result_file.write(f"Shortest Word: {dfr.loc[dfr['word_lenght'].idxmin()]['item']}")


    except FileNotFoundError:
        return 'такого файла нееет'


def top_10_words(df):
    top_10_words = df.sort_values(by='count', ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    plt.bar(top_10_words['item'], top_10_words['count'])
    plt.title('Top 10 Most Frequent Words')
    plt.savefig(r'files\top_10_words.png', dpi=400)
    plt.show()


def top_10_chars(df):
    chars = df.sort_values(by='letter_count', ascending=False).head(10)
    # plt.style.use('_mpl-gallery')
    plt.bar(chars['letter'], chars['letter_count'])
    plt.title('Top 10 chars')
    plt.savefig(r'files\top_10_chars.png', dpi=400)
    plt.show()



if __name__ == "__main__":
    print('Введите путь файла без кавычек')
    file = input() # Enter file here
    # file = r"data/a.txt"  # тут файл
    #r'data/Vy-prizvali-nie-togho_.-Knigha-Timur-Askarovich-Aitbaiev.txt'

    file_obj = check_file(file)

    if file_obj:
        if isinstance(file_obj, FileTxt):
            file_obj.read_file()
            results(file_obj.file_path)
    else:
        print('выберите другой файл')
    df = pd.read_csv(r'files/unic_items.csv')
    top_10_words(df)
    top_10_chars(df)
    # print(df.head())
