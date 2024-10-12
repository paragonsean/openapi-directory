# AgcoApi.UsersApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2UsersIdGet**](UsersApi.md#apiV2UsersIdGet) | **GET** /api/v2/Users/{id} | Get a specific user
[**usersDelete**](UsersApi.md#usersDelete) | **DELETE** /api/v2/Users/{id} | Delete a user
[**usersGet**](UsersApi.md#usersGet) | **GET** /api/v2/Users | Get users
[**usersGetCurrentUser**](UsersApi.md#usersGetCurrentUser) | **GET** /api/v2/Users/Current | Gets the current user
[**usersPost**](UsersApi.md#usersPost) | **POST** /api/v2/Users | Create a user
[**usersPut**](UsersApi.md#usersPut) | **PUT** /api/v2/Users/{id} | Update a user
[**usersPutCurrentUser**](UsersApi.md#usersPutCurrentUser) | **PUT** /api/v2/Users/Current | Update a user



## apiV2UsersIdGet

> APIModelsUser apiV2UsersIdGet(id)

Get a specific user

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UsersApi();
let id = 56; // Number | The user ID
apiInstance.apiV2UsersIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The user ID | 

### Return type

[**APIModelsUser**](APIModelsUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## usersDelete

> usersDelete(id)

Delete a user

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UsersApi();
let id = 56; // Number | The user id
apiInstance.usersDelete(id, (error, data, response) => {
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
 **id** | **Number**| The user id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersGet

> APIPagedResponseAPIModelsUser usersGet(opts)

Get users

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UsersApi();
let opts = {
  'username': "username_example", // String | Optional. Search by username. Supports beginning and ending wildcards (*).
  'email': "email_example", // String | Optional. Search by email. Supports beginning and ending wildcards (*).
  'name': "name_example", // String | Optional. Search by name. Supports beginning and ending wildcards (*).
  'hasRole': "hasRole_example", // String | Optional. Return only users having the provided role name.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
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
 **username** | **String**| Optional. Search by username. Supports beginning and ending wildcards (*). | [optional] 
 **email** | **String**| Optional. Search by email. Supports beginning and ending wildcards (*). | [optional] 
 **name** | **String**| Optional. Search by name. Supports beginning and ending wildcards (*). | [optional] 
 **hasRole** | **String**| Optional. Return only users having the provided role name. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseAPIModelsUser**](APIPagedResponseAPIModelsUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## usersGetCurrentUser

> APIModelsUser usersGetCurrentUser()

Gets the current user

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UsersApi();
apiInstance.usersGetCurrentUser((error, data, response) => {
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

[**APIModelsUser**](APIModelsUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## usersPost

> APIModelsUser usersPost(aPIModelsUser)

Create a user

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UsersApi();
let aPIModelsUser = new AgcoApi.APIModelsUser(); // APIModelsUser | The user to create.
apiInstance.usersPost(aPIModelsUser, (error, data, response) => {
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
 **aPIModelsUser** | [**APIModelsUser**](APIModelsUser.md)| The user to create. | 

### Return type

[**APIModelsUser**](APIModelsUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## usersPut

> usersPut(id, aPIModelsUser)

Update a user

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UsersApi();
let id = 56; // Number | The user id
let aPIModelsUser = new AgcoApi.APIModelsUser(); // APIModelsUser | The user
apiInstance.usersPut(id, aPIModelsUser, (error, data, response) => {
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
 **id** | **Number**| The user id | 
 **aPIModelsUser** | [**APIModelsUser**](APIModelsUser.md)| The user | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined


## usersPutCurrentUser

> usersPutCurrentUser(aPIModelsUser)

Update a user

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UsersApi();
let aPIModelsUser = new AgcoApi.APIModelsUser(); // APIModelsUser | The user
apiInstance.usersPutCurrentUser(aPIModelsUser, (error, data, response) => {
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
 **aPIModelsUser** | [**APIModelsUser**](APIModelsUser.md)| The user | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined

