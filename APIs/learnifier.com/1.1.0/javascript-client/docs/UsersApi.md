# Learnifier.UsersApi

All URIs are relative to *http://learnifier.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extparticipationGet**](UsersApi.md#extparticipationGet) | **GET** /extparticipation | Gets a participation by external id
[**extuserGet**](UsersApi.md#extuserGet) | **GET** /extuser | Gets a user by external id
[**usersGet**](UsersApi.md#usersGet) | **GET** /users | Lists all users
[**usersPost**](UsersApi.md#usersPost) | **POST** /users | Adds a user
[**usersUseridGet**](UsersApi.md#usersUseridGet) | **GET** /users/{userid} | User information
[**usersUseridPatch**](UsersApi.md#usersUseridPatch) | **PATCH** /users/{userid} | Updates user information
[**usersUseridPickeyAPIKEYGet**](UsersApi.md#usersUseridPickeyAPIKEYGet) | **GET** /users/{userid}/pic?key&#x3D;{APIKEY} | User profile picture
[**usersUseridProjectParticipationsGet**](UsersApi.md#usersUseridProjectParticipationsGet) | **GET** /users/{userid}/projectParticipations | Returns information about the projects the user is a participant in.



## extparticipationGet

> Participation extparticipationGet(extid)

Gets a participation by external id

Gets a participation by external id.

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UsersApi();
let extid = "extid_example"; // String | The external id of the participation
apiInstance.extparticipationGet(extid, (error, data, response) => {
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
 **extid** | **String**| The external id of the participation | 

### Return type

[**Participation**](Participation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extuserGet

> User extuserGet(extid)

Gets a user by external id

Gets a user by external id.

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UsersApi();
let extid = "extid_example"; // String | The external id of the user
apiInstance.extuserGet(extid, (error, data, response) => {
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
 **extid** | **String**| The external id of the user | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGet

> [UserWithPermissions] usersGet(opts)

Lists all users

Lists all users. Only api callers that have full access can call this method.

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UsersApi();
let opts = {
  'limit': 5000, // Number | The maximum number of users to return
  'offset': 0 // Number | The offset to start listing users from
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
 **limit** | **Number**| The maximum number of users to return | [optional] [default to 5000]
 **offset** | **Number**| The offset to start listing users from | [optional] [default to 0]

### Return type

[**[UserWithPermissions]**](UserWithPermissions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersPost

> AddUserResponse usersPost(body)

Adds a user

Adds a user. No two users can have the same email address. Email is saved WITH case but compared regardless of case. Email can be changed for a user assuming it doesn&#39;t cause a conflict.

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UsersApi();
let body = new Learnifier.AddUser(); // AddUser | 
apiInstance.usersPost(body, (error, data, response) => {
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
 **body** | [**AddUser**](AddUser.md)|  | 

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUseridGet

> User usersUseridGet(userid)

User information

Returns information about a user 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UsersApi();
let userid = "userid_example"; // String | A user id
apiInstance.usersUseridGet(userid, (error, data, response) => {
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
 **userid** | **String**| A user id | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUseridPatch

> usersUseridPatch(userid, body)

Updates user information

Updates a user. All values that have a key defined in the input will be set. So if a value should not be updated omit it totally from the input, otherwise it will be unset.

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UsersApi();
let userid = "userid_example"; // String | The user id
let body = new Learnifier.AddUser(); // AddUser | 
apiInstance.usersUseridPatch(userid, body, (error, data, response) => {
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
 **userid** | **String**| The user id | 
 **body** | [**AddUser**](AddUser.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUseridPickeyAPIKEYGet

> usersUseridPickeyAPIKEYGet(userid, APIKEY)

User profile picture

Returns a thumbnail picture of the user. This can either be a selected picture or an auto generated image. This method doesn&#39;t require a full sign in. The api key is sufficient. The image is square and is likely, but not necessary, to be in 128x128 PNG format. However the format will always be either PNG, JPEG or GIF. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UsersApi();
let userid = "userid_example"; // String | The user id
let APIKEY = "APIKEY_example"; // String | 
apiInstance.usersUseridPickeyAPIKEYGet(userid, APIKEY, (error, data, response) => {
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
 **userid** | **String**| The user id | 
 **APIKEY** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUseridProjectParticipationsGet

> UserParticipationInfo usersUseridProjectParticipationsGet(userid)

Returns information about the projects the user is a participant in.

Returns information about the projects the user is a participant in. Only the projects that the current token have access to will be listed. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UsersApi();
let userid = "userid_example"; // String | A user id
apiInstance.usersUseridProjectParticipationsGet(userid, (error, data, response) => {
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
 **userid** | **String**| A user id | 

### Return type

[**UserParticipationInfo**](UserParticipationInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

