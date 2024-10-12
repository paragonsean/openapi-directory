# CartsMineSetPaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkoutPaymentInformationManagementV1SavePaymentInformationPost**](CartsMineSetPaymentInformationApi.md#checkoutPaymentInformationManagementV1SavePaymentInformationPost) | **POST** /V1/carts/mine/set-payment-information | carts/mine/set-payment-information |


<a id="checkoutPaymentInformationManagementV1SavePaymentInformationPost"></a>
# **checkoutPaymentInformationManagementV1SavePaymentInformationPost**
> Integer checkoutPaymentInformationManagementV1SavePaymentInformationPost(checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest)

carts/mine/set-payment-information

Set payment information for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineSetPaymentInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineSetPaymentInformationApi apiInstance = new CartsMineSetPaymentInformationApi(defaultClient);
    CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest = new CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest(); // CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
    try {
      Integer result = apiInstance.checkoutPaymentInformationManagementV1SavePaymentInformationPost(checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineSetPaymentInformationApi#checkoutPaymentInformationManagementV1SavePaymentInformationPost");
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

