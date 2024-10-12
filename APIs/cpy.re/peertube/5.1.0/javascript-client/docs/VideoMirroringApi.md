# PeerTube.VideoMirroringApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delMirroredVideo**](VideoMirroringApi.md#delMirroredVideo) | **DELETE** /api/v1/server/redundancy/videos/{redundancyId} | Delete a mirror done on a video
[**getMirroredVideos**](VideoMirroringApi.md#getMirroredVideos) | **GET** /api/v1/server/redundancy/videos | List videos being mirrored
[**putMirroredVideo**](VideoMirroringApi.md#putMirroredVideo) | **POST** /api/v1/server/redundancy/videos | Mirror a video



## delMirroredVideo

> delMirroredVideo(redundancyId)

Delete a mirror done on a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoMirroringApi();
let redundancyId = "redundancyId_example"; // String | id of an existing redundancy on a video
apiInstance.delMirroredVideo(redundancyId, (error, data, response) => {
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
 **redundancyId** | **String**| id of an existing redundancy on a video | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMirroredVideos

> [VideoRedundancy] getMirroredVideos(target, opts)

List videos being mirrored

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoMirroringApi();
let target = "target_example"; // String | direction of the mirror
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "sort_example" // String | Sort abuses by criteria
};
apiInstance.getMirroredVideos(target, opts, (error, data, response) => {
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
 **target** | **String**| direction of the mirror | 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort abuses by criteria | [optional] 

### Return type

[**[VideoRedundancy]**](VideoRedundancy.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putMirroredVideo

> putMirroredVideo(opts)

Mirror a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoMirroringApi();
let opts = {
  'putMirroredVideoRequest': new PeerTube.PutMirroredVideoRequest() // PutMirroredVideoRequest | 
};
apiInstance.putMirroredVideo(opts, (error, data, response) => {
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
 **putMirroredVideoRequest** | [**PutMirroredVideoRequest**](PutMirroredVideoRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

