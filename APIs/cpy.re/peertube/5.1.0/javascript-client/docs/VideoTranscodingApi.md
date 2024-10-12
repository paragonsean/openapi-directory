# PeerTube.VideoTranscodingApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1VideosIdStudioEditPost**](VideoTranscodingApi.md#apiV1VideosIdStudioEditPost) | **POST** /api/v1/videos/{id}/studio/edit | Create a studio task
[**createVideoTranscoding**](VideoTranscodingApi.md#createVideoTranscoding) | **POST** /api/v1/videos/{id}/transcoding | Create a transcoding job



## apiV1VideosIdStudioEditPost

> apiV1VideosIdStudioEditPost(id)

Create a studio task

Create a task to edit a video  (cut, add intro/outro etc)

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoTranscodingApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.apiV1VideosIdStudioEditPost(id, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## createVideoTranscoding

> createVideoTranscoding(id, opts)

Create a transcoding job

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoTranscodingApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let opts = {
  'createVideoTranscodingRequest': new PeerTube.CreateVideoTranscodingRequest() // CreateVideoTranscodingRequest | 
};
apiInstance.createVideoTranscoding(id, opts, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 
 **createVideoTranscodingRequest** | [**CreateVideoTranscodingRequest**](CreateVideoTranscodingRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

