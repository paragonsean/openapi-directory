# JellyfinApi.PlaystateApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**markPlayedItem**](PlaystateApi.md#markPlayedItem) | **POST** /Users/{userId}/PlayedItems/{itemId} | Marks an item as played for user.
[**markUnplayedItem**](PlaystateApi.md#markUnplayedItem) | **DELETE** /Users/{userId}/PlayedItems/{itemId} | Marks an item as unplayed for user.
[**onPlaybackProgress**](PlaystateApi.md#onPlaybackProgress) | **POST** /Users/{userId}/PlayingItems/{itemId}/Progress | Reports a user&#39;s playback progress.
[**onPlaybackStart**](PlaystateApi.md#onPlaybackStart) | **POST** /Users/{userId}/PlayingItems/{itemId} | Reports that a user has begun playing an item.
[**onPlaybackStopped**](PlaystateApi.md#onPlaybackStopped) | **DELETE** /Users/{userId}/PlayingItems/{itemId} | Reports that a user has stopped playing an item.
[**pingPlaybackSession**](PlaystateApi.md#pingPlaybackSession) | **POST** /Sessions/Playing/Ping | Pings a playback session.
[**reportPlaybackProgress**](PlaystateApi.md#reportPlaybackProgress) | **POST** /Sessions/Playing/Progress | Reports playback progress within a session.
[**reportPlaybackStart**](PlaystateApi.md#reportPlaybackStart) | **POST** /Sessions/Playing | Reports playback has started within a session.
[**reportPlaybackStopped**](PlaystateApi.md#reportPlaybackStopped) | **POST** /Sessions/Playing/Stopped | Reports playback has stopped within a session.



## markPlayedItem

> UserItemDataDto markPlayedItem(userId, itemId, opts)

Marks an item as played for user.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaystateApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
let opts = {
  'datePlayed': new Date("2013-10-20T19:20:30+01:00") // Date | Optional. The date the item was played.
};
apiInstance.markPlayedItem(userId, itemId, opts, (error, data, response) => {
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
 **userId** | **String**| User id. | 
 **itemId** | **String**| Item id. | 
 **datePlayed** | **Date**| Optional. The date the item was played. | [optional] 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## markUnplayedItem

> UserItemDataDto markUnplayedItem(userId, itemId)

Marks an item as unplayed for user.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaystateApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
apiInstance.markUnplayedItem(userId, itemId, (error, data, response) => {
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
 **userId** | **String**| User id. | 
 **itemId** | **String**| Item id. | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## onPlaybackProgress

> onPlaybackProgress(userId, itemId, opts)

Reports a user&#39;s playback progress.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaystateApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
let opts = {
  'mediaSourceId': "mediaSourceId_example", // String | The id of the MediaSource.
  'positionTicks': 789, // Number | Optional. The current position, in ticks. 1 tick = 10000 ms.
  'audioStreamIndex': 56, // Number | The audio stream index.
  'subtitleStreamIndex': 56, // Number | The subtitle stream index.
  'volumeLevel': 56, // Number | Scale of 0-100.
  'playMethod': new JellyfinApi.PlayMethod(), // PlayMethod | The play method.
  'liveStreamId': "liveStreamId_example", // String | The live stream id.
  'playSessionId': "playSessionId_example", // String | The play session id.
  'repeatMode': new JellyfinApi.RepeatMode(), // RepeatMode | The repeat mode.
  'isPaused': false, // Boolean | Indicates if the player is paused.
  'isMuted': false // Boolean | Indicates if the player is muted.
};
apiInstance.onPlaybackProgress(userId, itemId, opts, (error, data, response) => {
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
 **userId** | **String**| User id. | 
 **itemId** | **String**| Item id. | 
 **mediaSourceId** | **String**| The id of the MediaSource. | [optional] 
 **positionTicks** | **Number**| Optional. The current position, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **audioStreamIndex** | **Number**| The audio stream index. | [optional] 
 **subtitleStreamIndex** | **Number**| The subtitle stream index. | [optional] 
 **volumeLevel** | **Number**| Scale of 0-100. | [optional] 
 **playMethod** | [**PlayMethod**](.md)| The play method. | [optional] 
 **liveStreamId** | **String**| The live stream id. | [optional] 
 **playSessionId** | **String**| The play session id. | [optional] 
 **repeatMode** | [**RepeatMode**](.md)| The repeat mode. | [optional] 
 **isPaused** | **Boolean**| Indicates if the player is paused. | [optional] [default to false]
 **isMuted** | **Boolean**| Indicates if the player is muted. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## onPlaybackStart

> onPlaybackStart(userId, itemId, opts)

Reports that a user has begun playing an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaystateApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
let opts = {
  'mediaSourceId': "mediaSourceId_example", // String | The id of the MediaSource.
  'audioStreamIndex': 56, // Number | The audio stream index.
  'subtitleStreamIndex': 56, // Number | The subtitle stream index.
  'playMethod': new JellyfinApi.PlayMethod(), // PlayMethod | The play method.
  'liveStreamId': "liveStreamId_example", // String | The live stream id.
  'playSessionId': "playSessionId_example", // String | The play session id.
  'canSeek': false // Boolean | Indicates if the client can seek.
};
apiInstance.onPlaybackStart(userId, itemId, opts, (error, data, response) => {
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
 **userId** | **String**| User id. | 
 **itemId** | **String**| Item id. | 
 **mediaSourceId** | **String**| The id of the MediaSource. | [optional] 
 **audioStreamIndex** | **Number**| The audio stream index. | [optional] 
 **subtitleStreamIndex** | **Number**| The subtitle stream index. | [optional] 
 **playMethod** | [**PlayMethod**](.md)| The play method. | [optional] 
 **liveStreamId** | **String**| The live stream id. | [optional] 
 **playSessionId** | **String**| The play session id. | [optional] 
 **canSeek** | **Boolean**| Indicates if the client can seek. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## onPlaybackStopped

> onPlaybackStopped(userId, itemId, opts)

Reports that a user has stopped playing an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaystateApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
let opts = {
  'mediaSourceId': "mediaSourceId_example", // String | The id of the MediaSource.
  'nextMediaType': "nextMediaType_example", // String | The next media type that will play.
  'positionTicks': 789, // Number | Optional. The position, in ticks, where playback stopped. 1 tick = 10000 ms.
  'liveStreamId': "liveStreamId_example", // String | The live stream id.
  'playSessionId': "playSessionId_example" // String | The play session id.
};
apiInstance.onPlaybackStopped(userId, itemId, opts, (error, data, response) => {
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
 **userId** | **String**| User id. | 
 **itemId** | **String**| Item id. | 
 **mediaSourceId** | **String**| The id of the MediaSource. | [optional] 
 **nextMediaType** | **String**| The next media type that will play. | [optional] 
 **positionTicks** | **Number**| Optional. The position, in ticks, where playback stopped. 1 tick &#x3D; 10000 ms. | [optional] 
 **liveStreamId** | **String**| The live stream id. | [optional] 
 **playSessionId** | **String**| The play session id. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## pingPlaybackSession

> pingPlaybackSession(opts)

Pings a playback session.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaystateApi();
let opts = {
  'playSessionId': "playSessionId_example" // String | Playback session id.
};
apiInstance.pingPlaybackSession(opts, (error, data, response) => {
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
 **playSessionId** | **String**| Playback session id. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reportPlaybackProgress

> reportPlaybackProgress(opts)

Reports playback progress within a session.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaystateApi();
let opts = {
  'playbackProgressInfo': new JellyfinApi.PlaybackProgressInfo() // PlaybackProgressInfo | The playback progress info.
};
apiInstance.reportPlaybackProgress(opts, (error, data, response) => {
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
 **playbackProgressInfo** | [**PlaybackProgressInfo**](PlaybackProgressInfo.md)| The playback progress info. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## reportPlaybackStart

> reportPlaybackStart(opts)

Reports playback has started within a session.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaystateApi();
let opts = {
  'playbackStartInfo': new JellyfinApi.PlaybackStartInfo() // PlaybackStartInfo | The playback start info.
};
apiInstance.reportPlaybackStart(opts, (error, data, response) => {
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
 **playbackStartInfo** | [**PlaybackStartInfo**](PlaybackStartInfo.md)| The playback start info. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## reportPlaybackStopped

> reportPlaybackStopped(opts)

Reports playback has stopped within a session.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaystateApi();
let opts = {
  'playbackStopInfo': new JellyfinApi.PlaybackStopInfo() // PlaybackStopInfo | The playback stop info.
};
apiInstance.reportPlaybackStopped(opts, (error, data, response) => {
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
 **playbackStopInfo** | [**PlaybackStopInfo**](PlaybackStopInfo.md)| The playback stop info. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined

