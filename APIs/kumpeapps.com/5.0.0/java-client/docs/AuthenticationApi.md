# AuthenticationApi

All URIs are relative to *https://restapi.kumpeapps.com/v5*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appkeyPatch**](AuthenticationApi.md#appkeyPatch) | **PATCH** /appkey | Compromise app key |
| [**appkeyPost**](AuthenticationApi.md#appkeyPost) | **POST** /appkey | Request app key |
| [**appkeyPut**](AuthenticationApi.md#appkeyPut) | **PUT** /appkey | Deactivate app key |
| [**authAppkeyPatch**](AuthenticationApi.md#authAppkeyPatch) | **PATCH** /authentication/appkey | Compromise app key |
| [**authAppkeyPost**](AuthenticationApi.md#authAppkeyPost) | **POST** /authentication/appkey | Request app key |
| [**authAppkeyPut**](AuthenticationApi.md#authAppkeyPut) | **PUT** /authentication/appkey | Deactivate app key |
| [**authAuthkeyGet**](AuthenticationApi.md#authAuthkeyGet) | **GET** /authentication/authkey | Request auth key for user (login user) |
| [**authAuthkeyPatch**](AuthenticationApi.md#authAuthkeyPatch) | **PATCH** /authentication/authkey | Compromise auth key |
| [**authAuthkeyPost**](AuthenticationApi.md#authAuthkeyPost) | **POST** /authentication/authkey | Request auth key for user (login user) |
| [**authAuthkeyPut**](AuthenticationApi.md#authAuthkeyPut) | **PUT** /authentication/authkey | Deactivate auth key (logout) |
| [**authVerifyotpGet**](AuthenticationApi.md#authVerifyotpGet) | **GET** /authentication/verifyotp | Verifies YubiKey OTP for authenticated user |
| [**authkeyGet**](AuthenticationApi.md#authkeyGet) | **GET** /authkey | Request auth key for user (login user) |
| [**authkeyPatch**](AuthenticationApi.md#authkeyPatch) | **PATCH** /authkey | Compromise auth key |
| [**authkeyPost**](AuthenticationApi.md#authkeyPost) | **POST** /authkey | Request auth key for user (login user) |
| [**authkeyPut**](AuthenticationApi.md#authkeyPut) | **PUT** /authkey | Deactivate auth key (logout) |


<a id="appkeyPatch"></a>
# **appkeyPatch**
> InlineResponse202 appkeyPatch(appKey, comments)

Compromise app key

Pass an app key to mark it as compromised. This may be submitted by the app owner or a concerned party that has optained the compromised app key.

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String appKey = "appKey_example"; // String | compromised app key
    String comments = "comments_example"; // String | Comments (like how was this compromised)
    try {
      InlineResponse202 result = apiInstance.appkeyPatch(appKey, comments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#appkeyPatch");
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
| **appKey** | **String**| compromised app key | |
| **comments** | **String**| Comments (like how was this compromised) | [optional] |

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | App key deactivated |  -  |

<a id="appkeyPost"></a>
# **appkeyPost**
> InlineResponse201 appkeyPost(username, password, supportsYubikey)

Request app key

Request a new app key by passing username and password for app account

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String username = "username_example"; // String | Username assigned to your app
    String password = "password_example"; // String | Password assigned to your app
    Boolean supportsYubikey = true; // Boolean | App supports YubiKey OTP
    try {
      InlineResponse201 result = apiInstance.appkeyPost(username, password, supportsYubikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#appkeyPost");
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
| **username** | **String**| Username assigned to your app | |
| **password** | **String**| Password assigned to your app | |
| **supportsYubikey** | **Boolean**| App supports YubiKey OTP | |

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | app key created |  -  |

<a id="appkeyPut"></a>
# **appkeyPut**
> InlineResponse202 appkeyPut(appKey)

Deactivate app key

Pass your app key to deactivate the key

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: app_key
    ApiKeyAuth app_key = (ApiKeyAuth) defaultClient.getAuthentication("app_key");
    app_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //app_key.setApiKeyPrefix("Token");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String appKey = "appKey_example"; // String | app key to deactivate
    try {
      InlineResponse202 result = apiInstance.appkeyPut(appKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#appkeyPut");
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
| **appKey** | **String**| app key to deactivate | |

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | App key deactivated |  -  |

<a id="authAppkeyPatch"></a>
# **authAppkeyPatch**
> InlineResponse202 authAppkeyPatch(appKey, comments)

Compromise app key

Pass an app key to mark it as compromised. This may be submitted by the app owner or a concerned party that has optained the compromised app key.

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String appKey = "appKey_example"; // String | compromised app key
    String comments = "comments_example"; // String | Comments (like how was this compromised)
    try {
      InlineResponse202 result = apiInstance.authAppkeyPatch(appKey, comments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authAppkeyPatch");
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
| **appKey** | **String**| compromised app key | |
| **comments** | **String**| Comments (like how was this compromised) | [optional] |

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | App key deactivated |  -  |

<a id="authAppkeyPost"></a>
# **authAppkeyPost**
> InlineResponse201 authAppkeyPost(username, password, supportsYubikey)

Request app key

Request a new app key by passing username and password for app account

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String username = "username_example"; // String | Username assigned to your app
    String password = "password_example"; // String | Password assigned to your app
    Boolean supportsYubikey = true; // Boolean | App supports YubiKey OTP
    try {
      InlineResponse201 result = apiInstance.authAppkeyPost(username, password, supportsYubikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authAppkeyPost");
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
| **username** | **String**| Username assigned to your app | |
| **password** | **String**| Password assigned to your app | |
| **supportsYubikey** | **Boolean**| App supports YubiKey OTP | |

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | app key created |  -  |

<a id="authAppkeyPut"></a>
# **authAppkeyPut**
> InlineResponse202 authAppkeyPut(appKey)

Deactivate app key

Pass your app key to deactivate the key

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: app_key
    ApiKeyAuth app_key = (ApiKeyAuth) defaultClient.getAuthentication("app_key");
    app_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //app_key.setApiKeyPrefix("Token");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String appKey = "appKey_example"; // String | app key to deactivate
    try {
      InlineResponse202 result = apiInstance.authAppkeyPut(appKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authAppkeyPut");
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
| **appKey** | **String**| app key to deactivate | |

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | App key deactivated |  -  |

<a id="authAuthkeyGet"></a>
# **authAuthkeyGet**
> InlineResponse2011 authAuthkeyGet(username, password, otp, deviceName, identifierForVendor)

Request auth key for user (login user)

Obtain auth key for user that has provided their username and password to login to your app. (or to obtain an auth key for a script like IFTTT)

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: app_key
    ApiKeyAuth app_key = (ApiKeyAuth) defaultClient.getAuthentication("app_key");
    app_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //app_key.setApiKeyPrefix("Token");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String username = "username_example"; // String | Authenticated username
    String password = "password_example"; // String | Authenticated password
    String otp = "otp_example"; // String | YubiKey OTP (if configured for user)
    String deviceName = "deviceName_example"; // String | User's device name
    String identifierForVendor = "identifierForVendor_example"; // String | identifierForVendor for User's Device (if app is iOS)
    try {
      InlineResponse2011 result = apiInstance.authAuthkeyGet(username, password, otp, deviceName, identifierForVendor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authAuthkeyGet");
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
| **username** | **String**| Authenticated username | |
| **password** | **String**| Authenticated password | |
| **otp** | **String**| YubiKey OTP (if configured for user) | [optional] |
| **deviceName** | **String**| User&#39;s device name | [optional] |
| **identifierForVendor** | **String**| identifierForVendor for User&#39;s Device (if app is iOS) | [optional] |

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User Authenticated Sucessfully |  -  |
| **401** | Invalid/Locked/Blocked/Compromised AppKey |  -  |
| **403** | Access Denied |  -  |
| **449** | OTP required but not supplied. Please resubmit request with OTP |  -  |

<a id="authAuthkeyPatch"></a>
# **authAuthkeyPatch**
> InlineResponse202 authAuthkeyPatch(authKey, comments)

Compromise auth key

Mark user auth key as compromised

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String authKey = "authKey_example"; // String | auth key to mark as compromised
    String comments = "comments_example"; // String | Comments (like how was this compromised)
    try {
      InlineResponse202 result = apiInstance.authAuthkeyPatch(authKey, comments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authAuthkeyPatch");
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
| **authKey** | **String**| auth key to mark as compromised | |
| **comments** | **String**| Comments (like how was this compromised) | [optional] |

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Auth key marked as compromised and locked |  -  |
| **401** | Invalid/Locked/Blocked/Compromised AppKey |  -  |

<a id="authAuthkeyPost"></a>
# **authAuthkeyPost**
> InlineResponse2011 authAuthkeyPost(username, password, otp)

Request auth key for user (login user)

Obtain auth key for user that has provided their username and password to login to your app. (or to obtain an auth key for a script like IFTTT)

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: app_key
    ApiKeyAuth app_key = (ApiKeyAuth) defaultClient.getAuthentication("app_key");
    app_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //app_key.setApiKeyPrefix("Token");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String username = "username_example"; // String | Authenticated username
    String password = "password_example"; // String | Authenticated password
    String otp = "otp_example"; // String | YubiKey OTP (if configured for user)
    try {
      InlineResponse2011 result = apiInstance.authAuthkeyPost(username, password, otp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authAuthkeyPost");
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
| **username** | **String**| Authenticated username | |
| **password** | **String**| Authenticated password | |
| **otp** | **String**| YubiKey OTP (if configured for user) | [optional] |

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User Authenticated Sucessfully |  -  |
| **401** | Invalid/Locked/Blocked/Compromised AppKey |  -  |
| **403** | Access Denied |  -  |
| **449** | OTP required but not supplied. Please resubmit request with OTP |  -  |

<a id="authAuthkeyPut"></a>
# **authAuthkeyPut**
> InlineResponse202 authAuthkeyPut(authKey)

Deactivate auth key (logout)

Deactivate auth key for user logging them out of your application

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: app_key
    ApiKeyAuth app_key = (ApiKeyAuth) defaultClient.getAuthentication("app_key");
    app_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //app_key.setApiKeyPrefix("Token");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String authKey = "authKey_example"; // String | auth key to logout
    try {
      InlineResponse202 result = apiInstance.authAuthkeyPut(authKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authAuthkeyPut");
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
| **authKey** | **String**| auth key to logout | |

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **401** | Invalid/Locked/Blocked/Compromised AppKey |  -  |

<a id="authVerifyotpGet"></a>
# **authVerifyotpGet**
> authVerifyotpGet(otp)

Verifies YubiKey OTP for authenticated user

Verifies YubiKey OTP for authenticated user

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String otp = "otp_example"; // String | YubiKey OTP code
    try {
      apiInstance.authVerifyotpGet(otp);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authVerifyotpGet");
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
| **otp** | **String**| YubiKey OTP code | |

### Return type

null (empty response body)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User Authenticated Sucessfully |  -  |
| **401** | Invalid/Locked/Blocked/Compromised AppKey/AuthKey |  -  |
| **403** | Access Denied |  -  |

<a id="authkeyGet"></a>
# **authkeyGet**
> InlineResponse2011 authkeyGet(username, password, otp)

Request auth key for user (login user)

Obtain auth key for user that has provided their username and password to login to your app. (or to obtain an auth key for a script like IFTTT)

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: app_key
    ApiKeyAuth app_key = (ApiKeyAuth) defaultClient.getAuthentication("app_key");
    app_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //app_key.setApiKeyPrefix("Token");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String username = "username_example"; // String | Authenticated username
    String password = "password_example"; // String | Authenticated password
    String otp = "otp_example"; // String | YubiKey OTP (if configured for user)
    try {
      InlineResponse2011 result = apiInstance.authkeyGet(username, password, otp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authkeyGet");
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
| **username** | **String**| Authenticated username | |
| **password** | **String**| Authenticated password | |
| **otp** | **String**| YubiKey OTP (if configured for user) | [optional] |

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User Authenticated Sucessfully |  -  |
| **401** | Invalid/Locked/Blocked/Compromised AppKey |  -  |
| **403** | Access Denied |  -  |
| **449** | OTP required but not supplied. Please resubmit request with OTP |  -  |

<a id="authkeyPatch"></a>
# **authkeyPatch**
> InlineResponse202 authkeyPatch(authKey, comments)

Compromise auth key

Mark user auth key as compromised

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String authKey = "authKey_example"; // String | auth key to mark as compromised
    String comments = "comments_example"; // String | Comments (like how was this compromised)
    try {
      InlineResponse202 result = apiInstance.authkeyPatch(authKey, comments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authkeyPatch");
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
| **authKey** | **String**| auth key to mark as compromised | |
| **comments** | **String**| Comments (like how was this compromised) | [optional] |

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Auth key marked as compromised and locked |  -  |
| **401** | Invalid/Locked/Blocked/Compromised AppKey |  -  |

<a id="authkeyPost"></a>
# **authkeyPost**
> InlineResponse2011 authkeyPost(username, password, otp)

Request auth key for user (login user)

Obtain auth key for user that has provided their username and password to login to your app. (or to obtain an auth key for a script like IFTTT)

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: app_key
    ApiKeyAuth app_key = (ApiKeyAuth) defaultClient.getAuthentication("app_key");
    app_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //app_key.setApiKeyPrefix("Token");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String username = "username_example"; // String | Authenticated username
    String password = "password_example"; // String | Authenticated password
    String otp = "otp_example"; // String | YubiKey OTP (if configured for user)
    try {
      InlineResponse2011 result = apiInstance.authkeyPost(username, password, otp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authkeyPost");
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
| **username** | **String**| Authenticated username | |
| **password** | **String**| Authenticated password | |
| **otp** | **String**| YubiKey OTP (if configured for user) | [optional] |

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User Authenticated Sucessfully |  -  |
| **401** | Invalid/Locked/Blocked/Compromised AppKey |  -  |
| **403** | Access Denied |  -  |
| **449** | OTP required but not supplied. Please resubmit request with OTP |  -  |

<a id="authkeyPut"></a>
# **authkeyPut**
> InlineResponse202 authkeyPut(authKey)

Deactivate auth key (logout)

Deactivate auth key for user logging them out of your application

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
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: app_key
    ApiKeyAuth app_key = (ApiKeyAuth) defaultClient.getAuthentication("app_key");
    app_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //app_key.setApiKeyPrefix("Token");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String authKey = "authKey_example"; // String | auth key to logout
    try {
      InlineResponse202 result = apiInstance.authkeyPut(authKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authkeyPut");
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
| **authKey** | **String**| auth key to logout | |

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **401** | Invalid/Locked/Blocked/Compromised AppKey |  -  |

