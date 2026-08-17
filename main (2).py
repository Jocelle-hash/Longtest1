Notebooks = float(input("Total number of notebooks? "))
Nb_box = float(input("How many notebooks can fit into a box? "))
print("Total number of notebooks:", Notebooks)
print("Number of notebooks that can fit in a box", Nb_box)

full_boxes = int(Notebooks) // int(Nb_box) 
print("Number of full boxes:", full_boxes)
leftover_books = (Notebooks % Nb_box)
print("Number of leftover books:", leftover_books)

#just incase the order is less than how many can fit in a box
if Notebooks < Nb_box:
    print("The box isn't filled")