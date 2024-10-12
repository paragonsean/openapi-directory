# JellyfinApi.UniversalAudioApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUniversalAudioStream**](UniversalAudioApi.md#getUniversalAudioStream) | **GET** /Audio/{itemId}/universal | Gets an audio stream.
[**headUniversalAudioStream**](UniversalAudioApi.md#headUniversalAudioStream) | **HEAD** /Audio/{itemId}/universal | Gets an audio stream.



## getUniversalAudioStream

> File getUniversalAudioStream(itemId, opts)

Gets an audio stream.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.UniversalAudioApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'container': ["null"], // [String] | Optional. The audio container.
  'mediaSourceId': "mediaSourceId_example", // String | The media version id, if playing an alternate version.
  'deviceId': "deviceId_example", // String | The device id of the client requesting. Used to stop encoding processes when needed.
  'userId': "userId_example", // String | Optional. The user id.
  'audioCodec': "audioCodec_example", // String | Optional. The audio codec to transcode to.
  'maxAudioChannels': 56, // Number | Optional. The maximum number of audio channels.
  'transcodingAudioChannels': 56, // Number | Optional. The number of how many audio channels to transcode to.
  'maxStreamingBitrate': 56, // Number | Optional. The maximum streaming bitrate.
  'audioBitRate': 56, // Number | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
  'startTimeTicks': 789, // Number | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
  'transcodingContainer': "transcodingContainer_example", // String | Optional. The container to transcode to.
  'transcodingProtocol': "transcodingProtocol_example", // String | Optional. The transcoding protocol.
  'maxAudioSampleRate': 56, // Number | Optional. The maximum audio sample rate.
  'maxAudioBitDepth': 56, // Number | Optional. The maximum audio bit depth.
  'enableRemoteMedia': true, // Boolean | Optional. Whether to enable remote media.
  'breakOnNonKeyFrames': true, // Boolean | Optional. Whether to break on non key frames.
  'enableRedirection': true // Boolean | Whether to enable redirection. Defaults to true.
};
apiInstance.getUniversalAudioStream(itemId, opts, (error, data, response) => {
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
 **container** | [**[String]**](String.md)| Optional. The audio container. | [optional] 
 **mediaSourceId** | **String**| The media version id, if playing an alternate version. | [optional] 
 **deviceId** | **String**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **userId** | **String**| Optional. The user id. | [optional] 
 **audioCodec** | **String**| Optional. The audio codec to transcode to. | [optional] 
 **maxAudioChannels** | **Number**| Optional. The maximum number of audio channels. | [optional] 
 **transcodingAudioChannels** | **Number**| Optional. The number of how many audio channels to transcode to. | [optional] 
 **maxStreamingBitrate** | **Number**| Optional. The maximum streaming bitrate. | [optional] 
 **audioBitRate** | **Number**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **startTimeTicks** | **Number**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **transcodingContainer** | **String**| Optional. The container to transcode to. | [optional] 
 **transcodingProtocol** | **String**| Optional. The transcoding protocol. | [optional] 
 **maxAudioSampleRate** | **Number**| Optional. The maximum audio sample rate. | [optional] 
 **maxAudioBitDepth** | **Number**| Optional. The maximum audio bit depth. | [optional] 
 **enableRemoteMedia** | **Boolean**| Optional. Whether to enable remote media. | [optional] 
 **breakOnNonKeyFrames** | **Boolean**| Optional. Whether to break on non key frames. | [optional] 
 **enableRedirection** | **Boolean**| Whether to enable redirection. Defaults to true. | [optional] [default to true]

### Return type

**File**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/*


## headUniversalAudioStream

> File headUniversalAudioStream(itemId, opts)

Gets an audio stream.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.UniversalAudioApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'container': ["null"], // [String] | Optional. The audio container.
  'mediaSourceId': "mediaSourceId_example", // String | The media version id, if playing an alternate version.
  'deviceId': "deviceId_example", // String | The device id of the client requesting. Used to stop encoding processes when needed.
  'userId': "userId_example", // String | Optional. The user id.
  'audioCodec': "audioCodec_example", // String | Optional. The audio codec to transcode to.
  'maxAudioChannels': 56, // Number | Optional. The maximum number of audio channels.
  'transcodingAudioChannels': 56, // Number | Optional. The number of how many audio channels to transcode to.
  'maxStreamingBitrate': 56, // Number | Optional. The maximum streaming bitrate.
  'audioBitRate': 56, // Number | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
  'startTimeTicks': 789, // Number | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
  'transcodingContainer': "transcodingContainer_example", // String | Optional. The container to transcode to.
  'transcodingProtocol': "transcodingProtocol_example", // String | Optional. The transcoding protocol.
  'maxAudioSampleRate': 56, // Number | Optional. The maximum audio sample rate.
  'maxAudioBitDepth': 56, // Number | Optional. The maximum audio bit depth.
  'enableRemoteMedia': true, // Boolean | Optional. Whether to enable remote media.
  'breakOnNonKeyFrames': true, // Boolean | Optional. Whether to break on non key frames.
  'enableRedirection': true // Boolean | Whether to enable redirection. Defaults to true.
};
apiInstance.headUniversalAudioStream(itemId, opts, (error, data, response) => {
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
 **container** | [**[String]**](String.md)| Optional. The audio container. | [optional] 
 **mediaSourceId** | **String**| The media version id, if playing an alternate version. | [optional] 
 **deviceId** | **String**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **userId** | **String**| Optional. The user id. | [optional] 
 **audioCodec** | **String**| Optional. The audio codec to transcode to. | [optional] 
 **maxAudioChannels** | **Number**| Optional. The maximum number of audio channels. | [optional] 
 **transcodingAudioChannels** | **Number**| Optional. The number of how many audio channels to transcode to. | [optional] 
 **maxStreamingBitrate** | **Number**| Optional. The maximum streaming bitrate. | [optional] 
 **audioBitRate** | **Number**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **startTimeTicks** | **Number**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **transcodingContainer** | **String**| Optional. The container to transcode to. | [optional] 
 **transcodingProtocol** | **String**| Optional. The transcoding protocol. | [optional] 
 **maxAudioSampleRate** | **Number**| Optional. The maximum audio sample rate. | [optional] 
 **maxAudioBitDepth** | **Number**| Optional. The maximum audio bit depth. | [optional] 
 **enableRemoteMedia** | **Boolean**| Optional. Whether to enable remote media. | [optional] 
 **breakOnNonKeyFrames** | **Boolean**| Optional. Whether to break on non key frames. | [optional] 
 **enableRedirection** | **Boolean**| Whether to enable redirection. Defaults to true. | [optional] [default to true]

### Return type

**File**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/*

