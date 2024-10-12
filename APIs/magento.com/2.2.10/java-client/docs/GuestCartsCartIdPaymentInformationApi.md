# GuestCartsCartIdPaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkoutGuestPaymentInformationManagementV1GetPaymentInformationGet**](GuestCartsCartIdPaymentInformationApi.md#checkoutGuestPaymentInformationManagementV1GetPaymentInformationGet) | **GET** /V1/guest-carts/{cartId}/payment-information | guest-carts/{cartId}/payment-information |
| [**checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost**](GuestCartsCartIdPaymentInformationApi.md#checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost) | **POST** /V1/guest-carts/{cartId}/payment-information | guest-carts/{cartId}/payment-information |


<a id="checkoutGuestPaymentInformationManagementV1GetPaymentInformationGet"></a>
# **checkoutGuestPaymentInformationManagementV1GetPaymentInformationGet**
> CheckoutDataPaymentDetailsInterface checkoutGuestPaymentInformationManagementV1GetPaymentInformationGet(cartId)

guest-carts/{cartId}/payment-information

Get payment information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdPaymentInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdPaymentInformationApi apiInstance = new GuestCartsCartIdPaymentInformationApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    try {
      CheckoutDataPaymentDetailsInterface result = apiInstance.checkoutGuestPaymentInformationManagementV1GetPaymentInformationGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdPaymentInformationApi#checkoutGuestPaymentInformationManagementV1GetPaymentInformationGet");
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

### Return type

[**CheckoutDataPaymentDetailsInterface**](CheckoutDataPaymentDetailsInterface.md)

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

<a id="checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost"></a>
# **checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost**
> Integer checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost(cartId, checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest)

guest-carts/{cartId}/payment-information

Set payment information and place order for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdPaymentInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdPaymentInformationApi apiInstance = new GuestCartsCartIdPaymentInformationApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest = new CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest(); // CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
    try {
      Integer result = apiInstance.checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost(cartId, checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdPaymentInformationApi#checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost");
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

