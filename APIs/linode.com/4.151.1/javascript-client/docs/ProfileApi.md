# LinodeApi.ProfileApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addSSHKey**](ProfileApi.md#addSSHKey) | **POST** /profile/sshkeys | SSH Key Add
[**createPersonalAccessToken**](ProfileApi.md#createPersonalAccessToken) | **POST** /profile/tokens | Personal Access Token Create
[**deletePersonalAccessToken**](ProfileApi.md#deletePersonalAccessToken) | **DELETE** /profile/tokens/{tokenId} | Personal Access Token Revoke
[**deleteProfileApp**](ProfileApi.md#deleteProfileApp) | **DELETE** /profile/apps/{appId} | App Access Revoke
[**deleteProfilePhoneNumber**](ProfileApi.md#deleteProfilePhoneNumber) | **DELETE** /profile/phone-number | Phone Number Delete
[**deleteSSHKey**](ProfileApi.md#deleteSSHKey) | **DELETE** /profile/sshkeys/{sshKeyId} | SSH Key Delete
[**getDevices**](ProfileApi.md#getDevices) | **GET** /profile/devices | Trusted Devices List
[**getPersonalAccessToken**](ProfileApi.md#getPersonalAccessToken) | **GET** /profile/tokens/{tokenId} | Personal Access Token View
[**getPersonalAccessTokens**](ProfileApi.md#getPersonalAccessTokens) | **GET** /profile/tokens | Personal Access Tokens List
[**getProfile**](ProfileApi.md#getProfile) | **GET** /profile | Profile View
[**getProfileApp**](ProfileApi.md#getProfileApp) | **GET** /profile/apps/{appId} | Authorized App View
[**getProfileApps**](ProfileApi.md#getProfileApps) | **GET** /profile/apps | Authorized Apps List
[**getProfileGrants**](ProfileApi.md#getProfileGrants) | **GET** /profile/grants | Grants List
[**getProfileLogin**](ProfileApi.md#getProfileLogin) | **GET** /profile/logins/{loginId} | Login View
[**getProfileLogins**](ProfileApi.md#getProfileLogins) | **GET** /profile/logins | Logins List
[**getSSHKey**](ProfileApi.md#getSSHKey) | **GET** /profile/sshkeys/{sshKeyId} | SSH Key View
[**getSSHKeys**](ProfileApi.md#getSSHKeys) | **GET** /profile/sshkeys | SSH Keys List
[**getSecurityQuestions**](ProfileApi.md#getSecurityQuestions) | **GET** /profile/security-questions | Security Questions List
[**getTrustedDevice**](ProfileApi.md#getTrustedDevice) | **GET** /profile/devices/{deviceId} | Trusted Device View
[**getUserPreferences**](ProfileApi.md#getUserPreferences) | **GET** /profile/preferences | User Preferences View
[**postProfilePhoneNumber**](ProfileApi.md#postProfilePhoneNumber) | **POST** /profile/phone-number | Phone Number Verification Code Send
[**postProfilePhoneNumberVerify**](ProfileApi.md#postProfilePhoneNumberVerify) | **POST** /profile/phone-number/verify | Phone Number Verify
[**postSecurityQuestions**](ProfileApi.md#postSecurityQuestions) | **POST** /profile/security-questions | Security Questions Answer
[**revokeTrustedDevice**](ProfileApi.md#revokeTrustedDevice) | **DELETE** /profile/devices/{deviceId} | Trusted Device Revoke
[**tfaConfirm**](ProfileApi.md#tfaConfirm) | **POST** /profile/tfa-enable-confirm | Two Factor Authentication Confirm/Enable
[**tfaDisable**](ProfileApi.md#tfaDisable) | **POST** /profile/tfa-disable | Two Factor Authentication Disable
[**tfaEnable**](ProfileApi.md#tfaEnable) | **POST** /profile/tfa-enable | Two Factor Secret Create
[**updatePersonalAccessToken**](ProfileApi.md#updatePersonalAccessToken) | **PUT** /profile/tokens/{tokenId} | Personal Access Token Update
[**updateProfile**](ProfileApi.md#updateProfile) | **PUT** /profile | Profile Update
[**updateSSHKey**](ProfileApi.md#updateSSHKey) | **PUT** /profile/sshkeys/{sshKeyId} | SSH Key Update
[**updateUserPreferences**](ProfileApi.md#updateUserPreferences) | **PUT** /profile/preferences | User Preferences Update



## addSSHKey

> SSHKey addSSHKey(opts)

SSH Key Add

Adds an SSH Key to your Account profile. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let opts = {
  'sSHKey': new LinodeApi.SSHKey() // SSHKey | Add SSH Key
};
apiInstance.addSSHKey(opts, (error, data, response) => {
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
 **sSHKey** | [**SSHKey**](SSHKey.md)| Add SSH Key | [optional] 

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPersonalAccessToken

> PersonalAccessToken createPersonalAccessToken(createPersonalAccessTokenRequest)

Personal Access Token Create

Creates a Personal Access Token for your User. The raw token will be returned in the response, but will never be returned again afterward so be sure to take note of it. You may create a token with _at most_ the scopes of your current token. The created token will be able to access your Account until the given expiry, or until it is revoked. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let createPersonalAccessTokenRequest = new LinodeApi.CreatePersonalAccessTokenRequest(); // CreatePersonalAccessTokenRequest | Information about the requested token.
apiInstance.createPersonalAccessToken(createPersonalAccessTokenRequest, (error, data, response) => {
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
 **createPersonalAccessTokenRequest** | [**CreatePersonalAccessTokenRequest**](CreatePersonalAccessTokenRequest.md)| Information about the requested token. | 

### Return type

[**PersonalAccessToken**](PersonalAccessToken.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deletePersonalAccessToken

> Object deletePersonalAccessToken(tokenId)

Personal Access Token Revoke

Revokes a Personal Access Token. The token will be invalidated immediately, and requests using that token will fail with a 401. It is possible to revoke access to the token making the request to revoke a token, but keep in mind that doing so could lose you access to the api and require you to create a new token through some other means. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let tokenId = 56; // Number | The ID of the token to access.
apiInstance.deletePersonalAccessToken(tokenId, (error, data, response) => {
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
 **tokenId** | **Number**| The ID of the token to access. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteProfileApp

> Object deleteProfileApp(appId)

App Access Revoke

Expires this app token. This token may no longer be used to access your Account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let appId = 56; // Number | The authorized app ID to manage.
apiInstance.deleteProfileApp(appId, (error, data, response) => {
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
 **appId** | **Number**| The authorized app ID to manage. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteProfilePhoneNumber

> Object deleteProfilePhoneNumber()

Phone Number Delete

Delete the verified phone number for the User making this request.  Use this command to opt out of SMS messages for the requesting User after a phone number has been verified with the **Phone Number Verify** ([POST /profile/phone-number/verify](/docs/api/profile/#phone-number-verify)) command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
apiInstance.deleteProfilePhoneNumber((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## deleteSSHKey

> Object deleteSSHKey(sshKeyId)

SSH Key Delete

Deletes an SSH Key you have access to.  **Note:** deleting an SSH Key will *not* remove it from any Linode or Disk that was deployed with &#x60;authorized_keys&#x60;. In those cases, the keys must be manually deleted on the Linode or Disk. This endpoint will only delete the key&#39;s association from your Profile. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let sshKeyId = 56; // Number | The ID of the SSHKey
apiInstance.deleteSSHKey(sshKeyId, (error, data, response) => {
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
 **sshKeyId** | **Number**| The ID of the SSHKey | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDevices

> GetDevices200Response getDevices()

Trusted Devices List

Returns a paginated list of active TrustedDevices for your User. Browsers with an active Remember Me Session are logged into your account until the session expires or is revoked. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
apiInstance.getDevices((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getPersonalAccessToken

> PersonalAccessToken getPersonalAccessToken(tokenId)

Personal Access Token View

Returns a single Personal Access Token. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let tokenId = 56; // Number | The ID of the token to access.
apiInstance.getPersonalAccessToken(tokenId, (error, data, response) => {
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
 **tokenId** | **Number**| The ID of the token to access. | 

### Return type

[**PersonalAccessToken**](PersonalAccessToken.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalAccessTokens

> GetPersonalAccessTokens200Response getPersonalAccessTokens()

Personal Access Tokens List

Returns a paginated list of Personal Access Tokens currently active for your User. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
apiInstance.getPersonalAccessTokens((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getProfile

> Profile getProfile()

Profile View

Returns information about the current User. This can be used to see who is acting in applications where more than one token is managed. For example, in third-party OAuth applications.  This endpoint is always accessible, no matter what OAuth scopes the acting token has. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
apiInstance.getProfile((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getProfileApp

> AuthorizedApp getProfileApp(appId)

Authorized App View

Returns information about a single app you&#39;ve authorized to access your Account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let appId = 56; // Number | The authorized app ID to manage.
apiInstance.getProfileApp(appId, (error, data, response) => {
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
 **appId** | **Number**| The authorized app ID to manage. | 

### Return type

[**AuthorizedApp**](AuthorizedApp.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProfileApps

> GetProfileApps200Response getProfileApps(opts)

Authorized Apps List

This is a collection of OAuth apps that you&#39;ve given access to your Account, and includes the level of access granted. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getProfileApps(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetProfileApps200Response**](GetProfileApps200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProfileGrants

> GrantsResponse getProfileGrants()

Grants List

This returns a GrantsResponse describing what the acting User has been granted access to.  For unrestricted users, this will return a  204 and no body because unrestricted users have access to everything without grants.  This will not return information about entities you do not have access to.  This endpoint is useful when writing third-party OAuth applications to see what options you should present to the acting User.  For example, if they do not have &#x60;global.add_linodes&#x60;, you might not display a button to deploy a new Linode.  Any client may access this endpoint; no OAuth scopes are required. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
apiInstance.getProfileGrants((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getProfileLogin

> Login getProfileLogin(loginId)

Login View

Returns a login object displaying information about a successful account login from this user. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let loginId = 56; // Number | The ID of the login object to access.
apiInstance.getProfileLogin(loginId, (error, data, response) => {
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
 **loginId** | **Number**| The ID of the login object to access. | 

### Return type

[**Login**](Login.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProfileLogins

> GetAccountLogins200Response getProfileLogins()

Logins List

Returns a collection of successful account logins from this user during the last 90 days. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
apiInstance.getProfileLogins((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getSSHKey

> SSHKey getSSHKey(sshKeyId)

SSH Key View

Returns a single SSH Key object identified by &#x60;id&#x60; that you have access to view. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let sshKeyId = 56; // Number | The ID of the SSHKey
apiInstance.getSSHKey(sshKeyId, (error, data, response) => {
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
 **sshKeyId** | **Number**| The ID of the SSHKey | 

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSSHKeys

> GetSSHKeys200Response getSSHKeys(opts)

SSH Keys List

Returns a collection of SSH Keys you&#39;ve added to your Profile. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getSSHKeys(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetSSHKeys200Response**](GetSSHKeys200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSecurityQuestions

> SecurityQuestionsGet getSecurityQuestions()

Security Questions List

Returns a collection of security questions and their responses, if any, for your User Profile. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
apiInstance.getSecurityQuestions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getTrustedDevice

> TrustedDevice getTrustedDevice(deviceId)

Trusted Device View

Returns a single active TrustedDevice for your User. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let deviceId = 56; // Number | The ID of the TrustedDevice
apiInstance.getTrustedDevice(deviceId, (error, data, response) => {
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
 **deviceId** | **Number**| The ID of the TrustedDevice | 

### Return type

[**TrustedDevice**](TrustedDevice.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserPreferences

> Object getUserPreferences()

User Preferences View

View a list of user preferences tied to the OAuth client that generated the token making the request. The user preferences endpoints allow consumers of the API to store arbitrary JSON data, such as a user&#39;s font size preference or preferred display name. User preferences are available for each OAuth client registered to your account, and as such an account can have multiple user preferences. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
apiInstance.getUserPreferences((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## postProfilePhoneNumber

> Object postProfilePhoneNumber(opts)

Phone Number Verification Code Send

Send a one-time verification code via SMS message to the submitted phone number. Providing your phone number helps ensure you can securely access your Account in case other ways to connect are lost. Your phone number is only used to verify your identity by sending an SMS message. Standard carrier messaging fees may apply.  * By accessing this command you are opting in to receive SMS messages. You can opt out of SMS messages by using the **Phone Number Delete** ([DELETE /profile/phone-number](/docs/api/profile/#phone-number-delete)) command after your phone number is verified.  * Verification codes are valid for 10 minutes after they are sent.  * Subsequent requests made prior to code expiration result in sending the same code.  Once a verification code is received, verify your phone number with the **Phone Number Verify** ([POST /profile/phone-number/verify](/docs/api/profile/#phone-number-verify)) command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let opts = {
  'postProfilePhoneNumberRequest': new LinodeApi.PostProfilePhoneNumberRequest() // PostProfilePhoneNumberRequest | Enter a phone number and country code for verification.
};
apiInstance.postProfilePhoneNumber(opts, (error, data, response) => {
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
 **postProfilePhoneNumberRequest** | [**PostProfilePhoneNumberRequest**](PostProfilePhoneNumberRequest.md)| Enter a phone number and country code for verification. | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postProfilePhoneNumberVerify

> Object postProfilePhoneNumberVerify(opts)

Phone Number Verify

Verify a phone number by confirming the one-time code received via SMS message after accessing the **Phone Verification Code Send** ([POST /profile/phone-number](/docs/api/profile/#phone-number-verification-code-send)) command.  * Verification codes are valid for 10 minutes after they are sent.  * Only the same User that made the verification code request can use that code with this command.  Once completed, the verified phone number is assigned to the User making the request. To change the verified phone number for a User, first use the **Phone Number Delete** ([DELETE /profile/phone-number](/docs/api/profile/#phone-number-delete)) command, then begin the verification process again with the **Phone Verification Code Send** ([POST /profile/phone-number](/docs/api/profile/#phone-number-verification-code-send)) command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let opts = {
  'postProfilePhoneNumberVerifyRequest': new LinodeApi.PostProfilePhoneNumberVerifyRequest() // PostProfilePhoneNumberVerifyRequest | Enter a phone verification code for confirmation.
};
apiInstance.postProfilePhoneNumberVerify(opts, (error, data, response) => {
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
 **postProfilePhoneNumberVerifyRequest** | [**PostProfilePhoneNumberVerifyRequest**](PostProfilePhoneNumberVerifyRequest.md)| Enter a phone verification code for confirmation. | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postSecurityQuestions

> SecurityQuestionsPost postSecurityQuestions(opts)

Security Questions Answer

Adds security question responses for your User.  Requires exactly three unique questions.  Previous responses are overwritten if answered or reset to &#x60;null&#x60; if unanswered.  **Note**: Security questions must be answered for your User prior to accessing the **Two Factor Secret Create** ([POST /profile/tfa-enable](/docs/api/profile/#two-factor-secret-create)) command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let opts = {
  'securityQuestionsPost': new LinodeApi.SecurityQuestionsPost() // SecurityQuestionsPost | Answer Security Questions
};
apiInstance.postSecurityQuestions(opts, (error, data, response) => {
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
 **securityQuestionsPost** | [**SecurityQuestionsPost**](SecurityQuestionsPost.md)| Answer Security Questions | [optional] 

### Return type

[**SecurityQuestionsPost**](SecurityQuestionsPost.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## revokeTrustedDevice

> Object revokeTrustedDevice(deviceId)

Trusted Device Revoke

Revoke an active TrustedDevice for your User.  Once a TrustedDevice is revoked, this device will have to log in again before accessing your Linode account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let deviceId = 56; // Number | The ID of the TrustedDevice
apiInstance.revokeTrustedDevice(deviceId, (error, data, response) => {
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
 **deviceId** | **Number**| The ID of the TrustedDevice | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tfaConfirm

> TfaConfirm200Response tfaConfirm(tfaConfirmRequest)

Two Factor Authentication Confirm/Enable

Confirms that you can successfully generate Two Factor codes and enables TFA on your Account. Once this is complete, login attempts from untrusted computers will be required to provide a Two Factor code before they are successful. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let tfaConfirmRequest = new LinodeApi.TfaConfirmRequest(); // TfaConfirmRequest | The Two Factor code you generated with your Two Factor secret.
apiInstance.tfaConfirm(tfaConfirmRequest, (error, data, response) => {
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
 **tfaConfirmRequest** | [**TfaConfirmRequest**](TfaConfirmRequest.md)| The Two Factor code you generated with your Two Factor secret. | 

### Return type

[**TfaConfirm200Response**](TfaConfirm200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tfaDisable

> Object tfaDisable()

Two Factor Authentication Disable

Disables Two Factor Authentication for your User. Once successful, login attempts from untrusted computers will only require a password before being successful. This is less secure, and is discouraged. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
apiInstance.tfaDisable((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## tfaEnable

> TfaEnable200Response tfaEnable()

Two Factor Secret Create

Generates a Two Factor secret for your User. To enable TFA for your User, enter the secret obtained from this command with the **Two Factor Authentication Confirm/Enable** ([POST /profile/tfa-enable-confirm](/docs/api/profile/#two-factor-authentication-confirmenable)) command. Once enabled, logins from untrusted computers are required to provide a TFA code before they are successful.  **Note**: Before you can enable TFA, security questions must be answered for your User by accessing the **Security Questions Answer** ([POST /profile/security-questions](/docs/api/profile/#security-questions-answer)) command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
apiInstance.tfaEnable((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## updatePersonalAccessToken

> PersonalAccessToken updatePersonalAccessToken(tokenId, personalAccessToken)

Personal Access Token Update

Updates a Personal Access Token. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let tokenId = 56; // Number | The ID of the token to access.
let personalAccessToken = new LinodeApi.PersonalAccessToken(); // PersonalAccessToken | The fields to update.
apiInstance.updatePersonalAccessToken(tokenId, personalAccessToken, (error, data, response) => {
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
 **tokenId** | **Number**| The ID of the token to access. | 
 **personalAccessToken** | [**PersonalAccessToken**](PersonalAccessToken.md)| The fields to update. | 

### Return type

[**PersonalAccessToken**](PersonalAccessToken.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProfile

> Profile updateProfile(profile)

Profile Update

Update information in your Profile.  This endpoint requires the \&quot;account:read_write\&quot; OAuth Scope. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let profile = new LinodeApi.Profile(); // Profile | The fields to update.
apiInstance.updateProfile(profile, (error, data, response) => {
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
 **profile** | [**Profile**](Profile.md)| The fields to update. | 

### Return type

[**Profile**](Profile.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSSHKey

> SSHKey updateSSHKey(sshKeyId, updateSSHKeyRequest)

SSH Key Update

Updates an SSH Key that you have permission to &#x60;read_write&#x60;.  Only SSH key labels can be updated. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let sshKeyId = 56; // Number | The ID of the SSHKey
let updateSSHKeyRequest = new LinodeApi.UpdateSSHKeyRequest(); // UpdateSSHKeyRequest | The fields to update. 
apiInstance.updateSSHKey(sshKeyId, updateSSHKeyRequest, (error, data, response) => {
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
 **sshKeyId** | **Number**| The ID of the SSHKey | 
 **updateSSHKeyRequest** | [**UpdateSSHKeyRequest**](UpdateSSHKeyRequest.md)| The fields to update.  | 

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUserPreferences

> Object updateUserPreferences(body)

User Preferences Update

Updates a user&#39;s preferences. These preferences are tied to the OAuth client that generated the token making the request. The user preferences endpoints allow consumers of the API to store arbitrary JSON data, such as a user&#39;s font size preference or preferred display name. An account may have multiple preferences. Preferences, and the pertaining request body, may contain any arbitrary JSON data that the user would like to store. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ProfileApi();
let body = {key: null}; // Object | The user preferences to update or store. 
apiInstance.updateUserPreferences(body, (error, data, response) => {
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
 **body** | **Object**| The user preferences to update or store.  | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

