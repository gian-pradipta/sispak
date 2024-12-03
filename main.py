import json
import json
from naive_bayes import *
import csv

with open('dataset.csv', 'r') as csvfile:
    kamus1 = []
    csv_reader = csv.reader(csvfile)
    line_number = 0
    for line in csv_reader:
        if line_number == 0:
            params = line
        else:
            kamus = dict()
            for i in range(len(params)):
                kamus[params[i]] = line[i]
            kamus1.append(kamus)
        line_number += 1

def seperate_based_on_class(data: list, target: str) -> list:
    class_seperated : dict = {}
    for x in data:
        if x[target] not in class_seperated:
            class_seperated[x[target]] = [x]
        else:
            class_seperated[x[target]].append(x)
    return class_seperated


def get_dataset() -> list:
    global kamus1
    def change_temp_c(data):
        data["temp_c"] = float(data["temp_c"].replace(",","."))
        if data["temp_c"] > 38:
            data["temp_c"] = "yes"
        else:
            data["temp_c"] = "no"
        return data
    def del_pid(data):
        del data["p_i_d"]
        return data
    def del_f(data):
        del data["current_temp"]
        return data

    kamus1 = list(map(change_temp_c, kamus1))
    kamus1 = list(map(del_pid,kamus1))
    kamus1 = list(map(del_f,kamus1))

    return kamus1

def print_cantik(hashmap) -> None:
    pretty_dict = json.dumps(hashmap, indent=4)
    print(pretty_dict)


def main() -> None:
    dataset : list = get_dataset()
    data = seperate_based_on_class(dataset, "dengue")



    new_case = {
        "temp_c": "yes",
        "pain_behind_the_eyes": "no",
        "metallic_taste_in_the_mouth": "no",
        "appetite_loss": "yes",
        "addominal_pain": "no",
        "nausea_vomiting": "yes",
        "diarrhoea": "no",
    }

    result = do_naive_bayes(data, new_case )
    print_cantik(result)

if __name__ == "__main__":
    main()