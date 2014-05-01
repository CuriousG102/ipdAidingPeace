class TextInterface:
    def __init__(self):
        print "Welcome to the ipdAidingPeace country parser. This program has no"
        print "error protection and therefore has strict requirements."
        print "Csv files must have a header row, then the data."
        print "The header row must contain these cells: 'Title', 'Short Description', and 'Long Description'"
        print "From that raw file, the program will produce a csv file of uniques"
        print "Fill in that csv file with lat, long, and precision codes"
        print "Then launch the program again, feed it the csv file of uniques and"
        print "the file it was produced from, and it will copy back the list of lat,"
        print "long, and precision codes"

    def askWhatOperation(self):
        print "Note: Be careful that your input is exactly correct, or the program will crash!"
        operation = input("Would you like to find unique values from a spreadsheet\
        or populate a spreadsheet with your list of unique values? For the first option, press 0, for the second option, press 1. Then press enter.")

        return operation

    def exit(self):
        print "Your task has been accomplished. Goodbye!"

    def getInFileName(self, prompt):
        return raw_input("Please enter the exact filepath and name+extension of the \
        input csv file for %s: " % prompt)

    def getOutFileName(self, prompt):
        return raw_input("Please enter the exact filepath and name+extension of the \
        output csv file for %s: " % prompt)
