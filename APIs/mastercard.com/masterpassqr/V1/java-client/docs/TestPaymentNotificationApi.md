# TestPaymentNotificationApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sendNotificationPaymentRetry**](TestPaymentNotificationApi.md#sendNotificationPaymentRetry) | **POST** /send/v1/partners/{partnerId}/events/generate/payment | Client can simulate a Mastercard Merchant Presented QR Payment notification to the registered URL endpoint.  |


<a id="sendNotificationPaymentRetry"></a>
# **sendNotificationPaymentRetry**
> NotificationResponse162Wrapper sendNotificationPaymentRetry(partnerId, notificationRequest)

Client can simulate a Mastercard Merchant Presented QR Payment notification to the registered URL endpoint. 

Client can simulate a Mastercard Merchant Presented QR Payment notification to the registered URL endpoint. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestPaymentNotificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    TestPaymentNotificationApi apiInstance = new TestPaymentNotificationApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
    NotificationRequest159Wrapper notificationRequest = new NotificationRequest159Wrapper(); // NotificationRequest159Wrapper | Contains the details of the request message.
    try {
      NotificationResponse162Wrapper result = apiInstance.sendNotificationPaymentRetry(partnerId, notificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestPaymentNotificationApi#sendNotificationPaymentRetry");
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
| **partnerId** | **String**| Path Param - Provider assigned partner id. Details - string, 32 | |
| **notificationRequest** | [**NotificationRequest159Wrapper**](NotificationRequest159Wrapper.md)| Contains the details of the request message. | [optional] |

### Return type

[**NotificationResponse162Wrapper**](NotificationResponse162Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: N/A

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains the details of the response message. |  -  |

