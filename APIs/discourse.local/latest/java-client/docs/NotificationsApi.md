# NotificationsApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNotifications**](NotificationsApi.md#getNotifications) | **GET** /notifications.json | Get the notifications that belong to the current user |
| [**markNotificationsAsRead**](NotificationsApi.md#markNotificationsAsRead) | **PUT** /notifications/mark-read.json | Mark notifications as read |


<a id="getNotifications"></a>
# **getNotifications**
> GetNotifications200Response getNotifications()

Get the notifications that belong to the current user

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
    defaultClient.setBasePath("http://discourse.local");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    try {
      GetNotifications200Response result = apiInstance.getNotifications();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#getNotifications");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNotifications200Response**](GetNotifications200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | notifications |  -  |

<a id="markNotificationsAsRead"></a>
# **markNotificationsAsRead**
> UpdateGroup200Response markNotificationsAsRead(markNotificationsAsReadRequest)

Mark notifications as read

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
    defaultClient.setBasePath("http://discourse.local");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    MarkNotificationsAsReadRequest markNotificationsAsReadRequest = new MarkNotificationsAsReadRequest(); // MarkNotificationsAsReadRequest | 
    try {
      UpdateGroup200Response result = apiInstance.markNotificationsAsRead(markNotificationsAsReadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#markNotificationsAsRead");
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
| **markNotificationsAsReadRequest** | [**MarkNotificationsAsReadRequest**](MarkNotificationsAsReadRequest.md)|  | [optional] |

### Return type

[**UpdateGroup200Response**](UpdateGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | notifications marked read |  -  |

