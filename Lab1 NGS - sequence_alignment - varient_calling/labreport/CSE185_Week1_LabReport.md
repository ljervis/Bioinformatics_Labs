# Week 1 Lab Report 
##### Luke Jervis

## Abstract

The goal of this lab was to identify causes of ampicillin antibiotic resistance in a strain of E. coli. Identification of mutations responsible for conferring antibiotic resistance were found through sequence analysis using paired end sequencing reads in fastq files and a reference genome in a fasta file. Identifying the mechanism of resistance is an important discovery as it can be used by clinicians when deciding the most effective treatment for a patient who is infected with this particular strain of E. coli. This knowledge can also be used by scientists interested in creating new drugs to battle antibiotic resistant E coli. It was identified that this particular strain of E. coli was likely to be conferring resistance by reducing the amount of ampicillin in the cell.   

## Introduction

The common course of action when a patient is diagnosed with an E. coli bacterial infection is to prescribe the antibiotic ampicillin. Unfortunately there are strains of E coli. that are resistant to this antibiotic, making treatment with ampicillin less effective. Ampicillin targets the protein transpeptidase which is responsible for cross linking peptidoglycan. Disruption of transpeptidase impedes the bacteria’s ability to synthesize a cell wall leading to death. Other antibiotics have different cellular targets like the cell membrane, essential enzymes, protein synthesis. Antibiotics can be either bacteriostatic, stopping the bacteria from reproducing while not necessarily killing them. Other antibiotics are bactericide, killing the bacteria themselves. Ampicillin is an example of a bacteriostatic antibiotic. Unfortunately bacteriostatic antibiotics are at higher risk of conferring resistance because advantageous mutations that bacteria may acquire can be shared with others in the population even though the individual is unable to reproduce. 

In this report we are concerned with identifying the specific mutations and mechanisms by which an ampicillin resistant bacteria strain is conferring resistance. We will do this by analyzing and comparing the genome of our resistant strain against a non-resistant, reference genome. Mutations within gene coding regions that change the resultant proteins amino acid sequence are researched to help identify possible functionality changes. This knowledge is used to propose the mechanism of resistance behind the mutation.                
This research is important because it adds to the available body of knowledge giving physicians valuable information that can be used to effectively prescribe antibiotics to patients with bacterial infections. Due to falling costs of whole genome sequencing it is becoming possible to culture and sequence patients with infections in less than a week. this can "simultaneously reveal mutations and acquired genes that bestow resistance to many antibiotics" and provide much more information than the "handful of known resistance markers" searched by common PCR reactions (Peacock 2014). 

## Methods

We started with raw paired-end sequencing data of an ampicillin resistant strain of E coli. These were stored in two fastq files. The raw reference genome was stored in the one fasta file: NC_000913.3.fasta. We began analysis by running the paired-end sequencing data through fastqc with default settings, a simple fastq statistics analysis program. This produced two files that gave us a visual representation of the quality of our sequenced reads. To increase the quality of our reads we ran the paired-end sequencing data through a trimming tool called sickle with default settings and again with quality set to 30. For the rest of the analysis the two trimmed, paired-end fastq files outputted by sickle with default settings were used. 

Next, we aligned these two trimmed, paired-end fastq files to the reference genome. The reference genome was indexed using the bwa algorithm with default settings and BWA-MEM was used to align the two trimmed, paired-end fastq files with default settings. The results were saved in a SAM file for further analysis. The SAM file was compressed to a BAM file using Samtools with default settings. The resultant BAM file was sorted and indexed also using Samtools with default settings. This sorted and indexed BAM file was visually inspected using the Samtools command tview with default settings. Next, mutations were identified by first creating an mpileup file with default settings. The resultant mpileup file was ran through the variant scanner, varscan with a threshold of 70% and saved to a VCF file. 

Identification of variant locations and protein changes were found with the online tool, Ensemble Variant Effect Predictor. The VCF file was first modified using the AWK command available in the labreport folder before uploading to Ensemble Variant Effect Predictor. Genes involved in mutations that resulted in changes in the amino acid sequence of proteins were manually researched for functionality using the online resources Ecoli Wiki and google.            

