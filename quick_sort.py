import colorama
from colorama import Fore

def get_numbers(*args):
	numbers_list = []
	while True:
		number = input(Fore.BLUE + "enter the number: ")
		if number == "exite":
			break
		else:
			numbers_list.append(int(number))
	return numbers_list


# find the partition
def partition(list_of_numbers, min, max):

	pivot = list_of_numbers[max]
	a = min - 1
	for b in range(min, max):
		if list_of_numbers[b] <= pivot:
			a +=1
			(list_of_numbers[a], list_of_numbers[b]) = (list_of_numbers[b], list_of_numbers[a])

	
	(list_of_numbers[a + 1], list_of_numbers[max]) = (list_of_numbers[max], list_of_numbers[a + 1])

	return a + 1

def quickSort(list_of_numbers, min, max):
	if min < max:

		pivot = partition(list_of_numbers, min, max)

		quickSort(list_of_numbers, min, pivot - 1)

		quickSort(list_of_numbers, pivot + 1, max)


numbers = get_numbers()
print(Fore.RED + f'the numbers BEFORE sorting are: {numbers}')

size = len(numbers)

quickSort(numbers, 0, size - 1)

print(Fore.GREEN + f'the numbers AFTER sorting are: {numbers}')


