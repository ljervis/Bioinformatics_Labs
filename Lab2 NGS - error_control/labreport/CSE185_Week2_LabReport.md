# Deep Sequencing of Influenza A Virus HA Genes  
# CSE 185 Week 2 Lab Report
##### Luke Jervis

## Abstract
This lab focused on an myself after I contracted the influenza A virus from my roommate. This was strange because a hemagglutination inhibition (HI) assay preformed on viral samples from my roomate resulted in a profile that closely matching that of the H3N2 strain. I had previously been vaccinated against this strain so how was this possible? Using sequencing data of HA genes from my roomates sample we used deep sequencing analysis to assess whether the virus was a quisispecies, with a portion of the viral population still able to infect me. We found seven common (> 95% frequency) and five statistically significant rare variants (>0.1% frequency) with three variants falling in the epitope regions of the hemeagglutinin genes.

## Introduction
The influenza A virus undergoes rapid mutagenesis, and a vaccine to fight against the virus is re-assessed for each new flu season.  When the vaccine is administered to an individual, the immune system produces antibodies that target the epitope regions of the viral surface protein hemagglutinin (HA). Antigenetic drift, or the accumulation of mutations in the epitope regions of the virus, decreases the antibodies binding affinity leading to a lower immune response toward the virus. "Antigenic variation constitutes one mechanism employed by influenza viruses to evade the adaptive response of the host immune system (Muñoz 2015)." Due to high mutation rates, the virus can exist as a quasispecies within a single host. Some population of the viral quasispecies may accumulate mutations protecting them from the antibodies that the vaccine helped create and rendering the host sick. 

It is well known that the flu vaccine is not completely effective and effectiveness can vary from year to year as different mutations accumulate and spread throughout the population. One method of determining the strain of virus an individual may be infected with is through a hemagglutination inhibition (HI) assay. This type of assay can test binding of antibodies against known flu strains. It is possible however that an infected individual who’s viral strain is covered by the vaccine according to the HI assay may still get sick. This may be due to rare variants populations in the quasispecies that have aquired mutations protecting them from the vaccine.  

Conventional sequencing of the virus can identify new strains but may miss important rare strains. If we increase the depth of our coverage we can identify rare variants with much lower frequency that may be causing the individual to get sick. This is the concept behind the targeted deep sequencing analysis used in this lab. When deep sequencing there are many sources of sequencing error that must be accounted for when predicting whether a variant is real. To account for any sequencer errors we compared with data from sequencing runs from isogenic samples and only identified variants that were greater that three standard deviations from these control runs as viable. 

## Methods
We started with Illumina single-end sequencing data in fastq format (roomate.fastq) from my roomates viral sample. We were also given three control sequences in fastq format from isogenic samples (SRR1705858.fastq SRR1705859.fastq SRR1705860.fastq). After inspection, we discovered that the files had already been trimmed of low quality bases. We used a reference sequence with assession ID KF848938.1 from NCBI for alignment. This sequence was downloaded in fasta format with the efetch function with nucleotide as the id flag and saved in a file titled KF848938.1.fasta. 

The reference genome file was indexed using the BWA tool with default options. All four fastq files were aligned to the reference KF848938.1.fastq file using the bwa mem tool with default settings and sorted/indexed using samtools with default settings, ultimatly saving to BAM files (roomate.bam SRR1705858.bam SRR1705859.bam SRR1705860.bam)

To find varients mpileup files were created for each of the bam files with the KF848938.1 reference sequence and a depth limit (-d) of 1000000. These files were saved (roommate.mpileup SRR1705858.mpileup SRR1705859.mpileup SRR1705860.mpileup). We used the tool VarScan with the mpileup2snp option set, the minimum varient frequency (--min-var-freq) set to 0.95 and the (--varients) flag set to produce a vcf file containing common varients from the roomate.mpileup file (roommate.vcf). We then ran VarScan on all mpileup files with the mpileup2snp option set, the minimum varient frequency (--min-var-freq) set to 0.001 and the (--varients) flag set to produce a vcf file in order to find rare varients and save them ( roommate_rare.vcf SRR1705858.vcf SRR1705859.vcf SRR1705860.vcf). 

The common varients in the roommate.vcf file were manually annotated using the online tool WebDSV to find amino acid changes. For all rare varients in the control vcf files (SRR1705858.vcf SRR1705859.vcf SRR1705860.vcf) the average frequency and standard deviation of all varients in each file was calculated using Microsoft Excel and saved (Week_2_Lab_Data.xlsx). WebDSV was used to annotate all varients from (roommate_rare.vcf) that had frequecies greater than three standard deviations from the averages in the control files. Statistically significant varients in epitope regions of the HA genes were identified using the epitope locations listed in Munoz et al(1). 

## Results
Reads were mapped to the reference KF848938.1 sequence using the BWA-MEM tool and the number of unmapped reads was used to find the information in table 1. 

#### Table 1. Sequence Read Information

| Sequence File | Initial Read Number | Mapped Read Number |
| ------------- | ------------------- | ------------------ |
| roommate.fastq | 286739 | 283309 |
| SRR1705858.fastq | 256586 | 256500 |
| SRR1705859.fastq | 233327 | 233251 |
| SRR1705860.fastq | 249964 | 249888 |

