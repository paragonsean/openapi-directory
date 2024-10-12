# QuantitativePhenotypeApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getChartInfoUsingGET**](QuantitativePhenotypeApi.md#getChartInfoUsingGET) | **GET** /phenotype/phenominer/chart/{speciesTypeKey}/{refRgdId}/{termString} | Return a list of quantitative phenotypes values based on a combination of Clinical Measurement, Experimental Condition, Rat Strain, and/or Measurement Method ontology terms.  Results will be all records that match all terms submitted.  Ontology ids should be submitted as a comma delimited list (ex. RS:0000029,CMO:0000155,CMO:0000139).  Species type is an integer value (3&#x3D;rat, 4&#x3D;chinchilla).  Reference RGD ID for a study works like a filter. |
| [**getChartInfoUsingGET1**](QuantitativePhenotypeApi.md#getChartInfoUsingGET1) | **GET** /phenotype/phenominer/chart/{speciesTypeKey}/{termString} | Return a list of quantitative phenotypes values based on a combination of Clinical Measurement, Experimental Condition, Rat Strain, and/or Measurement Method ontology terms.  Results will be all records that match all terms submitted.  Ontology ids should be submitted as a comma delimited list (ex. RS:0000029,CMO:0000155,CMO:0000139).  Species type is an integer value (3&#x3D;rat, 4&#x3D;chinchilla) |


<a id="getChartInfoUsingGET"></a>
# **getChartInfoUsingGET**
> Map&lt;String, Object&gt; getChartInfoUsingGET(speciesTypeKey, refRgdId, termString)

Return a list of quantitative phenotypes values based on a combination of Clinical Measurement, Experimental Condition, Rat Strain, and/or Measurement Method ontology terms.  Results will be all records that match all terms submitted.  Ontology ids should be submitted as a comma delimited list (ex. RS:0000029,CMO:0000155,CMO:0000139).  Species type is an integer value (3&#x3D;rat, 4&#x3D;chinchilla).  Reference RGD ID for a study works like a filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuantitativePhenotypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    QuantitativePhenotypeApi apiInstance = new QuantitativePhenotypeApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | Species Type Key - 3=rat 4=chinchilla 
    Integer refRgdId = 56; // Integer | Reference RGD ID for a study
    String termString = "termString_example"; // String | List of term accession IDs
    try {
      Map<String, Object> result = apiInstance.getChartInfoUsingGET(speciesTypeKey, refRgdId, termString);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuantitativePhenotypeApi#getChartInfoUsingGET");
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
| **speciesTypeKey** | **Integer**| Species Type Key - 3&#x3D;rat 4&#x3D;chinchilla  | |
| **refRgdId** | **Integer**| Reference RGD ID for a study | |
| **termString** | **String**| List of term accession IDs | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getChartInfoUsingGET1"></a>
# **getChartInfoUsingGET1**
> Map&lt;String, Object&gt; getChartInfoUsingGET1(speciesTypeKey, termString)

Return a list of quantitative phenotypes values based on a combination of Clinical Measurement, Experimental Condition, Rat Strain, and/or Measurement Method ontology terms.  Results will be all records that match all terms submitted.  Ontology ids should be submitted as a comma delimited list (ex. RS:0000029,CMO:0000155,CMO:0000139).  Species type is an integer value (3&#x3D;rat, 4&#x3D;chinchilla)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuantitativePhenotypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    QuantitativePhenotypeApi apiInstance = new QuantitativePhenotypeApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | Species Type Key - 3=rat 4=chinchilla 
    String termString = "termString_example"; // String | List of term accession IDs
    try {
      Map<String, Object> result = apiInstance.getChartInfoUsingGET1(speciesTypeKey, termString);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuantitativePhenotypeApi#getChartInfoUsingGET1");
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
| **speciesTypeKey** | **Integer**| Species Type Key - 3&#x3D;rat 4&#x3D;chinchilla  | |
| **termString** | **String**| List of term accession IDs | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

