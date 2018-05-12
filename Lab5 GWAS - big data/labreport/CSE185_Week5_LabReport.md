# Investigation and prediction of eye color through genome-wide association study and SNP analysis
##### Luke Jervis

## Abstract

In this study we investigate single nucleotide polymorphisms (SNP's) associated with eye color in humans.  A cohort of DNA samples was collected and a SNP genotype array preformed. Using a simple genome-wide association study (GWAS), we identified __2__ significant SNP variants in our sample cohort including one of six significant SNP variants identified by Walsh et al. (4.) as being associated with eye color. Using their sample cohort, an eye color prediction tool was created using the algorithm described in Liu et al. (2.). Identified variants were interpreted using a variety of genomics tools. Variants in the OCA2 and HERC2 gene regions were reported, and it is suggested that these SNP's are involved differential production of the eye color pigment, melanin. We hope this study represents a method of SNP variant identification for complex disease phenotypes which may be used to find associated genomic regions and identify direct future therapeutic studies.      

## Introduction

We began with a cohort of 261 genotype samples originating from a heterogeneous population with blue or brown eyes.  The SNP genotype array tested for 911774 different SNP variants. This data was used to identify variants with genome-wide significance potentially associated with eye color. We achieved this through a GWAS, accounting for cofounders in our data using principle component analysis. Using statistical analysis techniques, we show that PCA was necessary to account for population structure variations in our data set. This study identifies how ancestral variations in sample cohorts can impact the results of a GWAS, and provides and example of how to properly account for it. 

Another sample cohort from the paper by Walsh et. al. was used in this study to develop a program that predicts eye color based on the 6 SNP's they identified. We also calculate differences in eye color probability between samples origination from northern and southern Europe. Finally we use the variants in this paper to suggest a mechanistic way in which eye color is achieved. We show how a GWAS and downstream analysis can identify specific genomic regions that are involved in complex traits, such as eye color, and can help build our mechanistic understanding of these traits. 

## Methods

### Dataset Description

We began with a cohort of 261 samples from a heterogeneous population of humans with blue or brown eyes. A SNP genotype array tested each sample for 911774 different variants. There were 104 brown eyed samples and 157 blue eyed samples in our data set. We used a data set of SNP's published by Walsh et al. (4.) that included a cohort of 206 samples testing for 6 SNP's they identified as accociated with eye color. These samples originated from northern and southern Europeans with either blue, brown, or other eye color.  

### GWAS

The tool plink Chang et al. (3.) version 1.9 was used to analyse the SNP genotype array data for most of our downstream analysis. We used principle component analysis (PCA) to control for population structure in our data. Plink was used to calculate the top 10 principle components in our data. We set the (--file) argument to our input data prefix (lab5_gwas_eyecolor), the (--pca) argument to 10, and the (--out) argument to our output data prefix (PCA). 

Plink was then used to preform a basic logistic regression GWAS, first with no covariates. We set the (--file) argument to our input data prefix (lab5_gwas_eyecolor), the (--pheno) argument to our phenotype information file (lab5_gwas_eyecolor.phen), the (--out) argument to our output data prefix (GWAS), the (--logistic) flag set, and the (--allow-no-sex) flag set to prevent samples with ambiguous sex from having their phenotype set to missing. Plink was then run again using the covariates we previously calculated. We set all the same arguments/flags as the first run and then set the (--covar) argument to our covariate file (PCA.eigenvec), and added the (hide-covar) modifier to the (--logistic) flag to remove covariate specific lines from the report.  

After the GWAS runs, plink was used on the covariate results to "clump" the linkage disequilibrium (LD) regions containing  significant variants into likely independent signals. We set the (--field) argument to our input data prefix (lab5_gwas_eyecolor), the (--clump) argument to the GWAS results output with covariates (GWAS_Covar.assoc.logistic), the (--clump-field) argument to P, (--clump-p1) to 0.0001,  (--clump-p2) to 0.01, (--clump-r2) to 0.5, (--clump-kb) to 250, and the (--out) argument to our output data prefix (CLUMP). 

### Eye color prediction

A program was written in python to predict eye color and compute region based eye color probabilities according to the method described in Liu et al. (2.). An investigation into how these variants might be affecting eye color was carried out using the IGV browser, James T. et al (5.). Additional histone modification ChiP-seq data sets were loaded onto the browser from the ENCODE Project (6.). Genes containing variants were looked up on http://uswest.ensembl.org to find function and protein products were researched on http://www.uniprot.org. 

## Results 

### GWAS 

Plink Chang et al. (3.) version 1.9 was used to analyse the SNP genotype array data. As our cohort was from a heterogeneous population, coufounding factors including characteristics like age, lifestyle, environment and population structure could all lead to spurious signals in our downstream GWAS analysis (1.). We used principle component analysis (PCA) to control for population structure in our data. PCA is a dimension reduction technique that identifies trends explaining variation (confounding factors) in our data. We used plink to calculate the top 10 principle components (PC) in our data. A scatter plot showing the top two PC values was created using Microsoft Excel 2013 (Figure 1) and can be found in the labreport folder (Principle_Component_Data.xlsx). The scatter plot can be visually clustered into three distinct ancestry groups present in our data set. 

#### Figure 1. Principle Component 1 & 2 Scatter Plot

![](https://github.com/cse185-sp18/cse185-week5-ljervis/blob/master/labreport/Principle_Component_Scatter_Plot.JPG)

A simple logistic regression GWAS was completed using plink with and without the PC addition (covariates). Without PCs, our GWAS reported __24__ variants passing genome-wide significance (p < 5*10^-8). When PC's were added __4__ significant variants were reported. This result was predictable, as controlling for covariates should lead to less false positives being reported. To visualize our results we generated a Manhattan plot and a Quantile-Quantile (QQ) plot for both GWAS runs (Figure 2-5) using the assocplots python package (7.). The Manhattan plots visualize our findings p-values with respect to genomic position. Comparing these figures we see that the run with covariates shows less noise and cleaner peaks. The QQ plots visualize the distribution of p-values in the data, and compares this with the theoretical distribution given the null hypothesis. In the QQ plot with out covariants we see an inflation of p-values along the distribution, signaling population stratification (9.). This results agrees with the PC scatter plot (Figure 1), suggesting there are confounding factors present in the data. In the QQ plot with covariants the bulk of the distribution is on the theoretical distribution, as expected. Due to these factors we decided to use the GWAS results with covariates for the remainder of the analysis.   

#### Figure 2. Manhattan Plots With Covariates  

![](https://github.com/cse185-sp18/cse185-week5-ljervis/blob/master/labreport/GWAS_Covar_manhattan.png)

#### Figure 3. Manhattan Plots Without Covariates

![](https://github.com/cse185-sp18/cse185-week5-ljervis/blob/master/labreport/GWAS_manhattan.png) 

#### Figure 4. QQ Plots With Covariates 

![](https://github.com/cse185-sp18/cse185-week5-ljervis/blob/master/labreport/GWAS_Covar_qq.png)

#### Figure 5. QQ Plots Without Covariates 

![](https://github.com/cse185-sp18/cse185-week5-ljervis/blob/master/labreport/GWAS_qq.png)

We noticed some "high rise" spikes in the covariate Manhattan plot, suggesting not all points found in spike regions were significant and would result in false positives. To account for this we used plink to "clump" the linkage disequilibrum (LD) regions into likely independent signals. After clumping of the covariate data, 39 variants were found and  __2__ variants were reported as passing genome-wide significance (Table 1).  Comparing with significant variants associated with eye color in Walsh et al. (4.), one of their results (rs12913832) was reported in our data, belonging to a clump we identified (rs1129038). P-values of variants identified in their study are shown (Table 3). 

#### Table 1. Significant Variants After Clumping

| Chromosome | Start | Rsid | P-Val | 
| --- | --- | --- | --- |
| 15 | 28356859 | rs1129038 | 2.75e-13 | 
| 15 | 28288121 | rs1470608 | 3.56e-08 |

#### Table 2. Previously Reported Significant Variants 

| Chromosome | Start | Rsid | Minor Allele | P-Val (identified in this study) | 
| --- | --- | --- | --- | --- |
| 15 | 28365618 | rs12913832 | A | 3.039e-13 | 
| 15 | 28230318 | rs1800407 | T | 0.2506 |
| 14 | 92773663 | rs12896399 | G | 0.874 |
| 5 | 33951693 | rs16891982 | C |  0.08098 |
| 11 | 89011046 | rs1393350 | A | 0.0343 |
| 6 | 396321 | rs12203592 | T | 0.7099 |

### Eye color prediction

In this section we used SNP variant data from Walsh et al. (4.) containing __206__ samples and testing for __6__ variants involved in eye color. A program was written in python to predict eye color from variant genotypes according to the method described in Liu et al. (2.) The same program computes the mean probability of blue, brown, and other eye colors for samples from northern Europe and samples from southern Europe in our data set.  The program (EyeColorPrediction.py) can be found in the labreport folder along with a Microsoft Excel spread sheet of results (EyeColorPredictionOutput.xlsx). 

Further analysis of the identified variants was completed using the IGV browser loaded with human hg19 reference genome. The H3K27 and H3K4me1 histone modifications for seven human cell types were also added. We identified a region encompassing the OCA2 and HERC2 genes that contained four significant variants from the study (rs12913832, rs1800407, rs1129038, rs1470608). This region showed a large amount of histone modification suggesting it may be a regulatory region (Figure 6). Further research suggested to us that this region is involved in the production of an important eye pigment called melanin.

#### Figure 6. IGV Browser OCA2 and HERC2 Regions

![](https://github.com/cse185-sp18/cse185-week5-ljervis/blob/master/labreport/IGV_Browser_OCA2_HERC2.JPG)

## Discussion

We found that controlling for population structure was extremely important for our GWAS results. As seen in the comparison of principle components 1 and 2 (Figure 1) there are three visually discernible clusters. This is common in heterogeneous sample populations such the one used in this study. The clusters identify groups of samples with ancestral similarity to one another and dissimilarity with other clusters. These cofounding factors can influence our GWAS results and lead to false positives. For this reason we preformed a GWAS with and without PC covariants to compare the results. We found that the use of covariants produced a similar p-value distribution to what we would expect. Without covariants the distribution was noisier (Figure 5) and inflated (Figure 3). Furthermore, we found far fewer significant variants with the use of covariates, as we would expect from this adjustment. These results highlight the importance of accounting for cofounding factors when performing GWAS.

We found one genome-wide significance SNP of  the six previously identified SNP variants from Walsh et al. in our results. We propose that our sample cohort may have had samples from different global origins than the ones used in the Walsh et. al. paper. Furthermore, differences in genotype assay preparation and bioinformatics pipelines may have lead to these different results. 

SNP's variants within the OCA2 gene and the neighboring HERC2 gene have shown association with human eye color variation, Richard A. et al (8.).  Both of the SNP variants we identified in our GWAS and one variant identified in the study by Walsh et. al. lie in the OCA2 gene region. The protein product of the OCA2 gene is called P protein and is involved in the production of cells storing the pigment protein melanin which is present in the iris. Furthermore, another variant identified in the paper (rs12913832) occurs in a region of the HERC2 gene that has been identified as a regulatory region for the expression of OCA2. The high levels of histone modifications we saw in this region supports this idea. We conclude that SNP variants in these regions are likely to alter the amount of melanin present in the eyes leading to differences in eye color. We hope that this study highlighted the power of GWAS studies to identify genomic regions involved in complex phenotype traits. 

## Citations 
(1.) Gymrek, MG. (2018). cse185-spring18-week5. UCSD.

(2.) F.  Liu,  K.  van Duijn,  J.R.  Vingerling,  A.  Hofman,  A.G.Uitterlinden,  A.C.J.W.  Janssens,  M.  Kayser, Eye color and the prediction of complex phenotypes from genotypes, Curr. Biol.,  19  (2009), pp.  R192-R193

(3.) Chang CC, Chow CC, Tellier LCAM, Vattikuti S, Purcell SM, Lee JJ (2015) Second-generation PLINK: rising to the challenge of larger and richer datasets. GigaScience, 4.

(4.) Susan Walsh, Fan Liu, Kaye N. Ballantyne, Mannis van Oven, Oscar Lao, Manfred Kayser, IrisPlex: A sensitive DNA tool for accurate prediction of blue and brown eye colour in the absence of ancestry information, Forensic Science International: Genetics, Volume 5, Issue 3, 2011.

(5.) Robinson, James T. et al. “Integrative Genomics Viewer.” _Nature biotechnology_29.1 (2011): 24–26. _PMC_. Web. 8 May 2018.

(6.) The ENCODE Project Consortium. “An Integrated Encyclopedia of DNA Elements in the Human Genome.” _Nature_ 489.7414 (2012): 57–74. _PMC_. Web. 8 May 2018.

(7.) Khramtsova, Ekaterina A., and Barbara E. Stranger. 2016. “Assocplots: A Python Package for Static and Interactive Visualization of Multiple-Group GWAS Results.” Bioinformatics , October. Oxford Univ Press. doi:10.1093/bioinformatics/btw641. 

(8.) Sturm, Richard A. et al. “A Single SNP in an Evolutionary Conserved Region within Intron 86 of the _HERC2_ Gene Determines Human Blue-Brown Eye Color.” _American Journal of Human Genetics_ 82.2 (2008): 424–431. _PMC_. Web. 9 May 2018.

(9.) Mccarthy, Mark I., et al. “Genome-Wide Association Studies for Complex Traits: Consensus, Uncertainty and Challenges.” Nature Reviews Genetics, vol. 9, no. 5, 2008, pp. 356–369., doi:10.1038/nrg2344.
