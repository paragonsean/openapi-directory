# CartsMineShippingInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkoutShippingInformationManagementV1SaveAddressInformationPost**](CartsMineShippingInformationApi.md#checkoutShippingInformationManagementV1SaveAddressInformationPost) | **POST** /V1/carts/mine/shipping-information | carts/mine/shipping-information |


<a id="checkoutShippingInformationManagementV1SaveAddressInformationPost"></a>
# **checkoutShippingInformationManagementV1SaveAddressInformationPost**
> CheckoutDataPaymentDetailsInterface checkoutShippingInformationManagementV1SaveAddressInformationPost(checkoutShippingInformationManagementV1SaveAddressInformationPostRequest)

carts/mine/shipping-information



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineShippingInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineShippingInformationApi apiInstance = new CartsMineShippingInformationApi(defaultClient);
    CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest checkoutShippingInformationManagementV1SaveAddressInformationPostRequest = new CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest(); // CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest | 
    try {
      CheckoutDataPaymentDetailsInterface result = apiInstance.checkoutShippingInformationManagementV1SaveAddressInformationPost(checkoutShippingInformationManagementV1SaveAddressInformationPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineShippingInformationApi#checkoutShippingInformationManagementV1SaveAddressInformationPost");
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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

