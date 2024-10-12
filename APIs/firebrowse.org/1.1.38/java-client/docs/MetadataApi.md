# MetadataApi

All URIs are relative to *http://firebrowse.org/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**barcode**](MetadataApi.md#barcode) | **GET** /Metadata/SampleType/Barcode/{TCGA_Barcode} | Given a TCGA barcode, return its short letter sample type code. |
| [**centers**](MetadataApi.md#centers) | **GET** /Metadata/Centers | Obtain identities of TCGA consortium member centers. |
| [**clinicalNames**](MetadataApi.md#clinicalNames) | **GET** /Metadata/ClinicalNames | Retrieve names of all TCGA clinical data elements (CDEs). |
| [**clinicalNamesFH**](MetadataApi.md#clinicalNamesFH) | **GET** /Metadata/ClinicalNames_FH | Retrieve names of CDEs normalized by Firehose and selected for analyses. |
| [**code**](MetadataApi.md#code) | **GET** /Metadata/SampleType/Code/{code} | Translate from numeric to symbolic TCGA sample codes. |
| [**cohorts**](MetadataApi.md#cohorts) | **GET** /Metadata/Cohorts | Translate TCGA cohort abbreviations to full disease names. |
| [**counts**](MetadataApi.md#counts) | **GET** /Metadata/Counts | Retrieve sample counts. |
| [**dates**](MetadataApi.md#dates) | **GET** /Metadata/Dates | Retrieve dates of all GDAC Firehose stddata &amp; analyses runs that have been ingested into FireBrowse. |
| [**heartBeat**](MetadataApi.md#heartBeat) | **GET** /Metadata/HeartBeat | Simple way to discern whether API server is up and running |
| [**mAFColNames**](MetadataApi.md#mAFColNames) | **GET** /Metadata/MAFColNames | Retrieve names of all columns in the mutation annotation files (MAFs) served by FireBrowse. |
| [**patients**](MetadataApi.md#patients) | **GET** /Metadata/Patients | Retrieve list of all TCGA patients. |
| [**platforms**](MetadataApi.md#platforms) | **GET** /Metadata/Platforms | Translate TCGA platform codes to full platform names. |
| [**sampleTypes**](MetadataApi.md#sampleTypes) | **GET** /Metadata/SampleTypes | Return all TCGA sample type codes, both numeric and symbolic. |
| [**shortLetterCode**](MetadataApi.md#shortLetterCode) | **GET** /Metadata/SampleType/ShortLetterCode/{short_letter_code} | Translate from symbolic to numeric TCGA sample codes. |
| [**tSSites**](MetadataApi.md#tSSites) | **GET** /Metadata/TSSites | Obtain identities of tissue source sites in TCGA. |


<a id="barcode"></a>
# **barcode**
> barcode(tcGABarcode, format)

Given a TCGA barcode, return its short letter sample type code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String tcGABarcode = "tcGABarcode_example"; // String | Enter a single TCGA barcode, of any form: e.g. TCGA-GF-A4EO-06 or TCGA-EL-A3D5-01A-22D-A202-08
    String format = "json"; // String | Format of result.
    try {
      apiInstance.barcode(tcGABarcode, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#barcode");
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
| **tcGABarcode** | **String**| Enter a single TCGA barcode, of any form: e.g. TCGA-GF-A4EO-06 or TCGA-EL-A3D5-01A-22D-A202-08 | |
| **format** | **String**| Format of result. | [optional] [default to json] [enum: json, tsv, csv] |

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

<a id="centers"></a>
# **centers**
> centers(format, center)

Obtain identities of TCGA consortium member centers.

By default this function returns a table of all consortium members in TCGA, aka centers; it provides both the HTTP domain and full organizational name of each center.  A subset of this table may be obtained by explicitly specifying one or more domain names.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> center = Arrays.asList(); // List<String> | Narrow search to one or more TCGA centers from the scrollable list.
    try {
      apiInstance.centers(format, center);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#centers");
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
| **center** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA centers from the scrollable list. | [optional] [enum: bcgsc.ca, broad.mit.edu, broadinstitute.org, genome.wustl.edu, hgsc.bcm.edu, hms.harvard.edu, hudsonalpha.org, intgen.org, jhu-usc.edu, jhu.edu, lbl.gov, mdanderson.org, mskcc.org, nationwidechildrens.org, pnl.gov, rubicongenomics.com, sanger.ac.uk, systemsbiology.org, ucsc.edu, unc.edu, vanderbilt.edu] |

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

<a id="clinicalNames"></a>
# **clinicalNames**
> clinicalNames(format)

Retrieve names of all TCGA clinical data elements (CDEs).

Retrieve names of all patient-level clinical data elements (CDES) available in TCGA, unioned across all disease cohorts. A CDE will be listed here only when it has a value other than NA for at least 1 patient case in any disease cohort. For more information on how these CDEs are processed see our &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation\&quot;&gt;pipeline documentation&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String format = "json"; // String | Format of result.
    try {
      apiInstance.clinicalNames(format);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#clinicalNames");
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

<a id="clinicalNamesFH"></a>
# **clinicalNamesFH**
> clinicalNamesFH(format)

Retrieve names of CDEs normalized by Firehose and selected for analyses.

This service returns the names of patient-level clinical data elements (CDEs) that have been normalized by Firehose for use in analyses, unioned across all disease cohorts. For more information on how these CDEs are processed, see our &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation\&quot;&gt;pipeline documentation&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String format = "json"; // String | Format of result.
    try {
      apiInstance.clinicalNamesFH(format);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#clinicalNamesFH");
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

<a id="code"></a>
# **code**
> code(code, format)

Translate from numeric to symbolic TCGA sample codes.

Convert a TCGA numeric sample type code (e.g. 01, 02) to its corresponding symbolic (short letter) code (e.g. TP, TR).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    List<String> code = Arrays.asList(); // List<String> | Narrow search to one or more TCGA sample type codes.
    String format = "json"; // String | Format of result.
    try {
      apiInstance.code(code, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#code");
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
| **code** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA sample type codes. | [enum: 01, 03, 07, 9, 12, 20, 40, 02, 04, 05, 06, 8, 10, 11, 13, 14, 50, 60, 61] |
| **format** | **String**| Format of result. | [optional] [default to json] [enum: json, tsv, csv] |

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

<a id="cohorts"></a>
# **cohorts**
> cohorts(format, cohort)

Translate TCGA cohort abbreviations to full disease names.

By default this function returns a table containing all TCGA cohort abbreviations and their corresponding disease names.  A subset of that table may be obtained by explicitly specifying one or more cohort abbreviations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    try {
      apiInstance.cohorts(format, cohort);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#cohorts");
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

<a id="counts"></a>
# **counts**
> counts(format, date, cohort, sampleType, dataType, totals, sortBy)

Retrieve sample counts.

Returns the aliquot counts for each disease cohort, per sample type and data type.  The sample type designation of \&quot;Tumor\&quot; may be used to aggregate the count of all tumor aliquots into a single number per disease and data type. See the SampleTypes function for a complete description of sample types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<LocalDate> date = Arrays.asList(); // List<LocalDate> | Select one or more date stamps.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<String> sampleType = Arrays.asList(); // List<String> | Narrow search to one or more TCGA sample types from the scrollable list.
    List<String> dataType = Arrays.asList(); // List<String> | Narrow search to one or more TCGA data types from the scrollable list.
    Boolean totals = true; // Boolean | Output an entry providing the totals for each data type.
    String sortBy = "cohort"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.counts(format, date, cohort, sampleType, dataType, totals, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#counts");
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
| **sampleType** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA sample types from the scrollable list. | [optional] [enum: FFPE, NB, NBC, NBM, NT, TAM, TAP, TB, TM, TP, TR, Tumor] |
| **dataType** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA data types from the scrollable list. | [optional] [enum: bcr, clinical, cn, lowp, methylation, mrna, mrnaseq, mir, mirseq, rppa, maf, rawmaf] |
| **totals** | **Boolean**| Output an entry providing the totals for each data type. | [optional] [default to true] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: cohort] |

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

<a id="dates"></a>
# **dates**
> dates(format)

Retrieve dates of all GDAC Firehose stddata &amp; analyses runs that have been ingested into FireBrowse.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String format = "json"; // String | Format of result.
    try {
      apiInstance.dates(format);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#dates");
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

<a id="heartBeat"></a>
# **heartBeat**
> heartBeat(format)

Simple way to discern whether API server is up and running

Returns a message to indicate that API (server) is up and running, or times out if not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String format = "json"; // String | Format of result.
    try {
      apiInstance.heartBeat(format);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#heartBeat");
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

<a id="mAFColNames"></a>
# **mAFColNames**
> mAFColNames(format)

Retrieve names of all columns in the mutation annotation files (MAFs) served by FireBrowse.

Retrieve the names of all columns in the mutation annotation files (MAFs) hosted by FireBrowse.  For more information on the mutation data, and how it is processed by Firehose, please consult the &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation#Documentation-MutationPipelines\&quot;&gt;pipeline documentation&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String format = "json"; // String | Format of result.
    try {
      apiInstance.mAFColNames(format);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#mAFColNames");
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

<a id="patients"></a>
# **patients**
> patients(format, cohort, page, pageSize, sortBy)

Retrieve list of all TCGA patients.

This service returns a list of all TCGA patient barcodes in FireBrowse, optionally filtered by disease cohort.  The barcodes are obtained directy from the clinical data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> cohort = Arrays.asList(); // List<String> | Narrow search to one or more TCGA disease cohorts from the scrollable list.
    List<Integer> page = Arrays.asList(1); // List<Integer> | Which page (slice) of entire results set should be returned. 
    List<Integer> pageSize = Arrays.asList(250); // List<Integer> | Number of records per page of results.  Max is 2000.
    String sortBy = "cohort"; // String | Which column in the results should be used for sorting paginated results?
    try {
      apiInstance.patients(format, cohort, page, pageSize, sortBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#patients");
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
| **page** | [**List&lt;Integer&gt;**](Integer.md)| Which page (slice) of entire results set should be returned.  | [optional] |
| **pageSize** | [**List&lt;Integer&gt;**](Integer.md)| Number of records per page of results.  Max is 2000. | [optional] |
| **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to cohort] [enum: cohort] |

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

<a id="platforms"></a>
# **platforms**
> platforms(format, platform)

Translate TCGA platform codes to full platform names.

By default this function returns a table of all of the technology platforms used to sequence or characterize samples in TCGA--both their short platform codes and full names.  A subset of this table may be obtained by explicitly specifying one or more platform codes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> platform = Arrays.asList(); // List<String> | Narrow search to one or more TCGA data generation platforms from the scrollable list.
    try {
      apiInstance.platforms(format, platform);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#platforms");
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
| **platform** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TCGA data generation platforms from the scrollable list. | [optional] [enum: 454, ABI, AgilentG4502A_07, AgilentG4502A_07_1, AgilentG4502A_07_2, AgilentG4502A_07_3, bio, biotab, CGH-1x1M_G4447A, diagnostic_images, fh_analyses, fh_reports, fh_stddata, Genome_Wide_SNP_6, GenomeWideSNP_5, H-miRNA_8x15K, H-miRNA_8x15Kv2, H-miRNA_EarlyAccess, H-miRNA_G4470A, HG-CGH-244A, HG-CGH-415K_G4124A, HG-U133_Plus_2, HG-U133A_2, HT_HG-U133A, HuEx-1_0-st-v2, Human1MDuo, HumanHap550, HumanMethylation27, HumanMethylation450, IlluminaDNAMethylation_OMA002_CPI, IlluminaDNAMethylation_OMA003_CPI, IlluminaGA_DNASeq, IlluminaGA_DNASeq_automated, IlluminaGA_DNASeq_Cont, IlluminaGA_DNASeq_Cont_automated, IlluminaGA_DNASeq_Cont_curated, IlluminaGA_DNASeq_curated, IlluminaGA_miRNASeq, IlluminaGA_mRNA_DGE, IlluminaGA_RNASeq, IlluminaGA_RNASeqV2, IlluminaGG, IlluminaHiSeq_DNASeq, IlluminaHiSeq_DNASeq_automated, IlluminaHiSeq_DNASeq_Cont, IlluminaHiSeq_DNASeq_Cont_automated, IlluminaHiSeq_DNASeq_Cont_curated, IlluminaHiSeq_DNASeq_curated, IlluminaHiSeq_DNASeqC, IlluminaHiSeq_miRNASeq, IlluminaHiSeq_mRNA_DGE, IlluminaHiSeq_RNASeq, IlluminaHiSeq_RNASeqV2, IlluminaHiSeq_TotalRNASeqV2, IlluminaHiSeq_WGBS, Mapping250K_Nsp, Mapping250K_Sty, MDA_RPPA_Core, microsat_i, minbio, minbiotab, Mixed_DNASeq, Mixed_DNASeq_automated, Mixed_DNASeq_Cont, Mixed_DNASeq_Cont_automated, Mixed_DNASeq_Cont_curated, Mixed_DNASeq_curated, pathology_reports, SOLiD_DNASeq, SOLiD_DNASeq_automated, SOLiD_DNASeq_Cont, SOLiD_DNASeq_Cont_automated, SOLiD_DNASeq_Cont_curated, SOLiD_DNASeq_curated, tissue_images, WHG-1x44K_G4112A, WHG-4x44K_G4112F, WHG-CGH_4x44B] |

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

<a id="sampleTypes"></a>
# **sampleTypes**
> sampleTypes(format)

Return all TCGA sample type codes, both numeric and symbolic.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String format = "json"; // String | Format of result.
    try {
      apiInstance.sampleTypes(format);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#sampleTypes");
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

<a id="shortLetterCode"></a>
# **shortLetterCode**
> shortLetterCode(shortLetterCode, format)

Translate from symbolic to numeric TCGA sample codes.

Convert a TCGA sample type code in symbolic form (or &#39;short letter code&#39; like TP, TR) to its corresponding numeric form (e.g. 01, 02).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    List<String> shortLetterCode = Arrays.asList(); // List<String> | TCGA sample type short letter code(s) (e.g. TP, NB, etc.). 
    String format = "json"; // String | Format of result.
    try {
      apiInstance.shortLetterCode(shortLetterCode, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#shortLetterCode");
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
| **shortLetterCode** | [**List&lt;String&gt;**](String.md)| TCGA sample type short letter code(s) (e.g. TP, NB, etc.).  | [enum: TP, TB, TAM, TBM, NBC, CELLC, TRB, TR, TRBM, TAP, TM, THOC, NB, NT, NEBV, NBM, CELL, XP, XCL] |
| **format** | **String**| Format of result. | [optional] [default to json] [enum: json, tsv, csv] |

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

<a id="tSSites"></a>
# **tSSites**
> tSSites(format, tssCode)

Obtain identities of tissue source sites in TCGA.

By default this function returns a table of all sites which contributed source tissue to TCGA, aka TSS&#39;s. A subset of this table may be obtained by explicitly specifying one or more sites.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://firebrowse.org/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String format = "json"; // String | Format of result.
    List<String> tssCode = Arrays.asList(); // List<String> | Narrow search to one or more TSS codes
    try {
      apiInstance.tSSites(format, tssCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#tSSites");
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
| **tssCode** | [**List&lt;String&gt;**](String.md)| Narrow search to one or more TSS codes | [optional] [enum: 01, 02, 04, 05, 06, 07, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1Z, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 2A, 2E, 2F, 2G, 2H, 2J, 2K, 2L, 2M, 2N, 2P, 2V, 2W, 2X, 2Y, 2Z, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 3A, 3B, 3C, 3E, 3G, 3H, 3J, 3K, 3L, 3M, 3N, 3P, 3Q, 3R, 3S, 3T, 3U, 3W, 3X, 3Z, 41, 42, 43, 44, 46, 49, 4A, 4B, 4C, 4D, 4E, 4G, 4H, 4J, 4K, 4L, 4N, 4P, 4Q, 4R, 4S, 4T, 4V, 4W, 4X, 4Y, 4Z, 50, 51, 52, 53, 55, 56, 57, 58, 59, 5A, 5B, 5C, 5D, 5F, 5G, 5H, 5J, 5K, 5L, 5M, 5N, 5P, 5Q, 5R, 5S, 5T, 5U, 5V, 5W, 5X, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 6A, 6D, 6G, 6H, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 85, 86, 87, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, A1, A2, A3, A4, A5, A6, A7, A8, AA, AB, AC, AD, AF, AG, AH, AJ, AK, AL, AM, AN, AO, AP, AQ, AR, AS, AT, AU, AV, AW, AX, AY, AZ, B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, BA, BB, BC, BD, BF, BG, BH, BI, BJ, BK, BL, BM, BP, BQ, BR, BS, BT, BW, C4, C5, C8, C9, CA, CB, CC, CD, CE, CF, CG, CH, CI, CJ, CK, CL, CM, CN, CQ, CR, CS, CU, CV, CW, CX, CZ, D1, D3, D5, D6, D7, D8, D9, DA, DB, DC, DD, DE, DF, DG, DH, DI, DJ, DK, DM, DO, DQ, DR, DS, DT, DU, DV, DW, DX, DY, DZ, E1, E2, E3, E5, E6, E7, E8, E9, EA, EB, EC, ED, EE, EF, EI, EJ, EK, EL, EM, EO, EP, EQ, ER, ES, ET, EU, EV, EW, EX, EY, EZ, F1, F2, F4, F5, F6, F7, F9, FA, FB, FC, FD, FE, FF, FG, FH, FI, FJ, FK, FL, FM, FN, FP, FQ, FR, FS, FT, FU, FV, FW, FX, FY, FZ, G2, G3, G4, G5, G6, G7, G8, G9, GC, GD, GE, GF, GG, GH, GI, GJ, GK, GL, GM, GN, GP, GR, GS, GU, GV, GZ, H1, H2, H3, H4, H5, H6, H7, H8, H9, HA, HB, HC, HD, HE, HF, HG, HH, HI, HJ, HK, HL, HM, HN, HP, HQ, HR, HS, HT, HU, HV, HW, HZ, IA, IB, IC, IE, IF, IG, IH, IJ, IK, IM, IN, IP, IQ, IR, IS, IW, IZ, J1, J2, J4, J7, J8, J9, JA, JL, JU, JV, JW, JX, JY, JZ, K1, K4, K6, K7, K8, KA, KB, KC, KD, KE, KF, KG, KH, KJ, KK, KL, KM, KN, KO, KP, KQ, KR, KS, KT, KU, KV, KZ, L1, L3, L4, L5, L6, L7, L8, L9, LA, LB, LC, LD, LG, LH, LI, LK, LL, LN, LP, LQ, LS, LT, M7, M8, M9, MA, MB, ME, MF, MG, MH, MI, MJ, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, N1, N5, N6, N7, N8, N9, NA, NB, NC, ND, NF, NG, NH, NI, NJ, NK, NM, NP, NQ, NS, O1, O2, O8, O9, OC, OD, OE, OJ, OK, OL, OR, OU, OW, OX, OY, P3, P4, P5, P6, P7, P8, P9, PA, PB, PC, PD, PE, PG, PH, PJ, PK, PL, PN, PQ, PR, PT, PZ, Q1, Q2, Q3, Q4, Q9, QA, QB, QC, QD, QF, QG, QH, QJ, QK, QL, QM, QN, QQ, QR, QS, QT, QU, QV, QW, R1, R2, R3, R5, R6, R7, R8, R9, RA, RB, RC, RD, RE, RG, RH, RL, RM, RN, RP, RQ, RR, RS, RT, RU, RV, RW, RX, RY, RZ, S2, S3, S4, S5, S6, S7, S8, S9, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SN, SO, SP, SQ, SR, SS, ST, SU, SW, SX, SY, T1, T2, T3, T6, T7, T9, TE, TG, TK, TL, TM, TN, TP, TQ, TR, TS, TT, TV, UB, UC, UD, UE, UF, UJ, UL, UN, UP, UR, US, UT, UU, UV, UW, UY, UZ, V1, V2, V3, V4, V5, V6, V7, V8, V9, VA, VB, VD, VF, VG, VK, VL, VM, VN, VP, VQ, VR, VS, VT, VV, VW, VX, VZ, W2, W3, W4, W5, W6, W7, W8, W9, WA, WB, WC, WD, WE, WF, WG, WH, WJ, WK, WL, WM, WN, WP, WQ, WR, WS, WT, WU, WW, WX, WY, WZ, X2, X3, X4, X5, X6, X7, X8, X9, XA, XB, XC, XD, XE, XF, XG, XH, XJ, XK, XM, XN, XP, XQ, XR, XS, XT, XU, XV, XX, XY, Y3, Y5, Y6, Y8, YA, YB, YC, YD, YF, YG, YH, YJ, YL, YN, YR, YS, YT, YU, YV, YW, YX, YY, YZ, Z2, Z3, Z4, Z5, Z6, Z7, Z8, ZA, ZB, ZC, ZD, ZE, ZF, ZG, ZH, ZJ, ZK, ZL, ZM, ZN, ZP, ZQ, ZR, ZS, ZT, ZU, ZW, ZX] |

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

