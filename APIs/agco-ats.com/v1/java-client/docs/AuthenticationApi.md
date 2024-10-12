# AuthenticationApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authenticationDefault**](AuthenticationApi.md#authenticationDefault) | **POST** /api/v2/Authentication | Authenticate a user. |
| [**authenticationIsAlive**](AuthenticationApi.md#authenticationIsAlive) | **GET** /api/v2/Authentication/IsAlive | Acknowledges the connection to the API |
| [**authenticationPutManageTokens**](AuthenticationApi.md#authenticationPutManageTokens) | **PUT** /api/v2/AuthenticatedUsers/{UserID}/Tokens | Manage API tokens. |
| [**authenticationRequestPasswordReset**](AuthenticationApi.md#authenticationRequestPasswordReset) | **POST** /api/v2/Authentication/RequestPasswordReset | Request a password reset. |
| [**authenticationResetPasword**](AuthenticationApi.md#authenticationResetPasword) | **POST** /api/v2/Authentication/ResetPasword | Reset a password |


<a id="authenticationDefault"></a>
# **authenticationDefault**
> APIModelsAuthenticatedUser authenticationDefault(apIModelsCredentials)

Authenticate a user.

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    APIModelsCredentials apIModelsCredentials = new APIModelsCredentials(); // APIModelsCredentials | Create a user account.
    try {
      APIModelsAuthenticatedUser result = apiInstance.authenticationDefault(apIModelsCredentials);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authenticationDefault");
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
| **apIModelsCredentials** | [**APIModelsCredentials**](APIModelsCredentials.md)| Create a user account. | |

### Return type

[**APIModelsAuthenticatedUser**](APIModelsAuthenticatedUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="authenticationIsAlive"></a>
# **authenticationIsAlive**
> authenticationIsAlive()

Acknowledges the connection to the API

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    try {
      apiInstance.authenticationIsAlive();
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authenticationIsAlive");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="authenticationPutManageTokens"></a>
# **authenticationPutManageTokens**
> authenticationPutManageTokens(userID, apIModelsTokenOptions)

Manage API tokens.

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    Integer userID = 56; // Integer | 
    APIModelsTokenOptions apIModelsTokenOptions = new APIModelsTokenOptions(); // APIModelsTokenOptions | The options for token management.
    try {
      apiInstance.authenticationPutManageTokens(userID, apIModelsTokenOptions);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authenticationPutManageTokens");
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
| **userID** | **Integer**|  | |
| **apIModelsTokenOptions** | [**APIModelsTokenOptions**](APIModelsTokenOptions.md)| The options for token management. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="authenticationRequestPasswordReset"></a>
# **authenticationRequestPasswordReset**
> authenticationRequestPasswordReset(apIModelsPasswordResetRequest)

Request a password reset.

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    APIModelsPasswordResetRequest apIModelsPasswordResetRequest = new APIModelsPasswordResetRequest(); // APIModelsPasswordResetRequest | The password reset request.
    try {
      apiInstance.authenticationRequestPasswordReset(apIModelsPasswordResetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authenticationRequestPasswordReset");
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
| **apIModelsPasswordResetRequest** | [**APIModelsPasswordResetRequest**](APIModelsPasswordResetRequest.md)| The password reset request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="authenticationResetPasword"></a>
# **authenticationResetPasword**
> authenticationResetPasword(apIModelsPasswordReset)

Reset a password

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    APIModelsPasswordReset apIModelsPasswordReset = new APIModelsPasswordReset(); // APIModelsPasswordReset | The password reset detail.
    try {
      apiInstance.authenticationResetPasword(apIModelsPasswordReset);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authenticationResetPasword");
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
| **apIModelsPasswordReset** | [**APIModelsPasswordReset**](APIModelsPasswordReset.md)| The password reset detail. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

