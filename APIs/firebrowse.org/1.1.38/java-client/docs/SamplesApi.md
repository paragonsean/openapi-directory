# SamplesApi

All URIs are relative to *http://firebrowse.org/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clinical**](SamplesApi.md#clinical) | **GET** /Samples/Clinical | Retrieve TCGA CDEs verbatim, i.e. not normalized by Firehose. |
| [**clinicalFH**](SamplesApi.md#clinicalFH) | **GET** /Samples/Clinical_FH | Retrieve CDEs normalized by Firehose and selected for analyses. |
| [**mRNASeq**](SamplesApi.md#mRNASeq) | **GET** /Samples/mRNASeq | Retrieve mRNASeq data. |
| [**miRSeq**](SamplesApi.md#miRSeq) | **GET** /Samples/miRSeq | Retrieve miRSeq data. |


<a id="clinical"></a>
# **clinical**
> clinical(format, cohort, tcgaParticipantBarcode, cdeName, page, pageSize, sortBy)

Retrieve TCGA CDEs verbatim, i.e. not normalized by Firehose.

This service returns patient clinical data from TCGA, verbatim. It differs from the Samples/Clinical_FH method by providing access to all TCGA CDEs in their original form, not merely the subset of CDEs normalized by Firehose for analyses.  Results may be selected by disease cohort, patient barcode or CDE name, but at least one cohort, barcode, or CDE must be provided. When filtering by CDE note that only when a patient record contains one or more of the selected CDEs will it be returned. Visit the Metadata/ClinicalNames api function to see the entire list of TCGA CDEs that may be queried via this method. For more information on how clinical data are processed, see our &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation#Documentation-ClinicalPipeline\&quot;&gt;pipeline documentation&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    SamplesApi apiInstance = new SamplesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> tcgaParticipantBarcode = Arrays.asList(); // List<String> | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    List<String> cdeName = Arrays.asList(); // List<String> | Retrieve results only for specified CDEs, per the Metadata/ClinicalNames function
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(150); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "tcga_participant_barcode"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.clinical(format, cohort, tcgaParticipantBarcode, cdeName, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamplesApi#clinical");
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
| **cohort** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] [enum: ACC, BLCA, BRCA, CESC, CHOL, COAD, COADREAD, DLBC, ESCA, FPPP, GBM, GBMLGG, HNSC, KICH, KIPAN, KIRC, KIRP, LAML, LGG, LIHC, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, READ, SARC, SKCM, STAD, STES, TGCT, THCA, THYM, UCEC, UCS, UVM] |
| **tcgaParticipantBarcode** | [**List&lt;String&gt;**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] |
| **cdeName** | [**List&lt;String&gt;**](String.md)| Retrieve results only for specified CDEs, per the Metadata/ClinicalNames function | [optional] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: tcga_participant_barcode, cohort, cde_name] |

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

<a id="clinicalFH"></a>
# **clinicalFH**
> clinicalFH(format, cohort, tcgaParticipantBarcode, fhCdeName, page, pageSize, sortBy)

Retrieve CDEs normalized by Firehose and selected for analyses.

This service returns patient-level clinical data elements (CDEs) that have been normalized by Firehose for use in analyses. Results may be selected by disease cohort, patient barcode or CDE name, but at least one cohort, barcode or CDE must be provided. When filtering by CDE note that only when a  patient record contains one or more of the selected CDEs will it be returned. Visit &lt;a href&#x3D;\&quot;http://gdac.broadinstitute.org/runs/info/clinical\&quot;&gt;this table of CDEs&lt;/a&gt; to see what&#39;s available for every disase cohort; for more information on how these CDEs are processed see our &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation#Documentation-ClinicalPipeline\&quot;&gt;pipeline documentation&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    SamplesApi apiInstance = new SamplesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> tcgaParticipantBarcode = Arrays.asList(); // List<String> | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    List<String> fhCdeName = Arrays.asList(); // List<String> | Retrieve results only for the CDEs specified from the scrollable list.
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "tcga_participant_barcode"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.clinicalFH(format, cohort, tcgaParticipantBarcode, fhCdeName, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamplesApi#clinicalFH");
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
| **cohort** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] [enum: ACC, BLCA, BRCA, CESC, CHOL, COAD, COADREAD, DLBC, ESCA, FPPP, GBM, GBMLGG, HNSC, KICH, KIPAN, KIRC, KIRP, LAML, LGG, LIHC, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, READ, SARC, SKCM, STAD, STES, TGCT, THCA, THYM, UCEC, UCS, UVM] |
| **tcgaParticipantBarcode** | [**List&lt;String&gt;**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] |
| **fhCdeName** | [**List&lt;String&gt;**](String.md)| Retrieve results only for the CDEs specified from the scrollable list. | [optional] [enum: age_at_diagnosis, age_began_smoking_in_years, Breslow_thickness, cause_of_death, cervical_carcinoma_pelvic_extension_text, cervix_suv_results, chemo_concurrent_type, clinical_stage, corpus_involvement, date_of_initial_pathologic_diagnosis, days_to_death, days_to_last_followup, days_to_last_known_alive, days_to_psa, days_to_submitted_specimen_dx, ethnicity, extrathyroidal_extension, gender, gleason_score, height_cm_at_diagnosis, histological_type, history_hormonal_contraceptives_use, hysterectomy_type, initial_pathologic_dx_year, karnofsky_performance_score, keratinization_squamous_cell, lymph_node_location, lymph_nodes_examined, lymph_nodes_examined_he_count, lymphovascular_involvement, melanoma_primary_known, melanoma_ulceration, menopause_status, multifocality, neoplasm_histologic_grade, number_of_lymph_nodes, number_pack_years_smoked, pathologic_stage, pathology_M_stage, pathology_N_stage, pathology_T_stage, pos_lymph_node_location, pregnancies_count_ectopic, pregnancies_count_live_birth, pregnancies_count_stillbirth, pregnancies_count_total, pregnancy_spontaneous_abortion_count, pregnancy_therapeutic_abortion_count, psa_value, race, radiation_exposure, radiation_therapy, radiation_therapy_status, residual_tumor, tobacco_smoking_history, tobacco_smoking_pack_years_smoked, tobacco_smoking_year_stopped, tumor_size, tumor_stage, tumor_status, tumor_tissue_site, vital_status, weight_kg_at_diagnosis, year_of_tobacco_smoking_onset, years_to_birth] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: tcga_participant_barcode, cohort, fh_cde_name] |

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

<a id="mRNASeq"></a>
# **mRNASeq**
> mRNASeq(format, gene, cohort, tcgaParticipantBarcode, sampleType, protocol, page, pageSize, sortBy)

Retrieve mRNASeq data.

This service returns sample-level log2 mRNASeq expression values. Results may be filtered by gene, cohort, barcode, sample type or characterization protocol, but at least one gene must be supplied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    SamplesApi apiInstance = new SamplesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> gene = Arrays.asList(); // List<String> | Comma separated list of gene name(s).
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> tcgaParticipantBarcode = Arrays.asList(); // List<String> | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    List<String> sampleType = Arrays.asList(); // List<String> | Narrow search to one or more TCGA sample types from the scrollable list.
    List<String> protocol = Arrays.asList("RSEM"); // List<String> | Narrow search to one or more sample characterization protocols from the scrollable list.
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "tcga_participant_barcode"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.mRNASeq(format, gene, cohort, tcgaParticipantBarcode, sampleType, protocol, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamplesApi#mRNASeq");
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
| **gene** | [**List&lt;String&gt;**](String.md)| Comma separated list of gene name(s). | [optional] |
| **cohort** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] [enum: ACC, BLCA, BRCA, CESC, CHOL, COAD, COADREAD, DLBC, ESCA, FPPP, GBM, GBMLGG, HNSC, KICH, KIPAN, KIRC, KIRP, LAML, LGG, LIHC, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, READ, SARC, SKCM, STAD, STES, TGCT, THCA, THYM, UCEC, UCS, UVM] |
| **tcgaParticipantBarcode** | [**List&lt;String&gt;**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] |
| **sampleType** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA sample types from the scrollable list. | [optional] [enum: NB, NBC, NBM, NT, TAM, TAP, TB, TM, TP, TR] |
| **protocol** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more sample characterization protocols from the scrollable list. | [optional] [enum: RPKM, RSEM] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: tcga_participant_barcode, cohort, gene, protocol, sample_type] |

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

