# TestRefundNotificationApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sendNotificationRefundRetry**](TestRefundNotificationApi.md#sendNotificationRefundRetry) | **POST** /send/v1/partners/{partnerId}/events/generate/refund | Client can simulate a Mastercard Merchant Presented QR Refund notification to the registered URL endpoint.  |


<a id="sendNotificationRefundRetry"></a>
# **sendNotificationRefundRetry**
> NotificationResponse166Wrapper sendNotificationRefundRetry(partnerId, notificationRequest)

Client can simulate a Mastercard Merchant Presented QR Refund notification to the registered URL endpoint. 

Client can simulate a Mastercard Merchant Presented QR Refund notification to the registered URL endpoint. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestRefundNotificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    TestRefundNotificationApi apiInstance = new TestRefundNotificationApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
    NotificationRequest163Wrapper notificationRequest = new NotificationRequest163Wrapper(); // NotificationRequest163Wrapper | Contains the details of the request message.
    try {
      NotificationResponse166Wrapper result = apiInstance.sendNotificationRefundRetry(partnerId, notificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestRefundNotificationApi#sendNotificationRefundRetry");
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
| **notificationRequest** | [**NotificationRequest163Wrapper**](NotificationRequest163Wrapper.md)| Contains the details of the request message. | [optional] |

### Return type

[**NotificationResponse166Wrapper**](NotificationResponse166Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: N/A

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains the details of the response message. |  -  |

