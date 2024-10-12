# InstagramApi.UsersApi

All URIs are relative to *https://api.instagram.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersSearchGet**](UsersApi.md#usersSearchGet) | **GET** /users/search | Search for a user by name.
[**usersSelfFeedGet**](UsersApi.md#usersSelfFeedGet) | **GET** /users/self/feed | See the authenticated user&#39;s feed.
[**usersSelfMediaLikedGet**](UsersApi.md#usersSelfMediaLikedGet) | **GET** /users/self/media/liked | See the list of media liked by the authenticated user.
[**usersUserIdGet**](UsersApi.md#usersUserIdGet) | **GET** /users/{user-id} | Get basic information about a user.
[**usersUserIdMediaRecentGet**](UsersApi.md#usersUserIdMediaRecentGet) | **GET** /users/{user-id}/media/recent | Get the most recent media published by a user.



## usersSearchGet

> UsersInfoResponse usersSearchGet(q, opts)

Search for a user by name.

Search for a user by name.

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

let apiInstance = new InstagramApi.UsersApi();
let q = "q_example"; // String | A query string.
let opts = {
  'count': 56 // Number | Number of users to return.
};
apiInstance.usersSearchGet(q, opts, (error, data, response) => {
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
 **q** | **String**| A query string. | 
 **count** | **Number**| Number of users to return. | [optional] 

### Return type

[**UsersInfoResponse**](UsersInfoResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersSelfFeedGet

> MediaListResponse usersSelfFeedGet(opts)

See the authenticated user&#39;s feed.

See the authenticated user&#39;s feed.  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015 

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

let apiInstance = new InstagramApi.UsersApi();
let opts = {
  'count': 56, // Number | Count of media to return.
  'minId': "minId_example", // String | Return media later than this `min_id`.
  'maxId': "maxId_example" // String | Return media earlier than this `max_id`.
};
apiInstance.usersSelfFeedGet(opts, (error, data, response) => {
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
 **count** | **Number**| Count of media to return. | [optional] 
 **minId** | **String**| Return media later than this &#x60;min_id&#x60;. | [optional] 
 **maxId** | **String**| Return media earlier than this &#x60;max_id&#x60;. | [optional] 

### Return type

[**MediaListResponse**](MediaListResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersSelfMediaLikedGet

> MediaListResponse usersSelfMediaLikedGet(opts)

See the list of media liked by the authenticated user.

See the list of media liked by the authenticated user. Private media is returned as long as the authenticated user has permission to view that media. Liked media lists are only available for the currently authenticated user. 

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

let apiInstance = new InstagramApi.UsersApi();
let opts = {
  'count': 56, // Number | Count of media to return.
  'maxLikeId': "maxLikeId_example" // String | Return media liked before this id.
};
apiInstance.usersSelfMediaLikedGet(opts, (error, data, response) => {
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
 **count** | **Number**| Count of media to return. | [optional] 
 **maxLikeId** | **String**| Return media liked before this id. | [optional] 

### Return type

[**MediaListResponse**](MediaListResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdGet

> UserResponse usersUserIdGet(userId)

Get basic information about a user.

Get basic information about a user. To get information about the owner of the access token, you can use **self** instead of the &#x60;user-id&#x60;.  Security scope &#x60;public_content&#x60; is required to read information about other users. 

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

let apiInstance = new InstagramApi.UsersApi();
let userId = "userId_example"; // String | The ID of a user to get information about, or **self** to retrieve information about authenticated user.
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
 **userId** | **String**| The ID of a user to get information about, or **self** to retrieve information about authenticated user. | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdMediaRecentGet

> MediaListResponse usersUserIdMediaRecentGet(userId, opts)

Get the most recent media published by a user.

Get the most recent media published by a user. To get the most recent media published by the owner of the access token, you can use **self** instead of the &#x60;user-id&#x60;.  Security scope &#x60;public_content&#x60; is required to read information about other users. 

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

let apiInstance = new InstagramApi.UsersApi();
let userId = "userId_example"; // String | The ID of a user to get recent media of, or **self** to retrieve media of authenticated user.
let opts = {
  'count': 56, // Number | Count of media to return.
  'maxTimestamp': 789, // Number | Return media before this UNIX timestamp.
  'minTimestamp': 789, // Number | Return media after this UNIX timestamp.
  'minId': "minId_example", // String | Return media later than this `min_id`.
  'maxId': "maxId_example" // String | Return media earlier than this `max_id`.
};
apiInstance.usersUserIdMediaRecentGet(userId, opts, (error, data, response) => {
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
 **userId** | **String**| The ID of a user to get recent media of, or **self** to retrieve media of authenticated user. | 
 **count** | **Number**| Count of media to return. | [optional] 
 **maxTimestamp** | **Number**| Return media before this UNIX timestamp. | [optional] 
 **minTimestamp** | **Number**| Return media after this UNIX timestamp. | [optional] 
 **minId** | **String**| Return media later than this &#x60;min_id&#x60;. | [optional] 
 **maxId** | **String**| Return media earlier than this &#x60;max_id&#x60;. | [optional] 

### Return type

[**MediaListResponse**](MediaListResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

