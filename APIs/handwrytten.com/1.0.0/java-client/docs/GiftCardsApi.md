# GiftCardsApi

All URIs are relative to *https://api.handwrytten.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getGiftCardDetails**](GiftCardsApi.md#getGiftCardDetails) | **GET** /giftCards/view | Lists information on gift cards |
| [**giftCardDetails**](GiftCardsApi.md#giftCardDetails) | **POST** /giftCards/view | Lists information on gift cards |


<a id="getGiftCardDetails"></a>
# **getGiftCardDetails**
> List&lt;GiftCard&gt; getGiftCardDetails()

Lists information on gift cards

Returns images and details (and associated denominations) of all gift cards

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    GiftCardsApi apiInstance = new GiftCardsApi(defaultClient);
    try {
      List<GiftCard> result = apiInstance.getGiftCardDetails();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardsApi#getGiftCardDetails");
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

[**List&lt;GiftCard&gt;**](GiftCard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="giftCardDetails"></a>
# **giftCardDetails**
> List&lt;GiftCard&gt; giftCardDetails()

Lists information on gift cards

Returns images and details (and associated denominations) of all gift cards

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    GiftCardsApi apiInstance = new GiftCardsApi(defaultClient);
    try {
      List<GiftCard> result = apiInstance.giftCardDetails();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardsApi#giftCardDetails");
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

[**List&lt;GiftCard&gt;**](GiftCard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

