# CSE 185 Lab Notebook - Week 4

Read count and read length for forelimb files:

`zcat FL_Rep1_chr5_1.fq.gz | wc -l
12717596`

`zcat FL_Rep1_chr5_1.fq.gz | head | awk '{ print length($0); }'`

__3179399 reads__

__50 bp reads__

Read count and read length for hindlimb files:

`zcat HL_Rep1_chr5_2.fq.gz | wc -l
15731352`

`zcat HL_Rep1_chr5_1.fq.gz | head | awk '{ print length($0); }'`

__3932838 reads__

__50 bp reads__

Read count and read length for midbrain files:

`zcat MB_Rep1_chr5_2.fq.gz | wc -l
13019900`

`zcat MB_Rep1_chr5_1.fq.gz | head | awk '{ print length($0); }'`

__3254975 reads__

__50 bp reads__

Ran fastqc on the the rep 1 and rep2 forelimb, hindlimb, and midbrain fastq files. 

Used samtools to view information about the alignment of RNA-Seq data to the reference transcriptome 

```
samtools view FL_Rep1_chr5.bam -H
@PG     ID:STAR PN:STAR VN:STAR_2.5.3a  CL:STAR   --runThreadN 4   --genomeDir m                m10STAR   --readFilesIn FL_Rep1_1.fastq.gz   FL_Rep1_2.fastq.gz      --readFiles                Command zcat      --outFileNamePrefix FL_Rep1   --outSAMtype BAM   SortedByCoord                inate
```

__STAR_2.5.3a Alignment Program Used__

__Reference genome used for alignment is mm10 Mouse__

Some of CIGAR scores had N operations, indicating that this region was skipped from the reference

"For mRNA-to-genome alignment, an N operation represents an intron. For other types of alignments, the interpretation of N is not defined." 

Downloaded IGV onto desktop and downloaded mm10 genome for viewing

Transfered all .tdf files to dektop and opened them in IGV

Pearson correlation between TPM values in each replicate:

` paste ./FL_Rep1/abundance.tsv ./FL_Rep2/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.99712632784422`

` paste ./FL_Rep1/abundance.tsv ./HL_Rep1/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.96063780258602`

` paste ./FL_Rep1/abundance.tsv ./HL_Rep2/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.95709385679504`

` paste ./FL_Rep1/abundance.tsv ./MB_Rep1/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.95751479760297`

` paste ./FL_Rep1/abundance.tsv ./MB_Rep2/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.94684196068136`

` paste ./HL_Rep1/abundance.tsv ./HL_Rep2/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.99559515606719`

` paste ./HL_Rep1/abundance.tsv ./FL_Rep1/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.96063780258602`

` paste ./HL_Rep1/abundance.tsv ./FL_Rep2/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.95942000208295`

` paste ./HL_Rep1/abundance.tsv ./MB_Rep1/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.93645656875347`

` paste ./HL_Rep1/abundance.tsv ./MB_Rep2/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.9269934429212`

` paste ./MB_Rep1/abundance.tsv ./MB_Rep2/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.99161833933741`

` paste ./MB_Rep1/abundance.tsv ./FL_Rep1/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.95751479760297`

` paste ./MB_Rep1/abundance.tsv ./FL_Rep2/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.96005923363607`

` paste ./MB_Rep1/abundance.tsv ./HL_Rep1/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.93645656875347`

` paste ./MB_Rep1/abundance.tsv ./HL_Rep2/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
0.93546002000061`

## Part II

Significant results from sleuth outputted to sleuth_results.tab 

`wc -l sleuth_results.tab`

There were 1940 significant results outputted by sleuth

Top 10 results

Gene: Rpl21

Gene: Shh

Gene: Uchl1

Gene: Sparcl1

Gene: Parm1

Gene: Nat8l

Gene: Garem2

Gene: Ubl3

Gene: Hmgn2

Gene: Gltp

Pscp .bedGraph files to desktop and loaded them into the IGV Browser

Downloaded the PhyloP data set from http://genome.ucsc.edu to view base-pair species conservation. 

Used mafft to preform multiple sequence alignment (MSA)

`mafft $public_dir/week4/zrs_sequences.fa > mafft_output.fa`

Used mview to create html file to visualize MSA

`mview -html full mafft_output.fa > mafft_output.html`

Found one region that is shared in all tracks except snakes 





















