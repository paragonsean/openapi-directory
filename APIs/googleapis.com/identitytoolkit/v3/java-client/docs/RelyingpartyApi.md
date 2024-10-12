# RelyingpartyApi

All URIs are relative to *https://www.googleapis.com/identitytoolkit/v3/relyingparty*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**identitytoolkitRelyingpartyCreateAuthUri**](RelyingpartyApi.md#identitytoolkitRelyingpartyCreateAuthUri) | **POST** /createAuthUri |  |
| [**identitytoolkitRelyingpartyDeleteAccount**](RelyingpartyApi.md#identitytoolkitRelyingpartyDeleteAccount) | **POST** /deleteAccount |  |
| [**identitytoolkitRelyingpartyDownloadAccount**](RelyingpartyApi.md#identitytoolkitRelyingpartyDownloadAccount) | **POST** /downloadAccount |  |
| [**identitytoolkitRelyingpartyEmailLinkSignin**](RelyingpartyApi.md#identitytoolkitRelyingpartyEmailLinkSignin) | **POST** /emailLinkSignin |  |
| [**identitytoolkitRelyingpartyGetAccountInfo**](RelyingpartyApi.md#identitytoolkitRelyingpartyGetAccountInfo) | **POST** /getAccountInfo |  |
| [**identitytoolkitRelyingpartyGetOobConfirmationCode**](RelyingpartyApi.md#identitytoolkitRelyingpartyGetOobConfirmationCode) | **POST** /getOobConfirmationCode |  |
| [**identitytoolkitRelyingpartyGetProjectConfig**](RelyingpartyApi.md#identitytoolkitRelyingpartyGetProjectConfig) | **GET** /getProjectConfig |  |
| [**identitytoolkitRelyingpartyGetPublicKeys**](RelyingpartyApi.md#identitytoolkitRelyingpartyGetPublicKeys) | **GET** /publicKeys |  |
| [**identitytoolkitRelyingpartyGetRecaptchaParam**](RelyingpartyApi.md#identitytoolkitRelyingpartyGetRecaptchaParam) | **GET** /getRecaptchaParam |  |
| [**identitytoolkitRelyingpartyResetPassword**](RelyingpartyApi.md#identitytoolkitRelyingpartyResetPassword) | **POST** /resetPassword |  |
| [**identitytoolkitRelyingpartySendVerificationCode**](RelyingpartyApi.md#identitytoolkitRelyingpartySendVerificationCode) | **POST** /sendVerificationCode |  |
| [**identitytoolkitRelyingpartySetAccountInfo**](RelyingpartyApi.md#identitytoolkitRelyingpartySetAccountInfo) | **POST** /setAccountInfo |  |
| [**identitytoolkitRelyingpartySetProjectConfig**](RelyingpartyApi.md#identitytoolkitRelyingpartySetProjectConfig) | **POST** /setProjectConfig |  |
| [**identitytoolkitRelyingpartySignOutUser**](RelyingpartyApi.md#identitytoolkitRelyingpartySignOutUser) | **POST** /signOutUser |  |
| [**identitytoolkitRelyingpartySignupNewUser**](RelyingpartyApi.md#identitytoolkitRelyingpartySignupNewUser) | **POST** /signupNewUser |  |
| [**identitytoolkitRelyingpartyUploadAccount**](RelyingpartyApi.md#identitytoolkitRelyingpartyUploadAccount) | **POST** /uploadAccount |  |
| [**identitytoolkitRelyingpartyVerifyAssertion**](RelyingpartyApi.md#identitytoolkitRelyingpartyVerifyAssertion) | **POST** /verifyAssertion |  |
| [**identitytoolkitRelyingpartyVerifyCustomToken**](RelyingpartyApi.md#identitytoolkitRelyingpartyVerifyCustomToken) | **POST** /verifyCustomToken |  |
| [**identitytoolkitRelyingpartyVerifyPassword**](RelyingpartyApi.md#identitytoolkitRelyingpartyVerifyPassword) | **POST** /verifyPassword |  |
| [**identitytoolkitRelyingpartyVerifyPhoneNumber**](RelyingpartyApi.md#identitytoolkitRelyingpartyVerifyPhoneNumber) | **POST** /verifyPhoneNumber |  |


<a id="identitytoolkitRelyingpartyCreateAuthUri"></a>
# **identitytoolkitRelyingpartyCreateAuthUri**
> CreateAuthUriResponse identitytoolkitRelyingpartyCreateAuthUri(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyCreateAuthUriRequest)



Creates the URI used by the IdP to authenticate the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartyCreateAuthUriRequest identitytoolkitRelyingpartyCreateAuthUriRequest = new IdentitytoolkitRelyingpartyCreateAuthUriRequest(); // IdentitytoolkitRelyingpartyCreateAuthUriRequest | 
    try {
      CreateAuthUriResponse result = apiInstance.identitytoolkitRelyingpartyCreateAuthUri(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyCreateAuthUriRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyCreateAuthUri");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartyCreateAuthUriRequest** | [**IdentitytoolkitRelyingpartyCreateAuthUriRequest**](IdentitytoolkitRelyingpartyCreateAuthUriRequest.md)|  | [optional] |

### Return type

[**CreateAuthUriResponse**](CreateAuthUriResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyDeleteAccount"></a>
# **identitytoolkitRelyingpartyDeleteAccount**
> DeleteAccountResponse identitytoolkitRelyingpartyDeleteAccount(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyDeleteAccountRequest)



Delete user account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartyDeleteAccountRequest identitytoolkitRelyingpartyDeleteAccountRequest = new IdentitytoolkitRelyingpartyDeleteAccountRequest(); // IdentitytoolkitRelyingpartyDeleteAccountRequest | 
    try {
      DeleteAccountResponse result = apiInstance.identitytoolkitRelyingpartyDeleteAccount(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyDeleteAccountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyDeleteAccount");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartyDeleteAccountRequest** | [**IdentitytoolkitRelyingpartyDeleteAccountRequest**](IdentitytoolkitRelyingpartyDeleteAccountRequest.md)|  | [optional] |

### Return type

[**DeleteAccountResponse**](DeleteAccountResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyDownloadAccount"></a>
# **identitytoolkitRelyingpartyDownloadAccount**
> DownloadAccountResponse identitytoolkitRelyingpartyDownloadAccount(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyDownloadAccountRequest)



Batch download user accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartyDownloadAccountRequest identitytoolkitRelyingpartyDownloadAccountRequest = new IdentitytoolkitRelyingpartyDownloadAccountRequest(); // IdentitytoolkitRelyingpartyDownloadAccountRequest | 
    try {
      DownloadAccountResponse result = apiInstance.identitytoolkitRelyingpartyDownloadAccount(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyDownloadAccountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyDownloadAccount");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartyDownloadAccountRequest** | [**IdentitytoolkitRelyingpartyDownloadAccountRequest**](IdentitytoolkitRelyingpartyDownloadAccountRequest.md)|  | [optional] |

### Return type

[**DownloadAccountResponse**](DownloadAccountResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyEmailLinkSignin"></a>
# **identitytoolkitRelyingpartyEmailLinkSignin**
> EmailLinkSigninResponse identitytoolkitRelyingpartyEmailLinkSignin(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyEmailLinkSigninRequest)



Reset password for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartyEmailLinkSigninRequest identitytoolkitRelyingpartyEmailLinkSigninRequest = new IdentitytoolkitRelyingpartyEmailLinkSigninRequest(); // IdentitytoolkitRelyingpartyEmailLinkSigninRequest | 
    try {
      EmailLinkSigninResponse result = apiInstance.identitytoolkitRelyingpartyEmailLinkSignin(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyEmailLinkSigninRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyEmailLinkSignin");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartyEmailLinkSigninRequest** | [**IdentitytoolkitRelyingpartyEmailLinkSigninRequest**](IdentitytoolkitRelyingpartyEmailLinkSigninRequest.md)|  | [optional] |

### Return type

[**EmailLinkSigninResponse**](EmailLinkSigninResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyGetAccountInfo"></a>
# **identitytoolkitRelyingpartyGetAccountInfo**
> GetAccountInfoResponse identitytoolkitRelyingpartyGetAccountInfo(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyGetAccountInfoRequest)



Returns the account info.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartyGetAccountInfoRequest identitytoolkitRelyingpartyGetAccountInfoRequest = new IdentitytoolkitRelyingpartyGetAccountInfoRequest(); // IdentitytoolkitRelyingpartyGetAccountInfoRequest | 
    try {
      GetAccountInfoResponse result = apiInstance.identitytoolkitRelyingpartyGetAccountInfo(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyGetAccountInfoRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyGetAccountInfo");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartyGetAccountInfoRequest** | [**IdentitytoolkitRelyingpartyGetAccountInfoRequest**](IdentitytoolkitRelyingpartyGetAccountInfoRequest.md)|  | [optional] |

### Return type

[**GetAccountInfoResponse**](GetAccountInfoResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyGetOobConfirmationCode"></a>
# **identitytoolkitRelyingpartyGetOobConfirmationCode**
> GetOobConfirmationCodeResponse identitytoolkitRelyingpartyGetOobConfirmationCode(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, relyingparty)



Get a code for user action confirmation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Relyingparty relyingparty = new Relyingparty(); // Relyingparty | 
    try {
      GetOobConfirmationCodeResponse result = apiInstance.identitytoolkitRelyingpartyGetOobConfirmationCode(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, relyingparty);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyGetOobConfirmationCode");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **relyingparty** | [**Relyingparty**](Relyingparty.md)|  | [optional] |

### Return type

[**GetOobConfirmationCodeResponse**](GetOobConfirmationCodeResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyGetProjectConfig"></a>
# **identitytoolkitRelyingpartyGetProjectConfig**
> IdentitytoolkitRelyingpartyGetProjectConfigResponse identitytoolkitRelyingpartyGetProjectConfig(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, delegatedProjectNumber, projectNumber)



Get project configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String delegatedProjectNumber = "delegatedProjectNumber_example"; // String | Delegated GCP project number of the request.
    String projectNumber = "projectNumber_example"; // String | GCP project number of the request.
    try {
      IdentitytoolkitRelyingpartyGetProjectConfigResponse result = apiInstance.identitytoolkitRelyingpartyGetProjectConfig(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, delegatedProjectNumber, projectNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyGetProjectConfig");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **delegatedProjectNumber** | **String**| Delegated GCP project number of the request. | [optional] |
| **projectNumber** | **String**| GCP project number of the request. | [optional] |

### Return type

[**IdentitytoolkitRelyingpartyGetProjectConfigResponse**](IdentitytoolkitRelyingpartyGetProjectConfigResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyGetPublicKeys"></a>
# **identitytoolkitRelyingpartyGetPublicKeys**
> Map&lt;String, String&gt; identitytoolkitRelyingpartyGetPublicKeys(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Get token signing public key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      Map<String, String> result = apiInstance.identitytoolkitRelyingpartyGetPublicKeys(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyGetPublicKeys");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

**Map&lt;String, String&gt;**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyGetRecaptchaParam"></a>
# **identitytoolkitRelyingpartyGetRecaptchaParam**
> GetRecaptchaParamResponse identitytoolkitRelyingpartyGetRecaptchaParam(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Get recaptcha secure param.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      GetRecaptchaParamResponse result = apiInstance.identitytoolkitRelyingpartyGetRecaptchaParam(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyGetRecaptchaParam");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**GetRecaptchaParamResponse**](GetRecaptchaParamResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyResetPassword"></a>
# **identitytoolkitRelyingpartyResetPassword**
> ResetPasswordResponse identitytoolkitRelyingpartyResetPassword(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyResetPasswordRequest)



Reset password for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartyResetPasswordRequest identitytoolkitRelyingpartyResetPasswordRequest = new IdentitytoolkitRelyingpartyResetPasswordRequest(); // IdentitytoolkitRelyingpartyResetPasswordRequest | 
    try {
      ResetPasswordResponse result = apiInstance.identitytoolkitRelyingpartyResetPassword(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyResetPasswordRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyResetPassword");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartyResetPasswordRequest** | [**IdentitytoolkitRelyingpartyResetPasswordRequest**](IdentitytoolkitRelyingpartyResetPasswordRequest.md)|  | [optional] |

### Return type

[**ResetPasswordResponse**](ResetPasswordResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartySendVerificationCode"></a>
# **identitytoolkitRelyingpartySendVerificationCode**
> IdentitytoolkitRelyingpartySendVerificationCodeResponse identitytoolkitRelyingpartySendVerificationCode(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartySendVerificationCodeRequest)



Send SMS verification code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartySendVerificationCodeRequest identitytoolkitRelyingpartySendVerificationCodeRequest = new IdentitytoolkitRelyingpartySendVerificationCodeRequest(); // IdentitytoolkitRelyingpartySendVerificationCodeRequest | 
    try {
      IdentitytoolkitRelyingpartySendVerificationCodeResponse result = apiInstance.identitytoolkitRelyingpartySendVerificationCode(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartySendVerificationCodeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartySendVerificationCode");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartySendVerificationCodeRequest** | [**IdentitytoolkitRelyingpartySendVerificationCodeRequest**](IdentitytoolkitRelyingpartySendVerificationCodeRequest.md)|  | [optional] |

### Return type

[**IdentitytoolkitRelyingpartySendVerificationCodeResponse**](IdentitytoolkitRelyingpartySendVerificationCodeResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartySetAccountInfo"></a>
# **identitytoolkitRelyingpartySetAccountInfo**
> SetAccountInfoResponse identitytoolkitRelyingpartySetAccountInfo(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartySetAccountInfoRequest)



Set account info for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartySetAccountInfoRequest identitytoolkitRelyingpartySetAccountInfoRequest = new IdentitytoolkitRelyingpartySetAccountInfoRequest(); // IdentitytoolkitRelyingpartySetAccountInfoRequest | 
    try {
      SetAccountInfoResponse result = apiInstance.identitytoolkitRelyingpartySetAccountInfo(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartySetAccountInfoRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartySetAccountInfo");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartySetAccountInfoRequest** | [**IdentitytoolkitRelyingpartySetAccountInfoRequest**](IdentitytoolkitRelyingpartySetAccountInfoRequest.md)|  | [optional] |

### Return type

[**SetAccountInfoResponse**](SetAccountInfoResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartySetProjectConfig"></a>
# **identitytoolkitRelyingpartySetProjectConfig**
> IdentitytoolkitRelyingpartySetProjectConfigResponse identitytoolkitRelyingpartySetProjectConfig(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartySetProjectConfigRequest)



Set project configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartySetProjectConfigRequest identitytoolkitRelyingpartySetProjectConfigRequest = new IdentitytoolkitRelyingpartySetProjectConfigRequest(); // IdentitytoolkitRelyingpartySetProjectConfigRequest | 
    try {
      IdentitytoolkitRelyingpartySetProjectConfigResponse result = apiInstance.identitytoolkitRelyingpartySetProjectConfig(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartySetProjectConfigRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartySetProjectConfig");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartySetProjectConfigRequest** | [**IdentitytoolkitRelyingpartySetProjectConfigRequest**](IdentitytoolkitRelyingpartySetProjectConfigRequest.md)|  | [optional] |

### Return type

[**IdentitytoolkitRelyingpartySetProjectConfigResponse**](IdentitytoolkitRelyingpartySetProjectConfigResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartySignOutUser"></a>
# **identitytoolkitRelyingpartySignOutUser**
> IdentitytoolkitRelyingpartySignOutUserResponse identitytoolkitRelyingpartySignOutUser(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartySignOutUserRequest)



Sign out user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartySignOutUserRequest identitytoolkitRelyingpartySignOutUserRequest = new IdentitytoolkitRelyingpartySignOutUserRequest(); // IdentitytoolkitRelyingpartySignOutUserRequest | 
    try {
      IdentitytoolkitRelyingpartySignOutUserResponse result = apiInstance.identitytoolkitRelyingpartySignOutUser(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartySignOutUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartySignOutUser");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartySignOutUserRequest** | [**IdentitytoolkitRelyingpartySignOutUserRequest**](IdentitytoolkitRelyingpartySignOutUserRequest.md)|  | [optional] |

### Return type

[**IdentitytoolkitRelyingpartySignOutUserResponse**](IdentitytoolkitRelyingpartySignOutUserResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartySignupNewUser"></a>
# **identitytoolkitRelyingpartySignupNewUser**
> SignupNewUserResponse identitytoolkitRelyingpartySignupNewUser(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartySignupNewUserRequest)



Signup new user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartySignupNewUserRequest identitytoolkitRelyingpartySignupNewUserRequest = new IdentitytoolkitRelyingpartySignupNewUserRequest(); // IdentitytoolkitRelyingpartySignupNewUserRequest | 
    try {
      SignupNewUserResponse result = apiInstance.identitytoolkitRelyingpartySignupNewUser(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartySignupNewUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartySignupNewUser");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartySignupNewUserRequest** | [**IdentitytoolkitRelyingpartySignupNewUserRequest**](IdentitytoolkitRelyingpartySignupNewUserRequest.md)|  | [optional] |

### Return type

[**SignupNewUserResponse**](SignupNewUserResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyUploadAccount"></a>
# **identitytoolkitRelyingpartyUploadAccount**
> UploadAccountResponse identitytoolkitRelyingpartyUploadAccount(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyUploadAccountRequest)



Batch upload existing user accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartyUploadAccountRequest identitytoolkitRelyingpartyUploadAccountRequest = new IdentitytoolkitRelyingpartyUploadAccountRequest(); // IdentitytoolkitRelyingpartyUploadAccountRequest | 
    try {
      UploadAccountResponse result = apiInstance.identitytoolkitRelyingpartyUploadAccount(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyUploadAccountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyUploadAccount");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartyUploadAccountRequest** | [**IdentitytoolkitRelyingpartyUploadAccountRequest**](IdentitytoolkitRelyingpartyUploadAccountRequest.md)|  | [optional] |

### Return type

[**UploadAccountResponse**](UploadAccountResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyVerifyAssertion"></a>
# **identitytoolkitRelyingpartyVerifyAssertion**
> VerifyAssertionResponse identitytoolkitRelyingpartyVerifyAssertion(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyVerifyAssertionRequest)



Verifies the assertion returned by the IdP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartyVerifyAssertionRequest identitytoolkitRelyingpartyVerifyAssertionRequest = new IdentitytoolkitRelyingpartyVerifyAssertionRequest(); // IdentitytoolkitRelyingpartyVerifyAssertionRequest | 
    try {
      VerifyAssertionResponse result = apiInstance.identitytoolkitRelyingpartyVerifyAssertion(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyVerifyAssertionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyVerifyAssertion");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartyVerifyAssertionRequest** | [**IdentitytoolkitRelyingpartyVerifyAssertionRequest**](IdentitytoolkitRelyingpartyVerifyAssertionRequest.md)|  | [optional] |

### Return type

[**VerifyAssertionResponse**](VerifyAssertionResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyVerifyCustomToken"></a>
# **identitytoolkitRelyingpartyVerifyCustomToken**
> VerifyCustomTokenResponse identitytoolkitRelyingpartyVerifyCustomToken(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyVerifyCustomTokenRequest)



Verifies the developer asserted ID token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartyVerifyCustomTokenRequest identitytoolkitRelyingpartyVerifyCustomTokenRequest = new IdentitytoolkitRelyingpartyVerifyCustomTokenRequest(); // IdentitytoolkitRelyingpartyVerifyCustomTokenRequest | 
    try {
      VerifyCustomTokenResponse result = apiInstance.identitytoolkitRelyingpartyVerifyCustomToken(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyVerifyCustomTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyVerifyCustomToken");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartyVerifyCustomTokenRequest** | [**IdentitytoolkitRelyingpartyVerifyCustomTokenRequest**](IdentitytoolkitRelyingpartyVerifyCustomTokenRequest.md)|  | [optional] |

### Return type

[**VerifyCustomTokenResponse**](VerifyCustomTokenResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyVerifyPassword"></a>
# **identitytoolkitRelyingpartyVerifyPassword**
> VerifyPasswordResponse identitytoolkitRelyingpartyVerifyPassword(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyVerifyPasswordRequest)



Verifies the user entered password.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartyVerifyPasswordRequest identitytoolkitRelyingpartyVerifyPasswordRequest = new IdentitytoolkitRelyingpartyVerifyPasswordRequest(); // IdentitytoolkitRelyingpartyVerifyPasswordRequest | 
    try {
      VerifyPasswordResponse result = apiInstance.identitytoolkitRelyingpartyVerifyPassword(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyVerifyPasswordRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyVerifyPassword");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartyVerifyPasswordRequest** | [**IdentitytoolkitRelyingpartyVerifyPasswordRequest**](IdentitytoolkitRelyingpartyVerifyPasswordRequest.md)|  | [optional] |

### Return type

[**VerifyPasswordResponse**](VerifyPasswordResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="identitytoolkitRelyingpartyVerifyPhoneNumber"></a>
# **identitytoolkitRelyingpartyVerifyPhoneNumber**
> IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse identitytoolkitRelyingpartyVerifyPhoneNumber(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyVerifyPhoneNumberRequest)



Verifies ownership of a phone number and creates/updates the user account accordingly.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelyingpartyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/identitytoolkit/v3/relyingparty");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RelyingpartyApi apiInstance = new RelyingpartyApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest identitytoolkitRelyingpartyVerifyPhoneNumberRequest = new IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest(); // IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest | 
    try {
      IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse result = apiInstance.identitytoolkitRelyingpartyVerifyPhoneNumber(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, identitytoolkitRelyingpartyVerifyPhoneNumberRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelyingpartyApi#identitytoolkitRelyingpartyVerifyPhoneNumber");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **identitytoolkitRelyingpartyVerifyPhoneNumberRequest** | [**IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest**](IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest.md)|  | [optional] |

### Return type

[**IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse**](IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

