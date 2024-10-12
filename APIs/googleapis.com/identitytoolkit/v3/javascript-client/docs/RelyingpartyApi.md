# GoogleIdentityToolkitApi.RelyingpartyApi

All URIs are relative to *https://www.googleapis.com/identitytoolkit/v3/relyingparty*

Method | HTTP request | Description
------------- | ------------- | -------------
[**identitytoolkitRelyingpartyCreateAuthUri**](RelyingpartyApi.md#identitytoolkitRelyingpartyCreateAuthUri) | **POST** /createAuthUri | 
[**identitytoolkitRelyingpartyDeleteAccount**](RelyingpartyApi.md#identitytoolkitRelyingpartyDeleteAccount) | **POST** /deleteAccount | 
[**identitytoolkitRelyingpartyDownloadAccount**](RelyingpartyApi.md#identitytoolkitRelyingpartyDownloadAccount) | **POST** /downloadAccount | 
[**identitytoolkitRelyingpartyEmailLinkSignin**](RelyingpartyApi.md#identitytoolkitRelyingpartyEmailLinkSignin) | **POST** /emailLinkSignin | 
[**identitytoolkitRelyingpartyGetAccountInfo**](RelyingpartyApi.md#identitytoolkitRelyingpartyGetAccountInfo) | **POST** /getAccountInfo | 
[**identitytoolkitRelyingpartyGetOobConfirmationCode**](RelyingpartyApi.md#identitytoolkitRelyingpartyGetOobConfirmationCode) | **POST** /getOobConfirmationCode | 
[**identitytoolkitRelyingpartyGetProjectConfig**](RelyingpartyApi.md#identitytoolkitRelyingpartyGetProjectConfig) | **GET** /getProjectConfig | 
[**identitytoolkitRelyingpartyGetPublicKeys**](RelyingpartyApi.md#identitytoolkitRelyingpartyGetPublicKeys) | **GET** /publicKeys | 
[**identitytoolkitRelyingpartyGetRecaptchaParam**](RelyingpartyApi.md#identitytoolkitRelyingpartyGetRecaptchaParam) | **GET** /getRecaptchaParam | 
[**identitytoolkitRelyingpartyResetPassword**](RelyingpartyApi.md#identitytoolkitRelyingpartyResetPassword) | **POST** /resetPassword | 
[**identitytoolkitRelyingpartySendVerificationCode**](RelyingpartyApi.md#identitytoolkitRelyingpartySendVerificationCode) | **POST** /sendVerificationCode | 
[**identitytoolkitRelyingpartySetAccountInfo**](RelyingpartyApi.md#identitytoolkitRelyingpartySetAccountInfo) | **POST** /setAccountInfo | 
[**identitytoolkitRelyingpartySetProjectConfig**](RelyingpartyApi.md#identitytoolkitRelyingpartySetProjectConfig) | **POST** /setProjectConfig | 
[**identitytoolkitRelyingpartySignOutUser**](RelyingpartyApi.md#identitytoolkitRelyingpartySignOutUser) | **POST** /signOutUser | 
[**identitytoolkitRelyingpartySignupNewUser**](RelyingpartyApi.md#identitytoolkitRelyingpartySignupNewUser) | **POST** /signupNewUser | 
[**identitytoolkitRelyingpartyUploadAccount**](RelyingpartyApi.md#identitytoolkitRelyingpartyUploadAccount) | **POST** /uploadAccount | 
[**identitytoolkitRelyingpartyVerifyAssertion**](RelyingpartyApi.md#identitytoolkitRelyingpartyVerifyAssertion) | **POST** /verifyAssertion | 
[**identitytoolkitRelyingpartyVerifyCustomToken**](RelyingpartyApi.md#identitytoolkitRelyingpartyVerifyCustomToken) | **POST** /verifyCustomToken | 
[**identitytoolkitRelyingpartyVerifyPassword**](RelyingpartyApi.md#identitytoolkitRelyingpartyVerifyPassword) | **POST** /verifyPassword | 
[**identitytoolkitRelyingpartyVerifyPhoneNumber**](RelyingpartyApi.md#identitytoolkitRelyingpartyVerifyPhoneNumber) | **POST** /verifyPhoneNumber | 



## identitytoolkitRelyingpartyCreateAuthUri

> CreateAuthUriResponse identitytoolkitRelyingpartyCreateAuthUri(opts)



Creates the URI used by the IdP to authenticate the user.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartyCreateAuthUriRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyCreateAuthUriRequest() // IdentitytoolkitRelyingpartyCreateAuthUriRequest | 
};
apiInstance.identitytoolkitRelyingpartyCreateAuthUri(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartyCreateAuthUriRequest** | [**IdentitytoolkitRelyingpartyCreateAuthUriRequest**](IdentitytoolkitRelyingpartyCreateAuthUriRequest.md)|  | [optional] 

### Return type

[**CreateAuthUriResponse**](CreateAuthUriResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartyDeleteAccount

> DeleteAccountResponse identitytoolkitRelyingpartyDeleteAccount(opts)



Delete user account.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartyDeleteAccountRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyDeleteAccountRequest() // IdentitytoolkitRelyingpartyDeleteAccountRequest | 
};
apiInstance.identitytoolkitRelyingpartyDeleteAccount(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartyDeleteAccountRequest** | [**IdentitytoolkitRelyingpartyDeleteAccountRequest**](IdentitytoolkitRelyingpartyDeleteAccountRequest.md)|  | [optional] 

### Return type

[**DeleteAccountResponse**](DeleteAccountResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartyDownloadAccount

> DownloadAccountResponse identitytoolkitRelyingpartyDownloadAccount(opts)



Batch download user accounts.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartyDownloadAccountRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyDownloadAccountRequest() // IdentitytoolkitRelyingpartyDownloadAccountRequest | 
};
apiInstance.identitytoolkitRelyingpartyDownloadAccount(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartyDownloadAccountRequest** | [**IdentitytoolkitRelyingpartyDownloadAccountRequest**](IdentitytoolkitRelyingpartyDownloadAccountRequest.md)|  | [optional] 

### Return type

[**DownloadAccountResponse**](DownloadAccountResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartyEmailLinkSignin

> EmailLinkSigninResponse identitytoolkitRelyingpartyEmailLinkSignin(opts)



Reset password for a user.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartyEmailLinkSigninRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyEmailLinkSigninRequest() // IdentitytoolkitRelyingpartyEmailLinkSigninRequest | 
};
apiInstance.identitytoolkitRelyingpartyEmailLinkSignin(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartyEmailLinkSigninRequest** | [**IdentitytoolkitRelyingpartyEmailLinkSigninRequest**](IdentitytoolkitRelyingpartyEmailLinkSigninRequest.md)|  | [optional] 

### Return type

[**EmailLinkSigninResponse**](EmailLinkSigninResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartyGetAccountInfo

> GetAccountInfoResponse identitytoolkitRelyingpartyGetAccountInfo(opts)



Returns the account info.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartyGetAccountInfoRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyGetAccountInfoRequest() // IdentitytoolkitRelyingpartyGetAccountInfoRequest | 
};
apiInstance.identitytoolkitRelyingpartyGetAccountInfo(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartyGetAccountInfoRequest** | [**IdentitytoolkitRelyingpartyGetAccountInfoRequest**](IdentitytoolkitRelyingpartyGetAccountInfoRequest.md)|  | [optional] 

### Return type

[**GetAccountInfoResponse**](GetAccountInfoResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartyGetOobConfirmationCode

> GetOobConfirmationCodeResponse identitytoolkitRelyingpartyGetOobConfirmationCode(opts)



Get a code for user action confirmation.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'relyingparty': new GoogleIdentityToolkitApi.Relyingparty() // Relyingparty | 
};
apiInstance.identitytoolkitRelyingpartyGetOobConfirmationCode(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **relyingparty** | [**Relyingparty**](Relyingparty.md)|  | [optional] 

### Return type

[**GetOobConfirmationCodeResponse**](GetOobConfirmationCodeResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartyGetProjectConfig

> IdentitytoolkitRelyingpartyGetProjectConfigResponse identitytoolkitRelyingpartyGetProjectConfig(opts)



Get project configuration.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'delegatedProjectNumber': "delegatedProjectNumber_example", // String | Delegated GCP project number of the request.
  'projectNumber': "projectNumber_example" // String | GCP project number of the request.
};
apiInstance.identitytoolkitRelyingpartyGetProjectConfig(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **delegatedProjectNumber** | **String**| Delegated GCP project number of the request. | [optional] 
 **projectNumber** | **String**| GCP project number of the request. | [optional] 

### Return type

[**IdentitytoolkitRelyingpartyGetProjectConfigResponse**](IdentitytoolkitRelyingpartyGetProjectConfigResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identitytoolkitRelyingpartyGetPublicKeys

> {String: String} identitytoolkitRelyingpartyGetPublicKeys(opts)



Get token signing public key.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.identitytoolkitRelyingpartyGetPublicKeys(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

**{String: String}**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identitytoolkitRelyingpartyGetRecaptchaParam

> GetRecaptchaParamResponse identitytoolkitRelyingpartyGetRecaptchaParam(opts)



Get recaptcha secure param.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.identitytoolkitRelyingpartyGetRecaptchaParam(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**GetRecaptchaParamResponse**](GetRecaptchaParamResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identitytoolkitRelyingpartyResetPassword

> ResetPasswordResponse identitytoolkitRelyingpartyResetPassword(opts)



Reset password for a user.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartyResetPasswordRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyResetPasswordRequest() // IdentitytoolkitRelyingpartyResetPasswordRequest | 
};
apiInstance.identitytoolkitRelyingpartyResetPassword(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartyResetPasswordRequest** | [**IdentitytoolkitRelyingpartyResetPasswordRequest**](IdentitytoolkitRelyingpartyResetPasswordRequest.md)|  | [optional] 

### Return type

[**ResetPasswordResponse**](ResetPasswordResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartySendVerificationCode

> IdentitytoolkitRelyingpartySendVerificationCodeResponse identitytoolkitRelyingpartySendVerificationCode(opts)



Send SMS verification code.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartySendVerificationCodeRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartySendVerificationCodeRequest() // IdentitytoolkitRelyingpartySendVerificationCodeRequest | 
};
apiInstance.identitytoolkitRelyingpartySendVerificationCode(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartySendVerificationCodeRequest** | [**IdentitytoolkitRelyingpartySendVerificationCodeRequest**](IdentitytoolkitRelyingpartySendVerificationCodeRequest.md)|  | [optional] 

### Return type

[**IdentitytoolkitRelyingpartySendVerificationCodeResponse**](IdentitytoolkitRelyingpartySendVerificationCodeResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartySetAccountInfo

> SetAccountInfoResponse identitytoolkitRelyingpartySetAccountInfo(opts)



Set account info for a user.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartySetAccountInfoRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartySetAccountInfoRequest() // IdentitytoolkitRelyingpartySetAccountInfoRequest | 
};
apiInstance.identitytoolkitRelyingpartySetAccountInfo(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartySetAccountInfoRequest** | [**IdentitytoolkitRelyingpartySetAccountInfoRequest**](IdentitytoolkitRelyingpartySetAccountInfoRequest.md)|  | [optional] 

### Return type

[**SetAccountInfoResponse**](SetAccountInfoResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartySetProjectConfig

> IdentitytoolkitRelyingpartySetProjectConfigResponse identitytoolkitRelyingpartySetProjectConfig(opts)



Set project configuration.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartySetProjectConfigRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartySetProjectConfigRequest() // IdentitytoolkitRelyingpartySetProjectConfigRequest | 
};
apiInstance.identitytoolkitRelyingpartySetProjectConfig(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartySetProjectConfigRequest** | [**IdentitytoolkitRelyingpartySetProjectConfigRequest**](IdentitytoolkitRelyingpartySetProjectConfigRequest.md)|  | [optional] 

### Return type

[**IdentitytoolkitRelyingpartySetProjectConfigResponse**](IdentitytoolkitRelyingpartySetProjectConfigResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartySignOutUser

> IdentitytoolkitRelyingpartySignOutUserResponse identitytoolkitRelyingpartySignOutUser(opts)



Sign out user.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartySignOutUserRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartySignOutUserRequest() // IdentitytoolkitRelyingpartySignOutUserRequest | 
};
apiInstance.identitytoolkitRelyingpartySignOutUser(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartySignOutUserRequest** | [**IdentitytoolkitRelyingpartySignOutUserRequest**](IdentitytoolkitRelyingpartySignOutUserRequest.md)|  | [optional] 

### Return type

[**IdentitytoolkitRelyingpartySignOutUserResponse**](IdentitytoolkitRelyingpartySignOutUserResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartySignupNewUser

> SignupNewUserResponse identitytoolkitRelyingpartySignupNewUser(opts)



Signup new user.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartySignupNewUserRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartySignupNewUserRequest() // IdentitytoolkitRelyingpartySignupNewUserRequest | 
};
apiInstance.identitytoolkitRelyingpartySignupNewUser(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartySignupNewUserRequest** | [**IdentitytoolkitRelyingpartySignupNewUserRequest**](IdentitytoolkitRelyingpartySignupNewUserRequest.md)|  | [optional] 

### Return type

[**SignupNewUserResponse**](SignupNewUserResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartyUploadAccount

> UploadAccountResponse identitytoolkitRelyingpartyUploadAccount(opts)



Batch upload existing user accounts.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartyUploadAccountRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyUploadAccountRequest() // IdentitytoolkitRelyingpartyUploadAccountRequest | 
};
apiInstance.identitytoolkitRelyingpartyUploadAccount(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartyUploadAccountRequest** | [**IdentitytoolkitRelyingpartyUploadAccountRequest**](IdentitytoolkitRelyingpartyUploadAccountRequest.md)|  | [optional] 

### Return type

[**UploadAccountResponse**](UploadAccountResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartyVerifyAssertion

> VerifyAssertionResponse identitytoolkitRelyingpartyVerifyAssertion(opts)



Verifies the assertion returned by the IdP.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartyVerifyAssertionRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyVerifyAssertionRequest() // IdentitytoolkitRelyingpartyVerifyAssertionRequest | 
};
apiInstance.identitytoolkitRelyingpartyVerifyAssertion(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartyVerifyAssertionRequest** | [**IdentitytoolkitRelyingpartyVerifyAssertionRequest**](IdentitytoolkitRelyingpartyVerifyAssertionRequest.md)|  | [optional] 

### Return type

[**VerifyAssertionResponse**](VerifyAssertionResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartyVerifyCustomToken

> VerifyCustomTokenResponse identitytoolkitRelyingpartyVerifyCustomToken(opts)



Verifies the developer asserted ID token.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartyVerifyCustomTokenRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyVerifyCustomTokenRequest() // IdentitytoolkitRelyingpartyVerifyCustomTokenRequest | 
};
apiInstance.identitytoolkitRelyingpartyVerifyCustomToken(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartyVerifyCustomTokenRequest** | [**IdentitytoolkitRelyingpartyVerifyCustomTokenRequest**](IdentitytoolkitRelyingpartyVerifyCustomTokenRequest.md)|  | [optional] 

### Return type

[**VerifyCustomTokenResponse**](VerifyCustomTokenResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartyVerifyPassword

> VerifyPasswordResponse identitytoolkitRelyingpartyVerifyPassword(opts)



Verifies the user entered password.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartyVerifyPasswordRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyVerifyPasswordRequest() // IdentitytoolkitRelyingpartyVerifyPasswordRequest | 
};
apiInstance.identitytoolkitRelyingpartyVerifyPassword(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartyVerifyPasswordRequest** | [**IdentitytoolkitRelyingpartyVerifyPasswordRequest**](IdentitytoolkitRelyingpartyVerifyPasswordRequest.md)|  | [optional] 

### Return type

[**VerifyPasswordResponse**](VerifyPasswordResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identitytoolkitRelyingpartyVerifyPhoneNumber

> IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse identitytoolkitRelyingpartyVerifyPhoneNumber(opts)



Verifies ownership of a phone number and creates/updates the user account accordingly.

### Example

```javascript
import GoogleIdentityToolkitApi from 'google_identity_toolkit_api';
let defaultClient = GoogleIdentityToolkitApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleIdentityToolkitApi.RelyingpartyApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'identitytoolkitRelyingpartyVerifyPhoneNumberRequest': new GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest() // IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest | 
};
apiInstance.identitytoolkitRelyingpartyVerifyPhoneNumber(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **identitytoolkitRelyingpartyVerifyPhoneNumberRequest** | [**IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest**](IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest.md)|  | [optional] 

### Return type

[**IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse**](IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

