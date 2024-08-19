# PermissionAddAndRemovePermissionsApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**permissionAppsAppIdDelete**](PermissionAddAndRemovePermissionsApi.md#permissionAppsAppIdDelete) | **DELETE** /permission/apps/{appId} | Removes permission that allows the app to access this user&#39;s data |
| [**permissionAppsAppIdGet**](PermissionAddAndRemovePermissionsApi.md#permissionAppsAppIdGet) | **GET** /permission/apps/{appId} | Returns permission that allows the app to access this user&#39;s data |
| [**permissionAppsAppIdPost**](PermissionAddAndRemovePermissionsApi.md#permissionAppsAppIdPost) | **POST** /permission/apps/{appId} | Adds permission to allow the app to access this user&#39;s data |


<a id="permissionAppsAppIdDelete"></a>
# **permissionAppsAppIdDelete**
> permissionAppsAppIdDelete(appId, userId)

Removes permission that allows the app to access this user&#39;s data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionAddAndRemovePermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PermissionAddAndRemovePermissionsApi apiInstance = new PermissionAddAndRemovePermissionsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the app
    String userId = "userId_example"; // String | The id of the user
    try {
      apiInstance.permissionAppsAppIdDelete(appId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionAddAndRemovePermissionsApi#permissionAppsAppIdDelete");
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
| **appId** | **String**| The id of the app | |
| **userId** | **String**| The id of the user | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - The access is not found |  -  |

<a id="permissionAppsAppIdGet"></a>
# **permissionAppsAppIdGet**
> Access permissionAppsAppIdGet(appId, userId)

Returns permission that allows the app to access this user&#39;s data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionAddAndRemovePermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PermissionAddAndRemovePermissionsApi apiInstance = new PermissionAddAndRemovePermissionsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the app
    String userId = "userId_example"; // String | The id of the user
    try {
      Access result = apiInstance.permissionAppsAppIdGet(appId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionAddAndRemovePermissionsApi#permissionAppsAppIdGet");
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
| **appId** | **String**| The id of the app | |
| **userId** | **String**| The id of the user | |

### Return type

[**Access**](Access.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - The access is not found |  -  |
| **0** | OK |  -  |

<a id="permissionAppsAppIdPost"></a>
# **permissionAppsAppIdPost**
> Access permissionAppsAppIdPost(appId, userId, date, ip)

Adds permission to allow the app to access this user&#39;s data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionAddAndRemovePermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PermissionAddAndRemovePermissionsApi apiInstance = new PermissionAddAndRemovePermissionsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the app
    String userId = "userId_example"; // String | The id of the user
    Long date = 56L; // Long | The time (in milliseconds) of when the user agreed to the access request
    String ip = "ip_example"; // String | The ip address of the user agreeing to the access request
    try {
      Access result = apiInstance.permissionAppsAppIdPost(appId, userId, date, ip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionAddAndRemovePermissionsApi#permissionAppsAppIdPost");
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
| **appId** | **String**| The id of the app | |
| **userId** | **String**| The id of the user | |
| **date** | **Long**| The time (in milliseconds) of when the user agreed to the access request | [optional] |
| **ip** | **String**| The ip address of the user agreeing to the access request | [optional] |

### Return type

[**Access**](Access.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - App not found |  -  |
| **0** | OK |  -  |

