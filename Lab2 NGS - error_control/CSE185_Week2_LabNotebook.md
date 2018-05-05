## Lab Notebook Week 2
# Luke Jervis

__clicker question 1__
Q. Was A/Hong Kong/4801/2014 (H3N2) used to make the 2017/2018 flu vaccine?
A. Yes

__clicker question 2__
Q. Based on the first 20 lines of the fastq file, how many cycles were probably carried out during the sequencing run?
A_1. It is impossible to tell for certian because some the reads have different lengths
A_2. 151 

__Input/Output__
1. wc -l roommate.fastq
1146956 roommate.fastq
__286739 reads in this file__

2. head -n 20 roommate.fastq
@SRR1705889.1 1 length=151
TATTAACCATGAAGACTATCATTGCTTTGAGCTACATTCTATGTCTGGTTTTCGCTCAAAAACTTCCTGGAAATGACAACAGCACGGCAACGCTGTGCCTTGGGCACCATGCAGTGCCAAACGGAGCGATAGTGAAAACAATCACGAATGA
+SRR1705889.1 1 length=151
?????BBBDDDDDDDDGGGGGGIIIHHIFFFHHHHHHIIHIIIFHHGHDFFHGAEHHHIHIIHHHHHIHFHIHIBFHHIHFFHFHHBE>DHHHHDHHHHCDFF;ADEHDFFHHG?BBBFDFFDDEGGB6AC?A>ACGACEE-CEEE8CCEC
@SRR1705889.2 2 length=151
TATTAACCATGAAGACTATCATTGCTTTGAGCTACATTCTATGTCTGGTTTTCGCTCAAAAACTTCCTGGAAATGACAACAGCACGGCAACGCTGTGCCTTGGGCACCATGCAGTGCCAAACGGAACGATAGTGAAAACAATCACGAATGA
+SRR1705889.2 2 length=151
????ABBBDDDDDDDDGGGGGGIIHHIIIIIIIHHHIIIIIIIIIIIIGHHIHHHHIHHGHFHIIIIIIGHIIIIIIIIIIIIIIHHHHHIHHHHHHHHHHHHHHHHHHHHHHGFGGGFFGGGGGGGGGGGGACCEGGGGGGEGGGCGGG?
@SRR1705889.3 3 length=131
ATCGTTCCGTTTGGCACTGCATGGTGCCCAAGGCACAGCGTTGCCGTGCTGTTGTCATTTCCAGGAAGTTTTTGAGCGAAAACCAGACATAGAATGTAGCTCAAAGCAATGATAGTCTTCATGGTTAATAG
+SRR1705889.3 3 length=131
??????BBDDDDDDDDGGGGGGIIFHIIIIIIIIIIIIIHHHHHIHEEHIIHHIIIIIIIIIIHIFHHHIIIIHHIIHHHHHHHHHHHHHHHHHHHHHHHHHHHHHGGGGGGGGGGGGGGGGGGDEGGGGG
@SRR1705889.4 4 length=131
ATCGTTCCGTTTGGCACTGCATGGTGCCCAAGGCACAGCGTTGCCGTGCTGTTGTCATTTCCAGGAAGTTTTTGAGCGAAAACCAGACATAGAATGTAGCTCAAAGCAATGATAGTCTTCATGGTTAATAG
+SRR1705889.4 4 length=131
??????BBDDDDEEEEGGGGGGIIFHIIIIIIIGIIIIHEHHHHIHHHHHHHHHHHIIIIIIIIIHHIGHHIIHHIIHHHHHHHHHHHHHHHHHHHHFHHHHFHHHGFGGGGGGGDDEGGGEGGEGGEEGG
@SRR1705889.5 5 length=108
GTGCCCAAGGCACAGCGTTGCCGTGCTGTTGTCATTTCCAGGAAGTTTTTGAGCGAAAACCAGACATAGAATGTAGCTCAAAGCAATGATAGTCTTCATGGTTAATAG
+SRR1705889.5 5 length=108
?????BB?BB9BBBBBC@CA>CCEE>E;EFF7CGDCFAA9CEAFFEEEFHC>EDEHHHC=>+AEFFHHFGGHHDGHHHGHHHH?DDD=DGHFHHF.7D@C..7CD,C,

