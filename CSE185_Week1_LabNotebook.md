# CSE 185 Lab Notebook - Week 1

#### Name: Luke Jervis
#### Date: 04/03/18

# Part I
__Input/Output:__
1. head -n 20 NC_000913.3.fasta -
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
TTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAA
TATAGGCATAGCGCACAGACAGATAAAAATTACAGAGTACACAACATCCATGAAACGCATTAGCACCACC
ATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGACGCGTACAGGAAACACAGAAAAAAG
CCCGCACCTGACAGTGCGGGCTTTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAA
GTTCGGCGGTACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGGGGCAGGTGGCCACCGTCCTCTCTGCCCCCGCCAAAATCACCAACCACCTGGTGGCGATGATTG
AAAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAACGTATTTTTGCCGAACTTTT
GACGGGACTCGCCGCCGCCCAGCCGGGGTTCCCGCTGGCGCAATTGAAAACTTTCGTCGATCAGGAATTT
GCCCAAATAAAACATGTCCTGCATGGCATTAGTTTGTTGGGGCAGTGCCCGGATAGCATCAACGCTGCGC
TGATTTGCCGTGGCGAGAAAATGTCGATCGCCATTATGGCCGGCGTATTAGAAGCGCGCGGTCACAACGT
TACTGTTATCGATCCGGTCGAAAAACTGCTGGCAGTGGGGCATTACCTCGAATCTACCGTCGATATTGCT
GAGTCCACCCGCCGTATTGCGGCAAGCCGCATTCCGGCTGATCACATGGTGCTGATGGCAGGTTTCACCG
CCGGTAATGAAAAAGGCGAACTGGTGGTGCTTGGACGCAACGGTTCCGACTACTCTGCTGCGGTGCTGGC
TGCCTGTTTACGCGCCGATTGTTGCGAGATTTGGACGGACGTTGACGGGGTCTATACCTGCGACCCGCGT
CAGGTGCCCGATGCGAGGTTGTTGAAGTCGATGTCCTACCAGGAAGCGATGGAGCTTTCCTACTTCGGCG
CTAAAGTTCTTCACCCCCGCACCATTACCCCCATCGCCCAGTTCCAGATCCCTTGCCTGATTAAAAATAC
CGGAAATCCTCAAGCACCAGGTACGCTCATTGGTGCCAGCCGTGATGAAGACGAATTACCGGTCAAGGGC
ATTTCCAATCTGAATAACATGGCAATGTTCAGCGTTTCTGGTCCGGGGATGAAAGGGATGGTCGGCATGG
2. head -n 20 amp_res_1.fastq -
@SRR1363232.1 GWZHISEQ01:153:C1W31ACXX:5:1101:2403:2164 length=101
CCATACACGCCGCTTTAGCACAGCGTTATGAGAACATTGAAGTTANNGCCGTAAATGACGGTTCAACAGATAAAACCCGTGCCATCCTGGATCGCATGGCT
+SRR1363232.1 GWZHISEQ01:153:C1W31ACXX:5:1101:2403:2164 length=101
@@@FDFBDHDHGGE:EEIJFEGIJJFDFGGGGIJJGII<?FGIIG##.5@A@EHHHEA@DB=1=AC>C?>;(5@:>@BD@@@BACCDCCD?::9?BDDD?9
@SRR1363232.2 GWZHISEQ01:153:C1W31ACXX:5:1101:2424:2217 length=101
CCCATCTTTCTACCCTGGAATAATCGTTTATATCCCTTGGCATTACCTCTCTTTGTTTACATTCCAACATCATTTTATAAACATTCCGCTTGTGTTTTTCT
+SRR1363232.2 GWZHISEQ01:153:C1W31ACXX:5:1101:2424:2217 length=101
CCCFFFFFHGHGHIJIJJIIJJJIIJIJIIJJGGHIGIEIJIAGGGGJJIJIGIGFB>DCHGJADHIIJGH@GDG@GHFGGGGBECCCFBDABC?CCD?CC
@SRR1363232.3 GWZHISEQ01:153:C1W31ACXX:5:1101:3103:2142 length=101
CTAAGATACACTCAACTGATATAGCNTCTCTCTACTACTATNGNNNNNTAGTCCACTTTCATAATGAAAAAATTGAAGAGGCAAGGATTTGTATAGACAAA
+SRR1363232.3 GWZHISEQ01:153:C1W31ACXX:5:1101:3103:2142 length=101
@@@ADFDFDBDDFHGEGIEIG?C@E#2AECGE@EGIIIJEI#0#####0077BF=C@BFC@GGHGGCHGGHDFDFFEEA;A@@??=<>@A@DDEC@CDCC9
@SRR1363232.4 GWZHISEQ01:153:C1W31ACXX:5:1101:3405:2144 length=101
ATTTATTTTTGCATTAGGGTATGAAGTTTCCGGGTTAGGTCNTNNNNNTGCCCTTTTCCTGGTGAAATTCATGGGCAAACGCACGCTGACGTTGGGTTATG
+SRR1363232.4 GWZHISEQ01:153:C1W31ACXX:5:1101:3405:2144 length=101
CCCFFFFFHHHHHJJJJJJEEHIJJJHHIIIJIJFHGJJHI#0#####0-;CHIJJJJJIJJGGECHCHEFFDDD@CCEC?DDDDDDDDDDBDBABBB?CC
@SRR1363232.5 GWZHISEQ01:153:C1W31ACXX:5:1101:3334:2162 length=101
AATAAACACCACTGAAGGGCGCTGTGAATCACAAGCTATGGCAANNNCATCAACGGTTTCAATGTCGTTGATTTCTCTTTTTTTAACCCCTCTACTCAACA
+SRR1363232.5 GWZHISEQ01:153:C1W31ACXX:5:1101:3334:2162 length=101
CCCFFFFFGHHHHJGIIJJIJJJJJJIIIJJJJIJIJJIJJJIC###-5BFGHGJGEFEFFFDEEDC=@DDACDDCDDDDDDDDBAC><BDDCCDED@CDD
3. head -n 20 amp_res_2.fastq -
@SRR1363232.1 GWZHISEQ01:153:C1W31ACXX:5:1101:2403:2164 length=101
TTCGAATACGAGGATTACCGGTTACGGCACCCACACGCGGGTTGTACAACATCGGTTCCACAATATATGCCGCCGCATCGCGGTCTAATAACGCATCGCCA
+SRR1363232.1 GWZHISEQ01:153:C1W31ACXX:5:1101:2403:2164 length=101
@?@FDD?B=FAFA<BHIIBHGEGGIHHGG<GG=DGGEGGGF/=@;AD@CDBCDDBDBBDEACD@CCD>(:A@B@BDD<@BDBB>B7:>ACACBDD<99@B?
@SRR1363232.2 GWZHISEQ01:153:C1W31ACXX:5:1101:2424:2217 length=101
ACCCAAGCCCAGGCACAACGCAGCGGCAAGCAACACGCCAATCCACATCACACAATCCATCGGCCTCGCTGGGTACGCTTAAGATAGCTGGCAATCAAACT
+SRR1363232.2 GWZHISEQ01:153:C1W31ACXX:5:1101:2424:2217 length=101
CCCFFFFFHHHFHGGJJJJJJIIIBIJJJJJIJJJJGGHIGHHHFFFFFF@CEDDDDCCDD?8;BBDBBBBDD9@CDBB?BDCCDDCDCCCDDBC<@CDC#
@SRR1363232.3 GWZHISEQ01:153:C1W31ACXX:5:1101:3103:2142 length=101
GGTTAGGCACATACATATCTACACATTCTTTNATCACAACTGCTTTTCGTCTTCTGGGTTCGAGTTGTAGTGATTTGTCTATACAAATCCTTGCCTCTTCA
+SRR1363232.3 GWZHISEQ01:153:C1W31ACXX:5:1101:3103:2142 length=101
BC@DFDFDHFHFDIGEIAHJGGIIGHEHGJI#11CFHABFD>DDGHEHIGDDAHFFFGBAGHEEGDE?EE?ABCCEDBECB>@CCECCA>>CCCCDDCC@@
@SRR1363232.4 GWZHISEQ01:153:C1W31ACXX:5:1101:3405:2144 length=101
GAAAAACCGTACCCCCGGTACGCGCGGTGTTGGAAGGTGTAAACGGTGCCAGCAGAATGTCGATAATGACAATCGCATAACCCAACGTCAGCGTGCGTTTG
+SRR1363232.4 GWZHISEQ01:153:C1W31ACXX:5:1101:3405:2144 length=101
CC@FFFFFGGHHHJJJJJHIIIJIIJJ@E@DHHGHFFCD?CEFEB@?ABDCCBDDDDDDDEDBDDDC>@CDDCDBDDDDDC@BDBDD8?BDCD?B9>8<B#
@SRR1363232.5 GWZHISEQ01:153:C1W31ACXX:5:1101:3334:2162 length=101
GGGTATGCCATGTCAACGATTATTATGGATTTATGTAGTTACACCCGACTAGGTTTAACCGGGTATCTGTTGAGTAGAGGGGTTAAAAAAAGAGAAATCAA
+SRR1363232.5 GWZHISEQ01:153:C1W31ACXX:5:1101:3334:2162 length=101
BCCDDFFFGHHHHJIIIJHIIJJJIJJJIIIJGIJHIIIJJJIJJJJIJIHIJBFGIGJJJJFAEEFFFFFFCE@EEEDDDB?@BCDDCBBBBDCDDDACC
4. cat NC_000913.3.fasta
5. wc -l amp_res_1.fastq - __14214080__ amp_res_1.fastq
6. wc -l amp_res_2.fastq - __14214080__ amp_res_2.fastq
7. wc -l NC_000913.3.fasta - __66311__ NC_000913.3.fasta
8. wc -m NC_000913.3.fasta - __4708034__ NC_000913.3.fasta

Average coverage = # sequence bases / length of genome

Average coverage = 101*(14214080/4)/4708034 = 77x

# Part II

__Input/Output__
1. fastqc -h
The manual page was displayed indicating the program was correctly set up
2. fastqc -o . /home/linux/ieng6/cs185s/public/week1/amp_res_2.fastq
generated two files: amp_res_2_fastqc.html amp_res_2_fastqc.zip
3. fastqc -o . /home/linux/ieng6/cs185s/public/week1/amp_res_1.fastq
generated two files: amp_res_1_fastqc.html amp_res_1_fastqc.zip
4. pscp ljervis@ieng6.ucsd.edu:/home/linux/ieng6/oce/8m/ljervis/week1/amp_res_1_fastqc.html C:/Users/lukej/Desktop/
transfered previously generated html file to my computer
number of reads previously determined: 3555520
number of reads determined by fastqc: 3553520
Basic statistics: green
Per base sequence quality: red
Per tile sequence quality: red 
Per sequence quality scores: green 
Per base sequence content: yellow
Per sequence GC centent: yellow
Per base N content: green
Sequence Length Distribution: green 
Sequence Duplication Levels: yellow
Overrepresented seqences: green
Adapter Content: green 
5. pscp ljervis@ieng6.ucsd.edu:/home/linux/ieng6/oce/8m/ljervis/week1/amp_res_2_fastqc.html C:/Users/lukej/Desktop/
transfered previously generated html file to my computer
number of reads previously determined: 3555520
number of reads determined by fastqc: 3553520
Basic statistics: green
Per base sequence quality: red
Per tile sequence quality: yellow 
Per sequence quality scores: green 
Per base sequence content: red 
Per sequence GC centent: yellow
Per base N content: green
Sequence Length Distribution: green
Sequence Duplication Levels: yellow
Overrepresented seqences: green
Adapter Content: green
6. sickle pe -f /home/linux/ieng6/cs185s/public/week1/amp_res_1.fastq -r /home/linux/ieng6/cs185s/public/week1/amp_res_2.fastq -t sanger -o trimpair1.fastq -p trimpair2.fastq -s singletons.fastq

PE forward file: /home/linux/ieng6/cs185s/public/week1/amp_res_1.fastq
PE reverse file: /home/linux/ieng6/cs185s/public/week1/amp_res_2.fastq

Total input FastQ records: 7107040 (3553520 pairs)

FastQ paired records kept: 6904494 (3452247 pairs)
FastQ single records kept: 98694 (from PE1: 94870, from PE2: 3824)
FastQ paired records discarded: 5158 (2579 pairs)
FastQ single records discarded: 98694 (from PE1: 3824, from PE2: 94870)

generated three files: trimpair1.fastq trimpair2.fastq singletons.fastq
7. wc -l trimpair1.fastq
13808988 trimpair1.fastq
read count: 3452247
8. wc -l trimpair2.fastq
13808988 trimpair2.fastq
read count: 3452247
9. pscp ljervis@ieng6.ucsd.edu:/home/linux/ieng6/oce/8m/ljervis/week1/trimpair2_fastqc.html C:/Users/lukej/Desktop/
transfered previously generated html file to my computer
10. pscp ljervis@ieng6.ucsd.edu:/home/linux/ieng6/oce/8m/ljervis/week1/trimpair2_fastqc.html C:/Users/lukej/Desktop/
pscp ljervis@ieng6.ucsd.edu:/home/linux/ieng6/oce/8m/ljervis/week1/trimpair2_fastqc.html C:/Users/lukej/Desktop/
11. wc -l singletons.fastq
394776 singletons.fastq
12. fastqc -o . trimpair1.fastq
generated two files: trimpair1_fastq.html trimpair1_fastq.zip
13. fastqc -o . trimpair2.fastq
generated two files: trimpair2_fastq.html trimpair2_fastq.zip
14. sickle pe -q 30 -f /home/linux/ieng6/cs185s/public/week1/amp_res_1.fastq -r /home/linux/ieng6/cs185s/public/week1/amp_res_2.fastq -t sanger -o trimpair1_30.fastq -p trimpair2_30.fastq -s singletons_30.fastq
PE forward file: /home/linux/ieng6/cs185s/public/week1/amp_res_1.fastq
PE reverse file: /home/linux/ieng6/cs185s/public/week1/amp_res_2.fastq

Total input FastQ records: 7107040 (3553520 pairs)

FastQ paired records kept: 6012550 (3006275 pairs)
FastQ single records kept: 375230 (from PE1: 283732, from PE2: 91498)
FastQ paired records discarded: 344030 (172015 pairs)
FastQ single records discarded: 375230 (from PE1: 91498, from PE2: 283732)

generated three files: trimpair1_30.fastq trimpair2_30.fastq singletons_30.fastq
15. bwa index NC_000913.3.fasta
[bwa_index] Pack FASTA... 0.04 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 2.26 seconds elapse.
[bwa_index] Update BWT... 0.04 sec
[bwa_index] Pack forward-only FASTA... 0.03 sec
[bwa_index] Construct SA from BWT and Occ... 0.82 sec
[main] Version: 0.7.12-r1039
[main] CMD: bwa index NC_000913.3.fasta
[main] Real time: 4.142 sec; CPU: 3.206 sec
16. bwa mem NC_000913.3.fasta trimpair1.fastq trimpair2.fastq > trimpaired.sam
generated one file: trimpaired.sam
17. head -n 5 trimpaired.sam
@SQ     SN:NC_000913.3  LN:4641652
@PG     ID:bwa  PN:bwa  VN:0.7.12-r1039 CL:bwa mem NC_000913.3.fasta trimpair1.fastq trimpair2.fastq
SRR1363232.1    83      NC_000913.3     1087469 60      101M    =       1087258 -312    AGCCATGCGATCCAGGATGGCACGGGTTTTATCTGTTGAACCGTCATTTACGGCNNTAACTTCAATGTTCTCATAACGCTGTGCTAAAGCGGCGTGTATGG     9?DDDB?9::?DCCDCCAB@@@DB@>:@5(;>?C>CA=1=BD@AEHHHE@A@5.##GIIGF?<IIGJJIGGGGFDFJJIGEFJIEE:EGGHDHDBFDF@@@     NM:i:2  MD:Z:54A0A45      AS:i:97 XS:i:0
SRR1363232.1    163     NC_000913.3     1087258 60      101M    =       1087469 312     TTCGAATACGAGGATTACCGGTTACGGCACCCACACGCGGGTTGTACAACATCGGTTCCACAATATATGCCGCCGCATCGCGGTCTAATAACGCATCGCCA     @?@FDD?B=FAFA<BHIIBHGEGGIHHGG<GG=DGGEGGGF/=@;AD@CDBCDDBDBBDEACD@CCD>(:A@B@BDD<@BDBB>B7:>ACACBDD<99@B?     NM:i:0  MD:Z:101 AS:i:101 XS:i:0
SRR1363232.2    99      NC_000913.3     1081173 60      101M    =       1081413 341     CCCATCTTTCTACCCTGGAATAATCGTTTATATCCCTTGGCATTACCTCTCTTTGTTTACATTCCAACATCATTTTATAAACATTCCGCTTGTGTTTTTCT     CCCFFFFFHGHGHIJIJJIIJJJIIJIJIIJJGGHIGIEIJIAGGGGJJIJIGIGFB>DCHGJADHIIJGH@GDG@GHFGGGGBECCCFBDABC?CCD?CC     NM:i:0  MD:Z:101 AS:i:101 XS:i:0
18. samtools flagstat trimpaired.sam
6906203 + 0 in total (QC-passed reads + QC-failed reads)
0 + 0 secondary
1709 + 0 supplementary
0 + 0 duplicates
6899109 + 0 mapped (99.90% : N/A)
6904494 + 0 paired in sequencing
3452247 + 0 read1
3452247 + 0 read2
6881172 + 0 properly paired (99.66% : N/A)
6891682 + 0 with itself and mate mapped
5718 + 0 singletons (0.08% : N/A)
0 + 0 with mate mapped to a different chr
0 + 0 with mate mapped to a different chr (mapQ>=5)
in total does not match my read count after trimming but is very close (6906203 != 6904494)
19. samtools view -S -b trimpaired.sam > trimpaired.bam
20. samtools sort trimpaired.bam > sortedtrimpaired.bam
21. samtools index sortedtrimpaired.bam
22. samtools tview sortedtrimpaired.bam NC_000913.3.fasta
a visual representation of the sam file is presented
jumped to position 46 using NC:000913.3:46 to see varients at this base. There is a read with a varient "A" in this position. Only one read shares this varient so I would argue this is a sequencing mistake. 
23. 
