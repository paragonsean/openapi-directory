# CartsCartIdGiftMessageApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdGiftMessageGet**](CartsCartIdGiftMessageApi.md#v1CartsCartIdGiftMessageGet) | **GET** /V1/carts/{cartId}/gift-message | carts/{cartId}/gift-message |
| [**v1CartsCartIdGiftMessagePost**](CartsCartIdGiftMessageApi.md#v1CartsCartIdGiftMessagePost) | **POST** /V1/carts/{cartId}/gift-message | carts/{cartId}/gift-message |


<a id="v1CartsCartIdGiftMessageGet"></a>
# **v1CartsCartIdGiftMessageGet**
> GiftMessageDataMessageInterface v1CartsCartIdGiftMessageGet(cartId)

carts/{cartId}/gift-message

Return the gift message for a specified order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdGiftMessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdGiftMessageApi apiInstance = new CartsCartIdGiftMessageApi(defaultClient);
    Integer cartId = 56; // Integer | The shopping cart ID.
    try {
      GiftMessageDataMessageInterface result = apiInstance.v1CartsCartIdGiftMessageGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdGiftMessageApi#v1CartsCartIdGiftMessageGet");
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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="v1CartsCartIdGiftMessagePost"></a>
# **v1CartsCartIdGiftMessagePost**
> Boolean v1CartsCartIdGiftMessagePost(cartId, giftMessageCartRepositoryV1SavePostRequest)

carts/{cartId}/gift-message

Set the gift message for an entire order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdGiftMessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdGiftMessageApi apiInstance = new CartsCartIdGiftMessageApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    GiftMessageCartRepositoryV1SavePostRequest giftMessageCartRepositoryV1SavePostRequest = new GiftMessageCartRepositoryV1SavePostRequest(); // GiftMessageCartRepositoryV1SavePostRequest | 
    try {
      Boolean result = apiInstance.v1CartsCartIdGiftMessagePost(cartId, giftMessageCartRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdGiftMessageApi#v1CartsCartIdGiftMessagePost");
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

