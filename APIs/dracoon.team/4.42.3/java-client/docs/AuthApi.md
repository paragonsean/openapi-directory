# AuthApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**completeOpenIdLogin**](AuthApi.md#completeOpenIdLogin) | **POST** /v4/auth/openid/login | Complete OpenID Connect authentication |
| [**initiateOpenIdLogin**](AuthApi.md#initiateOpenIdLogin) | **GET** /v4/auth/openid/login | Initiate OpenID Connect authentication |
| [**login**](AuthApi.md#login) | **POST** /v4/auth/login | Authenticate user (Login) |
| [**ping**](AuthApi.md#ping) | **GET** /v4/auth/ping | Ping |
| [**recoverUserName**](AuthApi.md#recoverUserName) | **POST** /v4/auth/recover_username | Recover username |
| [**requestPasswordReset**](AuthApi.md#requestPasswordReset) | **POST** /v4/auth/reset_password | Request password reset |
| [**resetPassword**](AuthApi.md#resetPassword) | **PUT** /v4/auth/reset_password/{token} | Reset password |
| [**validateResetPasswordToken**](AuthApi.md#validateResetPasswordToken) | **GET** /v4/auth/reset_password/{token} | Validate information for password reset |


<a id="completeOpenIdLogin"></a>
# **completeOpenIdLogin**
> LoginResponse completeOpenIdLogin(code, state, idToken)

Complete OpenID Connect authentication

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.14.0&lt;/h3&gt;  ### Description:   This is the second step of the OpenID Connect authentication.   The user hands over the authorization code and is logged in.  ### Precondition: Existing user with activated OpenID Connect authentication that is **NOT** locked.  ### Postcondition: User is logged in.  ### Further Information: None.

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
    defaultClient.setBasePath("/api");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String code = "code_example"; // String | Authorization code
    String state = "state_example"; // String | Authentication state
    String idToken = "idToken_example"; // String | Identity token
    try {
      LoginResponse result = apiInstance.completeOpenIdLogin(code, state, idToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#completeOpenIdLogin");
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
| **code** | **String**| Authorization code | |
| **state** | **String**| Authentication state | |
| **idToken** | **String**| Identity token | [optional] |

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **502** | Bad Gateway |  -  |

<a id="initiateOpenIdLogin"></a>
# **initiateOpenIdLogin**
> initiateOpenIdLogin(issuer, redirectUri, language, test)

Initiate OpenID Connect authentication

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.14.0&lt;/h3&gt;  ### Description: This is the first step of the OpenID Connect authentication.   The user is send to the OpenID Connect identity provider to authenticate himself and retrieve an authorization code.  ### Precondition: None.  ### Postcondition: User is redirected to OpenID Connect identity provider to authenticate himself.  ### Further Information: None.

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
    defaultClient.setBasePath("/api");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String issuer = "issuer_example"; // String | Issuer identifier of the OpenID Connect identity provider
    String redirectUri = "redirectUri_example"; // String | Redirect URI to complete the OpenID Connect authentication
    String language = "language_example"; // String | Language ID or ISO 639-1 code
    Boolean test = true; // Boolean | Flag to test the authentication parameters.  If the request is valid, the API will respond with `204 No Content`.
    try {
      apiInstance.initiateOpenIdLogin(issuer, redirectUri, language, test);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#initiateOpenIdLogin");
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
| **issuer** | **String**| Issuer identifier of the OpenID Connect identity provider | |
| **redirectUri** | **String**| Redirect URI to complete the OpenID Connect authentication | |
| **language** | **String**| Language ID or ISO 639-1 code | |
| **test** | **Boolean**| Flag to test the authentication parameters.  If the request is valid, the API will respond with &#x60;204 No Content&#x60;. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **302** | Found |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **502** | Bad Gateway |  -  |

<a id="login"></a>
# **login**
> LoginResponse login(loginRequest)

Authenticate user (Login)

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.13.0&lt;/h3&gt;  ### Description: Authenticates user and provides an authentication token (&#x60;X-Sds-Auth-Token&#x60;) that is required for the most operations.  ### Precondition: Existing user that is **NOT** locked.  ### Postcondition: User is logged in.  ### Further Information: The provided token is valid for **two hours**, every usage resets this period to two full hours again.   Logging off invalidates the token.    ### Available authentication methods: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Authentication Method (&#x60;authType&#x60;) | Description | | :--- | :--- | | &#x60;basic&#x60; | Log in with credentials stored in the database &lt;br&gt;Formerly known as &#x60;sql&#x60;.| | &#x60;active_directory&#x60; | Log in with Active Directory credentials | | &#x60;radius&#x60; | Log in with RADIUS username, PIN and token password.&lt;br&gt;Token (request parameter) may be set, otherwise this parameter is ignored. If token is set, password is optional. | | &#x60;openid&#x60; | Please use &#x60;POST /auth/openid/login&#x60; API to login with OpenID Connect identity |  &lt;/details&gt;

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
    defaultClient.setBasePath("/api");

    AuthApi apiInstance = new AuthApi(defaultClient);
    LoginRequest loginRequest = new LoginRequest(); // LoginRequest | 
    try {
      LoginResponse result = apiInstance.login(loginRequest);
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
| **loginRequest** | [**LoginRequest**](LoginRequest.md)|  | |

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |
| **502** | Bad Gateway |  -  |

<a id="ping"></a>
# **ping**
> String ping()

Ping

### Description: Test connection to DRACOON Core Service.  ### Precondition: None.  ### Postcondition: &#x60;200 OK&#x60; with current date string is returned if successful.  ### Further Information: None.

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
    defaultClient.setBasePath("/api");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      String result = apiInstance.ping();
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **406** | Not Acceptable |  -  |

<a id="recoverUserName"></a>
# **recoverUserName**
> recoverUserName(recoverUserNameRequest)

Recover username

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.13.0&lt;/h3&gt;  ### Description:   Request an email with the user names of all accounts connected to the email.  ### Precondition: Valid email address.  ### Postcondition: An email is sent to the provided address, with a list of account user names connected to it.  ### Further Information: None. 

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
    defaultClient.setBasePath("/api");

    AuthApi apiInstance = new AuthApi(defaultClient);
    RecoverUserNameRequest recoverUserNameRequest = new RecoverUserNameRequest(); // RecoverUserNameRequest | 
    try {
      apiInstance.recoverUserName(recoverUserNameRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#recoverUserName");
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
| **recoverUserNameRequest** | [**RecoverUserNameRequest**](RecoverUserNameRequest.md)|  | |

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
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestPasswordReset"></a>
# **requestPasswordReset**
> requestPasswordReset(resetPasswordRequest)

Request password reset

### Description:   Request an email with a password reset token for a certain user to reset password.  ### Precondition: Registered user account.  ### Postcondition: Provided user receives email with password reset token.  ### Further Information: None.

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
    defaultClient.setBasePath("/api");

    AuthApi apiInstance = new AuthApi(defaultClient);
    ResetPasswordRequest resetPasswordRequest = new ResetPasswordRequest(); // ResetPasswordRequest | 
    try {
      apiInstance.requestPasswordReset(resetPasswordRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#requestPasswordReset");
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
| **resetPasswordRequest** | [**ResetPasswordRequest**](ResetPasswordRequest.md)|  | |

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
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **406** | Not Acceptable |  -  |

<a id="resetPassword"></a>
# **resetPassword**
> resetPassword(token, resetPasswordWithTokenRequest)

Reset password

### Description:   Resets user&#39;s password.  ### Precondition: User received a password reset token.  ### Postcondition: User&#39;s password is reset to the provided password.  ### Further Information: Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]

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
    defaultClient.setBasePath("/api");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String token = "token_example"; // String | Password reset token
    ResetPasswordWithTokenRequest resetPasswordWithTokenRequest = new ResetPasswordWithTokenRequest(); // ResetPasswordWithTokenRequest | 
    try {
      apiInstance.resetPassword(token, resetPasswordWithTokenRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#resetPassword");
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
| **token** | **String**| Password reset token | |
| **resetPasswordWithTokenRequest** | [**ResetPasswordWithTokenRequest**](ResetPasswordWithTokenRequest.md)|  | |

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
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="validateResetPasswordToken"></a>
# **validateResetPasswordToken**
> ResetPasswordTokenValidateResponse validateResetPasswordToken(token)

Validate information for password reset

### Description:   Request all information for a password change dialogue e.g. real name of user.  ### Precondition: User received a password reset token.  ### Postcondition: Context information is returned.  ### Further Information: None.

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
    defaultClient.setBasePath("/api");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String token = "token_example"; // String | Password reset token
    try {
      ResetPasswordTokenValidateResponse result = apiInstance.validateResetPasswordToken(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#validateResetPasswordToken");
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
| **token** | **String**| Password reset token | |

### Return type

[**ResetPasswordTokenValidateResponse**](ResetPasswordTokenValidateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