Varients with frequency cutoff at 0.1% were found using VarScan on alignments and the statistics in table 2 were gathered in Excel.

#### Table 2. Control Run Variant Statistics 

| Control Sequence | Frequency Average | Frequency Standard Deviation | 
| --- | --- | --- |
| SRR1705858 | 0.26% | 0.0717% |
| SRR1705859 | 0.24% | 0.0524% |
| SRR1705860 | 0.25% | 0.078% |

Variants with frequency cutoff at 95% were found using VarScan on the roommates alignment and manually annotated using WebDSV. The annotation for each common variant are shown in table 3. 

#### Table 3. Common Roommate Sequence Variants

| Original Codon | Mutated Codon | Original AA | Position | Mutated AA | Mutation Type |
| --- | --- | --- | --- | --- | --- |
| ACA | ACG | Thr | 24 | Thr | Synonymous |
| GCC | GCU | Ala | 39 | Ala | Synonymous |
| GCA | UCA | Ala | 119 | Ser | Missense |
| UUU | UUC | Phe | 258 | Phe | Synonymous |
| GCT | GCG | Ala | 336 | Ala | Synonymous |
| CTA | CTC | Leu | 420 | Leu | Synonymous |
| TTG | CTG | Leu | 447 | Leu | Synonymous |

Variants with frequency cutoff at 0.1% were found using VarScan on the roommates alignment and manually annotated using WebDVS. Rare variants with a frequency greater than three standard deviations away from the averages from the control runs were retained as being real variants. The annotations for each real rare variant are shown in table 4. 

#### Table 4. Rare Roommate Sequence Variants

| Original Codon | Mutated Codon | Original AA | Position | Mutated AA | Mutation Type |
| --- | --- | --- | --- | --- | --- |
| CTG | CCT | Leu | 13 | Pro | Missense |
| AAC | AAT | Asn | 165 | Asn | Synonymous |
| CTG | CTA | Leu | 431 | Leu | Missense |
| CTG | CTA | Leu | 507 | Leu | Synonymous |
| GCC | ACC | Ala | 304 | Thr | Missense |

Real variants that appeared in an epitope region as defined in the Munoz et al.(1) paper were identified and shown in table 5. 

#### Table 5. Epitope Variants

| Position | Epitope | 
| -------- | ------- |
| 165 | B |
| 304 | C |
| 117 | D |

## Discussion

After running VarScan on my roommates alignment with a minimum variant frequency of 0.1% there were 31 variants reported back. Of these, a majority had a very low variant frequency (<0.5%). Unfortunately, during any sequencing experiment there is a risk of errors both "upstream", before sequencing, and "downstream", during sequencing. "Upstream" errors can occur though copying mistakes, representation bias, contamination, etc. "Downstream" errors can occur during cluster generation or misincorporation of bases during synthesis. All of these sources of error should be taken seriously when preforming deep sequencing as rare variants have an inherently low frequency rate and the danger of falsely labeling an error as a "true" variant is high. In order to accurately label and quantify variants, controls must be put in place. 

In this lab we used three different sources of sequencing data derived from isogenic samples of the standard H3N2 influenza virus as controls. The control data was put through the same pipeline as the roommates data and found all rare "mutations". Because these samples were taken from a standard H3N2 source, the "mutations" that we found were assumed to be due to sequencing error. Using the average and standard deviation of the rare variant frequencies in these samples as a reference, we chose to only label variants in our roommates data as "true" variants if their frequency was greater than three standard deviations away from the average of the controls. We could now say with a much higher level of certainty that these selected variants were truly present in the roommates sample and not a product of sequencing error. 

There are additional way to control for error in deep sequencing experiments like this. We could have sequenced our samples again using another sequencing technology such as the PacBio sequencer which has different biases compared to the Illumina machine that was used to generate our data. The method of preparing the sample library could also be changed to reduce any errors that may occur during this phase. An example is Illuminas TruSeq PCR-free library prep protocol which can reduce library bias and coverage gaps. A third way of reducing error is through further use of bioinformatics quality control tools after sequencing. QuorUM is an example of bioinformatics software that can be used for read error correction pre-assembly. 

Through our analysis we identified three variants that occurred in the epitope region of the HA genes. Epitope regions are recognized by antibodies and mutations of these regions through antigenetic drift could prevent attachment of antibodies, protecting the virus from the immune system (1). Three epitope based mutations affecting the amino acids (117, 165, 304) were identified in this experiment.
These mutations provide a possible mechanism by which some of the viral species in my roommates sample could evade the flu vaccine. These variants were too rare to be shown in the HI profile which closely matched the H3N2 species that should have been covered by the flu vaccine. This presents a way by which I got the flu thru my roommate after receiving a flu shot. Further analysis could be completed on viral samples taken from myself as it is possible that someone other than my roommate gave me the virus.  

## Citations

(1.) Muñoz, Enrique T., and Michael W. Deem. “Epitope Analysis for Influenza Vaccine Design.” Vaccine 23.9 (2005): 1144–1148. PMC. Web. 15 Apr. 2018.
