# AnalysesApi

All URIs are relative to *http://firebrowse.org/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**all**](AnalysesApi.md#all) | **GET** /Analyses/CopyNumber/Genes/All | Retrieve all data by genes Gistic2 results. |
| [**amplified**](AnalysesApi.md#amplified) | **GET** /Analyses/CopyNumber/Genes/Amplified | Retrieve Gistic2 significantly amplified genes results. |
| [**deleted**](AnalysesApi.md#deleted) | **GET** /Analyses/CopyNumber/Genes/Deleted | Retrieve Gistic2 significantly deleted genes results. |
| [**featureTable**](AnalysesApi.md#featureTable) | **GET** /Analyses/FeatureTable | Retrieve aggregated analysis features table. |
| [**focal**](AnalysesApi.md#focal) | **GET** /Analyses/CopyNumber/Genes/Focal | Retrieve focal data by genes Gistic2 results. |
| [**mAF**](AnalysesApi.md#mAF) | **GET** /Analyses/Mutation/MAF | Retrieve MutSig final analysis MAF. |
| [**mRNASeqQuartiles**](AnalysesApi.md#mRNASeqQuartiles) | **GET** /Analyses/mRNASeq/Quartiles | Returns RNASeq expression quartiles, e.g. suitable for drawing a boxplot. |
| [**reports**](AnalysesApi.md#reports) | **GET** /Analyses/Reports | Retrieve links to summary reports from Firehose analysis runs. |
| [**sMG**](AnalysesApi.md#sMG) | **GET** /Analyses/Mutation/SMG | Retrieve Significantly Mutated Genes (SMG). |
| [**thresholded**](AnalysesApi.md#thresholded) | **GET** /Analyses/CopyNumber/Genes/Thresholded | Retrieve all thresholded by genes Gistic2 results. |


<a id="all"></a>
# **all**
> all(format, cohort, gene, tcgaParticipantBarcode, page, pageSize, sortBy)

Retrieve all data by genes Gistic2 results.

This service provides access to the Gistic2 all_data_by_genes.txt output data. This data is a gene-level table of copy number values for all samples. The returned copy number values are in units (copy number - 2) so that no amplification or deletion is 0, genes with amplifications have positive values, and genes with deletions are negative values. The data are converted from marker level to gene level using the extreme method: a gene is assigned the greatest amplification or the least deletion value among the markers it covers. Results may be filtered by cohort, gene, or barcode, but at least one gene or barcode must be supplied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> gene = Arrays.asList(); // List<String> | Comma separated list of gene name(s).
    List<String> tcgaParticipantBarcode = Arrays.asList(); // List<String> | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "tcga_participant_barcode"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.all(format, cohort, gene, tcgaParticipantBarcode, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#all");
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
| **gene** | [**List&lt;String&gt;**](String.md)| Comma separated list of gene name(s). | [optional] |
| **tcgaParticipantBarcode** | [**List&lt;String&gt;**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: tcga_participant_barcode, cohort, gene] |

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

<a id="amplified"></a>
# **amplified**
> amplified(format, cohort, gene, q, page, pageSize, sortBy)

Retrieve Gistic2 significantly amplified genes results.

This service provides access to the Gistic2 amp_genes.conf_99.txt output data.  At least 1 gene or cohort must be supplied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> gene = Arrays.asList(); // List<String> | Comma separated list of gene name(s).
    BigDecimal q = new BigDecimal(78); // BigDecimal | Only return results with Q-value <= given threshold.
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "q"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.amplified(format, cohort, gene, q, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#amplified");
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
| **gene** | [**List&lt;String&gt;**](String.md)| Comma separated list of gene name(s). | [optional] |
| **q** | **BigDecimal**| Only return results with Q-value &lt;&#x3D; given threshold. | [optional] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: q, cohort, gene] |

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

<a id="deleted"></a>
# **deleted**
> deleted(format, cohort, gene, q, page, pageSize, sortBy)

Retrieve Gistic2 significantly deleted genes results.

This service provides access to the Gistic2 del_genes.conf_99.txt output data.  At least 1 gene or cohort must be supplied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> gene = Arrays.asList(); // List<String> | Comma separated list of gene name(s).
    BigDecimal q = new BigDecimal(78); // BigDecimal | Only return results with Q-value <= given threshold.
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "q"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.deleted(format, cohort, gene, q, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#deleted");
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
| **gene** | [**List&lt;String&gt;**](String.md)| Comma separated list of gene name(s). | [optional] |
| **q** | **BigDecimal**| Only return results with Q-value &lt;&#x3D; given threshold. | [optional] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: q, cohort, gene] |

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

<a id="featureTable"></a>
# **featureTable**
> featureTable(format, cohort, date, column, page, pageSize)

Retrieve aggregated analysis features table.

This service returns part or all of the so-called &lt;strong&gt;feature table&lt;/strong&gt;; which aggregates the most important findings across ALL pipelines in the GDAC Firehose analysis workflow into a single table for simple access.  One feature table is created per disease cohort.  Results may be filtered by date or cohort, but at least 1 cohort must be specified here. For more details please visit the &lt;a href&#x3D;https://confluence.broadinstitute.org/display/GDAC/Documentation\\#Documentation-FeatureTable&gt;online documentation&lt;/a&gt;.  Please note that the service is still undergoing experimental evaluation and does not return JSON format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    String format = "tsv"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<LocalDate> date = Arrays.asList(); // List<LocalDate> | Select one or more date stamps.
    List<String> column = Arrays.asList(); // List<String> | Comma separated list of which data columns/fields to return.
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    try {
      apiInstance.featureTable(format, cohort, date, column, page, pageSize);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#featureTable");
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
| **format** | **String**| Format of result. | [optional] [default to tsv] [enum: tsv, csv] |
| **cohort** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] [enum: ACC, BLCA, BRCA, CESC, CHOL, COAD, COADREAD, DLBC, ESCA, FPPP, GBM, GBMLGG, HNSC, KICH, KIPAN, KIRC, KIRP, LAML, LGG, LIHC, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, READ, SARC, SKCM, STAD, STES, TGCT, THCA, THYM, UCEC, UCS, UVM] |
| **date** | [**List&lt;LocalDate&gt;**](LocalDate.md)| Select one or more date stamps. | [optional] [enum: Thu Jan 01 00:36:00 EST 1970, Thu Jan 01 00:35:50 EST 1970, Thu Jan 01 00:35:50 EST 1970, Thu Jan 01 00:35:41 EST 1970] |
| **column** | [**List&lt;String&gt;**](String.md)| Comma separated list of which data columns/fields to return. | [optional] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |

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

<a id="focal"></a>
# **focal**
> focal(format, cohort, gene, tcgaParticipantBarcode, page, pageSize, sortBy)

Retrieve focal data by genes Gistic2 results.

This service provides access to the Gistic2 focal_data_by_genes.txt output data. This output is similar to the all_data_by_genes.txt output, but using only focal events with lengths greater than the  focal length cutoff. This data is a gene-level table of copy number values for all samples. The returned copy number values are in units (copy number - 2) so that no amplification or deletion is 0, genes with amplifications have positive values, and genes with deletions are negative values. The data are converted from marker level to gene level using the extreme method: a gene is assigned the greatest amplification or the least deletion value among the markers it covers. Results may be filtered by cohort, gene, and/or barcode, but at least one gene or barcode must be supplied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> gene = Arrays.asList(); // List<String> | Comma separated list of gene name(s).
    List<String> tcgaParticipantBarcode = Arrays.asList(); // List<String> | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "tcga_participant_barcode"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.focal(format, cohort, gene, tcgaParticipantBarcode, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#focal");
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
| **gene** | [**List&lt;String&gt;**](String.md)| Comma separated list of gene name(s). | [optional] |
| **tcgaParticipantBarcode** | [**List&lt;String&gt;**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: tcga_participant_barcode, cohort, gene] |

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

<a id="mAF"></a>
# **mAF**
> mAF(format, cohort, tool, gene, tcgaParticipantBarcode, column, page, pageSize, sortBy)

Retrieve MutSig final analysis MAF.

This service returns columns from the MAF generated by MutSig. Results may be filtered by gene, cohort, tool, or barcode, but at least one gene OR barcode OR cohort must be given.  By default a subset consisting of the most commonly used columns will be returned, but that can be modified with the column parameter. Specifying &#39;all&#39; in this parameter is a convenient way to return every column of the respective MAF, and has precedence over any any other column selection expression.  The complete list of column names that may be specified is &lt;a href&#x3D;&#39;http://firebrowse.org/api-docs/#!/Metadata/MAFColNames&#39;&gt;given here&lt;/a&gt;.  For more information on the mutation data, and how it is processed by Firehose, please consult the &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation#Documentation-MutationPipelines\&quot;&gt;pipeline documentation&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> tool = Arrays.asList("MutSig2CV"); // List<String> | Narrow search to include only data/results produced by the selected Firehose tool.
    List<String> gene = Arrays.asList(); // List<String> | Comma separated list of gene name(s).
    List<String> tcgaParticipantBarcode = Arrays.asList(); // List<String> | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    List<String> column = Arrays.asList(); // List<String> | Comma separated list of which data columns/fields to return.
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "tcga_participant_barcode"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.mAF(format, cohort, tool, gene, tcgaParticipantBarcode, column, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#mAF");
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
| **tool** | [**List&lt;String&gt;**](String.md)| Narrow search to include only data/results produced by the selected Firehose tool. | [optional] [enum: MutSig2.0, MutSig2CV] |
| **gene** | [**List&lt;String&gt;**](String.md)| Comma separated list of gene name(s). | [optional] |
| **tcgaParticipantBarcode** | [**List&lt;String&gt;**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] |
| **column** | [**List&lt;String&gt;**](String.md)| Comma separated list of which data columns/fields to return. | [optional] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: tcga_participant_barcode, cohort, tool, gene] |

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

<a id="mRNASeqQuartiles"></a>
# **mRNASeqQuartiles**
> mRNASeqQuartiles(gene, format, cohort, protocol, sampleType, exclude)

Returns RNASeq expression quartiles, e.g. suitable for drawing a boxplot.

For a given gene compute quartiles and extrema, suitable e.g. for drawing a boxplot (Tukey 1977).  Results may be filtered by cohort, sample type, patient barcode  or characterization protocol, and are returned sorted by cohort.  Note that samples for which no expression value was recorded (e.g. &lt;a href&#x3D;\&quot;http://firebrowse.org/api/v1/Samples/mRNASeq?&amp;gene&#x3D;egfr&amp;cohort&#x3D;SKCM&amp;tcga_participant_barcode&#x3D;TCGA-GN-A262\&quot;&gt;the melanoma sample TCGA-GN-262&lt;/a&gt;) are removed prior to calculation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    String gene = "gene_example"; // String | Enter a single gene name.
    String format = "json"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> protocol = Arrays.asList("RSEM"); // List<String> | Narrow search to one or more sample characterization protocols from the scrollable list.
    List<String> sampleType = Arrays.asList("tumors"); // List<String> | For which type of sample(s) should quartiles be computed?
    List<String> exclude = Arrays.asList(); // List<String> | Comma separated list of TCGA participants, identified by barcodes such as TCGA-GF-A4EO, denoting samples to exclude from computation.
    try {
      apiInstance.mRNASeqQuartiles(gene, format, cohort, protocol, sampleType, exclude);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#mRNASeqQuartiles");
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
| **gene** | **String**| Enter a single gene name. | |
| **format** | **String**| Format of result. | [optional] [default to json] [enum: json, tsv, csv] |
| **cohort** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] [enum: ACC, BLCA, BRCA, CESC, CHOL, COAD, COADREAD, DLBC, ESCA, FPPP, GBM, GBMLGG, HNSC, KICH, KIPAN, KIRC, KIRP, LAML, LGG, LIHC, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, READ, SARC, SKCM, STAD, STES, TGCT, THCA, THYM, UCEC, UCS, UVM] |
| **protocol** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more sample characterization protocols from the scrollable list. | [optional] [enum: RPKM, RSEM] |
| **sampleType** | [**List&lt;String&gt;**](String.md)| For which type of sample(s) should quartiles be computed? | [optional] [enum: tumors, normals, TP, TB, TAM, TBM, NBC, TRB, TR, TRBM, TAP, TM, THOC, NB, NT, NEBV, NBM] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Comma separated list of TCGA participants, identified by barcodes such as TCGA-GF-A4EO, denoting samples to exclude from computation. | [optional] |

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

<a id="reports"></a>
# **reports**
> reports(format, date, cohort, name, type, page, pageSize, sortBy)

Retrieve links to summary reports from Firehose analysis runs.

This service returns URLs to the analysis result reports for runs of the Broad Institute GDAC Firehose analysis pipeline. At least one year of run reports are maintained in the database, but the reports from the latest run will be returned by default. The set of &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Nozzle\&quot;&gt;Nozzle&lt;/a&gt; reports returned may be filtered by disease cohort, report type and report name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<LocalDate> date = Arrays.asList(); // List<LocalDate> | Select one or more date stamps.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> name = Arrays.asList(); // List<String> | Narrow search to one or more report names.
    List<String> type = Arrays.asList(); // List<String> | Narrow search to one or more report types.
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "date"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.reports(format, date, cohort, name, type, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#reports");
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
| **date** | [**List&lt;LocalDate&gt;**](LocalDate.md)| Select one or more date stamps. | [optional] [enum: Thu Jan 01 00:36:00 EST 1970, Thu Jan 01 00:35:50 EST 1970, Thu Jan 01 00:35:50 EST 1970, Thu Jan 01 00:35:41 EST 1970, Thu Jan 01 00:35:40 EST 1970, Thu Jan 01 00:35:40 EST 1970, Thu Jan 01 00:35:40 EST 1970, Thu Jan 01 00:35:30 EST 1970, Thu Jan 01 00:35:30 EST 1970, Thu Jan 01 00:35:30 EST 1970] |
| **cohort** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] [enum: ACC, BLCA, BRCA, CESC, CHOL, COAD, COADREAD, DLBC, ESCA, FPPP, GBM, GBMLGG, HNSC, KICH, KIPAN, KIRC, KIRP, LAML, LGG, LIHC, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, READ, SARC, SKCM, STAD, STES, TGCT, THCA, THYM, UCEC, UCS, UVM] |
| **name** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more report names. | [optional] [enum: Aggregate_AnalysisFeatures, CopyNumber_Clustering_CNMF, CopyNumber_Clustering_CNMF_thresholded, CopyNumber_Gistic2, CopyNumberLowPass_Gistic2, Correlate_Clinical_vs_CopyNumber_Arm, Correlate_Clinical_vs_CopyNumber_Focal, Correlate_Clinical_vs_Methylation, Correlate_Clinical_vs_miR, Correlate_Clinical_vs_miRseq, Correlate_Clinical_vs_Molecular_Subtypes, Correlate_Clinical_vs_mRNA, Correlate_Clinical_vs_mRNAseq, Correlate_Clinical_vs_Mutation, Correlate_Clinical_vs_Mutation_APOBEC_Categorical, Correlate_Clinical_vs_Mutation_APOBEC_Continuous, Correlate_Clinical_vs_MutationRate, Correlate_Clinical_vs_RPPA, Correlate_CopyNumber_vs_miR, Correlate_CopyNumber_vs_mRNA, Correlate_CopyNumber_vs_mRNAseq, Correlate_Methylation_vs_mRNA, Correlate_molecularSubtype_vs_CopyNumber_Arm, Correlate_molecularSubtype_vs_CopyNumber_Focal, Correlate_molecularSubtype_vs_Mutation, Correlate_mRNAseq_vs_Mutation_APOBEC, Methylation_Clustering_CNMF, miR_Clustering_CNMF, miR_Clustering_Consensus, miR_Clustering_Consensus_Plus, miR_FindDirectTargets, miRseq_Clustering_CNMF, miRseq_Clustering_Consensus, miRseq_Clustering_Consensus_Plus, miRseq_FindDirectTargets, miRseq_Mature_Clustering_CNMF, miRseq_Mature_Clustering_Consensus, miRseq_Mature_Clustering_Consensus_Plus, mRNA_Clustering_CNMF, mRNA_Clustering_Consensus, mRNA_Clustering_Consensus_Plus, mRNAseq_Clustering_CNMF, mRNAseq_Clustering_Consensus, mRNAseq_Clustering_Consensus_Plus, Mutation_APOBEC, Mutation_Assessor, Mutation_CHASM, MutSig2.0, MutSig2CV, MutSigCV, MutSigNozzleReport1.5, MutSigNozzleReport2.0, MutSigNozzleReport2CV, MutSigNozzleReportCV, MutSigNozzleReportMerged, Pathway_FindEnrichedGenes, Pathway_GSEA_mRNAseq, Pathway_Hotnet, Pathway_Overlaps_MSigDB_MutSig2CV, Pathway_Paradigm_mRNA, Pathway_Paradigm_mRNA_And_Copy_Number, Pathway_Paradigm_RNASeq, Pathway_Paradigm_RNASeq_And_Copy_Number, RPPA_Clustering_CNMF, RPPA_Clustering_Consensus, RPPA_Clustering_Consensus_Plus] |
| **type** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more report types. | [optional] [enum: Aggregate, Clustering, CopyNumber, Correlations, Expression, Mutation, Pathway] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to date] [enum: date, cohort, type, name] |

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

<a id="sMG"></a>
# **sMG**
> sMG(format, cohort, tool, rank, gene, q, page, pageSize, sortBy)

Retrieve Significantly Mutated Genes (SMG).

This service provides a list of significantly mutated genes, as scored by MutSig.  It may be filtered by cohort, rank, gene, tool and/or Q-value threshold, but at least one cohort or gene must be supplied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> tool = Arrays.asList("MutSig2CV"); // List<String> | Narrow search to include only data/results produced by the selected Firehose tool.
    Integer rank = 56; // Integer | Number of significant genes to return.
    List<String> gene = Arrays.asList(); // List<String> | Comma separated list of gene name(s).
    BigDecimal q = new BigDecimal(78); // BigDecimal | Only return results with Q-value <= given threshold.
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "q"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.sMG(format, cohort, tool, rank, gene, q, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#sMG");
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
| **tool** | [**List&lt;String&gt;**](String.md)| Narrow search to include only data/results produced by the selected Firehose tool. | [optional] [enum: MutSig2.0, MutSig2CV, MutSigCV] |
| **rank** | **Integer**| Number of significant genes to return. | [optional] |
| **gene** | [**List&lt;String&gt;**](String.md)| Comma separated list of gene name(s). | [optional] |
| **q** | **BigDecimal**| Only return results with Q-value &lt;&#x3D; given threshold. | [optional] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to rank] [enum: q, cohort, tool, gene, rank] |

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

<a id="thresholded"></a>
# **thresholded**
> thresholded(format, cohort, gene, tcgaParticipantBarcode, page, pageSize, sortBy)

Retrieve all thresholded by genes Gistic2 results.

This service provides access to the Gistic2 all_thresholded_by_genes.txt output data. A gene-level table of discrete amplification and deletion indicators for all samples. A table value of 0 means no amplification or deletion above the threshold. Amplifications are positive numbers: 1 means amplification above the amplification threshold; 2 means amplifications larger to the arm level amplifications observed for the sample. Deletions are represented by negative table values: -1 represents deletion beyond the threshold; -2 means deletions greater than the minimum arm-level deletion observed for the sample. Results maybe filtered by cohort, gene or barcode, but at least one gene or barcode must be supplied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> gene = Arrays.asList(); // List<String> | Comma separated list of gene name(s).
    List<String> tcgaParticipantBarcode = Arrays.asList(); // List<String> | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "tcga_participant_barcode"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.thresholded(format, cohort, gene, tcgaParticipantBarcode, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#thresholded");
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
| **gene** | [**List&lt;String&gt;**](String.md)| Comma separated list of gene name(s). | [optional] |
| **tcgaParticipantBarcode** | [**List&lt;String&gt;**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] |
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: tcga_participant_barcode, cohort, gene] |

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

