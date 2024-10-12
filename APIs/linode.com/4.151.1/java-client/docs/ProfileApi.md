# ProfileApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addSSHKey**](ProfileApi.md#addSSHKey) | **POST** /profile/sshkeys | SSH Key Add |
| [**createPersonalAccessToken**](ProfileApi.md#createPersonalAccessToken) | **POST** /profile/tokens | Personal Access Token Create |
| [**deletePersonalAccessToken**](ProfileApi.md#deletePersonalAccessToken) | **DELETE** /profile/tokens/{tokenId} | Personal Access Token Revoke |
| [**deleteProfileApp**](ProfileApi.md#deleteProfileApp) | **DELETE** /profile/apps/{appId} | App Access Revoke |
| [**deleteProfilePhoneNumber**](ProfileApi.md#deleteProfilePhoneNumber) | **DELETE** /profile/phone-number | Phone Number Delete |
| [**deleteSSHKey**](ProfileApi.md#deleteSSHKey) | **DELETE** /profile/sshkeys/{sshKeyId} | SSH Key Delete |
| [**getDevices**](ProfileApi.md#getDevices) | **GET** /profile/devices | Trusted Devices List |
| [**getPersonalAccessToken**](ProfileApi.md#getPersonalAccessToken) | **GET** /profile/tokens/{tokenId} | Personal Access Token View |
| [**getPersonalAccessTokens**](ProfileApi.md#getPersonalAccessTokens) | **GET** /profile/tokens | Personal Access Tokens List |
| [**getProfile**](ProfileApi.md#getProfile) | **GET** /profile | Profile View |
| [**getProfileApp**](ProfileApi.md#getProfileApp) | **GET** /profile/apps/{appId} | Authorized App View |
| [**getProfileApps**](ProfileApi.md#getProfileApps) | **GET** /profile/apps | Authorized Apps List |
| [**getProfileGrants**](ProfileApi.md#getProfileGrants) | **GET** /profile/grants | Grants List |
| [**getProfileLogin**](ProfileApi.md#getProfileLogin) | **GET** /profile/logins/{loginId} | Login View |
| [**getProfileLogins**](ProfileApi.md#getProfileLogins) | **GET** /profile/logins | Logins List |
| [**getSSHKey**](ProfileApi.md#getSSHKey) | **GET** /profile/sshkeys/{sshKeyId} | SSH Key View |
| [**getSSHKeys**](ProfileApi.md#getSSHKeys) | **GET** /profile/sshkeys | SSH Keys List |
| [**getSecurityQuestions**](ProfileApi.md#getSecurityQuestions) | **GET** /profile/security-questions | Security Questions List |
| [**getTrustedDevice**](ProfileApi.md#getTrustedDevice) | **GET** /profile/devices/{deviceId} | Trusted Device View |
| [**getUserPreferences**](ProfileApi.md#getUserPreferences) | **GET** /profile/preferences | User Preferences View |
| [**postProfilePhoneNumber**](ProfileApi.md#postProfilePhoneNumber) | **POST** /profile/phone-number | Phone Number Verification Code Send |
| [**postProfilePhoneNumberVerify**](ProfileApi.md#postProfilePhoneNumberVerify) | **POST** /profile/phone-number/verify | Phone Number Verify |
| [**postSecurityQuestions**](ProfileApi.md#postSecurityQuestions) | **POST** /profile/security-questions | Security Questions Answer |
| [**revokeTrustedDevice**](ProfileApi.md#revokeTrustedDevice) | **DELETE** /profile/devices/{deviceId} | Trusted Device Revoke |
| [**tfaConfirm**](ProfileApi.md#tfaConfirm) | **POST** /profile/tfa-enable-confirm | Two Factor Authentication Confirm/Enable |
| [**tfaDisable**](ProfileApi.md#tfaDisable) | **POST** /profile/tfa-disable | Two Factor Authentication Disable |
| [**tfaEnable**](ProfileApi.md#tfaEnable) | **POST** /profile/tfa-enable | Two Factor Secret Create |
| [**updatePersonalAccessToken**](ProfileApi.md#updatePersonalAccessToken) | **PUT** /profile/tokens/{tokenId} | Personal Access Token Update |
| [**updateProfile**](ProfileApi.md#updateProfile) | **PUT** /profile | Profile Update |
| [**updateSSHKey**](ProfileApi.md#updateSSHKey) | **PUT** /profile/sshkeys/{sshKeyId} | SSH Key Update |
| [**updateUserPreferences**](ProfileApi.md#updateUserPreferences) | **PUT** /profile/preferences | User Preferences Update |


<a id="addSSHKey"></a>
# **addSSHKey**
> SSHKey addSSHKey(ssHKey)

SSH Key Add

Adds an SSH Key to your Account profile. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    SSHKey ssHKey = new SSHKey(); // SSHKey | Add SSH Key
    try {
      SSHKey result = apiInstance.addSSHKey(ssHKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#addSSHKey");
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
| **ssHKey** | [**SSHKey**](SSHKey.md)| Add SSH Key | [optional] |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SSH Key associated successfully. |  -  |
| **0** | Error |  -  |

<a id="createPersonalAccessToken"></a>
# **createPersonalAccessToken**
> PersonalAccessToken createPersonalAccessToken(createPersonalAccessTokenRequest)

Personal Access Token Create

Creates a Personal Access Token for your User. The raw token will be returned in the response, but will never be returned again afterward so be sure to take note of it. You may create a token with _at most_ the scopes of your current token. The created token will be able to access your Account until the given expiry, or until it is revoked. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    CreatePersonalAccessTokenRequest createPersonalAccessTokenRequest = new CreatePersonalAccessTokenRequest(); // CreatePersonalAccessTokenRequest | Information about the requested token.
    try {
      PersonalAccessToken result = apiInstance.createPersonalAccessToken(createPersonalAccessTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#createPersonalAccessToken");
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
| **createPersonalAccessTokenRequest** | [**CreatePersonalAccessTokenRequest**](CreatePersonalAccessTokenRequest.md)| Information about the requested token. | |

### Return type

[**PersonalAccessToken**](PersonalAccessToken.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Token created successfully. |  -  |
| **0** | Error |  -  |

<a id="deletePersonalAccessToken"></a>
# **deletePersonalAccessToken**
> Object deletePersonalAccessToken(tokenId)

Personal Access Token Revoke

Revokes a Personal Access Token. The token will be invalidated immediately, and requests using that token will fail with a 401. It is possible to revoke access to the token making the request to revoke a token, but keep in mind that doing so could lose you access to the api and require you to create a new token through some other means. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer tokenId = 56; // Integer | The ID of the token to access.
    try {
      Object result = apiInstance.deletePersonalAccessToken(tokenId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#deletePersonalAccessToken");
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
| **tokenId** | **Integer**| The ID of the token to access. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Token revoked successfully. |  -  |
| **0** | Error |  -  |

<a id="deleteProfileApp"></a>
# **deleteProfileApp**
> Object deleteProfileApp(appId)

App Access Revoke

Expires this app token. This token may no longer be used to access your Account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer appId = 56; // Integer | The authorized app ID to manage.
    try {
      Object result = apiInstance.deleteProfileApp(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#deleteProfileApp");
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
| **appId** | **Integer**| The authorized app ID to manage. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | App&#39;s authorization has been revoked. |  -  |
| **0** | Error |  -  |

<a id="deleteProfilePhoneNumber"></a>
# **deleteProfilePhoneNumber**
> Object deleteProfilePhoneNumber()

Phone Number Delete

Delete the verified phone number for the User making this request.  Use this command to opt out of SMS messages for the requesting User after a phone number has been verified with the **Phone Number Verify** ([POST /profile/phone-number/verify](/docs/api/profile/#phone-number-verify)) command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    try {
      Object result = apiInstance.deleteProfilePhoneNumber();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#deleteProfilePhoneNumber");
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

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone number deletion request successful.  |  -  |
| **0** | Error |  -  |

<a id="deleteSSHKey"></a>
# **deleteSSHKey**
> Object deleteSSHKey(sshKeyId)

SSH Key Delete

Deletes an SSH Key you have access to.  **Note:** deleting an SSH Key will *not* remove it from any Linode or Disk that was deployed with &#x60;authorized_keys&#x60;. In those cases, the keys must be manually deleted on the Linode or Disk. This endpoint will only delete the key&#39;s association from your Profile. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer sshKeyId = 56; // Integer | The ID of the SSHKey
    try {
      Object result = apiInstance.deleteSSHKey(sshKeyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#deleteSSHKey");
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
| **sshKeyId** | **Integer**| The ID of the SSHKey | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SSH Key deleted successfully. |  -  |
| **0** | Error |  -  |

<a id="getDevices"></a>
# **getDevices**
> GetDevices200Response getDevices()

Trusted Devices List

Returns a paginated list of active TrustedDevices for your User. Browsers with an active Remember Me Session are logged into your account until the session expires or is revoked. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    try {
      GetDevices200Response result = apiInstance.getDevices();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getDevices");
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

[**GetDevices200Response**](GetDevices200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of TrustedDevice objects. |  -  |
| **0** | Error |  -  |

<a id="getPersonalAccessToken"></a>
# **getPersonalAccessToken**
> PersonalAccessToken getPersonalAccessToken(tokenId)

Personal Access Token View

Returns a single Personal Access Token. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer tokenId = 56; // Integer | The ID of the token to access.
    try {
      PersonalAccessToken result = apiInstance.getPersonalAccessToken(tokenId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getPersonalAccessToken");
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
| **tokenId** | **Integer**| The ID of the token to access. | |

### Return type

[**PersonalAccessToken**](PersonalAccessToken.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested token. |  -  |
| **0** | Error |  -  |

<a id="getPersonalAccessTokens"></a>
# **getPersonalAccessTokens**
> GetPersonalAccessTokens200Response getPersonalAccessTokens()

Personal Access Tokens List

Returns a paginated list of Personal Access Tokens currently active for your User. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    try {
      GetPersonalAccessTokens200Response result = apiInstance.getPersonalAccessTokens();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getPersonalAccessTokens");
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

[**GetPersonalAccessTokens200Response**](GetPersonalAccessTokens200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of active tokens. |  -  |
| **0** | Error |  -  |

<a id="getProfile"></a>
# **getProfile**
> Profile getProfile()

Profile View

Returns information about the current User. This can be used to see who is acting in applications where more than one token is managed. For example, in third-party OAuth applications.  This endpoint is always accessible, no matter what OAuth scopes the acting token has. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    try {
      Profile result = apiInstance.getProfile();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getProfile");
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

[**Profile**](Profile.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Profile response. |  -  |
| **0** | Error |  -  |

<a id="getProfileApp"></a>
# **getProfileApp**
> AuthorizedApp getProfileApp(appId)

Authorized App View

Returns information about a single app you&#39;ve authorized to access your Account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer appId = 56; // Integer | The authorized app ID to manage.
    try {
      AuthorizedApp result = apiInstance.getProfileApp(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getProfileApp");
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
| **appId** | **Integer**| The authorized app ID to manage. | |

### Return type

[**AuthorizedApp**](AuthorizedApp.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The app requested. |  -  |
| **0** | Error |  -  |

<a id="getProfileApps"></a>
# **getProfileApps**
> GetProfileApps200Response getProfileApps(page, pageSize)

Authorized Apps List

This is a collection of OAuth apps that you&#39;ve given access to your Account, and includes the level of access granted. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetProfileApps200Response result = apiInstance.getProfileApps(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getProfileApps");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetProfileApps200Response**](GetProfileApps200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of apps you&#39;ve authorized.  |  -  |
| **0** | Error |  -  |

<a id="getProfileGrants"></a>
# **getProfileGrants**
> GrantsResponse getProfileGrants()

Grants List

This returns a GrantsResponse describing what the acting User has been granted access to.  For unrestricted users, this will return a  204 and no body because unrestricted users have access to everything without grants.  This will not return information about entities you do not have access to.  This endpoint is useful when writing third-party OAuth applications to see what options you should present to the acting User.  For example, if they do not have &#x60;global.add_linodes&#x60;, you might not display a button to deploy a new Linode.  Any client may access this endpoint; no OAuth scopes are required. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    try {
      GrantsResponse result = apiInstance.getProfileGrants();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getProfileGrants");
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

[**GrantsResponse**](GrantsResponse.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | GrantsResponse |  -  |
| **204** | This is an unrestricted User, who has no grants. This User can access everything on the Account.  |  -  |
| **0** | Error |  -  |

<a id="getProfileLogin"></a>
# **getProfileLogin**
> Login getProfileLogin(loginId)

Login View

Returns a login object displaying information about a successful account login from this user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer loginId = 56; // Integer | The ID of the login object to access.
    try {
      Login result = apiInstance.getProfileLogin(loginId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getProfileLogin");
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
| **loginId** | **Integer**| The ID of the login object to access. | |

### Return type

[**Login**](Login.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested login object. |  -  |
| **0** | Error |  -  |

<a id="getProfileLogins"></a>
# **getProfileLogins**
> GetAccountLogins200Response getProfileLogins()

Logins List

Returns a collection of successful account logins from this user during the last 90 days. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    try {
      GetAccountLogins200Response result = apiInstance.getProfileLogins();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getProfileLogins");
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

[**GetAccountLogins200Response**](GetAccountLogins200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of successful account logins from this user during the last 90 days.  |  -  |
| **0** | Error |  -  |

<a id="getSSHKey"></a>
# **getSSHKey**
> SSHKey getSSHKey(sshKeyId)

SSH Key View

Returns a single SSH Key object identified by &#x60;id&#x60; that you have access to view. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer sshKeyId = 56; // Integer | The ID of the SSHKey
    try {
      SSHKey result = apiInstance.getSSHKey(sshKeyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getSSHKey");
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
| **sshKeyId** | **Integer**| The ID of the SSHKey | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An SSH Key object |  -  |
| **0** | Error |  -  |

<a id="getSSHKeys"></a>
# **getSSHKeys**
> GetSSHKeys200Response getSSHKeys(page, pageSize)

SSH Keys List

Returns a collection of SSH Keys you&#39;ve added to your Profile. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetSSHKeys200Response result = apiInstance.getSSHKeys(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getSSHKeys");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetSSHKeys200Response**](GetSSHKeys200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of SSH Key objects. |  -  |
| **0** | Error |  -  |

<a id="getSecurityQuestions"></a>
# **getSecurityQuestions**
> SecurityQuestionsGet getSecurityQuestions()

Security Questions List

Returns a collection of security questions and their responses, if any, for your User Profile. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    try {
      SecurityQuestionsGet result = apiInstance.getSecurityQuestions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getSecurityQuestions");
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

[**SecurityQuestionsGet**](SecurityQuestionsGet.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of security questions. |  -  |
| **0** | Error |  -  |

<a id="getTrustedDevice"></a>
# **getTrustedDevice**
> TrustedDevice getTrustedDevice(deviceId)

Trusted Device View

Returns a single active TrustedDevice for your User. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer deviceId = 56; // Integer | The ID of the TrustedDevice
    try {
      TrustedDevice result = apiInstance.getTrustedDevice(deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getTrustedDevice");
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
| **deviceId** | **Integer**| The ID of the TrustedDevice | |

### Return type

[**TrustedDevice**](TrustedDevice.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested TrustedDevice object |  -  |
| **0** | Error |  -  |

<a id="getUserPreferences"></a>
# **getUserPreferences**
> Object getUserPreferences()

User Preferences View

View a list of user preferences tied to the OAuth client that generated the token making the request. The user preferences endpoints allow consumers of the API to store arbitrary JSON data, such as a user&#39;s font size preference or preferred display name. User preferences are available for each OAuth client registered to your account, and as such an account can have multiple user preferences. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    try {
      Object result = apiInstance.getUserPreferences();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getUserPreferences");
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

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an object of user preferences. |  -  |
| **0** | Error |  -  |

<a id="postProfilePhoneNumber"></a>
# **postProfilePhoneNumber**
> Object postProfilePhoneNumber(postProfilePhoneNumberRequest)

Phone Number Verification Code Send

Send a one-time verification code via SMS message to the submitted phone number. Providing your phone number helps ensure you can securely access your Account in case other ways to connect are lost. Your phone number is only used to verify your identity by sending an SMS message. Standard carrier messaging fees may apply.  * By accessing this command you are opting in to receive SMS messages. You can opt out of SMS messages by using the **Phone Number Delete** ([DELETE /profile/phone-number](/docs/api/profile/#phone-number-delete)) command after your phone number is verified.  * Verification codes are valid for 10 minutes after they are sent.  * Subsequent requests made prior to code expiration result in sending the same code.  Once a verification code is received, verify your phone number with the **Phone Number Verify** ([POST /profile/phone-number/verify](/docs/api/profile/#phone-number-verify)) command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    PostProfilePhoneNumberRequest postProfilePhoneNumberRequest = new PostProfilePhoneNumberRequest(); // PostProfilePhoneNumberRequest | Enter a phone number and country code for verification.
    try {
      Object result = apiInstance.postProfilePhoneNumber(postProfilePhoneNumberRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#postProfilePhoneNumber");
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
| **postProfilePhoneNumberRequest** | [**PostProfilePhoneNumberRequest**](PostProfilePhoneNumberRequest.md)| Enter a phone number and country code for verification. | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone number verification code request successful.  |  -  |
| **0** | Error |  -  |

<a id="postProfilePhoneNumberVerify"></a>
# **postProfilePhoneNumberVerify**
> Object postProfilePhoneNumberVerify(postProfilePhoneNumberVerifyRequest)

Phone Number Verify

Verify a phone number by confirming the one-time code received via SMS message after accessing the **Phone Verification Code Send** ([POST /profile/phone-number](/docs/api/profile/#phone-number-verification-code-send)) command.  * Verification codes are valid for 10 minutes after they are sent.  * Only the same User that made the verification code request can use that code with this command.  Once completed, the verified phone number is assigned to the User making the request. To change the verified phone number for a User, first use the **Phone Number Delete** ([DELETE /profile/phone-number](/docs/api/profile/#phone-number-delete)) command, then begin the verification process again with the **Phone Verification Code Send** ([POST /profile/phone-number](/docs/api/profile/#phone-number-verification-code-send)) command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    PostProfilePhoneNumberVerifyRequest postProfilePhoneNumberVerifyRequest = new PostProfilePhoneNumberVerifyRequest(); // PostProfilePhoneNumberVerifyRequest | Enter a phone verification code for confirmation.
    try {
      Object result = apiInstance.postProfilePhoneNumberVerify(postProfilePhoneNumberVerifyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#postProfilePhoneNumberVerify");
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
| **postProfilePhoneNumberVerifyRequest** | [**PostProfilePhoneNumberVerifyRequest**](PostProfilePhoneNumberVerifyRequest.md)| Enter a phone verification code for confirmation. | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone number verification successful.  |  -  |
| **0** | Error |  -  |

<a id="postSecurityQuestions"></a>
# **postSecurityQuestions**
> SecurityQuestionsPost postSecurityQuestions(securityQuestionsPost)

Security Questions Answer

Adds security question responses for your User.  Requires exactly three unique questions.  Previous responses are overwritten if answered or reset to &#x60;null&#x60; if unanswered.  **Note**: Security questions must be answered for your User prior to accessing the **Two Factor Secret Create** ([POST /profile/tfa-enable](/docs/api/profile/#two-factor-secret-create)) command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    SecurityQuestionsPost securityQuestionsPost = new SecurityQuestionsPost(); // SecurityQuestionsPost | Answer Security Questions
    try {
      SecurityQuestionsPost result = apiInstance.postSecurityQuestions(securityQuestionsPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#postSecurityQuestions");
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
| **securityQuestionsPost** | [**SecurityQuestionsPost**](SecurityQuestionsPost.md)| Answer Security Questions | [optional] |

### Return type

[**SecurityQuestionsPost**](SecurityQuestionsPost.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Security Questions answered successfully. |  -  |
| **0** | Error |  -  |

<a id="revokeTrustedDevice"></a>
# **revokeTrustedDevice**
> Object revokeTrustedDevice(deviceId)

Trusted Device Revoke

Revoke an active TrustedDevice for your User.  Once a TrustedDevice is revoked, this device will have to log in again before accessing your Linode account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer deviceId = 56; // Integer | The ID of the TrustedDevice
    try {
      Object result = apiInstance.revokeTrustedDevice(deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#revokeTrustedDevice");
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
| **deviceId** | **Integer**| The ID of the TrustedDevice | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session revoked successfully |  -  |
| **0** | Error |  -  |

<a id="tfaConfirm"></a>
# **tfaConfirm**
> TfaConfirm200Response tfaConfirm(tfaConfirmRequest)

Two Factor Authentication Confirm/Enable

Confirms that you can successfully generate Two Factor codes and enables TFA on your Account. Once this is complete, login attempts from untrusted computers will be required to provide a Two Factor code before they are successful. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    TfaConfirmRequest tfaConfirmRequest = new TfaConfirmRequest(); // TfaConfirmRequest | The Two Factor code you generated with your Two Factor secret.
    try {
      TfaConfirm200Response result = apiInstance.tfaConfirm(tfaConfirmRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#tfaConfirm");
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
| **tfaConfirmRequest** | [**TfaConfirmRequest**](TfaConfirmRequest.md)| The Two Factor code you generated with your Two Factor secret. | |

### Return type

[**TfaConfirm200Response**](TfaConfirm200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TFA enabled successfully |  -  |
| **0** | Error |  -  |

<a id="tfaDisable"></a>
# **tfaDisable**
> Object tfaDisable()

Two Factor Authentication Disable

Disables Two Factor Authentication for your User. Once successful, login attempts from untrusted computers will only require a password before being successful. This is less secure, and is discouraged. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    try {
      Object result = apiInstance.tfaDisable();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#tfaDisable");
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

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TFA disabled. |  -  |
| **0** | Error |  -  |

<a id="tfaEnable"></a>
# **tfaEnable**
> TfaEnable200Response tfaEnable()

Two Factor Secret Create

Generates a Two Factor secret for your User. To enable TFA for your User, enter the secret obtained from this command with the **Two Factor Authentication Confirm/Enable** ([POST /profile/tfa-enable-confirm](/docs/api/profile/#two-factor-authentication-confirmenable)) command. Once enabled, logins from untrusted computers are required to provide a TFA code before they are successful.  **Note**: Before you can enable TFA, security questions must be answered for your User by accessing the **Security Questions Answer** ([POST /profile/security-questions](/docs/api/profile/#security-questions-answer)) command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    try {
      TfaEnable200Response result = apiInstance.tfaEnable();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#tfaEnable");
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

[**TfaEnable200Response**](TfaEnable200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Two Factor secret generated |  -  |
| **0** | Error |  -  |

<a id="updatePersonalAccessToken"></a>
# **updatePersonalAccessToken**
> PersonalAccessToken updatePersonalAccessToken(tokenId, personalAccessToken)

Personal Access Token Update

Updates a Personal Access Token. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer tokenId = 56; // Integer | The ID of the token to access.
    PersonalAccessToken personalAccessToken = new PersonalAccessToken(); // PersonalAccessToken | The fields to update.
    try {
      PersonalAccessToken result = apiInstance.updatePersonalAccessToken(tokenId, personalAccessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#updatePersonalAccessToken");
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
| **tokenId** | **Integer**| The ID of the token to access. | |
| **personalAccessToken** | [**PersonalAccessToken**](PersonalAccessToken.md)| The fields to update. | |

### Return type

[**PersonalAccessToken**](PersonalAccessToken.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Token updated successfully. |  -  |
| **0** | Error |  -  |

<a id="updateProfile"></a>
# **updateProfile**
> Profile updateProfile(profile)

Profile Update

Update information in your Profile.  This endpoint requires the \&quot;account:read_write\&quot; OAuth Scope. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Profile profile = new Profile(); // Profile | The fields to update.
    try {
      Profile result = apiInstance.updateProfile(profile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#updateProfile");
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
| **profile** | [**Profile**](Profile.md)| The fields to update. | |

### Return type

[**Profile**](Profile.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Profile updated successfully. |  -  |
| **0** | Error |  -  |

<a id="updateSSHKey"></a>
# **updateSSHKey**
> SSHKey updateSSHKey(sshKeyId, updateSSHKeyRequest)

SSH Key Update

Updates an SSH Key that you have permission to &#x60;read_write&#x60;.  Only SSH key labels can be updated. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Integer sshKeyId = 56; // Integer | The ID of the SSHKey
    UpdateSSHKeyRequest updateSSHKeyRequest = new UpdateSSHKeyRequest(); // UpdateSSHKeyRequest | The fields to update. 
    try {
      SSHKey result = apiInstance.updateSSHKey(sshKeyId, updateSSHKeyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#updateSSHKey");
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
| **sshKeyId** | **Integer**| The ID of the SSHKey | |
| **updateSSHKeyRequest** | [**UpdateSSHKeyRequest**](UpdateSSHKeyRequest.md)| The fields to update.  | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SSH Key updated successfully. |  -  |
| **0** | Error |  -  |

<a id="updateUserPreferences"></a>
# **updateUserPreferences**
> Object updateUserPreferences(body)

User Preferences Update

Updates a user&#39;s preferences. These preferences are tied to the OAuth client that generated the token making the request. The user preferences endpoints allow consumers of the API to store arbitrary JSON data, such as a user&#39;s font size preference or preferred display name. An account may have multiple preferences. Preferences, and the pertaining request body, may contain any arbitrary JSON data that the user would like to store. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    Object body = null; // Object | The user preferences to update or store. 
    try {
      Object result = apiInstance.updateUserPreferences(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#updateUserPreferences");
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
| **body** | **Object**| The user preferences to update or store.  | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an object of user preferences. |  -  |
| **0** | Error |  -  |

