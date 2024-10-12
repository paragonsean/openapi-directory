# BioentitysetSlimmerApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEntitySetAnatomySlimmer**](BioentitysetSlimmerApi.md#getEntitySetAnatomySlimmer) | **GET** /bioentityset/slimmer/anatomy | For a given gene(s), summarize its annotations over a defined set of slim |
| [**getEntitySetFunctionSlimmer**](BioentitysetSlimmerApi.md#getEntitySetFunctionSlimmer) | **GET** /bioentityset/slimmer/function | For a given gene(s), summarize its annotations over a defined set of slim |
| [**getEntitySetPhenotypeSlimmer**](BioentitysetSlimmerApi.md#getEntitySetPhenotypeSlimmer) | **GET** /bioentityset/slimmer/phenotype | For a given gene(s), summarize its annotations over a defined set of slim |


<a id="getEntitySetAnatomySlimmer"></a>
# **getEntitySetAnatomySlimmer**
> getEntitySetAnatomySlimmer(subject, slim, excludeAutomaticAssertions, rows, start)

For a given gene(s), summarize its annotations over a defined set of slim

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentitysetSlimmerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentitysetSlimmerApi apiInstance = new BioentitysetSlimmerApi(defaultClient);
    List<String> subject = Arrays.asList(); // List<String> | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO)
    Boolean excludeAutomaticAssertions = false; // Boolean | If set, excludes associations that involve IEAs (ECO:0000501)
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    try {
      apiInstance.getEntitySetAnatomySlimmer(subject, slim, excludeAutomaticAssertions, rows, start);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentitysetSlimmerApi#getEntitySetAnatomySlimmer");
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
| **subject** | [**List&lt;String&gt;**](String.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) | |
| **excludeAutomaticAssertions** | **Boolean**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |

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
| **200** | Success |  -  |

<a id="getEntitySetFunctionSlimmer"></a>
# **getEntitySetFunctionSlimmer**
> getEntitySetFunctionSlimmer(subject, slim, relationshipType, excludeAutomaticAssertions, rows, start)

For a given gene(s), summarize its annotations over a defined set of slim

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentitysetSlimmerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentitysetSlimmerApi apiInstance = new BioentitysetSlimmerApi(defaultClient);
    List<String> subject = Arrays.asList(); // List<String> | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO)
    String relationshipType = "involved_in"; // String | relationship type ('involved_in' or 'acts_upstream_of_or_within')
    Boolean excludeAutomaticAssertions = false; // Boolean | If set, excludes associations that involve IEAs (ECO:0000501)
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    try {
      apiInstance.getEntitySetFunctionSlimmer(subject, slim, relationshipType, excludeAutomaticAssertions, rows, start);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentitysetSlimmerApi#getEntitySetFunctionSlimmer");
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
| **subject** | [**List&lt;String&gt;**](String.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) | |
| **relationshipType** | **String**| relationship type (&#39;involved_in&#39; or &#39;acts_upstream_of_or_within&#39;) | [optional] [default to acts_upstream_of_or_within] [enum: involved_in, acts_upstream_of_or_within] |
| **excludeAutomaticAssertions** | **Boolean**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |

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
| **200** | Success |  -  |

<a id="getEntitySetPhenotypeSlimmer"></a>
# **getEntitySetPhenotypeSlimmer**
> getEntitySetPhenotypeSlimmer(subject, slim, excludeAutomaticAssertions, rows, start)

For a given gene(s), summarize its annotations over a defined set of slim

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentitysetSlimmerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentitysetSlimmerApi apiInstance = new BioentitysetSlimmerApi(defaultClient);
    List<String> subject = Arrays.asList(); // List<String> | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO)
    Boolean excludeAutomaticAssertions = false; // Boolean | If set, excludes associations that involve IEAs (ECO:0000501)
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    try {
      apiInstance.getEntitySetPhenotypeSlimmer(subject, slim, excludeAutomaticAssertions, rows, start);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentitysetSlimmerApi#getEntitySetPhenotypeSlimmer");
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
| **subject** | [**List&lt;String&gt;**](String.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) | |
| **excludeAutomaticAssertions** | **Boolean**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |

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
| **200** | Success |  -  |

