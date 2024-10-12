# Apacta.UsersApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersBulkActivate**](UsersApi.md#usersBulkActivate) | **POST** /users/bulkActivate | Activate multiple users
[**usersBulkDeactivate**](UsersApi.md#usersBulkDeactivate) | **POST** /users/bulkDeactivate | Deactivate multiple users
[**usersGet**](UsersApi.md#usersGet) | **GET** /users | Get list of users in company
[**usersPost**](UsersApi.md#usersPost) | **POST** /users | Add user to company
[**usersResendWelcomeSmsGet**](UsersApi.md#usersResendWelcomeSmsGet) | **GET** /users/resendWelcomeSms | Resend Welcome SMS to the user
[**usersUserIdDelete**](UsersApi.md#usersUserIdDelete) | **DELETE** /users/{user_id} | Delete user
[**usersUserIdGet**](UsersApi.md#usersUserIdGet) | **GET** /users/{user_id} | View user
[**usersUserIdIntegrationSettingsGet**](UsersApi.md#usersUserIdIntegrationSettingsGet) | **GET** /users/{user_id}/integration_settings | Get a list of user integration settings
[**usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete**](UsersApi.md#usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete) | **DELETE** /users/{user_id}/integration_settings/{integration_settings_user_id} | Delete a user integration setting
[**usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet**](UsersApi.md#usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet) | **GET** /users/{user_id}/integration_settings/{integration_settings_user_id} | Get a user integration setting
[**usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut**](UsersApi.md#usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut) | **PUT** /users/{user_id}/integration_settings/{integration_settings_user_id} | Edit a user integration setting
[**usersUserIdIntegrationSettingsPost**](UsersApi.md#usersUserIdIntegrationSettingsPost) | **POST** /users/{user_id}/integration_settings | Add a user integration setting
[**usersUserIdPut**](UsersApi.md#usersUserIdPut) | **PUT** /users/{user_id} | Edit user
[**usersUserIdUploadImagePost**](UsersApi.md#usersUserIdUploadImagePost) | **POST** /users/{user_id}/uploadImage | Upload a new image to a user



## usersBulkActivate

> EmptySuccessResponse usersBulkActivate(opts)

Activate multiple users

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let opts = {
  'bulkActionRequestBody': new Apacta.BulkActionRequestBody() // BulkActionRequestBody | User ids
};
apiInstance.usersBulkActivate(opts, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| User ids | [optional] 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersBulkDeactivate

> EmptySuccessResponse usersBulkDeactivate(opts)

Deactivate multiple users

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let opts = {
  'bulkActionRequestBody': new Apacta.BulkActionRequestBody() // BulkActionRequestBody | User ids
};
apiInstance.usersBulkDeactivate(opts, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| User ids | [optional] 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersGet

> ProjectsProjectIdUsersGet200Response usersGet(opts)

Get list of users in company

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let opts = {
  'firstName': "firstName_example", // String | Used to filter on the `first_name` of the users
  'lastName': "lastName_example", // String | Used to filter on the `last_name` of the users
  'email': "email_example", // String | Used to filter on the `email` of the users
  'stockLocationId': "stockLocationId_example", // String | Used to filter on the `stock_location_id` of the users
  'isActive': true // Boolean | Filters active/inactive users
};
apiInstance.usersGet(opts, (error, data, response) => {
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
 **firstName** | **String**| Used to filter on the &#x60;first_name&#x60; of the users | [optional] 
 **lastName** | **String**| Used to filter on the &#x60;last_name&#x60; of the users | [optional] 
 **email** | **String**| Used to filter on the &#x60;email&#x60; of the users | [optional] 
 **stockLocationId** | **String**| Used to filter on the &#x60;stock_location_id&#x60; of the users | [optional] 
 **isActive** | **Boolean**| Filters active/inactive users | [optional] 

### Return type

[**ProjectsProjectIdUsersGet200Response**](ProjectsProjectIdUsersGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersPost

> ClockingRecordsPost201Response usersPost(opts)

Add user to company

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let opts = {
  'usersPostRequest': new Apacta.UsersPostRequest() // UsersPostRequest | 
};
apiInstance.usersPost(opts, (error, data, response) => {
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
 **usersPostRequest** | [**UsersPostRequest**](UsersPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersResendWelcomeSmsGet

> UsersResendWelcomeSmsGet200Response usersResendWelcomeSmsGet()

Resend Welcome SMS to the user

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
apiInstance.usersResendWelcomeSmsGet((error, data, response) => {
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

[**UsersResendWelcomeSmsGet200Response**](UsersResendWelcomeSmsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdDelete

> ClockingRecordsClockingRecordIdPut200Response usersUserIdDelete(userId)

Delete user

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let userId = "userId_example"; // String | 
apiInstance.usersUserIdDelete(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdGet

> ProjectsProjectIdUsersUserIdGet200Response usersUserIdGet(userId)

View user

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let userId = "userId_example"; // String | 
apiInstance.usersUserIdGet(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

[**ProjectsProjectIdUsersUserIdGet200Response**](ProjectsProjectIdUsersUserIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdIntegrationSettingsGet

> UsersUserIdIntegrationSettingsGet200Response usersUserIdIntegrationSettingsGet(userId)

Get a list of user integration settings

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let userId = "userId_example"; // String | 
apiInstance.usersUserIdIntegrationSettingsGet(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

[**UsersUserIdIntegrationSettingsGet200Response**](UsersUserIdIntegrationSettingsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete

> EmptySuccessResponse usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete(userId, integrationSettingsUserId)

Delete a user integration setting

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let userId = "userId_example"; // String | 
let integrationSettingsUserId = "integrationSettingsUserId_example"; // String | 
apiInstance.usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete(userId, integrationSettingsUserId, (error, data, response) => {
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
 **userId** | **String**|  | 
 **integrationSettingsUserId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet

> UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet(userId, integrationSettingsUserId)

Get a user integration setting

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let userId = "userId_example"; // String | 
let integrationSettingsUserId = "integrationSettingsUserId_example"; // String | 
apiInstance.usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet(userId, integrationSettingsUserId, (error, data, response) => {
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
 **userId** | **String**|  | 
 **integrationSettingsUserId** | **String**|  | 

### Return type

[**UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response**](UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut

> EmptySuccessResponse usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut(userId, integrationSettingsUserId)

Edit a user integration setting

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let userId = "userId_example"; // String | 
let integrationSettingsUserId = "integrationSettingsUserId_example"; // String | 
apiInstance.usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut(userId, integrationSettingsUserId, (error, data, response) => {
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
 **userId** | **String**|  | 
 **integrationSettingsUserId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdIntegrationSettingsPost

> CreateSuccessResponse usersUserIdIntegrationSettingsPost(userId, opts)

Add a user integration setting

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let userId = "userId_example"; // String | 
let opts = {
  'companiesCompanyIdIntegrationSettingsPostRequest': new Apacta.CompaniesCompanyIdIntegrationSettingsPostRequest() // CompaniesCompanyIdIntegrationSettingsPostRequest | 
};
apiInstance.usersUserIdIntegrationSettingsPost(userId, opts, (error, data, response) => {
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
 **userId** | **String**|  | 
 **companiesCompanyIdIntegrationSettingsPostRequest** | [**CompaniesCompanyIdIntegrationSettingsPostRequest**](CompaniesCompanyIdIntegrationSettingsPostRequest.md)|  | [optional] 

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUserIdPut

> ClockingRecordsClockingRecordIdPut200Response usersUserIdPut(userId)

Edit user

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let userId = "userId_example"; // String | 
apiInstance.usersUserIdPut(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdUploadImagePost

> CreateSuccessResponse usersUserIdUploadImagePost(userId, opts)

Upload a new image to a user

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UsersApi();
let userId = "userId_example"; // String | 
let opts = {
  'image': "/path/to/file" // File | 
};
apiInstance.usersUserIdUploadImagePost(userId, opts, (error, data, response) => {
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
 **userId** | **String**|  | 
 **image** | **File**|  | [optional] 

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