3. cat roommate.fastq | awk 'NR%4==0 {print length}' | sort -n | uniq -c
     74 35
     16 36
     24 37
     36 38
     30 39
     37 40
     33 41
     26 42
     40 43
     42 44
     30 45
     52 46
     38 47
     51 48
     46 49
     50 50
     48 51
     57 52
     46 53
     66 54
     55 55
     55 56
     51 57
     43 58
     53 59
     62 60
     51 61
     67 62
     64 63
     61 64
     43 65
     55 66
     66 67
     66 68
     57 69
     57 70
     68 71
     62 72
     70 73
     54 74
     60 75
     70 76
     57 77
     83 78
     82 79
     86 80
     73 81
     95 82
     78 83
     86 84
     81 85
     67 86
     87 87
     72 88
    106 89
    109 90
    111 91
     95 92
     93 93
    110 94
    133 95
    101 96
    107 97
     86 98
    137 99
    117 100
    138 101
    123 102
    121 103
    125 104
    111 105
    111 106
    157 107
    115 108
    116 109
    107 110
    126 111
    142 112
    116 113
    106 114
    123 115
    129 116
    163 117
    164 118
    128 119
    152 120
    179 121
    174 122
    142 123
    149 124
    136 125
    175 126
    179 127
    160 128
    172 129
    209 130
    161 131
    191 132
    166 133
    216 134
    166 135
    167 136
    190 137
    221 138
    269 139
    295 140
   1139 141
    294 142
    865 143
   2911 144
    620 145
   3152 146
  13708 147
   5400 148
  15570 149
  45169 150
 187237 151
__maximum read length is 151__

4. efetch -db nucleotide -id KF848938.1 -format fasta > KF848938.1.fasta

5. bwa index KF848938.1.fasta
[bwa_index] Pack FASTA... 0.00 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 0.00 seconds elapse.
[bwa_index] Update BWT... 0.00 sec
[bwa_index] Pack forward-only FASTA... 0.00 sec
[bwa_index] Construct SA from BWT and Occ... 0.00 sec
[main] Version: 0.7.12-r1039
[main] CMD: bwa index KF848938.1.fasta
[main] Real time: 0.019 sec; CPU: 0.004 sec

6. bwa mem KF848938.1.fasta $public_dir/week2/roommate.fastq | samtools view -S -b | samtools sort > roomate.bam
[M::bwa_idx_load_from_disk] read 0 ALT contigs
[M::process] read 67542 sequences (10000222 bp)...
[M::process] read 67246 sequences (10000273 bp)...
[M::mem_process_seqs] Processed 67542 reads in 2.276 CPU sec, 2.214 real sec
[M::process] read 67118 sequences (10000102 bp)...
[M::mem_process_seqs] Processed 67246 reads in 2.756 CPU sec, 2.658 real sec
[M::process] read 67512 sequences (10000069 bp)...
[M::mem_process_seqs] Processed 67118 reads in 2.810 CPU sec, 2.709 real sec
[M::process] read 17321 sequences (2575106 bp)...
[M::mem_process_seqs] Processed 67512 reads in 3.071 CPU sec, 3.023 real sec
[M::mem_process_seqs] Processed 17321 reads in 1.491 CPU sec, 1.434 real sec
[main] Version: 0.7.12-r1039
[main] CMD: bwa mem KF848938.1.fasta /home/linux/ieng6/cs185s/public/week2/roommate.fastq
[main] Real time: 12.479 sec; CPU: 12.495 sec

7. samtools view -f4 roomate.bam | wc -l
3430
__the number of mapped reads: 283309__

8. samtools index roommate.bam

9. samtools mpileup -d 1000000 -f KF848938.1.fasta roomate.bam > roomate.mpileup
[mpileup] 1 samples in 1 input files

