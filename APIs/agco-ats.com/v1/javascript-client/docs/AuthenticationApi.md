# AgcoApi.AuthenticationApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticationDefault**](AuthenticationApi.md#authenticationDefault) | **POST** /api/v2/Authentication | Authenticate a user.
[**authenticationIsAlive**](AuthenticationApi.md#authenticationIsAlive) | **GET** /api/v2/Authentication/IsAlive | Acknowledges the connection to the API
[**authenticationPutManageTokens**](AuthenticationApi.md#authenticationPutManageTokens) | **PUT** /api/v2/AuthenticatedUsers/{UserID}/Tokens | Manage API tokens.
[**authenticationRequestPasswordReset**](AuthenticationApi.md#authenticationRequestPasswordReset) | **POST** /api/v2/Authentication/RequestPasswordReset | Request a password reset.
[**authenticationResetPasword**](AuthenticationApi.md#authenticationResetPasword) | **POST** /api/v2/Authentication/ResetPasword | Reset a password



## authenticationDefault

> APIModelsAuthenticatedUser authenticationDefault(aPIModelsCredentials)

Authenticate a user.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthenticationApi();
let aPIModelsCredentials = new AgcoApi.APIModelsCredentials(); // APIModelsCredentials | Create a user account.
apiInstance.authenticationDefault(aPIModelsCredentials, (error, data, response) => {
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
 **aPIModelsCredentials** | [**APIModelsCredentials**](APIModelsCredentials.md)| Create a user account. | 

### Return type

[**APIModelsAuthenticatedUser**](APIModelsAuthenticatedUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## authenticationIsAlive

> authenticationIsAlive()

Acknowledges the connection to the API

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthenticationApi();
apiInstance.authenticationIsAlive((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## authenticationPutManageTokens

> authenticationPutManageTokens(userID, aPIModelsTokenOptions)

Manage API tokens.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthenticationApi();
let userID = 56; // Number | 
let aPIModelsTokenOptions = new AgcoApi.APIModelsTokenOptions(); // APIModelsTokenOptions | The options for token management.
apiInstance.authenticationPutManageTokens(userID, aPIModelsTokenOptions, (error, data, response) => {
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
 **userID** | **Number**|  | 
 **aPIModelsTokenOptions** | [**APIModelsTokenOptions**](APIModelsTokenOptions.md)| The options for token management. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined


## authenticationRequestPasswordReset

> authenticationRequestPasswordReset(aPIModelsPasswordResetRequest)

Request a password reset.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthenticationApi();
let aPIModelsPasswordResetRequest = new AgcoApi.APIModelsPasswordResetRequest(); // APIModelsPasswordResetRequest | The password reset request.
apiInstance.authenticationRequestPasswordReset(aPIModelsPasswordResetRequest, (error, data, response) => {
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
 **aPIModelsPasswordResetRequest** | [**APIModelsPasswordResetRequest**](APIModelsPasswordResetRequest.md)| The password reset request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined


## authenticationResetPasword

> authenticationResetPasword(aPIModelsPasswordReset)

Reset a password

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthenticationApi();
let aPIModelsPasswordReset = new AgcoApi.APIModelsPasswordReset(); // APIModelsPasswordReset | The password reset detail.
apiInstance.authenticationResetPasword(aPIModelsPasswordReset, (error, data, response) => {
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
 **aPIModelsPasswordReset** | [**APIModelsPasswordReset**](APIModelsPasswordReset.md)| The password reset detail. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined

