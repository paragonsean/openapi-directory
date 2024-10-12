# DefaultApi

All URIs are relative to *http://xkcd.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**comicIdInfo0JsonGet**](DefaultApi.md#comicIdInfo0JsonGet) | **GET** /{comicId}/info.0.json |  |
| [**info0JsonGet**](DefaultApi.md#info0JsonGet) | **GET** /info.0.json |  |


<a id="comicIdInfo0JsonGet"></a>
# **comicIdInfo0JsonGet**
> Comic comicIdInfo0JsonGet(comicId)



Fetch comics and metadata  by comic id. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://xkcd.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BigDecimal comicId = new BigDecimal(78); // BigDecimal | 
    try {
      Comic result = apiInstance.comicIdInfo0JsonGet(comicId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#comicIdInfo0JsonGet");
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
| **comicId** | **BigDecimal**|  | |

### Return type

[**Comic**](Comic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="info0JsonGet"></a>
# **info0JsonGet**
> Comic info0JsonGet()



Fetch current comic and metadata. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://xkcd.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Comic result = apiInstance.info0JsonGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#info0JsonGet");
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

[**Comic**](Comic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

