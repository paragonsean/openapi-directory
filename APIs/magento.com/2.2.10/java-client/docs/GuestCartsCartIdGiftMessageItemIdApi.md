# GuestCartsCartIdGiftMessageItemIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftMessageGuestItemRepositoryV1GetGet**](GuestCartsCartIdGiftMessageItemIdApi.md#giftMessageGuestItemRepositoryV1GetGet) | **GET** /V1/guest-carts/{cartId}/gift-message/{itemId} | guest-carts/{cartId}/gift-message/{itemId} |
| [**giftMessageGuestItemRepositoryV1SavePost**](GuestCartsCartIdGiftMessageItemIdApi.md#giftMessageGuestItemRepositoryV1SavePost) | **POST** /V1/guest-carts/{cartId}/gift-message/{itemId} | guest-carts/{cartId}/gift-message/{itemId} |


<a id="giftMessageGuestItemRepositoryV1GetGet"></a>
# **giftMessageGuestItemRepositoryV1GetGet**
> GiftMessageDataMessageInterface giftMessageGuestItemRepositoryV1GetGet(cartId, itemId)

guest-carts/{cartId}/gift-message/{itemId}

Return the gift message for a specified item in a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdGiftMessageItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdGiftMessageItemIdApi apiInstance = new GuestCartsCartIdGiftMessageItemIdApi(defaultClient);
    String cartId = "cartId_example"; // String | The shopping cart ID.
    Integer itemId = 56; // Integer | The item ID.
    try {
      GiftMessageDataMessageInterface result = apiInstance.giftMessageGuestItemRepositoryV1GetGet(cartId, itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdGiftMessageItemIdApi#giftMessageGuestItemRepositoryV1GetGet");
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
| **cartId** | **String**| The shopping cart ID. | |
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
| **0** | Unexpected error |  -  |

<a id="giftMessageGuestItemRepositoryV1SavePost"></a>
# **giftMessageGuestItemRepositoryV1SavePost**
> Boolean giftMessageGuestItemRepositoryV1SavePost(cartId, itemId, giftMessageCartRepositoryV1SavePostRequest)

guest-carts/{cartId}/gift-message/{itemId}

Set the gift message for a specified item in a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdGiftMessageItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdGiftMessageItemIdApi apiInstance = new GuestCartsCartIdGiftMessageItemIdApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    Integer itemId = 56; // Integer | The item ID.
    GiftMessageCartRepositoryV1SavePostRequest giftMessageCartRepositoryV1SavePostRequest = new GiftMessageCartRepositoryV1SavePostRequest(); // GiftMessageCartRepositoryV1SavePostRequest | 
    try {
      Boolean result = apiInstance.giftMessageGuestItemRepositoryV1SavePost(cartId, itemId, giftMessageCartRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdGiftMessageItemIdApi#giftMessageGuestItemRepositoryV1SavePost");
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
| **0** | Unexpected error |  -  |

