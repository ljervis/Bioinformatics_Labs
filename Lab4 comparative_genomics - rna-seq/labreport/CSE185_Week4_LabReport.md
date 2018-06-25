
# Comparative Genomics Investigation of Limb Development Across Species
##### Luke Jervis

## Abstract 

In this report we use comparative genomics techniques to identify genes and regulatory regions potentially involved in limb development. We identified possible genes and genetic modifications contributing to the development of limbs in some species and not others (e.g. snakes) . A bioinformatics pipeline analyzing RNA-Seq data from three different developing mouse tissues was used in this study to identify differentially expressed genes.  ChIP-sequencing (5.) and base-pair species conservation data were used to analyse a target enhancer regions involved in limb development (6.). We identified 1940 significant (qval <= 0.05) deferentially expressed genes between the three mouse tissues. The *Shh* gene and its enhancer region *ZRS* were targeted, and a region of the highly conserved *ZRS* enhancer sequence was identified as showing divergence in non-limb forming snake species. Additional research regarding this sequence is suggested. Furthermore, the approach used in this study provides a viable method for future comparative genomics studies and the identified regions can be used as targets for limb malformation studies.  

## Introduction and Background Information 

This study used comparative genomics to identify regions of the genome that are involved in limb development. The amount of RNA produced for each gene correlates with the amount of protein product being produced in that tissue, leading to phenotypic expression such as the growth of limbs vs. no limbs. Levels of RNA transcript between tissue types can be used to identify the specific genes being activated in those tissues. In this study, differential gene expression between tissue types was quantified by analyzing RNA-Seq data and used to identify genes and regulatory regions involved in limb formation. 

Epigenetic histone modifications on enhancer and promoter regions is one way tissue specificity is achieved in tissue types. Identification of regions that may be involved in producing a particular phenotype is possible through quantitative analysis of these histone modifications. In this study, we used ChiP-Sequencing data along with our differential expression analysis to identify enhancer regions that are involved in limb formation. Once a region is identified as producing up regulation of a target gene (though histone modification) and shows conservation across species, multiple sequence alignment (MSA) between species can be used to identify specific regions showing differentiation. In this study we use MSA on the conserved *ZRS* enhancer region to identify sequence level differences between limb forming and non-limb forming species. 

Using these techniques, we identified both genes and enhancer regions that are involved in limb development. We hope that the identification of these regions can provide targets for further research on limb development and malformations. Furthermore, we hope that the methods used in this study can be applied to other important biological and medical questions that are lacking in a genetic basis.  
 
## Methods

### RNA-seq datasets

The RNA-Seq data sets used in this study originated from a developing mouse. Two replicate RNA-Seq sample data sets were taken from three tissue locations: hind limb (HL), fore limb (FL), and mid-brain (MB). The replicates were used to help mitigate any errors in the sequencing process and assess our pipeline. More information about the sequencing data sets that were used can be found in the table below. 

