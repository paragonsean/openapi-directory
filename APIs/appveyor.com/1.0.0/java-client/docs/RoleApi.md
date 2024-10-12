# RoleApi

All URIs are relative to *https://ci.appveyor.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addRole**](RoleApi.md#addRole) | **POST** /roles | Add role |
| [**deleteRole**](RoleApi.md#deleteRole) | **DELETE** /roles/{roleId} | Delete role |
| [**getRole**](RoleApi.md#getRole) | **GET** /roles/{roleId} | Get role |
| [**getRoles**](RoleApi.md#getRoles) | **GET** /roles | Get roles |
| [**updateRole**](RoleApi.md#updateRole) | **PUT** /roles | Update role |


<a id="addRole"></a>
# **addRole**
> RoleWithGroups addRole(body)

Add role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    RoleApi apiInstance = new RoleApi(defaultClient);
    RoleAddition body = new RoleAddition(); // RoleAddition | 
    try {
      RoleWithGroups result = apiInstance.addRole(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleApi#addRole");
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
| **body** | [**RoleAddition**](RoleAddition.md)|  | |

### Return type

[**RoleWithGroups**](RoleWithGroups.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="deleteRole"></a>
# **deleteRole**
> deleteRole(roleId)

Delete role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    RoleApi apiInstance = new RoleApi(defaultClient);
    Integer roleId = 56; // Integer | Role ID
    try {
      apiInstance.deleteRole(roleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleApi#deleteRole");
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
| **roleId** | **Integer**| Role ID | |

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="getRole"></a>
# **getRole**
> RoleWithGroups getRole(roleId)

Get role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    RoleApi apiInstance = new RoleApi(defaultClient);
    Integer roleId = 56; // Integer | Role ID
    try {
      RoleWithGroups result = apiInstance.getRole(roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleApi#getRole");
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
| **roleId** | **Integer**| Role ID | |

### Return type

[**RoleWithGroups**](RoleWithGroups.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getRoles"></a>
# **getRoles**
> List&lt;Role&gt; getRoles()

Get roles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    RoleApi apiInstance = new RoleApi(defaultClient);
    try {
      List<Role> result = apiInstance.getRoles();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleApi#getRoles");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="updateRole"></a>
# **updateRole**
> RoleWithGroups updateRole(body)

Update role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    RoleApi apiInstance = new RoleApi(defaultClient);
    RoleWithGroups body = new RoleWithGroups(); // RoleWithGroups | 
    try {
      RoleWithGroups result = apiInstance.updateRole(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleApi#updateRole");
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
| **body** | [**RoleWithGroups**](RoleWithGroups.md)|  | |

### Return type

[**RoleWithGroups**](RoleWithGroups.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