10. java -jar /home/linux/ieng6/cs185s/public/tools/VarScan.jar mpileup2snp roomate.mpileup --min-var-freq 0.95 --varients --output-vcf 1 > roomate.vcf
Only SNPs will be reported
Warning: No p-value threshold provided, so p-values will not be calculated
Min coverage:   8
Min reads2:     2
Min var freq:   0.95
Min avg qual:   15
P-value thresh: 0.01
Reading input from roomate.mpileup
1665 bases in pileup file
7 variant positions (7 SNP, 0 indel)
0 were failed by the strand-filter
7 variant positions reported (7 SNP, 0 indel)
__7 variants were reported back__

11. cat roomate.vcf | grep -v "^#" | awk '{print $2, $4, $5}'
72 A G
117 C T
595 G T
774 T C
1008 T G
1260 A C
1339 T C


Used NCBI to find the fasta sequence for KF848938.1 and found AA sequence using:
http://www.molbiotools.com/WebDSV/index.html
Manually annotated the varients found with VarScan 

| Original Codon | Mutated Codon | Original AA | Position | Mutated AA | Mutation Type |
| --- | --- | --- | --- | --- | --- |
| ACA | ACG | Thr | 24 | Thr | Synonymous |
| GCC | GCU | Ala | 39 | Ala | Synonymous |
| GCA | UCA | Ala | 119 | Ser | Missense |
| UUU | UUC | Phe | 258 | Phe | Synonymous |
| GCT | GCG | Ala | 336 | Ala | Synonymous |
| CTA | CTC | Leu | 420 | Leu | Synonymous |
| TTG | CTG | Leu | 447 | Leu | Synonymous |

12. java -jar $public_dir/tools/VarScan.jar mpileup2s                                                                                        np roomate.mpileup --min-var-freq 0.001 --variants --output-vcf 1 > roommate_rare.vcf
Only SNPs will be reported
Warning: No p-value threshold provided, so p-values will not be calculated
Min coverage:   8
Min reads2:     2
Min var freq:   0.001
Min avg qual:   15
P-value thresh: 0.01
Reading input from roomate.mpileup
1665 bases in pileup file
31 variant positions (31 SNP, 0 indel)
0 were failed by the strand-filter
31 variant positions reported (31 SNP, 0 indel)
__31 variants were reported back__

13.  cat roommate_rare.vcf | grep -v "^#" | awk '{print $2, $4, $5, $10}' | awk -F '[ :]' '{print $1, $2, $3, $10}'
38 T C 0.45%
72 A G 99.97%
117 C T 99.91%
216 A G 0.18%
218 A G 0.2%
254 A G 0.28%
276 A G 0.37%
295 C T 0.23%
319 T C 0.22%
409 T C 0.26%
495 C T 1.04%
524 A G 0.19%
595 G T 99.94%
691 A G 0.17%
722 A G 0.19%
774 T C 99.96%
910 G A 0.73%
915 T C 0.27%
987 A G 0.25%
1008 T G 99.9%
1043 A T 0.19%
1086 A G 0.26%
1100 T C 0.2%
1260 A C 99.9%
1293 G A 61.82%
1339 T C 99.97%
1460 A G 0.23%
1473 C T 0.23%
1517 A G 0.22%
1521 G A 1.12%
1604 T C 0.25%

## Part II

__Coverage of Control Sequences__
Number of reads = 999856
Length of reads = 151
Number of bases in reference genome = 1689
Coverage = (249964*151)/1689 = 22347X 

__Statistically Significant Rare Varients in Roommate Sequence__

| Original Codon | Mutated Codon | Original AA | Position | Mutated AA | Mutation Type |
| --- | --- | --- | --- | --- | --- |
| CTG | CCT | Leu | 13 | Pro | Missense |
| AAC | AAT | Asn | 165 | Asn | Synonymous |
| CTG | CTA | Leu | 431 | Leu | Missense |
| CTG | CTA | Leu | 507 | Leu | Synonymous |
| GCC | ACC | Ala | 304 | Thr | Missense |

