# NotificationApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNotificationCollection**](NotificationApi.md#getNotificationCollection) | **GET** /notifications | Retrieves the collection of Notification resources. |
| [**getNotificationItem**](NotificationApi.md#getNotificationItem) | **GET** /notifications/{id} | Retrieves a Notification resource. |


<a id="getNotificationCollection"></a>
# **getNotificationCollection**
> List&lt;NotificationRead&gt; getNotificationCollection(page)

Retrieves the collection of Notification resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    NotificationApi apiInstance = new NotificationApi(defaultClient);
    Integer page = 56; // Integer | The collection page number
    try {
      List<NotificationRead> result = apiInstance.getNotificationCollection(page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationApi#getNotificationCollection");
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
| **page** | **Integer**| The collection page number | [optional] |

### Return type

[**List&lt;NotificationRead&gt;**](NotificationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification collection response |  -  |

<a id="getNotificationItem"></a>
# **getNotificationItem**
> NotificationRead getNotificationItem(id)

Retrieves a Notification resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    NotificationApi apiInstance = new NotificationApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      NotificationRead result = apiInstance.getNotificationItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationApi#getNotificationItem");
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
| **id** | **String**|  | |

### Return type

[**NotificationRead**](NotificationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification resource response |  -  |
| **404** | Resource not found |  -  |