<a id="miRSeq"></a>
# **miRSeq**
> miRSeq(format, mir, cohort, tcgaParticipantBarcode, tool, sampleType, page, pageSize, sortBy)

Retrieve miRSeq data.

This service returns sample-level log2 miRSeq expression values. Results may be filtered by miR, cohort, barcode, sample type or Firehose preprocessing tool, but at least one miR must be supplied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    SamplesApi apiInstance = new SamplesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> mir = Arrays.asList(); // List<String> | Comma separated list of miR names (e.g. hsa-let-7b-5p,hsa-let-7a-1).
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> tcgaParticipantBarcode = Arrays.asList(); // List<String> | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    List<String> tool = Arrays.asList("miRseq_Mature_Preprocess"); // List<String> | Narrow search to include only data/results produced by the selected Firehose tool.
    List<String> sampleType = Arrays.asList(); // List<String> | Narrow search to one or more TCGA sample types from the scrollable list.
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "tcga_participant_barcode"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.miRSeq(format, mir, cohort, tcgaParticipantBarcode, tool, sampleType, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamplesApi#miRSeq");
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
| **mir** | [**List&lt;String&gt;**](String.md)| Comma separated list of miR names (e.g. hsa-let-7b-5p,hsa-let-7a-1). | [optional] |
| **cohort** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] [enum: ACC, BLCA, BRCA, CESC, CHOL, COAD, COADREAD, DLBC, ESCA, FPPP, GBM, GBMLGG, HNSC, KICH, KIPAN, KIRC, KIRP, LAML, LGG, LIHC, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, READ, SARC, SKCM, STAD, STES, TGCT, THCA, THYM, UCEC, UCS, UVM] |
| **tcgaParticipantBarcode** | [**List&lt;String&gt;**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] |
| **tool** | [**List&lt;String&gt;**](String.md)| Narrow search to include only data/results produced by the selected Firehose tool. | [optional] [enum: miRseq_Mature_Preprocess, miRseq_Preprocess] |
| **sampleType** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA sample types from the scrollable list. | [optional] [enum: NB, NBC, NBM, NT, TAM, TAP, TB, TM, TP, TR] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: tcga_participant_barcode, cohort, tool, mir, sample_type] |

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

