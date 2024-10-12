# GuestCartsCartIdSelectedPaymentMethodApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestPaymentMethodManagementV1GetGet**](GuestCartsCartIdSelectedPaymentMethodApi.md#quoteGuestPaymentMethodManagementV1GetGet) | **GET** /V1/guest-carts/{cartId}/selected-payment-method | guest-carts/{cartId}/selected-payment-method |
| [**quoteGuestPaymentMethodManagementV1SetPut**](GuestCartsCartIdSelectedPaymentMethodApi.md#quoteGuestPaymentMethodManagementV1SetPut) | **PUT** /V1/guest-carts/{cartId}/selected-payment-method | guest-carts/{cartId}/selected-payment-method |


<a id="quoteGuestPaymentMethodManagementV1GetGet"></a>
# **quoteGuestPaymentMethodManagementV1GetGet**
> QuoteDataPaymentInterface quoteGuestPaymentMethodManagementV1GetGet(cartId)

guest-carts/{cartId}/selected-payment-method

Return the payment method for a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdSelectedPaymentMethodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdSelectedPaymentMethodApi apiInstance = new GuestCartsCartIdSelectedPaymentMethodApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    try {
      QuoteDataPaymentInterface result = apiInstance.quoteGuestPaymentMethodManagementV1GetGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdSelectedPaymentMethodApi#quoteGuestPaymentMethodManagementV1GetGet");
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
| **cartId** | **String**| The cart ID. | |

### Return type

[**QuoteDataPaymentInterface**](QuoteDataPaymentInterface.md)

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

<a id="quoteGuestPaymentMethodManagementV1SetPut"></a>
# **quoteGuestPaymentMethodManagementV1SetPut**
> Integer quoteGuestPaymentMethodManagementV1SetPut(cartId, quotePaymentMethodManagementV1SetPutRequest)

guest-carts/{cartId}/selected-payment-method

Add a specified payment method to a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdSelectedPaymentMethodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdSelectedPaymentMethodApi apiInstance = new GuestCartsCartIdSelectedPaymentMethodApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    QuotePaymentMethodManagementV1SetPutRequest quotePaymentMethodManagementV1SetPutRequest = new QuotePaymentMethodManagementV1SetPutRequest(); // QuotePaymentMethodManagementV1SetPutRequest | 
    try {
      Integer result = apiInstance.quoteGuestPaymentMethodManagementV1SetPut(cartId, quotePaymentMethodManagementV1SetPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdSelectedPaymentMethodApi#quoteGuestPaymentMethodManagementV1SetPut");
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
| **cartId** | **String**| The cart ID. | |
| **quotePaymentMethodManagementV1SetPutRequest** | [**QuotePaymentMethodManagementV1SetPutRequest**](QuotePaymentMethodManagementV1SetPutRequest.md)|  | [optional] |

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

