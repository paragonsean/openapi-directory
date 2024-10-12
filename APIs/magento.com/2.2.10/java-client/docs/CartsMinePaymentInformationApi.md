# CartsMinePaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkoutPaymentInformationManagementV1GetPaymentInformationGet**](CartsMinePaymentInformationApi.md#checkoutPaymentInformationManagementV1GetPaymentInformationGet) | **GET** /V1/carts/mine/payment-information | carts/mine/payment-information |
| [**checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost**](CartsMinePaymentInformationApi.md#checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost) | **POST** /V1/carts/mine/payment-information | carts/mine/payment-information |


<a id="checkoutPaymentInformationManagementV1GetPaymentInformationGet"></a>
# **checkoutPaymentInformationManagementV1GetPaymentInformationGet**
> CheckoutDataPaymentDetailsInterface checkoutPaymentInformationManagementV1GetPaymentInformationGet()

carts/mine/payment-information

Get payment information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMinePaymentInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMinePaymentInformationApi apiInstance = new CartsMinePaymentInformationApi(defaultClient);
    try {
      CheckoutDataPaymentDetailsInterface result = apiInstance.checkoutPaymentInformationManagementV1GetPaymentInformationGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMinePaymentInformationApi#checkoutPaymentInformationManagementV1GetPaymentInformationGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost"></a>
# **checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost**
> Integer checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost(checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest)

carts/mine/payment-information

Set payment information and place order for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMinePaymentInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMinePaymentInformationApi apiInstance = new CartsMinePaymentInformationApi(defaultClient);
    CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest = new CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest(); // CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
    try {
      Integer result = apiInstance.checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost(checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMinePaymentInformationApi#checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost");
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

