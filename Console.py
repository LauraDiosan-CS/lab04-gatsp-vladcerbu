from Service import *


def run():
    while True:
        print("1 = Easy Test")
        print("2 = Medium Test")
        print("3 = Hard Test")
        print("4 = Very Hard Test")
        print("5 = Easy Test 2")
        print("6 = Berlin")
        print("0 = Exit")
        comm = input("Selectati: ")
        if comm == "0":
            print("Bye!")
            break
        elif comm == "1":
            pop = input("Dati numarul populatiei: ")
            gen = input("Dati numarul de generatii: ")
            rez = doga(int(pop), int(gen),
                    "E:\\FMI Sem.4\\Inteligenta Artificiala\\Lab\\lab04_teste\\easy_test2.txt",
                    "E:\\FMI Sem.4\\Inteligenta Artificiala\\Lab\\lab04_teste\\easy_solution2.txt")
            print("Drumul cel mai scurt: ", rez.repres)
            print("Lungime: ", rez.fitness)
            print()
        elif comm == "2":
            pop = input("Dati numarul populatiei: ")
            gen = input("Dati numarul de generatii: ")
            rez = doga(int(pop), int(gen),
                    "E:\\FMI Sem.4\\Inteligenta Artificiala\\Lab\\lab04_teste\\medium_test2.txt",
                    "E:\\FMI Sem.4\\Inteligenta Artificiala\\Lab\\lab04_teste\\medium_solution2.txt")
            print("Drumul cel mai scurt: ", rez.repres)
            print("Lungime: ", rez.fitness)
            print()
        elif comm == "3":
            pop = input("Dati numarul populatiei: ")
            gen = input("Dati numarul de generatii: ")
            rez = doga(int(pop), int(gen),
                    "E:\\FMI Sem.4\\Inteligenta Artificiala\\Lab\\lab04_teste\\hard_test2.txt",
                    "E:\\FMI Sem.4\\Inteligenta Artificiala\\Lab\\lab04_teste\\hard_solution2.txt")
            print("Drumul cel mai scurt: ", rez.repres)
            print("Lungime: ", rez.fitness)
            print()
        elif comm == "4":
            pop = input("Dati numarul populatiei: ")
            gen = input("Dati numarul de generatii: ")
            rez = doga(int(pop), int(gen),
                    "E:\\FMI Sem.4\\Inteligenta Artificiala\\Lab\\lab04_teste\\vhard_test2.txt",
                    "E:\\FMI Sem.4\\Inteligenta Artificiala\\Lab\\lab04_teste\\vhard_solution2.txt")
            print("Drumul cel mai scurt: ", rez.repres)
            print("Lungime: ", rez.fitness)
            print()
        elif comm == "5":
            pop = input("Dati numarul populatiei: ")
            gen = input("Dati numarul de generatii: ")
            rez = doga(int(pop), int(gen),
                       "E:\\FMI Sem.4\\Inteligenta Artificiala\\Lab\\lab04_teste\\easy2_test.txt",
                       "E:\\FMI Sem.4\\Inteligenta Artificiala\\Lab\\lab04_teste\\easy2_solution.txt")
            print("Drumul cel mai scurt: ", rez.repres)
            print("Lungime: ", rez.fitness)
            print()
        elif comm == "6":
            pop = input("Dati numarul populatiei: ")
            gen = input("Dati numarul de generatii: ")
            rez = doga(int(pop), int(gen),
                       "E:\\FMI Sem.4\\Inteligenta Artificiala\\Lab\\lab04_teste\\berlin522.txt",
                       "E:\\FMI Sem.4\\Inteligenta Artificiala\\Lab\\lab04_teste\\berlin_solution.txt")
            print("Drumul cel mai scurt: ", rez.repres)
            print("Lungime: ", rez.fitness)
            print()
        else:
            print("Nu exista aceasta comanda!")
            print()
    return 0
