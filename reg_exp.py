import csv
import re

with open('phonebook_raw.csv') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def contacts(contact_list: list):
    new_list = list()
    name_list = list()
    for item in contact_list:
        name = ' '.join(item[0:3]).split(' ')
        result = [name[0], name[1], name[2], item[3], item[4],
                  re.sub('(8|\+?7)\s*(\(*)([0-9]{3})(\)*)(\s*|\-*)([0-9]{3})(\s*|\-*)([0-9]{2})(\s*|\-*)([0-9]{2})\s*'
                         '(\(*)([а-я]{3}\.)*\s*(\d{4})*(\))*', r'+7(\3)\6-\8-\10 \12\13', item[5]),
                  item[6]]
        if ' '.join(result[0:2]).strip() in name_list:
            i = name_list.index(' '.join(result[0:2]).strip())
            for j in range(2, 7):
                if result[j].strip() not in new_list[i][j]:
                    new_list[i][j] = (new_list[i][j] + ' ' + result[j]).strip()
        else:
            name_list.append(' '.join(result[0:2]).strip())
            new_list.append(result)
    return new_list


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts(contacts_list))
