# GiftWrappingsIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftWrappingWrappingRepositoryV1DeleteByIdDelete**](GiftWrappingsIdApi.md#giftWrappingWrappingRepositoryV1DeleteByIdDelete) | **DELETE** /V1/gift-wrappings/{id} | gift-wrappings/{id} |
| [**giftWrappingWrappingRepositoryV1GetGet**](GiftWrappingsIdApi.md#giftWrappingWrappingRepositoryV1GetGet) | **GET** /V1/gift-wrappings/{id} | gift-wrappings/{id} |


<a id="giftWrappingWrappingRepositoryV1DeleteByIdDelete"></a>
# **giftWrappingWrappingRepositoryV1DeleteByIdDelete**
> Boolean giftWrappingWrappingRepositoryV1DeleteByIdDelete(id)

gift-wrappings/{id}

Delete gift wrapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftWrappingsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GiftWrappingsIdApi apiInstance = new GiftWrappingsIdApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      Boolean result = apiInstance.giftWrappingWrappingRepositoryV1DeleteByIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftWrappingsIdApi#giftWrappingWrappingRepositoryV1DeleteByIdDelete");
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
| **id** | **Integer**|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="giftWrappingWrappingRepositoryV1GetGet"></a>
# **giftWrappingWrappingRepositoryV1GetGet**
> GiftWrappingDataWrappingInterface giftWrappingWrappingRepositoryV1GetGet(id, storeId)

gift-wrappings/{id}

Return data object for specified wrapping ID and store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftWrappingsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GiftWrappingsIdApi apiInstance = new GiftWrappingsIdApi(defaultClient);
    Integer id = 56; // Integer | 
    Integer storeId = 56; // Integer | 
    try {
      GiftWrappingDataWrappingInterface result = apiInstance.giftWrappingWrappingRepositoryV1GetGet(id, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftWrappingsIdApi#giftWrappingWrappingRepositoryV1GetGet");
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
| **id** | **Integer**|  | |
| **storeId** | **Integer**|  | [optional] |

### Return type

[**GiftWrappingDataWrappingInterface**](GiftWrappingDataWrappingInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

