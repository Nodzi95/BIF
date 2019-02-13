f = open("C:\\Users\\nodzi\\Desktop\\BIF_test_text.gff", "r")
#f = open("C:\\Users\\nodzi\\Downloads\\pqs_chr7_hg38.tar\\pqs_chr7_hg38\\pqs_chr7_hg38.gff", "r")
max = ["", "", "", 0, 0, 0, "", ""]
tmp = ["", "", "", 0, 0, 0, "", ""]
for line in f:
    if '##' in line:
        print 'comment'
    else:
        lists = line.split("	")
        j = 0
        for i in lists:
            tmp[j] = i
            j = j+1
        print tmp

        #print line.find("	", line.find("	", line.find("	")+1)+1)
