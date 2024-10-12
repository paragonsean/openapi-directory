# CartsMineItemsItemIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteCartItemRepositoryV1DeleteByIdDelete**](CartsMineItemsItemIdApi.md#quoteCartItemRepositoryV1DeleteByIdDelete) | **DELETE** /V1/carts/mine/items/{itemId} | carts/mine/items/{itemId} |
| [**quoteCartItemRepositoryV1SavePut**](CartsMineItemsItemIdApi.md#quoteCartItemRepositoryV1SavePut) | **PUT** /V1/carts/mine/items/{itemId} | carts/mine/items/{itemId} |


<a id="quoteCartItemRepositoryV1DeleteByIdDelete"></a>
# **quoteCartItemRepositoryV1DeleteByIdDelete**
> Boolean quoteCartItemRepositoryV1DeleteByIdDelete(itemId)

carts/mine/items/{itemId}

Removes the specified item from the specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineItemsItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineItemsItemIdApi apiInstance = new CartsMineItemsItemIdApi(defaultClient);
    Integer itemId = 56; // Integer | The item ID of the item to be removed.
    try {
      Boolean result = apiInstance.quoteCartItemRepositoryV1DeleteByIdDelete(itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineItemsItemIdApi#quoteCartItemRepositoryV1DeleteByIdDelete");
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

<a id="quoteCartItemRepositoryV1SavePut"></a>
# **quoteCartItemRepositoryV1SavePut**
> QuoteDataCartItemInterface quoteCartItemRepositoryV1SavePut(itemId, quoteCartItemRepositoryV1SavePostRequest)

carts/mine/items/{itemId}

Add/update the specified cart item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineItemsItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineItemsItemIdApi apiInstance = new CartsMineItemsItemIdApi(defaultClient);
    String itemId = "itemId_example"; // String | 
    QuoteCartItemRepositoryV1SavePostRequest quoteCartItemRepositoryV1SavePostRequest = new QuoteCartItemRepositoryV1SavePostRequest(); // QuoteCartItemRepositoryV1SavePostRequest | 
    try {
      QuoteDataCartItemInterface result = apiInstance.quoteCartItemRepositoryV1SavePut(itemId, quoteCartItemRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineItemsItemIdApi#quoteCartItemRepositoryV1SavePut");
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

