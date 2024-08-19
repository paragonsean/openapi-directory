# IQualifyManagementApi.UsersInIQualifyApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersPost**](UsersInIQualifyApi.md#usersPost) | **POST** /users | Add new user
[**usersUserEmailGet**](UsersInIQualifyApi.md#usersUserEmailGet) | **GET** /users/{userEmail} | Find user by email
[**usersUserEmailInviteEmailPost**](UsersInIQualifyApi.md#usersUserEmailInviteEmailPost) | **POST** /users/{userEmail}/invite-email | Resend invitation email
[**usersUserEmailOfferingsGet**](UsersInIQualifyApi.md#usersUserEmailOfferingsGet) | **GET** /users/{userEmail}/offerings | Find user&#39;s offerings
[**usersUserEmailOfferingsPost**](UsersInIQualifyApi.md#usersUserEmailOfferingsPost) | **POST** /users/{userEmail}/offerings | Adds the user to the specified offerings as a learner
[**usersUserEmailPatch**](UsersInIQualifyApi.md#usersUserEmailPatch) | **PATCH** /users/{userEmail} | Update user
[**usersUserEmailPermissionsPermissionNamePost**](UsersInIQualifyApi.md#usersUserEmailPermissionsPermissionNamePost) | **POST** /users/{userEmail}/permissions/{permissionName} | Add permission to user
[**usersUserEmailSuspendPut**](UsersInIQualifyApi.md#usersUserEmailSuspendPut) | **PUT** /users/{userEmail}/suspend | Suspend user



## usersPost

> UserResponse usersPost(user)

Add new user

Creates a new user.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.UsersInIQualifyApi();
let user = new IQualifyManagementApi.User(); // User | user
apiInstance.usersPost(user, (error, data, response) => {
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
 **user** | [**User**](User.md)| user | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUserEmailGet

> UserResponse usersUserEmailGet(userEmail)

Find user by email

Responds with a user matching the specified email.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.UsersInIQualifyApi();
let userEmail = "userEmail_example"; // String | user's email
apiInstance.usersUserEmailGet(userEmail, (error, data, response) => {
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
 **userEmail** | **String**| user&#39;s email | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserEmailInviteEmailPost

> usersUserEmailInviteEmailPost(userEmail)

Resend invitation email

Re-sends an invitation e-mail to the specified user.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.UsersInIQualifyApi();
let userEmail = "userEmail_example"; // String | user's email
apiInstance.usersUserEmailInviteEmailPost(userEmail, (error, data, response) => {
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
 **userEmail** | **String**| user&#39;s email | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserEmailOfferingsGet

> [OfferingMetadataResponse] usersUserEmailOfferingsGet(userEmail)

Find user&#39;s offerings

Responds with all offerings that the user in.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.UsersInIQualifyApi();
let userEmail = "userEmail_example"; // String | user's email
apiInstance.usersUserEmailOfferingsGet(userEmail, (error, data, response) => {
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
 **userEmail** | **String**| user&#39;s email | 

### Return type

[**[OfferingMetadataResponse]**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserEmailOfferingsPost

> [OfferingMetadataResponse] usersUserEmailOfferingsPost(userEmail, requestBody)

Adds the user to the specified offerings as a learner

Adds a user to an array of offerings by offeringId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.UsersInIQualifyApi();
let userEmail = "userEmail_example"; // String | user's email
let requestBody = ["null"]; // [String] | offering ids
apiInstance.usersUserEmailOfferingsPost(userEmail, requestBody, (error, data, response) => {
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
 **userEmail** | **String**| user&#39;s email | 
 **requestBody** | [**[String]**](String.md)| offering ids | 

### Return type

[**[OfferingMetadataResponse]**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUserEmailPatch

> UserResponse usersUserEmailPatch(userEmail, opts)

Update user

Updates the specified user by email.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.UsersInIQualifyApi();
let userEmail = "userEmail_example"; // String | user's email
let opts = {
  'user': new IQualifyManagementApi.User() // User | 
};
apiInstance.usersUserEmailPatch(userEmail, opts, (error, data, response) => {
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
 **userEmail** | **String**| user&#39;s email | 
 **user** | [**User**](User.md)|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUserEmailPermissionsPermissionNamePost

> UserResponse usersUserEmailPermissionsPermissionNamePost(userEmail, permissionName)

Add permission to user

Adds additional permissions to the specified user.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.UsersInIQualifyApi();
let userEmail = "userEmail_example"; // String | user's email
let permissionName = "permissionName_example"; // String | permission name
apiInstance.usersUserEmailPermissionsPermissionNamePost(userEmail, permissionName, (error, data, response) => {
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
 **userEmail** | **String**| user&#39;s email | 
 **permissionName** | **String**| permission name | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserEmailSuspendPut

> usersUserEmailSuspendPut(userEmail, suspendedRequest)

Suspend user

Suspends the specified user&#39;s account.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.UsersInIQualifyApi();
let userEmail = "userEmail_example"; // String | user's email
let suspendedRequest = new IQualifyManagementApi.SuspendedRequest(); // SuspendedRequest | 
apiInstance.usersUserEmailSuspendPut(userEmail, suspendedRequest, (error, data, response) => {
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
 **userEmail** | **String**| user&#39;s email | 
 **suspendedRequest** | [**SuspendedRequest**](SuspendedRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

