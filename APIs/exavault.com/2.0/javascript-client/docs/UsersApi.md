# ExaVault.UsersApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addUser**](UsersApi.md#addUser) | **POST** /users | Create a user
[**deleteUser**](UsersApi.md#deleteUser) | **DELETE** /users/{id} | Delete a user
[**getUserById**](UsersApi.md#getUserById) | **GET** /users/{id} | Get info for a user
[**listUsers**](UsersApi.md#listUsers) | **GET** /users | Get a list of users
[**updateUser**](UsersApi.md#updateUser) | **PATCH** /users/{id} | Update a user



## addUser

> UserResponse addUser(evApiKey, evAccessToken, opts)

Create a user

Adds a new user to the account. The user may be configured as an admin or standard user, and (if a standard user) may be assigned a restricted [home directory](/docs/account/04-users/00-introduction#setting-the-user-s-home-directory) and restricted [permissions](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions).   **Notes:**  - You must be an [admin-level user](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to use this.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.UsersApi();
let evApiKey = "evApiKey_example"; // String | API key required to make the API call
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'addUserRequestBody': {"email":"testuser@example.com","expiration":"2011-03-21 00:18:56","homeResource":"/","locked":true,"nickname":"testnickname","onboarding":true,"password":"string","permissions":{"changePassword":true,"delete":true,"deleteFormData":true,"download":true,"list":true,"modify":true,"notification":true,"share":true,"upload":true,"viewFormData":true},"role":"user","timeZone":"America/Los_Angeles","username":"testuser","welcomeEmail":true} // AddUserRequestBody | 
};
apiInstance.addUser(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API key required to make the API call | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **addUserRequestBody** | [**AddUserRequestBody**](AddUserRequestBody.md)|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteUser

> EmptyResponse deleteUser(id, evApiKey, evAccessToken)

Delete a user

Delete a user from the account. Deleting a user does **NOT** delete any files from the account; it merely removes a user&#39;s access. Aternatively, locking a user via the [PATCH /users/{id}](#operation/updateUser) will keep the user in your account, but make it unable to log in.   Resources and shares owned by the deleted user will be owned by the master user after the deletion.  **Notes:**   - You must have [admin-level access](/docs/account/04-users/01-admin-users) to delete a user. - The primary owner of the account cannot be deleted. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.UsersApi();
let id = 2224; // Number | The user's ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method.
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
apiInstance.deleteUser(id, evApiKey, evAccessToken, (error, data, response) => {
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
 **id** | **Number**| The user&#39;s ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method. | 
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserById

> UserResponse getUserById(id, evApiKey, evAccessToken, opts)

Get info for a user

Get the details for a specific user. You can use the &#x60;include&#x60; parameter to also get the details of related records, such as the account or the home directory.  **Notes:**  - You must have [admin or master](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) access to use this.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.UsersApi();
let id = 2224; // Number | The user's ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method.
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'include': "homeResource,owneraccount" // String | Comma-separated list of relationships to include in response. Possible values include **homeResource** and **ownerAccount**.
};
apiInstance.getUserById(id, evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **id** | **Number**| The user&#39;s ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method. | 
 **evApiKey** | **String**| API Key | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **include** | **String**| Comma-separated list of relationships to include in response. Possible values include **homeResource** and **ownerAccount**. | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUsers

> UserCollectionResponse listUsers(evApiKey, evAccessToken, opts)

Get a list of users

Get a list of the users in your account. There are three main types of searches you can do with this method:  1. Search for a user by username. If you provide the &#x60;username&#x60; parameter in your call, then only the user who exactly matches that username will be in the list of matches. Any other parameters are ignored. 1. Search for a user by individual filter fields (&#x60;nickname&#x60;,&#x60;email&#x60;,&#x60;role&#x60;,&#x60;status&#x60;,&#x60;homeDir&#x60;). Users in the list will be ones who match all of the filters you choose to search by. For example, you could look for users with the \&quot;admin\&quot; &#x60;role&#x60; AND &#x60;email&#x60; addresses ending in \&quot;*@acme.com\&quot;.  1. Search for a user by search string. If you provide the &#x60;search&#x60; parameter, users whose nickname OR email OR role OR homeDir match value your provide.  **Notes:**  - You must be an [admin-level user](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to use this. - The homeDir is the full path to the user&#39;s home directory, not a resource ID or hash.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.UsersApi();
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'username': "testuser", // String | The username of the user you are looking for. Only entries with the same username as this will be in the list of results. Does not support wildcard searches.
  'homeResource': "homeResource_example", // String | Resource identifier for user's home directory. Does not support wildcard searches.
  'nickname': "nickname_example", // String | Nickname to search for. Ignored if `username` is provided. Supports wildcard searches.
  'email': "*@example.co", // String | Email to search for. Ignored if `username` is provided. Supports wildcard searches
  'role': "use", // String | Types of users to include the list. Ignored if `username` is provided. Valid options are **admin**, **master** and **user**
  'status': 56, // Number | Whether a user is locked. Ignored if `username` is provided. **0** means user is locked, **1** means user is not locked. 
  'search': "search_example", // String | Searches the nickname, email, role and homeDir fields for the provided value. Ignored if `username` is provided. Supports wildcard searches.
  'offset': 50, // Number | Starting user record in the result set. Can be used for pagination.
  'sort': "homeDir,-modified", // String | Sort order or matching users. You can sort by multiple columns by separating sort options with a comma; the sort will be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.  Valid sort fields are: **nickname**, **username**, **email**, **homeDir** and **modified**
  'limit': 100, // Number | Number of users to return. Can be used for pagination.
  'include': "homeResource,ownerAccount" // String | Comma separated list of relationships to include in response. Valid options are **homeResource** and **ownerAccount**.
};
apiInstance.listUsers(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **username** | **String**| The username of the user you are looking for. Only entries with the same username as this will be in the list of results. Does not support wildcard searches. | [optional] 
 **homeResource** | **String**| Resource identifier for user&#39;s home directory. Does not support wildcard searches. | [optional] 
 **nickname** | **String**| Nickname to search for. Ignored if &#x60;username&#x60; is provided. Supports wildcard searches. | [optional] 
 **email** | **String**| Email to search for. Ignored if &#x60;username&#x60; is provided. Supports wildcard searches | [optional] 
 **role** | **String**| Types of users to include the list. Ignored if &#x60;username&#x60; is provided. Valid options are **admin**, **master** and **user** | [optional] 
 **status** | **Number**| Whether a user is locked. Ignored if &#x60;username&#x60; is provided. **0** means user is locked, **1** means user is not locked.  | [optional] 
 **search** | **String**| Searches the nickname, email, role and homeDir fields for the provided value. Ignored if &#x60;username&#x60; is provided. Supports wildcard searches. | [optional] 
 **offset** | **Number**| Starting user record in the result set. Can be used for pagination. | [optional] 
 **sort** | **String**| Sort order or matching users. You can sort by multiple columns by separating sort options with a comma; the sort will be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.  Valid sort fields are: **nickname**, **username**, **email**, **homeDir** and **modified** | [optional] 
 **limit** | **Number**| Number of users to return. Can be used for pagination. | [optional] 
 **include** | **String**| Comma separated list of relationships to include in response. Valid options are **homeResource** and **ownerAccount**. | [optional] 

### Return type

[**UserCollectionResponse**](UserCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateUser

> UserResponse updateUser(id, evApiKey, evAccessToken, opts)

Update a user

Updates the settings for the user. Note that the unique key for this API call is our internal ID, and _not_ the username, as the username can be changed.  In the request body, you should only send the parameters for values that you wish to change for the user.  **Notes:**  - You must have [admin or master](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) access to edit other users. If you have user-level access, you can only update your own user settings. - You cannot edit a master user with this method.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.UsersApi();
let id = 2224; // Number | The user's ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method.
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'updateUserRequestBody': {"email":"testuser@example.com","expiration":"2011-03-21 00:18:56","homeResource":"/","locked":true,"nickname":"testnickname","onboarding":true,"password":"string","permissions":{"changePassword":true,"delete":true,"deleteFormData":true,"download":true,"list":true,"modify":true,"notification":true,"share":true,"upload":true,"viewFormData":true},"role":"user","timeZone":"America/Los_Angeles","username":"testuser"} // UpdateUserRequestBody | 
};
apiInstance.updateUser(id, evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **id** | **Number**| The user&#39;s ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method. | 
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **updateUserRequestBody** | [**UpdateUserRequestBody**](UpdateUserRequestBody.md)|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

