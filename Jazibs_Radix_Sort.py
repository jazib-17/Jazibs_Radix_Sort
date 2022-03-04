'''
   Jazib's Implementation of the Radix Sort Algorithm

   Author: Jazib Ahmed
   Email: jazib7537@gmail.com
'''

# Importing the random package necessary for this program
import random


def radix_sort(list1):
    """
    This function uses radix sort to sort the given list and then returns the
    sorted list.
    """

    # Making a b_list that will hold 10 lists, namely b_0...b_9
    b_list = [[],[],[],[],[],[],[],[],[],[]]

    # For loop that runs till the length of the biggest number in the list
    for i in range(1,len(str(max(list1)))+1):

        #For loop that goes through each number in the list
        for x in list1:

            # Having a temporary variable to convert each number to an integer
            temp = str(x)

            # Moving the number to the first list (b_0) if its length is not big
            # enough compared to the biggest number in the list
            if len(temp) < i:
                b_list[0].append(x)

            # Else statement that moves the number to its numbered b list based on
            # its ones, tens etc digit determined by the i value in the first for loop
            else:
                b_list[int(temp[-i])].append(x)

        # Emptying the list of numbers given
        list1 = []

        # For loop that goes through each list in b_list
        for index in range(len(b_list)):

            # For loop that goes through each number in each list of b_list
            for number in b_list[index]:
                # Adding all numbers from each list of b_list to the emptied
                # list of numbers given
                list1.append(number)

            # Emptying each list of b_list after all the numbers from that list have
            # been added
            b_list[index] = []

    # Returning the list of the sorted numbers
    return list1

def demo():
    """ This function will demo the radix sort function created above. """

    # Making an unsorted list using random and applying the radix sort algorithm to it
    unsorted = random.sample(range(1, 9999), 100)
    radix = radix_sort(unsorted)

    # Printing out the results
    print("Unsorted List: \n" + str(unsorted))
    print("-----------\nSorted List: \n" + str(radix))

# Calling on demo function to run the program
demo()