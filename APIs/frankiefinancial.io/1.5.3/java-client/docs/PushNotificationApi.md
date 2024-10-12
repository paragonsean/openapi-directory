# PushNotificationApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**notifyResult**](PushNotificationApi.md#notifyResult) | **POST** /your/configured/path/{requestId} | Push Notification Payload |


<a id="notifyResult"></a>
# **notifyResult**
> notifyResult(requestId, notifcationResult)

Push Notification Payload

Whenever you request that a transaction be put into the background, there needs to be a mechanism for notifying you that the request has been completed. This notification will push you the high-level details of the result, and you can then query the results at your leisiure.  The same notification process will also be used to push alerts to your system. This means that RequestIDs may not match your records 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushNotificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");

    PushNotificationApi apiInstance = new PushNotificationApi(defaultClient);
    String requestId = "requestId_example"; // String | This will be the same RequestId that was sent in the 202 acceptance response. 
    NotificationResultObject notifcationResult = new NotificationResultObject(); // NotificationResultObject | 
    try {
      apiInstance.notifyResult(requestId, notifcationResult);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushNotificationApi#notifyResult");
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
| **requestId** | **String**| This will be the same RequestId that was sent in the 202 acceptance response.  | |
| **notifcationResult** | [**NotificationResultObject**](NotificationResultObject.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Customer has accepted the notification and we don&#39;t need to retry sending it. |  -  |
| **400** | The notification represents a type of notification the customer was not expecting, or can accept. No retry. |  -  |
| **500** | The Customer cannot accept the notification at this time. Please resend again later |  -  |

