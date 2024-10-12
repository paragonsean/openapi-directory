# CartsMineCollectionPointSearchRequestApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**temandoShippingCollectionPointCartCollectionPointManagementV1DeleteSearchRequestDelete**](CartsMineCollectionPointSearchRequestApi.md#temandoShippingCollectionPointCartCollectionPointManagementV1DeleteSearchRequestDelete) | **DELETE** /V1/carts/mine/collection-point/search-request | carts/mine/collection-point/search-request |
| [**temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPut**](CartsMineCollectionPointSearchRequestApi.md#temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPut) | **PUT** /V1/carts/mine/collection-point/search-request | carts/mine/collection-point/search-request |


<a id="temandoShippingCollectionPointCartCollectionPointManagementV1DeleteSearchRequestDelete"></a>
# **temandoShippingCollectionPointCartCollectionPointManagementV1DeleteSearchRequestDelete**
> Boolean temandoShippingCollectionPointCartCollectionPointManagementV1DeleteSearchRequestDelete()

carts/mine/collection-point/search-request



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineCollectionPointSearchRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineCollectionPointSearchRequestApi apiInstance = new CartsMineCollectionPointSearchRequestApi(defaultClient);
    try {
      Boolean result = apiInstance.temandoShippingCollectionPointCartCollectionPointManagementV1DeleteSearchRequestDelete();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineCollectionPointSearchRequestApi#temandoShippingCollectionPointCartCollectionPointManagementV1DeleteSearchRequestDelete");
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
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

<a id="temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPut"></a>
# **temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPut**
> TemandoShippingDataCollectionPointSearchRequestInterface temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPut(temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest)

carts/mine/collection-point/search-request



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineCollectionPointSearchRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineCollectionPointSearchRequestApi apiInstance = new CartsMineCollectionPointSearchRequestApi(defaultClient);
    TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest = new TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest(); // TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest | 
    try {
      TemandoShippingDataCollectionPointSearchRequestInterface result = apiInstance.temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPut(temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineCollectionPointSearchRequestApi#temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPut");
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
| **temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest** | [**TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest**](TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest.md)|  | [optional] |

### Return type

[**TemandoShippingDataCollectionPointSearchRequestInterface**](TemandoShippingDataCollectionPointSearchRequestInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

