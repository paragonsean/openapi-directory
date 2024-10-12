# MyNotificationsApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1UsersMeNotificationSettingsPut**](MyNotificationsApi.md#apiV1UsersMeNotificationSettingsPut) | **PUT** /api/v1/users/me/notification-settings | Update my notification settings |
| [**apiV1UsersMeNotificationsGet**](MyNotificationsApi.md#apiV1UsersMeNotificationsGet) | **GET** /api/v1/users/me/notifications | List my notifications |
| [**apiV1UsersMeNotificationsReadAllPost**](MyNotificationsApi.md#apiV1UsersMeNotificationsReadAllPost) | **POST** /api/v1/users/me/notifications/read-all | Mark all my notification as read |
| [**apiV1UsersMeNotificationsReadPost**](MyNotificationsApi.md#apiV1UsersMeNotificationsReadPost) | **POST** /api/v1/users/me/notifications/read | Mark notifications as read by their id |


<a id="apiV1UsersMeNotificationSettingsPut"></a>
# **apiV1UsersMeNotificationSettingsPut**
> apiV1UsersMeNotificationSettingsPut(apiV1UsersMeNotificationSettingsPutRequest)

Update my notification settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyNotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyNotificationsApi apiInstance = new MyNotificationsApi(defaultClient);
    ApiV1UsersMeNotificationSettingsPutRequest apiV1UsersMeNotificationSettingsPutRequest = new ApiV1UsersMeNotificationSettingsPutRequest(); // ApiV1UsersMeNotificationSettingsPutRequest | 
    try {
      apiInstance.apiV1UsersMeNotificationSettingsPut(apiV1UsersMeNotificationSettingsPutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyNotificationsApi#apiV1UsersMeNotificationSettingsPut");
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
| **apiV1UsersMeNotificationSettingsPutRequest** | [**ApiV1UsersMeNotificationSettingsPutRequest**](ApiV1UsersMeNotificationSettingsPutRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="apiV1UsersMeNotificationsGet"></a>
# **apiV1UsersMeNotificationsGet**
> NotificationListResponse apiV1UsersMeNotificationsGet(unread, start, count, sort)

List my notifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyNotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyNotificationsApi apiInstance = new MyNotificationsApi(defaultClient);
    Boolean unread = true; // Boolean | only list unread notifications
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      NotificationListResponse result = apiInstance.apiV1UsersMeNotificationsGet(unread, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyNotificationsApi#apiV1UsersMeNotificationsGet");
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
| **unread** | **Boolean**| only list unread notifications | [optional] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |

### Return type

[**NotificationListResponse**](NotificationListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1UsersMeNotificationsReadAllPost"></a>
# **apiV1UsersMeNotificationsReadAllPost**
> apiV1UsersMeNotificationsReadAllPost()

Mark all my notification as read

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyNotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyNotificationsApi apiInstance = new MyNotificationsApi(defaultClient);
    try {
      apiInstance.apiV1UsersMeNotificationsReadAllPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyNotificationsApi#apiV1UsersMeNotificationsReadAllPost");
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

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="apiV1UsersMeNotificationsReadPost"></a>
# **apiV1UsersMeNotificationsReadPost**
> apiV1UsersMeNotificationsReadPost(apiV1UsersMeNotificationsReadPostRequest)

Mark notifications as read by their id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyNotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyNotificationsApi apiInstance = new MyNotificationsApi(defaultClient);
    ApiV1UsersMeNotificationsReadPostRequest apiV1UsersMeNotificationsReadPostRequest = new ApiV1UsersMeNotificationsReadPostRequest(); // ApiV1UsersMeNotificationsReadPostRequest | 
    try {
      apiInstance.apiV1UsersMeNotificationsReadPost(apiV1UsersMeNotificationsReadPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyNotificationsApi#apiV1UsersMeNotificationsReadPost");
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
| **apiV1UsersMeNotificationsReadPostRequest** | [**ApiV1UsersMeNotificationsReadPostRequest**](ApiV1UsersMeNotificationsReadPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

