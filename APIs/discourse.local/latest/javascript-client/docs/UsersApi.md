# DiscourseApiDocumentation.UsersApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminGetUser**](UsersApi.md#adminGetUser) | **GET** /admin/users/{id}.json | Get a user by id
[**adminListUsers**](UsersApi.md#adminListUsers) | **GET** /admin/users/list/{flag}.json | Get a list of users
[**anonymizeUser**](UsersApi.md#anonymizeUser) | **PUT** /admin/users/{id}/anonymize.json | Anonymize a user
[**changePassword**](UsersApi.md#changePassword) | **PUT** /users/password-reset/{token}.json | Change password
[**createUser**](UsersApi.md#createUser) | **POST** /users.json | Creates a user
[**deleteUser**](UsersApi.md#deleteUser) | **DELETE** /admin/users/{id}.json | Delete a user
[**getUser**](UsersApi.md#getUser) | **GET** /u/{username}.json | Get a single user by username
[**getUserEmails**](UsersApi.md#getUserEmails) | **GET** /u/{username}/emails.json | Get email addresses belonging to a user
[**getUserExternalId**](UsersApi.md#getUserExternalId) | **GET** /u/by-external/{external_id}.json | Get a user by external_id
[**getUserIdentiyProviderExternalId**](UsersApi.md#getUserIdentiyProviderExternalId) | **GET** /u/by-external/{provider}/{external_id}.json | Get a user by identity provider external ID
[**listUserActions**](UsersApi.md#listUserActions) | **GET** /user_actions.json | Get a list of user actions
[**listUserBadges_0**](UsersApi.md#listUserBadges_0) | **GET** /user-badges/{username}.json | List badges for a user
[**listUsersPublic**](UsersApi.md#listUsersPublic) | **GET** /directory_items.json | Get a public list of users
[**logOutUser**](UsersApi.md#logOutUser) | **POST** /admin/users/{id}/log_out.json | Log a user out
[**refreshGravatar**](UsersApi.md#refreshGravatar) | **POST** /user_avatar/{username}/refresh_gravatar.json | Refresh gravatar
[**sendPasswordResetEmail**](UsersApi.md#sendPasswordResetEmail) | **POST** /session/forgot_password.json | Send password reset email
[**silenceUser**](UsersApi.md#silenceUser) | **PUT** /admin/users/{id}/silence.json | Silence a user
[**suspendUser**](UsersApi.md#suspendUser) | **PUT** /admin/users/{id}/suspend.json | Suspend a user
[**updateAvatar**](UsersApi.md#updateAvatar) | **PUT** /u/{username}/preferences/avatar/pick.json | Update avatar
[**updateEmail**](UsersApi.md#updateEmail) | **PUT** /u/{username}/preferences/email.json | Update email
[**updateUser**](UsersApi.md#updateUser) | **PUT** /u/{username}.json | Update a user
[**updateUsername**](UsersApi.md#updateUsername) | **PUT** /u/{username}/preferences/username.json | Update username



## adminGetUser

> AdminGetUser200Response adminGetUser(id)

Get a user by id

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let id = 56; // Number | 
apiInstance.adminGetUser(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**AdminGetUser200Response**](AdminGetUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminListUsers

> [AdminListUsers200ResponseInner] adminListUsers(flag, opts)

Get a list of users

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let flag = "flag_example"; // String | 
let opts = {
  'order': "order_example", // String | 
  'asc': "asc_example", // String | 
  'page': 56, // Number | 
  'showEmails': true // Boolean | 
};
apiInstance.adminListUsers(flag, opts, (error, data, response) => {
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
 **flag** | **String**|  | 
 **order** | **String**|  | [optional] 
 **asc** | **String**|  | [optional] 
 **page** | **Number**|  | [optional] 
 **showEmails** | **Boolean**|  | [optional] 

### Return type

[**[AdminListUsers200ResponseInner]**](AdminListUsers200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## anonymizeUser

> AnonymizeUser200Response anonymizeUser(id)

Anonymize a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let id = 56; // Number | 
apiInstance.anonymizeUser(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**AnonymizeUser200Response**](AnonymizeUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## changePassword

> changePassword(token, opts)

Change password

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let token = "token_example"; // String | 
let opts = {
  'changePasswordRequest': new DiscourseApiDocumentation.ChangePasswordRequest() // ChangePasswordRequest | 
};
apiInstance.changePassword(token, opts, (error, data, response) => {
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
 **token** | **String**|  | 
 **changePasswordRequest** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createUser

> CreateUser200Response createUser(apiKey, apiUsername, opts)

Creates a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let opts = {
  'createUserRequest': new DiscourseApiDocumentation.CreateUserRequest() // CreateUserRequest | 
};
apiInstance.createUser(apiKey, apiUsername, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **createUserRequest** | [**CreateUserRequest**](CreateUserRequest.md)|  | [optional] 

### Return type

[**CreateUser200Response**](CreateUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteUser

> DeleteUser200Response deleteUser(id, opts)

Delete a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let id = 56; // Number | 
let opts = {
  'deleteUserRequest': new DiscourseApiDocumentation.DeleteUserRequest() // DeleteUserRequest | 
};
apiInstance.deleteUser(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **deleteUserRequest** | [**DeleteUserRequest**](DeleteUserRequest.md)|  | [optional] 

### Return type

[**DeleteUser200Response**](DeleteUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getUser

> GetUserExternalId200Response getUser(apiKey, apiUsername, username)

Get a single user by username

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let username = "username_example"; // String | 
apiInstance.getUser(apiKey, apiUsername, username, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **username** | **String**|  | 

### Return type

[**GetUserExternalId200Response**](GetUserExternalId200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserEmails

> GetUserEmails200Response getUserEmails(username)

Get email addresses belonging to a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let username = "username_example"; // String | 
apiInstance.getUserEmails(username, (error, data, response) => {
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
 **username** | **String**|  | 

### Return type

[**GetUserEmails200Response**](GetUserEmails200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserExternalId

> GetUserExternalId200Response getUserExternalId(apiKey, apiUsername, externalId)

Get a user by external_id

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let externalId = "externalId_example"; // String | 
apiInstance.getUserExternalId(apiKey, apiUsername, externalId, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **externalId** | **String**|  | 

### Return type

[**GetUserExternalId200Response**](GetUserExternalId200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserIdentiyProviderExternalId

> GetUserExternalId200Response getUserIdentiyProviderExternalId(apiKey, apiUsername, provider, externalId)

Get a user by identity provider external ID

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let provider = "provider_example"; // String | Authentication provider name. Can be found in the provider callback URL: `/auth/{provider}/callback`
let externalId = "externalId_example"; // String | 
apiInstance.getUserIdentiyProviderExternalId(apiKey, apiUsername, provider, externalId, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **provider** | **String**| Authentication provider name. Can be found in the provider callback URL: &#x60;/auth/{provider}/callback&#x60; | 
 **externalId** | **String**|  | 

### Return type

[**GetUserExternalId200Response**](GetUserExternalId200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUserActions

> ListUserActions200Response listUserActions(offset, username, filter)

Get a list of user actions

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let offset = 56; // Number | 
let username = "username_example"; // String | 
let filter = "filter_example"; // String | 
apiInstance.listUserActions(offset, username, filter, (error, data, response) => {
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
 **offset** | **Number**|  | 
 **username** | **String**|  | 
 **filter** | **String**|  | 

### Return type

[**ListUserActions200Response**](ListUserActions200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUserBadges_0

> ListUserBadges200Response listUserBadges_0(username)

List badges for a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let username = "username_example"; // String | 
apiInstance.listUserBadges_0(username, (error, data, response) => {
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
 **username** | **String**|  | 

### Return type

[**ListUserBadges200Response**](ListUserBadges200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUsersPublic

> ListUsersPublic200Response listUsersPublic(period, order, opts)

Get a public list of users

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let period = "period_example"; // String | 
let order = "order_example"; // String | 
let opts = {
  'asc': "asc_example", // String | 
  'page': 56 // Number | 
};
apiInstance.listUsersPublic(period, order, opts, (error, data, response) => {
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
 **period** | **String**|  | 
 **order** | **String**|  | 
 **asc** | **String**|  | [optional] 
 **page** | **Number**|  | [optional] 

### Return type

[**ListUsersPublic200Response**](ListUsersPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## logOutUser

> DeleteGroup200Response logOutUser(id)

Log a user out

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let id = 56; // Number | 
apiInstance.logOutUser(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**DeleteGroup200Response**](DeleteGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## refreshGravatar

> RefreshGravatar200Response refreshGravatar(username)

Refresh gravatar

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let username = "username_example"; // String | 
apiInstance.refreshGravatar(username, (error, data, response) => {
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
 **username** | **String**|  | 

### Return type

[**RefreshGravatar200Response**](RefreshGravatar200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendPasswordResetEmail

> SendPasswordResetEmail200Response sendPasswordResetEmail(opts)

Send password reset email

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let opts = {
  'sendPasswordResetEmailRequest': new DiscourseApiDocumentation.SendPasswordResetEmailRequest() // SendPasswordResetEmailRequest | 
};
apiInstance.sendPasswordResetEmail(opts, (error, data, response) => {
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
 **sendPasswordResetEmailRequest** | [**SendPasswordResetEmailRequest**](SendPasswordResetEmailRequest.md)|  | [optional] 

### Return type

[**SendPasswordResetEmail200Response**](SendPasswordResetEmail200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## silenceUser

> SilenceUser200Response silenceUser(id, opts)

Silence a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let id = 56; // Number | 
let opts = {
  'silenceUserRequest': new DiscourseApiDocumentation.SilenceUserRequest() // SilenceUserRequest | 
};
apiInstance.silenceUser(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **silenceUserRequest** | [**SilenceUserRequest**](SilenceUserRequest.md)|  | [optional] 

### Return type

[**SilenceUser200Response**](SilenceUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## suspendUser

> SuspendUser200Response suspendUser(id, opts)

Suspend a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let id = 56; // Number | 
let opts = {
  'suspendUserRequest': new DiscourseApiDocumentation.SuspendUserRequest() // SuspendUserRequest | 
};
apiInstance.suspendUser(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **suspendUserRequest** | [**SuspendUserRequest**](SuspendUserRequest.md)|  | [optional] 

### Return type

[**SuspendUser200Response**](SuspendUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAvatar

> DeleteGroup200Response updateAvatar(username, opts)

Update avatar

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let username = "username_example"; // String | 
let opts = {
  'updateAvatarRequest': new DiscourseApiDocumentation.UpdateAvatarRequest() // UpdateAvatarRequest | 
};
apiInstance.updateAvatar(username, opts, (error, data, response) => {
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
 **username** | **String**|  | 
 **updateAvatarRequest** | [**UpdateAvatarRequest**](UpdateAvatarRequest.md)|  | [optional] 

### Return type

[**DeleteGroup200Response**](DeleteGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEmail

> updateEmail(username, opts)

Update email

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let username = "username_example"; // String | 
let opts = {
  'updateEmailRequest': new DiscourseApiDocumentation.UpdateEmailRequest() // UpdateEmailRequest | 
};
apiInstance.updateEmail(username, opts, (error, data, response) => {
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
 **username** | **String**|  | 
 **updateEmailRequest** | [**UpdateEmailRequest**](UpdateEmailRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateUser

> UpdateUser200Response updateUser(apiKey, apiUsername, username, opts)

Update a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let username = "username_example"; // String | 
let opts = {
  'updateUserRequest': new DiscourseApiDocumentation.UpdateUserRequest() // UpdateUserRequest | 
};
apiInstance.updateUser(apiKey, apiUsername, username, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **username** | **String**|  | 
 **updateUserRequest** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | [optional] 

### Return type

[**UpdateUser200Response**](UpdateUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUsername

> updateUsername(username, opts)

Update username

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.UsersApi();
let username = "username_example"; // String | 
let opts = {
  'updateUsernameRequest': new DiscourseApiDocumentation.UpdateUsernameRequest() // UpdateUsernameRequest | 
};
apiInstance.updateUsername(username, opts, (error, data, response) => {
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
 **username** | **String**|  | 
 **updateUsernameRequest** | [**UpdateUsernameRequest**](UpdateUsernameRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

