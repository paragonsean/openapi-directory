# LoginApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**logout**](LoginApi.md#logout) | **POST** /v1/logout | Logout |
| [**resetPassword**](LoginApi.md#resetPassword) | **POST** /v1/password/reset | Reset password |
| [**validateAccessToken**](LoginApi.md#validateAccessToken) | **POST** /v1/validate | validate |
| [**veloAuth**](LoginApi.md#veloAuth) | **POST** /v1/authenticate | Authentication endpoint |


<a id="logout"></a>
# **logout**
> logout()

Logout

&lt;p&gt;Given a valid access token in the header then log out the authenticated user or client &lt;/p&gt; &lt;p&gt;Will revoke the token&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoginApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    LoginApi apiInstance = new LoginApi(defaultClient);
    try {
      apiInstance.logout();
    } catch (ApiException e) {
      System.err.println("Exception when calling LoginApi#logout");
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | User has been logged out |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="resetPassword"></a>
# **resetPassword**
> resetPassword(resetPasswordRequest)

Reset password

&lt;p&gt;Reset password &lt;/p&gt; &lt;p&gt;An email with an embedded link will be sent to the receipient of the email address &lt;/p&gt; &lt;p&gt;The link will contain a token to be used for resetting the password &lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoginApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");

    LoginApi apiInstance = new LoginApi(defaultClient);
    ResetPasswordRequest resetPasswordRequest = new ResetPasswordRequest(); // ResetPasswordRequest | An Email address to send the reset password link to
    try {
      apiInstance.resetPassword(resetPasswordRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoginApi#resetPassword");
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
| **resetPasswordRequest** | [**ResetPasswordRequest**](ResetPasswordRequest.md)| An Email address to send the reset password link to | |

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
| **204** | the request was accepted |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |

<a id="validateAccessToken"></a>
# **validateAccessToken**
> AccessTokenResponse validateAccessToken(accessTokenValidationRequest, authorization)

validate

&lt;p&gt;The second part of login involves validating using an MFA device&lt;/p&gt; &lt;p&gt;An access token with PRE_AUTH authorities is required&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoginApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    LoginApi apiInstance = new LoginApi(defaultClient);
    AccessTokenValidationRequest accessTokenValidationRequest = new AccessTokenValidationRequest(); // AccessTokenValidationRequest | An OTP from the user's registered MFA Device 
    String authorization = "authorization_example"; // String | Bearer token authorization leg of validate
    try {
      AccessTokenResponse result = apiInstance.validateAccessToken(accessTokenValidationRequest, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoginApi#validateAccessToken");
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
| **accessTokenValidationRequest** | [**AccessTokenValidationRequest**](AccessTokenValidationRequest.md)| An OTP from the user&#39;s registered MFA Device  | |
| **authorization** | **String**| Bearer token authorization leg of validate | [optional] |

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User request has been validated |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="veloAuth"></a>
# **veloAuth**
> AuthResponse veloAuth(grantType)

Authentication endpoint

&lt;p&gt;Use this endpoint to obtain an access token for calling Velo Payments APIs. &lt;/p&gt; &lt;p&gt;You need your API key and API secret issued by Velo&lt;/p&gt; &lt;p&gt;To login and get an access token the API key and API secret must be Base64 encoded by concatenating them with a colon between them&lt;/p&gt; &lt;p&gt;e.g. Given an ApiKey: 44a9537d-d55d-4b47-8082-14061c2bcdd8 and ApiSecret: c396b26b-137a-44fd-87f5-34631f8fd529&lt;/p&gt; &lt;p&gt;Using a Base64 encode function Base64Encoder().encode(\&quot;44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529\&quot;)&lt;/p&gt; &lt;p&gt;Included as a Basic Authorization header: -H \&quot;Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ&#x3D;&#x3D;\&quot; &lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoginApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LoginApi apiInstance = new LoginApi(defaultClient);
    String grantType = "client_credentials"; // String | OAuth grant type. Should use 'client_credentials'
    try {
      AuthResponse result = apiInstance.veloAuth(grantType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoginApi#veloAuth");
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
| **grantType** | **String**| OAuth grant type. Should use &#39;client_credentials&#39; | [optional] [default to client_credentials] |

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Authenication response |  * Cache-Control - Ensure clients do not cache request <br>  * Pragma - Ensure clients do not cache request <br>  |

