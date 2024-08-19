# NoScopeApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**heartBeatGetAuthorization**](NoScopeApi.md#heartBeatGetAuthorization) | **GET** /heartbeat/authorized | Returns http status code 204 for successful authentication. |
| [**heartBeatGetDatabaseStatus**](NoScopeApi.md#heartBeatGetDatabaseStatus) | **GET** /heartbeat/database | Can be used to check the status of the database. |
| [**heartBeatGetServerStatus**](NoScopeApi.md#heartBeatGetServerStatus) | **GET** /heartbeat/server | Can be used to check the status of the REST Api. |
| [**publicBearerAuthenticationGetAccessTokenJson**](NoScopeApi.md#publicBearerAuthenticationGetAccessTokenJson) | **POST** /v1/login/oauth/access_token | Get oAuth2 access token. |
| [**publicBearerAuthenticationGetAccessTokenTokenFromRefreshToken**](NoScopeApi.md#publicBearerAuthenticationGetAccessTokenTokenFromRefreshToken) | **POST** /v1/refreshtoken | Get new access token using a refresh token. |
| [**publicBearerAuthenticationGetAuthorizationCode**](NoScopeApi.md#publicBearerAuthenticationGetAuthorizationCode) | **GET** /v1/login/oauth/authorize | Get the oAuth2 authorization code flow code. |
| [**publicBearerAuthenticationGetLoginToken**](NoScopeApi.md#publicBearerAuthenticationGetLoginToken) | **POST** /v1/token | Can be used to get the login information and access token for the api client. |
| [**publicBearerAuthenticationLogout**](NoScopeApi.md#publicBearerAuthenticationLogout) | **POST** /v1/signout | Logout. Invalidates refresh token. Access token will be invalid when it expires. |


<a id="heartBeatGetAuthorization"></a>
# **heartBeatGetAuthorization**
> heartBeatGetAuthorization()

Returns http status code 204 for successful authentication.

This route requires authentication, returns 204 http status when successful.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    NoScopeApi apiInstance = new NoScopeApi(defaultClient);
    try {
      apiInstance.heartBeatGetAuthorization();
    } catch (ApiException e) {
      System.err.println("Exception when calling NoScopeApi#heartBeatGetAuthorization");
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

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="heartBeatGetDatabaseStatus"></a>
# **heartBeatGetDatabaseStatus**
> File heartBeatGetDatabaseStatus()

Can be used to check the status of the database.

This does not require authentication.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");

    NoScopeApi apiInstance = new NoScopeApi(defaultClient);
    try {
      File result = apiInstance.heartBeatGetDatabaseStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NoScopeApi#heartBeatGetDatabaseStatus");
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

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns message \&quot;Database is alive.\&quot; |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="heartBeatGetServerStatus"></a>
# **heartBeatGetServerStatus**
> File heartBeatGetServerStatus()

Can be used to check the status of the REST Api.

This does not require authentication.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");

    NoScopeApi apiInstance = new NoScopeApi(defaultClient);
    try {
      File result = apiInstance.heartBeatGetServerStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NoScopeApi#heartBeatGetServerStatus");
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

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns message \&quot;Server is alive.\&quot; |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="publicBearerAuthenticationGetAccessTokenJson"></a>
# **publicBearerAuthenticationGetAccessTokenJson**
> PublicAuthenticationOutputModel publicBearerAuthenticationGetAccessTokenJson(accessTokenCredentials)

Get oAuth2 access token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    NoScopeApi apiInstance = new NoScopeApi(defaultClient);
    AccessTokenCredentials accessTokenCredentials = new AccessTokenCredentials(); // AccessTokenCredentials | AccessTokenCredentials model
    try {
      PublicAuthenticationOutputModel result = apiInstance.publicBearerAuthenticationGetAccessTokenJson(accessTokenCredentials);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NoScopeApi#publicBearerAuthenticationGetAccessTokenJson");
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
| **accessTokenCredentials** | [**AccessTokenCredentials**](AccessTokenCredentials.md)| AccessTokenCredentials model | [optional] |

### Return type

[**PublicAuthenticationOutputModel**](PublicAuthenticationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PublicAuthenticationOutputModel |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="publicBearerAuthenticationGetAccessTokenTokenFromRefreshToken"></a>
# **publicBearerAuthenticationGetAccessTokenTokenFromRefreshToken**
> PublicAuthenticationOutputModel publicBearerAuthenticationGetAccessTokenTokenFromRefreshToken(body)

Get new access token using a refresh token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    NoScopeApi apiInstance = new NoScopeApi(defaultClient);
    String body = "body_example"; // String | Refresh token.
    try {
      PublicAuthenticationOutputModel result = apiInstance.publicBearerAuthenticationGetAccessTokenTokenFromRefreshToken(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NoScopeApi#publicBearerAuthenticationGetAccessTokenTokenFromRefreshToken");
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
| **body** | **String**| Refresh token. | [optional] |

### Return type

[**PublicAuthenticationOutputModel**](PublicAuthenticationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PublicAuthenticationOutputModel |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="publicBearerAuthenticationGetAuthorizationCode"></a>
# **publicBearerAuthenticationGetAuthorizationCode**
> ExceptionModel publicBearerAuthenticationGetAuthorizationCode(responseType, state, clientId, redirectUri, scope)

Get the oAuth2 authorization code flow code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    NoScopeApi apiInstance = new NoScopeApi(defaultClient);
    String responseType = "responseType_example"; // String | code
    String state = "state_example"; // String | Unguessable random string.
    String clientId = "clientId_example"; // String | Client id.
    String redirectUri = "redirectUri_example"; // String | Url where to redirect after code has been retrieved.
    String scope = ""; // String | Scopes that client requests. If scopes that are not allowed for the client are requested, returns unauthorized.
    try {
      ExceptionModel result = apiInstance.publicBearerAuthenticationGetAuthorizationCode(responseType, state, clientId, redirectUri, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NoScopeApi#publicBearerAuthenticationGetAuthorizationCode");
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
| **responseType** | **String**| code | [optional] |
| **state** | **String**| Unguessable random string. | [optional] |
| **clientId** | **String**| Client id. | [optional] |
| **redirectUri** | **String**| Url where to redirect after code has been retrieved. | [optional] |
| **scope** | **String**| Scopes that client requests. If scopes that are not allowed for the client are requested, returns unauthorized. | [optional] [default to ] |

### Return type

[**ExceptionModel**](ExceptionModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="publicBearerAuthenticationGetLoginToken"></a>
# **publicBearerAuthenticationGetLoginToken**
> PublicAuthenticationOutputModel publicBearerAuthenticationGetLoginToken(clientCredentials)

Can be used to get the login information and access token for the api client.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    NoScopeApi apiInstance = new NoScopeApi(defaultClient);
    ClientCredentials clientCredentials = new ClientCredentials(); // ClientCredentials | ClientCredentials of the client.
    try {
      PublicAuthenticationOutputModel result = apiInstance.publicBearerAuthenticationGetLoginToken(clientCredentials);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NoScopeApi#publicBearerAuthenticationGetLoginToken");
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
| **clientCredentials** | [**ClientCredentials**](ClientCredentials.md)| ClientCredentials of the client. | [optional] |

### Return type

[**PublicAuthenticationOutputModel**](PublicAuthenticationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PublicAuthenticationOutputModel |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="publicBearerAuthenticationLogout"></a>
# **publicBearerAuthenticationLogout**
> File publicBearerAuthenticationLogout(body)

Logout. Invalidates refresh token. Access token will be invalid when it expires.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    NoScopeApi apiInstance = new NoScopeApi(defaultClient);
    String body = "body_example"; // String | 
    try {
      File result = apiInstance.publicBearerAuthenticationLogout(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NoScopeApi#publicBearerAuthenticationLogout");
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
| **body** | **String**|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

