# GuestCartsCartIdItemsItemIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestCartItemRepositoryV1DeleteByIdDelete**](GuestCartsCartIdItemsItemIdApi.md#quoteGuestCartItemRepositoryV1DeleteByIdDelete) | **DELETE** /V1/guest-carts/{cartId}/items/{itemId} | guest-carts/{cartId}/items/{itemId} |
| [**quoteGuestCartItemRepositoryV1SavePut**](GuestCartsCartIdItemsItemIdApi.md#quoteGuestCartItemRepositoryV1SavePut) | **PUT** /V1/guest-carts/{cartId}/items/{itemId} | guest-carts/{cartId}/items/{itemId} |


<a id="quoteGuestCartItemRepositoryV1DeleteByIdDelete"></a>
# **quoteGuestCartItemRepositoryV1DeleteByIdDelete**
> Boolean quoteGuestCartItemRepositoryV1DeleteByIdDelete(cartId, itemId)

guest-carts/{cartId}/items/{itemId}

Remove the specified item from the specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdItemsItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdItemsItemIdApi apiInstance = new GuestCartsCartIdItemsItemIdApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    Integer itemId = 56; // Integer | The item ID of the item to be removed.
    try {
      Boolean result = apiInstance.quoteGuestCartItemRepositoryV1DeleteByIdDelete(cartId, itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdItemsItemIdApi#quoteGuestCartItemRepositoryV1DeleteByIdDelete");
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
| **cartId** | **String**| The cart ID. | |
| **itemId** | **Integer**| The item ID of the item to be removed. | |

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
| **0** | Unexpected error |  -  |

<a id="quoteGuestCartItemRepositoryV1SavePut"></a>
# **quoteGuestCartItemRepositoryV1SavePut**
> QuoteDataCartItemInterface quoteGuestCartItemRepositoryV1SavePut(cartId, itemId, quoteCartItemRepositoryV1SavePostRequest)

guest-carts/{cartId}/items/{itemId}

Add/update the specified cart item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdItemsItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdItemsItemIdApi apiInstance = new GuestCartsCartIdItemsItemIdApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    String itemId = "itemId_example"; // String | 
    QuoteCartItemRepositoryV1SavePostRequest quoteCartItemRepositoryV1SavePostRequest = new QuoteCartItemRepositoryV1SavePostRequest(); // QuoteCartItemRepositoryV1SavePostRequest | 
    try {
      QuoteDataCartItemInterface result = apiInstance.quoteGuestCartItemRepositoryV1SavePut(cartId, itemId, quoteCartItemRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdItemsItemIdApi#quoteGuestCartItemRepositoryV1SavePut");
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
| **itemId** | **String**|  | |
| **quoteCartItemRepositoryV1SavePostRequest** | [**QuoteCartItemRepositoryV1SavePostRequest**](QuoteCartItemRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **0** | Unexpected error |  -  |

