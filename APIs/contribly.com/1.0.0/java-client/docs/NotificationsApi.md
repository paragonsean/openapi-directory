# NotificationsApi

All URIs are relative to *https://api.contribly.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**notificationsContributionsIdPreviewGet**](NotificationsApi.md#notificationsContributionsIdPreviewGet) | **GET** /notifications/contributions/{id}/preview |  |


<a id="notificationsContributionsIdPreviewGet"></a>
# **notificationsContributionsIdPreviewGet**
> NotificationPreview notificationsContributionsIdPreviewGet(id, message)



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
    defaultClient.setBasePath("https://api.contribly.com/1");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String id = "id_example"; // String | Id of the contribution to preview a notification for
    String message = "message_example"; // String | Type of message to preview.
    try {
      NotificationPreview result = apiInstance.notificationsContributionsIdPreviewGet(id, message);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationsContributionsIdPreviewGet");
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
| **id** | **String**| Id of the contribution to preview a notification for | |
| **message** | **String**| Type of message to preview. | |

### Return type

[**NotificationPreview**](NotificationPreview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification preview |  -  |

