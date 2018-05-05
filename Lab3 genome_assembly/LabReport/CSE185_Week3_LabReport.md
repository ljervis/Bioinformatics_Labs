# Assessment of de Bruijn based de novo assembly pipeline of _Staphylococcus aureus_ using FR and RF paired-end sequencing data 
## CSE 185 Week 3 Lab Report
##### Luke Jervis

## Abstract

The purpose of this study was to assess a de novo assembly pipeline. De novo assembly is a commonly used approach when analyzing NGS
data. The genome of the bacteria, _Staphylococcus aureus_ was sequenced. This genome is commonly used to benchmark assembly methods (1). After assessment we found our pipeline to be a viable method of de novo assembly, resulting in high coverage with an acceptable number of misassembly events.

## Introduction

De novo assembly is required for a number of situations. When sequencing a genome for which a reference has not been created a de novo 
approach is necessary. It is also necessary when the organism whose genome you are sequencing is unknown, such as in many non-model
organisms. Even when the genome does have an identified reference genome, the application of de novo assembly can be beneficial when
searching for large structural variations that may not be present in the reference (1). We began the investigation with data from two 
sequencing libraries, one paired-end with a forward/reverse directionality (FR), and the other paired-end with a reverse/forward (RF) 
directionality. The FR library was used in the initial assembly of contigs, or overlapping sequencing reads. A de Bruijn graph approach was used in this report. De Bruijn-graph-based approaches have been successful in assembling highly accurate short reads such as those used in our investigation (2). The second RF library 
was then used to scaffold our assembled contigs. Once fully assembled, the results were validated against a reference genome (NCBI reference 
id NC_010079)(11). 

## Methods

An overview of this investigations workflow is summarized in the list below:
1. Inspection of k-mer distribution 
2. K-mer based error correction
4. Inspection of corrected k-mer distribution
5. Assembly of contigs
5. Scaffolding
7. Gap filling
8. Validation of assembly

Initially we inspected the FR and RF libraries using fastqc (3) with default settings. Fastqc generated read quality plots for each fastq 
file which can be viewed in the results section. The frequency of all k-mers in the forward file from the FR library (frag_1.fasta) was 
evaluated with jellyfish (6) and saved to a histogram.  We used the jellyfish count command with the k-mer length (-m) set to 31, a 
hashtable size (-s) of 10000000, and the (-C) flag set to ignore directionality. This histogram was saved to the file 31.histo. To 
visualize the k-mer frequency histogram we created plots using Ipython (12) with the pandas and matplotlib libraries. These plots are shown 
in the results section. 

Next, k-mer based error correction was performed on the FR library (frag_1.fasta; frag_2.fasta) to replace low frequency k-mers with
similar high frequency k-mers. The KmerFreq_HA command from the SOAPdenovo2 package (8) was used to create a frequency hash table for use during correction. We used the 
KmerFreq_HA command with kmer-size (-k) set to 27, maximum read length (-L) set to 100 base pairs, initial hash table size (-i) set to 
10000000, output prefix (-p) set to prefix, and file list (-l) set to filelist (containing the names freq_1.fasta and freq_2.fasta). 
Correction of reads was achieved with the Corrector_HA command with k-mer size(-k) set to 27, quality ASCII shift (-Q) set to 33, 
output file (-o) set to 3, and low frequency cutoff (-l) set to 5. The corrected files were saved in fastq format and used for 
subsequent contig assembly. Jellyfish count was used with the same parameters as before to see how the distribution of k-mers changed 
in the corrected data (frag_1.fastq.cor.pair_1.fq). The histogram was also plotted using the same method as before and is show in the 
results section. 

Assembly of our corrected reads was achieved using the tool minia (7) with a list of corrected files (-in), k-mer size (-kmer-size) set 
to 31, minimum k-mer abundance size (-abundance-min) set to 2, and output (-o) set to assembled. The resulting contigs were analyzed 
for their statistics added to a class spreadsheet for comparison with others running the same lab with potentially different k-mer size 
(-kmer-size). The class results are in the CSE185_Week3_Section1_Class_Data file and N50 averages shown in the results section. The N50 value of our assembled contigs was obtained 
using the web tool QUAST (4). 

We next used the scaffolding tool SSPACE (9) to align the RF library files (short_jump_1.fastq; short_jump_2.fastq) to the contigs, then 
connect the contigs into larger scaffolds. A library file (sspace_library) was created for the SSPACE tool with both RF library files,
an insert size of 3426, an insert size error of 0.5, and the orientation RF. The SSPACE command was then used with the library (-l)
set to the sspace_library file, the list of contigs (-s) set to the minia output contig file, a minimum contig size (-z) of 100, output
prefix(-b) set to output_scaffold_prefix, a verbose (-v) output of 1, and dot file (-p) set to 1. 

