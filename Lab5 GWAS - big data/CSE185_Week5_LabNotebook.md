# __Week 5 Lab Notebook__
### Luke Jervis


## __Part I__

Count the number of samples.

`wc -l lab5_gwas_eyecolor.ped`

261 samples 

Find the ratio of brown (1) vs. blue (2) eyes 

```
cat lab5_gwas_eyecolor.phen | cut -f3 | sort | uniq -c

104 1
157 2
```

104/157  = __0.662__

Count the number of markers in our dataset 

```
wc -l lab5_gwas_eyecolor.map

911774 lab5_gwas_eyecolor.map
```

__911774__ markers 

Analyzing population structure 

```
plink --file $public_dir/week5/lab5_gwas_eyecolor --pca 10 --out PCA
```

Preforming a basic GWAS

No Covariants

```
plink --file $public_dir/week5/lab5_gwas_eyecolor --pheno $public_dir/week5/lab5_gwas_eyecolor.phen --out GWAS --logistic --allow-no-sex
PLINK v1.90b5.4 64-bit (10 Apr 2018)           www.cog-genomics.org/plink/1.9/
(C) 2005-2018 Shaun Purcell, Christopher Chang   GNU General Public License v3
Logging to GWAS.log.
Options in effect:
  --allow-no-sex
  --file /home/linux/ieng6/cs185s/public/week5/lab5_gwas_eyecolor
  --logistic
  --out GWAS
  --pheno /home/linux/ieng6/cs185s/public/week5/lab5_gwas_eyecolor.phen

128774 MB RAM detected; reserving 64387 MB for main workspace.
.ped scan complete (for binary autoconversion).
Performing single-pass .bed write (911774 variants, 261 people).
--file: GWAS-temporary.bed + GWAS-temporary.bim + GWAS-temporary.fam written.
911774 variants loaded from .bim file.
261 people (0 males, 0 females, 261 ambiguous) loaded from .fam.
Ambiguous sex IDs written to GWAS.nosex .
261 phenotype values present after --pheno.
Using 1 thread (no multithreaded calculations invoked).
Before main variant filters, 261 founders and 0 nonfounders present.
Calculating allele frequencies... done.
Total genotyping rate is 0.999909.
911774 variants and 261 people pass filters and QC.
Among remaining phenotypes, 157 are cases and 104 are controls.
Writing logistic model association results to GWAS.assoc.logistic ... done.
```

With Covariants

```
plink --file $public_dir/week5/lab5_gwas_eyecolor --pheno $public_dir/week5/lab5_gwas_eyecolor.phen --out GWAS_Covar --logistic hide-covar --allow-no-sex --covar PCA.eigenvec
PLINK v1.90b5.4 64-bit (10 Apr 2018)           www.cog-genomics.org/plink/1.9/
(C) 2005-2018 Shaun Purcell, Christopher Chang   GNU General Public License v3
Logging to GWAS_Covar.log.
Options in effect:
  --allow-no-sex
  --covar PCA.eigenvec
  --file /home/linux/ieng6/cs185s/public/week5/lab5_gwas_eyecolor
  --logistic hide-covar
  --out GWAS_Covar
  --pheno /home/linux/ieng6/cs185s/public/week5/lab5_gwas_eyecolor.phen

128774 MB RAM detected; reserving 64387 MB for main workspace.
.ped scan complete (for binary autoconversion).
Performing single-pass .bed write (911774 variants, 261 people).
--file: GWAS_Covar-temporary.bed + GWAS_Covar-temporary.bim +
GWAS_Covar-temporary.fam written.
911774 variants loaded from .bim file.
261 people (0 males, 0 females, 261 ambiguous) loaded from .fam.
Ambiguous sex IDs written to GWAS_Covar.nosex .
261 phenotype values present after --pheno.
Using 1 thread (no multithreaded calculations invoked).
--covar: 10 covariates loaded.
Before main variant filters, 261 founders and 0 nonfounders present.
Calculating allele frequencies... done.
Total genotyping rate is 0.999909.
911774 variants and 261 people pass filters and QC.
Among remaining phenotypes, 157 are cases and 104 are controls.
Writing logistic model association results to GWAS_Covar.assoc.logistic ...
done.
```
Used python to find variants with p val less than 5 * 10^-8

__4__ variants in GWAS_Covar (with covariants)

```
15 rs1470608 28288121 1 ADD 261 0.1111 -5.512 3.557e-08
15 rs7170869 28288748 1 ADD 261 0.1111 -5.512 3.557e-08
15 rs1129038 28356859 1 ADD 261 0.01011 -7.306 2.749e-13
15 rs12913832 28365618 1 ADD 261 0.008607 -7.293 3.039e-13
```

__24__ variants in GWAS (no covariants)

