# CartsCartIdItemsItemIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdItemsItemIdDelete**](CartsCartIdItemsItemIdApi.md#v1CartsCartIdItemsItemIdDelete) | **DELETE** /V1/carts/{cartId}/items/{itemId} | carts/{cartId}/items/{itemId} |
| [**v1CartsCartIdItemsItemIdPut**](CartsCartIdItemsItemIdApi.md#v1CartsCartIdItemsItemIdPut) | **PUT** /V1/carts/{cartId}/items/{itemId} | carts/{cartId}/items/{itemId} |


<a id="v1CartsCartIdItemsItemIdDelete"></a>
# **v1CartsCartIdItemsItemIdDelete**
> Boolean v1CartsCartIdItemsItemIdDelete(cartId, itemId)

carts/{cartId}/items/{itemId}

Removes the specified item from the specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdItemsItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdItemsItemIdApi apiInstance = new CartsCartIdItemsItemIdApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    Integer itemId = 56; // Integer | The item ID of the item to be removed.
    try {
      Boolean result = apiInstance.v1CartsCartIdItemsItemIdDelete(cartId, itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdItemsItemIdApi#v1CartsCartIdItemsItemIdDelete");
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
| **cartId** | **Integer**| The cart ID. | |
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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="v1CartsCartIdItemsItemIdPut"></a>
# **v1CartsCartIdItemsItemIdPut**
> QuoteDataCartItemInterface v1CartsCartIdItemsItemIdPut(cartId, itemId, quoteCartItemRepositoryV1SavePostRequest)

carts/{cartId}/items/{itemId}

Add/update the specified cart item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdItemsItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdItemsItemIdApi apiInstance = new CartsCartIdItemsItemIdApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    String itemId = "itemId_example"; // String | 
    QuoteCartItemRepositoryV1SavePostRequest quoteCartItemRepositoryV1SavePostRequest = new QuoteCartItemRepositoryV1SavePostRequest(); // QuoteCartItemRepositoryV1SavePostRequest | 
    try {
      QuoteDataCartItemInterface result = apiInstance.v1CartsCartIdItemsItemIdPut(cartId, itemId, quoteCartItemRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdItemsItemIdApi#v1CartsCartIdItemsItemIdPut");
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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

