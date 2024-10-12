# NotificationRuleSubscriberApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**notificationRuleSubscriberDelete**](NotificationRuleSubscriberApi.md#notificationRuleSubscriberDelete) | **DELETE** /notificationrulesubscribers/{webId} | Delete a notification rule subscriber. |
| [**notificationRuleSubscriberGet**](NotificationRuleSubscriberApi.md#notificationRuleSubscriberGet) | **GET** /notificationrulesubscribers/{webId} | Retrieve a notification rule subscriber. |
| [**notificationRuleSubscriberGetByPath**](NotificationRuleSubscriberApi.md#notificationRuleSubscriberGetByPath) | **GET** /notificationrulesubscribers | Retrieve a notification rule subscriber by path. |
| [**notificationRuleSubscriberGetNotificationRuleSubscribers**](NotificationRuleSubscriberApi.md#notificationRuleSubscriberGetNotificationRuleSubscribers) | **GET** /notificationrulesubscribers/{webId}/notificationrulesubscribers | Retrieve notification rule subscriber subscribers. |
| [**notificationRuleSubscriberUpdate**](NotificationRuleSubscriberApi.md#notificationRuleSubscriberUpdate) | **PATCH** /notificationrulesubscribers/{webId} | Update a notification rule subscriber. |


<a id="notificationRuleSubscriberDelete"></a>
# **notificationRuleSubscriberDelete**
> notificationRuleSubscriberDelete(webId)

Delete a notification rule subscriber.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleSubscriberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleSubscriberApi apiInstance = new NotificationRuleSubscriberApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule subscriber.
    try {
      apiInstance.notificationRuleSubscriberDelete(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleSubscriberApi#notificationRuleSubscriberDelete");
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
| **webId** | **String**| The ID of the notification rule subscriber. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The notification rule subscriber was deleted. |  -  |

<a id="notificationRuleSubscriberGet"></a>
# **notificationRuleSubscriberGet**
> NotificationRuleSubscriber notificationRuleSubscriberGet(webId, selectedFields, webIdType)

Retrieve a notification rule subscriber.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleSubscriberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleSubscriberApi apiInstance = new NotificationRuleSubscriberApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the resource to use as the root of the search.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      NotificationRuleSubscriber result = apiInstance.notificationRuleSubscriberGet(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleSubscriberApi#notificationRuleSubscriberGet");
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
| **webId** | **String**| The ID of the resource to use as the root of the search. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**NotificationRuleSubscriber**](NotificationRuleSubscriber.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A notification rule subscriber |  -  |

<a id="notificationRuleSubscriberGetByPath"></a>
# **notificationRuleSubscriberGetByPath**
> NotificationRuleSubscriber notificationRuleSubscriberGetByPath(path, selectedFields, webIdType)

Retrieve a notification rule subscriber by path.

This method returns a Notification Rule Subscriber based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleSubscriberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleSubscriberApi apiInstance = new NotificationRuleSubscriberApi(defaultClient);
    String path = "path_example"; // String | The path to the notification rule subscriber.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      NotificationRuleSubscriber result = apiInstance.notificationRuleSubscriberGetByPath(path, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleSubscriberApi#notificationRuleSubscriberGetByPath");
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
| **path** | **String**| The path to the notification rule subscriber. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**NotificationRuleSubscriber**](NotificationRuleSubscriber.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified notification rule subscriber. |  -  |

<a id="notificationRuleSubscriberGetNotificationRuleSubscribers"></a>
# **notificationRuleSubscriberGetNotificationRuleSubscribers**
> ItemsNotificationRuleSubscriber notificationRuleSubscriberGetNotificationRuleSubscribers(webId, selectedFields, webIdType)

Retrieve notification rule subscriber subscribers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleSubscriberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleSubscriberApi apiInstance = new NotificationRuleSubscriberApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the resource to use as the root of the search.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsNotificationRuleSubscriber result = apiInstance.notificationRuleSubscriberGetNotificationRuleSubscribers(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleSubscriberApi#notificationRuleSubscriberGetNotificationRuleSubscribers");
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
| **webId** | **String**| The ID of the resource to use as the root of the search. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsNotificationRuleSubscriber**](ItemsNotificationRuleSubscriber.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of notification rules subscribers. |  -  |

<a id="notificationRuleSubscriberUpdate"></a>
# **notificationRuleSubscriberUpdate**
> notificationRuleSubscriberUpdate(webId, notificationRuleSubscriber)

Update a notification rule subscriber.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleSubscriberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleSubscriberApi apiInstance = new NotificationRuleSubscriberApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule subscriber.
    NotificationRuleSubscriber notificationRuleSubscriber = new NotificationRuleSubscriber(); // NotificationRuleSubscriber | A partial notification rule subscriber containing the desired changes.
    try {
      apiInstance.notificationRuleSubscriberUpdate(webId, notificationRuleSubscriber);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleSubscriberApi#notificationRuleSubscriberUpdate");
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
| **webId** | **String**| The ID of the notification rule subscriber. | |
| **notificationRuleSubscriber** | [**NotificationRuleSubscriber**](NotificationRuleSubscriber.md)| A partial notification rule subscriber containing the desired changes. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The notification rule subscriber was updated. |  -  |

