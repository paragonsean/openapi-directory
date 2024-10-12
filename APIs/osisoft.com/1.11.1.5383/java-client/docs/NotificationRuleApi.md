# NotificationRuleApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**notificationRuleCreateNotificationRuleSubscriber**](NotificationRuleApi.md#notificationRuleCreateNotificationRuleSubscriber) | **POST** /notificationrules/{webId}/notificationrulesubscribers | Create a notification rule subscriber. |
| [**notificationRuleCreateSecurityEntry**](NotificationRuleApi.md#notificationRuleCreateSecurityEntry) | **POST** /notificationrules/{webId}/securityentries | Create a security entry owned by the notification rule. |
| [**notificationRuleDelete**](NotificationRuleApi.md#notificationRuleDelete) | **DELETE** /notificationrules/{webId} | Delete a notification rule. |
| [**notificationRuleDeleteSecurityEntry**](NotificationRuleApi.md#notificationRuleDeleteSecurityEntry) | **DELETE** /notificationrules/{webId}/securityentries/{name} | Delete a security entry owned by the notification rule. |
| [**notificationRuleGet**](NotificationRuleApi.md#notificationRuleGet) | **GET** /notificationrules/{webId} | Retrieve a notification rule. |
| [**notificationRuleGetByPath**](NotificationRuleApi.md#notificationRuleGetByPath) | **GET** /notificationrules | Retrieve a notification rule by path. |
| [**notificationRuleGetNotificationRuleSubscribers**](NotificationRuleApi.md#notificationRuleGetNotificationRuleSubscribers) | **GET** /notificationrules/{webId}/notificationrulesubscribers | Retrieve notification rule subscribers. |
| [**notificationRuleGetNotificationRulesQuery**](NotificationRuleApi.md#notificationRuleGetNotificationRulesQuery) | **GET** /notificationrules/search | Retrieve notification rules based on the specified conditions. Returns notification rules using the specified search query string. |
| [**notificationRuleGetSecurity**](NotificationRuleApi.md#notificationRuleGetSecurity) | **GET** /notificationrules/{webId}/security | Get the security information of the specified security item associated with the notification rule for a specified user. |
| [**notificationRuleGetSecurityEntries**](NotificationRuleApi.md#notificationRuleGetSecurityEntries) | **GET** /notificationrules/{webId}/securityentries | Retrieve the security entries associated with the notification rule based on the specified criteria. By default, all security entries for this notification rule are returned. |
| [**notificationRuleGetSecurityEntryByName**](NotificationRuleApi.md#notificationRuleGetSecurityEntryByName) | **GET** /notificationrules/{webId}/securityentries/{name} | Retrieve the security entry associated with the notification rule with the specified name. |
| [**notificationRuleUpdate**](NotificationRuleApi.md#notificationRuleUpdate) | **PATCH** /notificationrules/{webId} | Update a notification rule by replacing items in its definition. |
| [**notificationRuleUpdateSecurityEntry**](NotificationRuleApi.md#notificationRuleUpdateSecurityEntry) | **PUT** /notificationrules/{webId}/securityentries/{name} | Update a security entry owned by the notification rule. |


<a id="notificationRuleCreateNotificationRuleSubscriber"></a>
# **notificationRuleCreateNotificationRuleSubscriber**
> notificationRuleCreateNotificationRuleSubscriber(webId, notificationRuleSubscriber, webIdType)

Create a notification rule subscriber.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule on which to create the notification rule subscriber.
    NotificationRuleSubscriber notificationRuleSubscriber = new NotificationRuleSubscriber(); // NotificationRuleSubscriber | The new notification rule subscriber definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.notificationRuleCreateNotificationRuleSubscriber(webId, notificationRuleSubscriber, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleCreateNotificationRuleSubscriber");
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
| **webId** | **String**| The ID of the notification rule on which to create the notification rule subscriber. | |
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

<a id="notificationRuleCreateSecurityEntry"></a>
# **notificationRuleCreateSecurityEntry**
> notificationRuleCreateSecurityEntry(webId, securityEntry, applyToChildren, webIdType)

Create a security entry owned by the notification rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule, where the security entry will be created.
    SecurityEntry securityEntry = new SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.notificationRuleCreateSecurityEntry(webId, securityEntry, applyToChildren, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleCreateSecurityEntry");
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
| **webId** | **String**| The ID of the notification rule, where the security entry will be created. | |
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

<a id="notificationRuleDelete"></a>
# **notificationRuleDelete**
> notificationRuleDelete(webId)

Delete a notification rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule.
    try {
      apiInstance.notificationRuleDelete(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleDelete");
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
| **webId** | **String**| The ID of the notification rule. | |

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
| **204** | The notification rule was deleted. |  -  |

<a id="notificationRuleDeleteSecurityEntry"></a>
# **notificationRuleDeleteSecurityEntry**
> notificationRuleDeleteSecurityEntry(name, webId, applyToChildren)

Delete a security entry owned by the notification rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    String webId = "webId_example"; // String | The ID of the notification rule, where the security entry will be deleted.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    try {
      apiInstance.notificationRuleDeleteSecurityEntry(name, webId, applyToChildren);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleDeleteSecurityEntry");
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
| **webId** | **String**| The ID of the notification rule, where the security entry will be deleted. | |
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

<a id="notificationRuleGet"></a>
# **notificationRuleGet**
> NotificationRule notificationRuleGet(webId, selectedFields, webIdType)

Retrieve a notification rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the resource to use as the root of the search.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      NotificationRule result = apiInstance.notificationRuleGet(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleGet");
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

[**NotificationRule**](NotificationRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A notification rule |  -  |

<a id="notificationRuleGetByPath"></a>
# **notificationRuleGetByPath**
> NotificationRule notificationRuleGetByPath(path, selectedFields, webIdType)

Retrieve a notification rule by path.

This method returns a Notification Rule based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String path = "path_example"; // String | The path to the notification rule.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      NotificationRule result = apiInstance.notificationRuleGetByPath(path, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleGetByPath");
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
| **path** | **String**| The path to the notification rule. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified notification rule. |  -  |

<a id="notificationRuleGetNotificationRuleSubscribers"></a>
# **notificationRuleGetNotificationRuleSubscribers**
> ItemsNotificationRuleSubscriber notificationRuleGetNotificationRuleSubscribers(webId, selectedFields, webIdType)

Retrieve notification rule subscribers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the resource to use as the root of the search.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsNotificationRuleSubscriber result = apiInstance.notificationRuleGetNotificationRuleSubscribers(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleGetNotificationRuleSubscribers");
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
| **200** | A list of notification rule subscribers. |  -  |

<a id="notificationRuleGetNotificationRulesQuery"></a>
# **notificationRuleGetNotificationRulesQuery**
> ItemsNotificationRule notificationRuleGetNotificationRulesQuery(databaseWebId, maxCount, query, selectedFields, startIndex, webIdType)

Retrieve notification rules based on the specified conditions. Returns notification rules using the specified search query string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String databaseWebId = "databaseWebId_example"; // String | The ID of the asset database to use as the root of the query.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String query = "query_example"; // String | The query string is a list of filters used to perform an AFSearch for the Notification rules in the asset database. An example would be: \"query=Name:=MyNotificationRule* Template:=NoteRuleTemplate\".
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsNotificationRule result = apiInstance.notificationRuleGetNotificationRulesQuery(databaseWebId, maxCount, query, selectedFields, startIndex, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleGetNotificationRulesQuery");
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
| **query** | **String**| The query string is a list of filters used to perform an AFSearch for the Notification rules in the asset database. An example would be: \&quot;query&#x3D;Name:&#x3D;MyNotificationRule* Template:&#x3D;NoteRuleTemplate\&quot;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsNotificationRule**](ItemsNotificationRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of notification rules matching the specified conditions. |  -  |

<a id="notificationRuleGetSecurity"></a>
# **notificationRuleGetSecurity**
> ItemsSecurityRights notificationRuleGetSecurity(webId, userIdentity, forceRefresh, selectedFields, webIdType)

Get the security information of the specified security item associated with the notification rule for a specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule for the security to be checked.
    List<String> userIdentity = Arrays.asList(); // List<String> | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
    Boolean forceRefresh = true; // Boolean | Indicates if the security cache should be refreshed before getting security information. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsSecurityRights result = apiInstance.notificationRuleGetSecurity(webId, userIdentity, forceRefresh, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleGetSecurity");
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
| **webId** | **String**| The ID of the notification rule for the security to be checked. | |
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

<a id="notificationRuleGetSecurityEntries"></a>
# **notificationRuleGetSecurityEntries**
> ItemsSecurityEntry notificationRuleGetSecurityEntries(webId, nameFilter, selectedFields, webIdType)

Retrieve the security entries associated with the notification rule based on the specified criteria. By default, all security entries for this notification rule are returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering security entries. The default is no filter.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsSecurityEntry result = apiInstance.notificationRuleGetSecurityEntries(webId, nameFilter, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleGetSecurityEntries");
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
| **webId** | **String**| The ID of the notification rule. | |
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

<a id="notificationRuleGetSecurityEntryByName"></a>
# **notificationRuleGetSecurityEntryByName**
> SecurityEntry notificationRuleGetSecurityEntryByName(name, webId, selectedFields, webIdType)

Retrieve the security entry associated with the notification rule with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    String webId = "webId_example"; // String | The ID of the notification rule.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      SecurityEntry result = apiInstance.notificationRuleGetSecurityEntryByName(name, webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleGetSecurityEntryByName");
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
| **webId** | **String**| The ID of the notification rule. | |
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

<a id="notificationRuleUpdate"></a>
# **notificationRuleUpdate**
> notificationRuleUpdate(webId, notificationRule)

Update a notification rule by replacing items in its definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification rule to update.
    NotificationRule notificationRule = new NotificationRule(); // NotificationRule | A partial notification rule containing the desired changes.
    try {
      apiInstance.notificationRuleUpdate(webId, notificationRule);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleUpdate");
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
| **webId** | **String**| The ID of the notification rule to update. | |
| **notificationRule** | [**NotificationRule**](NotificationRule.md)| A partial notification rule containing the desired changes. | |

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
| **204** | The notification rule was updated. |  -  |

<a id="notificationRuleUpdateSecurityEntry"></a>
# **notificationRuleUpdateSecurityEntry**
> notificationRuleUpdateSecurityEntry(name, webId, securityEntry, applyToChildren)

Update a security entry owned by the notification rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationRuleApi apiInstance = new NotificationRuleApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry.
    String webId = "webId_example"; // String | The ID of the notification rule, where the security entry will be updated.
    SecurityEntry securityEntry = new SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    try {
      apiInstance.notificationRuleUpdateSecurityEntry(name, webId, securityEntry, applyToChildren);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRuleApi#notificationRuleUpdateSecurityEntry");
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
| **webId** | **String**| The ID of the notification rule, where the security entry will be updated. | |
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

