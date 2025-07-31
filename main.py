from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

new_list = []
result_list = []

pattern = r"(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?"
replace = r"+7(\2)\3-\4-\5\7\8\9"


def directory():

  for i in contacts_list:
    result_name = ' '.join(i[:3]).split(' ')
    if result_name[2] == '':
      del result_name[2]   #result_name[:] = [item for item in result_name if item]
      print(result_name)
      result_contact = [result_name[0], result_name[1], result_name[2], i[3], i[4], re.sub(pattern, replace, i[5]), i[6]]
      new_list.append(result_contact)
    else:
      result_contact = [result_name[0], result_name[1], result_name[2], i[3], i[4], re.sub(pattern, replace, i[5]), i[6]]
      new_list.append(result_contact)


def remove_duplicates():
  for contact in new_list:
    last_name = contact[0]
    first_name = contact[1]
    for new_contact in new_list:
      new_last_name = new_contact[0]
      new_first_name = new_contact[1]
      if first_name == new_first_name and last_name == new_last_name:
        if contact[2] == '':
           contact[2] = new_contact[2]
        if contact[3] == '':
          contact[3] = new_contact[3]
        if contact[4] == '':
          contact[4] = new_contact[4]
        if contact[5] == '':
          contact[5] = new_contact[5]
        if contact[6] == '':
          contact[6] = new_contact[6]

  for i in new_list:
    if i not in result_list:
       result_list.append(i)
  return result_list


if __name__ == '__main__':
  directory()
  remove_duplicates()

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(result_list)