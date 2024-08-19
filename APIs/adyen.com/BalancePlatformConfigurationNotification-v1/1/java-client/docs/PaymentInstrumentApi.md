# PaymentInstrumentApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postBalancePlatformPaymentInstrumentCreated**](PaymentInstrumentApi.md#postBalancePlatformPaymentInstrumentCreated) | **POST** /balancePlatform.paymentInstrument.created | Payment instrument created |
| [**postBalancePlatformPaymentInstrumentUpdated**](PaymentInstrumentApi.md#postBalancePlatformPaymentInstrumentUpdated) | **POST** /balancePlatform.paymentInstrument.updated | Payment instrument updated |


<a id="postBalancePlatformPaymentInstrumentCreated"></a>
# **postBalancePlatformPaymentInstrumentCreated**
> BalancePlatformNotificationResponse postBalancePlatformPaymentInstrumentCreated(paymentNotificationRequest)

Payment instrument created

Adyen sends this webhook when you successfully [create a payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments).  &gt;The webhook does not include the card number when creating virtual cards. You can only get the card number in the response of the POST [/paymentInstruments](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments#responses-200-card-number) request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInstrumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    PaymentInstrumentApi apiInstance = new PaymentInstrumentApi(defaultClient);
    PaymentNotificationRequest paymentNotificationRequest = new PaymentNotificationRequest(); // PaymentNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformPaymentInstrumentCreated(paymentNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInstrumentApi#postBalancePlatformPaymentInstrumentCreated");
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
| **paymentNotificationRequest** | [**PaymentNotificationRequest**](PaymentNotificationRequest.md)|  | [optional] |

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postBalancePlatformPaymentInstrumentUpdated"></a>
# **postBalancePlatformPaymentInstrumentUpdated**
> BalancePlatformNotificationResponse postBalancePlatformPaymentInstrumentUpdated(paymentNotificationRequest)

Payment instrument updated

Adyen sends this webhook when you successfully [update a payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/paymentInstruments/_id_). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInstrumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    PaymentInstrumentApi apiInstance = new PaymentInstrumentApi(defaultClient);
    PaymentNotificationRequest paymentNotificationRequest = new PaymentNotificationRequest(); // PaymentNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformPaymentInstrumentUpdated(paymentNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInstrumentApi#postBalancePlatformPaymentInstrumentUpdated");
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
| **paymentNotificationRequest** | [**PaymentNotificationRequest**](PaymentNotificationRequest.md)|  | [optional] |

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

