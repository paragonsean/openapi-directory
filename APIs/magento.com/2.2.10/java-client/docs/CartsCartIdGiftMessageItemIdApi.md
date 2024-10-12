# CartsCartIdGiftMessageItemIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdGiftMessageItemIdGet**](CartsCartIdGiftMessageItemIdApi.md#v1CartsCartIdGiftMessageItemIdGet) | **GET** /V1/carts/{cartId}/gift-message/{itemId} | carts/{cartId}/gift-message/{itemId} |
| [**v1CartsCartIdGiftMessageItemIdPost**](CartsCartIdGiftMessageItemIdApi.md#v1CartsCartIdGiftMessageItemIdPost) | **POST** /V1/carts/{cartId}/gift-message/{itemId} | carts/{cartId}/gift-message/{itemId} |


<a id="v1CartsCartIdGiftMessageItemIdGet"></a>
# **v1CartsCartIdGiftMessageItemIdGet**
> GiftMessageDataMessageInterface v1CartsCartIdGiftMessageItemIdGet(cartId, itemId)

carts/{cartId}/gift-message/{itemId}

Return the gift message for a specified item in a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdGiftMessageItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdGiftMessageItemIdApi apiInstance = new CartsCartIdGiftMessageItemIdApi(defaultClient);
    Integer cartId = 56; // Integer | The shopping cart ID.
    Integer itemId = 56; // Integer | The item ID.
    try {
      GiftMessageDataMessageInterface result = apiInstance.v1CartsCartIdGiftMessageItemIdGet(cartId, itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdGiftMessageItemIdApi#v1CartsCartIdGiftMessageItemIdGet");
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
| **cartId** | **Integer**| The shopping cart ID. | |
| **itemId** | **Integer**| The item ID. | |

### Return type

[**GiftMessageDataMessageInterface**](GiftMessageDataMessageInterface.md)

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

<a id="v1CartsCartIdGiftMessageItemIdPost"></a>
# **v1CartsCartIdGiftMessageItemIdPost**
> Boolean v1CartsCartIdGiftMessageItemIdPost(cartId, itemId, giftMessageCartRepositoryV1SavePostRequest)

carts/{cartId}/gift-message/{itemId}

Set the gift message for a specified item in a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdGiftMessageItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdGiftMessageItemIdApi apiInstance = new CartsCartIdGiftMessageItemIdApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    Integer itemId = 56; // Integer | The item ID.
    GiftMessageCartRepositoryV1SavePostRequest giftMessageCartRepositoryV1SavePostRequest = new GiftMessageCartRepositoryV1SavePostRequest(); // GiftMessageCartRepositoryV1SavePostRequest | 
    try {
      Boolean result = apiInstance.v1CartsCartIdGiftMessageItemIdPost(cartId, itemId, giftMessageCartRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdGiftMessageItemIdApi#v1CartsCartIdGiftMessageItemIdPost");
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
| **itemId** | **Integer**| The item ID. | |
| **giftMessageCartRepositoryV1SavePostRequest** | [**GiftMessageCartRepositoryV1SavePostRequest**](GiftMessageCartRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

**Boolean**

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

