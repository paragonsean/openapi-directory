# SliceboxApi.UsersApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersCurrentGet**](UsersApi.md#usersCurrentGet) | **GET** /users/current | 
[**usersGet**](UsersApi.md#usersGet) | **GET** /users | 
[**usersIdDelete**](UsersApi.md#usersIdDelete) | **DELETE** /users/{id} | 
[**usersLoginPost**](UsersApi.md#usersLoginPost) | **POST** /users/login | 
[**usersLogoutPost**](UsersApi.md#usersLogoutPost) | **POST** /users/logout | 
[**usersPost**](UsersApi.md#usersPost) | **POST** /users | 



## usersCurrentGet

> UserInfo usersCurrentGet()



obtain information on the currently logged in user as specified by the supplied session cookie, IP address and user agent.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.UsersApi();
apiInstance.usersCurrentGet((error, data, response) => {
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

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## usersGet

> [User] usersGet(opts)



Returns all users of slicebox

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.UsersApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of users
  'count': 20 // Number | size of returned slice of users
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
 **startindex** | **Number**| start index of returned slice of users | [optional] [default to 0]
 **count** | **Number**| size of returned slice of users | [optional] [default to 20]

### Return type

[**[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## usersIdDelete

> usersIdDelete(id)



deletes a single user based on the ID supplied

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.UsersApi();
let id = 789; // Number | ID of user to delete
apiInstance.usersIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of user to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersLoginPost

> usersLoginPost(userPass)



Obtain a session cookie that can be used to authenticate future API calls from the present IP address and with the present user agent.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.UsersApi();
let userPass = new SliceboxApi.UserPass(); // UserPass | username and password for user logging in
apiInstance.usersLoginPost(userPass, (error, data, response) => {
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
 **userPass** | [**UserPass**](UserPass.md)| username and password for user logging in | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined


## usersLogoutPost

> usersLogoutPost()



Logout the current user by responding with a delete cookie header removing the session cookie for this user.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.UsersApi();
apiInstance.usersLogoutPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersPost

> User usersPost(user)



Creates a new user. Dupicates are accepted but not added.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.UsersApi();
let user = new SliceboxApi.NewUser(); // NewUser | User to add
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
 **user** | [**NewUser**](NewUser.md)| User to add | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream

