# CartsMineGiftCardsGiftCardCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftCardAccountGiftCardAccountManagementV1DeleteByQuoteIdDelete**](CartsMineGiftCardsGiftCardCodeApi.md#giftCardAccountGiftCardAccountManagementV1DeleteByQuoteIdDelete) | **DELETE** /V1/carts/mine/giftCards/{giftCardCode} | carts/mine/giftCards/{giftCardCode} |


<a id="giftCardAccountGiftCardAccountManagementV1DeleteByQuoteIdDelete"></a>
# **giftCardAccountGiftCardAccountManagementV1DeleteByQuoteIdDelete**
> Boolean giftCardAccountGiftCardAccountManagementV1DeleteByQuoteIdDelete(giftCardCode)

carts/mine/giftCards/{giftCardCode}

Remove GiftCard Account entity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineGiftCardsGiftCardCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineGiftCardsGiftCardCodeApi apiInstance = new CartsMineGiftCardsGiftCardCodeApi(defaultClient);
    String giftCardCode = "giftCardCode_example"; // String | 
    try {
      Boolean result = apiInstance.giftCardAccountGiftCardAccountManagementV1DeleteByQuoteIdDelete(giftCardCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineGiftCardsGiftCardCodeApi#giftCardAccountGiftCardAccountManagementV1DeleteByQuoteIdDelete");
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
| **giftCardCode** | **String**|  | |

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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

