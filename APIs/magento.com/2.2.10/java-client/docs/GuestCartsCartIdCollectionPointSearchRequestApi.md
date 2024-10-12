# GuestCartsCartIdCollectionPointSearchRequestApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**temandoShippingCollectionPointGuestCartCollectionPointManagementV1DeleteSearchRequestDelete**](GuestCartsCartIdCollectionPointSearchRequestApi.md#temandoShippingCollectionPointGuestCartCollectionPointManagementV1DeleteSearchRequestDelete) | **DELETE** /V1/guest-carts/{cartId}/collection-point/search-request | guest-carts/{cartId}/collection-point/search-request |
| [**temandoShippingCollectionPointGuestCartCollectionPointManagementV1SaveSearchRequestPut**](GuestCartsCartIdCollectionPointSearchRequestApi.md#temandoShippingCollectionPointGuestCartCollectionPointManagementV1SaveSearchRequestPut) | **PUT** /V1/guest-carts/{cartId}/collection-point/search-request | guest-carts/{cartId}/collection-point/search-request |


<a id="temandoShippingCollectionPointGuestCartCollectionPointManagementV1DeleteSearchRequestDelete"></a>
# **temandoShippingCollectionPointGuestCartCollectionPointManagementV1DeleteSearchRequestDelete**
> Boolean temandoShippingCollectionPointGuestCartCollectionPointManagementV1DeleteSearchRequestDelete(cartId)

guest-carts/{cartId}/collection-point/search-request



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdCollectionPointSearchRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdCollectionPointSearchRequestApi apiInstance = new GuestCartsCartIdCollectionPointSearchRequestApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    try {
      Boolean result = apiInstance.temandoShippingCollectionPointGuestCartCollectionPointManagementV1DeleteSearchRequestDelete(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdCollectionPointSearchRequestApi#temandoShippingCollectionPointGuestCartCollectionPointManagementV1DeleteSearchRequestDelete");
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
| **cartId** | **String**|  | |

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

<a id="temandoShippingCollectionPointGuestCartCollectionPointManagementV1SaveSearchRequestPut"></a>
# **temandoShippingCollectionPointGuestCartCollectionPointManagementV1SaveSearchRequestPut**
> TemandoShippingDataCollectionPointSearchRequestInterface temandoShippingCollectionPointGuestCartCollectionPointManagementV1SaveSearchRequestPut(cartId, temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest)

guest-carts/{cartId}/collection-point/search-request



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdCollectionPointSearchRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdCollectionPointSearchRequestApi apiInstance = new GuestCartsCartIdCollectionPointSearchRequestApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest = new TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest(); // TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest | 
    try {
      TemandoShippingDataCollectionPointSearchRequestInterface result = apiInstance.temandoShippingCollectionPointGuestCartCollectionPointManagementV1SaveSearchRequestPut(cartId, temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdCollectionPointSearchRequestApi#temandoShippingCollectionPointGuestCartCollectionPointManagementV1SaveSearchRequestPut");
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
| **cartId** | **String**|  | |
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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

