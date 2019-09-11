import csv

a = ["ЗВ", "Тер", "ИИ", "Дурак", "Мать", "Леви", ]

with open("exv.csv", "w") as d:
    w = csv.writer(d, delimiter=",")
    w.writerow(["ЗВ",
                "Тер",
                "ИИ"])
    w.writerow(["Дурак",
                "Мать",
                "Леви"])
with open("exv.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))