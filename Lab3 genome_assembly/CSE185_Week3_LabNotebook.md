# CSE 185 Lab Notebook - Week 3

## Part I

### Step 1
Cloned github repo into week 3 folder on ieng6-700.ucsd.edu server

Copied __frag_1.fastq frag_2.fastq short_jump_1.fastq short_jump_2.fastq__ into week 3 directory 

Found the number of reads in each file from the line count / 4:

`wc -l short_jump_2.fastq
4445728 short_jump_2.fastq`

1111432 reads

`wc -l short_jump_1.fastq
4445728 short_jump_1.fastq`

1111432 reads 

`wc -l frag_2.fastq
6230376 frag_2.fastq`

1557594 reads

`wc -l frag_1.fastq
6230376 frag_1.fastq`

1557594 reads

Ran fastqc on each of the four .fasta files:

`fastqc -o . frag_1.fastq frag_2.fastq short_jump_1.fastq short_jump_2.fastq`

Created an html and zip file for each input file

Transferd all four html to desktop using pscp 

Used the k-mer counting program Jellyfish to count the frequency of k-mers in our data

`jellyfish count -m 31 -s 10000000 -o 31 -C frag_1.fastq`

Created a hito file

`jellyfish histo 31 > 31.histo`

Used Ipython to create a visual histogram .pdf file 

```
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
plt.figure()
r31 = pd.read_csv("31.histo", sep=" ", names=["kmercount", "number"])
plt.bar(r31.iloc[1:100,]["kmercount"], r31.iloc[1:100,]["number"]);
plt.savefig("frag_1_31.pdf")
```

The bin labled __five__ in the 31.histo file corrosponds to the first valley in the .pdf figure 

We are using error correction modules from __SOAPdenovo2__ to run k-mer error correction on the __frag_1.fastq__ and __frag_2.fastq__ files. 

First a test file with the list of files we want to process was created with emacs.

`KmerFreq_HA -k 27 -L 100 -i 10000000 -p prefix -l filelist`

This created the files: prefix.freq.stat prefix.freq.gz

Read correction was done with the following corrector command with the valley point (-l flag) set to bin 5.

`Corrector_HA -k 27 -Q 33 -o 3 -l 5 prefix.freq.gz filelist`

This created a number of files including __frag_1.fastq.cor.pair_1.fq frag_2.fastq.cor.pair_2.fq__

We used jellyfish to see how the distribution of k-mers differed from the collected data:

`jellyfish count -m 31 -s 10000000 -o 31corrected -C frag_1.fastq.cor.pair_1.fq
jellyfish histo 31corrected > 31corrected.histo`

Used Ipython to create a file __frag_1_corrected31.pdf__ using the same proccess as before

Found the number of reads in the corrected files:

`wc -l frag_1.fastq.cor.pair_1.fq
4217408 frag_1.fastq.cor.pair_1.fq`

1054352 reads

` wc -l frag_2.fastq.cor.pair_2.fq
4217408 frag_2.fastq.cor.pair_2.fq`

1054352 reads

Valley point of 31corrected.histo is bin __2__ and first peak is bin __14__

Found the new average read length of the corrected files using the awk command

`awk 'NR%4==2{sum+=length($0)}END{print sum/(NR/4)}' frag_1.fastq.cor.pair_1.fq`

average read length frag_1 95.6211

`awk 'NR%4==2{sum+=length($0)}END{print sum/(NR/4)}' frag_2.fastq.cor.pair_2.fq`

average read length frag_2 93.3242

Found the number of bases in the corrected files using the awk command.

`awk 'NR%4==2{sum+=length($0)}END{print sum}' frag_1.fastq.cor.pair_1.fq`

100818279 bases 

`awk 'NR%4==2{sum+=length($0)}END{print sum}' frag_2.fastq.cor.pair_2.fq`

98396570 bases 

Estimated the genome size of our bacteria with the following formula:

N = (M*L)/(L-K+1) Genome_size = T/N

Assembled the corrected reads with the tool minia setting the kmer size to 31

