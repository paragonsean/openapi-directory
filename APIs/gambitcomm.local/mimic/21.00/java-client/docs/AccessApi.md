# AccessApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accessAdd**](AccessApi.md#accessAdd) | **POST** /mimic/access/add/{user}/{agents}/{mask} | Adds/Overwrites the user entry in the access control database. |
| [**accessDel**](AccessApi.md#accessDel) | **DELETE** /mimic/access/del/{user} | Clears a users entry from access control database. |
| [**accessGetAcldb**](AccessApi.md#accessGetAcldb) | **GET** /mimic/access/get/acldb | Returns the current access control database in use. |
| [**accessGetAdmindir**](AccessApi.md#accessGetAdmindir) | **GET** /mimic/access/get/admindir | Returns the current admin directory. |
| [**accessGetAdminuser**](AccessApi.md#accessGetAdminuser) | **GET** /mimic/access/get/adminuser | Returns the current administrator. |
| [**accessGetEnabled**](AccessApi.md#accessGetEnabled) | **GET** /mimic/access/get/enabled | Returns the state of access control checking. |
| [**accessList**](AccessApi.md#accessList) | **GET** /mimic/access/list | Returns an array of entries. |
| [**accessLoad**](AccessApi.md#accessLoad) | **PUT** /mimic/access/load/{filename} | Loads the specified file for access control data. |
| [**accessSave**](AccessApi.md#accessSave) | **PUT** /mimic/access/save/{filename} | Saves current access control data in specified file. |
| [**accessSetAcldb**](AccessApi.md#accessSetAcldb) | **PUT** /mimic/access/set/acldb/{databaseName} | Allows setting the name of the current access control database. |
| [**accessSetEnabled**](AccessApi.md#accessSetEnabled) | **PUT** /mimic/access/set/enabled/{enabledOrNot} | Allows the user to enable/disable the access control check. |


<a id="accessAdd"></a>
# **accessAdd**
> String accessAdd(user, agents, mask)

Adds/Overwrites the user entry in the access control database.

Adds/Overwrites the user entry in the access control database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AccessApi apiInstance = new AccessApi(defaultClient);
    String user = "user_example"; // String | Username of the simulator hosting system
    String agents = "agents_example"; // String | Agent range in minimal range representation
    String mask = "mask_example"; // String | Currently not used
    try {
      String result = apiInstance.accessAdd(user, agents, mask);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessApi#accessAdd");
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
| **user** | **String**| Username of the simulator hosting system | |
| **agents** | **String**| Agent range in minimal range representation | |
| **mask** | **String**| Currently not used | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="accessDel"></a>
# **accessDel**
> String accessDel(user)

Clears a users entry from access control database.

Using &#39;*&#39; for user clears all the users.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AccessApi apiInstance = new AccessApi(defaultClient);
    String user = "user_example"; // String | username of the simulator hosting system
    try {
      String result = apiInstance.accessDel(user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessApi#accessDel");
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
| **user** | **String**| username of the simulator hosting system | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="accessGetAcldb"></a>
# **accessGetAcldb**
> String accessGetAcldb()

Returns the current access control database in use.

If nothing is specified then this returns \&quot;\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AccessApi apiInstance = new AccessApi(defaultClient);
    try {
      String result = apiInstance.accessGetAcldb();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessApi#accessGetAcldb");
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

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="accessGetAdmindir"></a>
# **accessGetAdmindir**
> String accessGetAdmindir()

Returns the current admin directory.

If nothing is specified in admin/settings.cfg then returns \&quot;\&quot;. If no admin directory is specified then the shared area will be used where needed (e.g. for persistent info, access control data files etc. )

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AccessApi apiInstance = new AccessApi(defaultClient);
    try {
      String result = apiInstance.accessGetAdmindir();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessApi#accessGetAdmindir");
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

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="accessGetAdminuser"></a>
# **accessGetAdminuser**
> String accessGetAdminuser()

Returns the current administrator.

If nothing is specified in admin/settings.cfg then returns \&quot;\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AccessApi apiInstance = new AccessApi(defaultClient);
    try {
      String result = apiInstance.accessGetAdminuser();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessApi#accessGetAdminuser");
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

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="accessGetEnabled"></a>
# **accessGetEnabled**
> String accessGetEnabled()

Returns the state of access control checking.

0 indicates that it is disabled, 1 indicates it is enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AccessApi apiInstance = new AccessApi(defaultClient);
    try {
      String result = apiInstance.accessGetEnabled();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessApi#accessGetEnabled");
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

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="accessList"></a>
# **accessList**
> List&lt;AccessEntry&gt; accessList()

Returns an array of entries.

Each entry consists of user, agents (in minimal range representation) and access mask (not used currently).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AccessApi apiInstance = new AccessApi(defaultClient);
    try {
      List<AccessEntry> result = apiInstance.accessList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessApi#accessList");
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

[**List&lt;AccessEntry&gt;**](AccessEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="accessLoad"></a>
# **accessLoad**
> List&lt;String&gt; accessLoad(filename)

Loads the specified file for access control data.

If filename is not specified then the currently set &#39;acldb&#39; parameter is used.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AccessApi apiInstance = new AccessApi(defaultClient);
    String filename = "filename_example"; // String | Filename to load
    try {
      List<String> result = apiInstance.accessLoad(filename);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessApi#accessLoad");
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
| **filename** | **String**| Filename to load | |

### Return type

**List&lt;String&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="accessSave"></a>
# **accessSave**
> List&lt;String&gt; accessSave(filename)

Saves current access control data in specified file.

If filename is not specified then the currently set &#39;acldb&#39; parameter is used.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AccessApi apiInstance = new AccessApi(defaultClient);
    String filename = "filename_example"; // String | Filename to save
    try {
      List<String> result = apiInstance.accessSave(filename);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessApi#accessSave");
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
| **filename** | **String**| Filename to save | |

### Return type

**List&lt;String&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="accessSetAcldb"></a>
# **accessSetAcldb**
> String accessSetAcldb(databaseName)

Allows setting the name of the current access control database.

This will be used for subsequent load and save operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AccessApi apiInstance = new AccessApi(defaultClient);
    String databaseName = "databaseName_example"; // String | Database name to use
    try {
      String result = apiInstance.accessSetAcldb(databaseName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessApi#accessSetAcldb");
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
| **databaseName** | **String**| Database name to use | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="accessSetEnabled"></a>
# **accessSetEnabled**
> String accessSetEnabled(enabledOrNot)

Allows the user to enable/disable the access control check.

0 indicates disabled, 1 indicates enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AccessApi apiInstance = new AccessApi(defaultClient);
    String enabledOrNot = "enabledOrNot_example"; // String | indicator
    try {
      String result = apiInstance.accessSetEnabled(enabledOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessApi#accessSetEnabled");
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
| **enabledOrNot** | **String**| indicator | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

