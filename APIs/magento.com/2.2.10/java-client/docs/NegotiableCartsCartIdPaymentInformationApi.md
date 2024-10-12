# NegotiableCartsCartIdPaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuotePaymentInformationManagementV1GetPaymentInformationGet**](NegotiableCartsCartIdPaymentInformationApi.md#negotiableQuotePaymentInformationManagementV1GetPaymentInformationGet) | **GET** /V1/negotiable-carts/{cartId}/payment-information | negotiable-carts/{cartId}/payment-information |
| [**negotiableQuotePaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost**](NegotiableCartsCartIdPaymentInformationApi.md#negotiableQuotePaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost) | **POST** /V1/negotiable-carts/{cartId}/payment-information | negotiable-carts/{cartId}/payment-information |


<a id="negotiableQuotePaymentInformationManagementV1GetPaymentInformationGet"></a>
# **negotiableQuotePaymentInformationManagementV1GetPaymentInformationGet**
> CheckoutDataPaymentDetailsInterface negotiableQuotePaymentInformationManagementV1GetPaymentInformationGet(cartId)

negotiable-carts/{cartId}/payment-information

Get payment information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableCartsCartIdPaymentInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableCartsCartIdPaymentInformationApi apiInstance = new NegotiableCartsCartIdPaymentInformationApi(defaultClient);
    Integer cartId = 56; // Integer | 
    try {
      CheckoutDataPaymentDetailsInterface result = apiInstance.negotiableQuotePaymentInformationManagementV1GetPaymentInformationGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableCartsCartIdPaymentInformationApi#negotiableQuotePaymentInformationManagementV1GetPaymentInformationGet");
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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="negotiableQuotePaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost"></a>
# **negotiableQuotePaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost**
> Integer negotiableQuotePaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost(cartId, checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest)

negotiable-carts/{cartId}/payment-information

Set payment information and place order for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableCartsCartIdPaymentInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableCartsCartIdPaymentInformationApi apiInstance = new NegotiableCartsCartIdPaymentInformationApi(defaultClient);
    Integer cartId = 56; // Integer | 
    CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest = new CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest(); // CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
    try {
      Integer result = apiInstance.negotiableQuotePaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost(cartId, checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableCartsCartIdPaymentInformationApi#negotiableQuotePaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost");
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

