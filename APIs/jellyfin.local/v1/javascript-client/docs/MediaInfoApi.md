# JellyfinApi.MediaInfoApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**closeLiveStream**](MediaInfoApi.md#closeLiveStream) | **POST** /LiveStreams/Close | Closes a media source.
[**getBitrateTestBytes**](MediaInfoApi.md#getBitrateTestBytes) | **GET** /Playback/BitrateTest | Tests the network with a request with the size of the bitrate.
[**getPlaybackInfo**](MediaInfoApi.md#getPlaybackInfo) | **GET** /Items/{itemId}/PlaybackInfo | Gets live playback media info for an item.
[**getPostedPlaybackInfo**](MediaInfoApi.md#getPostedPlaybackInfo) | **POST** /Items/{itemId}/PlaybackInfo | Gets live playback media info for an item.
[**openLiveStream**](MediaInfoApi.md#openLiveStream) | **POST** /LiveStreams/Open | Opens a media source.



## closeLiveStream

> closeLiveStream(liveStreamId)

Closes a media source.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.MediaInfoApi();
let liveStreamId = "liveStreamId_example"; // String | The livestream id.
apiInstance.closeLiveStream(liveStreamId, (error, data, response) => {
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
 **liveStreamId** | **String**| The livestream id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBitrateTestBytes

> File getBitrateTestBytes(opts)

Tests the network with a request with the size of the bitrate.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.MediaInfoApi();
let opts = {
  'size': 102400 // Number | The bitrate. Defaults to 102400.
};
apiInstance.getBitrateTestBytes(opts, (error, data, response) => {
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
 **size** | **Number**| The bitrate. Defaults to 102400. | [optional] [default to 102400]

### Return type

**File**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPlaybackInfo

> PlaybackInfoResponse getPlaybackInfo(itemId, userId)

Gets live playback media info for an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.MediaInfoApi();
let itemId = "itemId_example"; // String | The item id.
let userId = "userId_example"; // String | The user id.
apiInstance.getPlaybackInfo(itemId, userId, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **userId** | **String**| The user id. | 

### Return type

[**PlaybackInfoResponse**](PlaybackInfoResponse.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPostedPlaybackInfo

> PlaybackInfoResponse getPostedPlaybackInfo(itemId, opts)

Gets live playback media info for an item.

For backwards compatibility parameters can be sent via Query or Body, with Query having higher precedence.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.MediaInfoApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'userId': "userId_example", // String | The user id.
  'maxStreamingBitrate': 56, // Number | The maximum streaming bitrate.
  'startTimeTicks': 789, // Number | The start time in ticks.
  'audioStreamIndex': 56, // Number | The audio stream index.
  'subtitleStreamIndex': 56, // Number | The subtitle stream index.
  'maxAudioChannels': 56, // Number | The maximum number of audio channels.
  'mediaSourceId': "mediaSourceId_example", // String | The media source id.
  'liveStreamId': "liveStreamId_example", // String | The livestream id.
  'autoOpenLiveStream': true, // Boolean | Whether to auto open the livestream.
  'enableDirectPlay': true, // Boolean | Whether to enable direct play. Default: true.
  'enableDirectStream': true, // Boolean | Whether to enable direct stream. Default: true.
  'enableTranscoding': true, // Boolean | Whether to enable transcoding. Default: true.
  'allowVideoStreamCopy': true, // Boolean | Whether to allow to copy the video stream. Default: true.
  'allowAudioStreamCopy': true, // Boolean | Whether to allow to copy the audio stream. Default: true.
  'playbackInfoDto': new JellyfinApi.PlaybackInfoDto() // PlaybackInfoDto | The playback info.
};
apiInstance.getPostedPlaybackInfo(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **userId** | **String**| The user id. | [optional] 
 **maxStreamingBitrate** | **Number**| The maximum streaming bitrate. | [optional] 
 **startTimeTicks** | **Number**| The start time in ticks. | [optional] 
 **audioStreamIndex** | **Number**| The audio stream index. | [optional] 
 **subtitleStreamIndex** | **Number**| The subtitle stream index. | [optional] 
 **maxAudioChannels** | **Number**| The maximum number of audio channels. | [optional] 
 **mediaSourceId** | **String**| The media source id. | [optional] 
 **liveStreamId** | **String**| The livestream id. | [optional] 
 **autoOpenLiveStream** | **Boolean**| Whether to auto open the livestream. | [optional] 
 **enableDirectPlay** | **Boolean**| Whether to enable direct play. Default: true. | [optional] 
 **enableDirectStream** | **Boolean**| Whether to enable direct stream. Default: true. | [optional] 
 **enableTranscoding** | **Boolean**| Whether to enable transcoding. Default: true. | [optional] 
 **allowVideoStreamCopy** | **Boolean**| Whether to allow to copy the video stream. Default: true. | [optional] 
 **allowAudioStreamCopy** | **Boolean**| Whether to allow to copy the audio stream. Default: true. | [optional] 
 **playbackInfoDto** | [**PlaybackInfoDto**](PlaybackInfoDto.md)| The playback info. | [optional] 

### Return type

[**PlaybackInfoResponse**](PlaybackInfoResponse.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## openLiveStream

> LiveStreamResponse openLiveStream(opts)

Opens a media source.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.MediaInfoApi();
let opts = {
  'openToken': "openToken_example", // String | The open token.
  'userId': "userId_example", // String | The user id.
  'playSessionId': "playSessionId_example", // String | The play session id.
  'maxStreamingBitrate': 56, // Number | The maximum streaming bitrate.
  'startTimeTicks': 789, // Number | The start time in ticks.
  'audioStreamIndex': 56, // Number | The audio stream index.
  'subtitleStreamIndex': 56, // Number | The subtitle stream index.
  'maxAudioChannels': 56, // Number | The maximum number of audio channels.
  'itemId': "itemId_example", // String | The item id.
  'enableDirectPlay': true, // Boolean | Whether to enable direct play. Default: true.
  'enableDirectStream': true, // Boolean | Whether to enable direct stream. Default: true.
  'openLiveStreamDto': new JellyfinApi.OpenLiveStreamDto() // OpenLiveStreamDto | The open live stream dto.
};
apiInstance.openLiveStream(opts, (error, data, response) => {
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
 **openToken** | **String**| The open token. | [optional] 
 **userId** | **String**| The user id. | [optional] 
 **playSessionId** | **String**| The play session id. | [optional] 
 **maxStreamingBitrate** | **Number**| The maximum streaming bitrate. | [optional] 
 **startTimeTicks** | **Number**| The start time in ticks. | [optional] 
 **audioStreamIndex** | **Number**| The audio stream index. | [optional] 
 **subtitleStreamIndex** | **Number**| The subtitle stream index. | [optional] 
 **maxAudioChannels** | **Number**| The maximum number of audio channels. | [optional] 
 **itemId** | **String**| The item id. | [optional] 
 **enableDirectPlay** | **Boolean**| Whether to enable direct play. Default: true. | [optional] 
 **enableDirectStream** | **Boolean**| Whether to enable direct stream. Default: true. | [optional] 
 **openLiveStreamDto** | [**OpenLiveStreamDto**](OpenLiveStreamDto.md)| The open live stream dto. | [optional] 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

