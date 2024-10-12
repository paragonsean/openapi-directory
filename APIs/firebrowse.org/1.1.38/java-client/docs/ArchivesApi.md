# ArchivesApi

All URIs are relative to *http://firebrowse.org/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**standardData**](ArchivesApi.md#standardData) | **GET** /Archives/StandardData | Retrieve standard data archives. |


<a id="standardData"></a>
# **standardData**
> standardData(format, date, cohort, dataType, tool, platform, center, level, protocol, page, pageSize, sortBy)

Retrieve standard data archives.

This service returns the archive URLs for our Firehose standard data runs, providing a RESTful interface similar in spirit to the command line &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Download\&quot;&gt;firehose_get&lt;/a&gt; tool. The archives can be filtered based on date, cohort, data type, platform, center, data level, and protocol.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    ArchivesApi apiInstance = new ArchivesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<LocalDate> date = Arrays.asList(); // List<LocalDate> | Select one or more date stamps.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> dataType = Arrays.asList(); // List<String> | Narrow search to one or more TCGA data types from the scrollable list.
    List<String> tool = Arrays.asList(); // List<String> | Narrow search to include only data/results produced by the selected Firehose tool.
    List<String> platform = Arrays.asList(); // List<String> | Narrow search to one or more TCGA data generation platforms from the scrollable list.
    List<String> center = Arrays.asList(); // List<String> | Narrow search to one or more TCGA centers from the scrollable list.
    List<Integer> level = Arrays.asList(); // List<Integer> | Narrow search to one or more TCGA data levels.
    List<String> protocol = Arrays.asList(); // List<String> | Narrow search to one or more sample characterization protocols from the scrollable list.
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "cohort"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.standardData(format, date, cohort, dataType, tool, platform, center, level, protocol, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchivesApi#standardData");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **format** | **String**| Format of result. | [optional] [default to json] [enum: json, tsv, csv] |
| **date** | [**List&lt;LocalDate&gt;**](LocalDate.md)| Select one or more date stamps. | [optional] [enum: Thu Jan 01 00:36:00 EST 1970, Thu Jan 01 00:35:51 EST 1970, Thu Jan 01 00:35:50 EST 1970, Thu Jan 01 00:35:50 EST 1970, Thu Jan 01 00:35:50 EST 1970, Thu Jan 01 00:35:50 EST 1970, Thu Jan 01 00:35:41 EST 1970, Thu Jan 01 00:35:41 EST 1970, Thu Jan 01 00:35:40 EST 1970, Thu Jan 01 00:35:40 EST 1970, Thu Jan 01 00:35:40 EST 1970, Thu Jan 01 00:35:40 EST 1970, Thu Jan 01 00:35:40 EST 1970] |
| **cohort** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] [enum: ACC, BLCA, BRCA, CESC, CHOL, COAD, COADREAD, DLBC, ESCA, FPPP, GBM, GBMLGG, HNSC, KICH, KIPAN, KIRC, KIRP, LAML, LGG, LIHC, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, READ, SARC, SKCM, STAD, STES, TGCT, THCA, THYM, UCEC, UCS, UVM] |
| **dataType** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA data types from the scrollable list. | [optional] [enum: Clinical, CopyNumber, LowPass, MAF, Methylation, miR, miRSeq, mRNA, mRNASeq, rawMAF, rawWIG, RPPA, WIG] |
| **tool** | [**List&lt;String&gt;**](String.md)| Narrow search to include only data/results produced by the selected Firehose tool. | [optional] [enum: Clinical_Pick_Tier1, Merge_Clinical, Merge_cna__cgh_1x1m_g4447a__mskcc_org__Level_3__segmentation_data_computation__seg, Merge_cna__hg_cgh_244a__hms_harvard_edu__Level_3__segmentation__seg, Merge_cna__hg_cgh_244a__mskcc_org__Level_3__segmentation_data_computation__seg, Merge_cna__hg_cgh_415k_g4124a__hms_harvard_edu__Level_3__segmentation__seg, Merge_cna__illuminahiseq_dnaseqc__hms_harvard_edu__Level_3__segmentation__seg, Merge_exon__huex_1_0_st_v2__lbl_gov__Level_2__quantile_normalization_exon__data, Merge_exon__huex_1_0_st_v2__lbl_gov__Level_3__quantile_normalization_gene__data, Merge_exon__huex_1_0_st_v2__lbl_gov__Level_3__segmented_as_firma__data, Merge_methylation__humanmethylation27__jhu_usc_edu__Level_3__within_bioassay_data_set_function__data, Merge_methylation__humanmethylation450__jhu_usc_edu__Level_3__within_bioassay_data_set_function__data, Merge_mirna__h_mirna_8x15k__unc_edu__Level_3__unc_DWD_Batch_adjusted__data, Merge_mirna__h_mirna_8x15kv2__unc_edu__Level_3__unc_DWD_Batch_adjusted__data, Merge_mirnaseq__illuminaga_mirnaseq__bcgsc_ca__Level_3__miR_gene_expression__data, Merge_mirnaseq__illuminaga_mirnaseq__bcgsc_ca__Level_3__miR_isoform_expression__data, Merge_mirnaseq__illuminahiseq_mirnaseq__bcgsc_ca__Level_3__miR_gene_expression__data, Merge_mirnaseq__illuminahiseq_mirnaseq__bcgsc_ca__Level_3__miR_isoform_expression__data, Merge_protein_exp__mda_rppa_core__mdanderson_org__Level_3__protein_normalization__data, Merge_rnaseq__illuminaga_rnaseq__bcgsc_ca__Level_3__exon_expression__data, Merge_rnaseq__illuminaga_rnaseq__bcgsc_ca__Level_3__gene_expression__data, Merge_rnaseq__illuminaga_rnaseq__bcgsc_ca__Level_3__splice_junction_expression__data, Merge_rnaseq__illuminaga_rnaseq__unc_edu__Level_3__exon_expression__data, Merge_rnaseq__illuminaga_rnaseq__unc_edu__Level_3__gene_expression__data, Merge_rnaseq__illuminaga_rnaseq__unc_edu__Level_3__splice_junction_expression__data, Merge_rnaseq__illuminahiseq_rnaseq__bcgsc_ca__Level_3__exon_expression__data, Merge_rnaseq__illuminahiseq_rnaseq__bcgsc_ca__Level_3__gene_expression__data, Merge_rnaseq__illuminahiseq_rnaseq__bcgsc_ca__Level_3__splice_junction_expression__data, Merge_rnaseq__illuminahiseq_rnaseq__unc_edu__Level_3__exon_expression__data, Merge_rnaseq__illuminahiseq_rnaseq__unc_edu__Level_3__gene_expression__data, Merge_rnaseq__illuminahiseq_rnaseq__unc_edu__Level_3__splice_junction_expression__data, Merge_rnaseqv2__illuminaga_rnaseqv2__unc_edu__Level_3__exon_quantification__data, Merge_rnaseqv2__illuminaga_rnaseqv2__unc_edu__Level_3__junction_quantification__data, Merge_rnaseqv2__illuminaga_rnaseqv2__unc_edu__Level_3__RSEM_genes__data, Merge_rnaseqv2__illuminaga_rnaseqv2__unc_edu__Level_3__RSEM_genes_normalized__data, Merge_rnaseqv2__illuminaga_rnaseqv2__unc_edu__Level_3__RSEM_isoforms__data, Merge_rnaseqv2__illuminaga_rnaseqv2__unc_edu__Level_3__RSEM_isoforms_normalized__data, Merge_rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__exon_quantification__data, Merge_rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__junction_quantification__data, Merge_rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__RSEM_genes__data, Merge_rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__RSEM_genes_normalized__data, Merge_rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__RSEM_isoforms__data, Merge_rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__RSEM_isoforms_normalized__data, Merge_snp__genome_wide_snp_6__broad_mit_edu__Level_2__birdseed_genotype__birdseed, Merge_snp__genome_wide_snp_6__broad_mit_edu__Level_3__segmented_scna_hg18__seg, Merge_snp__genome_wide_snp_6__broad_mit_edu__Level_3__segmented_scna_hg19__seg, Merge_snp__genome_wide_snp_6__broad_mit_edu__Level_3__segmented_scna_minus_germline_cnv_hg18__seg, Merge_snp__genome_wide_snp_6__broad_mit_edu__Level_3__segmented_scna_minus_germline_cnv_hg19__seg, Merge_snp__human1mduo__hudsonalpha_org__Level_3__segmented_cna__seg, Merge_snp__human1mduo__hudsonalpha_org__Level_3__segmented_cnv__seg, Merge_snp__human1mduo__hudsonalpha_org__Level_3__segmented_loh__seg, Merge_snp__humanhap550__hudsonalpha_org__Level_3__segmented_cna__seg, Merge_snp__humanhap550__hudsonalpha_org__Level_3__segmented_cnv__seg, Merge_snp__humanhap550__hudsonalpha_org__Level_3__segmented_loh__seg, Merge_transcriptome__agilentg4502a_07_1__unc_edu__Level_2__unc_lowess_normalization_probe_level__data, Merge_transcriptome__agilentg4502a_07_1__unc_edu__Level_3__unc_lowess_normalization_gene_level__data, Merge_transcriptome__agilentg4502a_07_2__unc_edu__Level_2__unc_lowess_normalization_probe_level__data, Merge_transcriptome__agilentg4502a_07_2__unc_edu__Level_3__unc_lowess_normalization_gene_level__data, Merge_transcriptome__agilentg4502a_07_3__unc_edu__Level_2__unc_lowess_normalization_probe_level__data, Merge_transcriptome__agilentg4502a_07_3__unc_edu__Level_3__unc_lowess_normalization_gene_level__data, Merge_transcriptome__ht_hg_u133a__broad_mit_edu__Level_2__probeset_rma__data, Merge_transcriptome__ht_hg_u133a__broad_mit_edu__Level_3__gene_rma__data, Methylation_Preprocess, miRseq_Mature_Preprocess, miRseq_Preprocess, mRNA_Preprocess_Median, mRNAseq_Preprocess, Mutation_Packager_Calls, Mutation_Packager_Coverage, Mutation_Packager_Oncotated_Calls, Mutation_Packager_Oncotated_Raw_Calls, Mutation_Packager_Raw_Calls, Mutation_Packager_Raw_Coverage, RPPA_AnnotateWithGene] |
| **platform** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA data generation platforms from the scrollable list. | [optional] [enum: 454, ABI, AgilentG4502A_07, AgilentG4502A_07_1, AgilentG4502A_07_2, AgilentG4502A_07_3, bio, biotab, CGH-1x1M_G4447A, diagnostic_images, fh_analyses, fh_reports, fh_stddata, Genome_Wide_SNP_6, GenomeWideSNP_5, H-miRNA_8x15K, H-miRNA_8x15Kv2, H-miRNA_EarlyAccess, H-miRNA_G4470A, HG-CGH-244A, HG-CGH-415K_G4124A, HG-U133_Plus_2, HG-U133A_2, HT_HG-U133A, HuEx-1_0-st-v2, Human1MDuo, HumanHap550, HumanMethylation27, HumanMethylation450, IlluminaDNAMethylation_OMA002_CPI, IlluminaDNAMethylation_OMA003_CPI, IlluminaGA_DNASeq, IlluminaGA_DNASeq_automated, IlluminaGA_DNASeq_Cont, IlluminaGA_DNASeq_Cont_automated, IlluminaGA_DNASeq_Cont_curated, IlluminaGA_DNASeq_curated, IlluminaGA_miRNASeq, IlluminaGA_mRNA_DGE, IlluminaGA_RNASeq, IlluminaGA_RNASeqV2, IlluminaGG, IlluminaHiSeq_DNASeq, IlluminaHiSeq_DNASeq_automated, IlluminaHiSeq_DNASeq_Cont, IlluminaHiSeq_DNASeq_Cont_automated, IlluminaHiSeq_DNASeq_Cont_curated, IlluminaHiSeq_DNASeq_curated, IlluminaHiSeq_DNASeqC, IlluminaHiSeq_miRNASeq, IlluminaHiSeq_mRNA_DGE, IlluminaHiSeq_RNASeq, IlluminaHiSeq_RNASeqV2, IlluminaHiSeq_TotalRNASeqV2, IlluminaHiSeq_WGBS, Mapping250K_Nsp, Mapping250K_Sty, MDA_RPPA_Core, microsat_i, minbio, minbiotab, Mixed_DNASeq, Mixed_DNASeq_automated, Mixed_DNASeq_Cont, Mixed_DNASeq_Cont_automated, Mixed_DNASeq_Cont_curated, Mixed_DNASeq_curated, pathology_reports, SOLiD_DNASeq, SOLiD_DNASeq_automated, SOLiD_DNASeq_Cont, SOLiD_DNASeq_Cont_automated, SOLiD_DNASeq_Cont_curated, SOLiD_DNASeq_curated, tissue_images, WHG-1x44K_G4112A, WHG-4x44K_G4112F, WHG-CGH_4x44B] |
| **center** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA centers from the scrollable list. | [optional] [enum: bcgsc.ca, broad.mit.edu, broadinstitute.org, genome.wustl.edu, hgsc.bcm.edu, hms.harvard.edu, hudsonalpha.org, intgen.org, jhu-usc.edu, jhu.edu, lbl.gov, mdanderson.org, mskcc.org, nationwidechildrens.org, pnl.gov, rubicongenomics.com, sanger.ac.uk, systemsbiology.org, ucsc.edu, unc.edu, vanderbilt.edu] |
| **level** | [**List&lt;Integer&gt;**](Integer.md)| Narrow search to one or more TCGA data levels. | [optional] [enum: 1, 2, 3, 4] |
| **protocol** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more sample characterization protocols from the scrollable list. | [optional] [enum: birdseed_genotype, exon_expression, exon_quantification, gene_expression, gene_rma, junction_quantification, miR_gene_expression, miR_isoform_expression, probeset_rma, protein_normalization, quantile_normalization_exon, quantile_normalization_gene, RSEM_genes, RSEM_genes_normalized, RSEM_isoforms, RSEM_isoforms_normalized, segmentation, segmentation_data_computation, segmented_as_firma, segmented_cna, segmented_cnv, segmented_loh, segmented_scna_hg18, segmented_scna_hg19, segmented_scna_minus_germline_cnv_hg18, segmented_scna_minus_germline_cnv_hg19, splice_junction_expression, unc_DWD_Batch_adjusted, unc_lowess_normalization_gene_level, unc_lowess_normalization_probe_level, within_bioassay_data_set_function] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: cohort, protocol, center, data_type, level, tool, platform, date] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

