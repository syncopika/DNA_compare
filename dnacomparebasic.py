#this is simply a function to handle multiple point mutations. not as cool as a GUI, but it works. 
#maybe someone may find it useful for something else! 

def DNAcompare():
    print('Please enter sequence 1')
    seq1=input()
    print('Please enter sequence 2')
    seq2=input()
    lenSeq1=len(seq1)
    lenSeq2=len(seq2)
    if lenSeq1>lenSeq2:
        seq1=seq1[0:lenSeq2]
        for i in range(0,len(seq2)):
            if seq1[i]!=seq2[i]:
                print(str(i)+', '+seq1[i]+', '+seq2[i])
    if lenSeq2>lenSeq1:
        seq2=seq2[0:len(seq1)]
        for i in range(0,len(seq1)):
            if seq1[i]!=seq2[i]:
                print(str(i)+', '+seq1[i]+', '+seq2[i])
    if lenSeq1==lenSeq2:
        for i in range(0,len(seq1)):
            if seq1[i]!=seq2[i]:
                print(str(i)+', '+seq1[i]+', '+seq2[i])
