## Extract variants in specific genes from denovo-db
#### Tychele N. Turner, Ph.D.

##### Download the denovo-db files from Zenodo at https://zenodo.org/records/13901296

The script `extract_genes.py` will pull out variant data, in specific genes, from the tab-delimited files in denovo-db.

##### Run default settings to pull out variants in a gene
```
python3 extract_genes.py --nonssc denovo-db_1.8_not_ssc.annotated.final.tab.gz \
 --ssc denovo-db_1.8_ssc.annotated.final.tab.gz \
 --gene EBF3
```

##### Run with additional consequences (you should check the output message on the screen for what you want)
```
python3 extract_genes.py --nonssc denovo-db_1.8_not_ssc.annotated.final.tab.gz \ 
 --ssc denovo-db_1.8_ssc.annotated.final.tab.gz \
 --gene EBF3 \
 --consequences upstream_gene_variant 5_prime_UTR_variant frameshift_variant non_coding_transcript_exon_variant splice_donor_variant splice_donor_variant,non_coding_transcript_variant splice_acceptor_variant splice_acceptor_variant,non_coding_transcript_variant stop_gained downstream_gene_variant intron_variant missense_variant stop_gained,protein_altering_variant intron_variant,non_coding_transcript_variant splice_region_variant,splice_polypyrimidine_tract_variant,intron_variant splice_region_variant,splice_polypyrimidine_tract_variant,intron_variant,non_coding_transcript_variant stop_gained,frameshift_variant synonymous_variant missense_variant,splice_region_variant splice_region_variant,non_coding_transcript_exon_variant frameshift_variant,splice_region_variant inframe_deletion 3_prime_UTR_variant
```

