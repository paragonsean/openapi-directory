# ManagementApi

All URIs are relative to *https://api.nextauth.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApiKey**](ManagementApi.md#createApiKey) | **POST** /apikeys/ | Create a new API key. |
| [**getAllPermissions**](ManagementApi.md#getAllPermissions) | **GET** /servers/{serverid}/permissions/ | Get all permissions for the specified server. |
| [**getApiKeys**](ManagementApi.md#getApiKeys) | **GET** /apikeys/ | Get all API keys. |
| [**getOrCreateUserRole**](ManagementApi.md#getOrCreateUserRole) | **POST** /servers/{serverid}/users/{userid}/role/ | Get or create a role for a specific user. |
| [**getPermissions**](ManagementApi.md#getPermissions) | **GET** /servers/{serverid}/permissions/{roleid} | Get all permissions for the specified server and role. |
| [**getUserRole**](ManagementApi.md#getUserRole) | **GET** /servers/{serverid}/users/{userid}/role/ | Get role for a specific user. |
| [**grantPermissions**](ManagementApi.md#grantPermissions) | **POST** /servers/{serverid}/permissions/{roleid} | Set new permissions for the specified role on a server |
| [**revokePermissions**](ManagementApi.md#revokePermissions) | **DELETE** /servers/{serverid}/permissions/{roleid} | Revoke all permissions for the specified server and role. |


<a id="createApiKey"></a>
# **createApiKey**
> ApiKey createApiKey(description)

Create a new API key.

Create a new API key. Required permission: global &#39;servers&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    ManagementApi apiInstance = new ManagementApi(defaultClient);
    String description = "description_example"; // String | Description for the new role
    try {
      ApiKey result = apiInstance.createApiKey(description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementApi#createApiKey");
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
| **description** | **String**| Description for the new role | |

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newly created apikey (with role and description) |  -  |

<a id="getAllPermissions"></a>
# **getAllPermissions**
> Permissions getAllPermissions(serverid)

Get all permissions for the specified server.

Returns all permissions. Required permission: &#39;servers&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    ManagementApi apiInstance = new ManagementApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    try {
      Permissions result = apiInstance.getAllPermissions(serverid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementApi#getAllPermissions");
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
| **serverid** | **String**| Base64 encoded server id | |

### Return type

[**Permissions**](Permissions.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of roles and permissions |  -  |
| **404** | Server not found |  -  |

<a id="getApiKeys"></a>
# **getApiKeys**
> ApiKeys getApiKeys()

Get all API keys.

Get all API keys generated by the current role. Required permission: global &#39;servers&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    ManagementApi apiInstance = new ManagementApi(defaultClient);
    try {
      ApiKeys result = apiInstance.getApiKeys();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementApi#getApiKeys");
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

[**ApiKeys**](ApiKeys.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of apikeys (with role and description) |  -  |

<a id="getOrCreateUserRole"></a>
# **getOrCreateUserRole**
> GetOrCreateUserRole200Response getOrCreateUserRole(serverid, userid)

Get or create a role for a specific user.

Get or create a role for a specific user. Required permission: &#39;users&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    ManagementApi apiInstance = new ManagementApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String userid = "userid_example"; // String | User name
    try {
      GetOrCreateUserRole200Response result = apiInstance.getOrCreateUserRole(serverid, userid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementApi#getOrCreateUserRole");
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
| **serverid** | **String**| Base64 encoded server id | |
| **userid** | **String**| User name | |

### Return type

[**GetOrCreateUserRole200Response**](GetOrCreateUserRole200Response.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User role (base 64 encoded) |  -  |
| **404** | User not found |  -  |

<a id="getPermissions"></a>
# **getPermissions**
> Permissions getPermissions(serverid, roleid)

Get all permissions for the specified server and role.

Returns all permissions. Required permission: &#39;servers&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    ManagementApi apiInstance = new ManagementApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String roleid = "roleid_example"; // String | Base64 encoded role id
    try {
      Permissions result = apiInstance.getPermissions(serverid, roleid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementApi#getPermissions");
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
| **serverid** | **String**| Base64 encoded server id | |
| **roleid** | **String**| Base64 encoded role id | |

### Return type

[**Permissions**](Permissions.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of roles and permissions |  -  |
| **404** | Server or role not found |  -  |

<a id="getUserRole"></a>
# **getUserRole**
> Role getUserRole(serverid, userid)

Get role for a specific user.

Get role for a specific user. Required permission: &#39;users&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    ManagementApi apiInstance = new ManagementApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String userid = "userid_example"; // String | User name
    try {
      Role result = apiInstance.getUserRole(serverid, userid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementApi#getUserRole");
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
| **serverid** | **String**| Base64 encoded server id | |
| **userid** | **String**| User name | |

### Return type

[**Role**](Role.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User role (base 64 encoded) |  -  |
| **404** | User not found, no role found for user |  -  |

<a id="grantPermissions"></a>
# **grantPermissions**
> grantPermissions(serverid, roleid, permissions)

Set new permissions for the specified role on a server

Set new permissions for the specified role on a server. This overwrites any existing permissions on this server for the specified role. Required permission: &#39;root&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    ManagementApi apiInstance = new ManagementApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String roleid = "roleid_example"; // String | Base64 encoded role id
    List<String> permissions = Arrays.asList(); // List<String> | Array of new permissions
    try {
      apiInstance.grantPermissions(serverid, roleid, permissions);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementApi#grantPermissions");
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
| **serverid** | **String**| Base64 encoded server id | |
| **roleid** | **String**| Base64 encoded role id | |
| **permissions** | [**List&lt;String&gt;**](String.md)| Array of new permissions | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok |  -  |
| **404** | Server or role not found |  -  |

<a id="revokePermissions"></a>
# **revokePermissions**
> revokePermissions(serverid, roleid)

Revoke all permissions for the specified server and role.

Revoke all permissions for the specified server and role. Required permission: &#39;root&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    ManagementApi apiInstance = new ManagementApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String roleid = "roleid_example"; // String | Base64 encoded role id
    try {
      apiInstance.revokePermissions(serverid, roleid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementApi#revokePermissions");
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
| **serverid** | **String**| Base64 encoded server id | |
| **roleid** | **String**| Base64 encoded role id | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok |  -  |
| **404** | Server or role not found |  -  |

