# PaymentGatewayApi

All URIs are relative to *http://api-test.qualpay.com/pg*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authorization**](PaymentGatewayApi.md#authorization) | **POST** /auth | Authorize Transaction |
| [**batchClose**](PaymentGatewayApi.md#batchClose) | **POST** /batchClose | Close Batch |
| [**callVoid**](PaymentGatewayApi.md#callVoid) | **POST** /void/{pgIdOrig} | Void a Previously Authorized Transaction |
| [**capture**](PaymentGatewayApi.md#capture) | **POST** /capture/{pgIdOrig} | Capture an Authorized Transaction |
| [**credit**](PaymentGatewayApi.md#credit) | **POST** /credit | Issue Credit to Cardholder |
| [**expire**](PaymentGatewayApi.md#expire) | **POST** /expireToken | Expire Token |
| [**force**](PaymentGatewayApi.md#force) | **POST** /force | Force Transaction Approval |
| [**getCardTypeInformation**](PaymentGatewayApi.md#getCardTypeInformation) | **POST** /ardef | Get Card type Information for Visa, Mastercard, and Discover |
| [**recharge**](PaymentGatewayApi.md#recharge) | **POST** /recharge/{pgIdOrig} | Recharge Previously Settled Transaction |
| [**refund**](PaymentGatewayApi.md#refund) | **POST** /refund/{pgIdOrig} | Refund Previously Captured Transaction |
| [**sale**](PaymentGatewayApi.md#sale) | **POST** /sale | Sale (Auth + Capture) |
| [**sendReceipt**](PaymentGatewayApi.md#sendReceipt) | **POST** /emailReceipt/{pgId} | Send Transaction Receipt Email |
| [**tokenize**](PaymentGatewayApi.md#tokenize) | **POST** /tokenize | Tokenize Card |
| [**verify**](PaymentGatewayApi.md#verify) | **POST** /verify | Verify Card |


<a id="authorization"></a>
# **authorization**
> PGApiTransactionResponse authorization(body)

Authorize Transaction

Authorizes a credit card for capture at a later time. An authorized transaction will continue to be open until it expires or a capture message is received. Authorizations are automatically voided if they are not captured within 28 days, although most issuing banks will release the hold after 24 hours in retail environments or 7 days in card not present environments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    PGApiTransactionRequest body = new PGApiTransactionRequest(); // PGApiTransactionRequest | Payment Gateway Authorization Request
    try {
      PGApiTransactionResponse result = apiInstance.authorization(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#authorization");
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
| **body** | [**PGApiTransactionRequest**](PGApiTransactionRequest.md)| Payment Gateway Authorization Request | |

### Return type

[**PGApiTransactionResponse**](PGApiTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="batchClose"></a>
# **batchClose**
> PGApiBatchCloseResponse batchClose(body)

Close Batch

Closes a batch. Use this request when the timing of the batch close needs to be controlled rather than relying on the once-daily automatic batch close which is 9 PM Pacific by default, and can be changed in the Qualpay Manager administration settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    PGApiBatchCloseRequest body = new PGApiBatchCloseRequest(); // PGApiBatchCloseRequest | Payment Gateway Batch Close Request
    try {
      PGApiBatchCloseResponse result = apiInstance.batchClose(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#batchClose");
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
| **body** | [**PGApiBatchCloseRequest**](PGApiBatchCloseRequest.md)| Payment Gateway Batch Close Request | |

### Return type

[**PGApiBatchCloseResponse**](PGApiBatchCloseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="callVoid"></a>
# **callVoid**
> PGApiVoidResponse callVoid(pgIdOrig, body)

Void a Previously Authorized Transaction

Authorizations can be voided at any time until Qualpay automatically voids them at 28 days. Captured transactions can be voided until the batch is closed. If your batch closes and you did not void the transaction in time, you may make a refund request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    String pgIdOrig = "pgIdOrig_example"; // String | pgIdOrig
    PGApiVoidRequest body = new PGApiVoidRequest(); // PGApiVoidRequest | Payment Gateway Void Request
    try {
      PGApiVoidResponse result = apiInstance.callVoid(pgIdOrig, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#callVoid");
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
| **pgIdOrig** | **String**| pgIdOrig | |
| **body** | [**PGApiVoidRequest**](PGApiVoidRequest.md)| Payment Gateway Void Request | |

### Return type

[**PGApiVoidResponse**](PGApiVoidResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="capture"></a>
# **capture**
> PGApiCaptureResponse capture(pgIdOrig, body)

Capture an Authorized Transaction

Captures an authorized transaction for any amount up to the amount originally authorized. An authorized transaction can only be captured once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    String pgIdOrig = "pgIdOrig_example"; // String | pgIdOrig
    PGApiCaptureRequest body = new PGApiCaptureRequest(); // PGApiCaptureRequest | Payment Gateway Capture Request
    try {
      PGApiCaptureResponse result = apiInstance.capture(pgIdOrig, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#capture");
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
| **pgIdOrig** | **String**| pgIdOrig | |
| **body** | [**PGApiCaptureRequest**](PGApiCaptureRequest.md)| Payment Gateway Capture Request | |

### Return type

[**PGApiCaptureResponse**](PGApiCaptureResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="credit"></a>
# **credit**
> PGApiTransactionResponse credit(body)

Issue Credit to Cardholder

Issues an unlinked credit. Credit requests require that the cardholder data is  provided in the request. Credits are only available during the first 30 days of account opening unless you contact Qualpay support to make other arrangements. The refund request should generally be used to return money to the cardholder, as it is a reversal of a previously captured transaction. A refund request is linked to the original transaction which is helpful for reconciliation purposes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    PGApiTransactionRequest body = new PGApiTransactionRequest(); // PGApiTransactionRequest | Payment Gateway Credit Request
    try {
      PGApiTransactionResponse result = apiInstance.credit(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#credit");
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
| **body** | [**PGApiTransactionRequest**](PGApiTransactionRequest.md)| Payment Gateway Credit Request | |

### Return type

[**PGApiTransactionResponse**](PGApiTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="expire"></a>
# **expire**
> PGApiExpireTokenResponse expire(body)

Expire Token

Once expired, the token (card_id) is no longer valid for use in future transactions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    PGApiExpireTokenRequest body = new PGApiExpireTokenRequest(); // PGApiExpireTokenRequest | Payment Gateway Expire Token Request
    try {
      PGApiExpireTokenResponse result = apiInstance.expire(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#expire");
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
| **body** | [**PGApiExpireTokenRequest**](PGApiExpireTokenRequest.md)| Payment Gateway Expire Token Request | |

### Return type

[**PGApiExpireTokenResponse**](PGApiExpireTokenResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="force"></a>
# **force**
> PGApiTransactionResponse force(body)

Force Transaction Approval

Forces an approval, used when an online authorization request received a &#39;declined&#39; reason code and you have received an authorization from a voice or automated response (ARU) system. The required fields are the same as a sale or authorization request, except that the expiration date (exp_date) is not required, and the 6-character authorization code (auth_code) is required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    PGApiTransactionRequest body = new PGApiTransactionRequest(); // PGApiTransactionRequest | Payment Gateway Force Request
    try {
      PGApiTransactionResponse result = apiInstance.force(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#force");
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
| **body** | [**PGApiTransactionRequest**](PGApiTransactionRequest.md)| Payment Gateway Force Request | |

### Return type

[**PGApiTransactionResponse**](PGApiTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="getCardTypeInformation"></a>
# **getCardTypeInformation**
> ArdefResponse getCardTypeInformation(body)

Get Card type Information for Visa, Mastercard, and Discover

Gets Card type information for Visa, Mastercard, and Discover. Useful if you prohibit or allow certain activity based on card type. For example, you may not want to allow a subscription to be created using a prepaid card.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    ArdefRequest body = new ArdefRequest(); // ArdefRequest | Card Type Request
    try {
      ArdefResponse result = apiInstance.getCardTypeInformation(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#getCardTypeInformation");
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
| **body** | [**ArdefRequest**](ArdefRequest.md)| Card Type Request | |

### Return type

[**ArdefResponse**](ArdefResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="recharge"></a>
# **recharge**
> PGApiRechargeResponse recharge(pgIdOrig, body)

Recharge Previously Settled Transaction

Creates a new sale transaction using the cardholder data from a previous successful transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    String pgIdOrig = "pgIdOrig_example"; // String | pgIdOrig
    PGApiRechargeRequest body = new PGApiRechargeRequest(); // PGApiRechargeRequest | Payment Gateway Recharge Request
    try {
      PGApiRechargeResponse result = apiInstance.recharge(pgIdOrig, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#recharge");
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
| **pgIdOrig** | **String**| pgIdOrig | |
| **body** | [**PGApiRechargeRequest**](PGApiRechargeRequest.md)| Payment Gateway Recharge Request | |

### Return type

[**PGApiRechargeResponse**](PGApiRechargeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="refund"></a>
# **refund**
> PGApiRefundResponse refund(pgIdOrig, body)

Refund Previously Captured Transaction

Returns money to the cardholder from a previously captured transaction. Multiple refunds are allowed per captured transaction, provided that the sum of all refunds does not exceed the original captured transaction amount. Authorizations that have not been captured are not eligible for a refund.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    String pgIdOrig = "pgIdOrig_example"; // String | pgIdOrig
    PGApiRefundRequest body = new PGApiRefundRequest(); // PGApiRefundRequest | Payment Gateway Refund Request
    try {
      PGApiRefundResponse result = apiInstance.refund(pgIdOrig, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#refund");
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
| **pgIdOrig** | **String**| pgIdOrig | |
| **body** | [**PGApiRefundRequest**](PGApiRefundRequest.md)| Payment Gateway Refund Request | |

### Return type

[**PGApiRefundResponse**](PGApiRefundResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="sale"></a>
# **sale**
> PGApiTransactionResponse sale(body)

Sale (Auth + Capture)

Requests authorization, and, if approved, will immediately capture the transaction to be included in the next batch close. This transaction type is used in card-present environments, and also card-not-present environments where no physical goods are being shipped.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    PGApiTransactionRequest body = new PGApiTransactionRequest(); // PGApiTransactionRequest | Payment Gateway Sale Request
    try {
      PGApiTransactionResponse result = apiInstance.sale(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#sale");
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
| **body** | [**PGApiTransactionRequest**](PGApiTransactionRequest.md)| Payment Gateway Sale Request | |

### Return type

[**PGApiTransactionResponse**](PGApiTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="sendReceipt"></a>
# **sendReceipt**
> PGApiEmailReceiptResponse sendReceipt(pgId, body)

Send Transaction Receipt Email

Sends the transaction receipt to multiple email addresses. Receipts can be sent only for successful transactions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    String pgId = "pgId_example"; // String | pgId
    PGApiEmailReceiptRequest body = new PGApiEmailReceiptRequest(); // PGApiEmailReceiptRequest | Payment Gateway Email Receipt Request
    try {
      PGApiEmailReceiptResponse result = apiInstance.sendReceipt(pgId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#sendReceipt");
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
| **pgId** | **String**| pgId | |
| **body** | [**PGApiEmailReceiptRequest**](PGApiEmailReceiptRequest.md)| Payment Gateway Email Receipt Request | |

### Return type

[**PGApiEmailReceiptResponse**](PGApiEmailReceiptResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="tokenize"></a>
# **tokenize**
> PGApiTokenizeResponse tokenize(body)

Tokenize Card

Once stored, a unique card_id is returned for use in future transactions. Optionally, tokenization can be requested in an authorization, verify, force, credit, or sale request by sending the tokenize field set to true.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    PGApiTokenizeRequest body = new PGApiTokenizeRequest(); // PGApiTokenizeRequest | Payment Gateway Tokenize Request
    try {
      PGApiTokenizeResponse result = apiInstance.tokenize(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#tokenize");
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
| **body** | [**PGApiTokenizeRequest**](PGApiTokenizeRequest.md)| Payment Gateway Tokenize Request | |

### Return type

[**PGApiTokenizeResponse**](PGApiTokenizeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

<a id="verify"></a>
# **verify**
> PGApiVerifyResponse verify(body)

Verify Card

A verify request will return success if the cardholder information was verified by the issuer. If AVS or CVV data is included in the message, then the AVS or CVV result code will be returned in the response message. This is useful if you want to determine if you have been presented with a valid card, but are not ready to authorize the card.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentGatewayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-test.qualpay.com/pg");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentGatewayApi apiInstance = new PaymentGatewayApi(defaultClient);
    PGApiVerifyRequest body = new PGApiVerifyRequest(); // PGApiVerifyRequest | Payment Gateway Card Verify Request
    try {
      PGApiVerifyResponse result = apiInstance.verify(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentGatewayApi#verify");
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
| **body** | [**PGApiVerifyRequest**](PGApiVerifyRequest.md)| Payment Gateway Card Verify Request | |

### Return type

[**PGApiVerifyResponse**](PGApiVerifyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Declined |  -  |
| **500** | Internal Server Error |  -  |
| **509** | Timeout |  -  |