```
2 rs2583551 85309672 1 ADD 261 0.2494 -5.59 2.275e-08
15 rs749846 28268990 1 ADD 261 0.1818 -5.954 2.611e-09
15 rs4778232 28281765 1 ADD 261 0.1889 -6.524 6.861e-11
15 rs1448485 28282741 1 ADD 261 0.1656 -5.956 2.584e-09
15 rs16950821 28283507 1 ADD 261 0.1624 -5.62 1.904e-08
15 rs8024968 28283689 1 ADD 261 0.1624 -5.62 1.904e-08
15 rs7177686 28287344 1 ADD 261 0.1726 -6.721 1.81e-11
15 rs1470608 28288121 1 ADD 261 0.134 -6.678 2.428e-11
15 rs6497253 28288549 1 ADD 261 0.1726 -6.721 1.81e-11
15 rs7170869 28288748 1 ADD 261 0.134 -6.678 2.428e-11
15 rs1375164 28291812 1 ADD 261 0.1733 -6.741 1.574e-11
15 rs1597196 28294922 1 ADD 261 0.2211 -5.778 7.563e-09
15 rs6497254 28296425 1 ADD 261 0.1733 -6.741 1.574e-11
15 rs7179994 28323770 1 ADD 261 0.1579 -6.074 1.248e-09
15 rs7174027 28328765 1 ADD 261 0.1359 -5.77 7.911e-09
15 rs4778138 28335820 1 ADD 261 0.1074 -6.778 1.216e-11
15 rs4778241 28338713 1 ADD 261 0.1351 -7.291 3.066e-13
15 rs1129038 28356859 1 ADD 261 0.01336 -8.461 2.646e-17
15 rs12913832 28365618 1 ADD 261 0.01221 -8.528 1.486e-17
15 rs3935591 28374012 1 ADD 261 0.08217 -6.986 2.82e-12
15 rs11636232 28386626 1 ADD 261 5.702 7.076 1.489e-12
15 rs916977 28513364 1 ADD 261 0.0813 -7.655 1.931e-14
15 rs8039195 28516084 1 ADD 261 0.09641 -6.966 3.258e-12
15 rs1667394 28530182 1 ADD 261 0.07354 -7.899 2.806e-15
```

`python gwas_plotter.py GWAS.assoc.logistic. GWAS`

`python gwas_plotter.py GWAS_Covar.assoc.logistic GWAS_Covar`

Moved files to my desktop and analysed them

Decided to use the results with co-variants for the remainder of the analysis

Clumped the GWAS output files

```
plink --file $public_dir/week5/lab5_gwas_eyecolor --clump GWAS_Covar.assoc.logistic --clump-field P --clump-p1 0.0001 --clump-p2 0.01 --clump-r2 0.5 --clump-kb 250 --out CLUMP
```

```
wc -l CLUMP.clumped
40 CLUMP.clumped
 ```

__39__ signals identified by plink in the .clumped file 

__2__ signals with p value less than 5 * 10^-8

```
15 1 rs1129038 28356859 2.75e-13 1 0 0 0 0 1 rs12913832(1)
15 1 rs1470608 28288121 3.56e-08 11 0 0 0 0 11 rs749846(1),rs3794604(1),rs4778232(1),rs1448485(1),rs16950821(1),rs8024968(1),rs7177686(1),rs6497253(1),rs7170869(1),rs1375164(1),rs6497254(1)
```

rs12913832 was identified as being clumped with rs1129038 

The following table has each previously identified variant and the p-val from this study (GWAS no covariant) 

| Chromosome | Start | Rsid | Minor Allele | P-Val | 
| --- | --- | --- | --- | --- |
| 15 | 28365618 | rs12913832 | A | 3.039e-13 | 
| 15 | 28230318 | rs1800407 | T | 0.2506 |
| 14 | 92773663 | rs12896399 | G | 0.874 |
| 5 | 33951693 | rs16891982 | C |  0.08098 |
| 11 | 89011046 | rs1393350 | A | 0.0343 |
| 6 | 396321 | rs12203592 | T | 0.7099 |

## __Part II__

Counted the number of samples in lab5_phred_eyecolor.vcf.gz

`zcat lab5_pred_eyecolor.vcf.gz | grep '#CHROM' | wc -w`

215  words - 9 header columns = __206__ samples 

`zcat lab5_pred_eyecolor.vcf.gz | grep -n '#CHROM'`
`zcat lab5_pred_eyecolor.vcf.gz | wc -l`

The header is on line 254 and there are 260 lines in the file. Because each line after the header corresponds to one variant, there are __6__ variants in this file. 

Got a header row listing the samples

`bcftools query -l lab5_pred_eyecolor.vcf.gz | datamash transpose | awk '{print "ID\t"$0"\t"}' > lab5_pred_eyecolor.tab`

Extracted the ID and sample genotypes for each variant

`bcftools query -f "%ID\t[%TGT\t]\n" final/lab5_pred_eyecolor.vcf.gz | sed 's/|//g' >> lab5_pred_eyecolor.tab`

Transposed the file

`cat lab5_pred_eyecolor.tab | datamash transpose > lab5_pred_eyecolor_transpose.tab`

Probability of having blue eyes: __0.765__

Probability of having brown eyes: __0.124__

Probability of having other colored eyes: __0.111__

Calculations for eye color probabilities can be found in the labreport folder "MyEyeColor.xlsx"

Probability of having blue eyes (Northern Europe) = __0.872__

Probability of having brown eyes (Northern Europe) = __0.078__

Probability of having other colored eyes (Northern Europe) = __0.049__

Probability of having blue eyes (Southern Europe) = __0.611__

Probability of having brown eyes (Southern Europe) = __0.174__

Probability of having other colored eyes (Southern Europe) = __0.215__

There is a higher probability of having blue eyes in northern Europe than southern Europe

Loaded the Human hg19 reference and .vcf files into IGV Browser

| Chromosome | Start | Rsid | Minor Allele | Gene Origin | 
| --- | --- | --- | --- | --- |
| 15 | 28365618 | rs12913832 | A | HERC2 | 
| 15 | 28230318 | rs1800407 | T | OCA2 |
| 14 | 92773663 | rs12896399 | G | SLC14A4 |
| 5 | 33951693 | rs16891982 | C | SLC45A2 |
| 11 | 89011046 | rs1393350 | A | TYR |
| 6 | 396321 | rs12203592 | T | IRF4 |
