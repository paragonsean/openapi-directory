# PaymentAuthorisationRefundOrFundsTransferInitiatedApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postBalancePlatformPaymentCreated**](PaymentAuthorisationRefundOrFundsTransferInitiatedApi.md#postBalancePlatformPaymentCreated) | **POST** /balancePlatform.payment.created | Payment authorisation, refund, or funds transfer initiated |
| [**postBalancePlatformPaymentUpdated**](PaymentAuthorisationRefundOrFundsTransferInitiatedApi.md#postBalancePlatformPaymentUpdated) | **POST** /balancePlatform.payment.updated | Payment authorisation expired or cancelled |


<a id="postBalancePlatformPaymentCreated"></a>
# **postBalancePlatformPaymentCreated**
> BalancePlatformNotificationResponse postBalancePlatformPaymentCreated(paymentNotificationRequest)

Payment authorisation, refund, or funds transfer initiated

Adyen sends this webhook when a payment authorisation, a refund, or a funds transfer has been initiated. This webhook only informs your server of requests. For the actual fund movements, you&#39;ll get the information from the subsequent outgoing or incoming transfer webhooks.   To differentiate the requests, check the content of the webhook.  * For payments, the webhook contains the authorisation result, information about the processing merchant, and shows a negative amount.   * For refunds, the webhook contains to which payment instrument the funds will be refunded, and shows a positive amount.  * For outgoing or incoming fund transfers, the webhook shows a positive or negative amount depending on the direction of the transfer, and only includes information about the balance account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuthorisationRefundOrFundsTransferInitiatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    PaymentAuthorisationRefundOrFundsTransferInitiatedApi apiInstance = new PaymentAuthorisationRefundOrFundsTransferInitiatedApi(defaultClient);
    PaymentNotificationRequest paymentNotificationRequest = new PaymentNotificationRequest(); // PaymentNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformPaymentCreated(paymentNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuthorisationRefundOrFundsTransferInitiatedApi#postBalancePlatformPaymentCreated");
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

<a id="postBalancePlatformPaymentUpdated"></a>
# **postBalancePlatformPaymentUpdated**
> BalancePlatformNotificationResponse postBalancePlatformPaymentUpdated(paymentNotificationRequest)

Payment authorisation expired or cancelled

Adyen sends this webhook when a payment authorisation has expired or has been cancelled. Use the &#x60;data.id&#x60; to track the original payment authorisation from the &#x60;balancePlatform.payment.created&#x60; webhook.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuthorisationRefundOrFundsTransferInitiatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    PaymentAuthorisationRefundOrFundsTransferInitiatedApi apiInstance = new PaymentAuthorisationRefundOrFundsTransferInitiatedApi(defaultClient);
    PaymentNotificationRequest paymentNotificationRequest = new PaymentNotificationRequest(); // PaymentNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformPaymentUpdated(paymentNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuthorisationRefundOrFundsTransferInitiatedApi#postBalancePlatformPaymentUpdated");
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

