# JellyfinApi.HlsSegmentApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHlsAudioSegmentLegacyAac**](HlsSegmentApi.md#getHlsAudioSegmentLegacyAac) | **GET** /Audio/{itemId}/hls/{segmentId}/stream.aac | Gets the specified audio segment for an audio item.
[**getHlsAudioSegmentLegacyMp3**](HlsSegmentApi.md#getHlsAudioSegmentLegacyMp3) | **GET** /Audio/{itemId}/hls/{segmentId}/stream.mp3 | Gets the specified audio segment for an audio item.
[**getHlsPlaylistLegacy**](HlsSegmentApi.md#getHlsPlaylistLegacy) | **GET** /Videos/{itemId}/hls/{playlistId}/stream.m3u8 | Gets a hls video playlist.
[**getHlsVideoSegmentLegacy**](HlsSegmentApi.md#getHlsVideoSegmentLegacy) | **GET** /Videos/{itemId}/hls/{playlistId}/{segmentId}.{segmentContainer} | Gets a hls video segment.
[**stopEncodingProcess**](HlsSegmentApi.md#stopEncodingProcess) | **DELETE** /Videos/ActiveEncodings | Stops an active encoding.



## getHlsAudioSegmentLegacyAac

> File getHlsAudioSegmentLegacyAac(itemId, segmentId)

Gets the specified audio segment for an audio item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.HlsSegmentApi();
let itemId = "itemId_example"; // String | The item id.
let segmentId = "segmentId_example"; // String | The segment id.
apiInstance.getHlsAudioSegmentLegacyAac(itemId, segmentId, (error, data, response) => {
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
 **segmentId** | **String**| The segment id. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/*


## getHlsAudioSegmentLegacyMp3

> File getHlsAudioSegmentLegacyMp3(itemId, segmentId)

Gets the specified audio segment for an audio item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.HlsSegmentApi();
let itemId = "itemId_example"; // String | The item id.
let segmentId = "segmentId_example"; // String | The segment id.
apiInstance.getHlsAudioSegmentLegacyMp3(itemId, segmentId, (error, data, response) => {
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
 **segmentId** | **String**| The segment id. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/*


## getHlsPlaylistLegacy

> File getHlsPlaylistLegacy(itemId, playlistId)

Gets a hls video playlist.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.HlsSegmentApi();
let itemId = "itemId_example"; // String | The video id.
let playlistId = "playlistId_example"; // String | The playlist id.
apiInstance.getHlsPlaylistLegacy(itemId, playlistId, (error, data, response) => {
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
 **itemId** | **String**| The video id. | 
 **playlistId** | **String**| The playlist id. | 

### Return type

**File**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/x-mpegURL


## getHlsVideoSegmentLegacy

> File getHlsVideoSegmentLegacy(itemId, playlistId, segmentId, segmentContainer)

Gets a hls video segment.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.HlsSegmentApi();
let itemId = "itemId_example"; // String | The item id.
let playlistId = "playlistId_example"; // String | The playlist id.
let segmentId = "segmentId_example"; // String | The segment id.
let segmentContainer = "segmentContainer_example"; // String | The segment container.
apiInstance.getHlsVideoSegmentLegacy(itemId, playlistId, segmentId, segmentContainer, (error, data, response) => {
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
 **playlistId** | **String**| The playlist id. | 
 **segmentId** | **String**| The segment id. | 
 **segmentContainer** | **String**| The segment container. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: video/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## stopEncodingProcess

> stopEncodingProcess(opts)

Stops an active encoding.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.HlsSegmentApi();
let opts = {
  'deviceId': "deviceId_example", // String | The device id of the client requesting. Used to stop encoding processes when needed.
  'playSessionId': "playSessionId_example" // String | The play session id.
};
apiInstance.stopEncodingProcess(opts, (error, data, response) => {
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
 **deviceId** | **String**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **playSessionId** | **String**| The play session id. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

