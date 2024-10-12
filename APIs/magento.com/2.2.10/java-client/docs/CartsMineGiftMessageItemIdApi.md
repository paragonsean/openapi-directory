# CartsMineGiftMessageItemIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftMessageItemRepositoryV1GetGet**](CartsMineGiftMessageItemIdApi.md#giftMessageItemRepositoryV1GetGet) | **GET** /V1/carts/mine/gift-message/{itemId} | carts/mine/gift-message/{itemId} |
| [**giftMessageItemRepositoryV1SavePost**](CartsMineGiftMessageItemIdApi.md#giftMessageItemRepositoryV1SavePost) | **POST** /V1/carts/mine/gift-message/{itemId} | carts/mine/gift-message/{itemId} |


<a id="giftMessageItemRepositoryV1GetGet"></a>
# **giftMessageItemRepositoryV1GetGet**
> GiftMessageDataMessageInterface giftMessageItemRepositoryV1GetGet(itemId)

carts/mine/gift-message/{itemId}

Return the gift message for a specified item in a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineGiftMessageItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineGiftMessageItemIdApi apiInstance = new CartsMineGiftMessageItemIdApi(defaultClient);
    Integer itemId = 56; // Integer | The item ID.
    try {
      GiftMessageDataMessageInterface result = apiInstance.giftMessageItemRepositoryV1GetGet(itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineGiftMessageItemIdApi#giftMessageItemRepositoryV1GetGet");
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

<a id="giftMessageItemRepositoryV1SavePost"></a>
# **giftMessageItemRepositoryV1SavePost**
> Boolean giftMessageItemRepositoryV1SavePost(itemId, giftMessageCartRepositoryV1SavePostRequest)

carts/mine/gift-message/{itemId}

Set the gift message for a specified item in a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineGiftMessageItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineGiftMessageItemIdApi apiInstance = new CartsMineGiftMessageItemIdApi(defaultClient);
    Integer itemId = 56; // Integer | The item ID.
    GiftMessageCartRepositoryV1SavePostRequest giftMessageCartRepositoryV1SavePostRequest = new GiftMessageCartRepositoryV1SavePostRequest(); // GiftMessageCartRepositoryV1SavePostRequest | 
    try {
      Boolean result = apiInstance.giftMessageItemRepositoryV1SavePost(itemId, giftMessageCartRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineGiftMessageItemIdApi#giftMessageItemRepositoryV1SavePost");
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

