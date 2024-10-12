# AuthApi

All URIs are relative to *https://openapi.space/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**login**](AuthApi.md#login) | **POST** /auth/login | Log in to OpenAPI space |
| [**loginApinf**](AuthApi.md#loginApinf) | **POST** /auth/login/apinf | Log in to OpenAPI space using an APInf account |
| [**loginApinfToken**](AuthApi.md#loginApinfToken) | **POST** /auth/login/apinf_token | Log in to OpenAPI space using an APInf authentication token |
| [**logout**](AuthApi.md#logout) | **POST** /auth/logout | Log out from OpenAPI space |
| [**ping**](AuthApi.md#ping) | **POST** /auth/ping | Check whether or not you are authenticated |
| [**register**](AuthApi.md#register) | **POST** /auth/register | Register to OpenAPI space |


<a id="login"></a>
# **login**
> LoginToken login(body)

Log in to OpenAPI space

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
    defaultClient.setBasePath("https://openapi.space/api/v1");

    AuthApi apiInstance = new AuthApi(defaultClient);
    Credentials body = new Credentials(); // Credentials | the user credentials
    try {
      LoginToken result = apiInstance.login(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#login");
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
| **body** | [**Credentials**](Credentials.md)| the user credentials | [optional] |

### Return type

[**LoginToken**](LoginToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | login successful |  -  |
| **401** | invalid password |  -  |
| **404** | user not found |  -  |

<a id="loginApinf"></a>
# **loginApinf**
> LoginToken loginApinf(body)

Log in to OpenAPI space using an APInf account

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
    defaultClient.setBasePath("https://openapi.space/api/v1");

    AuthApi apiInstance = new AuthApi(defaultClient);
    LoginApinfRequest body = new LoginApinfRequest(); // LoginApinfRequest | the APInf username and password
    try {
      LoginToken result = apiInstance.loginApinf(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#loginApinf");
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
| **body** | [**LoginApinfRequest**](LoginApinfRequest.md)| the APInf username and password | [optional] |

### Return type

[**LoginToken**](LoginToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | login successful |  -  |
| **401** | invalid username or password |  -  |

<a id="loginApinfToken"></a>
# **loginApinfToken**
> LoginToken loginApinfToken(body)

Log in to OpenAPI space using an APInf authentication token

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
    defaultClient.setBasePath("https://openapi.space/api/v1");

    AuthApi apiInstance = new AuthApi(defaultClient);
    LoginApinfTokenRequest body = new LoginApinfTokenRequest(); // LoginApinfTokenRequest | the APInf authentication token and user ID
    try {
      LoginToken result = apiInstance.loginApinfToken(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#loginApinfToken");
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
| **body** | [**LoginApinfTokenRequest**](LoginApinfTokenRequest.md)| the APInf authentication token and user ID | [optional] |

### Return type

[**LoginToken**](LoginToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | login successful |  -  |
| **401** | invalid user ID or auth token |  -  |

<a id="logout"></a>
# **logout**
> logout()

Log out from OpenAPI space

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
    defaultClient.setBasePath("https://openapi.space/api/v1");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      apiInstance.logout();
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#logout");
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

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | logout successful |  -  |
| **403** | user was not logged in |  -  |

<a id="ping"></a>
# **ping**
> Registration ping()

Check whether or not you are authenticated

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
    defaultClient.setBasePath("https://openapi.space/api/v1");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      Registration result = apiInstance.ping();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#ping");
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

[**Registration**](Registration.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | logged in |  -  |
| **403** | not logged in |  -  |

<a id="register"></a>
# **register**
> LoginToken register(body)

Register to OpenAPI space

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
    defaultClient.setBasePath("https://openapi.space/api/v1");

    AuthApi apiInstance = new AuthApi(defaultClient);
    Registration body = new Registration(); // Registration | registration details
    try {
      LoginToken result = apiInstance.register(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#register");
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
| **body** | [**Registration**](Registration.md)| registration details | [optional] |

### Return type

[**LoginToken**](LoginToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | registration successful |  -  |
| **409** | username or email taken |  -  |

