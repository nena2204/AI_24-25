from constraint import *
#Задача: Рaspored на натпревари во две хали
#Имате за задача да го распоредите одржувањето на повеќе натпревари во две хали. 
#За секој натпревар се знае категоријата на натпреварот и одредена хала во која ќе се одржи, но треба да се задоволат следниве услови:
#Услови: Разлика од 2 часа помеѓу натпреварите:
#За секој пар на натпревари што се одржуваат во ист ден, мора да има најмалку 2 часа разлика помеѓу нив. 
#Ова значи дека ако два натпревари се одржуваат во ист ден, нивните термини не смеат да се преклопуваат.
#Натпреварите во иста категорија не смеат да почнуваат во ист час:
#За секој натпревар од истата категорија, не смеат да почнат во ист час во било кој ден. Ова значи дека ако два натпревари се во иста категорија, нивните почетни часови не смеат да се совпаѓаат.
#Хала за натпревари на прва категорија:
#За натпреварите од првата категорија (cat1), сите тие мора да се одржат во Хала 1. Натпреварите од други категории може да се одржуваат во било која од двата холови (Хала 1 или Хала 2).

#Влез:
#На почетокот добивате број на натпревари (N).
# По тоа следат N редови со податоци за секој натпревар. За секој натпревар се наведува името на тимот и неговата категорија (например "cat1", "cat2", итн).
# На крајот добивате број на денови на кои ќе се одржат натпреварите.

# Излез:
# Излезот треба да биде распоред на натпреварите, кој ќе ги задоволи сите услови од задачата. За секој натпревар треба да биде дадена хала, ден и време кога ќе се одржи.

# Ако не е можно да се состави распоред кој ги задоволува сите услови, излезот треба да биде „No solution“.
# vo dve HALL
# vo each hall -> category, hall
"""Constrains
1. razlika od dva casa megju natprevarite
2. vo ista kategorija ne smeat u isti cas
3. za category 1 vo prva sala 

"""


def hall1_constraint(a):
    # Hall_2_Day_4_16
    _, x, _, _, _ = a.split("_")
    return x == "1"


def three_hours(input1, input2):
    # Hall_2_Day_4_16
    if input1.split("_")[3] == input2.split("_")[3]:
        return abs(int(input1.split("_")[4]) - int(input2.split("_")[4])) > 3

    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    num_competitions = int(input())
    matches = dict()
    # match 1 cat1
    for _ in range(num_competitions):
        key = input().split(" ")
        # match1 category
        matches[key[0]] = key[1]

    # print(matches)
    days = int(input())
    match_variables = [m for m in matches.keys()]
    termini_variables = list(range(9, 17))
    hall_variables = ["Hall_1", "Hall_2"]
    day_variables = [f"Day_{i}" for i in range(1, days + 1)]

    # promenlivi
    domain = []

    for h in hall_variables:
        for d in day_variables:
            for t in termini_variables:
                domain.append(f"{h}_{d}_{t}")

    # vo key imam match1 match2.... i matches[key] ke mi isprinta category
    # odnosno
    # 'M1': 'cat1'

    for key in match_variables:
        # print(matches[key])

        category = matches[key]
        if category == "cat1":
            problem.addConstraint(hall1_constraint, [key])
        problem.addVariable(key, domain)

    problem.addConstraint(AllDifferentConstraint(), match_variables)

    for i in range(len(match_variables)):
        for j in range(i + 1, len(match_variables)):
            problem.addConstraint(three_hours, [match_variables[i], match_variables[j]])

    solution = problem.getSolution()
    if solution:
        print(solution)
    else:
        print("No solution")
