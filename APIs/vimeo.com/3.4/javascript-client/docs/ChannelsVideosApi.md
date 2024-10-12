# Vimeo.ChannelsVideosApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoToChannel**](ChannelsVideosApi.md#addVideoToChannel) | **PUT** /channels/{channel_id}/videos/{video_id} | Add a specific video to a channel
[**addVideosToChannel**](ChannelsVideosApi.md#addVideosToChannel) | **PUT** /channels/{channel_id}/videos | Add a list of videos to a channel
[**deleteVideoFromChannel**](ChannelsVideosApi.md#deleteVideoFromChannel) | **DELETE** /channels/{channel_id}/videos/{video_id} | Remove a specific video from a channel
[**getAvailableVideoChannels**](ChannelsVideosApi.md#getAvailableVideoChannels) | **GET** /videos/{video_id}/available_channels | Get all the channels to which a user can add or remove a specific video
[**getChannelVideo**](ChannelsVideosApi.md#getChannelVideo) | **GET** /channels/{channel_id}/videos/{video_id} | Get a specific video in a channel
[**getChannelVideos**](ChannelsVideosApi.md#getChannelVideos) | **GET** /channels/{channel_id}/videos | Get all the videos in a channel
[**removeVideosFromChannel**](ChannelsVideosApi.md#removeVideosFromChannel) | **DELETE** /channels/{channel_id}/videos | Remove a list of videos from a channel



## addVideoToChannel

> addVideoToChannel(channelId, videoId)

Add a specific video to a channel

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

let apiInstance = new Vimeo.ChannelsVideosApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.addVideoToChannel(channelId, videoId, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addVideosToChannel

> addVideosToChannel(channelId, addVideosToChannelRequest)

Add a list of videos to a channel

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

let apiInstance = new Vimeo.ChannelsVideosApi();
let channelId = 927; // Number | The ID of the channel.
let addVideosToChannelRequest = new Vimeo.AddVideosToChannelRequest(); // AddVideosToChannelRequest | 
apiInstance.addVideosToChannel(channelId, addVideosToChannelRequest, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **addVideosToChannelRequest** | [**AddVideosToChannelRequest**](AddVideosToChannelRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteVideoFromChannel

> deleteVideoFromChannel(channelId, videoId)

Remove a specific video from a channel

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

let apiInstance = new Vimeo.ChannelsVideosApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.deleteVideoFromChannel(channelId, videoId, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAvailableVideoChannels

> [Channel] getAvailableVideoChannels(videoId)

Get all the channels to which a user can add or remove a specific video

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

let apiInstance = new Vimeo.ChannelsVideosApi();
let videoId = 258684937; // Number | The ID of the video.
apiInstance.getAvailableVideoChannels(videoId, (error, data, response) => {
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

[**[Channel]**](Channel.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.channel+json


## getChannelVideo

> Video getChannelVideo(channelId, videoId)

Get a specific video in a channel

This method returns a specific video in a channel. You can use it to determine whether the video is in the channel.

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

let apiInstance = new Vimeo.ChannelsVideosApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.getChannelVideo(channelId, videoId, (error, data, response) => {
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

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## getChannelVideos

> [Video] getChannelVideos(channelId, opts)

Get all the videos in a channel

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

let apiInstance = new Vimeo.ChannelsVideosApi();
let channelId = 927; // Number | The ID of the channel.
let opts = {
  'containingUri': "/videos/258684937", // String | The page that contains the video URI.
  'direction': "asc", // String | The sort direction of the results.
  'filter': "filter_example", // String | The attribute by which to filter the results.
  'filterEmbeddable': true, // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'query': "Stop motion", // String | The search query to use to filter the results.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getChannelVideos(channelId, opts, (error, data, response) => {
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
 **containingUri** | **String**| The page that contains the video URI. | [optional] 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **filter** | **String**| The attribute by which to filter the results. | [optional] 
 **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **query** | **String**| The search query to use to filter the results. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[Video]**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## removeVideosFromChannel

> Video removeVideosFromChannel(channelId, removeVideosFromChannelRequest)

Remove a list of videos from a channel

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

let apiInstance = new Vimeo.ChannelsVideosApi();
let channelId = 927; // Number | The ID of the channel.
let removeVideosFromChannelRequest = new Vimeo.RemoveVideosFromChannelRequest(); // RemoveVideosFromChannelRequest | 
apiInstance.removeVideosFromChannel(channelId, removeVideosFromChannelRequest, (error, data, response) => {
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
 **removeVideosFromChannelRequest** | [**RemoveVideosFromChannelRequest**](RemoveVideosFromChannelRequest.md)|  | 

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