To clean up our scaffolding input RF library we used the tool sickle (10) to trim both files with the forward fastq file (-f) set to 
short_jump_1.fastq, the reverse fastq file (-r) set to short_jump_2.fastq, the forward output (-o) set to trimmedfile1.fastq, the 
reverse output (-p) set to trimmedfile2.fastq, the quality type (-t) set to sanger, and the trimmed singles output (-s) set to 
singletons.fastq. SSPACE was run again on the trimmed RF files with the same options as before and there results were compared.
Closing of the scaffold gaps was attempted using the tool GapCloser (8). First we created a configuration file containing two libraries, 
one with the FR library, and one with the RF library. GapCloser was run with the scaffolds created by SSPACE (-a) set to 
output_scaffold_prefix_trimmed.final.scaffolds.fasta, the output file (-o) set to gap_closed_scaffolds.fa, maximum read length (-l) 
set to 100, and config file (-b) set to the configuration file we created, GapCloser.config. 

Finally, we compared our de novo aligned genome with the _Staphylococcus aureus_ reference genome fasta file and gene annotation 
(GFF form) on NCBI (accession id NC_010079). The analysis was done using the web tool QUAST. One report was made with the scaffolds, 
find gene boxes, and the prokaryotic button checked. Another report was made without the scaffolds box checked to visualize how our 
alignment matched up with the NCBI reference. 

## Results

Fastqc reports were created for each of the four library files (frag_1.fastq; frag_2.fastq; short_jump_1.fastq; short_jump_2.fastq). Figures 1-4 below display the per base sequence quality for reads in each fastq file. The full HTML reports can be found in the LabReport folder by clicking on the link below each image. 

#### Figure 1. Read Base Quality Graph for Frag_1.fastq

![alt text](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/LabReport/frag1_fastqc_quality.JPG "frag1 fastqc")

[fastqc report for FR library frag_1.fastq(HTML)](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/LabReport/frag_1_fastqc.html)

#### Figure 2. Read Base Quality Graph for Frag_2.fastq

![alt text](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/LabReport/frag2_fastqc_quality.JPG "frag2 fastqc")

[fastqc report for FR library frag_2.fastq(HTML)](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/LabReport/frag_2_fastqc.html)

#### Figure 3. Read Base Quality Graph for short_jump_1.fastq

![alt text](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/LabReport/short_jump1_fastqc_quality.JPG "shortjump1 fastqc")

[fastqc report for RF library short_jump_1.fastq(HTML)](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/LabReport/short_jump_1_fastqc.html)

#### Figure 4. Read Base Quality Graph for short_jump_2.fastq

![alt text](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/LabReport/short_jump2_fastqc_quality.JPG "shortjump2 fastqc")

[fastqc report for RF library short_jump_2.fastq(HTML)](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/LabReport/short_jump_2_fastqc.html)

Jellyfish and Ipython were used to create histograms of the k-mer frequency distribution of the read data contained in the FR library (frag_1) pre and post k-mer based error correction. Plots of these histograms are shown in figure 5 and figure 6 respectively. 

#### Figure 5. Kmer Freq Histogram Before Correction 

![alt text](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/kmer_freq_1_before_correction.png "kmer freq before correction")

#### Figure 6. Kmer Freq Hitogram After Correction

![alt text](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/kmer_freq_1_after_correction.png "kmer freq after correction")

Contigs were created using minia as described in the methods section. The results of assembly at each interm step are shown in table 1.

#### Table 1. Contig Statistics 

| Step | Number of Contigs | Max Contig Length | N50 |
| --- | --- | --- | --- |
| Post Contig Assembly | 718 | 80331 | 24652 |
| Post Scaffolding W/ Trimming| 423 | 120279 | 36115 |
| Post Scaffolding W/O Trimming | 282 | 258735 | 124060 |
| Post Gap Filling | 423 | 120279 | 36115 | 

Repeat studies using various k-mer lengths were completed. The average N50 values after assembly are shown in table 2. 

#### Table 2. Kmer Length vs. N50 Averages

![alt text](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/LabReport/N50%20vs.%20Kmer%20Length.JPG "kmer vs N50")

QUAST web tool was used for assessment of our assembly. An overview of the results are shown in figure 7.

#### Figure 7. QUAST Results After Gap Closing

![alt text](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/LabReport/Post%20Gap%20Closing%20QUAST%20No%20Scaffolds.JPG  "QUAST Results")

#### Figure 8. Icarus contig alignment viewer

