# QtlApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMappedQTLByPositionUsingGET**](QtlApi.md#getMappedQTLByPositionUsingGET) | **GET** /qtls/mapped/{chr}/{start}/{stop}/{mapKey} | Returns a list QTL for given position and assembly map |
| [**getQTLByRgdIdUsingGET**](QtlApi.md#getQTLByRgdIdUsingGET) | **GET** /qtls/{rgdId} | Return a QTL for provided RGD ID |
| [**getQtlListByPositionUsingGET**](QtlApi.md#getQtlListByPositionUsingGET) | **GET** /qtls/{chr}/{start}/{stop}/{mapKey} | Returns a list QTL for given position and assembly map |


<a id="getMappedQTLByPositionUsingGET"></a>
# **getMappedQTLByPositionUsingGET**
> List&lt;MappedQTL&gt; getMappedQTLByPositionUsingGET(chr, start, stop, mapKey)

Returns a list QTL for given position and assembly map

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QtlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    QtlApi apiInstance = new QtlApi(defaultClient);
    String chr = "chr_example"; // String | Chromosome
    Long start = 56L; // Long | Start Position
    Long stop = 56L; // Long | Stop Position
    Integer mapKey = 56; // Integer | A list of assembly map keys can be found using the lookup service
    try {
      List<MappedQTL> result = apiInstance.getMappedQTLByPositionUsingGET(chr, start, stop, mapKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QtlApi#getMappedQTLByPositionUsingGET");
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
| **mapKey** | **Integer**| A list of assembly map keys can be found using the lookup service | |

### Return type

[**List&lt;MappedQTL&gt;**](MappedQTL.md)

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

<a id="getQTLByRgdIdUsingGET"></a>
# **getQTLByRgdIdUsingGET**
> QTL getQTLByRgdIdUsingGET(rgdId)

Return a QTL for provided RGD ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QtlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    QtlApi apiInstance = new QtlApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      QTL result = apiInstance.getQTLByRgdIdUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QtlApi#getQTLByRgdIdUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

### Return type

[**QTL**](QTL.md)

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

<a id="getQtlListByPositionUsingGET"></a>
# **getQtlListByPositionUsingGET**
> List&lt;QTL&gt; getQtlListByPositionUsingGET(chr, start, stop, mapKey)

Returns a list QTL for given position and assembly map

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QtlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    QtlApi apiInstance = new QtlApi(defaultClient);
    String chr = "chr_example"; // String | Chromosome
    Long start = 56L; // Long | Start Position
    Long stop = 56L; // Long | Stop Position
    Integer mapKey = 56; // Integer | A list of assembly map keys can be found using the lookup service
    try {
      List<QTL> result = apiInstance.getQtlListByPositionUsingGET(chr, start, stop, mapKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QtlApi#getQtlListByPositionUsingGET");
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
| **mapKey** | **Integer**| A list of assembly map keys can be found using the lookup service | |

### Return type

[**List&lt;QTL&gt;**](QTL.md)

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

