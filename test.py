def _strGreaterThan(string1: str, string2: str) -> bool:
    l = [string1, string2]
    l.sort()
    if l[0] == string1:
        return True
    else:
        return False


def testBinarySearch (stringList, target, begining , end ):
    if begining <= end:
        middle = (begining+end) // 2
        print(middle)
        if stringList[middle] == target:
            return True
        elif _strGreaterThan(stringList[middle], target):
            return testBinarySearch(stringList, target, middle+1, end)
        elif _strGreaterThan(target, stringList[middle]):
            return testBinarySearch(stringList, target, begining, middle-1)
    else:
        return False

L = ['thing', 'fuck', 'whatever', 'horrible', 'how_is_this_possible']

L.sort()
print(L)
#print (testBinarySearch(L, 'whatever', 0, len(L)+1))
#print (testBinarySearch(L, 'horrible', 0, len(L)+1))
#print('got this far')
print(testBinarySearch(L, 'anything', 0, len(L)+1))