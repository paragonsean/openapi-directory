# PendoFeedbackApi.UserApi

All URIs are relative to *https://api.feedback.eu.pendo.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersGet**](UserApi.md#usersGet) | **GET** /users | fetch User records
[**usersIdDelete**](UserApi.md#usersIdDelete) | **DELETE** /users/{id} | Delete a User
[**usersIdGet**](UserApi.md#usersIdGet) | **GET** /users/{id} | Get a User record
[**usersIdPut**](UserApi.md#usersIdPut) | **PUT** /users/{id} | Update a User
[**usersIdTagsDelete**](UserApi.md#usersIdTagsDelete) | **DELETE** /users/{id}/tags | Delete custom User tags
[**usersIdTagsGet**](UserApi.md#usersIdTagsGet) | **GET** /users/{id}/tags | Get custom User tags
[**usersIdTagsPost**](UserApi.md#usersIdTagsPost) | **POST** /users/{id}/tags | Overwrite current custom User tags with the given tags
[**usersInviteEndUserPost**](UserApi.md#usersInviteEndUserPost) | **POST** /users/invite_end_user | Invite an EndUser (customer)
[**usersInviteVendorUserPost**](UserApi.md#usersInviteVendorUserPost) | **POST** /users/invite_vendor_user | Invite a VendorUser (Team member)
[**usersPost**](UserApi.md#usersPost) | **POST** /users | Ping to create or update an EndUser and Account in one call
[**usersSearchGet**](UserApi.md#usersSearchGet) | **GET** /users/search | Find a User with a query
[**vendorUsersPost**](UserApi.md#vendorUsersPost) | **POST** /vendor_users | Create or update a team member by their external_id



## usersGet

> [User] usersGet(role, opts)

fetch User records

get a list of User records

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.UserApi();
let role = "role_example"; // String | role
let opts = {
  'account': 56, // Number | Filter by Account ID, if supplied. Only useful if role param is endUser
  'start': 0, // Number | Offset to start at
  'limit': 300, // Number | Limit the number of records returned. Max value can be 300. If limit is set to more than 300 the api will return an error
  'orderBy': "orderBy_example", // String | The field to use for sort
  'orderDir': "orderDir_example" // String | The sort direction
};
apiInstance.usersGet(role, opts, (error, data, response) => {
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
 **role** | **String**| role | 
 **account** | **Number**| Filter by Account ID, if supplied. Only useful if role param is endUser | [optional] 
 **start** | **Number**| Offset to start at | [optional] [default to 0]
 **limit** | **Number**| Limit the number of records returned. Max value can be 300. If limit is set to more than 300 the api will return an error | [optional] [default to 300]
 **orderBy** | **String**| The field to use for sort | [optional] 
 **orderDir** | **String**| The sort direction | [optional] 

### Return type

[**[User]**](User.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdDelete

> User usersIdDelete(id)

Delete a User

This removes most traces of a User&#39;s existence from the system. For an EndUser you might want to consider just letting them churn after a period of inactivity.

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.UserApi();
let id = 3.4; // Number | 
apiInstance.usersIdDelete(id, (error, data, response) => {
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

[**User**](User.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdGet

> User usersIdGet(id)

Get a User record

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.UserApi();
let id = 3.4; // Number | 
apiInstance.usersIdGet(id, (error, data, response) => {
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

[**User**](User.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdPut

> User usersIdPut(id, opts)

Update a User

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.UserApi();
let id = 3.4; // Number | Feedback's User ID
let opts = {
  'user': new PendoFeedbackApi.UsersIdPutRequest() // UsersIdPutRequest | 
};
apiInstance.usersIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| Feedback&#39;s User ID | 
 **user** | [**UsersIdPutRequest**](UsersIdPutRequest.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdTagsDelete

> usersIdTagsDelete(id)

Delete custom User tags

Removes all custom tags associated with the User

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.UserApi();
let id = 3.4; // Number | Feedback's User ID
apiInstance.usersIdTagsDelete(id, (error, data, response) => {
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
 **id** | **Number**| Feedback&#39;s User ID | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersIdTagsGet

> usersIdTagsGet(id)

Get custom User tags

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.UserApi();
let id = 3.4; // Number | Feedback's User ID
apiInstance.usersIdTagsGet(id, (error, data, response) => {
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
 **id** | **Number**| Feedback&#39;s User ID | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersIdTagsPost

> usersIdTagsPost(id, tags)

Overwrite current custom User tags with the given tags

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.UserApi();
let id = 3.4; // Number | Feedback's User ID
let tags = {key: null}; // Object | An array of maps specifying tags under each tag group, for example:  [  {'impacts' => ['sales']},  {'resources' => ['dev', 'test', 'support']}  ]
apiInstance.usersIdTagsPost(id, tags, (error, data, response) => {
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
 **id** | **Number**| Feedback&#39;s User ID | 
 **tags** | **Object**| An array of maps specifying tags under each tag group, for example:  [  {&#39;impacts&#39; &#x3D;&gt; [&#39;sales&#39;]},  {&#39;resources&#39; &#x3D;&gt; [&#39;dev&#39;, &#39;test&#39;, &#39;support&#39;]}  ] | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersInviteEndUserPost

> usersInviteEndUserPost(data)

Invite an EndUser (customer)

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.UserApi();
let data = new PendoFeedbackApi.UsersInviteEndUserPostRequest(); // UsersInviteEndUserPostRequest | 
apiInstance.usersInviteEndUserPost(data, (error, data, response) => {
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
 **data** | [**UsersInviteEndUserPostRequest**](UsersInviteEndUserPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersInviteVendorUserPost

> usersInviteVendorUserPost(data)

Invite a VendorUser (Team member)

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.UserApi();
let data = new PendoFeedbackApi.UsersInviteVendorUserPostRequest(); // UsersInviteVendorUserPostRequest | 
apiInstance.usersInviteVendorUserPost(data, (error, data, response) => {
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
 **data** | [**UsersInviteVendorUserPostRequest**](UsersInviteVendorUserPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## usersPost

> usersPost(data)

Ping to create or update an EndUser and Account in one call

Replicates much of the functionality of the widget ping, allowing callers to create or update User records for End Users. If you call this with a new User and/or Account, the record will be created. If you call for an existing User/Account, the record will be updated. You can also call this at EndUser login time, or more frequently, to notify Feedback that the EndUser has been seen. This keeps Feedback&#39;s &#39;last seen&#39; data fresh and updates your reporting. This endpoint is used by our Zapier integration. The only value allowed in user.roles is &#39;endUser&#39;. The id you supply here for the User and Account should be your own unique id, which Feedback calls external_id. This probably isn&#39;t the same as Feedback&#39;s id seen elsewhere in the API.

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.UserApi();
let data = new PendoFeedbackApi.EndUserPing(); // EndUserPing | the account and user
apiInstance.usersPost(data, (error, data, response) => {
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
 **data** | [**EndUserPing**](EndUserPing.md)| the account and user | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## usersSearchGet

> User usersSearchGet(opts)

Find a User with a query

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.UserApi();
let opts = {
  'externalId': "externalId_example", // String | Find using your external ID, rather than the ID generated by Feedback
  'email': "email_example", // String | Find user by their email address. Role param must be specified when using this option
  'role': "role_example" // String | Users role ('vendorUser' or 'endUser'). Only useful when finding a user by their email address
};
apiInstance.usersSearchGet(opts, (error, data, response) => {
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
 **externalId** | **String**| Find using your external ID, rather than the ID generated by Feedback | [optional] 
 **email** | **String**| Find user by their email address. Role param must be specified when using this option | [optional] 
 **role** | **String**| Users role (&#39;vendorUser&#39; or &#39;endUser&#39;). Only useful when finding a user by their email address | [optional] 

### Return type

[**User**](User.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vendorUsersPost

> vendorUsersPost(data)

Create or update a team member by their external_id

the POST /vendor_users is very similar to the POST /users/invite_vendor_user but /vendor_users is intended for consumers to refresh team member data periodically, rather than just a one-off user creation.

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.UserApi();
let data = new PendoFeedbackApi.VendorUsersPostRequest(); // VendorUsersPostRequest | 
apiInstance.vendorUsersPost(data, (error, data, response) => {
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
 **data** | [**VendorUsersPostRequest**](VendorUsersPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

