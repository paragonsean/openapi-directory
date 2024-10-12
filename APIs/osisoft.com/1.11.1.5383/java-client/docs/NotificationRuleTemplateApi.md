# NotificationRuleTemplateApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**notificationRuleTemplateCreateNotificationRuleTemplateSubscriber**](NotificationRuleTemplateApi.md#notificationRuleTemplateCreateNotificationRuleTemplateSubscriber) | **POST** /notificationruletemplates/{webId}/notificationrulesubscribers | Create a notification rule subscriber. |
| [**notificationRuleTemplateCreateSecurityEntry**](NotificationRuleTemplateApi.md#notificationRuleTemplateCreateSecurityEntry) | **POST** /notificationruletemplates/{webId}/securityentries | Create a security entry owned by the notification rule template. |
| [**notificationRuleTemplateDelete**](NotificationRuleTemplateApi.md#notificationRuleTemplateDelete) | **DELETE** /notificationruletemplates/{webId} | Delete a notification rule template. |
| [**notificationRuleTemplateDeleteSecurityEntry**](NotificationRuleTemplateApi.md#notificationRuleTemplateDeleteSecurityEntry) | **DELETE** /notificationruletemplates/{webId}/securityentries/{name} | Delete a security entry owned by the notification rule template. |
| [**notificationRuleTemplateGet**](NotificationRuleTemplateApi.md#notificationRuleTemplateGet) | **GET** /notificationruletemplates/{webId} | Get the specified notification rule template. |
| [**notificationRuleTemplateGetByPath**](NotificationRuleTemplateApi.md#notificationRuleTemplateGetByPath) | **GET** /notificationruletemplates | Retrieve a notification rule template by path. |
| [**notificationRuleTemplateGetNotificationRuleTemplateSubscribers**](NotificationRuleTemplateApi.md#notificationRuleTemplateGetNotificationRuleTemplateSubscribers) | **GET** /notificationruletemplates/{webId}/notificationrulesubscribers | Retrieve notification rule template subscribers. |
| [**notificationRuleTemplateGetNotificationRuleTemplatesQuery**](NotificationRuleTemplateApi.md#notificationRuleTemplateGetNotificationRuleTemplatesQuery) | **GET** /notificationruletemplates/search | Retrieve Notification rule templates based on the specified conditions. Returns Notification rule templates using the specified search query string. |
| [**notificationRuleTemplateGetSecurity**](NotificationRuleTemplateApi.md#notificationRuleTemplateGetSecurity) | **GET** /notificationruletemplates/{webId}/security | Get the security information of the specified security item associated with the notification rule template for a specified user. |
| [**notificationRuleTemplateGetSecurityEntries**](NotificationRuleTemplateApi.md#notificationRuleTemplateGetSecurityEntries) | **GET** /notificationruletemplates/{webId}/securityentries | Retrieve the security entries associated with the notification rule template based on the specified criteria. By default, all security entries for this notification rule template are returned. |
| [**notificationRuleTemplateGetSecurityEntryByName**](NotificationRuleTemplateApi.md#notificationRuleTemplateGetSecurityEntryByName) | **GET** /notificationruletemplates/{webId}/securityentries/{name} | Retrieve the security entry associated with the notification rule template with the specified name. |
| [**notificationRuleTemplateUpdate**](NotificationRuleTemplateApi.md#notificationRuleTemplateUpdate) | **PATCH** /notificationruletemplates/{webId} | Update a notification rule template by replacing items in its definition. |
| [**notificationRuleTemplateUpdateSecurityEntry**](NotificationRuleTemplateApi.md#notificationRuleTemplateUpdateSecurityEntry) | **PUT** /notificationruletemplates/{webId}/securityentries/{name} | Update a security entry owned by the notification rule template. |


<a id="notificationRuleTemplateCreateNotificationRuleTemplateSubscriber"></a>
# **notificationRuleTemplateCreateNotificationRuleTemplateSubscriber**
> notificationRuleTemplateCreateNotificationRuleTemplateSubscriber(webId, notificationRuleSubscriber, webIdType)

Create a notification rule subscriber.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule template on which to create the notification rule subscriber.
    NotificationRuleSubscriber notificationRuleSubscriber = new NotificationRuleSubscriber(); // NotificationRuleSubscriber | The new notification rule subscriber definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.notificationRuleTemplateCreateNotificationRuleTemplateSubscriber(webId, notificationRuleSubscriber, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateCreateNotificationRuleTemplateSubscriber");
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
| **webId** | **String**| The ID of the notification rule template on which to create the notification rule subscriber. | |
| **notificationRuleSubscriber** | [**NotificationRuleSubscriber**](NotificationRuleSubscriber.md)| The new notification rule subscriber definition. | |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

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
| **201** | The notification rule subscriber was created. The response&#39;s Location header is a link to the notification rule subscriber. |  -  |

<a id="notificationRuleTemplateCreateSecurityEntry"></a>
# **notificationRuleTemplateCreateSecurityEntry**
> notificationRuleTemplateCreateSecurityEntry(webId, securityEntry, applyToChildren, webIdType)

Create a security entry owned by the notification rule template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule template, where the security entry will be created.
    SecurityEntry securityEntry = new SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.notificationRuleTemplateCreateSecurityEntry(webId, securityEntry, applyToChildren, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateCreateSecurityEntry");
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
| **webId** | **String**| The ID of the notification rule template, where the security entry will be created. | |
| **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied. | |
| **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

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
| **201** | The security entry was created. The response&#39;s Location header is a link to the security entry. |  -  |

<a id="notificationRuleTemplateDelete"></a>
# **notificationRuleTemplateDelete**
> notificationRuleTemplateDelete(webId)

Delete a notification rule template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule template.
    try {
      apiInstance.notificationRuleTemplateDelete(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateDelete");
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
| **webId** | **String**| The ID of the notification rule template. | |

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
| **204** | The notification rule template was deleted. |  -  |

<a id="notificationRuleTemplateDeleteSecurityEntry"></a>
# **notificationRuleTemplateDeleteSecurityEntry**
> notificationRuleTemplateDeleteSecurityEntry(name, webId, applyToChildren)

Delete a security entry owned by the notification rule template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    String webId = "webId_example"; // String | The ID of the notification rule template, where the security entry will be deleted.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    try {
      apiInstance.notificationRuleTemplateDeleteSecurityEntry(name, webId, applyToChildren);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateDeleteSecurityEntry");
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
| **name** | **String**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | |
| **webId** | **String**| The ID of the notification rule template, where the security entry will be deleted. | |
| **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] |

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
| **204** | The security entry was deleted. |  -  |

<a id="notificationRuleTemplateGet"></a>
# **notificationRuleTemplateGet**
> NotificationRuleTemplate notificationRuleTemplateGet(webId, selectedFields, webIdType)

Get the specified notification rule template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule template.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      NotificationRuleTemplate result = apiInstance.notificationRuleTemplateGet(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateGet");
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
| **webId** | **String**| The ID of the notification rule template. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**NotificationRuleTemplate**](NotificationRuleTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified notification rule template. |  -  |

<a id="notificationRuleTemplateGetByPath"></a>
# **notificationRuleTemplateGetByPath**
> NotificationRuleTemplate notificationRuleTemplateGetByPath(path, selectedFields, webIdType)

Retrieve a notification rule template by path.

This method returns a Notification Rule Template based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String path = "path_example"; // String | The path to the notification rule template.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      NotificationRuleTemplate result = apiInstance.notificationRuleTemplateGetByPath(path, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateGetByPath");
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
| **path** | **String**| The path to the notification rule template. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**NotificationRuleTemplate**](NotificationRuleTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified notification rule template. |  -  |

<a id="notificationRuleTemplateGetNotificationRuleTemplateSubscribers"></a>
# **notificationRuleTemplateGetNotificationRuleTemplateSubscribers**
> ItemsNotificationRuleSubscriber notificationRuleTemplateGetNotificationRuleTemplateSubscribers(webId, selectedFields, webIdType)

Retrieve notification rule template subscribers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the resource to use as the root of the search.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsNotificationRuleSubscriber result = apiInstance.notificationRuleTemplateGetNotificationRuleTemplateSubscribers(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateGetNotificationRuleTemplateSubscribers");
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
| **200** | A list of notification rule template subscribers. |  -  |

<a id="notificationRuleTemplateGetNotificationRuleTemplatesQuery"></a>
# **notificationRuleTemplateGetNotificationRuleTemplatesQuery**
> ItemsNotificationRuleTemplate notificationRuleTemplateGetNotificationRuleTemplatesQuery(databaseWebId, maxCount, query, selectedFields, startIndex, webIdType)

Retrieve Notification rule templates based on the specified conditions. Returns Notification rule templates using the specified search query string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String databaseWebId = "databaseWebId_example"; // String | The ID of the asset database to use as the root of the query.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String query = "query_example"; // String | The query string is a list of filters used to perform an AFSearch for the Notification rule templates in the asset database. An example would be: \"query=NotificationRuleTemplate:{ Name:='MyNotificationRuleTemplate' } Type:=Int32\".
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsNotificationRuleTemplate result = apiInstance.notificationRuleTemplateGetNotificationRuleTemplatesQuery(databaseWebId, maxCount, query, selectedFields, startIndex, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateGetNotificationRuleTemplatesQuery");
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
| **databaseWebId** | **String**| The ID of the asset database to use as the root of the query. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **query** | **String**| The query string is a list of filters used to perform an AFSearch for the Notification rule templates in the asset database. An example would be: \&quot;query&#x3D;NotificationRuleTemplate:{ Name:&#x3D;&#39;MyNotificationRuleTemplate&#39; } Type:&#x3D;Int32\&quot;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsNotificationRuleTemplate**](ItemsNotificationRuleTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of notification rule templates matching the specified conditions. |  -  |

<a id="notificationRuleTemplateGetSecurity"></a>
# **notificationRuleTemplateGetSecurity**
> ItemsSecurityRights notificationRuleTemplateGetSecurity(webId, userIdentity, forceRefresh, selectedFields, webIdType)

Get the security information of the specified security item associated with the notification rule template for a specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule template for the security to be checked.
    List<String> userIdentity = Arrays.asList(); // List<String> | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
    Boolean forceRefresh = true; // Boolean | Indicates if the security cache should be refreshed before getting security information. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsSecurityRights result = apiInstance.notificationRuleTemplateGetSecurity(webId, userIdentity, forceRefresh, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateGetSecurity");
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
| **webId** | **String**| The ID of the notification rule template for the security to be checked. | |
| **userIdentity** | [**List&lt;String&gt;**](String.md)| The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user&#39;s security rights will be returned. | |
| **forceRefresh** | **Boolean**| Indicates if the security cache should be refreshed before getting security information. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsSecurityRights**](ItemsSecurityRights.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Security rights. |  -  |
| **400** | An invalid or local account is specified as the user identity. |  -  |
| **401** | Access denied for the specified user identity. |  -  |
| **409** | Unsupported when using Anonymous authentication method. |  -  |
| **502** | Failed to retrieve the specified user identity. |  -  |

<a id="notificationRuleTemplateGetSecurityEntries"></a>
# **notificationRuleTemplateGetSecurityEntries**
> ItemsSecurityEntry notificationRuleTemplateGetSecurityEntries(webId, nameFilter, selectedFields, webIdType)

Retrieve the security entries associated with the notification rule template based on the specified criteria. By default, all security entries for this notification rule template are returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule template.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering security entries. The default is no filter.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsSecurityEntry result = apiInstance.notificationRuleTemplateGetSecurityEntries(webId, nameFilter, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateGetSecurityEntries");
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
| **webId** | **String**| The ID of the notification rule template. | |
| **nameFilter** | **String**| The name query string used for filtering security entries. The default is no filter. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsSecurityEntry**](ItemsSecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of security entries matching the specified condition. |  -  |

<a id="notificationRuleTemplateGetSecurityEntryByName"></a>
# **notificationRuleTemplateGetSecurityEntryByName**
> SecurityEntry notificationRuleTemplateGetSecurityEntryByName(name, webId, selectedFields, webIdType)

Retrieve the security entry associated with the notification rule template with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    String webId = "webId_example"; // String | The ID of the notification rule template.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      SecurityEntry result = apiInstance.notificationRuleTemplateGetSecurityEntryByName(name, webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateGetSecurityEntryByName");
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
| **name** | **String**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | |
| **webId** | **String**| The ID of the notification rule template. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**SecurityEntry**](SecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The security entry matching the specified condition. |  -  |
| **404** | The security entry with the specified name is not found. |  -  |

<a id="notificationRuleTemplateUpdate"></a>
# **notificationRuleTemplateUpdate**
> notificationRuleTemplateUpdate(webId, notificationRuleTemplate)

Update a notification rule template by replacing items in its definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule template to update.
    NotificationRuleTemplate notificationRuleTemplate = new NotificationRuleTemplate(); // NotificationRuleTemplate | A partial notification rule template containing the desired changes.
    try {
      apiInstance.notificationRuleTemplateUpdate(webId, notificationRuleTemplate);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateUpdate");
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
| **webId** | **String**| The ID of the notification rule template to update. | |
| **notificationRuleTemplate** | [**NotificationRuleTemplate**](NotificationRuleTemplate.md)| A partial notification rule template containing the desired changes. | |

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
| **204** | The notification rule template was updated. |  -  |

<a id="notificationRuleTemplateUpdateSecurityEntry"></a>
# **notificationRuleTemplateUpdateSecurityEntry**
> notificationRuleTemplateUpdateSecurityEntry(name, webId, securityEntry, applyToChildren)

Update a security entry owned by the notification rule template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleTemplateApi apiInstance = new NotificationRuleTemplateApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry.
    String webId = "webId_example"; // String | The ID of the notification rule template, where the security entry will be updated.
    SecurityEntry securityEntry = new SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    try {
      apiInstance.notificationRuleTemplateUpdateSecurityEntry(name, webId, securityEntry, applyToChildren);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleTemplateApi#notificationRuleTemplateUpdateSecurityEntry");
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
| **name** | **String**| The name of the security entry. | |
| **webId** | **String**| The ID of the notification rule template, where the security entry will be updated. | |
| **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | |
| **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] |

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
| **204** | The security entry was updated. |  -  |

