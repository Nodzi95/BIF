f = open("C:\\Users\\nodzi\\Documents\\GitHub\\BIF\\BIF_test_text.gff", "r")
#f = open("C:\\Users\\Nodzi\\Downloads\\pqs_chr7_hg38.tar\\pqs_chr7_hg38\\pqs_chr7_hg38.gff", "r")
import time

SEQ_INFO = 3
SEQ_ID = 0
SEQ_TYPE = 2
SEQ_START = 3
SEQ_END = 4
SEQ_VALUE = 5
SEQ_DIRECTION = 6
POS_DIRECTION = 1
NEG_DIRECTION = 0
SEQ_STOP = 8
TMP = []
def makeString(lMAX):
    for x in lMAX:
        string = str(x[SEQ_ID]) + "	" + str(x[1]) + "	" + str(x[SEQ_TYPE]) + "	" + str(x[SEQ_START]) + "	" + str(x[SEQ_END]) + "	" + str(x[SEQ_VALUE]) + "	" + str(x[SEQ_DIRECTION]) + "	" + str(x[7])
    return string


def sortEnd(elem):
    return elem[4]

def findMAX(arr):
    arr.sort(key=sortEnd)
    length = len(arr)
    max = 0
    MAX = []
    for i in range(length):
        tmpMax = arr[i][SEQ_VALUE]
        if tmpMax > max:
            max = tmpMax
            MAX = arr[i].copy()

        TMP.append(arr[i])
        findMAXr(arr[i:])
        for k in TMP[1:]:
            tmpMax += k[SEQ_VALUE]
        if tmpMax >= max:
            MAX = TMP.copy()
            max = tmpMax
        tmpMax = 0
        TMP.clear()


    print('final max: ' + str(max) + ' SEQ: ' + str(MAX))

#def findMAXr(arr):
#    print(arr)
#
#    length = len(arr)
#    if length <= 2:
#        return arr[0][SEQ_VALUE]
#    else:
#            if arr[0][SEQ_END] < arr[1][SEQ_START]:
#                print('halo')
#                return arr[1][SEQ_VALUE] + findMAXr(arr[1:])
#            else:
#                return findMAXr(arr[2:])

def findMAXr(arr):
    for i in range(1, len(arr)):
        if arr[0][SEQ_END] < arr[i][SEQ_START]:
            TMP.append(arr[i])
            return findMAXr(arr[i:])
    return




def readSeq(file):
    return






direction = 0
prev_direction = -1
prev_seqid = ""
prev_type = ""

S = []

start_time = time.time()

for line in f:
    if '##' in line:
        #print('comment')
        print(line)
    else:
        lists = line.split("	")
        tmp = ["", "", "", 0, 0, 0, "", ""]

        for i in range(SEQ_INFO):
            tmp[i] = lists[i]

        tmp[SEQ_START] = int(lists[SEQ_START])
        tmp[SEQ_END] = int(lists[SEQ_END])
        tmp[SEQ_VALUE] = float(lists[SEQ_VALUE])

        for i in range(SEQ_DIRECTION, SEQ_STOP):
            tmp[i] = lists[i]

        if tmp[SEQ_DIRECTION] == '+':
            direction = POS_DIRECTION
        else:
            direction = NEG_DIRECTION

        if prev_direction == direction and prev_seqid == tmp[SEQ_ID] and prev_type == tmp[SEQ_TYPE]:
            S.append(tmp)
        else:
            findMAX(S)
            #findMAX
            #print(S)
            S.clear()
            S.append(tmp)


        prev_seqid = tmp[SEQ_ID]
        prev_direction = direction
        prev_type = tmp[SEQ_TYPE]
#print(len(S), S)
findMAX(S)
print("--- %s seconds ---" % (time.time() - start_time))
