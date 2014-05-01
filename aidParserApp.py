import csv

class Parser:
    def __init__(self, interface):
        self.interface = interface()

    def run(self):
        FIND_UNIQUES = 0
        POPULATE = 1
        findUniquesOrPopulate = self.interface.askWhatOperation()

        if findUniquesOrPopulate == FIND_UNIQUES:
            self.findUniques()
        else:
            self.populate()
        
        self.interface.exit()

    def findUniques(self):
        fileName = self.interface.getInFileName('Country Data')
        table = self.getTable(fileName)
        uniqueTable = self.getUniques(table)
        outName = self.interface.getOutFileName('Unique names')
        
        f = open(outName, 'wb')
        writer = csv.writer(f, dialect='excel')
        writer.writerows(uniqueTable)
        f.close()

    def getTable(self, fileName):
        table = []
        
        with open(fileName, 'rU') as f:
            reader = csv.reader(f)
            for line in reader:
                table.append(line)

        return table

    def getUniques(self, table):
        outTable = []
        outTable.append(['Title', 'Short Description', 'Long Description', 'Lat', \
        'Long', 'Precision Code'])

        row = table[0]
        titleCol, sDescripCol, lDescripCol = row.index('Title'), \
        row.index('Short Description'), row.index('Long Description')

        uniqueVals = []

        for i in range(1, len(table)):
            row = table[i]
            title, sDescrip, lDescrip = row[titleCol], row[sDescripCol], row[lDescripCol]
            if not [title, sDescrip, lDescrip] in uniqueVals:
                uniqueVals.append([title, sDescrip, lDescrip])

        for line in uniqueVals:
            line.extend(['']*3)
            outTable.append(line)

        return outTable

    def populate(self):
        uniqueFileName = self.interface.getInFileName('Unique Names')
        
        f = open(uniqueFileName, 'rU')
        uniqueReader = csv.reader(f)

        uniqueTable = []

        for line in uniqueReader:
            uniqueTable.append(line)

        rawFileName = self.interface.getInFileName('Country Data')
        
        f1 = open(rawFileName, 'rU')
        rawReader = csv.reader(f1)
        rawTable = []

        for line in rawReader:
            rawTable.append(line)
        
        row = rawTable[0]

        titleCol, sDescripCol, lDescripCol = row.index('Title'), \
        row.index('Short Description'), row.index('Long Description')

        rawTable[0].extend(['Lat', 'Long', 'Precision Code'])

        for i in range(1, len(uniqueTable)):
            uniqueRow = uniqueTable(i)
            
            for j in range(1, len(rawTable)):
                rawRow = rawTable[j]

                if uniqueRow[0] == rawRow[titleCol] and uniqueRow[1] == rawRow[sDescripCol] and uniqueRow[2] == rawRow[lDescripCol]: # rows match
                    rawTable[j].extend(uniqueRow[3:])
        
        # rawTable now has lat and long from unique row

        f1.close()

        f2 = open(rawFileName, 'wb')
        rawWriter = csv.writer(f2, dialect = 'excel')

        rawWriter.writerows(rawTable)
        f2.close()













        
