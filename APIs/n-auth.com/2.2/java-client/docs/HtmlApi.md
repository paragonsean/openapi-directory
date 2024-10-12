# HtmlApi

All URIs are relative to *https://api.nextauth.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHtmlEnrol**](HtmlApi.md#getHtmlEnrol) | **GET** /servers/{serverid}/sessions/html/enrol | Generate HTML to enrol a new user |
| [**getHtmlFooter**](HtmlApi.md#getHtmlFooter) | **GET** /servers/{serverid}/sessions/html/footer | Generic HTML to add to footer. Required for login/logout/enrol functionality. |
| [**getHtmlLogin**](HtmlApi.md#getHtmlLogin) | **GET** /servers/{serverid}/sessions/html/login | Generate HTML for the login block |
| [**getSession_0**](HtmlApi.md#getSession_0) | **GET** /servers/{serverid}/sessions/ | Check if the user is logged in |
| [**logout_0**](HtmlApi.md#logout_0) | **POST** /servers/{serverid}/sessions/logout | Force a logout on the given session |


<a id="getHtmlEnrol"></a>
# **getHtmlEnrol**
> String getHtmlEnrol(serverid, xNonce, name, userid)

Generate HTML to enrol a new user

Generate HTML to enrol a new user. Required permission: &#39;sessions&#39;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HtmlApi;

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

    HtmlApi apiInstance = new HtmlApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    String name = "name_example"; // String | Name to forward to the nextAuth app for this account
    String userid = "userid_example"; // String | User name to register this user under
    try {
      String result = apiInstance.getHtmlEnrol(serverid, xNonce, name, userid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HtmlApi#getHtmlEnrol");
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
| **name** | **String**| Name to forward to the nextAuth app for this account | [optional] |
| **userid** | **String**| User name to register this user under | [optional] |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated HTML. |  -  |

<a id="getHtmlFooter"></a>
# **getHtmlFooter**
> String getHtmlFooter(serverid, xNonce, htmlFooterBody)

Generic HTML to add to footer. Required for login/logout/enrol functionality.

HTML to add to footer of HTML page. Required permission: &#39;sessions&#39;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HtmlApi;

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

    HtmlApi apiInstance = new HtmlApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    HtmlFooterBody htmlFooterBody = new HtmlFooterBody(); // HtmlFooterBody | Additional sessions that should be monitored through the websocket.
    try {
      String result = apiInstance.getHtmlFooter(serverid, xNonce, htmlFooterBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HtmlApi#getHtmlFooter");
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
| **htmlFooterBody** | [**HtmlFooterBody**](HtmlFooterBody.md)| Additional sessions that should be monitored through the websocket. | [optional] |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated HTML. |  -  |

<a id="getHtmlLogin"></a>
# **getHtmlLogin**
> String getHtmlLogin(serverid, xNonce, userContext)

Generate HTML for the login block

Generate HTML for the login block. Required permission: &#39;sessions&#39;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HtmlApi;

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

    HtmlApi apiInstance = new HtmlApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    UserContext userContext = new UserContext(); // UserContext | Session information to display to user.
    try {
      String result = apiInstance.getHtmlLogin(serverid, xNonce, userContext);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HtmlApi#getHtmlLogin");
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

**String**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated HTML. |  -  |

<a id="getSession_0"></a>
# **getSession_0**
> LoginStatus getSession_0(serverid, xNonce)

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
import org.openapitools.client.api.HtmlApi;

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

    HtmlApi apiInstance = new HtmlApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    try {
      LoginStatus result = apiInstance.getSession_0(serverid, xNonce);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HtmlApi#getSession_0");
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

<a id="logout_0"></a>
# **logout_0**
> logout_0(serverid, xNonce)

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
import org.openapitools.client.api.HtmlApi;

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

    HtmlApi apiInstance = new HtmlApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    try {
      apiInstance.logout_0(serverid, xNonce);
    } catch (ApiException e) {
      System.err.println("Exception when calling HtmlApi#logout_0");
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