__Epitope Mapping__
HA has five epitope regions (A, B, C, D, E)
Epitope A: residues 122, 124, 126, 130–133, 135, 137, 138, 140, 142–146, 150, 152, 168
Epitope B: residues 128, 129, 155–160, 163, 165, 186–190, 192–194, 196–198
Epitope C: residues 44–48, 50, 51, 53, 54, 273, 275, 276, 278–280, 294, 297, 299, 300, 304, 305, 307–312
Epitope D: residues 96,102,103,117,121,167,170–177,179,182, 201, 203, 207–209, 212–219, 226–230, 238, 240, 242, 244, 246–248
Epitope E: residues 57, 59, 62, 63, 67, 75, 78, 80–83, 86–88, 91, 92, 94, 109, 260–262, 265

__Mutated Epitope Regions__

| Position | Epitope | 
| -------- | ------- |
| 165 | B |
| 304 | C |
| 117 | D |


__Input/Output__

1. wc -l SRR1705858.fastq
1026344 SRR1705858.fastq
__256586 Reads__

2. wc -l SRR1705859.fastq
933308 SRR1705859.fastq

__233327 Reads__

3. wc -l SRR1705860.fastq
999856 SRR1705860.fastq
__249964 Reads__

4. tail -n +2 KF848938.1.fasta | wc -m
1689

5. for x in SRR1705858 SRR1705859 SRR1705860 ; do 
bwa mem KF848938.1.fasta $public_dir/week2/$x.fastq > $x.sam; done

[M::bwa_idx_load_from_disk] read 0 ALT contigs
[M::process] read 67448 sequences (10000210 bp)...
[M::process] read 67230 sequences (10000094 bp)...
[M::mem_process_seqs] Processed 67448 reads in 1.702 CPU sec, 1.622 real sec
[M::process] read 67100 sequences (10000113 bp)...
[M::mem_process_seqs] Processed 67230 reads in 1.919 CPU sec, 1.808 real sec
[M::process] read 54808 sequences (8118313 bp)...
[M::mem_process_seqs] Processed 67100 reads in 1.906 CPU sec, 1.772 real sec
[M::mem_process_seqs] Processed 54808 reads in 1.573 CPU sec, 1.529 real sec
[main] Version: 0.7.12-r1039
[main] CMD: bwa mem KF848938.1.fasta /home/linux/ieng6/cs185s/public/week2/SRR1705858.fastq
[main] Real time: 6.962 sec; CPU: 7.242 sec
[M::bwa_idx_load_from_disk] read 0 ALT contigs
[M::process] read 67476 sequences (10000274 bp)...
[M::process] read 67236 sequences (10000039 bp)...
[M::mem_process_seqs] Processed 67476 reads in 1.781 CPU sec, 1.684 real sec
[M::process] read 67216 sequences (10000283 bp)...
[M::mem_process_seqs] Processed 67236 reads in 2.209 CPU sec, 2.099 real sec
[M::process] read 31399 sequences (4635971 bp)...
[M::mem_process_seqs] Processed 67216 reads in 1.871 CPU sec, 1.779 real sec
[M::mem_process_seqs] Processed 31399 reads in 1.295 CPU sec, 1.242 real sec
[main] Version: 0.7.12-r1039
[main] CMD: bwa mem KF848938.1.fasta /home/linux/ieng6/cs185s/public/week2/SRR1705859.fastq
[main] Real time: 7.056 sec; CPU: 7.273 sec
[M::bwa_idx_load_from_disk] read 0 ALT contigs
[M::process] read 67356 sequences (10000126 bp)...
[M::process] read 67208 sequences (10000122 bp)...
[M::mem_process_seqs] Processed 67356 reads in 2.014 CPU sec, 1.933 real sec
[M::process] read 67010 sequences (10000072 bp)...
[M::mem_process_seqs] Processed 67208 reads in 2.228 CPU sec, 2.117 real sec
[M::process] read 48390 sequences (7170166 bp)...
[M::mem_process_seqs] Processed 67010 reads in 2.473 CPU sec, 2.366 real sec
[M::mem_process_seqs] Processed 48390 reads in 2.047 CPU sec, 1.997 real sec
[main] Version: 0.7.12-r1039
[main] CMD: bwa mem KF848938.1.fasta /home/linux/ieng6/cs185s/public/week2/SRR1705860.fastq
[main] Real time: 8.704 sec; CPU: 8.897 sec
__Created three files: SRR1705858.sam SRR1705859.sam SRR1705860.sam__

