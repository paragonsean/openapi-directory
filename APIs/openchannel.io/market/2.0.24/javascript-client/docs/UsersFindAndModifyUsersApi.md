# OpenChannelMarketApi.UsersFindAndModifyUsersApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersGet**](UsersFindAndModifyUsersApi.md#usersGet) | **GET** /users | Returns a paginated list of users
[**usersUserIdDelete**](UsersFindAndModifyUsersApi.md#usersUserIdDelete) | **DELETE** /users/{userId} | Removes a single user
[**usersUserIdGet**](UsersFindAndModifyUsersApi.md#usersUserIdGet) | **GET** /users/{userId} | Return a single user
[**usersUserIdPatch**](UsersFindAndModifyUsersApi.md#usersUserIdPatch) | **PATCH** /users/{userId} | Updates user fields
[**usersUserIdPost**](UsersFindAndModifyUsersApi.md#usersUserIdPost) | **POST** /users/{userId} | Updates a single user or adds the user if they don&#39;t exist



## usersGet

> UserPages usersGet(opts)

Returns a paginated list of users

- Results are paginated and the default is value is 100 if no limit is provided 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.UsersFindAndModifyUsersApi();
let opts = {
  'query': "query_example", // String | A query document. Example: {'name':'John'} matches all the users that have the name 'John'
  'sort': "sort_example", // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
  'pageNumber': 56, // Number | The result set page number to be returned
  'limit': 56 // Number | The maximum number of results to return per page
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
 **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;John&#39;} matches all the users that have the name &#39;John&#39; | [optional] 
 **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] 
 **pageNumber** | **Number**| The result set page number to be returned | [optional] 
 **limit** | **Number**| The maximum number of results to return per page | [optional] 

### Return type

[**UserPages**](UserPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## usersUserIdDelete

> usersUserIdDelete(userId)

Removes a single user

- Results are returned for the market provided within the basic authentication credentials 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.UsersFindAndModifyUsersApi();
let userId = "userId_example"; // String | The id of the user to be removed
apiInstance.usersUserIdDelete(userId, (error, data, response) => {
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
 **userId** | **String**| The id of the user to be removed | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersUserIdGet

> User usersUserIdGet(userId)

Return a single user

- Results are returned for the market provided within the basic authentication credentials 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.UsersFindAndModifyUsersApi();
let userId = "userId_example"; // String | The id of the user to be located
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
 **userId** | **String**| The id of the user to be located | 

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## usersUserIdPatch

> User usersUserIdPatch(userId, opts)

Updates user fields

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.UsersFindAndModifyUsersApi();
let userId = "userId_example"; // String | The id of the user to be updated
let opts = {
  'type': "type_example", // String | The type for this user
  'email': "email_example", // String | The user's email
  'username': "username_example", // String | The user's username
  'name': "name_example", // String | The user's name
  'customData': "customData_example" // String | A custom JSON object that you can create and attach to this record
};
apiInstance.usersUserIdPatch(userId, opts, (error, data, response) => {
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
 **userId** | **String**| The id of the user to be updated | 
 **type** | **String**| The type for this user | [optional] 
 **email** | **String**| The user&#39;s email | [optional] 
 **username** | **String**| The user&#39;s username | [optional] 
 **name** | **String**| The user&#39;s name | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## usersUserIdPost

> User usersUserIdPost(userId, opts)

Updates a single user or adds the user if they don&#39;t exist

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.UsersFindAndModifyUsersApi();
let userId = "userId_example"; // String | The id of the user to be updated
let opts = {
  'type': "type_example", // String | The type for this user
  'email': "email_example", // String | The user's email
  'username': "username_example", // String | The user's username
  'name': "name_example", // String | The user's name
  'customData': "customData_example" // String | A custom JSON object that you can create and attach to this record
};
apiInstance.usersUserIdPost(userId, opts, (error, data, response) => {
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
 **userId** | **String**| The id of the user to be updated | 
 **type** | **String**| The type for this user | [optional] 
 **email** | **String**| The user&#39;s email | [optional] 
 **username** | **String**| The user&#39;s username | [optional] 
 **name** | **String**| The user&#39;s name | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

