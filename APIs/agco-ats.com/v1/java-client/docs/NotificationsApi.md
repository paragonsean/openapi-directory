# NotificationsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**notificationsPostMail**](NotificationsApi.md#notificationsPostMail) | **POST** /api/v2/Notifications | Sends an email message. |


<a id="notificationsPostMail"></a>
# **notificationsPostMail**
> notificationsPostMail(apIModelsNotification)

Sends an email message.

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    APIModelsNotification apIModelsNotification = new APIModelsNotification(); // APIModelsNotification | The Notification Object.
    try {
      apiInstance.notificationsPostMail(apIModelsNotification);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationsPostMail");
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
| **apIModelsNotification** | [**APIModelsNotification**](APIModelsNotification.md)| The Notification Object. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

