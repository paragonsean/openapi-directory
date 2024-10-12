# Vimeo.VideosTextTracksApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTextTrack**](VideosTextTracksApi.md#createTextTrack) | **POST** /videos/{video_id}/texttracks | Add a text track to a video
[**createTextTrackAlt1**](VideosTextTracksApi.md#createTextTrackAlt1) | **POST** /channels/{channel_id}/videos/{video_id}/texttracks | Add a text track to a video
[**deleteTextTrack**](VideosTextTracksApi.md#deleteTextTrack) | **DELETE** /videos/{video_id}/texttracks/{texttrack_id} | Delete a text track
[**editTextTrack**](VideosTextTracksApi.md#editTextTrack) | **PATCH** /videos/{video_id}/texttracks/{texttrack_id} | Edit a text track
[**getTextTrack**](VideosTextTracksApi.md#getTextTrack) | **GET** /videos/{video_id}/texttracks/{texttrack_id} | Get a specific text track
[**getTextTracks**](VideosTextTracksApi.md#getTextTracks) | **GET** /videos/{video_id}/texttracks | Get all the text tracks of a video
[**getTextTracksAlt1**](VideosTextTracksApi.md#getTextTracksAlt1) | **GET** /channels/{channel_id}/videos/{video_id}/texttracks | Get all the text tracks of a video



## createTextTrack

> TextTrack createTextTrack(videoId, createTextTrackAlt1Request)

Add a text track to a video

For additional information, see our [text track upload guide](https://developer.vimeo.com/api/upload/texttracks).

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

let apiInstance = new Vimeo.VideosTextTracksApi();
let videoId = 258684937; // Number | The ID of the video.
let createTextTrackAlt1Request = new Vimeo.CreateTextTrackAlt1Request(); // CreateTextTrackAlt1Request | 
apiInstance.createTextTrack(videoId, createTextTrackAlt1Request, (error, data, response) => {
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
 **createTextTrackAlt1Request** | [**CreateTextTrackAlt1Request**](CreateTextTrackAlt1Request.md)|  | 

### Return type

[**TextTrack**](TextTrack.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.video.texttrack+json
- **Accept**: application/vnd.vimeo.video.texttrack+json


## createTextTrackAlt1

> TextTrack createTextTrackAlt1(channelId, videoId, createTextTrackAlt1Request)

Add a text track to a video

For additional information, see our [text track upload guide](https://developer.vimeo.com/api/upload/texttracks).

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

let apiInstance = new Vimeo.VideosTextTracksApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
let createTextTrackAlt1Request = new Vimeo.CreateTextTrackAlt1Request(); // CreateTextTrackAlt1Request | 
apiInstance.createTextTrackAlt1(channelId, videoId, createTextTrackAlt1Request, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **videoId** | **Number**| The ID of the video. | 
 **createTextTrackAlt1Request** | [**CreateTextTrackAlt1Request**](CreateTextTrackAlt1Request.md)|  | 

### Return type

[**TextTrack**](TextTrack.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.video.texttrack+json
- **Accept**: application/vnd.vimeo.video.texttrack+json


## deleteTextTrack

> deleteTextTrack(texttrackId, videoId)

Delete a text track

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

let apiInstance = new Vimeo.VideosTextTracksApi();
let texttrackId = 12345; // Number | The ID of the text track.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.deleteTextTrack(texttrackId, videoId, (error, data, response) => {
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
 **texttrackId** | **Number**| The ID of the text track. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video.texttrack+json


## editTextTrack

> TextTrack editTextTrack(texttrackId, videoId, opts)

Edit a text track

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

let apiInstance = new Vimeo.VideosTextTracksApi();
let texttrackId = 12345; // Number | The ID of the text track.
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'editTextTrackRequest': new Vimeo.EditTextTrackRequest() // EditTextTrackRequest | 
};
apiInstance.editTextTrack(texttrackId, videoId, opts, (error, data, response) => {
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
 **texttrackId** | **Number**| The ID of the text track. | 
 **videoId** | **Number**| The ID of the video. | 
 **editTextTrackRequest** | [**EditTextTrackRequest**](EditTextTrackRequest.md)|  | [optional] 

### Return type

[**TextTrack**](TextTrack.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.video.texttrack+json
- **Accept**: application/vnd.vimeo.video.texttrack+json


## getTextTrack

> TextTrack getTextTrack(texttrackId, videoId)

Get a specific text track

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

let apiInstance = new Vimeo.VideosTextTracksApi();
let texttrackId = 12345; // Number | The ID of the text track.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.getTextTrack(texttrackId, videoId, (error, data, response) => {
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
 **texttrackId** | **Number**| The ID of the text track. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**TextTrack**](TextTrack.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video.texttrack+json


## getTextTracks

> [TextTrack] getTextTracks(videoId)

Get all the text tracks of a video

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

let apiInstance = new Vimeo.VideosTextTracksApi();
let videoId = 258684937; // Number | The ID of the video.
apiInstance.getTextTracks(videoId, (error, data, response) => {
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

### Return type

[**[TextTrack]**](TextTrack.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video.texttrack+json


## getTextTracksAlt1

> [TextTrack] getTextTracksAlt1(channelId, videoId)

Get all the text tracks of a video

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

let apiInstance = new Vimeo.VideosTextTracksApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.getTextTracksAlt1(channelId, videoId, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**[TextTrack]**](TextTrack.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video.texttrack+json