6. for x in SRR1705858 SRR1705859 SRR1705860 ; do 
 samtools view -S -b $x.sam > $x.bam 
 done
__Created three files: SRR1705858.bam; SRR1705859.bam; SRR1705860.bam__

7. samtools sort SRR1705860.bam > sorted_SSR1705860.bam
__Created one file: sorted_SRR1705860.bam__

8. samtools view -f4 sorted_SRR1705860.bam | wc -l
76

9. samtools sort SRR1705858.bam > sorted_SSR1705858.bam
__Created one file: sorted_SRR1705858.bam__

10. samtools view -f4 sorted_SRR1705858.bam | wc -l
86

11. samtools sort SRR1705859.bam > sorted_SSR1705859.bam
__Created one file: sorted_SRR1705859.bam__

12. samtools view -f4 sorted_SRR1705859.bam | wc -l
76

13. java -jar $public_dir/tools/VarScan.jar mpileup2snp sorted_SRR1705858.mpileup --min-var-freq 0.001 --varients --output-vcf 1 > sorted_SRR1705858.vcf
Only SNPs will be reported
Warning: No p-value threshold provided, so p-values will not be calculated
Min coverage:   8
Min reads2:     2
Min var freq:   0.001
Min avg qual:   15
P-value thresh: 0.01
Reading input from sorted_SRR1705858.mpileup
1665 bases in pileup file
58 variant positions (58 SNP, 0 indel)
1 were failed by the strand-filter
57 variant positions reported (57 SNP, 0 indel)

14. java -jar $public_dir/tools/VarScan.jar mpileup2snp sorted_SRR1705859.mpileup --min-var-freq 0.001 --varients --output-vcf 1 > sorted_SRR1705859.vcf
Only SNPs will be reported
Warning: No p-value threshold provided, so p-values will not be calculated
Min coverage:   8
Min reads2:     2
Min var freq:   0.001
Min avg qual:   15
P-value thresh: 0.01
Reading input from sorted_SRR1705859.mpileup
1665 bases in pileup file
54 variant positions (54 SNP, 0 indel)
2 were failed by the strand-filter
52 variant positions reported (52 SNP, 0 indel)

15. java -jar $public_dir/tools/VarScan.jar mpileup2snp sorted_SRR1705860.mpileup --min-var-freq 0.001 --varients --output-vcf 1 > sorted_SRR1705860.vcf
Only SNPs will be reported
Warning: No p-value threshold provided, so p-values will not be calculated
Min coverage:   8
Min reads2:     2
Min var freq:   0.001
Min avg qual:   15
P-value thresh: 0.01
Reading input from sorted_SRR1705860.mpileup
1665 bases in pileup file
61 variant positions (61 SNP, 0 indel)
0 were failed by the strand-filter
61 variant positions reported (61 SNP, 0 indel)

16. cat sorted_SRR1705858.vcf | grep -v "^#" | awk '{print $2, $4, $5, $10}' | awk -F '[ :]' '{print $1, $2, $3, $10}'
38 T C 0.66%
54 T C 0.3%
72 A G 0.3%
95 A G 0.24%
117 C T 0.3%
165 T C 0.24%
183 A G 0.3%
216 A G 0.22%
218 A G 0.28%
222 T C 0.26%
235 T C 0.25%
254 A G 0.25%
276 A G 0.22%
297 T C 0.2%
328 T C 0.2%
340 T C 0.23%
356 A G 0.22%
370 A G 0.21%
389 T C 0.23%
409 T C 0.22%
414 T C 0.28%
421 A G 0.18%
426 A G 0.19%
463 A G 0.19%
516 A G 0.2%
566 A G 0.22%
595 G T 0.34%
597 A G 0.17%
660 A G 0.2%
670 A G 0.29%
691 A G 0.23%
722 A G 0.23%
744 A G 0.21%
774 T C 0.3%
859 A G 0.27%
915 T C 0.26%
987 A G 0.22%
1008 T G 0.27%
1031 A G 0.28%
1043 A G 0.24%
1056 T C 0.2%
1086 A G 0.33%
1089 A G 0.22%
1213 A G 0.24%
1260 A C 0.3%
1264 T C 0.26%
1280 T C 0.25%
1281 T C 0.22%
1286 T C 0.2%
1339 T C 0.41%
1358 A G 0.26%
1398 T C 0.2%
1421 A G 0.31%
1460 A G 0.34%
1482 A G 0.24%
1580 T C 0.25%
1591 T C 0.29%

