# PaymentsApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/Payment/v25*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postAuthorise**](PaymentsApi.md#postAuthorise) | **POST** /authorise | Create an authorisation |
| [**postAuthorise3d**](PaymentsApi.md#postAuthorise3d) | **POST** /authorise3d | Complete a 3DS authorisation |


<a id="postAuthorise"></a>
# **postAuthorise**
> PaymentResult postAuthorise(paymentRequest)

Create an authorisation

Creates a payment with a unique reference (&#x60;pspReference&#x60;) and attempts to obtain an authorisation hold. For cards, this amount can be captured or cancelled later. Non-card payment methods typically don&#39;t support this and will automatically capture as part of the authorisation. &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments) endpoint under Checkout API instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pal-test.adyen.com/pal/servlet/Payment/v25");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    PaymentRequest paymentRequest = new PaymentRequest(); // PaymentRequest | 
    try {
      PaymentResult result = apiInstance.postAuthorise(paymentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#postAuthorise");
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
| **paymentRequest** | [**PaymentRequest**](PaymentRequest.md)|  | [optional] |

### Return type

[**PaymentResult**](PaymentResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postAuthorise3d"></a>
# **postAuthorise3d**
> PaymentResult postAuthorise3d(paymentRequest3d)

Complete a 3DS authorisation

For an authenticated 3D Secure session, completes the payment authorisation. This endpoint must receive the &#x60;md&#x60; and &#x60;paResponse&#x60; parameters that you get from the card issuer after a shopper pays via 3D Secure.  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce/3d-secure). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/details&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments/details) endpoint under Checkout API instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pal-test.adyen.com/pal/servlet/Payment/v25");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    PaymentRequest3d paymentRequest3d = new PaymentRequest3d(); // PaymentRequest3d | 
    try {
      PaymentResult result = apiInstance.postAuthorise3d(paymentRequest3d);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#postAuthorise3d");
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
| **paymentRequest3d** | [**PaymentRequest3d**](PaymentRequest3d.md)|  | [optional] |

### Return type

[**PaymentResult**](PaymentResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

