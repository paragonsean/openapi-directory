# NegotiableCartsCartIdSetPaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuotePaymentInformationManagementV1SavePaymentInformationPost**](NegotiableCartsCartIdSetPaymentInformationApi.md#negotiableQuotePaymentInformationManagementV1SavePaymentInformationPost) | **POST** /V1/negotiable-carts/{cartId}/set-payment-information | negotiable-carts/{cartId}/set-payment-information |


<a id="negotiableQuotePaymentInformationManagementV1SavePaymentInformationPost"></a>
# **negotiableQuotePaymentInformationManagementV1SavePaymentInformationPost**
> Integer negotiableQuotePaymentInformationManagementV1SavePaymentInformationPost(cartId, checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest)

negotiable-carts/{cartId}/set-payment-information

Set payment information for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableCartsCartIdSetPaymentInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableCartsCartIdSetPaymentInformationApi apiInstance = new NegotiableCartsCartIdSetPaymentInformationApi(defaultClient);
    Integer cartId = 56; // Integer | 
    CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest = new CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest(); // CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
    try {
      Integer result = apiInstance.negotiableQuotePaymentInformationManagementV1SavePaymentInformationPost(cartId, checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableCartsCartIdSetPaymentInformationApi#negotiableQuotePaymentInformationManagementV1SavePaymentInformationPost");
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
| **checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest** | [**CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest**](CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest.md)|  | [optional] |

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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

