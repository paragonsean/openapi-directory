# NotificationsApi

All URIs are relative to *https://api.illumidesk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**notificationRead**](NotificationsApi.md#notificationRead) | **GET** /v1/{namespace}/notifications/{notification_id} | Retrieve a specific notification. |
| [**notificationSettingsCreate**](NotificationsApi.md#notificationSettingsCreate) | **POST** /v1/{namespace}/notifications/settings/ | Create global notification settings |
| [**notificationSettingsEntityCreate**](NotificationsApi.md#notificationSettingsEntityCreate) | **POST** /v1/{namespace}/notifications/settings/entity/{entity} | Create global notification settings |
| [**notificationSettingsEntityRead**](NotificationsApi.md#notificationSettingsEntityRead) | **GET** /v1/{namespace}/notifications/settings/entity/{entity} | Retrieve global notification settings for the authenticated user |
| [**notificationSettingsEntityUpdate**](NotificationsApi.md#notificationSettingsEntityUpdate) | **PATCH** /v1/{namespace}/notifications/settings/entity/{entity} | Modify global notification settings. |
| [**notificationSettingsRead**](NotificationsApi.md#notificationSettingsRead) | **GET** /v1/{namespace}/notifications/settings/ | Retrieve global notification settings for the authenticated user |
| [**notificationSettingsUpdate**](NotificationsApi.md#notificationSettingsUpdate) | **PATCH** /v1/{namespace}/notifications/settings/ | Modify global notification settings. |
| [**notificationUpdate**](NotificationsApi.md#notificationUpdate) | **PATCH** /v1/{namespace}/notifications/{notification_id} | Mark a specific notification as either read or unread. |
| [**notificationsList**](NotificationsApi.md#notificationsList) | **GET** /v1/{namespace}/notifications/ | Get notifications of all types and entities for the authenticated user. |
| [**notificationsListEntity**](NotificationsApi.md#notificationsListEntity) | **GET** /v1/{namespace}/notifications/entity/{entity} | Get notifications of all types and entities for the authenticated user. |
| [**notificationsUpdateEntityList**](NotificationsApi.md#notificationsUpdateEntityList) | **PATCH** /v1/{namespace}/notifications/entity/{entity} | Mark a list of notifications as either read or unread. |
| [**notificationsUpdateList**](NotificationsApi.md#notificationsUpdateList) | **PATCH** /v1/{namespace}/notifications/ | Mark a list of notifications as either read or unread. |


<a id="notificationRead"></a>
# **notificationRead**
> Notification notificationRead(namespace, notificationId)

Retrieve a specific notification.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team data.
    String notificationId = "notificationId_example"; // String | Notification UUID.
    try {
      Notification result = apiInstance.notificationRead(namespace, notificationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationRead");
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
| **namespace** | **String**| User or team data. | |
| **notificationId** | **String**| Notification UUID. | |

### Return type

[**Notification**](Notification.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve a notification. |  -  |
| **404** | Notification not found. |  -  |

<a id="notificationSettingsCreate"></a>
# **notificationSettingsCreate**
> NotificationSettings notificationSettingsCreate(namespace, notificationSettingsData)

Create global notification settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    NotificationSettingsData notificationSettingsData = new NotificationSettingsData(); // NotificationSettingsData | 
    try {
      NotificationSettings result = apiInstance.notificationSettingsCreate(namespace, notificationSettingsData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationSettingsCreate");
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
| **namespace** | **String**| User or team name. | |
| **notificationSettingsData** | [**NotificationSettingsData**](NotificationSettingsData.md)|  | |

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Global Notification Settings created successfully. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="notificationSettingsEntityCreate"></a>
# **notificationSettingsEntityCreate**
> NotificationSettings notificationSettingsEntityCreate(namespace, entity, notificationSettingsData)

Create global notification settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String entity = "billing"; // String | Entity whose settings should be retrieved.
    NotificationSettingsData notificationSettingsData = new NotificationSettingsData(); // NotificationSettingsData | 
    try {
      NotificationSettings result = apiInstance.notificationSettingsEntityCreate(namespace, entity, notificationSettingsData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationSettingsEntityCreate");
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
| **namespace** | **String**| User or team name. | |
| **entity** | **String**| Entity whose settings should be retrieved. | [enum: billing] |
| **notificationSettingsData** | [**NotificationSettingsData**](NotificationSettingsData.md)|  | [optional] |

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Global Notification Settings created successfully. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="notificationSettingsEntityRead"></a>
# **notificationSettingsEntityRead**
> List&lt;NotificationSettings&gt; notificationSettingsEntityRead(namespace, entity)

Retrieve global notification settings for the authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team data.
    String entity = "billing"; // String | Entity whose settings should be retrieved.
    try {
      List<NotificationSettings> result = apiInstance.notificationSettingsEntityRead(namespace, entity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationSettingsEntityRead");
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
| **namespace** | **String**| User or team data. | |
| **entity** | **String**| Entity whose settings should be retrieved. | [enum: billing] |

### Return type

[**List&lt;NotificationSettings&gt;**](NotificationSettings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Global notification settings |  -  |
| **404** | Notification not found. |  -  |

<a id="notificationSettingsEntityUpdate"></a>
# **notificationSettingsEntityUpdate**
> NotificationSettings notificationSettingsEntityUpdate(namespace, entity, notificationSettingsData)

Modify global notification settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String entity = "billing"; // String | Entity whose settings should be retrieved.
    NotificationSettingsData notificationSettingsData = new NotificationSettingsData(); // NotificationSettingsData | 
    try {
      NotificationSettings result = apiInstance.notificationSettingsEntityUpdate(namespace, entity, notificationSettingsData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationSettingsEntityUpdate");
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
| **namespace** | **String**| User or team name. | |
| **entity** | **String**| Entity whose settings should be retrieved. | [enum: billing] |
| **notificationSettingsData** | [**NotificationSettingsData**](NotificationSettingsData.md)|  | [optional] |

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification Settings updated |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Notification Settings not found. |  -  |

<a id="notificationSettingsRead"></a>
# **notificationSettingsRead**
> List&lt;NotificationSettings&gt; notificationSettingsRead(namespace)

Retrieve global notification settings for the authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team data.
    try {
      List<NotificationSettings> result = apiInstance.notificationSettingsRead(namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationSettingsRead");
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
| **namespace** | **String**| User or team data. | |

### Return type

[**List&lt;NotificationSettings&gt;**](NotificationSettings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Global notification settings |  -  |
| **404** | Notification not found. |  -  |

<a id="notificationSettingsUpdate"></a>
# **notificationSettingsUpdate**
> NotificationSettings notificationSettingsUpdate(namespace, notificationSettingsData)

Modify global notification settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    NotificationSettingsData notificationSettingsData = new NotificationSettingsData(); // NotificationSettingsData | 
    try {
      NotificationSettings result = apiInstance.notificationSettingsUpdate(namespace, notificationSettingsData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationSettingsUpdate");
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
| **namespace** | **String**| User or team name. | |
| **notificationSettingsData** | [**NotificationSettingsData**](NotificationSettingsData.md)|  | [optional] |

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification Settings updated |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Notification Settings not found. |  -  |

<a id="notificationUpdate"></a>
# **notificationUpdate**
> Notification notificationUpdate(namespace, notificationId, notificationData)

Mark a specific notification as either read or unread.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team data.
    String notificationId = "notificationId_example"; // String | Notification UUID.
    NotificationUpdateData notificationData = new NotificationUpdateData(); // NotificationUpdateData | 
    try {
      Notification result = apiInstance.notificationUpdate(namespace, notificationId, notificationData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationUpdate");
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
| **namespace** | **String**| User or team data. | |
| **notificationId** | **String**| Notification UUID. | |
| **notificationData** | [**NotificationUpdateData**](NotificationUpdateData.md)|  | [optional] |

### Return type

[**Notification**](Notification.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification updated |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Notification not found. |  -  |

<a id="notificationsList"></a>
# **notificationsList**
> List&lt;Notification&gt; notificationsList(namespace, limit, offset, ordering, read)

Get notifications of all types and entities for the authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team data.
    String limit = "limit_example"; // String | Limit when getting items.
    String offset = "offset_example"; // String | Offset when getting items.
    String ordering = "ordering_example"; // String | Ordering when getting items.
    Boolean read = true; // Boolean | When true, get only read notifications. When false, get only unread notifications. Default behavior is to return both read and unread.
    try {
      List<Notification> result = apiInstance.notificationsList(namespace, limit, offset, ordering, read);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationsList");
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
| **namespace** | **String**| User or team data. | |
| **limit** | **String**| Limit when getting items. | [optional] |
| **offset** | **String**| Offset when getting items. | [optional] |
| **ordering** | **String**| Ordering when getting items. | [optional] |
| **read** | **Boolean**| When true, get only read notifications. When false, get only unread notifications. Default behavior is to return both read and unread. | [optional] |

### Return type

[**List&lt;Notification&gt;**](Notification.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of notifications |  -  |

<a id="notificationsListEntity"></a>
# **notificationsListEntity**
> List&lt;Notification&gt; notificationsListEntity(namespace, entity, limit, offset, ordering, read)

Get notifications of all types and entities for the authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team data.
    String entity = "billing"; // String | Entity to filter notifications by.
    String limit = "limit_example"; // String | Limit when getting items.
    String offset = "offset_example"; // String | Offset when getting items.
    String ordering = "ordering_example"; // String | Ordering when getting items.
    Boolean read = true; // Boolean | When true, get only read notifications. When false, get only unread notifications. Default behavior is to return both read and unread.
    try {
      List<Notification> result = apiInstance.notificationsListEntity(namespace, entity, limit, offset, ordering, read);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationsListEntity");
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
| **namespace** | **String**| User or team data. | |
| **entity** | **String**| Entity to filter notifications by. | [enum: billing] |
| **limit** | **String**| Limit when getting items. | [optional] |
| **offset** | **String**| Offset when getting items. | [optional] |
| **ordering** | **String**| Ordering when getting items. | [optional] |
| **read** | **Boolean**| When true, get only read notifications. When false, get only unread notifications. Default behavior is to return both read and unread. | [optional] |

### Return type

[**List&lt;Notification&gt;**](Notification.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of notifications |  -  |

<a id="notificationsUpdateEntityList"></a>
# **notificationsUpdateEntityList**
> Notification notificationsUpdateEntityList(namespace, entity, notificationData)

Mark a list of notifications as either read or unread.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String entity = "billing"; // String | Entity to filter notifications by.
    NotificationListUpdateData notificationData = new NotificationListUpdateData(); // NotificationListUpdateData | 
    try {
      Notification result = apiInstance.notificationsUpdateEntityList(namespace, entity, notificationData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationsUpdateEntityList");
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
| **namespace** | **String**| User or team name. | |
| **entity** | **String**| Entity to filter notifications by. | [enum: billing] |
| **notificationData** | [**NotificationListUpdateData**](NotificationListUpdateData.md)|  | |

### Return type

[**Notification**](Notification.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification updated |  -  |
| **400** | Invalid data supplied |  -  |

<a id="notificationsUpdateList"></a>
# **notificationsUpdateList**
> Notification notificationsUpdateList(namespace, notificationData)

Mark a list of notifications as either read or unread.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    NotificationListUpdateData notificationData = new NotificationListUpdateData(); // NotificationListUpdateData | 
    try {
      Notification result = apiInstance.notificationsUpdateList(namespace, notificationData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#notificationsUpdateList");
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
| **namespace** | **String**| User or team name. | |
| **notificationData** | [**NotificationListUpdateData**](NotificationListUpdateData.md)|  | |

### Return type

[**Notification**](Notification.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification updated |  -  |
| **400** | Invalid data supplied |  -  |