## Results

Coverage of the reference genome through paired-end sequencing: 155X

Paired-end sequencing data was ran through fastqc, results can be viewed in the amp_res_1_fastqc.html and amp_res_2_fastqc.html files found in the labreport folder. The per-base sequence quality of both paired-end sequencing files was marked red in these files and upon visual inspection it is apparent that as the read length grew the quality of the bases decreased. 

A trimming tool called sickle was used to increase the quality of the reads in the sequencing data files. The trimmed files were ran through fastqc and the results can be viewed in the trimpair1_fastqc.html and trimpair2_fastqc.html files found in the labreport folder. The per-base sequence quality of both paired-end sequencing files was marked green in these files indicating that the reads were trimmed to an acceptable average quality for further analysis.  

Information regarding the location of the identified mutations and the type of change they created in the resulting amino acid sequence was found by uploading our modified VCF file to Ensemble Variant Effect Predictor. Important results of this analysis are shown in the table below. 

| Location | Type | Gene Name | Mutation | Substitution |
| -------- | ---- | --------- | -------- | ------------ |
| 92439 | Gene | b0084 | Missense | A |
| 803662 | Gene | b0771 | Missense | A |
| 852762 | Non-Coding | NA | NA | NA |
| 1905761 | Gene | b1821 | Missense | A |
| 3535147 | Gene | b3404 | Missense | C |
| 4390754 | Gene | b1461 | Synonymous | T | 

The following table summarizes the initial number of reads in our sequencing data files, the number retained after trimming and the number that aligned to the reference genome.

| Initial Read Count | Post-Trimming Read Count | Aligned Read Count | 
| ------------------ | ------------------------ | ------------------ |
| 7107040 | 6904494 | 6899109 |

EcoliWiki and google was used to gather information about the genes that were affected by these mutations and possible cellular effects of the mutations. The results are summarized in the table below. 

| Gene Name | Function | Possible Cellular Effects |
| --------- | -------- | ------------------------- |
ftsl | Filamentation, temperature sensitive | thermosensitive cell lysis and filamentation resulting from inhibition of cell division; at lower cell density more pronounced thermosensitive growth was observed | 
ybhj | Predicted Hydratase | No known effects |
mntp | putative efflux pump | Deletion of mntP leads to profound manganese sensitivity and to elevated intracellular manganese levels |
envz | Osmosensor histidine protein kinase/phosphatase | regulates production of outer membrane proteins |
rsga | GTPase A | No known effect |

## Discussion

Missense mutation of the mntP gene was interesting because it codes for a protein efflux pump. As we have learned, one of the ways in which bacteria acquire antibiotic resistance is through mutations that cause the drug to be pumped out of the cell. This missense mutation could give rise to a gain of function mutation that increases the bacteria’s ability to pump the ampicillin out of the cell thus resisting its effects. 

Also interesting is the mutation in the envZ gene coding for a protein kinase that regulates production of outer membrane proteins. As we have learned ampicillin affects the cell wall by inhibiting transpeptidase. This mutation could lead to higher production of membrane proteins that decrease the cells permeability to ampicillin stopping it from entering and inducing its effects.   

Finally, the mutation of gene ftsL may also be of interest as it codes for a protein involved in filamentation and temperature sensitivity. A mutation in this gene could increase growth response or alter a metabolic pathway to compensate for the degenerative affects of ampicillin. 

Given all the data we have gathered and my research I would hypothesize that this strains main mechanism of resistance is by reducing the amount of drug in the cell by efflux pumps and decreasing permeability. Given this hypothesis I would recommend a hydrophobic antibiotic such as a cephalosporin.  

Whole genome sequencing of this strain may have identified rare mutations that normal PCR based tests would not have tested for, thus providing us with a more thorough understanding of mutations in this strain.   

## Citations
Peacock, Sharon. “Health Care: Bring Microbial Sequencing to Hospitals.” Nature, vol. 509, no. 7502, 2014, pp. 557–559., doi:10.1038/509557a.
