# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def get_dict_of_names(names):
    first_letter_dict = {}
    for name in sorted(names):
        first_letter = name[0]
        if first_letter not in first_letter_dict:
            first_letter_dict[first_letter] = []
        first_letter_dict[first_letter].append(name)
    return first_letter_dict

names = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
print(get_dict_of_names(names))