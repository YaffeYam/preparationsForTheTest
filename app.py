from mainFolder.calcFolder.calc import calc
from mainFolder.checkArray import check_array
from mainFolder.arrayModule.sortArray import print_sorted_array
from mainFolder.failedAndSuccessfulRuns.failedRun import failing_function
from mainFolder.failedAndSuccessfulRuns.successfulRun import successful_function

#Prints the outcome of the index set to be calculated
def main():
    print("Multiplying 2*3:")
    print (calc(3))
    print ("--------------------------------------")
    
    #Will print "False" since the numbers are unique
    print ("Are there duplicates in this array?")
    print (check_array([2,3,5]))
    print ("--------------------------------------")

    #Will print "True" since the number 10 isn't unique
    print ("Are there duplicates in this array?")
    print (check_array([10,10,5,9]))
    print ("--------------------------------------")

    print ("Printing an array before and after it's been sorted:")
    my_array = [4, 2, 7, 1, 9, 5]
    print("Original array:", my_array)
    print_sorted_array(my_array)

if __name__ == "__main__":
    main()