# GuestCartsCartIdGiftMessageApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftMessageGuestCartRepositoryV1GetGet**](GuestCartsCartIdGiftMessageApi.md#giftMessageGuestCartRepositoryV1GetGet) | **GET** /V1/guest-carts/{cartId}/gift-message | guest-carts/{cartId}/gift-message |
| [**giftMessageGuestCartRepositoryV1SavePost**](GuestCartsCartIdGiftMessageApi.md#giftMessageGuestCartRepositoryV1SavePost) | **POST** /V1/guest-carts/{cartId}/gift-message | guest-carts/{cartId}/gift-message |


<a id="giftMessageGuestCartRepositoryV1GetGet"></a>
# **giftMessageGuestCartRepositoryV1GetGet**
> GiftMessageDataMessageInterface giftMessageGuestCartRepositoryV1GetGet(cartId)

guest-carts/{cartId}/gift-message

Return the gift message for a specified order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdGiftMessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdGiftMessageApi apiInstance = new GuestCartsCartIdGiftMessageApi(defaultClient);
    String cartId = "cartId_example"; // String | The shopping cart ID.
    try {
      GiftMessageDataMessageInterface result = apiInstance.giftMessageGuestCartRepositoryV1GetGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdGiftMessageApi#giftMessageGuestCartRepositoryV1GetGet");
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
| **0** | Unexpected error |  -  |

<a id="giftMessageGuestCartRepositoryV1SavePost"></a>
# **giftMessageGuestCartRepositoryV1SavePost**
> Boolean giftMessageGuestCartRepositoryV1SavePost(cartId, giftMessageCartRepositoryV1SavePostRequest)

guest-carts/{cartId}/gift-message

Set the gift message for an entire order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdGiftMessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdGiftMessageApi apiInstance = new GuestCartsCartIdGiftMessageApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    GiftMessageCartRepositoryV1SavePostRequest giftMessageCartRepositoryV1SavePostRequest = new GiftMessageCartRepositoryV1SavePostRequest(); // GiftMessageCartRepositoryV1SavePostRequest | 
    try {
      Boolean result = apiInstance.giftMessageGuestCartRepositoryV1SavePost(cartId, giftMessageCartRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdGiftMessageApi#giftMessageGuestCartRepositoryV1SavePost");
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

