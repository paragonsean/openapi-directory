# NotificationsApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tryNotificationConfig**](NotificationsApi.md#tryNotificationConfig) | **POST** /v1/notifications/try | Try sending a notifications |


<a id="tryNotificationConfig"></a>
# **tryNotificationConfig**
> NotificationRead tryNotificationConfig(notification)

Try sending a notifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    Notification notification = new Notification(); // Notification | 
    try {
      NotificationRead result = apiInstance.tryNotificationConfig(notification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#tryNotificationConfig");
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
| **notification** | [**Notification**](Notification.md)|  | |

### Return type

[**NotificationRead**](NotificationRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

