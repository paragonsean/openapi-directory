# NegotiableCartsCartIdGiftCardsGiftCardCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteGiftCardAccountManagementV1DeleteByQuoteIdDelete**](NegotiableCartsCartIdGiftCardsGiftCardCodeApi.md#negotiableQuoteGiftCardAccountManagementV1DeleteByQuoteIdDelete) | **DELETE** /V1/negotiable-carts/{cartId}/giftCards/{giftCardCode} | negotiable-carts/{cartId}/giftCards/{giftCardCode} |


<a id="negotiableQuoteGiftCardAccountManagementV1DeleteByQuoteIdDelete"></a>
# **negotiableQuoteGiftCardAccountManagementV1DeleteByQuoteIdDelete**
> Boolean negotiableQuoteGiftCardAccountManagementV1DeleteByQuoteIdDelete(cartId, giftCardCode)

negotiable-carts/{cartId}/giftCards/{giftCardCode}

Remove GiftCard Account entity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableCartsCartIdGiftCardsGiftCardCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableCartsCartIdGiftCardsGiftCardCodeApi apiInstance = new NegotiableCartsCartIdGiftCardsGiftCardCodeApi(defaultClient);
    Integer cartId = 56; // Integer | 
    String giftCardCode = "giftCardCode_example"; // String | 
    try {
      Boolean result = apiInstance.negotiableQuoteGiftCardAccountManagementV1DeleteByQuoteIdDelete(cartId, giftCardCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableCartsCartIdGiftCardsGiftCardCodeApi#negotiableQuoteGiftCardAccountManagementV1DeleteByQuoteIdDelete");
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

