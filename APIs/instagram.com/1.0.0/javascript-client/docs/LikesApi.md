# InstagramApi.LikesApi

All URIs are relative to *https://api.instagram.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediaMediaIdLikesDelete**](LikesApi.md#mediaMediaIdLikesDelete) | **DELETE** /media/{media-id}/likes | Remove a like on this media by the current user.
[**mediaMediaIdLikesGet**](LikesApi.md#mediaMediaIdLikesGet) | **GET** /media/{media-id}/likes | Get a list of users who have liked this media.
[**mediaMediaIdLikesPost**](LikesApi.md#mediaMediaIdLikesPost) | **POST** /media/{media-id}/likes | Set a like on this media by the current user.



## mediaMediaIdLikesDelete

> StatusResponse mediaMediaIdLikesDelete(mediaId)

Remove a like on this media by the current user.

Remove a like on this media by the currently authenticated user.

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

let apiInstance = new InstagramApi.LikesApi();
let mediaId = "mediaId_example"; // String | The ID of the media resource.
apiInstance.mediaMediaIdLikesDelete(mediaId, (error, data, response) => {
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
 **mediaId** | **String**| The ID of the media resource. | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaMediaIdLikesGet

> UsersInfoResponse mediaMediaIdLikesGet(mediaId)

Get a list of users who have liked this media.

Get a list of users who have liked this media.

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

let apiInstance = new InstagramApi.LikesApi();
let mediaId = "mediaId_example"; // String | The ID of the media resource.
apiInstance.mediaMediaIdLikesGet(mediaId, (error, data, response) => {
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
 **mediaId** | **String**| The ID of the media resource. | 

### Return type

[**UsersInfoResponse**](UsersInfoResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaMediaIdLikesPost

> StatusResponse mediaMediaIdLikesPost(mediaId)

Set a like on this media by the current user.

Set a like on this media by the currently authenticated user.

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

let apiInstance = new InstagramApi.LikesApi();
let mediaId = "mediaId_example"; // String | The ID of the media resource.
apiInstance.mediaMediaIdLikesPost(mediaId, (error, data, response) => {
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
 **mediaId** | **String**| The ID of the media resource. | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

