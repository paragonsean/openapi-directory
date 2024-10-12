# OrdersApi

All URIs are relative to *https://checkout-test.adyen.com/v66*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postOrders**](OrdersApi.md#postOrders) | **POST** /orders | Create an order |
| [**postOrdersCancel**](OrdersApi.md#postOrdersCancel) | **POST** /orders/cancel | Cancel an order |
| [**postPaymentMethodsBalance**](OrdersApi.md#postPaymentMethodsBalance) | **POST** /paymentMethods/balance | Get the balance of a gift card |


<a id="postOrders"></a>
# **postOrders**
> CreateOrderResponse postOrders(idempotencyKey, createOrderRequest)

Create an order

Creates an order to be used for partial payments. Make a POST &#x60;/orders&#x60; call before making a &#x60;/payments&#x60; call when processing payments with different payment methods.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://checkout-test.adyen.com/v66");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String idempotencyKey = "37ca9c97-d1d1-4c62-89e8-706891a563ed"; // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    CreateOrderRequest createOrderRequest = new CreateOrderRequest(); // CreateOrderRequest | 
    try {
      CreateOrderResponse result = apiInstance.postOrders(idempotencyKey, createOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#postOrders");
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
| **createOrderRequest** | [**CreateOrderRequest**](CreateOrderRequest.md)|  | [optional] |

### Return type

[**CreateOrderResponse**](CreateOrderResponse.md)

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

<a id="postOrdersCancel"></a>
# **postOrdersCancel**
> CancelOrderResponse postOrdersCancel(idempotencyKey, cancelOrderRequest)

Cancel an order

Cancels an order. Cancellation of an order results in an automatic rollback of all payments made in the order, either by canceling or refunding the payment, depending on the type of payment method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://checkout-test.adyen.com/v66");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String idempotencyKey = "37ca9c97-d1d1-4c62-89e8-706891a563ed"; // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    CancelOrderRequest cancelOrderRequest = new CancelOrderRequest(); // CancelOrderRequest | 
    try {
      CancelOrderResponse result = apiInstance.postOrdersCancel(idempotencyKey, cancelOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#postOrdersCancel");
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
| **cancelOrderRequest** | [**CancelOrderRequest**](CancelOrderRequest.md)|  | [optional] |

### Return type

[**CancelOrderResponse**](CancelOrderResponse.md)

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

<a id="postPaymentMethodsBalance"></a>
# **postPaymentMethodsBalance**
> BalanceCheckResponse postPaymentMethodsBalance(idempotencyKey, balanceCheckRequest)

Get the balance of a gift card

Retrieves the balance remaining on a shopper&#39;s gift card. To check a gift card&#39;s balance, make a POST &#x60;/paymentMethods/balance&#x60; call and include the gift card&#39;s details inside a &#x60;paymentMethod&#x60; object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://checkout-test.adyen.com/v66");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String idempotencyKey = "37ca9c97-d1d1-4c62-89e8-706891a563ed"; // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    BalanceCheckRequest balanceCheckRequest = new BalanceCheckRequest(); // BalanceCheckRequest | 
    try {
      BalanceCheckResponse result = apiInstance.postPaymentMethodsBalance(idempotencyKey, balanceCheckRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#postPaymentMethodsBalance");
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
| **balanceCheckRequest** | [**BalanceCheckRequest**](BalanceCheckRequest.md)|  | [optional] |

### Return type

[**BalanceCheckResponse**](BalanceCheckResponse.md)

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

