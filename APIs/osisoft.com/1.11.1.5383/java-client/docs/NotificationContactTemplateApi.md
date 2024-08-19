# NotificationContactTemplateApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**notificationContactTemplateCreateSecurityEntry**](NotificationContactTemplateApi.md#notificationContactTemplateCreateSecurityEntry) | **POST** /notificationcontacttemplates/{webId}/securityentries | Create a security entry owned by the notification contact template. |
| [**notificationContactTemplateDelete**](NotificationContactTemplateApi.md#notificationContactTemplateDelete) | **DELETE** /notificationcontacttemplates/{webId} | Delete a notification contact template. |
| [**notificationContactTemplateDeleteSecurityEntry**](NotificationContactTemplateApi.md#notificationContactTemplateDeleteSecurityEntry) | **DELETE** /notificationcontacttemplates/{webId}/securityentries/{name} | Delete a security entry owned by the notification contact template. |
| [**notificationContactTemplateGet**](NotificationContactTemplateApi.md#notificationContactTemplateGet) | **GET** /notificationcontacttemplates/{webId} | Retrieve a notification contact template. |
| [**notificationContactTemplateGetByPath**](NotificationContactTemplateApi.md#notificationContactTemplateGetByPath) | **GET** /notificationcontacttemplates | Retrieve a notification contact template by path. |
| [**notificationContactTemplateGetNotificationContactTemplates**](NotificationContactTemplateApi.md#notificationContactTemplateGetNotificationContactTemplates) | **GET** /notificationcontacttemplates/{webId}/notificationcontacttemplates | Retrieve notification contact template&#39;s child templates. |
| [**notificationContactTemplateGetNotificationContactTemplatesQuery**](NotificationContactTemplateApi.md#notificationContactTemplateGetNotificationContactTemplatesQuery) | **GET** /notificationcontacttemplates/search | Retrieve notification contact templates based on the specified conditions. Returns notification contact templates using the specified search query string. |
| [**notificationContactTemplateGetSecurity**](NotificationContactTemplateApi.md#notificationContactTemplateGetSecurity) | **GET** /notificationcontacttemplates/{webId}/security | Get the security information of the specified security item associated with the notification contact template for a specified user. |
| [**notificationContactTemplateGetSecurityEntries**](NotificationContactTemplateApi.md#notificationContactTemplateGetSecurityEntries) | **GET** /notificationcontacttemplates/{webId}/securityentries | Retrieve the security entries associated with the notification contact template based on the specified criteria. By default, all security entries for this notification contact template are returned. |
| [**notificationContactTemplateGetSecurityEntryByName**](NotificationContactTemplateApi.md#notificationContactTemplateGetSecurityEntryByName) | **GET** /notificationcontacttemplates/{webId}/securityentries/{name} | Retrieve the security entry associated with the notification contact template with the specified name. |
| [**notificationContactTemplateUpdate**](NotificationContactTemplateApi.md#notificationContactTemplateUpdate) | **PATCH** /notificationcontacttemplates/{webId} | Update a notification contact template by replacing items in its definition. |
| [**notificationContactTemplateUpdateSecurityEntry**](NotificationContactTemplateApi.md#notificationContactTemplateUpdateSecurityEntry) | **PUT** /notificationcontacttemplates/{webId}/securityentries/{name} | Update a security entry owned by the notification contact template. |


<a id="notificationContactTemplateCreateSecurityEntry"></a>
# **notificationContactTemplateCreateSecurityEntry**
> notificationContactTemplateCreateSecurityEntry(webId, securityEntry, applyToChildren, webIdType)

Create a security entry owned by the notification contact template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationContactTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationContactTemplateApi apiInstance = new NotificationContactTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification contact template, where the security entry will be created.
    SecurityEntry securityEntry = new SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.notificationContactTemplateCreateSecurityEntry(webId, securityEntry, applyToChildren, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationContactTemplateApi#notificationContactTemplateCreateSecurityEntry");
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
| **webId** | **String**| The ID of the notification contact template, where the security entry will be created. | |
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

<a id="notificationContactTemplateDelete"></a>
# **notificationContactTemplateDelete**
> notificationContactTemplateDelete(webId)

Delete a notification contact template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationContactTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationContactTemplateApi apiInstance = new NotificationContactTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification contact template to be deleted.
    try {
      apiInstance.notificationContactTemplateDelete(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationContactTemplateApi#notificationContactTemplateDelete");
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
| **webId** | **String**| The ID of the notification contact template to be deleted. | |

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
| **204** | The notification contact template was deleted. |  -  |

<a id="notificationContactTemplateDeleteSecurityEntry"></a>
# **notificationContactTemplateDeleteSecurityEntry**
> notificationContactTemplateDeleteSecurityEntry(name, webId, applyToChildren)

Delete a security entry owned by the notification contact template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationContactTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationContactTemplateApi apiInstance = new NotificationContactTemplateApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    String webId = "webId_example"; // String | The ID of the notification contact template, where the security entry will be deleted.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    try {
      apiInstance.notificationContactTemplateDeleteSecurityEntry(name, webId, applyToChildren);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationContactTemplateApi#notificationContactTemplateDeleteSecurityEntry");
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
| **webId** | **String**| The ID of the notification contact template, where the security entry will be deleted. | |
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

<a id="notificationContactTemplateGet"></a>
# **notificationContactTemplateGet**
> NotificationContactTemplate notificationContactTemplateGet(webId, selectedFields, webIdType)

Retrieve a notification contact template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationContactTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationContactTemplateApi apiInstance = new NotificationContactTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification contact template.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      NotificationContactTemplate result = apiInstance.notificationContactTemplateGet(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationContactTemplateApi#notificationContactTemplateGet");
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
| **webId** | **String**| The ID of the notification contact template. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**NotificationContactTemplate**](NotificationContactTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified notification contact template. |  -  |

<a id="notificationContactTemplateGetByPath"></a>
# **notificationContactTemplateGetByPath**
> NotificationContactTemplate notificationContactTemplateGetByPath(path, selectedFields, webIdType)

Retrieve a notification contact template by path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationContactTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationContactTemplateApi apiInstance = new NotificationContactTemplateApi(defaultClient);
    String path = "path_example"; // String | The path to the notification contact template.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      NotificationContactTemplate result = apiInstance.notificationContactTemplateGetByPath(path, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationContactTemplateApi#notificationContactTemplateGetByPath");
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
| **path** | **String**| The path to the notification contact template. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**NotificationContactTemplate**](NotificationContactTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified notification contact template. |  -  |

<a id="notificationContactTemplateGetNotificationContactTemplates"></a>
# **notificationContactTemplateGetNotificationContactTemplates**
> NotificationContactTemplate notificationContactTemplateGetNotificationContactTemplates(webId, selectedFields, webIdType)

Retrieve notification contact template&#39;s child templates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationContactTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationContactTemplateApi apiInstance = new NotificationContactTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification contact template.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      NotificationContactTemplate result = apiInstance.notificationContactTemplateGetNotificationContactTemplates(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationContactTemplateApi#notificationContactTemplateGetNotificationContactTemplates");
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
| **webId** | **String**| The ID of the notification contact template. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**NotificationContactTemplate**](NotificationContactTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of notification contact templates. |  -  |

<a id="notificationContactTemplateGetNotificationContactTemplatesQuery"></a>
# **notificationContactTemplateGetNotificationContactTemplatesQuery**
> ItemsNotificationContactTemplate notificationContactTemplateGetNotificationContactTemplatesQuery(assetServerWebId, maxCount, query, selectedFields, startIndex, webIdType)

Retrieve notification contact templates based on the specified conditions. Returns notification contact templates using the specified search query string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationContactTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationContactTemplateApi apiInstance = new NotificationContactTemplateApi(defaultClient);
    String assetServerWebId = "assetServerWebId_example"; // String | The ID of the asset server to use as the root of the query.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String query = "query_example"; // String | The query string is a list of filters used to perform an AFSearch for the Notification Contact Templates in the asset database. An example would be: \"query=Name:='MyNotificationContactTemplate'\".
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsNotificationContactTemplate result = apiInstance.notificationContactTemplateGetNotificationContactTemplatesQuery(assetServerWebId, maxCount, query, selectedFields, startIndex, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationContactTemplateApi#notificationContactTemplateGetNotificationContactTemplatesQuery");
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
| **assetServerWebId** | **String**| The ID of the asset server to use as the root of the query. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **query** | **String**| The query string is a list of filters used to perform an AFSearch for the Notification Contact Templates in the asset database. An example would be: \&quot;query&#x3D;Name:&#x3D;&#39;MyNotificationContactTemplate&#39;\&quot;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsNotificationContactTemplate**](ItemsNotificationContactTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of notification contact templates matching the specified conditions. |  -  |

<a id="notificationContactTemplateGetSecurity"></a>
# **notificationContactTemplateGetSecurity**
> ItemsSecurityRights notificationContactTemplateGetSecurity(webId, userIdentity, forceRefresh, selectedFields, webIdType)

Get the security information of the specified security item associated with the notification contact template for a specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationContactTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationContactTemplateApi apiInstance = new NotificationContactTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification contact template for the security to be checked.
    List<String> userIdentity = Arrays.asList(); // List<String> | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
    Boolean forceRefresh = true; // Boolean | Indicates if the security cache should be refreshed before getting security information. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsSecurityRights result = apiInstance.notificationContactTemplateGetSecurity(webId, userIdentity, forceRefresh, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationContactTemplateApi#notificationContactTemplateGetSecurity");
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
| **webId** | **String**| The ID of the notification contact template for the security to be checked. | |
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

<a id="notificationContactTemplateGetSecurityEntries"></a>
# **notificationContactTemplateGetSecurityEntries**
> ItemsSecurityEntry notificationContactTemplateGetSecurityEntries(webId, nameFilter, selectedFields, webIdType)

Retrieve the security entries associated with the notification contact template based on the specified criteria. By default, all security entries for this notification contact template are returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationContactTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationContactTemplateApi apiInstance = new NotificationContactTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification contact template.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering security entries. The default is no filter.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsSecurityEntry result = apiInstance.notificationContactTemplateGetSecurityEntries(webId, nameFilter, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationContactTemplateApi#notificationContactTemplateGetSecurityEntries");
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
| **webId** | **String**| The ID of the notification contact template. | |
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

<a id="notificationContactTemplateGetSecurityEntryByName"></a>
# **notificationContactTemplateGetSecurityEntryByName**
> SecurityEntry notificationContactTemplateGetSecurityEntryByName(name, webId, selectedFields, webIdType)

Retrieve the security entry associated with the notification contact template with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationContactTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationContactTemplateApi apiInstance = new NotificationContactTemplateApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    String webId = "webId_example"; // String | The ID of the notification contact template.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      SecurityEntry result = apiInstance.notificationContactTemplateGetSecurityEntryByName(name, webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationContactTemplateApi#notificationContactTemplateGetSecurityEntryByName");
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
| **webId** | **String**| The ID of the notification contact template. | |
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

<a id="notificationContactTemplateUpdate"></a>
# **notificationContactTemplateUpdate**
> notificationContactTemplateUpdate(webId, notificationContactTemplate)

Update a notification contact template by replacing items in its definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationContactTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationContactTemplateApi apiInstance = new NotificationContactTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the notification contact template to update.
    NotificationContactTemplate notificationContactTemplate = new NotificationContactTemplate(); // NotificationContactTemplate | A partial notification contact template containing the desired changes.
    try {
      apiInstance.notificationContactTemplateUpdate(webId, notificationContactTemplate);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationContactTemplateApi#notificationContactTemplateUpdate");
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
| **webId** | **String**| The ID of the notification contact template to update. | |
| **notificationContactTemplate** | [**NotificationContactTemplate**](NotificationContactTemplate.md)| A partial notification contact template containing the desired changes. | |

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
| **204** | The notification contact template was updated. |  -  |

<a id="notificationContactTemplateUpdateSecurityEntry"></a>
# **notificationContactTemplateUpdateSecurityEntry**
> notificationContactTemplateUpdateSecurityEntry(name, webId, securityEntry, applyToChildren)

Update a security entry owned by the notification contact template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationContactTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    NotificationContactTemplateApi apiInstance = new NotificationContactTemplateApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry.
    String webId = "webId_example"; // String | The ID of the notification contact template, where the security entry will be updated.
    SecurityEntry securityEntry = new SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    try {
      apiInstance.notificationContactTemplateUpdateSecurityEntry(name, webId, securityEntry, applyToChildren);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationContactTemplateApi#notificationContactTemplateUpdateSecurityEntry");
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
| **webId** | **String**| The ID of the notification contact template, where the security entry will be updated. | |
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

