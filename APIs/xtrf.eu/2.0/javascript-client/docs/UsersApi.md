# XtrfHomePortalApi.UsersApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changePassword**](UsersApi.md#changePassword) | **PUT** /users/{userId}/password | Sets user&#39;s password to a new value.
[**getAllNamesWithIds1**](UsersApi.md#getAllNamesWithIds1) | **GET** /users | Returns list of simple users representations
[**getById6**](UsersApi.md#getById6) | **GET** /users/{userId} | Returns user details.
[**getCustomField1**](UsersApi.md#getCustomField1) | **GET** /users/{userId}/customFields/{customFieldKey} | Returns custom field of a given user.
[**getCustomFields4**](UsersApi.md#getCustomFields4) | **GET** /users/{userId}/customFields | Returns custom fields of a given user.
[**getMe**](UsersApi.md#getMe) | **GET** /users/me | Returns currently signed in user details.
[**getTimeZone**](UsersApi.md#getTimeZone) | **GET** /users/me/timeZone | Returns time zone preferred by user currently signed in.
[**update3**](UsersApi.md#update3) | **PUT** /users/{userId} | Updates an existing user.
[**updateCustomField1**](UsersApi.md#updateCustomField1) | **PUT** /users/{userId}/customFields/{customFieldKey} | Updates given custom field of a given user.
[**updateCustomFields2**](UsersApi.md#updateCustomFields2) | **PUT** /users/{userId}/customFields | Updates custom fields of a given user.



## changePassword

> changePassword(userId, opts)

Sets user&#39;s password to a new value.

Sets user&#39;s password to a new value.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.UsersApi();
let userId = 789; // Number | user's internal identifier
let opts = {
  'newPassword': "newPassword_example", // String | new password
  'oldPassword': "oldPassword_example" // String | old password
};
apiInstance.changePassword(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| user&#39;s internal identifier | 
 **newPassword** | **String**| new password | [optional] 
 **oldPassword** | **String**| old password | [optional] 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## getAllNamesWithIds1

> [EntityWithNameDTO] getAllNamesWithIds1()

Returns list of simple users representations

Returns list of simple users representations

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.UsersApi();
apiInstance.getAllNamesWithIds1((error, data, response) => {
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

[**[EntityWithNameDTO]**](EntityWithNameDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getById6

> UserDTO getById6(userId)

Returns user details.

Returns user details.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.UsersApi();
let userId = 789; // Number | user's internal identifier
apiInstance.getById6(userId, (error, data, response) => {
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
 **userId** | **Number**| user&#39;s internal identifier | 

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getCustomField1

> CustomFieldDTO getCustomField1(userId, customFieldKey)

Returns custom field of a given user.

Returns custom field of a given user.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.UsersApi();
let userId = 789; // Number | user's internal identifier
let customFieldKey = "customFieldKey_example"; // String | custom field's key
apiInstance.getCustomField1(userId, customFieldKey, (error, data, response) => {
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
 **userId** | **Number**| user&#39;s internal identifier | 
 **customFieldKey** | **String**| custom field&#39;s key | 

### Return type

[**CustomFieldDTO**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getCustomFields4

> [CustomFieldDTO] getCustomFields4(userId)

Returns custom fields of a given user.

Returns custom fields of a given user.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.UsersApi();
let userId = 789; // Number | user's internal identifier
apiInstance.getCustomFields4(userId, (error, data, response) => {
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
 **userId** | **Number**| user&#39;s internal identifier | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getMe

> UserDTO getMe()

Returns currently signed in user details.

Returns currently signed in user details.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.UsersApi();
apiInstance.getMe((error, data, response) => {
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

[**UserDTO**](UserDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getTimeZone

> TimeZoneDTO getTimeZone()

Returns time zone preferred by user currently signed in.

Returns time zone preferred by user currently signed in.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.UsersApi();
apiInstance.getTimeZone((error, data, response) => {
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

[**TimeZoneDTO**](TimeZoneDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## update3

> UserDTO update3(userId, userDTO)

Updates an existing user.

Updates an existing user.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.UsersApi();
let userId = 789; // Number | user's internal identifier
let userDTO = /home-api/assets/examples/users/update2.json#requestBody; // UserDTO | Updated existing user.
apiInstance.update3(userId, userDTO, (error, data, response) => {
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
 **userId** | **Number**| user&#39;s internal identifier | 
 **userDTO** | [**UserDTO**](UserDTO.md)| Updated existing user. | 

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateCustomField1

> CustomFieldDTO updateCustomField1(userId, customFieldKey, customFieldDTO)

Updates given custom field of a given user.

Updates given custom field of a given user.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.UsersApi();
let userId = 789; // Number | user's internal identifier
let customFieldKey = "customFieldKey_example"; // String | custom field's key
let customFieldDTO = /home-api/assets/examples/users/updateCustomField.json#requestBody; // CustomFieldDTO | Updated custom fields of a given user.
apiInstance.updateCustomField1(userId, customFieldKey, customFieldDTO, (error, data, response) => {
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
 **userId** | **Number**| user&#39;s internal identifier | 
 **customFieldKey** | **String**| custom field&#39;s key | 
 **customFieldDTO** | [**CustomFieldDTO**](CustomFieldDTO.md)| Updated custom fields of a given user. | 

### Return type

[**CustomFieldDTO**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateCustomFields2

> [CustomFieldDTO] updateCustomFields2(userId, customFieldDTO)

Updates custom fields of a given user.

Updates custom fields of a given user.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.UsersApi();
let userId = 789; // Number | user's internal identifier
let customFieldDTO = /home-api/assets/examples/users/updateCustomFields.json#requestBody; // [CustomFieldDTO] | Updated custom fields of a given user.
apiInstance.updateCustomFields2(userId, customFieldDTO, (error, data, response) => {
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
 **userId** | **Number**| user&#39;s internal identifier | 
 **customFieldDTO** | [**[CustomFieldDTO]**](CustomFieldDTO.md)| Updated custom fields of a given user. | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

