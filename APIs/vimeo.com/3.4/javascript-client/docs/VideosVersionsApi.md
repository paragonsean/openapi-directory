# Vimeo.VideosVersionsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createVideoVersion**](VideosVersionsApi.md#createVideoVersion) | **POST** /videos/{video_id}/versions | Add a version to a video



## createVideoVersion

> VideoVersions createVideoVersion(videoId, createVideoVersionRequest)

Add a version to a video

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

let apiInstance = new Vimeo.VideosVersionsApi();
let videoId = 258684937; // Number | The ID of the video.
let createVideoVersionRequest = new Vimeo.CreateVideoVersionRequest(); // CreateVideoVersionRequest | 
apiInstance.createVideoVersion(videoId, createVideoVersionRequest, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 
 **createVideoVersionRequest** | [**CreateVideoVersionRequest**](CreateVideoVersionRequest.md)|  | 

### Return type

[**VideoVersions**](VideoVersions.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.video.version+json
- **Accept**: application/vnd.vimeo.video.version+json

