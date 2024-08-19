# InstagramApi.RelationshipsApi

All URIs are relative to *https://api.instagram.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersSelfRequestedByGet**](RelationshipsApi.md#usersSelfRequestedByGet) | **GET** /users/self/requested-by | List the users who have requested this user&#39;s permission to follow.
[**usersUserIdFollowedByGet**](RelationshipsApi.md#usersUserIdFollowedByGet) | **GET** /users/{user-id}/followed-by | Get the list of users this user is followed by.
[**usersUserIdFollowsGet**](RelationshipsApi.md#usersUserIdFollowsGet) | **GET** /users/{user-id}/follows | Get the list of users this user follows.
[**usersUserIdRelationshipGet**](RelationshipsApi.md#usersUserIdRelationshipGet) | **GET** /users/{user-id}/relationship | Get information about a relationship to another user.
[**usersUserIdRelationshipPost**](RelationshipsApi.md#usersUserIdRelationshipPost) | **POST** /users/{user-id}/relationship | Modify the relationship between the current user and the target user.



## usersSelfRequestedByGet

> UsersInfoResponse usersSelfRequestedByGet()

List the users who have requested this user&#39;s permission to follow.

List the users who have requested this user&#39;s permission to follow.

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.RelationshipsApi();
apiInstance.usersSelfRequestedByGet((error, data, response) => {
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

[**UsersInfoResponse**](UsersInfoResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdFollowedByGet

> UsersPagingResponse usersUserIdFollowedByGet(userId)

Get the list of users this user is followed by.

Get the list of users this user is followed by. To get users followed by the owner of the access token, you can use **self** instead of the &#x60;user-id&#x60;. 

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.RelationshipsApi();
let userId = "userId_example"; // String | The ID of a user, or **self** to retrieve information about authenticated user.
apiInstance.usersUserIdFollowedByGet(userId, (error, data, response) => {
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
 **userId** | **String**| The ID of a user, or **self** to retrieve information about authenticated user. | 

### Return type

[**UsersPagingResponse**](UsersPagingResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdFollowsGet

> UsersPagingResponse usersUserIdFollowsGet(userId)

Get the list of users this user follows.

Get the list of users this user follows. To get follows of the owner of the access token, you can use **self** instead of the &#x60;user-id&#x60;. 

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.RelationshipsApi();
let userId = "userId_example"; // String | The ID of a user, or **self** to retrieve information about authenticated user.
apiInstance.usersUserIdFollowsGet(userId, (error, data, response) => {
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
 **userId** | **String**| The ID of a user, or **self** to retrieve information about authenticated user. | 

### Return type

[**UsersPagingResponse**](UsersPagingResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdRelationshipGet

> RelationshipResponse usersUserIdRelationshipGet(userId)

Get information about a relationship to another user.

Get information about a relationship to another user.

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.RelationshipsApi();
let userId = "userId_example"; // String | The ID of a user to get information about.
apiInstance.usersUserIdRelationshipGet(userId, (error, data, response) => {
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
 **userId** | **String**| The ID of a user to get information about. | 

### Return type

[**RelationshipResponse**](RelationshipResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdRelationshipPost

> RelationshipPostResponse usersUserIdRelationshipPost(userId, action)

Modify the relationship between the current user and the target user.

Modify the relationship between the current user and the target user.

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.RelationshipsApi();
let userId = "userId_example"; // String | The ID of the target user.
let action = "action_example"; // String | Type of action to apply for relationship with the user.
apiInstance.usersUserIdRelationshipPost(userId, action, (error, data, response) => {
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
 **userId** | **String**| The ID of the target user. | 
 **action** | **String**| Type of action to apply for relationship with the user. | 

### Return type

[**RelationshipPostResponse**](RelationshipPostResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

