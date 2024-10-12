# RubrikRestApi.UserApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generateTotpSecret**](UserApi.md#generateTotpSecret) | **POST** /user/{id}/totp/new_secret | Generate a TOTP secret key for the given user
[**getTotpStatus**](UserApi.md#getTotpStatus) | **GET** /user/{id}/totp/status | Get the TOTP status for the given user
[**getUserAccountLockoutSettings**](UserApi.md#getUserAccountLockoutSettings) | **GET** /user/lockout | Get the local user account lockout settings
[**manageUserAccountLockoutSettings**](UserApi.md#manageUserAccountLockoutSettings) | **PATCH** /user/lockout | Update the local user account lockout settings
[**resetTotp**](UserApi.md#resetTotp) | **DELETE** /user/{id}/totp/config | Reset the TOTP for the given user
[**setupTotp**](UserApi.md#setupTotp) | **PUT** /user/{id}/totp/config | Configure the TOTP secret for the given user
[**unlockUser**](UserApi.md#unlockUser) | **POST** /user/{id}/unlock | Unlock a user account



## generateTotpSecret

> TotpSecret generateTotpSecret(id)

Generate a TOTP secret key for the given user

Use this endpoint to generate the time-based one time password (TOTP) secret key for a specified user account. The secret is a key value encoded in Base32 and includes a URI for generating a scannable QR code. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserApi();
let id = "id_example"; // String | The user account object ID.
apiInstance.generateTotpSecret(id, (error, data, response) => {
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
 **id** | **String**| The user account object ID. | 

### Return type

[**TotpSecret**](TotpSecret.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTotpStatus

> TotpStatus getTotpStatus(id)

Get the TOTP status for the given user

Get the time-based one time password (TOTP) status for a specified user account. The TOTP status specifies whether that account has TOTP enabled and whether TOTP is being enforced for that account. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserApi();
let id = "id_example"; // String | The user account object ID.
apiInstance.getTotpStatus(id, (error, data, response) => {
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
 **id** | **String**| The user account object ID. | 

### Return type

[**TotpStatus**](TotpStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserAccountLockoutSettings

> LocalUserAccountLockoutStatus getUserAccountLockoutSettings()

Get the local user account lockout settings

Get the local user account lockout settings which are used to configure whether user accounts will be locked on failed logins, when they will be locked and the duration for which they will stay locked. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserApi();
apiInstance.getUserAccountLockoutSettings((error, data, response) => {
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

[**LocalUserAccountLockoutStatus**](LocalUserAccountLockoutStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## manageUserAccountLockoutSettings

> LocalUserAccountLockoutStatus manageUserAccountLockoutSettings(localUserAccountLockoutConfig)

Update the local user account lockout settings

Update the local user account lockout settings which are used to configure whether user accounts will be locked on failed logins, when they will be locked and the duration for which they will stay locked. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserApi();
let localUserAccountLockoutConfig = new RubrikRestApi.LocalUserAccountLockoutConfig(); // LocalUserAccountLockoutConfig | Update the local user account lockout settings.
apiInstance.manageUserAccountLockoutSettings(localUserAccountLockoutConfig, (error, data, response) => {
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
 **localUserAccountLockoutConfig** | [**LocalUserAccountLockoutConfig**](LocalUserAccountLockoutConfig.md)| Update the local user account lockout settings. | 

### Return type

[**LocalUserAccountLockoutStatus**](LocalUserAccountLockoutStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resetTotp

> resetTotp(id)

Reset the TOTP for the given user

Reset the TOTP settings to the default disabled state for the specified user account. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserApi();
let id = "id_example"; // String | The user account object ID.
apiInstance.resetTotp(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The user account object ID. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setupTotp

> setupTotp(id, totpConfigUpdateRequest)

Configure the TOTP secret for the given user

Use this endpoint to configure the time-based one time password (TOTP) secret for a specified user account. The endpoint replaces an existing secret with the new one. The Rubrik cluster checks the secret against a one time password (OTP) to ensure validity. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserApi();
let id = "id_example"; // String | The user account object ID.
let totpConfigUpdateRequest = new RubrikRestApi.TotpConfigUpdateRequest(); // TotpConfigUpdateRequest | The time-based one time password (TOTP) configuration.
apiInstance.setupTotp(id, totpConfigUpdateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The user account object ID. | 
 **totpConfigUpdateRequest** | [**TotpConfigUpdateRequest**](TotpConfigUpdateRequest.md)| The time-based one time password (TOTP) configuration. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## unlockUser

> unlockUser(id)

Unlock a user account

Unlock a user account that has been locked because of too many failed login attempts.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserApi();
let id = "id_example"; // String | The ID of the user account that has been locked.
apiInstance.unlockUser(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the user account that has been locked. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

