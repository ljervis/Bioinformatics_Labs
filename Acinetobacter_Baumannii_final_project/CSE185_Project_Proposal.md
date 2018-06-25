# Investigation into _Acinetobacter Baumannii_ biofilm production using differential gene expression analysis and functional gene annotation of sessile and planktonic cells

### Biological Question
_Acinetobacter Baumannii_ is a bacterium commonly found in hospital environments. It is a source of severe hospital born infections and the prevalence of multi drug resistant strains is on the rise. _A. baumannii_ has the ability to become sessile and form protective biofilms that can persist on abiotic surfaces. Formation of these biofilms also increases their resistance to drugs. The formation of biofilms is a complicated process that is currently under investigation. This project will compare the mRNA transcriptome expression profiles of free floating planktonic cells and sessile cells to gain an understanding into the mechanism by which A. baumannii form biofilms.      

### Dataset
The data that will be used is paired-end RNA-Seq data from an Illumina HiScanSQ sequencer in fasta format. The mRNA library sequenced was prepared using Illuminas Truseq RNA sample preparation protocol. Each of the two samples, sessile and planktonic, have two biological replicates for a total of four fasta files. The data was made publicly available on the SRA database. 

| Type | Replicate | Accession Number | File Format | File Size | 
| --- | --- | --- | --- | --- |
| Stationary | 1 | SRX263970 | fasta | 173.2Mb |
| Stationary | 2 | SRX263972 | fasta | 143.6Mb |
| Sessile | 1 | SRX263965 | fasta | 208.9Mb |
| Sessile | 2 | SRX263968 | fasta | 54.8Mb |

The data sets used were published by the following paper: 

Rumbo-Feal, Soraya et al. “Whole Transcriptome Analysis of _Acinetobacter__Baumannii_ Assessed by RNA-Sequencing Reveals Different mRNA Expression Profiles in Biofilm Compared to Planktonic Cells.” Ed. Gunnar F Kaufmann. _PLoS ONE_ 8.8 (2013): e72968. _PMC_. Web. 26 May 2018.

### Bioinformatics pipeline
The fasta files will be aligned to the _Acinetobacter Baumannii_ reference genome (GenBank: CP000521.1) using BowTie (version 1.2.2). Read annotation and coverage will be carried out using the R Bioconductor Genominator package. Gene expression will be quantified using Kallisto and differential expression analysis will be quantified using Sleuth. Blast2GO will then be used for functional annotation of identified genes. 
