import json
import os

def load_and_prepare_translit_dict(translit_dict_path='translit_dict.json'):
    with open(translit_dict_path, 'r', encoding='utf-8') as file:
        translit_dict = json.load(file)

    prepared_dict = {}
    for key, value in translit_dict.items():
        prepared_dict[key.lower()] = value.lower()
        prepared_dict[key.upper()] = value.capitalize()

    return prepared_dict

def transliterate_russian_to_english(text, translit_dict):
    transliterated_text = "".join([translit_dict.get(char, char) for char in text])
    return transliterated_text


def transliterate_file(input_file_name, translit_dict):
    base_name, _ = os.path.splitext(input_file_name)
    output_file_name = f"{base_name}_output.txt"

    with open(input_file_name, 'r', encoding='utf-8') as input_file, \
            open(output_file_name, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            transliterated_line = transliterate_russian_to_english(line.strip(), translit_dict)
            output_file.write(transliterated_line + '\n')
    print(f"Транслитерированный текст записан в {output_file_name}")

translit_dict = load_and_prepare_translit_dict()

input_file_name = 'input1.txt'

transliterate_file(input_file_name, translit_dict)
