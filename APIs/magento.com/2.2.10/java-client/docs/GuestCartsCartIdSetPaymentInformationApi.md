# GuestCartsCartIdSetPaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkoutGuestPaymentInformationManagementV1SavePaymentInformationPost**](GuestCartsCartIdSetPaymentInformationApi.md#checkoutGuestPaymentInformationManagementV1SavePaymentInformationPost) | **POST** /V1/guest-carts/{cartId}/set-payment-information | guest-carts/{cartId}/set-payment-information |


<a id="checkoutGuestPaymentInformationManagementV1SavePaymentInformationPost"></a>
# **checkoutGuestPaymentInformationManagementV1SavePaymentInformationPost**
> Integer checkoutGuestPaymentInformationManagementV1SavePaymentInformationPost(cartId, checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest)

guest-carts/{cartId}/set-payment-information

Set payment information for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdSetPaymentInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdSetPaymentInformationApi apiInstance = new GuestCartsCartIdSetPaymentInformationApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest = new CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest(); // CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
    try {
      Integer result = apiInstance.checkoutGuestPaymentInformationManagementV1SavePaymentInformationPost(cartId, checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdSetPaymentInformationApi#checkoutGuestPaymentInformationManagementV1SavePaymentInformationPost");
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
| **checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest** | [**CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest**](CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest.md)|  | [optional] |

### Return type

**Integer**

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
| **0** | Unexpected error |  -  |

