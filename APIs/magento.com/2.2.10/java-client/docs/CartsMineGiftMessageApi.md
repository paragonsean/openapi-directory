# CartsMineGiftMessageApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftMessageCartRepositoryV1GetGet**](CartsMineGiftMessageApi.md#giftMessageCartRepositoryV1GetGet) | **GET** /V1/carts/mine/gift-message | carts/mine/gift-message |
| [**giftMessageCartRepositoryV1SavePost**](CartsMineGiftMessageApi.md#giftMessageCartRepositoryV1SavePost) | **POST** /V1/carts/mine/gift-message | carts/mine/gift-message |


<a id="giftMessageCartRepositoryV1GetGet"></a>
# **giftMessageCartRepositoryV1GetGet**
> GiftMessageDataMessageInterface giftMessageCartRepositoryV1GetGet()

carts/mine/gift-message

Return the gift message for a specified order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineGiftMessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineGiftMessageApi apiInstance = new CartsMineGiftMessageApi(defaultClient);
    try {
      GiftMessageDataMessageInterface result = apiInstance.giftMessageCartRepositoryV1GetGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineGiftMessageApi#giftMessageCartRepositoryV1GetGet");
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

<a id="giftMessageCartRepositoryV1SavePost"></a>
# **giftMessageCartRepositoryV1SavePost**
> Boolean giftMessageCartRepositoryV1SavePost(giftMessageCartRepositoryV1SavePostRequest)

carts/mine/gift-message

Set the gift message for an entire order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineGiftMessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineGiftMessageApi apiInstance = new CartsMineGiftMessageApi(defaultClient);
    GiftMessageCartRepositoryV1SavePostRequest giftMessageCartRepositoryV1SavePostRequest = new GiftMessageCartRepositoryV1SavePostRequest(); // GiftMessageCartRepositoryV1SavePostRequest | 
    try {
      Boolean result = apiInstance.giftMessageCartRepositoryV1SavePost(giftMessageCartRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineGiftMessageApi#giftMessageCartRepositoryV1SavePost");
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

