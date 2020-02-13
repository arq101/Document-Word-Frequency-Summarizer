from collections import defaultdict
import os
import pytest

import document_word_counter as doc_wc


@pytest.fixture
def source_file_directory_path(tmpdir):
    doc1 = tmpdir.join('doc1.txt')
    doc1.write('The fundamentals to measure economic strength')
    doc2 = tmpdir.join('doc2.txt')
    doc2.write('The important engine of economic growth and strength')
    return str(tmpdir)


@pytest.fixture
def words_of_interest_file(tmpdir):
    words_of_interest = tmpdir.join('monitor_words.txt')
    words_of_interest.write('Economics\n'
                            'Strength\n'
                            'Fundamentals')
    return words_of_interest.strpath


class TestDocumentWordCounter(object):

    def test_get_files_to_be_read(self, source_file_directory_path):
        files_list = doc_wc.get_files_to_be_read(dir_path=source_file_directory_path, file_ext='txt')
        expected_files = [os.path.join(source_file_directory_path, 'doc1.txt'),
                          os.path.join(source_file_directory_path, 'doc2.txt')]
        assert set(files_list) == set(expected_files)

    def test_get_files_to_be_read_invalid_extension_format(self, source_file_directory_path):
        with pytest.raises(ValueError):
            doc_wc.get_files_to_be_read(dir_path=source_file_directory_path, file_ext='..jpeg')

    def test_produce_word_summary(self, source_file_directory_path):
        input_files = [os.path.join(source_file_directory_path, 'doc1.txt'),
                       os.path.join(source_file_directory_path, 'doc2.txt')]
        words_found = doc_wc.produce_word_summary(data_files=input_files)

        expected_word_summary = defaultdict(lambda: {})
        expected_word_summary['The'] = {
            'count': 2, 'docs': ['doc1.txt', 'doc2.txt'],
            'sentences': ['The fundamentals to measure economic strength',
                          'The important engine of economic growth and strength']}
        expected_word_summary['Fundamentals'] = {
            'count': 1, 'docs': ['doc1.txt'],
            'sentences': ['The fundamentals to measure economic strength']}
        expected_word_summary['To'] = {
                'count': 1, 'docs': ['doc1.txt'],
                'sentences': ['The fundamentals to measure economic strength']}
        expected_word_summary['Measure'] = {
                'count': 1, 'docs': ['doc1.txt'],
                'sentences': ['The fundamentals to measure economic strength']}
        expected_word_summary['Economic'] = {
                'count': 2, 'docs': ['doc1.txt', 'doc2.txt'],
                'sentences': ['The fundamentals to measure economic strength',
                              'The important engine of economic growth and strength']}
        expected_word_summary['Strength'] = {
                'count': 2, 'docs': ['doc1.txt', 'doc2.txt'],
                'sentences': ['The fundamentals to measure economic strength',
                              'The important engine of economic growth and strength']}
        expected_word_summary['Important'] = {
                'count': 1, 'docs': ['doc2.txt'],
                'sentences': ['The important engine of economic growth and strength']}
        expected_word_summary['Engine'] = {
                'count': 1, 'docs': ['doc2.txt'],
                'sentences': ['The important engine of economic growth and strength']}
        expected_word_summary['Of'] = {
                'count': 1, 'docs': ['doc2.txt'],
                'sentences': ['The important engine of economic growth and strength']}
        expected_word_summary['Growth'] = {
                'count': 1, 'docs': ['doc2.txt'],
                'sentences': ['The important engine of economic growth and strength']}
        expected_word_summary['And'] = {
                'count': 1, 'docs': ['doc2.txt'],
                'sentences': ['The important engine of economic growth and strength']}
        assert sorted(list(expected_word_summary.keys())) == sorted(list(words_found.keys()))
        assert words_found['Economic']['count'] == expected_word_summary['Economic']['count']
        assert words_found['Economic']['sentences'] == expected_word_summary['Economic']['sentences']
        assert words_found['Economic']['docs'] == expected_word_summary['Economic']['docs']

    def test_get_words_of_interest(self, words_of_interest_file):
        words_to_scan = doc_wc.get_words_of_interest(file_path=words_of_interest_file)
        expected_words = ['Economics', 'Strength', 'Fundamentals']
        assert set(words_to_scan) == set(expected_words)

    def test_print_tabulated_word_count_summary(self):
        # TODO ran out of time
        pass
