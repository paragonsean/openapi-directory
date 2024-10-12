# NegotiableCartsCartIdShippingInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteShippingInformationManagementV1SaveAddressInformationPost**](NegotiableCartsCartIdShippingInformationApi.md#negotiableQuoteShippingInformationManagementV1SaveAddressInformationPost) | **POST** /V1/negotiable-carts/{cartId}/shipping-information | negotiable-carts/{cartId}/shipping-information |


<a id="negotiableQuoteShippingInformationManagementV1SaveAddressInformationPost"></a>
# **negotiableQuoteShippingInformationManagementV1SaveAddressInformationPost**
> CheckoutDataPaymentDetailsInterface negotiableQuoteShippingInformationManagementV1SaveAddressInformationPost(cartId, checkoutShippingInformationManagementV1SaveAddressInformationPostRequest)

negotiable-carts/{cartId}/shipping-information



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableCartsCartIdShippingInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableCartsCartIdShippingInformationApi apiInstance = new NegotiableCartsCartIdShippingInformationApi(defaultClient);
    Integer cartId = 56; // Integer | 
    CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest checkoutShippingInformationManagementV1SaveAddressInformationPostRequest = new CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest(); // CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest | 
    try {
      CheckoutDataPaymentDetailsInterface result = apiInstance.negotiableQuoteShippingInformationManagementV1SaveAddressInformationPost(cartId, checkoutShippingInformationManagementV1SaveAddressInformationPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableCartsCartIdShippingInformationApi#negotiableQuoteShippingInformationManagementV1SaveAddressInformationPost");
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