17. cat sorted_SRR1705859.vcf | grep -v "^#" | awk '{print $2, $4, $5, $10}' | awk -F '[ :]' '{print $1, $2, $3, $10}'
44 T C 0.47%
158 A G 0.24%
165 T C 0.27%
183 A G 0.22%
193 A G 0.22%
216 A G 0.24%
218 A G 0.29%
222 T C 0.25%
254 A G 0.19%
276 A G 0.24%
319 T C 0.23%
340 T C 0.21%
356 A G 0.24%
370 A G 0.21%
398 A G 0.22%
403 A G 0.19%
409 T C 0.19%
414 T C 0.22%
421 A G 0.18%
463 A G 0.19%
499 A G 0.21%
516 A G 0.2%
548 A G 0.19%
591 A G 0.19%
607 A G 0.18%
660 A G 0.27%
670 A G 0.28%
691 A G 0.23%
722 A G 0.23%
744 A G 0.25%
793 A G 0.17%
859 A G 0.29%
898 A G 0.2%
915 T C 0.21%
987 A G 0.22%
1031 A G 0.28%
1056 T C 0.19%
1086 A G 0.21%
1100 T C 0.21%
1213 A G 0.22%
1264 T C 0.21%
1280 T C 0.24%
1358 A G 0.25%
1366 A G 0.22%
1398 T C 0.23%
1421 A G 0.24%
1460 A G 0.37%
1482 A G 0.25%
1517 A G 0.24%
1520 T C 0.27%
1600 T C 0.35%
1604 T C 0.31%

18. cat sorted_SRR1705860.vcf | grep -v "^#" | awk '{print $2, $4, $5, $10}' | awk -F '[ :]' '{print $1, $2, $3, $10}'
38 T C 0.7%
44 T C 0.5%
95 A G 0.24%
105 A G 0.25%
133 A G 0.22%
158 A G 0.26%
165 T C 0.25%
183 A G 0.23%
199 A G 0.19%
216 A G 0.24%
218 A G 0.23%
222 T C 0.3%
228 T C 0.19%
230 A G 0.19%
235 T C 0.25%
254 A G 0.23%
271 A G 0.21%
276 A G 0.33%
297 T C 0.23%
319 T C 0.21%
340 T C 0.21%
356 A G 0.21%
370 A G 0.22%
389 T C 0.2%
409 T C 0.19%
414 T C 0.3%
421 A G 0.21%
463 A G 0.2%
499 A G 0.19%
566 A G 0.24%
597 A G 0.18%
607 A G 0.2%
660 A G 0.28%
670 A G 0.33%
691 A G 0.23%
722 A G 0.25%
744 A G 0.22%
759 T C 0.19%
859 A G 0.25%
915 T C 0.27%
987 A G 0.22%
1031 A G 0.26%
1043 A G 0.21%
1056 T C 0.2%
1086 A G 0.3%
1089 A G 0.22%
1105 A G 0.22%
1209 A G 0.27%
1213 A G 0.24%
1264 T C 0.27%
1280 T C 0.25%
1281 T C 0.21%
1301 A G 0.22%
1358 A G 0.29%
1366 A G 0.21%
1398 T C 0.23%
1421 A G 0.37%
1460 A G 0.26%
1482 A G 0.23%
1580 T C 0.27%
1604 T C 0.3%
