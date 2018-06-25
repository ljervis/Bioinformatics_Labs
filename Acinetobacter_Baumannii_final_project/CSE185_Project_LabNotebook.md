# Lab notebook for CSE185 Final Project

## Possible Datasets

#### Idea 1

RNA-Seq identifies novel myocardial gene expression signatures of heart failure
GEO Accession: GSE57345

#### Idea 2

[Article](https://www.nature.com/articles/nprot.2012.016)
Differential gene and transcript expression analysis of RNA-seq experiments with TopHat and Cufflinks


#### Idea 3 

[Article](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0072968)
Differential analysis of mRNA from stationary and biofilm Acinetobacter baumannii ATCC 17978 

Tools used in paper-
* HiScanSQ Illumina sequencer to generate 50 base pair reads for each sample 
* Aligned against reference genome using Bow Tie (max three mismatches within the first 50 bases)
* Reads annotated with Bioconductor Genominator 
* Gene expression estimated with DESeq 
* Functional re-annotation of genes with Blast2GO 

Raw sequences in SRA 
 
| Type | Replicate | Accession Number |
| --- | --- | --- |
| Stationary | 1 | SRX263970 | 
| Stationary | 2 | SRX263972 |
| Biofilm | 1 | SRX263965 | 
| Biofilm | 2 | SRX263968 |

--------

My plan is to use the stationary and biofilm replicate fastq files, align, find gene expression, and annotate. I will then compare the results of my pipeline with the results in the paper.

--------

fastqc ran on all fasta files. Results available in Fastqc folder.

Sickle was used to trim the reads and increase their quality.

```
sickle pe -options -f SRX263965_1.fastq -r SRX263965_2.fastq -t sanger -o ./Fastqc/SRX263965_1_trimmed.fastq -p ./Fastqc/SRX263965_2_trimmed.fastq -s ./Fastqc/SRX263965_trimmed_singles.fastq

PE forward file: SRX263965_1.fastq
PE reverse file: SRX263965_2.fastq

Total input FastQ records: 6207670 (3103835 pairs)

FastQ paired records kept: 5425432 (2712716 pairs)
FastQ single records kept: 365138 (from PE1: 26174, from PE2: 338964)
FastQ paired records discarded: 51962 (25981 pairs)
FastQ single records discarded: 365138 (from PE1: 338964, from PE2: 26174)
```

Reran fastqc to see quality change 

```
fastqc -o . SRX263965_1_trimmed.fastq SRX263965_2_trimmed.fastq 
```

fasta files were aligned to the Acinetobacter baumannii ATCC 17978, complete genome (CP000521.1). 

Biofilm - SRX263968

```
bowtie -S ./RefSeq/AB -1 SRX263968_1.fastq -2 SRX263968_2.fastq SRX263968.sam
# reads processed: 852311
# reads with at least one reported alignment: 575510 (67.52%)
# reads that failed to align: 276801 (32.48%)
Reported 575510 paired-end alignments

cut -f3 SRX263968.sam | grep -c \*
553602

 grep -c "^SR" SRX263968.sam
1704622
```
1704622 - 553602 = __1151020__ aligned reads


Biofilm - SRX263965

```
bowtie -S ./RefSeq/AB -1 SRX263965_1.fastq -2 SRX263965_2.fastq SRX263965.sam
# reads processed: 3103835
# reads with at least one reported alignment: 2760957 (88.95%)
# reads that failed to align: 342878 (11.05%)
Reported 2760957 paired-end alignments

cut -f3 SRX263965.sam | grep -c \*
685756
grep -c "^SR" SRX263965.sam
6207670
```
6207670 - 685756 = __5521914__ aligned reads

Stationary - SRX263970

```
bowtie -S ./RefSeq/AB -1 SRX263970_1.fastq -2 SRX263970_2.fastq SRX263970.sam
# reads processed: 2569359
# reads with at least one reported alignment: 2305419 (89.73%)
# reads that failed to align: 263940 (10.27%)
Reported 2305419 paired-end alignments

cut -f3 SRX263970.sam | grep -c \*
527880

grep -c "^SR" SRX263970.sam
5138718
```
5138718 - 527880 = __4610838__ aligned reads 


Stationary - SRX263972

```
 bowtie -S ./RefSeq/AB -1 SRX263972_1.fastq -2 SRX263972_2.fastq SRX263972.sam
# reads processed: 2123702
# reads with at least one reported alignment: 1844361 (86.85%)
# reads that failed to align: 279341 (13.15%)
Reported 1844361 paired-end alignments

cut -f3 SRX263972.sam | grep -c \*
492786

grep -c "^SR" SRX263972.sam
3712832
```
3712832 - 492786 = __3220046__ aligned reads 

reads that were aligned using bowtie and reference genome CP000521.1 

| Type | Replicate | Accession Number | Reads Aligned |
| --- | --- | --- | --- |
| Stationary | 1 | SRX263970 | 4610838 |
| Stationary | 2 | SRX263972 | 3220046 |
| Biofilm | 1 | SRX263965 | 5521914 |
| Biofilm | 2 | SRX263968 | 1151020 |

Ran kallisto on all data sets. The script can be found in the /scripts folder. Supplied a gtf file found online. The manual for kallisto can be found here [kallisto manual](https://pachterlab.github.io/kallisto/manual)

Downloaded IGV genome browser. Loaded the Acinetobacter baumannii ATCC genome into the browser. 

Pearson correlation between kallisto outputs:
```
paste /home/linux/ieng6/oce/8m/ljervis/FinalProject/kallisto_output/SRX263965/abundance.tsv /home/linux/ieng6/oce/8m/ljervis/FinalProject/kallisto_output/SRX263968/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
```

After much trial and error I have realized that kallisto needs a reference transcriptome and will only display counts per chromosome if given a genome. As I am working with a bacteria that has one chromosome there was only one row in my abundance.tsv file. It took me longer than I would like to admit to figure this out. After searching for some time I was unable to find a reference transcriptome for AB so I will now try and find a different tool to find differential gene expression. 

I downloaded bowtie2 and tophat2 onto ieng6 server. I then repeated alignment to the genome with tophat. 

```
tophat ../RefSeq/AB ../SRX263965_1.fastq ../SRX263965_2.fastq --output-dir=./SRX263965/
```

This is currently being repeated for all four samples.

cufflinks was run to find novel transcripts. 

cufflinks was taking way to long so I decided to try something else.  

Used gffread to generate fasta file from gtf file and reference genome (CP018664.1)

```
./gffread -w ../FinalProject/RefSeq/CP018664.1.transcripts.fa -g ../FinalProject/RefSeq/CP018664.1.fasta.fai ../FinalProject/RefSeq/genomicgff.gtf
```
I have now created a transcript fasta file that I can use with kallisto for gene abundance analysis.

```
kallisto quant -t 3 -i CP018664.1.kallisto.idx -o ../KallistoOutput/ -b 100 ../SRX263965_1.fastq ../SRX263965_2.fastq
```
^^ this finally worked! 

I am now going to run pearson correlation between the samples for a sanity check. 

```
 paste ./SRX263965/abundance.tsv ./SRX263968/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
```

| ------- | SRX263965 | SRX263968 | SRX263970 | SRX263972 | 
| ------- | ------- | ------- | ------- | --------| 
| SRX263965 | ----- | 0.955 | 0.835 | 0.972 |  
| SRX263968 | 0.955 | ----- | 0.756 | 0.941 | 
| SRX263970 | 0.835 | 0.756 | ----- | 0.886 | 
| SRX263972 | 0.972 | 0.941 | 0.886 | ----- | 

ran sleuth on all samples

checking the number of results 

```
wc -l sleuth_results.tab
131 sleuth_results.tab
```

---

Downloaded reference genome NC_009085.1 and .gff3

converted .gff3 to .gtf with cufflinks gffread tool

```
./gffread ../FinalProject/RefSeq/NC_009085.1.gff3 -T -o ../FinalProject/RefSeq/NC_009085.1.gtf
```

used the reference genome and gtf file to create a fasta file 

```
./gffread -w ../FinalProject/RefSeq/NC_009085.1.transcripts.fa -g ../FinalProject/RefSeq/NC_009085.1.fa ../FinalProject/RefSeq/NC_009085.1.gtf
```

made an index file for this fasta file 

```
kallisto index --index=NC_009085.1.kallisto.idx NC_009085.1.transcripts.fa
```

used this index to quantify transcript abundance 

``` 
kallisto quant -t 3 -i NC_009085.1.kallisto.idx -o ../KallistoOutputNC_009085.1/ -b 100 ../SRX263965_1.fastq ../SRX263965_2.fastq
```
Repeated for each sample 

sleuth was then used to find differentially expressed genes

The scripts will be on github

PCA and count distributions were plotted

```
plot_pca(so, color_by='condition')
plot_group_density(so, use_filtered=TRUE, units="est_counts", trans="log", grouping = setdiff(colnames(so$sample_to_covariates), "sample"), offset=1)
```

I ran kallisto and sleuth using the same procedure on two different reference genomes. Both the one used in the paper (NC_009085.1) and another one (CP018664.1). When I looked up the one used in the paper on NCBI nucleotide database the following warning appeared:

```
This RefSeq record was removed because data validation identified problems with the assembly or annotation
```

For this reason I used the second reference genome and compared the results between the two. 

Loaded up sleuth and preformed a likelihood ratio test (lrt). After creating the sleuth model we fit the model to a full and reduced model and used them for the lrt. 

What this has accomplished is to “smooth” the raw kallisto abundance estimates for each sample using a linear model with a parameter that represents the experimental condition (in this case DS vs. WW). To test for transcripts that are differential expressed between the conditions, sleuth performs a second fit to a “reduced” model that presumes abundances are equal in the two conditions. To identify differential expressed transcripts sleuth will then identify transcripts with a significantly better fit with the “full” model.

saved the significant results (qval <= 0.05) to sleuth_results_NC_009085.1 

Next I preformed a wald test and saved the significant results: sleuth_results_wald_test_NC_009085.1

saved the sleuth object: sleuth_object_NC_009085.1

Create a sleuth live object for visualization.

Next step is to compare my results with the papers results. 

I went ahead and ran kallisto and sleuth starting with the trimmed fastq files for comparison.

```
kallisto quant -t 3 -i ./RefSeq/NC_009085.1.kallisto.idx -o ./KallistoOutputTrimmedNC_009085.1/ -b 100 ./Fastqc/SRX263965/SRX263965_1_trimmed.fastq ./Fastqc/SRX263965/SRX263965_2_trimmed.fastq
```

loaded up sleuth and created a sleuth object "sleuth_object_trimmed_NC_009085.1"

Preformed an lrt test and saved the results in "sleuth_results.tab"

Preformed a wald test and save the results in "sleuth_results_WT.tab"

I am now going to run pearson correlation between the samples for a sanity check. 

```
 paste ./SRX263965/abundance.tsv ./SRX263968/abundance.tsv | cut -f 5,10 | grep -v tpm | awk '(!($1==0 && $2==0))' | datamash ppearson 1:2
```

| ------- | SRX263965 | SRX263968 | SRX263970 | SRX263972 | 
| ------- | ------- | ------- | ------- | --------| 
| SRX263965 | ----- | ----- | ----- | ----- |  
| SRX263968 | 0.993 | ----- | ----- | ----- | 
| SRX263970 | 0.964 | 0.982 | ----- | ----- | 
| SRX263972 | 0.966 | 0.983 | 1.000 | ----- | 