![alt text](https://github.com/cse185-sp18/cse185-week3-ljervis/blob/master/LabReport/Contig%20Alignment%20Viewer.JPG "Icarus Results")

According to the QUAST documentation, the "broken" results can be used to assess whether the scaffolding step was helpful in the assembly of the genome. QUAST splits the "Gap_Closed_Scaffolds" fasta file that we provided into its contigs and assembles them to the reference genome without taking the scaffolds into account. As shown in figure 7, our alignment with scaffolding provided larger continuous blocks of alignment with the reference (Figure 7. largest contig, largest alignment, NGA50). 

97.896% of the reference genome was covered by our alignment in both the scaffold and "broken" alignments (Figure 7. Genome Fraction (%)). 

Both the scaffold and "broken" alignments had a mismatch rate of 5.33 mismatched per 100kbp aligned bases (Figure 7. # mismatches per 100 kbp).

There was one misassemble in both the scaffold and "broken" assemblies (Figure 7. # misassembles).

When viewing the alignment in the icarus browser Figure 8. Contigs that map in fragments are shown in red and blocks with erroneous but similar genomic coordinates are shown in orange (5).    

The full QUAST report can be found in in the LabReport folder. 

## Discussion

The assembly of _Staphylococcus aureus_ presented in this report resulted in a 97.896% coverage of the reference genome. The assembly covers almost the complete reference genome but there are 3 extensive and 27 local misassemble events as reported in the Icarus browser. The _Staphylococcus aureus_ is highly variable (1). This variability could account for some of the misassembles reported. According to NCBI (NC_010079)(11) there are 3,061 genes in the _Staphylococcus aureus_ genome. Quast's gene prediction tool found 2849 or 93% of total genes in our assembly. Many of the assembled scaffolds contain complete gene sequences but some genes overlap multiple scaffolds (Example: USA300HOU_RS07300, ID=gene1509, coordinates: 1466736-1467173). 

Further mate-pair sequencing of the genome with longer gaps than the ones used in our library (>3500bp) would improve our assembly and help connect the current scaffolds. Choice of k-mer length can have pronounced effects on the success of assembly and the ideal choice depends on the dataset. Longer k-mers are more unique and make assembly easier but increase error rate. Error correction can be preformed with high enough coverage (1). In this report k-mer lengths of 31bp were used. Repeat experiments with varying k-mer lengths were also preformed to compare contig assembly. Generally, higher k-mer length lead to larger contigs and N50 values for our data (Table 2.) As shown in this report the pipeline used offers an accurate method of de novo sequence assembly. Further studies with other genomes will be required to demonstrate the pipelines robustness.    

## Citations
(1.) Gymrek, MG. (2018). _cse185-spring18-week3._ UCSD.  
Department of Physics. (2012). Introductory physics handbook and lab manual (in italics). New York, NY: Best College.

(2.) Nagarajan, Niranjan, and Mihai Pop. “Sequence Assembly Demystified.” Nature Reviews Genetics, vol. 14, no. 3, 2013, pp. 157–167., doi:10.1038/nrg3367.

(3.) FastQC A Quality Control tool for High Throughput Sequence Data http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ by S. Andrews

(4.) Alexey Gurevich, Vladislav Saveliev, Nikolay Vyahhi and Glenn Tesler, 
QUAST: quality assessment tool for genome assemblies,
Bioinformatics (2013) 29 (8): 1072-1075. doi: 10.1093/bioinformatics/btt086

(5.) Alla Mikheenko, Gleb Valin, Andrey Prjibelski, Vladislav Saveliev, Alexey Gurevich,
Icarus: visualizer for de novo assembly evaluation,
Bioinformatics (2016) 32 (21): 3321-3323. doi: 10.1093/bioinformatics/btw379

(6.) Guillaume Marcais and Carl Kingsford, A fast, lock-free approach for efficient parallel counting of occurrences of k-mers. Bioinformatics (2011) 27(6): 764-770 (first published online January 7, 2011) doi:10.1093/bioinformatics/btr011

(7.) Chikhi R, Rizk G (2012). Space-efficient and exact de Bruijn Graph representation based on a Bloom Filter. WABI, Lecture notes in computer. Springer: Science and Publishing House.

(8.) Luo et al.: SOAPdenovo2: an empirically improved memory-efficient short-read de novo assembler. GigaScience 2012 1:18.

(9.) Boetzer M, Henkel VJ, Jansen HJ, Butler D and Pirovano W. 2011. Scaffolding pre-assembled contigs using SSPACE. Bioinformatics 27(4) p578-9.

(10.) Joshi NA, Fass JN. (2011). Sickle: A sliding-window, adaptive, quality-based trimming tool for FastQ files 
(Version 1.33) [Software].  Available at https://github.com/najoshi/sickle.

(11.) National Center for Biotechnology Information (NCBI)[Internet]. Bethesda (MD): National Library of Medicine (US), National Center for Biotechnology Information; [1988] – [cited 2018 Apr 16]. Available from: https://www.ncbi.nlm.nih.gov/

(12.) Fernando Pérez, Brian E. Granger, IPython: A System for Interactive Scientific Computing, Computing in Science and Engineering, vol. 9, no. 3, pp. 21-29, May/June 2007, doi:10.1109/MCSE.2007.53. URL: http://ipython.org
