# SessionsApi

All URIs are relative to *https://api.nextauth.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getQrLogin**](SessionsApi.md#getQrLogin) | **GET** /servers/{serverid}/sessions/qr/login | Generate data for a login qr code |
| [**getSession**](SessionsApi.md#getSession) | **GET** /servers/{serverid}/sessions/ | Check if the user is logged in |
| [**logout**](SessionsApi.md#logout) | **POST** /servers/{serverid}/sessions/logout | Force a logout on the given session |
| [**provokeLogin**](SessionsApi.md#provokeLogin) | **POST** /servers/{serverid}/sessions/provokelogin | Push a login confirmation to the user&#39;s app |
| [**provokeLoginOnAccount**](SessionsApi.md#provokeLoginOnAccount) | **POST** /servers/{serverid}/accounts/{accountid}/provokelogin | Push a login confirmation to the user&#39;s app |
| [**provokeLoginOnUser**](SessionsApi.md#provokeLoginOnUser) | **POST** /servers/{serverid}/users/{userid}/provokelogin | Push a login confirmation to the user&#39;s app |


<a id="getQrLogin"></a>
# **getQrLogin**
> File getQrLogin(serverid, xNonce, img, s, userContext)

Generate data for a login qr code

Returns the data for a login qr code. Required permission: &#39;sessions&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

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

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    String img = "img_example"; // String | \"png\" for a PNG image, not set for raw data in the qr code
    Integer s = 56; // Integer | size in pixels of the qr code, defaults to 500
    UserContext userContext = new UserContext(); // UserContext | Session information to display to user.
    try {
      File result = apiInstance.getQrLogin(serverid, xNonce, img, s, userContext);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#getQrLogin");
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
| **xNonce** | **String**| Nonce to identify the browser/webserver session | |
| **img** | **String**| \&quot;png\&quot; for a PNG image, not set for raw data in the qr code | [optional] |
| **s** | **Integer**| size in pixels of the qr code, defaults to 500 | [optional] |
| **userContext** | [**UserContext**](UserContext.md)| Session information to display to user. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Raw byte array containing the login qr code data (either raw or as a PNG image). |  -  |

<a id="getSession"></a>
# **getSession**
> LoginStatus getSession(serverid, xNonce)

Check if the user is logged in

Based on the browser/webserver session identifier, check if the user is logged in and return the associated username. This also returns additional information: the data for the login qr code and whether or not a loggin can be provoked directly from the server. Required permission: &#39;sessions&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

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

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    try {
      LoginStatus result = apiInstance.getSession(serverid, xNonce);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#getSession");
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
| **xNonce** | **String**| Nonce to identify the browser/webserver session | |

### Return type

[**LoginStatus**](LoginStatus.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current login status. |  -  |

<a id="logout"></a>
# **logout**
> logout(serverid, xNonce)

Force a logout on the given session

Force a logout on the given session. Required permission: &#39;sessions&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

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

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    try {
      apiInstance.logout(serverid, xNonce);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#logout");
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
| **xNonce** | **String**| Nonce to identify the browser/webserver session | |

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

<a id="provokeLogin"></a>
# **provokeLogin**
> provokeLogin(serverid, xNonce, userContext)

Push a login confirmation to the user&#39;s app

Push a login to the nextAuth app for the user to confirm, based on last account that successfully logged in for the given session. Required permission: &#39;sessions&#39;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

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

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    UserContext userContext = new UserContext(); // UserContext | Session information to display to user.
    try {
      apiInstance.provokeLogin(serverid, xNonce, userContext);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#provokeLogin");
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
| **xNonce** | **String**| Nonce to identify the browser/webserver session | |
| **userContext** | [**UserContext**](UserContext.md)| Session information to display to user. | [optional] |

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
| **200** | OK |  -  |

<a id="provokeLoginOnAccount"></a>
# **provokeLoginOnAccount**
> provokeLoginOnAccount(serverid, xNonce, accountid, userContext)

Push a login confirmation to the user&#39;s app

Push a login to the nextAuth app for the user to confirm, based on the given account (app instance). Required permission: &#39;sessions&#39; or &#39;accounts&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

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

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Base64 encoded nonce to identify the browser/webserver session
    Integer accountid = 56; // Integer | Account id
    UserContext userContext = new UserContext(); // UserContext | Session information to display to user
    try {
      apiInstance.provokeLoginOnAccount(serverid, xNonce, accountid, userContext);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#provokeLoginOnAccount");
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
| **xNonce** | **String**| Base64 encoded nonce to identify the browser/webserver session | |
| **accountid** | **Integer**| Account id | |
| **userContext** | [**UserContext**](UserContext.md)| Session information to display to user | [optional] |

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
| **200** | OK |  -  |

<a id="provokeLoginOnUser"></a>
# **provokeLoginOnUser**
> provokeLoginOnUser(serverid, xNonce, userid, userContext)

Push a login confirmation to the user&#39;s app

Push a login to the nextAuth app for the user to confirm, based on the given userid. Required permission: &#39;sessions&#39; or &#39;users&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

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

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    String userid = "userid_example"; // String | User name
    UserContext userContext = new UserContext(); // UserContext | Session information to display to user.
    try {
      apiInstance.provokeLoginOnUser(serverid, xNonce, userid, userContext);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#provokeLoginOnUser");
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
| **xNonce** | **String**| Nonce to identify the browser/webserver session | |
| **userid** | **String**| User name | |
| **userContext** | [**UserContext**](UserContext.md)| Session information to display to user. | [optional] |

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
| **200** | OK |  -  |

