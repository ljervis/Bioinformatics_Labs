# Week 1 Lab Report 
##### Luke Jervis

## Abstract
In no more than 100 words, briefly summarize what was done in the lab this week, what the findings were, and why they were important.

The goal of this lab was to identify causes of antibiotic resistance in an E. coli strain. This was achieved through sequence analysis of our strain and identification of mutations responsible for confering antibiotic resistance. knowledge of the mechanism of resistance can be used by clinicians when deciding the most effective treatment for a patient. It can also be used by scientists interested in creating new drugs to battle antibiotic resistant E coli.   

## Introduction
In 2-3 paragraphs, provide enough background information to understand the biology behind the weeks project. Be sure to state what problem or question the week’s lab work addressed, and why it is important. You must cite at least one scientific journal article for this section (it can, but doesn’t have to be, the assigned reading). When you use outside resources, use in-text citations in the text attributing any ideas or information from materials outside of our course lecture or tutorial. In-text citations give the source for information right where it is written (1).

When someone gets a bacterial infection a common course of action is prescribe the patient antibiotics. Unfortunatly many bacteria that cause these infections are becoming resistant to the antibiotics that are commonly prescribes, makeing them less effective in treating the infection.  
 
 
## Methods
This section should contain sufficient information so that other bioinformaticists could reproduce your results. You should briefly describe your raw data (what is it, what is the name of the reference) and describe what you did with it. You should write this in 2-3 paragraphs, not in a list. When you use a bioinformatics software program, do not write out the full command you typed, but do specify which program (ie ‘bwa-mem’ or ‘samtools tview’) you used and whether you used the default options. If you did not use the defaults, you should specify the exact settings you used. The first time you mention bioinformatics software or an online tool, you should cite it and specify which version of the tool you used. The correct citation for most software can be found by looking up its documentation on line (you don’t have to cite common tools like python or perl or the bash shell). If you write a custom script, (for example, our awk script from week 1), include that code in the labreport folder and reference it in your writeup.

## Results
This section should include the results of your data processing and data analysis, and may include tables with read lengths, pictures of quality distributions, or tables of gene names for examples. In the text, briefly restate how you got the results in full sentences, but in less detail than the methods, before you say what the results are (ie ‘reads were mapped to the reference and scanned to identify positions that likely contained mutations. We found….’). Refer to tables and figures by number, and include a brief descriptive title for each. Be sure to include any results specifically requested in the lab project tutorial. The results section should be as objective as possible, so please refrain from interpreting the meaning or significance here. It should be just the facts.

For every mutation you found that changes the protein sequence, you must research each gene by name to find out what it does (Ecoli Wiki, EcoCyc, google, and pubmed are good resources). Try to track down how that function could be involved in antibiotic resistance. If one of the proteins is a gene regulator (transcription factor), try to find out what it regulates. Include what you find in your lab report, and cite where you found it. Include this in the results section.

Also in your results section, make a table showing how many reads you started with, how many were left after trimming, and how many aligned. Please also include a description or image of the per-position read quality before and after trimming.

It would require additional biochemical testing to verify EXACTLY how each mutation changes the function of the protein its in. However, your job is to try to come up with a working hypothesis that could explain the mechanism of resistance behind the mutations (for instance, if the mutation is in a gene that makes a protein that is the antibiotic’s target, you could propose that that mutation changed the target so the antibiotic couldn’t bind anymore). Use what you know about the 4 mechanisms of antibiotic resistance to make predictions. Not all of the proteins may be involved in our E coli strain’s resistance, so you only need to make predictions for THREE of the mutations, but you should research all of them, so you are using the ones you can best make a logical prediction for. Include your predictions for the mechanism of antibiotic resistance for three of the genes in your discussion, and explain the logic behind your predictions.

Finally, make a treatment recommendation for someone infected with this strain of E coli. Suggest alternative antibiotics with different targets, and/or secondary therapies that might be useful.

What do you think you learned from whole genome sequencing that traditional antibiotic resistance testing wouldn’t have told you?

## Discussion
In 2-3 paragraphs, explain what you think the results mean, and why you are interpreting them this way. If you encountered any problems, or answered questions, discuss them and suggest ways to solve them with future experiments or analyses. Also include any information specifically requested in the tutorial.

## Citations
You can use any commonly used format you like, but be consistent. Lab reports will be submitted via turnitin to check for plagiarism, so be sure to cite other people’s ideas, and put everything in your own words (paraphrasing) if you aren’t using direct quotes.