| Tissue/Replicate | Number of Reads | Read Lengths (bp's) | Sequecing Type |
| --- | --- | --- | --- | 
| HL/1 | 3932838 | 50 | paired end |
| HL/2 | 2811913 | 50 | paired end |
| FL/1 | 3179399 | 50 | paired end | 
| FL/2 | 2965029 | 50 | paired end |
| MB/1 | 3254975 | 50 | paired end |
| MB/2 | 3413939 | 50 | paired end |
 
Fastqc analysis was completed on all sequencing fasta files (7.). The full html reports can be viewed in the labreport folder. Upon observation we noticed that the *base sequence content* flag was marked as red in all of the reports. No other flags were raised in the reports. The *base sequence content* flag is not a cause for concern and it is apparent to a certain extent in all RNA-Seq data. Random priming in the library preparation often biases toward certain hexeomers. This bias doesn't seem to cause any problems with downstream analysis (2). 

The reference genome used in this study was: __mm10 Mouse__

### RNA-seq analysis

We used the tool kallisto version 0.44.0 to quantify transcript abundance for all six RNA-Seq fasta files (9.). This tool uses a kmer counting approach based on a De Brujn graph to quantify Transcripts Per Kilobase Million (TPM) values for each transcript. A script was written to run the command with the following non-default parameters: 100 bootstrap samples, the quant algorithm option running three threads (-t), a gene structure file in GTF format  (-g), and a kallisto index file of target sequences (-i). The exact script we used can be found in the /scripts folder.  

We used a tool called sleuth to identify deferentially expressed genes using our kallisto output files (10.). This tool took advantage of our technical replicates in its determination of significant transcripts. The tool was used commands in R, and significant results (qval <= 0.05) saved in a tab delineated file (.tab). A qval is an false discovery rate (FDR) adjusted threshold using the benjamini-hochberg procedure. 

### Enhancer analyses	

Visualization of various data alignments was achieved using the IGV genome browser (11.). Multiple data sets, read abundance, and annotated Refseq data can all be simultaneously visualized and explored using this tool, making it a good fit for this study. The six aligned read count files (.tdf) were uploaded to the browser.  The *Shh* gene and the enhancer *ZRS* were identified as targets in our study and explored in more detail using the browser. Additional ChiP-sequencing data sets were used to explore histone modifications (H3K27ac and H3K4me1) for each sample. A PhyloP track containing per-base sequence conservation measures was also added to the browser in this region for motif identification. The PhyloP track was downloaded as a custom track file from UCSC's genome browser (6.) with the following non-default parameters:  Group - Comparative Genomics, Track - Conservation, Table - 60 Vert. Cons (phyloP60wayAll), Region - position chr5:23414443-36455956, Filter "Limit data output to" - 10 million lines, Output format - custom track, Output file -phyloP60wayAll_mm10_Shh_region.wig, DATA VALUE - selected. 

## Results

### RNA-seq analysis

Differential gene expression data was quantified using TPM values by Kallisto. Concordance between the resulting TPM value data sets was calculated pairwise for each of the six files using Pearson coefficients (Table 1). Highlighted in bold are the coefficients between replicate data sets. We found that the replicate data sets show higher coefficient values (almost a linear relationship) than non replicate samples, as we would expected. Apart from the replicates, we see higher coefficients between the HL/FL data sets than either HL/MB or FL/MB sets.   

#### Table 1. Pearson Coefficients Between Samples    

| ------- | FL_Rep1 | FL_Rep2 | HL_Rep1 | HL_Rep2 | MB_Rep1 | MB_Rep2 |
| ------- | ------- | ------- | ------- | --------| ------- | ------- |
| __FL_Rep1__ | ----- | __0.997__ | 0.960 | 0.957 | 0.957 | 0.946 | 
| __FL_Rep2__ | __0.997__ | ----- | 0.959 | 0.956 | 0.960 | 0.952 |
| __HL_Rep1__ | 0.960 | 0.959 | ----- | __0.995__ | 0.936 | 0.926 |
| __HL_Rep2__ | 0.957 | 0.956 | __0.995__ | ----- | 0.935 | 0.926 |
| __MB_Rep1__ | 0.957 | 0.960 | 0.936 | 0.935 | ----- | __0.991__ |
| __MB_Rep2__ | 0.946 | 0.952 | 0.926 | 0.926 | __0.991__ | ----- |

After verifying that TPM values were computed correctly, Sleuth was used to identify differentially expressed transcripts using the Kallisto output. There were __1940__ significant differentially expressed transcripts outputted from sleuth  (qval <= 0.05) . The ten most significant transcripts were looked up for their genes of origin in the Enseble *Mus musculus* database (http://uswest.ensembl.org/Mus_musculus/Info/Index) and visualized using the IGV browser. 

Screenshots from the IGV browser for the first seven results are shown below (Figures 1 - 7) in order of significance and can be viewed in the labreport folder.

#### Figures 1-7. IGV Browser Screenshots of Significant Deferentially Expressed Genes (red = FL Replicates, blue = HL Replicates, green = MB Replicates; For each tissue type replicate 1 is shown above replicate 2)

####  Figure 1. Rpl21

![](https://github.com/cse185-sp18/cse185-week4-ljervis/blob/master/labreport/Rpl21.JPG)

#### Figure 2.  Shh

![](https://github.com/cse185-sp18/cse185-week4-ljervis/blob/master/labreport/SHH.JPG)

#### Figure 3.  Uchl1

![](https://github.com/cse185-sp18/cse185-week4-ljervis/blob/master/labreport/Uchl1.JPG)

#### Figure 4.  Sparcl1

![](https://github.com/cse185-sp18/cse185-week4-ljervis/blob/master/labreport/Sparcl1.JPG)

#### Figure 5.  Parm1

![](https://github.com/cse185-sp18/cse185-week4-ljervis/blob/master/labreport/Parm1.JPG)

#### Figure 6.  Nat8l

![](https://github.com/cse185-sp18/cse185-week4-ljervis/blob/master/labreport/Nat8l.JPG)

#### Figure 7.  Ubl3

![](https://github.com/cse185-sp18/cse185-week4-ljervis/blob/master/labreport/Ubl3.JPG)

### Enhancer analysis

We identified the *Shh* gene as a target for further analysis given that it was tagged as having highly differential expression between tested tissue types, and its role in early development of limbs, digits and brain tissue. The *Shh* gene is is controlled be the *ZRS* enhancer, that is know to be specific to limb tissue development (1.). ChiP-sequencing data sets for H3K4me1 and H3K27ac histone modifications were loaded into the the IGV browser to search for potential regulatory regions of the *Shh* gene in the *ZRS* and surrounding regions of the genome. A screenshot of our ChiP-sequencing data sets in the IGV browser are shown (Figure 8). 

#### Figure 8. Histone Modification Data Sets in IGV Browser (red = FL, blue = HL, green = MB; tracks 8 - 10 = H3K27ac , tracks 11 - 13 = H3K4me)

![](https://github.com/cse185-sp18/cse185-week4-ljervis/blob/master/labreport/Histone%20Modification%20Tracks.JPG)

Generally, we see a stronger signal from the H3K4me1 histone modification tracks compared to H3K27ac in all regions covered by this data set. For the H3k4me1 tracks we see more coordination between signals in the HL/FL data sets compared to the HL/MB  or FL/MB data sets. This is consistent with our transcript abundance data based on the Pearson coefficient data (Table 1). For all tracks, there are signals coordinated with both intron and exon sequences but peak regions are most often found in intron or non-coding sequences before the adjacent gene (Figure 9).  A PhyloP data setfrom the UCSC database was added to the IGV browser to view base-pair species conservation and identify motifs. There are conservation signals in both intron and exon sequences but the strongest signals tend to fall within exon, or gene coding  sequences. Focusing on the *ZRS* region (chr5:29,314,718-29,315,770) (Figure 10), we see strong signals from both H3K4me1 and H3K27ac histone modifications of the HL and FL tracks, but weak signals from the MB tracks. Furthermore, we see strong base-pair sequence conservation from the PhyloP track in this same region. 

#### Figure 9. Emilin1 Histone Modifications in IGV Browser (red = FL, blue = HL, green = MB; tracks 8 - 10 = H3K27ac , tracks 11 - 13 = H3K4me)

![](https://github.com/cse185-sp18/cse185-week4-ljervis/blob/master/labreport/Emilin1%20Histone%20Modification%20Example.JPG)

#### Figure 10. ZRS Region in IGV Browser (red = FL, blue = HL, green = MB; tracks 8 - 10 = H3K27ac , tracks 11 - 13 = H3K4me, track 14 = base-pair species conservation)

![](https://github.com/cse185-sp18/cse185-week4-ljervis/blob/master/labreport/ZRS%20Region.JPG)

Multiple sequence alignment was preformed in the *ZRS* region between species with limbs: human, mouse, cow, dolphin, and snake species without limbs: python, rattlesnake, cobra, and boa. An html file showing this alignment can be viewed in the labreport folder. We found one region that was conserved in all species with limbs but deleted in species without limbs (Figure 11.). We believe this to be an important deletion in snake species that impedes the development of limbs. 

#### Figure 11. Deleted Sequence in MSA (Row 1 = human_zrs, Row 2 = mouse_zrs, Row 3 = cow_zrs, Row 4 = dolphin_zrs, Row 5 = python_zrs, Row 6 = rattlesnake_zrs, Row 7 = cobra_zrs, Row 8 = boa_zrs)

![](https://github.com/cse185-sp18/cse185-week4-ljervis/blob/master/labreport/Snake_1.JPG) 

### Extra Credit 

A python script was used to aggregate all TPM values from the kallisto output files into a tab delininated file and a heatmap was created with the online tool Morpheus (12.) (Figure 12.). Hierarchical clustering was completed using one minus person correlation and average linkage method. Looking at the columns we see that the replicate samples cluster together. Furthermore, the HL and FL replicates cluster together before MB as expected. Looking at the rows we see a clear pattern of differentiation between genes in the HL and FL samples compared to the MB samples. Many genes up-regulated in HL/FL samples are down regulated in MB samples and vice versa.

#### Figure 12. Heatmap of TPM Values With Clusters. 

![](https://github.com/cse185-sp18/cse185-week4-ljervis/blob/master/labreport/MorpheusHeatMapWithClustering.JPG)

Geno ontology was preformed for the top 10 differentially expressed genes using the Panther database (13.). 

#### Table 2. Gene Ontology Results

| Gene | GO Biological Processes | GO Molecular Functions |
|------|-------------------------|------------------------|
| Rpl21 | - | Protein binding; structural constituent of ribosomes |
| Shh | lung, tongue, skin, hair, eye, and kidney development | protein binding; metal ion binding; peptidase activity |
| Gltp | lipid transport | protein binding; lipid binding; glycolipid binding |
| Ubl3 | - | - |
| Garem2 | - | - |
| Parm1 | positive regulation of telomerase activity | - |
| Sparcl1 | signal transduction; anatomical structural development | extracellular matrix binding; collagen binding; metal and calcium binding |
| Nat8l | positive regulation of dopamine uptake | transferase activity |
| Uchl1 | Cell proliferation; negative regulation of MAP kinase; neuromuscular process | protease activity; ligase activity |
| Hmgn2 | negative regulation of transcription by RNA Pol II; regulation of development | - |

## Discussion

*Shh* is a gene encoding a protein, Sonic Hedgehog, which functions as a chemical signal during early development. Among other things, this signal coordinates the development of limbs and digits making it an interesting target for study in our investigation. Interestingly *Shh* was identified as being differentially expressed in our analysis of hind limb (HL), fore limb (FL), and mid-brain (MB) tissues. Both HL and FL had strong *Shh* transcript abundance signals while MB showed significantly less. Upon analysis of gene activating histone modifications ( H3K4me1 and H3K27ac) in this region we saw strong signals in both the HL and FL tissues but weak signals in the MB tissue. These insights support the belief that *Shh* is highly expressed in limb specific tissues and not others. 

The highly conserved *ZRS* enhancer controls the expression of *Shh* in different tissues. *ZRS* was identified as being a possible regulatory region for limb development. Like the *Shh* region, the *ZRS* region showed strong histone modification signals in HL and FL and weak signals in MB tissue.  We hypothesized that a modification within the *ZRS* region in snake species may lead to decreased expression of *Shh* and inhibit the development of limbs in these species. Computational analysis of histone modifications in intron regions surrounding *Shh* may lead to identification of other enhancer regions. Using multiple sequence alignment between snake and non-snake species we identified a small region within the *ZRS* enhancer sequence that was conserved in all species with limbs but deleted in all snake species.  

This deletion may inhibit the up-regulation of *Shh* by the *ZRS* enhancer decreasing the transcription of *Shh* gene. It is possible that this deleted region constituted a binding site for a transcription factor (TF). Left unable to bind this deletion would inhibit any up-regulation the TF might provide in other species with this conserved binding site. Members of the ETS family of transcription factors bind to the *ZRS* enhancer region and provide *Shh* gene regulation (3.). In order to test whether these ETS TF's bind to the *ZRS* region at this identified region, further experiments are needed. A gel shift assay know as EMSA can determine specific protein-DNA interaction. Although not used in this study, future EMSA assays could help determine whether the deleted region we identified constitutes a binding site for ETS transcription factors. 

## Citations

(1.) Gymrek, MG. (2018). cse185-spring18-week4. UCSD.

(2.) Hansen, Hansen. “QC Fail Sequencing » Positional Sequence Bias in Random Primed Libraries.” Sequencing, sequencing.qcfail.com/articles/positional-sequence-bias-in-random-primed-libraries/.

(3.) Lettice LA, Williamson I, Wiltshire JH, et al. Opposing Functions of the ETS Factor Family Define _Shh_ Spatial Expression in Limb Buds and Underlie Polydactyly. _Developmental Cell_. 2012;22(2):459-467. doi:10.1016/j.devcel.2011.12.010.

(4.) The butterfly effect in embryology (2016) _Chemiotics II_.

(5.) Landt SG, Marinov GK, Kundaje A, et al. ChIP-seq guidelines and practices of the ENCODE and modENCODE consortia. _Genome Research_. 2012;22(9):1813-1831. doi:10.1101/gr.136184.111.

(6.) Kent WJ, Sugnet CW, Furey TS, Roskin KM, Pringle TH, Zahler AM, Haussler D. [The human genome browser at UCSC]
(http://www.genome.org/cgi/content/abstract/12/6/996). _Genome Res._ 2002 Jun;12(6):996-1006.

(7.) FastQC A Quality Control tool for High Throughput Sequence Data [http://www.bioinformatics.babraham.ac.uk/projects/fastqc/](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/) by S. Andrews

(8.) [www.ebi.ac.uk](https://www.ebi.ac.uk/) The European Bioinformatics Institute.

(9.) Nicolas L Bray, Harold Pimentel, Páll Melsted and Lior Pachter, [Near-optimal probabilistic RNA-seq quantification](http://www.nature.com/nbt/journal/v34/n5/full/nbt.3519.html), Nature Biotechnology **34**, 525–527 (2016), doi:10.1038/nbt.3519

(10.) Harold J. Pimentel, Nicolas Bray, Suzette Puente, Páll Melsted and Lior Pachter, [Differential analysis of RNA-Seq incorporating quantification uncertainty](http://www.nature.com/nmeth/journal/vaop/ncurrent/full/nmeth.4324.html), Nature Methods (2017), advanced access http://dx.doi.org/10.1038/nmeth.4324.

(11.) Robinson JT, Thorvaldsdóttir H, Winckler W, et al. Integrative Genomics Viewer. _Nature biotechnology_. 2011;29(1):24-26. doi:10.1038/nbt.1754.

(12.) https://software.broadinstitute.org/morpheus/#

(13.) Huaiyu Mi, Xiaosong Huang, Anushya Muruganujan, Haiming Tang, Caitlin Mills, Diane Kang, and Paul D. Thomas Nucl. Acids Res. (2016) doi: 10.1093/nar/gkw1138
