from collections import Counter
import os

def create_even_occurrence_list(input_file):
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}_output.txt"

    try:
        with open(input_file, 'r') as file:
            input_data = file.read()
            input_list = [int(item) for item in input_data.replace(',', ' ').split()]

        occurrence_count = Counter(input_list)

        # occurrence_count = {}
        # for item in input_list:
        # if item is occurrence_count:
        # occurrence_count[item] += 1
        # else:
        # occurrence_count[item] = 1

        result_list = []
        added_elements = set()

        for item in reversed(input_list):
            if occurrence_count[item] % 2 == 0 and item not in added_elements:
                result_list.append(item)
                added_elements.add(item)

        with open(output_file, 'w') as file:
            result_list_str = ', '.join(map(str, result_list))
            file.write(result_list_str)

        print(f"Результат записан в файл: {output_file}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
    except IOError:
        print("Ошибка ввода-вывода при работе с файлами.")
    except ValueError:
        print("Ошибка: Во входных данных присутствуют нечисловые значения.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

input_file = 'example1.txt'

create_even_occurrence_list(input_file)
