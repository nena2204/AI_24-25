from constraint import *

# dve sali za film
# razl genre, za deca do 18:00 drugite od 12:00 do 23:00 OKKK
# film traje 2 saati i posle sekoj mora da ima prazno 30 min
# ako ima eden vo edna sala ne moze istovremeno drug vo druga sala

def two_hours_difference(input1, input2):
    # Hall_2_Day_4_16
    # Hall_2_Day_4_16
    _, hallnumber1, _, daynumber1, starthour1 = input1.split("_")
    _, hallnumber2, _, daynumber2, starthour2 = input2.split("_")

    hour1, minutes1 = starthour1.split(":")
    hour2, minutes2 = starthour2.split(":")
    if hallnumber1 == hallnumber2 and daynumber1 == daynumber2:
        start1 = int(hour1) * 60 + int(minutes1)
        start2 = int(hour2) * 60 + int(minutes2)
        timediff = abs(start1 - start2)

        if timediff >= 150:
            return True
        else:
            return False
    else:
        return True

def kids_movie_constraint(a):
    # Hall_2_Day_4_16
    _, _, _, _, x = a.split("_")  # tuka go imam saato poslednata brojka
    hour, minutes = x.split(":")
    return int(hour) < 18


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    num_movies = int(input())
    movies = dict()
    for i in range(num_movies):
        key = input().split(" ")
        movies[key[0]] = key[1]
        # film1 detski

    days = int(input())
    movie_variables = [m for m in movies.keys()]
    time_movies = ["12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "17:00", "17:30", "18:00", "18:30", "19:00",
                   "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00"]
    day_variables = [f"Day_{i}" for i in range(1, days + 1)]
    hall_variables = ["Hall_1", "Hall_2"]

    domain = []
    for h in hall_variables:
        for d in day_variables:
            for time in time_movies:
                domain.append(f"{h}_{d}_{time}")

    for key in movie_variables:
        category = movies[key]  # Get the mapped category for each movie
        if category == "detski":
            problem.addConstraint(kids_movie_constraint, [key])
        problem.addVariable(key, domain)

    problem.addConstraint(AllDifferentConstraint(), movie_variables)

    for i in range(len(movie_variables)):
        for j in range(1 + i, len(movie_variables)):
            problem.addConstraint(two_hours_difference, [movie_variables[i], movie_variables[j]])

    solutions = problem.getSolution()
    if solutions:
        print(solutions)
    else:
        print("No solutions")
