# PaymentLinksApi

All URIs are relative to *https://checkout-test.adyen.com/v64*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPaymentLinksLinkId**](PaymentLinksApi.md#getPaymentLinksLinkId) | **GET** /paymentLinks/{linkId} | Get a payment link |
| [**patchPaymentLinksLinkId**](PaymentLinksApi.md#patchPaymentLinksLinkId) | **PATCH** /paymentLinks/{linkId} | Update the status of a payment link |
| [**postPaymentLinks**](PaymentLinksApi.md#postPaymentLinks) | **POST** /paymentLinks | Create a payment link |


<a id="getPaymentLinksLinkId"></a>
# **getPaymentLinksLinkId**
> PaymentLinkResponse getPaymentLinksLinkId(linkId)

Get a payment link

Retrieves the payment link details using the payment link &#x60;id&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://checkout-test.adyen.com/v64");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PaymentLinksApi apiInstance = new PaymentLinksApi(defaultClient);
    String linkId = "linkId_example"; // String | Unique identifier of the payment link.
    try {
      PaymentLinkResponse result = apiInstance.getPaymentLinksLinkId(linkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentLinksApi#getPaymentLinksLinkId");
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
| **linkId** | **String**| Unique identifier of the payment link. | |

### Return type

[**PaymentLinkResponse**](PaymentLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

<a id="patchPaymentLinksLinkId"></a>
# **patchPaymentLinksLinkId**
> PaymentLinkResponse patchPaymentLinksLinkId(linkId, updatePaymentLinkRequest)

Update the status of a payment link

Updates the status of a payment link. Use this endpoint to [force the expiry of a payment link](https://docs.adyen.com/online-payments/pay-by-link#update-payment-link-status).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://checkout-test.adyen.com/v64");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PaymentLinksApi apiInstance = new PaymentLinksApi(defaultClient);
    String linkId = "linkId_example"; // String | Unique identifier of the payment link.
    UpdatePaymentLinkRequest updatePaymentLinkRequest = new UpdatePaymentLinkRequest(); // UpdatePaymentLinkRequest | 
    try {
      PaymentLinkResponse result = apiInstance.patchPaymentLinksLinkId(linkId, updatePaymentLinkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentLinksApi#patchPaymentLinksLinkId");
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
| **linkId** | **String**| Unique identifier of the payment link. | |
| **updatePaymentLinkRequest** | [**UpdatePaymentLinkRequest**](UpdatePaymentLinkRequest.md)|  | [optional] |

### Return type

[**PaymentLinkResponse**](PaymentLinkResponse.md)

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

<a id="postPaymentLinks"></a>
# **postPaymentLinks**
> PaymentLinkResponse postPaymentLinks(idempotencyKey, paymentLinkRequest)

Create a payment link

Creates a payment link to our hosted payment form where shoppers can pay. The list of payment methods presented to the shopper depends on the &#x60;currency&#x60; and &#x60;country&#x60; parameters sent in the request.  For more information, refer to [Pay by Link documentation](https://docs.adyen.com/online-payments/pay-by-link#create-payment-links-through-api).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://checkout-test.adyen.com/v64");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PaymentLinksApi apiInstance = new PaymentLinksApi(defaultClient);
    String idempotencyKey = "37ca9c97-d1d1-4c62-89e8-706891a563ed"; // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    PaymentLinkRequest paymentLinkRequest = new PaymentLinkRequest(); // PaymentLinkRequest | 
    try {
      PaymentLinkResponse result = apiInstance.postPaymentLinks(idempotencyKey, paymentLinkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentLinksApi#postPaymentLinks");
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
| **paymentLinkRequest** | [**PaymentLinkRequest**](PaymentLinkRequest.md)|  | [optional] |

### Return type

[**PaymentLinkResponse**](PaymentLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created - the request has succeeded. |  * Idempotency-Key -  <br>  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  * Idempotency-Key -  <br>  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

