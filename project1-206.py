import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

	inFile = open(file, 'r')
	list = []
	readlines = inFile.readlines()


	temp1 = readlines[0]
	temp2 = temp1.rstrip()
	header = temp2.split(',')
	for object in readlines[1:]:
		i = 0
		dict_object = {}
		split_object = object.split(",")
		for x in split_object:
			dict_object[header[i]] = x
			i += 1
		list.append(dict_object)
	inFile.close()
	return list


def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	sort_dict = sorted(data, key = lambda x: x[col])
	first_name = str(sort_dict[0]['First'])
	last_name = str(sort_dict[0]['Last'])
	return '{} {}'.format(first_name, last_name)


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	class_dict = {}
	for object in data:
		if object["Class"] in class_dict:
			class_dict[object["Class"]] += 1
		else:
			class_dict[object["Class"]] = 1

	return sorted(class_dict.items(), key = lambda x: x[1], reverse=True)


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	month_dict = {}
	for object in a:
		birth_month = object["DOB"].split('/')[0]
		if birth_month in month_dict:
			month_dict[birth_month] += 1
		else:
			month_dict[birth_month] = 1
	return int(sorted(month_dict, key = lambda x: month_dict[x], reverse = True)[0])

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	OutFile = open(fileName, 'w')
	sort_file = sorted(a, key = lambda x:x[col])
	for x in sort_file:
		first_name = str(x['First'])
		last_name = str(x['Last'])
		email_name = str(x['Email'])
		OutFile.write('{},{},{}\n'.format(first_name, last_name, email_name))
	OutFile.close()
	return

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	ages = []
	for dic in a:
		ages.append(2018 - int(dic['DOB'].split('/')[-1].strip('\n')))
	return round(sum(ages)/len(ages))

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
