# CartsCartIdGiftCardsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPut**](CartsCartIdGiftCardsApi.md#giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPut) | **PUT** /V1/carts/{cartId}/giftCards | carts/{cartId}/giftCards |


<a id="giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPut"></a>
# **giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPut**
> Boolean giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPut(cartId, giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest)

carts/{cartId}/giftCards



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdGiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdGiftCardsApi apiInstance = new CartsCartIdGiftCardsApi(defaultClient);
    Integer cartId = 56; // Integer | 
    GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest = new GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest(); // GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest | 
    try {
      Boolean result = apiInstance.giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPut(cartId, giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdGiftCardsApi#giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPut");
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

