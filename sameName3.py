#Create a program about survival item
#Create a list of the survival item
#Program should be able to count the number of item
#Chosed item must be printed
#should you use try:except block
#should you use if : else statement

#Creating list of items
survival_item = ['Bag', 'Flashlight', 'Crowbar', 'Jacket', 'Medkit', 'Bow and arrow']
print("These are the numbers of item inside the invetory, Items:", len(survival_item))

#Counting and printing of item
print("Pick the number you want to use in the inventory:")
index = 5
if index < len(survival_item):
    print(survival_item[index])
    print(f"You Chosed {survival_item[index]} out of: {survival_item}")
    print("add more:?")
else:
    print("You exceed the number of index!")
