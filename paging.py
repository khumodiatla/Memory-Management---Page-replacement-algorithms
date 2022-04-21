# 2022 April 6
#

import sys
import random

def FIFO(size, pages):
    # Check if frame size is between 1 and 7
    if size >= 1 and size <= 7:
        pageArray = []
        faultCount = 0

        pages = pages.split(' ') 

        # Add the first page to the pageArray
        pageArray.append( pages[0])

        faultCount +=1
        replaceTracker = 0

        for i in range (1, len(pages)):
            if(  len(pageArray) != size):
                if( pages[i] not in pageArray ):
                    pageArray.append(pages[i])
                    faultCount +=1
            else:
                if( pages[i] not in pageArray):
                    
                    pageArray[replaceTracker] = pages[i]
                    faultCount +=1
                    replaceTracker += 1

                    # Check if replaceTracker is not == size and reset it
                    if(replaceTracker == size):
                        replaceTracker = 0
                                
        return faultCount


def LRU(size, pages):
    # Check if frame size is between 1 and 7
    if size >= 1 and size <= 7:
        pageArray = []
        faultCount = 0

        pages = pages.split(' ') 

        # Add the first page to the pageArray
        pageArray.append( pages[0])

        faultCount +=1
        replaceTracker = 0

        for i in range (1, len(pages)):
            if(  len(pageArray) != size):
                if( pages[i] not in pageArray ):
                    pageArray.append(pages[i])
                    faultCount +=1
            else:
                if( pages[i] not in pageArray):

                    reverseArray = pages[:i][::-1]
                    indexArray = []

                    for j in range(len(pageArray)):
                        indexArray.append(reverseArray.index(pageArray[j]))
                    
                    value_toReplace = reverseArray[max(indexArray)]
                    replaceTracker = pageArray.index(value_toReplace)

                    pageArray[replaceTracker] = pages[i]
                    faultCount +=1

        return faultCount

    else:
        print


def OPT(size, pages):
    # Check if frame size is between 1 and 7
    if size >= 1 and size <= 7:
        pageArray = []
        faultCount = 0

        pages = pages.split(' ') 

        # Add the first page to the pageArray
        pageArray.append( pages[0])

        faultCount +=1
        replaceTracker = 0

        for i in range (1, len(pages)):
            if(  len(pageArray) != size):
                if( pages[i] not in pageArray ):
                    pageArray.append(pages[i])
                    faultCount +=1
            else:
                if( pages[i] not in pageArray):
                    
                    remainingPages = pages[i:]
                    indexArray = []
                    valuesInPages = []

                    for j in range(len(pageArray)):
                        if( pageArray[j] in remainingPages):
                            indexArray.append( remainingPages.index(pageArray[j]) )
                            valuesInPages.append( pageArray[j])
                        else:
                            indexArray.append(-1)

                    if( -1 not in indexArray):
                        value_toReplace = remainingPages[max(indexArray)]
                        replaceTracker = pageArray.index(value_toReplace)

                        pageArray[replaceTracker] = pages[i]
                        faultCount +=1
                    else:
                        if( indexArray.count(-1) == 1):
                            replaceTracker = indexArray.index(-1)

                            pageArray[replaceTracker] = pages[i]
                            faultCount +=1
                        elif( indexArray.count(-1) == size):
                            reverseArray = pages[:i][::-1]
                            indexArray = []

                            for j in range(len(pageArray)):
                                indexArray.append(reverseArray.index(pageArray[j]))
                            
                            value_toReplace = reverseArray[max(indexArray)]
                            replaceTracker = pageArray.index(value_toReplace)

                            pageArray[replaceTracker] = pages[i]
                            faultCount +=1
                        else:
                            pages_copy = []

                            for k in range(len(pages)):
                                pages_copy.append(pages[k])

                            delete_count = 0
                            for k in range(len(valuesInPages)):
                                for j in range( pages_copy.count(valuesInPages[k])):
                                    pages_copy.remove(valuesInPages[k])
                                    delete_count += 1

                            reverseArray = pages_copy[:i-delete_count][::-1]
                            indexArray = []

                            for z in range(len(pageArray)):
                                if( pageArray[z] in reverseArray):
                                    indexArray.append(reverseArray.index(pageArray[z]))
                            
                            value_toReplace = reverseArray[max(indexArray)]
                            replaceTracker = pageArray.index(value_toReplace)

                            pageArray[replaceTracker] = pages[i]
                            faultCount +=1
                                

        return faultCount


def main():
    # ...TODO ..

    # page reference size
    no_pages = 16

    # a random page-reference string where page numbers range from 0 to 9
    pages = ''
    for i in range(no_pages):
        pages += str(random.randint(0,9)) + " "

    # frame sizes between 1 and 7 entered by the user
    size  = int(sys.argv[1])

    print('FIFO', FIFO(size,pages), 'page faults.')
    print('LRU', LRU(size,pages), 'page faults.')
    print('OPT', OPT(size,pages), 'page faults.')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ('Usage: python paging.py [number of pages]')
    else:
        main()
