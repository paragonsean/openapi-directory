# Vimeo.VideosUploadApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**completeStreamingUpload**](VideosUploadApi.md#completeStreamingUpload) | **DELETE** /users/{user_id}/uploads/{upload} | Complete a user&#39;s streaming upload
[**getUploadAttempt**](VideosUploadApi.md#getUploadAttempt) | **GET** /users/{user_id}/uploads/{upload} | Get a user&#39;s upload attempt
[**uploadVideo**](VideosUploadApi.md#uploadVideo) | **POST** /users/{user_id}/videos | Upload a video
[**uploadVideoAlt1**](VideosUploadApi.md#uploadVideoAlt1) | **POST** /me/videos | Upload a video



## completeStreamingUpload

> completeStreamingUpload(upload, userId, signature, videoFileId)

Complete a user&#39;s streaming upload

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.VideosUploadApi();
let upload = 12345; // Number | The ID of the upload attempt.
let userId = 152184; // Number | The ID of the user.
let signature = "cd89a20adde7a608f3331e71c37bdfa087bacbf3"; // String | The crypto signature of the completed upload.
let videoFileId = 1234; // Number | The ID of the uploaded file.
apiInstance.completeStreamingUpload(upload, userId, signature, videoFileId, (error, data, response) => {
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
 **upload** | **Number**| The ID of the upload attempt. | 
 **userId** | **Number**| The ID of the user. | 
 **signature** | **String**| The crypto signature of the completed upload. | 
 **videoFileId** | **Number**| The ID of the uploaded file. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUploadAttempt

> UploadAttempt getUploadAttempt(upload, userId)

Get a user&#39;s upload attempt

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.VideosUploadApi();
let upload = 12345; // Number | The ID of the upload attempt.
let userId = 152184; // Number | The ID of the user.
apiInstance.getUploadAttempt(upload, userId, (error, data, response) => {
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
 **upload** | **Number**| The ID of the upload attempt. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

[**UploadAttempt**](UploadAttempt.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.uploadattempt+json


## uploadVideo

> Video uploadVideo(userId, uploadVideoAlt1Request)

Upload a video

Begin the video upload process. For more information, see our [upload documentation](https://developer.vimeo.com/api/upload/videos).

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.VideosUploadApi();
let userId = 152184; // Number | The ID of the user.
let uploadVideoAlt1Request = new Vimeo.UploadVideoAlt1Request(); // UploadVideoAlt1Request | 
apiInstance.uploadVideo(userId, uploadVideoAlt1Request, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **uploadVideoAlt1Request** | [**UploadVideoAlt1Request**](UploadVideoAlt1Request.md)|  | 

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.video+json
- **Accept**: application/vnd.vimeo.video+json


## uploadVideoAlt1

> Video uploadVideoAlt1(uploadVideoAlt1Request)

Upload a video

Begin the video upload process. For more information, see our [upload documentation](https://developer.vimeo.com/api/upload/videos).

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.VideosUploadApi();
let uploadVideoAlt1Request = new Vimeo.UploadVideoAlt1Request(); // UploadVideoAlt1Request | 
apiInstance.uploadVideoAlt1(uploadVideoAlt1Request, (error, data, response) => {
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
 **uploadVideoAlt1Request** | [**UploadVideoAlt1Request**](UploadVideoAlt1Request.md)|  | 

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.video+json
- **Accept**: application/vnd.vimeo.video+json

