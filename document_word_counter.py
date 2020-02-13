#!/usr/bin/env python

from collections import Counter, defaultdict
import glob
import os
import re
from beautifultable import BeautifulTable


INPUT_SRC_DOCS_DIR_PATH = './input_test_docs'
WORDS_OF_INTEREST_FILE = './words_of_interest/words_of_interest_1.txt'


def get_files_to_be_read(dir_path, file_ext):
    """Function finds files in a given directory that match the extension.

    :returns: list of full file paths
    """
    # get the file extension characters only, don't care about any given prefixes
    if re.fullmatch(r'\*?\.?([A-Z]+)', file_ext, flags=re.IGNORECASE):
        file_ext = re.fullmatch(r'\*?\.?([A-Z]+)', file_ext, flags=re.IGNORECASE).group(1)
        file_ext_pattern = '*.' + file_ext
    else:
        raise ValueError('File extension is in invalid format! \n'
                         'Expected format eg.: txt, .jpeg, *.png')

    # set up a wildcard for the file name with the given file extension
    # glob returns a list of full file paths matching the wildcard
    path_name = os.path.join(dir_path, file_ext_pattern)
    files_to_be_read = glob.glob(path_name)
    return files_to_be_read


def produce_word_summary(data_files):
    """Function responsible for producing the summary of words found in the documents that were scanned.

    Produces a count of each word,
    the document in which that word appeared
    and the sentences in which that word appeared.

    :returns: dict summary of words
    """
    word_summary = defaultdict(lambda: {})
    for file_path in data_files:
        with open(file_path, 'r') as fh:
            _, _sep, filename = file_path.rpartition('/')

            # since source files are small, read all lines at once
            all_lines = fh.readlines()

            # remove any punctuation marks within a line and then get the words ...
            all_words = [word.title() for line in all_lines for word in re.sub(r'[^\w]', ' ', line).split()]
            word_counts = Counter(all_words)
            all_sentences = [s.strip() for line in all_lines for s in line.split('.')]

            for word, count in word_counts.items():
                # for the word that has been counted, find the sentences in which it appears for the current file
                sentences_with_word = [s for s in all_sentences if word.lower() in s.lower()]

                #
                # example of the word_summary data structure
                #
                # word_summary = {
                #     'Alpine': {
                #         'count':        2,
                #         'docs':         ['doc1.txt', 'doc2.txt'],
                #         'sentences':    ['Welcome to The Alpine Club.', 'The Alpine Club was established in 1850']
                #     },
                #     ...
                # }
                #

                try:
                    word_summary[word]['count'] = word_summary[word]['count'] + count
                except KeyError:
                    word_summary[word]['count'] = count

                try:
                    word_summary[word]['sentences'].extend(sentences_with_word)
                except KeyError:
                    word_summary[word]['sentences'] = sentences_with_word

                try:
                    word_summary[word]['docs'].append(filename)
                except KeyError:
                    word_summary[word]['docs'] = [filename]

    return word_summary


def get_words_of_interest(file_path):
    """Reads a file containing a subset of words already extracted, deemed to be of interest.

    :returns: list of words
    """
    with open(file_path, 'r') as fh:
        lines = fh.readlines()
    words = [word.strip().title() for word in lines]
    return words


def print_tabulated_word_count_summary(data_dict, words_of_interest=None):
    """Prints the word summary in tabulated format to the terminal.

    :returns: None
    """
    # NOTE:
    # after experimenting with several tabulating libraries, settled on BeautifulTable.
    # This was the only one I found where the content fit inside the terminal screen without mis-aligning the output.
    table = BeautifulTable(max_width=160)
    table.column_headers = ['Word', 'Count', 'Documents', 'Sentences containing the word']

    if words_of_interest:
        # only tabulate the words of interest
        for key_word in words_of_interest:
            table.append_row(
                [
                    key_word,
                    data_dict[key_word]['count'],
                    ' '.join(data_dict[key_word]['docs']),
                    ' |\n'.join(data_dict[key_word]['sentences'])
                ]
            )
    else:
        # this adds all the words found from the documents and tabulates them
        for key, value in data_dict.items():
            table.append_row(
                [
                    key,
                    value['count'],
                    value['docs'],
                    ' |\n'.join(value['sentences'])
                ]
            )
    table.set_style(BeautifulTable.STYLE_BOX)
    table.column_alignments['Sentences containing the word'] = BeautifulTable.ALIGN_LEFT
    print(table)
    return None


def main():
    files_list = get_files_to_be_read(dir_path=INPUT_SRC_DOCS_DIR_PATH, file_ext='.txt')
    summary_results = produce_word_summary(data_files=files_list)
    interesting_words = get_words_of_interest(file_path=WORDS_OF_INTEREST_FILE)
    print_tabulated_word_count_summary(data_dict=summary_results, words_of_interest=interesting_words)
    # print_tabulated_word_count_summary(data_dict=summary_results)   # prints all the words found


if __name__ == '__main__':
    main()
