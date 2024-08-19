# AccountApi

All URIs are relative to *https://appwrite.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountCreateRecovery**](AccountApi.md#accountCreateRecovery) | **POST** /account/recovery | Create Password Recovery |
| [**accountCreateVerification**](AccountApi.md#accountCreateVerification) | **POST** /account/verification | Create Email Verification |
| [**accountDelete**](AccountApi.md#accountDelete) | **DELETE** /account | Delete Account |
| [**accountDeleteSession**](AccountApi.md#accountDeleteSession) | **DELETE** /account/sessions/{sessionId} | Delete Account Session |
| [**accountDeleteSessions**](AccountApi.md#accountDeleteSessions) | **DELETE** /account/sessions | Delete All Account Sessions |
| [**accountGet**](AccountApi.md#accountGet) | **GET** /account | Get Account |
| [**accountGetLogs**](AccountApi.md#accountGetLogs) | **GET** /account/logs | Get Account Logs |
| [**accountGetPrefs**](AccountApi.md#accountGetPrefs) | **GET** /account/prefs | Get Account Preferences |
| [**accountGetSession**](AccountApi.md#accountGetSession) | **GET** /account/sessions/{sessionId} | Get Session By ID |
| [**accountGetSessions**](AccountApi.md#accountGetSessions) | **GET** /account/sessions | Get Account Sessions |
| [**accountUpdateEmail**](AccountApi.md#accountUpdateEmail) | **PATCH** /account/email | Update Account Email |
| [**accountUpdateName**](AccountApi.md#accountUpdateName) | **PATCH** /account/name | Update Account Name |
| [**accountUpdatePassword**](AccountApi.md#accountUpdatePassword) | **PATCH** /account/password | Update Account Password |
| [**accountUpdatePrefs**](AccountApi.md#accountUpdatePrefs) | **PATCH** /account/prefs | Update Account Preferences |
| [**accountUpdateRecovery**](AccountApi.md#accountUpdateRecovery) | **PUT** /account/recovery | Complete Password Recovery |
| [**accountUpdateVerification**](AccountApi.md#accountUpdateVerification) | **PUT** /account/verification | Complete Email Verification |


<a id="accountCreateRecovery"></a>
# **accountCreateRecovery**
> Token accountCreateRecovery(accountCreateRecoveryRequest)

Create Password Recovery

Sends the user an email with a temporary secret key for password reset. When the user clicks the confirmation link he is redirected back to your app password reset URL with the secret key and email address values attached to the URL query string. Use the query string params to submit a request to the [PUT /account/recovery](/docs/client/account#accountUpdateRecovery) endpoint to complete the process. The verification link sent to the user&#39;s email address is valid for 1 hour.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    AccountCreateRecoveryRequest accountCreateRecoveryRequest = new AccountCreateRecoveryRequest(); // AccountCreateRecoveryRequest | 
    try {
      Token result = apiInstance.accountCreateRecovery(accountCreateRecoveryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountCreateRecovery");
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
| **accountCreateRecoveryRequest** | [**AccountCreateRecoveryRequest**](AccountCreateRecoveryRequest.md)|  | [optional] |

### Return type

[**Token**](Token.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Token |  -  |

<a id="accountCreateVerification"></a>
# **accountCreateVerification**
> Token accountCreateVerification(accountCreateVerificationRequest)

Create Email Verification

Use this endpoint to send a verification message to your user email address to confirm they are the valid owners of that address. Both the **userId** and **secret** arguments will be passed as query parameters to the URL you have provided to be attached to the verification email. The provided URL should redirect the user back to your app and allow you to complete the verification process by verifying both the **userId** and **secret** parameters. Learn more about how to [complete the verification process](/docs/client/account#accountUpdateVerification). The verification link sent to the user&#39;s email address is valid for 7 days.  Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md), the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    AccountCreateVerificationRequest accountCreateVerificationRequest = new AccountCreateVerificationRequest(); // AccountCreateVerificationRequest | 
    try {
      Token result = apiInstance.accountCreateVerification(accountCreateVerificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountCreateVerification");
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
| **accountCreateVerificationRequest** | [**AccountCreateVerificationRequest**](AccountCreateVerificationRequest.md)|  | [optional] |

### Return type

[**Token**](Token.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Token |  -  |

<a id="accountDelete"></a>
# **accountDelete**
> accountDelete()

Delete Account

Delete a currently logged in user account. Behind the scene, the user record is not deleted but permanently blocked from any access. This is done to avoid deleted accounts being overtaken by new users with the same email address. Any user-related resources like documents or storage files should be deleted separately.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      apiInstance.accountDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountDelete");
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

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="accountDeleteSession"></a>
# **accountDeleteSession**
> accountDeleteSession(sessionId)

Delete Account Session

Use this endpoint to log out the currently logged in user from all their account sessions across all of their different devices. When using the option id argument, only the session unique ID provider will be deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String sessionId = "sessionId_example"; // String | Session unique ID. Use the string 'current' to delete the current device session.
    try {
      apiInstance.accountDeleteSession(sessionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountDeleteSession");
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
| **sessionId** | **String**| Session unique ID. Use the string &#39;current&#39; to delete the current device session. | |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="accountDeleteSessions"></a>
# **accountDeleteSessions**
> accountDeleteSessions()

Delete All Account Sessions

Delete all sessions from the user account and remove any sessions cookies from the end client.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      apiInstance.accountDeleteSessions();
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountDeleteSessions");
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

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="accountGet"></a>
# **accountGet**
> User accountGet()

Get Account

Get currently logged in user data as JSON object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      User result = apiInstance.accountGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGet");
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

[**User**](User.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User |  -  |

<a id="accountGetLogs"></a>
# **accountGetLogs**
> LogList accountGetLogs()

Get Account Logs

Get currently logged in user list of latest security activity logs. Each log returns user IP address, location and date and time of log.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      LogList result = apiInstance.accountGetLogs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGetLogs");
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

[**LogList**](LogList.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Logs List |  -  |

<a id="accountGetPrefs"></a>
# **accountGetPrefs**
> Map&lt;String, Object&gt; accountGetPrefs()

Get Account Preferences

Get currently logged in user preferences as a key-value object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.accountGetPrefs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGetPrefs");
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

**Map&lt;String, Object&gt;**

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Preferences |  -  |

<a id="accountGetSession"></a>
# **accountGetSession**
> Session accountGetSession(sessionId)

Get Session By ID

Use this endpoint to get a logged in user&#39;s session using a Session ID. Inputting &#39;current&#39; will return the current session being used.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String sessionId = "sessionId_example"; // String | Session unique ID. Use the string 'current' to get the current device session.
    try {
      Session result = apiInstance.accountGetSession(sessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGetSession");
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
| **sessionId** | **String**| Session unique ID. Use the string &#39;current&#39; to get the current device session. | |

### Return type

[**Session**](Session.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session |  -  |

<a id="accountGetSessions"></a>
# **accountGetSessions**
> SessionList accountGetSessions()

Get Account Sessions

Get currently logged in user list of active sessions across different devices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      SessionList result = apiInstance.accountGetSessions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGetSessions");
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

[**SessionList**](SessionList.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sessions List |  -  |

<a id="accountUpdateEmail"></a>
# **accountUpdateEmail**
> User accountUpdateEmail(accountUpdateEmailRequest)

Update Account Email

Update currently logged in user account email address. After changing user address, user confirmation status is being reset and a new confirmation mail is sent. For security measures, user password is required to complete this request. This endpoint can also be used to convert an anonymous account to a normal one, by passing an email address and a new password.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    AccountUpdateEmailRequest accountUpdateEmailRequest = new AccountUpdateEmailRequest(); // AccountUpdateEmailRequest | 
    try {
      User result = apiInstance.accountUpdateEmail(accountUpdateEmailRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountUpdateEmail");
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
| **accountUpdateEmailRequest** | [**AccountUpdateEmailRequest**](AccountUpdateEmailRequest.md)|  | [optional] |

### Return type

[**User**](User.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User |  -  |

<a id="accountUpdateName"></a>
# **accountUpdateName**
> User accountUpdateName(accountUpdateNameRequest)

Update Account Name

Update currently logged in user account name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    AccountUpdateNameRequest accountUpdateNameRequest = new AccountUpdateNameRequest(); // AccountUpdateNameRequest | 
    try {
      User result = apiInstance.accountUpdateName(accountUpdateNameRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountUpdateName");
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
| **accountUpdateNameRequest** | [**AccountUpdateNameRequest**](AccountUpdateNameRequest.md)|  | [optional] |

### Return type

[**User**](User.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User |  -  |

<a id="accountUpdatePassword"></a>
# **accountUpdatePassword**
> User accountUpdatePassword(accountUpdatePasswordRequest)

Update Account Password

Update currently logged in user password. For validation, user is required to pass in the new password, and the old password. For users created with OAuth and Team Invites, oldPassword is optional.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    AccountUpdatePasswordRequest accountUpdatePasswordRequest = new AccountUpdatePasswordRequest(); // AccountUpdatePasswordRequest | 
    try {
      User result = apiInstance.accountUpdatePassword(accountUpdatePasswordRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountUpdatePassword");
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
| **accountUpdatePasswordRequest** | [**AccountUpdatePasswordRequest**](AccountUpdatePasswordRequest.md)|  | [optional] |

### Return type

[**User**](User.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User |  -  |

<a id="accountUpdatePrefs"></a>
# **accountUpdatePrefs**
> User accountUpdatePrefs(accountUpdatePrefsRequest)

Update Account Preferences

Update currently logged in user account preferences. You can pass only the specific settings you wish to update.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    AccountUpdatePrefsRequest accountUpdatePrefsRequest = new AccountUpdatePrefsRequest(); // AccountUpdatePrefsRequest | 
    try {
      User result = apiInstance.accountUpdatePrefs(accountUpdatePrefsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountUpdatePrefs");
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
| **accountUpdatePrefsRequest** | [**AccountUpdatePrefsRequest**](AccountUpdatePrefsRequest.md)|  | [optional] |

### Return type

[**User**](User.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User |  -  |

<a id="accountUpdateRecovery"></a>
# **accountUpdateRecovery**
> Token accountUpdateRecovery(accountUpdateRecoveryRequest)

Complete Password Recovery

Use this endpoint to complete the user account password reset. Both the **userId** and **secret** arguments will be passed as query parameters to the redirect URL you have provided when sending your request to the [POST /account/recovery](/docs/client/account#accountCreateRecovery) endpoint.  Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    AccountUpdateRecoveryRequest accountUpdateRecoveryRequest = new AccountUpdateRecoveryRequest(); // AccountUpdateRecoveryRequest | 
    try {
      Token result = apiInstance.accountUpdateRecovery(accountUpdateRecoveryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountUpdateRecovery");
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
| **accountUpdateRecoveryRequest** | [**AccountUpdateRecoveryRequest**](AccountUpdateRecoveryRequest.md)|  | [optional] |

### Return type

[**Token**](Token.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Token |  -  |

<a id="accountUpdateVerification"></a>
# **accountUpdateVerification**
> Token accountUpdateVerification(accountUpdateVerificationRequest)

Complete Email Verification

Use this endpoint to complete the user email verification process. Use both the **userId** and **secret** parameters that were attached to your app URL to verify the user email ownership. If confirmed this route will return a 200 status code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    AccountUpdateVerificationRequest accountUpdateVerificationRequest = new AccountUpdateVerificationRequest(); // AccountUpdateVerificationRequest | 
    try {
      Token result = apiInstance.accountUpdateVerification(accountUpdateVerificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountUpdateVerification");
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
| **accountUpdateVerificationRequest** | [**AccountUpdateVerificationRequest**](AccountUpdateVerificationRequest.md)|  | [optional] |

### Return type

[**Token**](Token.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Token |  -  |