```
minia -in corrected_list -kmer-size 31 -abundance-min 2 -out assembled
 -in                                      : corrected_list
    -kmer-size                               : 31
    -abundance-min                           : 2
    -out                                     : assembled
    -traversal                               : contig
    -starter                                 : best
    -contig-max-len                          : 10000000
    -bfs-max-depth                           : 500
    -bfs-max-breadth                         : 20
    -fasta-line                              : 0
    -abundance-max                           : 4294967295
    -histo-max                               : 10000
    -solidity-kind                           : sum
    -max-memory                              : 2000
    -max-disk                                : 0
    -out-dir                                 : .
    -minimizer-type                          : 0
    -minimizer-size                          : 8
    -repartition-type                        : 0
    -bloom                                   : neighbor
    -debloom                                 : cascading
    -debloom-impl                            : minimizer
    -branching-nodes                         : stored
    -topology-stats                          : 0
    -mphf                                    : emphf
    -nb-cores                                : 8
    -verbose                                 : 1
    -integer-precision                       : 0
    -verbose                                 : 1
    stats
        traversal                                : contig
        start_selector                           : best
        nb_contigs                               : 2744
        nb_small_contigs_discarded               : 3318
        nt_assembled                             : 2963417
        max_length                               : 22159
        max_length_left                          : 15880
        max_length_right                         : 17697
        debugging traversal stats
        large breadth                            : 0
        large depth                              : 13
        marked kmer inside traversal             : 2474
        traversal ends with dead-ends            : 1223
        in-branching large depth                 : 746
        in-branching large breadth               : 30
        in-branching other                       : 169
        couldn't validate consensuses            : 815
    time                                     : 29.251
        assembly                                 : 29.251
```


Found the number of contigs in the assembled file

`wc -l assembled.contigs.fa
1436 assembled.contigs.fa`

718 contigs 

Found the longest and the shortest contigs in the file

`cat assembled.contigs.fa | awk 'NR%2==0{print length}' | sort -n | head`

`cat assembled.contigs.fa | awk 'NR%2==0{print length}' | sort -n | tail`

shortest contig: 63

longest contig: 80331 

Used a web tool called QUAST to analyse the contig file.

N50 value: 24652

## Part II

Used Excel to create scatter plots with class data

Increasing the kmer size increased the max contig length and the N50 value. This indicates that a larger kmer size results in a __better__ assembly. 

Used the short jump library to scaffold minia contigs 

First created a library file __sspace_library__ for use with SSPACE tool sspace_library with the following parameters 

`Lib1 short_jump_1.fastq short_jump_2.fastq 3426 0.5 RF`

Used SSPACE tool to create scaffold 

`SSPACE_Basic_v2.0.pl -l sspace_library -s assembled_2.contigs.fa -z 100 -v 1 -p 1 -b output_scaffold_prefix`

Number of scaffolds "After scaffolding": 282

Max scaffols size: 258735

N50: 124060

Used Sickle to trimm low quality bases from fastq files

```
sickle pe -options -f short_jump_1.fastq -r short_jump_2.fastq -t sanger -o trimmedfile1.fastq -p trimmedfile2.fastq -s singletons.fastq

PE forward file: short_jump_1.fastq
PE reverse file: short_jump_2.fastq

Total input FastQ records: 2222864 (1111432 pairs)

FastQ paired records kept: 16502 (8251 pairs)
FastQ single records kept: 62192 (from PE1: 57101, from PE2: 5091)
FastQ paired records discarded: 2081978 (1040989 pairs)
FastQ single records discarded: 62192 (from PE1: 5091, from PE2: 57101)
```

Reran SSPACE with trimmed fastq files

Number of scaffolds "After scaffolding": 423

Max scaffold size: 120279

N50 = 36115

Closing the gaps in the scaffolds with GapCloser

Created __GapCloser.config__ file 

`GapCloser -a output_scaffold_prefix_trimmed.final.scaffolds.fasta -o gap_closed_scaffolds.fa -l 100 -b GapCloser.config`

Used QUAST to assess quality of assembly. 

Downloaded __NC_010079.1__ FASTQ and GFF3 files

Uploaded these files and __gap_closed_scaffold.fa__ to QUAST for assessment 

