# CartsGuestCartsCartIdGiftCardsGiftCardCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete**](CartsGuestCartsCartIdGiftCardsGiftCardCodeApi.md#giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete) | **DELETE** /V1/carts/guest-carts/{cartId}/giftCards/{giftCardCode} | carts/guest-carts/{cartId}/giftCards/{giftCardCode} |


<a id="giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete"></a>
# **giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete**
> Boolean giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete(cartId, giftCardCode)

carts/guest-carts/{cartId}/giftCards/{giftCardCode}

Remove GiftCard Account entity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsGuestCartsCartIdGiftCardsGiftCardCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsGuestCartsCartIdGiftCardsGiftCardCodeApi apiInstance = new CartsGuestCartsCartIdGiftCardsGiftCardCodeApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    String giftCardCode = "giftCardCode_example"; // String | 
    try {
      Boolean result = apiInstance.giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete(cartId, giftCardCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsGuestCartsCartIdGiftCardsGiftCardCodeApi#giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete");
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
| **cartId** | **String**|  | |
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
| **0** | Unexpected error |  -  |

