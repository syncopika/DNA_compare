dnacompare (dnacomparebasic is w/o GUI)
===========
a simple dna sequence comparison program with GUI made in Python 3.3 with tkinter    

-finds **ONE** point mutation between 2 DNA sequences  
-also counts how many nucleotides in the sequence 

see here: http://33.media.tumblr.com/39e9389c6b91a9262045ad3cf39c39a6/tumblr_nbamxkCoVi1rvm1x2o1_1280.png 

**pros:**  
-finds you a single point mutation!  
-counts nucleotides!  
-tells you the nucleotide number of the mutation (starting from 1, and not 0)  
-tells you the original and changed nucleotide  
-if you're comparing sequences of different lengths, the comparison will be done by adjusting the longer string to the   length of the smaller one.  

**example:**  
seq1: atcgatcga  
seq2: atcgatcaa

the program will ouput: 8. g, a   
=> mutation at nucleotide number 8, guanine is changed to adenine.   

**cons :**  
-if your sequence contains multiple mutations, the program only outputs the last one  
-if you have a really long sequence (i.e.16494 bp), the program gets kinda laggy (although I've only tested this on my   netbook so far)  

**Background:**  

   I took a microbiology course last semester (today is 8/30/14) called BSCI283 at UMD. It was a nice course and I learned a lot, I think, but there was one exam that had a take home portion that required us to compare a couple sequences. This particular set of sequences had a length of 16494 base pairs. And apparently, there was supposed to be ONE single point mutation in the whole set. :< (I failed this part because I forgot to do it until last minute, but more importantly, I didn't have a way to quickly find the one, single mutation.) Anyway, so that inspired me to make this program. Although far from perfect, I think it would have maybe helped me had I had this program on the day I was working on the take-home part of that terrible exam.  
    
I made this program a couple weeks into attempting to self-study Python. 
