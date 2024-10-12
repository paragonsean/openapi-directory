# RatStrainApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllStrainsUsingGET**](RatStrainApi.md#getAllStrainsUsingGET) | **GET** /strains/all | Return all active strains in RGD |
| [**getStrainByRgdIdUsingGET**](RatStrainApi.md#getStrainByRgdIdUsingGET) | **GET** /strains/{rgdId} | Return a strain by RGD ID |
| [**getStrainsByPositionUsingGET**](RatStrainApi.md#getStrainsByPositionUsingGET) | **GET** /strains/{chr}/{start}/{stop}/{mapKey} | Return all active strains by position |


<a id="getAllStrainsUsingGET"></a>
# **getAllStrainsUsingGET**
> List&lt;Strain&gt; getAllStrainsUsingGET()

Return all active strains in RGD

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatStrainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    RatStrainApi apiInstance = new RatStrainApi(defaultClient);
    try {
      List<Strain> result = apiInstance.getAllStrainsUsingGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatStrainApi#getAllStrainsUsingGET");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Strain&gt;**](Strain.md)

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

<a id="getStrainByRgdIdUsingGET"></a>
# **getStrainByRgdIdUsingGET**
> Strain getStrainByRgdIdUsingGET(rgdId)

Return a strain by RGD ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatStrainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    RatStrainApi apiInstance = new RatStrainApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID of the strain
    try {
      Strain result = apiInstance.getStrainByRgdIdUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatStrainApi#getStrainByRgdIdUsingGET");
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
| **rgdId** | **Integer**| RGD ID of the strain | |

### Return type

[**Strain**](Strain.md)

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

<a id="getStrainsByPositionUsingGET"></a>
# **getStrainsByPositionUsingGET**
> List&lt;Strain&gt; getStrainsByPositionUsingGET(chr, start, stop, mapKey)

Return all active strains by position

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatStrainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    RatStrainApi apiInstance = new RatStrainApi(defaultClient);
    String chr = "chr_example"; // String | Chromosome
    Long start = 56L; // Long | Start Position
    Long stop = 56L; // Long | Stop Position
    Integer mapKey = 56; // Integer | RGD Map Key (available through lookup service)
    try {
      List<Strain> result = apiInstance.getStrainsByPositionUsingGET(chr, start, stop, mapKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatStrainApi#getStrainsByPositionUsingGET");
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
| **chr** | **String**| Chromosome | |
| **start** | **Long**| Start Position | |
| **stop** | **Long**| Stop Position | |
| **mapKey** | **Integer**| RGD Map Key (available through lookup service) | |

### Return type

[**List&lt;Strain&gt;**](Strain.md)

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

