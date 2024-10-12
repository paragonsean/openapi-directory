# ChromosomeApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getChromosomeByAssemblyUsingGET**](ChromosomeApi.md#getChromosomeByAssemblyUsingGET) | **GET** /maps/chr/{chromosome}/{mapKey} | Return a list of chromosomes |
| [**getChromosomesByAssemblyUsingGET**](ChromosomeApi.md#getChromosomesByAssemblyUsingGET) | **GET** /maps/chr/{mapKey} | Return a list of chromosomes |


<a id="getChromosomeByAssemblyUsingGET"></a>
# **getChromosomeByAssemblyUsingGET**
> Chromosome getChromosomeByAssemblyUsingGET(chromosome, mapKey)

Return a list of chromosomes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChromosomeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    ChromosomeApi apiInstance = new ChromosomeApi(defaultClient);
    String chromosome = "chromosome_example"; // String | chromosome
    Integer mapKey = 56; // Integer | mapKey
    try {
      Chromosome result = apiInstance.getChromosomeByAssemblyUsingGET(chromosome, mapKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChromosomeApi#getChromosomeByAssemblyUsingGET");
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
| **chromosome** | **String**| chromosome | |
| **mapKey** | **Integer**| mapKey | |

### Return type

[**Chromosome**](Chromosome.md)

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

<a id="getChromosomesByAssemblyUsingGET"></a>
# **getChromosomesByAssemblyUsingGET**
> List&lt;String&gt; getChromosomesByAssemblyUsingGET(mapKey)

Return a list of chromosomes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChromosomeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    ChromosomeApi apiInstance = new ChromosomeApi(defaultClient);
    Integer mapKey = 56; // Integer | mapKey
    try {
      List<String> result = apiInstance.getChromosomesByAssemblyUsingGET(mapKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChromosomeApi#getChromosomesByAssemblyUsingGET");
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
| **mapKey** | **Integer**| mapKey | |

### Return type

**List&lt;String&gt;**

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

