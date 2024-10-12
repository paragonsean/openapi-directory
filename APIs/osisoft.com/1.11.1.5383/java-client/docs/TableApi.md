# TableApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tableCreateSecurityEntry**](TableApi.md#tableCreateSecurityEntry) | **POST** /tables/{webId}/securityentries | Create a security entry owned by the table. |
| [**tableDelete**](TableApi.md#tableDelete) | **DELETE** /tables/{webId} | Delete a table. |
| [**tableDeleteSecurityEntry**](TableApi.md#tableDeleteSecurityEntry) | **DELETE** /tables/{webId}/securityentries/{name} | Delete a security entry owned by the table. |
| [**tableGet**](TableApi.md#tableGet) | **GET** /tables/{webId} | Retrieve a table. |
| [**tableGetByPath**](TableApi.md#tableGetByPath) | **GET** /tables | Retrieve a table by path. |
| [**tableGetCategories**](TableApi.md#tableGetCategories) | **GET** /tables/{webId}/categories | Get a table&#39;s categories. |
| [**tableGetData**](TableApi.md#tableGetData) | **GET** /tables/{webId}/data | Get the table&#39;s data. |
| [**tableGetSecurity**](TableApi.md#tableGetSecurity) | **GET** /tables/{webId}/security | Get the security information of the specified security item associated with the table for a specified user. |
| [**tableGetSecurityEntries**](TableApi.md#tableGetSecurityEntries) | **GET** /tables/{webId}/securityentries | Retrieve the security entries associated with the table based on the specified criteria. By default, all security entries for this table are returned. |
| [**tableGetSecurityEntryByName**](TableApi.md#tableGetSecurityEntryByName) | **GET** /tables/{webId}/securityentries/{name} | Retrieve the security entry associated with the table with the specified name. |
| [**tableUpdate**](TableApi.md#tableUpdate) | **PATCH** /tables/{webId} | Update a table by replacing items in its definition. |
| [**tableUpdateData**](TableApi.md#tableUpdateData) | **PUT** /tables/{webId}/data | Update the table&#39;s data. |
| [**tableUpdateSecurityEntry**](TableApi.md#tableUpdateSecurityEntry) | **PUT** /tables/{webId}/securityentries/{name} | Update a security entry owned by the table. |


<a id="tableCreateSecurityEntry"></a>
# **tableCreateSecurityEntry**
> tableCreateSecurityEntry(webId, securityEntry, applyToChildren, webIdType)

Create a security entry owned by the table.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the table where the security entry will be created.
    SecurityEntry securityEntry = new SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.tableCreateSecurityEntry(webId, securityEntry, applyToChildren, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableCreateSecurityEntry");
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
| **webId** | **String**| The ID of the table where the security entry will be created. | |
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

<a id="tableDelete"></a>
# **tableDelete**
> tableDelete(webId)

Delete a table.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the table to delete.
    try {
      apiInstance.tableDelete(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableDelete");
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
| **webId** | **String**| The ID of the table to delete. | |

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
| **204** | The table was deleted. |  -  |

<a id="tableDeleteSecurityEntry"></a>
# **tableDeleteSecurityEntry**
> tableDeleteSecurityEntry(name, webId, applyToChildren)

Delete a security entry owned by the table.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    String webId = "webId_example"; // String | The ID of the table where the security entry will be deleted.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    try {
      apiInstance.tableDeleteSecurityEntry(name, webId, applyToChildren);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableDeleteSecurityEntry");
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
| **webId** | **String**| The ID of the table where the security entry will be deleted. | |
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

<a id="tableGet"></a>
# **tableGet**
> Table tableGet(webId, selectedFields, webIdType)

Retrieve a table.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the table.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      Table result = apiInstance.tableGet(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableGet");
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
| **webId** | **String**| The ID of the table. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**Table**](Table.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified table. |  -  |

<a id="tableGetByPath"></a>
# **tableGetByPath**
> Table tableGetByPath(path, selectedFields, webIdType)

Retrieve a table by path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String path = "path_example"; // String | The path to the table.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      Table result = apiInstance.tableGetByPath(path, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableGetByPath");
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
| **path** | **String**| The path to the table. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**Table**](Table.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified table. |  -  |

<a id="tableGetCategories"></a>
# **tableGetCategories**
> ItemsTableCategory tableGetCategories(webId, selectedFields, webIdType)

Get a table&#39;s categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the table.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsTableCategory result = apiInstance.tableGetCategories(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableGetCategories");
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
| **webId** | **String**| The ID of the table. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsTableCategory**](ItemsTableCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of categories. |  -  |

<a id="tableGetData"></a>
# **tableGetData**
> TableData tableGetData(webId, selectedFields)

Get the table&#39;s data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the table.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    try {
      TableData result = apiInstance.tableGetData(webId, selectedFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableGetData");
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
| **webId** | **String**| The ID of the table. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |

### Return type

[**TableData**](TableData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The data for the specified table. |  -  |

<a id="tableGetSecurity"></a>
# **tableGetSecurity**
> ItemsSecurityRights tableGetSecurity(webId, userIdentity, forceRefresh, selectedFields, webIdType)

Get the security information of the specified security item associated with the table for a specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the table for the security to be checked.
    List<String> userIdentity = Arrays.asList(); // List<String> | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
    Boolean forceRefresh = true; // Boolean | Indicates if the security cache should be refreshed before getting security information. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsSecurityRights result = apiInstance.tableGetSecurity(webId, userIdentity, forceRefresh, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableGetSecurity");
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
| **webId** | **String**| The ID of the table for the security to be checked. | |
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

<a id="tableGetSecurityEntries"></a>
# **tableGetSecurityEntries**
> ItemsSecurityEntry tableGetSecurityEntries(webId, nameFilter, selectedFields, webIdType)

Retrieve the security entries associated with the table based on the specified criteria. By default, all security entries for this table are returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the table.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering security entries. The default is no filter.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsSecurityEntry result = apiInstance.tableGetSecurityEntries(webId, nameFilter, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableGetSecurityEntries");
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
| **webId** | **String**| The ID of the table. | |
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

<a id="tableGetSecurityEntryByName"></a>
# **tableGetSecurityEntryByName**
> SecurityEntry tableGetSecurityEntryByName(name, webId, selectedFields, webIdType)

Retrieve the security entry associated with the table with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    String webId = "webId_example"; // String | The ID of the table.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      SecurityEntry result = apiInstance.tableGetSecurityEntryByName(name, webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableGetSecurityEntryByName");
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
| **webId** | **String**| The ID of the table. | |
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

<a id="tableUpdate"></a>
# **tableUpdate**
> tableUpdate(webId, table)

Update a table by replacing items in its definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the table to update.
    Table table = new Table(); // Table | A partial table containing the desired changes.
    try {
      apiInstance.tableUpdate(webId, table);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableUpdate");
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
| **webId** | **String**| The ID of the table to update. | |
| **table** | [**Table**](Table.md)| A partial table containing the desired changes. | |

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
| **204** | The table was updated. |  -  |

<a id="tableUpdateData"></a>
# **tableUpdateData**
> tableUpdateData(webId, data)

Update the table&#39;s data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the table on which to update the data.
    TableData data = new TableData(); // TableData | The new table data definition.
    try {
      apiInstance.tableUpdateData(webId, data);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableUpdateData");
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
| **webId** | **String**| The ID of the table on which to update the data. | |
| **data** | [**TableData**](TableData.md)| The new table data definition. | |

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
| **201** | The table data was updated. |  -  |

<a id="tableUpdateSecurityEntry"></a>
# **tableUpdateSecurityEntry**
> tableUpdateSecurityEntry(name, webId, securityEntry, applyToChildren)

Update a security entry owned by the table.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TableApi apiInstance = new TableApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry.
    String webId = "webId_example"; // String | The ID of the table where the security entry will be updated.
    SecurityEntry securityEntry = new SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    try {
      apiInstance.tableUpdateSecurityEntry(name, webId, securityEntry, applyToChildren);
    } catch (ApiException e) {
      System.err.println("Exception when calling TableApi#tableUpdateSecurityEntry");
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
| **webId** | **String**| The ID of the table where the security entry will be updated. | |
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

