# UsersOktaApi.DefaultApi

All URIs are relative to *http://okta.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clearUserSessions**](DefaultApi.md#clearUserSessions) | **DELETE** /api/v1/users/{userId}/sessions | Clear User Sessions
[**findUser**](DefaultApi.md#findUser) | **GET** /api/v1/users | Find User
[**getAssignedAppLinks**](DefaultApi.md#getAssignedAppLinks) | **GET** /api/v1/users/{userId}/appLinks | Get Assigned App Links
[**getCurrentUser**](DefaultApi.md#getCurrentUser) | **GET** /api/v1/users/me | Get Current User
[**getGroupsForUser**](DefaultApi.md#getGroupsForUser) | **GET** /api/v1/users/{userId}/groups | Get Groups for User
[**getUser**](DefaultApi.md#getUser) | **GET** /api/v1/users/{userId} | Get User
[**resetFactors**](DefaultApi.md#resetFactors) | **POST** /api/v1/users/{userId}/lifecycle/reset_factors | Reset Factors



## clearUserSessions

> clearUserSessions(userId)

Clear User Sessions

Clear User Sessions

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.DefaultApi();
let userId = "userId_example"; // String | 
apiInstance.clearUserSessions(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: Not defined


## findUser

> findUser(opts)

Find User

Find User

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.DefaultApi();
let opts = {
  'q': "user" // String | 
};
apiInstance.findUser(opts, (error, data, response) => {
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
 **q** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: Not defined


## getAssignedAppLinks

> getAssignedAppLinks(userId)

Get Assigned App Links

Get Assigned App Links

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.DefaultApi();
let userId = "userId_example"; // String | 
apiInstance.getAssignedAppLinks(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: Not defined


## getCurrentUser

> getCurrentUser()

Get Current User

Get Current User

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.DefaultApi();
apiInstance.getCurrentUser((error, data, response) => {
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

- **Content-Type**: application/octet-stream
- **Accept**: Not defined


## getGroupsForUser

> getGroupsForUser(userId)

Get Groups for User

Get Groups for User

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.DefaultApi();
let userId = "userId_example"; // String | 
apiInstance.getGroupsForUser(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: Not defined


## getUser

> getUser(userId)

Get User

Get User

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.DefaultApi();
let userId = "userId_example"; // String | 
apiInstance.getUser(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: Not defined


## resetFactors

> resetFactors(userId)

Reset Factors

Reset Factors

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.DefaultApi();
let userId = "userId_example"; // String | 
apiInstance.resetFactors(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: Not defined

