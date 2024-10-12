# AuthenticationApi

All URIs are relative to *https://hub.docker.com/api/publisher/analytics/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postUsers2FALogin**](AuthenticationApi.md#postUsers2FALogin) | **POST** /v2/users/2fa-login | Second factor authentication. |
| [**postUsersLogin**](AuthenticationApi.md#postUsersLogin) | **POST** /v2/users/login | Create an authentication token |


<a id="postUsers2FALogin"></a>
# **postUsers2FALogin**
> PostUsersLoginSuccessResponse postUsers2FALogin(users2FALoginRequest)

Second factor authentication.

When a user has 2FA enabled, this is the second call to perform after &#x60;/v2/users/login&#x60; call.  Creates and returns a bearer token in JWT format that you can use to authenticate with Docker Hub APIs.  The returned token is used in the HTTP Authorization header like &#x60;Authorization: Bearer {TOKEN}&#x60;.  Most Docker Hub APIs require this token either to consume or to get detailed information. For example, to list images in a private repository. 

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
    defaultClient.setBasePath("https://hub.docker.com/api/publisher/analytics/v1");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    Users2FALoginRequest users2FALoginRequest = new Users2FALoginRequest(); // Users2FALoginRequest | Login details.
    try {
      PostUsersLoginSuccessResponse result = apiInstance.postUsers2FALogin(users2FALoginRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#postUsers2FALogin");
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
| **users2FALoginRequest** | [**Users2FALoginRequest**](Users2FALoginRequest.md)| Login details. | |

### Return type

[**PostUsersLoginSuccessResponse**](PostUsersLoginSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authentication successful |  -  |
| **401** | Authentication failed or second factor required |  -  |

<a id="postUsersLogin"></a>
# **postUsersLogin**
> PostUsersLoginSuccessResponse postUsersLogin(usersLoginRequest)

Create an authentication token

Creates and returns a bearer token in JWT format that you can use to authenticate with Docker Hub APIs.  The returned token is used in the HTTP Authorization header like &#x60;Authorization: Bearer {TOKEN}&#x60;.  Most Docker Hub APIs require this token either to consume or to get detailed information. For example, to list images in a private repository. 

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
    defaultClient.setBasePath("https://hub.docker.com/api/publisher/analytics/v1");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    UsersLoginRequest usersLoginRequest = new UsersLoginRequest(); // UsersLoginRequest | Login details.
    try {
      PostUsersLoginSuccessResponse result = apiInstance.postUsersLogin(usersLoginRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#postUsersLogin");
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
| **usersLoginRequest** | [**UsersLoginRequest**](UsersLoginRequest.md)| Login details. | |

### Return type

[**PostUsersLoginSuccessResponse**](PostUsersLoginSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authentication successful |  -  |
| **401** | Authentication failed or second factor required |  -  |

