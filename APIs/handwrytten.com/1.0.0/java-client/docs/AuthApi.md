# AuthApi

All URIs are relative to *https://api.handwrytten.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changePassword**](AuthApi.md#changePassword) | **POST** /auth/changePassword | changes a user&#39;s password |
| [**login**](AuthApi.md#login) | **POST** /auth/authorization | Logs in to an existing account |
| [**logout**](AuthApi.md#logout) | **POST** /auth/logout | logs out a session uid |
| [**register**](AuthApi.md#register) | **POST** /auth/register | Registers a new account |
| [**resetPasswordRequest**](AuthApi.md#resetPasswordRequest) | **POST** /auth/resetPasswordRequest | resets a user&#39;s password |


<a id="changePassword"></a>
# **changePassword**
> ChangePassword200Response changePassword(body)

changes a user&#39;s password

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
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    AuthApi apiInstance = new AuthApi(defaultClient);
    ChangePasswordRequest body = new ChangePasswordRequest(); // ChangePasswordRequest | Change password
    try {
      ChangePassword200Response result = apiInstance.changePassword(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#changePassword");
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
| **body** | [**ChangePasswordRequest**](ChangePasswordRequest.md)| Change password | |

### Return type

[**ChangePassword200Response**](ChangePassword200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful password change |  -  |
| **405** | Invalid input |  -  |

<a id="login"></a>
# **login**
> Login200Response login(body)

Logs in to an existing account

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
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    AuthApi apiInstance = new AuthApi(defaultClient);
    Login body = new Login(); // Login | Login to account
    try {
      Login200Response result = apiInstance.login(body);
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
| **body** | [**Login**](Login.md)| Login to account | |

### Return type

[**Login200Response**](Login200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful login |  -  |
| **400** | auth error |  -  |

<a id="logout"></a>
# **logout**
> ChangePassword200Response logout(body)

logs out a session uid

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
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    AuthApi apiInstance = new AuthApi(defaultClient);
    LogoutRequest body = new LogoutRequest(); // LogoutRequest | logout session
    try {
      ChangePassword200Response result = apiInstance.logout(body);
      System.out.println(result);
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

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**LogoutRequest**](LogoutRequest.md)| logout session | |

### Return type

[**ChangePassword200Response**](ChangePassword200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful logout |  -  |
| **405** | Invalid input |  -  |

<a id="register"></a>
# **register**
> Register200Response register(body)

Registers a new account

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
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    AuthApi apiInstance = new AuthApi(defaultClient);
    Registration body = new Registration(); // Registration | New user account information
    try {
      Register200Response result = apiInstance.register(body);
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
| **body** | [**Registration**](Registration.md)| New user account information | |

### Return type

[**Register200Response**](Register200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful registration |  -  |
| **405** | Invalid input |  -  |

<a id="resetPasswordRequest"></a>
# **resetPasswordRequest**
> ChangePassword200Response resetPasswordRequest(body)

resets a user&#39;s password

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
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    AuthApi apiInstance = new AuthApi(defaultClient);
    ResetPasswordRequestRequest body = new ResetPasswordRequestRequest(); // ResetPasswordRequestRequest | Reset password
    try {
      ChangePassword200Response result = apiInstance.resetPasswordRequest(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#resetPasswordRequest");
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
| **body** | [**ResetPasswordRequestRequest**](ResetPasswordRequestRequest.md)| Reset password | |

### Return type

[**ChangePassword200Response**](ChangePassword200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful reset request |  -  |
| **405** | Invalid input |  -  |

