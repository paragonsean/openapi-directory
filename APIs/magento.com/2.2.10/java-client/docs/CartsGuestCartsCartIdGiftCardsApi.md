# CartsGuestCartsCartIdGiftCardsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost**](CartsGuestCartsCartIdGiftCardsApi.md#giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost) | **POST** /V1/carts/guest-carts/{cartId}/giftCards | carts/guest-carts/{cartId}/giftCards |


<a id="giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost"></a>
# **giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost**
> Boolean giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost(cartId, giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest)

carts/guest-carts/{cartId}/giftCards



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsGuestCartsCartIdGiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsGuestCartsCartIdGiftCardsApi apiInstance = new CartsGuestCartsCartIdGiftCardsApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest = new GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest(); // GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest | 
    try {
      Boolean result = apiInstance.giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost(cartId, giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsGuestCartsCartIdGiftCardsApi#giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost");
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
| **0** | Unexpected error |  -  |

