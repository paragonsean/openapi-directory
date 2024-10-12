# PaymentsApi

All URIs are relative to *https://checkout-test.adyen.com/v65*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postCardDetails**](PaymentsApi.md#postCardDetails) | **POST** /cardDetails | Get the list of brands on the card |
| [**postPaymentMethods**](PaymentsApi.md#postPaymentMethods) | **POST** /paymentMethods | Get a list of available payment methods |
| [**postPayments**](PaymentsApi.md#postPayments) | **POST** /payments | Start a transaction |
| [**postPaymentsDetails**](PaymentsApi.md#postPaymentsDetails) | **POST** /payments/details | Submit details for a payment |


<a id="postCardDetails"></a>
# **postCardDetails**
> CardDetailsResponse postCardDetails(idempotencyKey, cardDetailsRequest)

Get the list of brands on the card

Send a request with at least the first 6 digits of the card number to get a response with an array of brands on the card. If you include [your supported brands](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cardDetails__reqParam_supportedBrands) in the request, the response also tells you if you support each [brand that was identified](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cardDetails__resParam_details).  If you have an API-only integration and collect card data, use this endpoint to find out if the shopper&#39;s card is co-branded. For co-branded cards, you must let the shopper choose the brand to pay with  if you support both brands.  

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
    defaultClient.setBasePath("https://checkout-test.adyen.com/v65");
    
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
    String idempotencyKey = "37ca9c97-d1d1-4c62-89e8-706891a563ed"; // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    CardDetailsRequest cardDetailsRequest = new CardDetailsRequest(); // CardDetailsRequest | 
    try {
      CardDetailsResponse result = apiInstance.postCardDetails(idempotencyKey, cardDetailsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#postCardDetails");
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
| **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] |
| **cardDetailsRequest** | [**CardDetailsRequest**](CardDetailsRequest.md)|  | [optional] |

### Return type

[**CardDetailsResponse**](CardDetailsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  * Idempotency-Key -  <br>  |

<a id="postPaymentMethods"></a>
# **postPaymentMethods**
> PaymentMethodsResponse postPaymentMethods(idempotencyKey, paymentMethodsRequest)

Get a list of available payment methods

Queries the available payment methods for a transaction based on the transaction context (like amount, country, and currency). Besides giving back a list of the available payment methods, the response also returns which input details you need to collect from the shopper (to be submitted to &#x60;/payments&#x60;).  Although we highly recommend using this endpoint to ensure you are always offering the most up-to-date list of payment methods, its usage is optional. You can, for example, also cache the &#x60;/paymentMethods&#x60; response and update it once a week.

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
    defaultClient.setBasePath("https://checkout-test.adyen.com/v65");
    
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
    String idempotencyKey = "37ca9c97-d1d1-4c62-89e8-706891a563ed"; // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    PaymentMethodsRequest paymentMethodsRequest = new PaymentMethodsRequest(); // PaymentMethodsRequest | 
    try {
      PaymentMethodsResponse result = apiInstance.postPaymentMethods(idempotencyKey, paymentMethodsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#postPaymentMethods");
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
| **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] |
| **paymentMethodsRequest** | [**PaymentMethodsRequest**](PaymentMethodsRequest.md)|  | [optional] |

### Return type

[**PaymentMethodsResponse**](PaymentMethodsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  * Idempotency-Key -  <br>  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  * Idempotency-Key -  <br>  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postPayments"></a>
# **postPayments**
> PaymentResponse postPayments(idempotencyKey, paymentRequest)

Start a transaction

Sends payment parameters (like amount, country, and currency) together with other required input details collected from the shopper. To know more about required parameters for specific payment methods, refer to our [payment method guides](https://docs.adyen.com/payment-methods).  The response depends on the [payment flow](https://docs.adyen.com/payment-methods#payment-flow): * For a direct flow, the response includes a &#x60;pspReference&#x60; and a &#x60;resultCode&#x60; with the payment result, for example **Authorised** or **Refused**.  * For a redirect or additional action, the response contains an &#x60;action&#x60; object. 

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
    defaultClient.setBasePath("https://checkout-test.adyen.com/v65");
    
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
    String idempotencyKey = "37ca9c97-d1d1-4c62-89e8-706891a563ed"; // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    PaymentRequest paymentRequest = new PaymentRequest(); // PaymentRequest | 
    try {
      PaymentResponse result = apiInstance.postPayments(idempotencyKey, paymentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#postPayments");
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
| **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] |
| **paymentRequest** | [**PaymentRequest**](PaymentRequest.md)|  | [optional] |

### Return type

[**PaymentResponse**](PaymentResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  * Idempotency-Key -  <br>  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  * Idempotency-Key -  <br>  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postPaymentsDetails"></a>
# **postPaymentsDetails**
> PaymentDetailsResponse postPaymentsDetails(idempotencyKey, paymentDetailsRequest)

Submit details for a payment

Submits details for a payment created using &#x60;/payments&#x60;. This step is only needed when no final state has been reached on the &#x60;/payments&#x60; request, for example when the shopper was redirected to another page to complete the payment.  

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
    defaultClient.setBasePath("https://checkout-test.adyen.com/v65");
    
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
    String idempotencyKey = "37ca9c97-d1d1-4c62-89e8-706891a563ed"; // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    PaymentDetailsRequest paymentDetailsRequest = new PaymentDetailsRequest(); // PaymentDetailsRequest | 
    try {
      PaymentDetailsResponse result = apiInstance.postPaymentsDetails(idempotencyKey, paymentDetailsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#postPaymentsDetails");
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
| **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] |
| **paymentDetailsRequest** | [**PaymentDetailsRequest**](PaymentDetailsRequest.md)|  | [optional] |

### Return type

[**PaymentDetailsResponse**](PaymentDetailsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  * Idempotency-Key -  <br>  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  * Idempotency-Key -  <br>  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

