# AuthenticationApi

All URIs are relative to *https://ioe2api.ijenko.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authAccountLogin**](AuthenticationApi.md#authAccountLogin) | **POST** /auth/login | Get a token using login+password |
| [**authRefreshToken**](AuthenticationApi.md#authRefreshToken) | **POST** /auth/refresh | Refresh a token |
| [**authResetPassword**](AuthenticationApi.md#authResetPassword) | **POST** /auth/reset-password | Ask for a new password |
| [**authRevokeToken**](AuthenticationApi.md#authRevokeToken) | **POST** /auth/revoke | Revoke a token |


<a id="authAccountLogin"></a>
# **authAccountLogin**
> AuthTokens authAccountLogin(loginInfo)

Get a token using login+password

Get an access+refresh tokens pair from login and password information.  The *access token* obtained with this request can then be used in an &#x60;Access-Token&#x60; HTTP header or in a &#x60;token&#x60; URL query parameter in requests that require authentication.  The *refresh token* can be used with &#x60;/auth/refresh&#x60; when the *access token* expires to retrieve a new *access token*. The lifetime of the refresh token is the maximum lifetime of this authentication request.  The default lifetime of the *refresh token* is defined by the &#x60;appId&#x60; used. The &#x60;ttl&#x60; input parameter allows to request a *refresh token* with a shorter lifetime.  To implement *logout*, use &#x60;/auth/revoke&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    AuthLogin loginInfo = new AuthLogin(); // AuthLogin | Login information.
    try {
      AuthTokens result = apiInstance.authAccountLogin(loginInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authAccountLogin");
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
| **loginInfo** | [**AuthLogin**](AuthLogin.md)| Login information. | |

### Return type

[**AuthTokens**](AuthTokens.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Login successful. The access token is given to use the API. The refresh token must be stored in a safe place. |  -  |
| **401** | Authentication failure. |  -  |
| **0** | Other error. |  -  |

<a id="authRefreshToken"></a>
# **authRefreshToken**
> AuthTokens authRefreshToken(refreshInfo)

Refresh a token

Get a new *access token* using a valid *refresh token*.  This is a **replacement** of the *access token*: if an existing *access token* was still not expired, it is invalidated. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    AuthRefresh refreshInfo = new AuthRefresh(); // AuthRefresh | Refresh token information.
    try {
      AuthTokens result = apiInstance.authRefreshToken(refreshInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authRefreshToken");
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
| **refreshInfo** | [**AuthRefresh**](AuthRefresh.md)| Refresh token information. | |

### Return type

[**AuthTokens**](AuthTokens.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Refresh successful. A new access token is given to use the API. |  -  |
| **401** | Authentication failure. |  -  |
| **0** | Other error. |  -  |

<a id="authResetPassword"></a>
# **authResetPassword**
> authResetPassword(resetPasswordInfo)

Ask for a new password

Trigger the request of a new password.  The account administrator will receive an e-mail with an URL pointing to a form to allow him/her to enter a new password. The old password is still functional until a new one is submitted.  Either the login or e-mail of the account must be given. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    AuthResetPassword resetPasswordInfo = new AuthResetPassword(); // AuthResetPassword | Account identification information
    try {
      apiInstance.authResetPassword(resetPasswordInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authResetPassword");
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
| **resetPasswordInfo** | [**AuthResetPassword**](AuthResetPassword.md)| Account identification information | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | As this request is not authenticated, response is always successful to not reveal (in)existence of accounts. |  -  |
| **0** | Other error. |  -  |

<a id="authRevokeToken"></a>
# **authRevokeToken**
> authRevokeToken()

Revoke a token

Invalidate the authentication used for the request. The access token and the refresh token will be invalid after this request. This request is typically called to implement logout. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    try {
      apiInstance.authRevokeToken();
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authRevokeToken");
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

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Revocation successful. The token used for the request is now invalid. |  -  |
| **401** | Authentication failure. |  -  |
| **0** | Other error. |  -  |

