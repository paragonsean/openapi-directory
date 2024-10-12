# UserApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateTotpSecret**](UserApi.md#generateTotpSecret) | **POST** /user/{id}/totp/new_secret | Generate a TOTP secret key for the given user |
| [**getTotpStatus**](UserApi.md#getTotpStatus) | **GET** /user/{id}/totp/status | Get the TOTP status for the given user |
| [**getUserAccountLockoutSettings**](UserApi.md#getUserAccountLockoutSettings) | **GET** /user/lockout | Get the local user account lockout settings |
| [**manageUserAccountLockoutSettings**](UserApi.md#manageUserAccountLockoutSettings) | **PATCH** /user/lockout | Update the local user account lockout settings |
| [**resetTotp**](UserApi.md#resetTotp) | **DELETE** /user/{id}/totp/config | Reset the TOTP for the given user |
| [**setupTotp**](UserApi.md#setupTotp) | **PUT** /user/{id}/totp/config | Configure the TOTP secret for the given user |
| [**unlockUser**](UserApi.md#unlockUser) | **POST** /user/{id}/unlock | Unlock a user account |


<a id="generateTotpSecret"></a>
# **generateTotpSecret**
> TotpSecret generateTotpSecret(id)

Generate a TOTP secret key for the given user

Use this endpoint to generate the time-based one time password (TOTP) secret key for a specified user account. The secret is a key value encoded in Base32 and includes a URI for generating a scannable QR code. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | The user account object ID.
    try {
      TotpSecret result = apiInstance.generateTotpSecret(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#generateTotpSecret");
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
| **id** | **String**| The user account object ID. | |

### Return type

[**TotpSecret**](TotpSecret.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully generated TOTP secret. |  -  |

<a id="getTotpStatus"></a>
# **getTotpStatus**
> TotpStatus getTotpStatus(id)

Get the TOTP status for the given user

Get the time-based one time password (TOTP) status for a specified user account. The TOTP status specifies whether that account has TOTP enabled and whether TOTP is being enforced for that account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | The user account object ID.
    try {
      TotpStatus result = apiInstance.getTotpStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getTotpStatus");
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
| **id** | **String**| The user account object ID. | |

### Return type

[**TotpStatus**](TotpStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The TOTP status of the user.  |  -  |

<a id="getUserAccountLockoutSettings"></a>
# **getUserAccountLockoutSettings**
> LocalUserAccountLockoutStatus getUserAccountLockoutSettings()

Get the local user account lockout settings

Get the local user account lockout settings which are used to configure whether user accounts will be locked on failed logins, when they will be locked and the duration for which they will stay locked. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    try {
      LocalUserAccountLockoutStatus result = apiInstance.getUserAccountLockoutSettings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserAccountLockoutSettings");
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

[**LocalUserAccountLockoutStatus**](LocalUserAccountLockoutStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the local user account lockout settings which are used to configure whether user accounts will be locked on failed logins, when they will be locked and the duration for which they will stay locked.  |  -  |

<a id="manageUserAccountLockoutSettings"></a>
# **manageUserAccountLockoutSettings**
> LocalUserAccountLockoutStatus manageUserAccountLockoutSettings(localUserAccountLockoutConfig)

Update the local user account lockout settings

Update the local user account lockout settings which are used to configure whether user accounts will be locked on failed logins, when they will be locked and the duration for which they will stay locked. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    LocalUserAccountLockoutConfig localUserAccountLockoutConfig = new LocalUserAccountLockoutConfig(); // LocalUserAccountLockoutConfig | Update the local user account lockout settings.
    try {
      LocalUserAccountLockoutStatus result = apiInstance.manageUserAccountLockoutSettings(localUserAccountLockoutConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#manageUserAccountLockoutSettings");
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
| **localUserAccountLockoutConfig** | [**LocalUserAccountLockoutConfig**](LocalUserAccountLockoutConfig.md)| Update the local user account lockout settings. | |

### Return type

[**LocalUserAccountLockoutStatus**](LocalUserAccountLockoutStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current configuration for local user account lockout feature.  |  -  |

<a id="resetTotp"></a>
# **resetTotp**
> resetTotp(id)

Reset the TOTP for the given user

Reset the TOTP settings to the default disabled state for the specified user account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | The user account object ID.
    try {
      apiInstance.resetTotp(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#resetTotp");
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
| **id** | **String**| The user account object ID. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully reset the TOTP. |  -  |

<a id="setupTotp"></a>
# **setupTotp**
> setupTotp(id, totpConfigUpdateRequest)

Configure the TOTP secret for the given user

Use this endpoint to configure the time-based one time password (TOTP) secret for a specified user account. The endpoint replaces an existing secret with the new one. The Rubrik cluster checks the secret against a one time password (OTP) to ensure validity. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | The user account object ID.
    TotpConfigUpdateRequest totpConfigUpdateRequest = new TotpConfigUpdateRequest(); // TotpConfigUpdateRequest | The time-based one time password (TOTP) configuration.
    try {
      apiInstance.setupTotp(id, totpConfigUpdateRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#setupTotp");
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
| **id** | **String**| The user account object ID. | |
| **totpConfigUpdateRequest** | [**TotpConfigUpdateRequest**](TotpConfigUpdateRequest.md)| The time-based one time password (TOTP) configuration. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully configured the TOTP settings for the specified user account.  |  -  |

<a id="unlockUser"></a>
# **unlockUser**
> unlockUser(id)

Unlock a user account

Unlock a user account that has been locked because of too many failed login attempts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | The ID of the user account that has been locked.
    try {
      apiInstance.unlockUser(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#unlockUser");
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
| **id** | **String**| The ID of the user account that has been locked. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully unlocked the user. |  -  |

