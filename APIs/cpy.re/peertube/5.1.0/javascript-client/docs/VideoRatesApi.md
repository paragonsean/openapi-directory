# PeerTube.VideoRatesApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1UsersMeVideosVideoIdRatingGet_0**](VideoRatesApi.md#apiV1UsersMeVideosVideoIdRatingGet_0) | **GET** /api/v1/users/me/videos/{videoId}/rating | Get rate of my user for a video
[**apiV1VideosIdRatePut**](VideoRatesApi.md#apiV1VideosIdRatePut) | **PUT** /api/v1/videos/{id}/rate | Like/dislike a video



## apiV1UsersMeVideosVideoIdRatingGet_0

> GetMeVideoRating apiV1UsersMeVideosVideoIdRatingGet_0(videoId)

Get rate of my user for a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoRatesApi();
let videoId = 56; // Number | The video id
apiInstance.apiV1UsersMeVideosVideoIdRatingGet_0(videoId, (error, data, response) => {
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
 **videoId** | **Number**| The video id | 

### Return type

[**GetMeVideoRating**](GetMeVideoRating.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1VideosIdRatePut

> apiV1VideosIdRatePut(id, opts)

Like/dislike a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoRatesApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let opts = {
  'apiV1VideosIdRatePutRequest': new PeerTube.ApiV1VideosIdRatePutRequest() // ApiV1VideosIdRatePutRequest | 
};
apiInstance.apiV1VideosIdRatePut(id, opts, (error, data, response) => {
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
 **apiV1VideosIdRatePutRequest** | [**ApiV1VideosIdRatePutRequest**](ApiV1VideosIdRatePutRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

