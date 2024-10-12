# CartsMineGiftCardsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPost**](CartsMineGiftCardsApi.md#giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPost) | **POST** /V1/carts/mine/giftCards | carts/mine/giftCards |


<a id="giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPost"></a>
# **giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPost**
> Boolean giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPost(giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest)

carts/mine/giftCards



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineGiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineGiftCardsApi apiInstance = new CartsMineGiftCardsApi(defaultClient);
    GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest = new GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest(); // GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest | 
    try {
      Boolean result = apiInstance.giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPost(giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineGiftCardsApi#giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPost");
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
| **giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest** | [**GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest**](GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest.md)|  | [optional] |

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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

