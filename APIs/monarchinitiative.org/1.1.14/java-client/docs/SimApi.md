# SimApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAnnotationScore**](SimApi.md#getAnnotationScore) | **GET** /sim/score | Get annotation score |
| [**getSimCompare**](SimApi.md#getSimCompare) | **GET** /sim/compare | Compare a reference profile vs one profiles |
| [**getSimSearch**](SimApi.md#getSimSearch) | **GET** /sim/search | Search for phenotypically similar diseases or model genes |
| [**postAnnotationScore**](SimApi.md#postAnnotationScore) | **POST** /sim/score | Get annotation score |
| [**postSimCompare**](SimApi.md#postSimCompare) | **POST** /sim/compare | Compare a reference profile vs one or more profiles |


<a id="getAnnotationScore"></a>
# **getAnnotationScore**
> SufficiencyOutput getAnnotationScore(id, absentId)

Get annotation score

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    SimApi apiInstance = new SimApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Phenotype identifier (eg HP:0004935)
    List<String> absentId = Arrays.asList(); // List<String> | absent phenotype (eg HP:0002828)
    try {
      SufficiencyOutput result = apiInstance.getAnnotationScore(id, absentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimApi#getAnnotationScore");
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
| **id** | [**List&lt;String&gt;**](String.md)| Phenotype identifier (eg HP:0004935) | [optional] |
| **absentId** | [**List&lt;String&gt;**](String.md)| absent phenotype (eg HP:0002828) | [optional] |

### Return type

[**SufficiencyOutput**](SufficiencyOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getSimCompare"></a>
# **getSimCompare**
> SimResult getSimCompare(isFeatureSet, metric, refId, queryId)

Compare a reference profile vs one profiles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    SimApi apiInstance = new SimApi(defaultClient);
    Boolean isFeatureSet = true; // Boolean | set to true if *all* input ids are phenotypic features, else set to false
    String metric = "phenodigm"; // String | Metric for computing similarity
    List<String> refId = Arrays.asList(); // List<String> | A phenotype or identifier that is composed of phenotypes (eg disease, gene)
    List<String> queryId = Arrays.asList(); // List<String> | A phenotype or identifier that is composed of phenotypes (eg disease, gene)
    try {
      SimResult result = apiInstance.getSimCompare(isFeatureSet, metric, refId, queryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimApi#getSimCompare");
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
| **isFeatureSet** | **Boolean**| set to true if *all* input ids are phenotypic features, else set to false | [optional] [default to true] |
| **metric** | **String**| Metric for computing similarity | [optional] [default to phenodigm] [enum: phenodigm, jaccard, simGIC, resnik, symmetric_resnik] |
| **refId** | [**List&lt;String&gt;**](String.md)| A phenotype or identifier that is composed of phenotypes (eg disease, gene) | [optional] |
| **queryId** | [**List&lt;String&gt;**](String.md)| A phenotype or identifier that is composed of phenotypes (eg disease, gene) | [optional] |

### Return type

[**SimResult**](SimResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getSimSearch"></a>
# **getSimSearch**
> SimResult getSimSearch(isFeatureSet, metric, id, limit, taxon)

Search for phenotypically similar diseases or model genes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    SimApi apiInstance = new SimApi(defaultClient);
    Boolean isFeatureSet = true; // Boolean | set to true if *all* input ids are phenotypic features, else set to false
    String metric = "phenodigm"; // String | Metric for computing similarity
    List<String> id = Arrays.asList(); // List<String> | A phenotype or identifier that is composed of phenotypes (eg disease, gene)
    Integer limit = 20; // Integer | number of rows, max 500
    String taxon = "taxon_example"; // String | ncbi taxon id
    try {
      SimResult result = apiInstance.getSimSearch(isFeatureSet, metric, id, limit, taxon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimApi#getSimSearch");
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
| **isFeatureSet** | **Boolean**| set to true if *all* input ids are phenotypic features, else set to false | [optional] [default to true] |
| **metric** | **String**| Metric for computing similarity | [optional] [default to phenodigm] [enum: phenodigm, jaccard, simGIC, resnik, symmetric_resnik] |
| **id** | [**List&lt;String&gt;**](String.md)| A phenotype or identifier that is composed of phenotypes (eg disease, gene) | [optional] |
| **limit** | **Integer**| number of rows, max 500 | [optional] [default to 20] |
| **taxon** | **String**| ncbi taxon id | [optional] |

### Return type

[**SimResult**](SimResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="postAnnotationScore"></a>
# **postAnnotationScore**
> SufficiencyOutput postAnnotationScore(sufficiencyPostInput)

Get annotation score

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    SimApi apiInstance = new SimApi(defaultClient);
    SufficiencyPostInput sufficiencyPostInput = new SufficiencyPostInput(); // SufficiencyPostInput | 
    try {
      SufficiencyOutput result = apiInstance.postAnnotationScore(sufficiencyPostInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimApi#postAnnotationScore");
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
| **sufficiencyPostInput** | [**SufficiencyPostInput**](SufficiencyPostInput.md)|  | |

### Return type

[**SufficiencyOutput**](SufficiencyOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="postSimCompare"></a>
# **postSimCompare**
> SimResult postSimCompare(compareInput)

Compare a reference profile vs one or more profiles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    SimApi apiInstance = new SimApi(defaultClient);
    CompareInput compareInput = new CompareInput(); // CompareInput | 
    try {
      SimResult result = apiInstance.postSimCompare(compareInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimApi#postSimCompare");
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
| **compareInput** | [**CompareInput**](CompareInput.md)|  | |

### Return type

[**SimResult**](SimResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

