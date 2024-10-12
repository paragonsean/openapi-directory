# CartsGuestCartsCartIdCheckGiftCardGiftCardCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftCardAccountGuestGiftCardAccountManagementV1CheckGiftCardGet**](CartsGuestCartsCartIdCheckGiftCardGiftCardCodeApi.md#giftCardAccountGuestGiftCardAccountManagementV1CheckGiftCardGet) | **GET** /V1/carts/guest-carts/{cartId}/checkGiftCard/{giftCardCode} | carts/guest-carts/{cartId}/checkGiftCard/{giftCardCode} |


<a id="giftCardAccountGuestGiftCardAccountManagementV1CheckGiftCardGet"></a>
# **giftCardAccountGuestGiftCardAccountManagementV1CheckGiftCardGet**
> BigDecimal giftCardAccountGuestGiftCardAccountManagementV1CheckGiftCardGet(cartId, giftCardCode)

carts/guest-carts/{cartId}/checkGiftCard/{giftCardCode}



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsGuestCartsCartIdCheckGiftCardGiftCardCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsGuestCartsCartIdCheckGiftCardGiftCardCodeApi apiInstance = new CartsGuestCartsCartIdCheckGiftCardGiftCardCodeApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    String giftCardCode = "giftCardCode_example"; // String | 
    try {
      BigDecimal result = apiInstance.giftCardAccountGuestGiftCardAccountManagementV1CheckGiftCardGet(cartId, giftCardCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsGuestCartsCartIdCheckGiftCardGiftCardCodeApi#giftCardAccountGuestGiftCardAccountManagementV1CheckGiftCardGet");
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

[**BigDecimal**](BigDecimal.md)

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
| **0** | Unexpected error |  -  |

