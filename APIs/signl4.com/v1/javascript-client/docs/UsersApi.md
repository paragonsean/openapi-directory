# Signl4Api.UsersApi

All URIs are relative to *https://connect.signl4.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersGet**](UsersApi.md#usersGet) | **GET** /users | Get all Users
[**usersUserIdChangePasswordPut**](UsersApi.md#usersUserIdChangePasswordPut) | **PUT** /users/{userId}/changePassword | Updates the password of a user
[**usersUserIdCheckPermissionsPost**](UsersApi.md#usersUserIdCheckPermissionsPost) | **POST** /users/{userId}/checkPermissions | Checks if a user has the provided permission.
[**usersUserIdDutyStatusGet**](UsersApi.md#usersUserIdDutyStatusGet) | **GET** /users/{userId}/dutyStatus | Get duty status by user Id
[**usersUserIdGet**](UsersApi.md#usersUserIdGet) | **GET** /users/{userId} | Get User by Id
[**usersUserIdImageGet**](UsersApi.md#usersUserIdImageGet) | **GET** /users/{userId}/image | 
[**usersUserIdImagePost**](UsersApi.md#usersUserIdImagePost) | **POST** /users/{userId}/image | Uploaded a profile image for a specified user.
[**usersUserIdProfilePut**](UsersApi.md#usersUserIdProfilePut) | **PUT** /users/{userId}/profile | Updates user profile of an user
[**usersUserIdPunchInAsManagerPost**](UsersApi.md#usersUserIdPunchInAsManagerPost) | **POST** /users/{userId}/punchInAsManager | Punch User in as Manager
[**usersUserIdPunchInPost**](UsersApi.md#usersUserIdPunchInPost) | **POST** /users/{userId}/punchIn | Punch User in
[**usersUserIdPunchOutPost**](UsersApi.md#usersUserIdPunchOutPost) | **POST** /users/{userId}/punchOut | Punch User out
[**usersUserIdSetupProgressGet**](UsersApi.md#usersUserIdSetupProgressGet) | **GET** /users/{userId}/setupProgress | Gets setup progress of a specific user.



## usersGet

> [UserInfo] usersGet()

Get all Users

Returns a list of user objects with details such as their email address and duty information. Only users who  are part of your team will be returned.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.UsersApi();
apiInstance.usersGet((error, data, response) => {
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

[**[UserInfo]**](UserInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## usersUserIdChangePasswordPut

> usersUserIdChangePasswordPut(userId, opts)

Updates the password of a user

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.UsersApi();
let userId = "userId_example"; // String | User ID of user whose password should be changed.
let opts = {
  'updatePasswordInfo': new Signl4Api.UpdatePasswordInfo() // UpdatePasswordInfo | 
};
apiInstance.usersUserIdChangePasswordPut(userId, opts, (error, data, response) => {
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
 **userId** | **String**| User ID of user whose password should be changed. | 
 **updatePasswordInfo** | [**UpdatePasswordInfo**](UpdatePasswordInfo.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## usersUserIdCheckPermissionsPost

> UserImage usersUserIdCheckPermissionsPost(userId, opts)

Checks if a user has the provided permission.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.UsersApi();
let userId = "userId_example"; // String | ID of the user to check permissions for.
let opts = {
  'teamId': "teamId_example", // String | 
  'stringItemsWrapper': new Signl4Api.StringItemsWrapper() // StringItemsWrapper | List of permissions to check
};
apiInstance.usersUserIdCheckPermissionsPost(userId, opts, (error, data, response) => {
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
 **userId** | **String**| ID of the user to check permissions for. | 
 **teamId** | **String**|  | [optional] 
 **stringItemsWrapper** | [**StringItemsWrapper**](StringItemsWrapper.md)| List of permissions to check | [optional] 

### Return type

[**UserImage**](UserImage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## usersUserIdDutyStatusGet

> UserDutyInfo usersUserIdDutyStatusGet(userId)

Get duty status by user Id

Returns a object with duty information.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.UsersApi();
let userId = "userId_example"; // String | Identifier of the user to get. Use 'Me' to get information about the currently logged in user. This is not possible with an api key.  Can also be an email address of a user in the team or the unique id of an according user object.”
apiInstance.usersUserIdDutyStatusGet(userId, (error, data, response) => {
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
 **userId** | **String**| Identifier of the user to get. Use &#39;Me&#39; to get information about the currently logged in user. This is not possible with an api key.  Can also be an email address of a user in the team or the unique id of an according user object.” | 

### Return type

[**UserDutyInfo**](UserDutyInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## usersUserIdGet

> UserInfo usersUserIdGet(userId)

Get User by Id

Returns a user object with details such as his email address and duty information.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.UsersApi();
let userId = "userId_example"; // String | Identifier of the user to get. Use 'Me' to get information about the currently logged in user. This is not possible with an api key.  Can also be an email address of a user in the team or the unique id of an according user object.”
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
 **userId** | **String**| Identifier of the user to get. Use &#39;Me&#39; to get information about the currently logged in user. This is not possible with an api key.  Can also be an email address of a user in the team or the unique id of an according user object.” | 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## usersUserIdImageGet

> UserImage usersUserIdImageGet(userId, opts)



### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.UsersApi();
let userId = "userId_example"; // String | 
let opts = {
  'height': 56, // Number | 
  'width': 56 // Number | 
};
apiInstance.usersUserIdImageGet(userId, opts, (error, data, response) => {
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
 **height** | **Number**|  | [optional] 
 **width** | **Number**|  | [optional] 

### Return type

[**UserImage**](UserImage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## usersUserIdImagePost

> usersUserIdImagePost(userId)

Uploaded a profile image for a specified user.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.UsersApi();
let userId = "userId_example"; // String | Id of the user.
apiInstance.usersUserIdImagePost(userId, (error, data, response) => {
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
 **userId** | **String**| Id of the user. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## usersUserIdProfilePut

> UserInfo usersUserIdProfilePut(userId, opts)

Updates user profile of an user

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.UsersApi();
let userId = "userId_example"; // String | ID of user to update.
let opts = {
  'userProfile': new Signl4Api.UserProfile() // UserProfile | 
};
apiInstance.usersUserIdProfilePut(userId, opts, (error, data, response) => {
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
 **userId** | **String**| ID of user to update. | 
 **userProfile** | [**UserProfile**](UserProfile.md)|  | [optional] 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## usersUserIdPunchInAsManagerPost

> UserDutyInfo usersUserIdPunchInAsManagerPost(userId)

Punch User in as Manager

The specified user will be punched in to duty as a manager.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.UsersApi();
let userId = "userId_example"; // String | Identifier of the user to punch in. Use 'Me' to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.”
apiInstance.usersUserIdPunchInAsManagerPost(userId, (error, data, response) => {
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
 **userId** | **String**| Identifier of the user to punch in. Use &#39;Me&#39; to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.” | 

### Return type

[**UserDutyInfo**](UserDutyInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## usersUserIdPunchInPost

> UserDutyInfo usersUserIdPunchInPost(userId)

Punch User in

The specified user will be punched in to duty.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.UsersApi();
let userId = "userId_example"; // String | Identifier of the user to punch in. Use 'Me' to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.”
apiInstance.usersUserIdPunchInPost(userId, (error, data, response) => {
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
 **userId** | **String**| Identifier of the user to punch in. Use &#39;Me&#39; to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.” | 

### Return type

[**UserDutyInfo**](UserDutyInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## usersUserIdPunchOutPost

> UserDutyInfo usersUserIdPunchOutPost(userId)

Punch User out

The specified user will be punched out from duty.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.UsersApi();
let userId = "userId_example"; // String | Identifier of the user to punch out. Use 'Me' to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.”
apiInstance.usersUserIdPunchOutPost(userId, (error, data, response) => {
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
 **userId** | **String**| Identifier of the user to punch out. Use &#39;Me&#39; to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.” | 

### Return type

[**UserDutyInfo**](UserDutyInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## usersUserIdSetupProgressGet

> UserSetupProgress usersUserIdSetupProgressGet(userId)

Gets setup progress of a specific user.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.UsersApi();
let userId = "userId_example"; // String | ID of the user the progress should be retrieved for.
apiInstance.usersUserIdSetupProgressGet(userId, (error, data, response) => {
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
 **userId** | **String**| ID of the user the progress should be retrieved for. | 

### Return type

[**UserSetupProgress**](UserSetupProgress.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

