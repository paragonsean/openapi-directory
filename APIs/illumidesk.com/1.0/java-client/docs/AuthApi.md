# AuthApi

All URIs are relative to *https://api.illumidesk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authJwtTokenAuth**](AuthApi.md#authJwtTokenAuth) | **POST** /auth/jwt-token-auth/ | Create JSON Web Token (JWT) |
| [**authJwtTokenRefresh**](AuthApi.md#authJwtTokenRefresh) | **POST** /auth/jwt-token-refresh/ | Refresh a JSON Web Token (JWT) |
| [**authJwtTokenVerify**](AuthApi.md#authJwtTokenVerify) | **POST** /auth/jwt-token-verify/ | Validate JSON Web Token (JWT) |
| [**authRegister**](AuthApi.md#authRegister) | **POST** /auth/register/ | Register a user |
| [**oauthLogin**](AuthApi.md#oauthLogin) | **GET** /auth/login/{provider}/ |  |


<a id="authJwtTokenAuth"></a>
# **authJwtTokenAuth**
> JWT authJwtTokenAuth(jwtData)

Create JSON Web Token (JWT)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");

    AuthApi apiInstance = new AuthApi(defaultClient);
    JWTData jwtData = new JWTData(); // JWTData | 
    try {
      JWT result = apiInstance.authJwtTokenAuth(jwtData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authJwtTokenAuth");
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
| **jwtData** | [**JWTData**](JWTData.md)|  | [optional] |

### Return type

[**JWT**](JWT.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | JWT created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="authJwtTokenRefresh"></a>
# **authJwtTokenRefresh**
> RefreshJSONWebToken authJwtTokenRefresh(refreshjwtData)

Refresh a JSON Web Token (JWT)

Obtains a new JSON Web Token using existing user credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");

    AuthApi apiInstance = new AuthApi(defaultClient);
    RefreshJSONWebTokenData refreshjwtData = new RefreshJSONWebTokenData(); // RefreshJSONWebTokenData | 
    try {
      RefreshJSONWebToken result = apiInstance.authJwtTokenRefresh(refreshjwtData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authJwtTokenRefresh");
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
| **refreshjwtData** | [**RefreshJSONWebTokenData**](RefreshJSONWebTokenData.md)|  | [optional] |

### Return type

[**RefreshJSONWebToken**](RefreshJSONWebToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | RefreshJSONWebToken created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="authJwtTokenVerify"></a>
# **authJwtTokenVerify**
> VerifyJSONWebToken authJwtTokenVerify(verifyjwtData)

Validate JSON Web Token (JWT)

Checks veraciy of token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");

    AuthApi apiInstance = new AuthApi(defaultClient);
    VerifyJSONWebTokenData verifyjwtData = new VerifyJSONWebTokenData(); // VerifyJSONWebTokenData | 
    try {
      VerifyJSONWebToken result = apiInstance.authJwtTokenVerify(verifyjwtData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authJwtTokenVerify");
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
| **verifyjwtData** | [**VerifyJSONWebTokenData**](VerifyJSONWebTokenData.md)|  | [optional] |

### Return type

[**VerifyJSONWebToken**](VerifyJSONWebToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | VerifyJSONWebToken created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="authRegister"></a>
# **authRegister**
> User authRegister(userData)

Register a user

User registration requires confirming email address to activate user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");

    AuthApi apiInstance = new AuthApi(defaultClient);
    UserData userData = new UserData(); // UserData | 
    try {
      User result = apiInstance.authRegister(userData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authRegister");
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
| **userData** | [**UserData**](UserData.md)|  | [optional] |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | User created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="oauthLogin"></a>
# **oauthLogin**
> oauthLogin(provider)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String provider = "github"; // String | OAuth2 provider
    try {
      apiInstance.oauthLogin(provider);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#oauthLogin");
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
| **provider** | **String**| OAuth2 provider | [enum: github, google, slack] |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Redirect to backend auth page |  -  |

