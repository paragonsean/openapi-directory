# PaymentsApi

All URIs are relative to *https://www.beanstream.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsPost**](PaymentsApi.md#paymentsPost) | **POST** /payments | Make Payment |
| [**paymentsTransIdCompletionsPost**](PaymentsApi.md#paymentsTransIdCompletionsPost) | **POST** /payments/{transId}/completions | Complete pre-auth |
| [**paymentsTransIdGet**](PaymentsApi.md#paymentsTransIdGet) | **GET** /payments/{transId} | Get payment |
| [**paymentsTransIdReturnsPost**](PaymentsApi.md#paymentsTransIdReturnsPost) | **POST** /payments/{transId}/returns | Return payment |
| [**paymentsTransIdVoidPost**](PaymentsApi.md#paymentsTransIdVoidPost) | **POST** /payments/{transId}/void | Void Transaction |


<a id="paymentsPost"></a>
# **paymentsPost**
> PaymentResponse paymentsPost(paymentRequest)

Make Payment

Make a payment using credit card, cash, cheque, profile, or token. Each payment type has its own json definition passed in the body. For all payments you have the standard Billing, Shipping, Comments, etc. fields that are optional. Only the amount is required along with the payment data for card, cash, cheque, profile, and token. You must change the payment_method for each payment type. Credit Card - \&quot;card\&quot;, Payment Profile - \&quot;payment_profile\&quot;, Legato Token - \&quot;token\&quot;, Cash - \&quot;cash\&quot;, Cheque - \&quot;cheque\&quot;, Interac - \&quot;interac\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    PaymentRequest paymentRequest = new PaymentRequest(); // PaymentRequest | 
    try {
      PaymentResponse result = apiInstance.paymentsPost(paymentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsPost");
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

[**PaymentResponse**](PaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payment response containing the payment details as well as if the payment was approved or declined. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

<a id="paymentsTransIdCompletionsPost"></a>
# **paymentsTransIdCompletionsPost**
> PaymentResponse paymentsTransIdCompletionsPost(transId, paymentRequest)

Complete pre-auth

Complete a pre-authorized payment. The amount of the transaction to complete must be less than or equal to the original pre-auth amount. Complete must be set to true.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    Double transId = 3.4D; // Double | The transaction id.
    PaymentRequest paymentRequest = new PaymentRequest(); // PaymentRequest | 
    try {
      PaymentResponse result = apiInstance.paymentsTransIdCompletionsPost(transId, paymentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsTransIdCompletionsPost");
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
| **transId** | **Double**| The transaction id. | |
| **paymentRequest** | [**PaymentRequest**](PaymentRequest.md)|  | [optional] |

### Return type

[**PaymentResponse**](PaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payment response containing the payment details as well as if the transaction was approved or declined. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

<a id="paymentsTransIdGet"></a>
# **paymentsTransIdGet**
> Transaction paymentsTransIdGet(transId)

Get payment

Get a previous payment (transaction).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    BigDecimal transId = new BigDecimal(78); // BigDecimal | The transaction id.
    try {
      Transaction result = apiInstance.paymentsTransIdGet(transId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsTransIdGet");
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
| **transId** | **BigDecimal**| The transaction id. | |

### Return type

[**Transaction**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A transaction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

<a id="paymentsTransIdReturnsPost"></a>
# **paymentsTransIdReturnsPost**
> PaymentResponse paymentsTransIdReturnsPost(transId, _return)

Return payment

Return payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    Double transId = 3.4D; // Double | The transaction id.
    ModelReturn _return = new ModelReturn(); // ModelReturn | 
    try {
      PaymentResponse result = apiInstance.paymentsTransIdReturnsPost(transId, _return);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsTransIdReturnsPost");
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
| **transId** | **Double**| The transaction id. | |
| **_return** | [**ModelReturn**](ModelReturn.md)|  | |

### Return type

[**PaymentResponse**](PaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payment response containing the payment details as well as if the transaction was approved or declined. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

<a id="paymentsTransIdVoidPost"></a>
# **paymentsTransIdVoidPost**
> PaymentResponse paymentsTransIdVoidPost(transId, _void)

Void Transaction

Void a transaction. You can void payments, returns, pre-auths, and completions. It will cancel that transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    Double transId = 3.4D; // Double | The transaction id to void.
    ModelVoid _void = new ModelVoid(); // ModelVoid | 
    try {
      PaymentResponse result = apiInstance.paymentsTransIdVoidPost(transId, _void);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsTransIdVoidPost");
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
| **transId** | **Double**| The transaction id to void. | |
| **_void** | [**ModelVoid**](ModelVoid.md)|  | |

### Return type

[**PaymentResponse**](PaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payment response containing the payment details as well as if the transaction was approved or declined. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

