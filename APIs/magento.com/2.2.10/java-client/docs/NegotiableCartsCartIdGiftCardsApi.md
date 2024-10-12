# NegotiableCartsCartIdGiftCardsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteGiftCardAccountManagementV1SaveByQuoteIdPost**](NegotiableCartsCartIdGiftCardsApi.md#negotiableQuoteGiftCardAccountManagementV1SaveByQuoteIdPost) | **POST** /V1/negotiable-carts/{cartId}/giftCards | negotiable-carts/{cartId}/giftCards |


<a id="negotiableQuoteGiftCardAccountManagementV1SaveByQuoteIdPost"></a>
# **negotiableQuoteGiftCardAccountManagementV1SaveByQuoteIdPost**
> Boolean negotiableQuoteGiftCardAccountManagementV1SaveByQuoteIdPost(cartId, giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest)

negotiable-carts/{cartId}/giftCards



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableCartsCartIdGiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableCartsCartIdGiftCardsApi apiInstance = new NegotiableCartsCartIdGiftCardsApi(defaultClient);
    Integer cartId = 56; // Integer | 
    GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest = new GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest(); // GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest | 
    try {
      Boolean result = apiInstance.negotiableQuoteGiftCardAccountManagementV1SaveByQuoteIdPost(cartId, giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableCartsCartIdGiftCardsApi#negotiableQuoteGiftCardAccountManagementV1SaveByQuoteIdPost");
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
| **cartId** | **Integer**|  | |
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

