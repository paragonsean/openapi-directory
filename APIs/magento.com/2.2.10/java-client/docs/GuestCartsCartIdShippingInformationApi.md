# GuestCartsCartIdShippingInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkoutGuestShippingInformationManagementV1SaveAddressInformationPost**](GuestCartsCartIdShippingInformationApi.md#checkoutGuestShippingInformationManagementV1SaveAddressInformationPost) | **POST** /V1/guest-carts/{cartId}/shipping-information | guest-carts/{cartId}/shipping-information |


<a id="checkoutGuestShippingInformationManagementV1SaveAddressInformationPost"></a>
# **checkoutGuestShippingInformationManagementV1SaveAddressInformationPost**
> CheckoutDataPaymentDetailsInterface checkoutGuestShippingInformationManagementV1SaveAddressInformationPost(cartId, checkoutShippingInformationManagementV1SaveAddressInformationPostRequest)

guest-carts/{cartId}/shipping-information



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdShippingInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdShippingInformationApi apiInstance = new GuestCartsCartIdShippingInformationApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest checkoutShippingInformationManagementV1SaveAddressInformationPostRequest = new CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest(); // CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest | 
    try {
      CheckoutDataPaymentDetailsInterface result = apiInstance.checkoutGuestShippingInformationManagementV1SaveAddressInformationPost(cartId, checkoutShippingInformationManagementV1SaveAddressInformationPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdShippingInformationApi#checkoutGuestShippingInformationManagementV1SaveAddressInformationPost");
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
| **checkoutShippingInformationManagementV1SaveAddressInformationPostRequest** | [**CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest**](CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest.md)|  | [optional] |

### Return type

[**CheckoutDataPaymentDetailsInterface**](CheckoutDataPaymentDetailsInterface.md)

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

