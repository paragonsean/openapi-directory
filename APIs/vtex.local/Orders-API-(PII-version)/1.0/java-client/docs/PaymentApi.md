# PaymentApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sendPaymentNotification2**](PaymentApi.md#sendPaymentNotification2) | **POST** /api/orders/pvt/document/{orderId}/payment/{paymentId}/notify-payment | Send payment notification |


<a id="sendPaymentNotification2"></a>
# **sendPaymentNotification2**
> sendPaymentNotification2(contentType, accept, orderId, paymentId)

Send payment notification

Send a payment notification of a given order, by order ID and payment ID.    &gt; The &#x60;Notify payment&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).    &gt; Learn more about [Transaction Details](https://help.vtex.com/en/tutorial/how-to-view-the-orders-details).      ## Request body properties    | Attribute    | Type        | Description |  | --------------- |:---------:| --------------------------------------:|  | &#x60;orderId&#x60; | string | Order Id |  | &#x60;paymentId&#x60; | string | Payment ID |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    PaymentApi apiInstance = new PaymentApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderId = "70caf3941s6df1"; // String | ID of the order.
    String paymentId = "45hsfg5jkyu1384jdsfgh654sfgj1"; // String | ID of the payment.
    try {
      apiInstance.sendPaymentNotification2(contentType, accept, orderId, paymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentApi#sendPaymentNotification2");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **orderId** | **String**| ID of the order. | |
| **paymentId** | **String**| ID of the payment. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **429** | Too Many Requests |  -  |

