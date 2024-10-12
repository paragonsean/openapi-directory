# SharedLineEndSizesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedLineendsizesGet**](SharedLineEndSizesApi.md#sharedLineendsizesGet) | **GET** /Shared/LineEndSizes | LineEndSizes: List All Possible Types |
| [**sharedLineendsizesGetId**](SharedLineEndSizesApi.md#sharedLineendsizesGetId) | **GET** /Shared/LineEndSizes/{id} | LineEndSizes: Get by Id |
| [**sharedLineendsizesTypeidGetTypeId**](SharedLineEndSizesApi.md#sharedLineendsizesTypeidGetTypeId) | **GET** /Shared/LineEndSizes/TypeId/{type_id} | LineEndSizes: Get By Type Id |


<a id="sharedLineendsizesGet"></a>
# **sharedLineendsizesGet**
> List&lt;SharedLineEndSizes&gt; sharedLineendsizesGet()

LineEndSizes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the LineEndSizes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedLineEndSizesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedLineEndSizesApi apiInstance = new SharedLineEndSizesApi(defaultClient);
    try {
      List<SharedLineEndSizes> result = apiInstance.sharedLineendsizesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedLineEndSizesApi#sharedLineendsizesGet");
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

[**List&lt;SharedLineEndSizes&gt;**](SharedLineEndSizes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="sharedLineendsizesGetId"></a>
# **sharedLineendsizesGetId**
> SharedLineEndSizes sharedLineendsizesGetId(id)

LineEndSizes: Get by Id

Get by Id: Use this method to retrieve a LineEndSizes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedLineEndSizesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedLineEndSizesApi apiInstance = new SharedLineEndSizesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedLineEndSizes result = apiInstance.sharedLineendsizesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedLineEndSizesApi#sharedLineendsizesGetId");
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
| **id** | **UUID**|  | |

### Return type

[**SharedLineEndSizes**](SharedLineEndSizes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="sharedLineendsizesTypeidGetTypeId"></a>
# **sharedLineendsizesTypeidGetTypeId**
> SharedLineEndSizes sharedLineendsizesTypeidGetTypeId(typeId)

LineEndSizes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedLineEndSizesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedLineEndSizesApi apiInstance = new SharedLineEndSizesApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      SharedLineEndSizes result = apiInstance.sharedLineendsizesTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedLineEndSizesApi#sharedLineendsizesTypeidGetTypeId");
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
| **typeId** | **Integer**|  | |

### Return type

[**SharedLineEndSizes**](SharedLineEndSizes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

