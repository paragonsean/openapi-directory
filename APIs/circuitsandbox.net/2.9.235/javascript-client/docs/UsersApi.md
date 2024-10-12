# RestApiVersion2.UsersApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLabel**](UsersApi.md#getLabel) | **GET** /users/labels | Returns all user labels
[**getPresence**](UsersApi.md#getPresence) | **GET** /users/presence | Gets the presence status
[**getProfile**](UsersApi.md#getProfile) | **GET** /users/profile | Gets the authenticated user&#39;s profile information
[**getSupportInfo**](UsersApi.md#getSupportInfo) | **GET** /users/supportinfo | Gets the support information
[**getUserByEmailAddress**](UsersApi.md#getUserByEmailAddress) | **GET** /users/{emailAddress}/getUserByEmail | Get user by email
[**getUserById**](UsersApi.md#getUserById) | **GET** /users/{id} | Gets the user&#39;s profile information
[**getUserPresence**](UsersApi.md#getUserPresence) | **GET** /users/{id}/presence | Gets the presence status
[**searchUser**](UsersApi.md#searchUser) | **GET** /users | Search for users
[**searchUsersList**](UsersApi.md#searchUsersList) | **GET** /users/list | Search multiple users.
[**setUserPresence**](UsersApi.md#setUserPresence) | **PUT** /users/presence | Updates the presence status



## getLabel

> [Label] getLabel()

Returns all user labels

Returns all labels of the user that were defined either explicit or implicit via assignment to conversations. OauthScopes: READ_USER_PROFILE, ORGANIZE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.UsersApi();
apiInstance.getLabel((error, data, response) => {
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

[**[Label]**](Label.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getPresence

> [Presence] getPresence(userIds)

Gets the presence status

Gets the presence status of the users whose IDs or email addresses are given. OauthScopes: READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.UsersApi();
let userIds = ["null"]; // [String] | A list of unique user IDs or email addresses of the users you want to query the presence state for
apiInstance.getPresence(userIds, (error, data, response) => {
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
 **userIds** | [**[String]**](String.md)| A list of unique user IDs or email addresses of the users you want to query the presence state for | 

### Return type

[**[Presence]**](Presence.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getProfile

> User getProfile()

Gets the authenticated user&#39;s profile information

Gets the authenticated user&#39;s profile information. OauthScopes: READ_USER_PROFILE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.UsersApi();
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

[**User**](User.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getSupportInfo

> SupportInfo getSupportInfo()

Gets the support information

Gets the support information for the tenant of the requesting user OauthScopes: READ_USER_PROFILE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.UsersApi();
apiInstance.getSupportInfo((error, data, response) => {
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

[**SupportInfo**](SupportInfo.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getUserByEmailAddress

> User getUserByEmailAddress(emailAddress, opts)

Get user by email

Get user by first or secondary email address OauthScopes: READ_USER_PROFILE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.UsersApi();
let emailAddress = "emailAddress_example"; // String | The main or secondary email address of a user.
let opts = {
  'secondaryLookup': true // Boolean | secondaryLookup enabled (default = false)
};
apiInstance.getUserByEmailAddress(emailAddress, opts, (error, data, response) => {
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
 **emailAddress** | **String**| The main or secondary email address of a user. | 
 **secondaryLookup** | **Boolean**| secondaryLookup enabled (default &#x3D; false) | [optional] 

### Return type

[**User**](User.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getUserById

> User getUserById(id)

Gets the user&#39;s profile information

Gets the profile information of the user with the given ID. OauthScopes: READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.UsersApi();
let id = "id_example"; // String | The unique ID or the email address of the user to fetch
apiInstance.getUserById(id, (error, data, response) => {
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
 **id** | **String**| The unique ID or the email address of the user to fetch | 

### Return type

[**User**](User.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getUserPresence

> Presence getUserPresence(id)

Gets the presence status

Gets the presence status of the users whose ID or email address is given. OauthScopes: READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.UsersApi();
let id = "id_example"; // String | The unique ID or the email address of the user to fetch.
apiInstance.getUserPresence(id, (error, data, response) => {
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
 **id** | **String**| The unique ID or the email address of the user to fetch. | 

### Return type

[**Presence**](Presence.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## searchUser

> [User] searchUser(name)

Search for users

Search for users based on an email address or username OauthScopes: READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.UsersApi();
let name = "name_example"; // String | Search for a user by name
apiInstance.searchUser(name, (error, data, response) => {
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
 **name** | **String**| Search for a user by name | 

### Return type

[**[User]**](User.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## searchUsersList

> [User] searchUsersList(name, opts)

Search multiple users.

Search multiple users given by id or email address. OauthScopes: READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.UsersApi();
let name = ["null"]; // [String] | Multiple email addresses or UUIDs.
let opts = {
  'returnFullUserInfo': false, // Boolean | Boolean, return full user info?
  'secondaryLookup': false // Boolean | Boolean, lookup secondary email?
};
apiInstance.searchUsersList(name, opts, (error, data, response) => {
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
 **name** | [**[String]**](String.md)| Multiple email addresses or UUIDs. | 
 **returnFullUserInfo** | **Boolean**| Boolean, return full user info? | [optional] [default to false]
 **secondaryLookup** | **Boolean**| Boolean, lookup secondary email? | [optional] [default to false]

### Return type

[**[User]**](User.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## setUserPresence

> Presence setUserPresence(state, opts)

Updates the presence status

Updates the presence status of the authenticated user. OauthScopes: WRITE_USER_PROFILE, MANAGE_PRESENCE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.UsersApi();
let state = "state_example"; // String | The user's presence.
let opts = {
  'clearDND': false, // Boolean | Clear the DND of the user.
  'dndUntil': new Date("2013-10-20T19:20:30+01:00"), // Date | Timestamp until the DND state of the user is active. This field is mandatory when the state is set to DND.
  'statusMessage': "statusMessage_example" // String | An optional status message that is displayed instead of the location
};
apiInstance.setUserPresence(state, opts, (error, data, response) => {
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
 **state** | **String**| The user&#39;s presence. | 
 **clearDND** | **Boolean**| Clear the DND of the user. | [optional] [default to false]
 **dndUntil** | **Date**| Timestamp until the DND state of the user is active. This field is mandatory when the state is set to DND. | [optional] 
 **statusMessage** | **String**| An optional status message that is displayed instead of the location | [optional] 

### Return type

[**Presence**](Presence.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

