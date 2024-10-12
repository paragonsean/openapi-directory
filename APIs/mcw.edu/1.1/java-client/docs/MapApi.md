# MapApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getChromosomeByAssemblyUsingGET_0**](MapApi.md#getChromosomeByAssemblyUsingGET_0) | **GET** /maps/chr/{chromosome}/{mapKey} | Return a list of chromosomes |
| [**getChromosomesByAssemblyUsingGET_0**](MapApi.md#getChromosomesByAssemblyUsingGET_0) | **GET** /maps/chr/{mapKey} | Return a list of chromosomes |
| [**getMapsBySpeciesUsingGET**](MapApi.md#getMapsBySpeciesUsingGET) | **GET** /maps/{speciesTypeKey} | Return a list of assemblies |


<a id="getChromosomeByAssemblyUsingGET_0"></a>
# **getChromosomeByAssemblyUsingGET_0**
> Chromosome getChromosomeByAssemblyUsingGET_0(chromosome, mapKey)

Return a list of chromosomes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MapApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    MapApi apiInstance = new MapApi(defaultClient);
    String chromosome = "chromosome_example"; // String | chromosome
    Integer mapKey = 56; // Integer | mapKey
    try {
      Chromosome result = apiInstance.getChromosomeByAssemblyUsingGET_0(chromosome, mapKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MapApi#getChromosomeByAssemblyUsingGET_0");
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

<a id="getChromosomesByAssemblyUsingGET_0"></a>
# **getChromosomesByAssemblyUsingGET_0**
> List&lt;String&gt; getChromosomesByAssemblyUsingGET_0(mapKey)

Return a list of chromosomes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MapApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    MapApi apiInstance = new MapApi(defaultClient);
    Integer mapKey = 56; // Integer | mapKey
    try {
      List<String> result = apiInstance.getChromosomesByAssemblyUsingGET_0(mapKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MapApi#getChromosomesByAssemblyUsingGET_0");
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

<a id="getMapsBySpeciesUsingGET"></a>
# **getMapsBySpeciesUsingGET**
> List&lt;Map&gt; getMapsBySpeciesUsingGET(speciesTypeKey)

Return a list of assemblies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MapApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    MapApi apiInstance = new MapApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | species Key
    try {
      List<Map> result = apiInstance.getMapsBySpeciesUsingGET(speciesTypeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MapApi#getMapsBySpeciesUsingGET");
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
| **speciesTypeKey** | **Integer**| species Key | |

### Return type

[**List&lt;Map&gt;**](Map.md)

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

