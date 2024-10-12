# MuxApi.LiveStreamsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createLiveStream**](LiveStreamsApi.md#createLiveStream) | **POST** /video/v1/live-streams | Create a live stream
[**createLiveStreamPlaybackId**](LiveStreamsApi.md#createLiveStreamPlaybackId) | **POST** /video/v1/live-streams/{LIVE_STREAM_ID}/playback-ids | Create a live stream playback ID
[**createLiveStreamSimulcastTarget**](LiveStreamsApi.md#createLiveStreamSimulcastTarget) | **POST** /video/v1/live-streams/{LIVE_STREAM_ID}/simulcast-targets | Create a live stream simulcast target
[**deleteLiveStream**](LiveStreamsApi.md#deleteLiveStream) | **DELETE** /video/v1/live-streams/{LIVE_STREAM_ID} | Delete a live stream
[**deleteLiveStreamPlaybackId**](LiveStreamsApi.md#deleteLiveStreamPlaybackId) | **DELETE** /video/v1/live-streams/{LIVE_STREAM_ID}/playback-ids/{PLAYBACK_ID} | Delete a live stream playback ID
[**deleteLiveStreamSimulcastTarget**](LiveStreamsApi.md#deleteLiveStreamSimulcastTarget) | **DELETE** /video/v1/live-streams/{LIVE_STREAM_ID}/simulcast-targets/{SIMULCAST_TARGET_ID} | Delete a Live Stream Simulcast Target
[**disableLiveStream**](LiveStreamsApi.md#disableLiveStream) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/disable | Disable a live stream
[**enableLiveStream**](LiveStreamsApi.md#enableLiveStream) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/enable | Enable a live stream
[**getLiveStream**](LiveStreamsApi.md#getLiveStream) | **GET** /video/v1/live-streams/{LIVE_STREAM_ID} | Retrieve a live stream
[**getLiveStreamPlaybackId**](LiveStreamsApi.md#getLiveStreamPlaybackId) | **GET** /video/v1/live-streams/{LIVE_STREAM_ID}/playback-ids/{PLAYBACK_ID} | Retrieve a live stream playback ID
[**getLiveStreamSimulcastTarget**](LiveStreamsApi.md#getLiveStreamSimulcastTarget) | **GET** /video/v1/live-streams/{LIVE_STREAM_ID}/simulcast-targets/{SIMULCAST_TARGET_ID} | Retrieve a Live Stream Simulcast Target
[**listLiveStreams**](LiveStreamsApi.md#listLiveStreams) | **GET** /video/v1/live-streams | List live streams
[**resetStreamKey**](LiveStreamsApi.md#resetStreamKey) | **POST** /video/v1/live-streams/{LIVE_STREAM_ID}/reset-stream-key | Reset a live stream&#39;s stream key
[**signalLiveStreamComplete**](LiveStreamsApi.md#signalLiveStreamComplete) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/complete | Signal a live stream is finished
[**updateLiveStream**](LiveStreamsApi.md#updateLiveStream) | **PATCH** /video/v1/live-streams/{LIVE_STREAM_ID} | Update a live stream
[**updateLiveStreamEmbeddedSubtitles**](LiveStreamsApi.md#updateLiveStreamEmbeddedSubtitles) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/embedded-subtitles | Update a live stream&#39;s embedded subtitles
[**updateLiveStreamGeneratedSubtitles**](LiveStreamsApi.md#updateLiveStreamGeneratedSubtitles) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/generated-subtitles | Update a live stream&#39;s generated subtitles



## createLiveStream

> LiveStreamResponse createLiveStream(createLiveStreamRequest)

Create a live stream

Creates a new live stream. Once created, an encoder can connect to Mux via the specified stream key and begin streaming to an audience.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let createLiveStreamRequest = {"new_asset_settings":{"playback_policy":["public"]},"playback_policy":["public"]}; // CreateLiveStreamRequest | 
apiInstance.createLiveStream(createLiveStreamRequest, (error, data, response) => {
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
 **createLiveStreamRequest** | [**CreateLiveStreamRequest**](CreateLiveStreamRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLiveStreamPlaybackId

> CreatePlaybackIDResponse createLiveStreamPlaybackId(LIVE_STREAM_ID, createPlaybackIDRequest)

Create a live stream playback ID

Create a new playback ID for this live stream, through which a viewer can watch the streamed content of the live stream.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
let createPlaybackIDRequest = {"policy":"signed"}; // CreatePlaybackIDRequest | 
apiInstance.createLiveStreamPlaybackId(LIVE_STREAM_ID, createPlaybackIDRequest, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 
 **createPlaybackIDRequest** | [**CreatePlaybackIDRequest**](CreatePlaybackIDRequest.md)|  | 

### Return type

[**CreatePlaybackIDResponse**](CreatePlaybackIDResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLiveStreamSimulcastTarget

> SimulcastTargetResponse createLiveStreamSimulcastTarget(LIVE_STREAM_ID, createSimulcastTargetRequest)

Create a live stream simulcast target

Create a simulcast target for the parent live stream. Simulcast target can only be created when the parent live stream is in idle state. Only one simulcast target can be created at a time with this API.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
let createSimulcastTargetRequest = {"passthrough":"Example","stream_key":"abcdefgh","url":"rtmp://live.example.com/app"}; // CreateSimulcastTargetRequest | 
apiInstance.createLiveStreamSimulcastTarget(LIVE_STREAM_ID, createSimulcastTargetRequest, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 
 **createSimulcastTargetRequest** | [**CreateSimulcastTargetRequest**](CreateSimulcastTargetRequest.md)|  | 

### Return type

[**SimulcastTargetResponse**](SimulcastTargetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteLiveStream

> deleteLiveStream(LIVE_STREAM_ID)

Delete a live stream

Deletes a live stream from the current environment. If the live stream is currently active and being streamed to, ingest will be terminated and the encoder will be disconnected.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
apiInstance.deleteLiveStream(LIVE_STREAM_ID, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 

### Return type

null (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteLiveStreamPlaybackId

> deleteLiveStreamPlaybackId(LIVE_STREAM_ID, PLAYBACK_ID)

Delete a live stream playback ID

Deletes the playback ID for the live stream. This will not disable ingest (as the live stream still exists). New attempts to play back the live stream will fail immediately. However, current viewers will be able to continue watching the stream for some period of time.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
let PLAYBACK_ID = "PLAYBACK_ID_example"; // String | The live stream's playback ID.
apiInstance.deleteLiveStreamPlaybackId(LIVE_STREAM_ID, PLAYBACK_ID, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 
 **PLAYBACK_ID** | **String**| The live stream&#39;s playback ID. | 

### Return type

null (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteLiveStreamSimulcastTarget

> deleteLiveStreamSimulcastTarget(LIVE_STREAM_ID, SIMULCAST_TARGET_ID)

Delete a Live Stream Simulcast Target

Delete the simulcast target using the simulcast target ID returned when creating the simulcast target. Simulcast Target can only be deleted when the parent live stream is in idle state.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
let SIMULCAST_TARGET_ID = "SIMULCAST_TARGET_ID_example"; // String | The ID of the simulcast target.
apiInstance.deleteLiveStreamSimulcastTarget(LIVE_STREAM_ID, SIMULCAST_TARGET_ID, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 
 **SIMULCAST_TARGET_ID** | **String**| The ID of the simulcast target. | 

### Return type

null (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## disableLiveStream

> DisableLiveStreamResponse disableLiveStream(LIVE_STREAM_ID)

Disable a live stream

Disables a live stream, making it reject incoming RTMP streams until re-enabled. The API also ends the live stream recording immediately when active. Ending the live stream recording adds the &#x60;EXT-X-ENDLIST&#x60; tag to the HLS manifest which notifies the player that this live stream is over.  Mux also closes the encoder connection immediately. Any attempt from the encoder to re-establish connection will fail till the live stream is re-enabled. 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
apiInstance.disableLiveStream(LIVE_STREAM_ID, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 

### Return type

[**DisableLiveStreamResponse**](DisableLiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableLiveStream

> EnableLiveStreamResponse enableLiveStream(LIVE_STREAM_ID)

Enable a live stream

Enables a live stream, allowing it to accept an incoming RTMP stream.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
apiInstance.enableLiveStream(LIVE_STREAM_ID, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 

### Return type

[**EnableLiveStreamResponse**](EnableLiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLiveStream

> LiveStreamResponse getLiveStream(LIVE_STREAM_ID)

Retrieve a live stream

Retrieves the details of a live stream that has previously been created. Supply the unique live stream ID that was returned from your previous request, and Mux will return the corresponding live stream information. The same information is returned when creating a live stream.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
apiInstance.getLiveStream(LIVE_STREAM_ID, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLiveStreamPlaybackId

> GetLiveStreamPlaybackIDResponse getLiveStreamPlaybackId(LIVE_STREAM_ID, PLAYBACK_ID)

Retrieve a live stream playback ID

Fetches information about a live stream&#39;s playback ID, through which a viewer can watch the streamed content from this live stream.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
let PLAYBACK_ID = "PLAYBACK_ID_example"; // String | The live stream's playback ID.
apiInstance.getLiveStreamPlaybackId(LIVE_STREAM_ID, PLAYBACK_ID, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 
 **PLAYBACK_ID** | **String**| The live stream&#39;s playback ID. | 

### Return type

[**GetLiveStreamPlaybackIDResponse**](GetLiveStreamPlaybackIDResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLiveStreamSimulcastTarget

> SimulcastTargetResponse getLiveStreamSimulcastTarget(LIVE_STREAM_ID, SIMULCAST_TARGET_ID)

Retrieve a Live Stream Simulcast Target

Retrieves the details of the simulcast target created for the parent live stream. Supply the unique live stream ID and simulcast target ID that was returned in the response of create simulcast target request, and Mux will return the corresponding information.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
let SIMULCAST_TARGET_ID = "SIMULCAST_TARGET_ID_example"; // String | The ID of the simulcast target.
apiInstance.getLiveStreamSimulcastTarget(LIVE_STREAM_ID, SIMULCAST_TARGET_ID, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 
 **SIMULCAST_TARGET_ID** | **String**| The ID of the simulcast target. | 

### Return type

[**SimulcastTargetResponse**](SimulcastTargetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLiveStreams

> ListLiveStreamsResponse listLiveStreams(opts)

List live streams

Lists the live streams that currently exist in the current environment.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let opts = {
  'limit': 25, // Number | Number of items to include in the response
  'page': 1, // Number | Offset by this many pages, of the size of `limit`
  'streamKey': "streamKey_example", // String | Filter response to return live stream for this stream key only
  'status': new MuxApi.LiveStreamStatus() // LiveStreamStatus | Filter response to return live streams with the specified status only
};
apiInstance.listLiveStreams(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of items to include in the response | [optional] [default to 25]
 **page** | **Number**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **streamKey** | **String**| Filter response to return live stream for this stream key only | [optional] 
 **status** | [**LiveStreamStatus**](.md)| Filter response to return live streams with the specified status only | [optional] 

### Return type

[**ListLiveStreamsResponse**](ListLiveStreamsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetStreamKey

> LiveStreamResponse resetStreamKey(LIVE_STREAM_ID)

Reset a live stream&#39;s stream key

Reset a live stream key if you want to immediately stop the current stream key from working and create a new stream key that can be used for future broadcasts.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
apiInstance.resetStreamKey(LIVE_STREAM_ID, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## signalLiveStreamComplete

> SignalLiveStreamCompleteResponse signalLiveStreamComplete(LIVE_STREAM_ID)

Signal a live stream is finished

(Optional) End the live stream recording immediately instead of waiting for the reconnect_window. &#x60;EXT-X-ENDLIST&#x60; tag is added to the HLS manifest which notifies the player that this live stream is over.  Mux does not close the encoder connection immediately. Encoders are often configured to re-establish connections immediately which would result in a new recorded asset. For this reason, Mux waits for 60s before closing the connection with the encoder. This 60s timeframe is meant to give encoder operators a chance to disconnect from their end. 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
apiInstance.signalLiveStreamComplete(LIVE_STREAM_ID, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 

### Return type

[**SignalLiveStreamCompleteResponse**](SignalLiveStreamCompleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateLiveStream

> LiveStreamResponse updateLiveStream(LIVE_STREAM_ID, updateLiveStreamRequest)

Update a live stream

Updates the parameters of a previously-created live stream. This currently supports a subset of variables. Supply the live stream ID and the updated parameters and Mux will return the corresponding live stream information. The information returned will be the same after update as for subsequent get live stream requests.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
let updateLiveStreamRequest = {"latency_mode":"standard","max_continuous_duration":1200,"reconnect_window":30}; // UpdateLiveStreamRequest | 
apiInstance.updateLiveStream(LIVE_STREAM_ID, updateLiveStreamRequest, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 
 **updateLiveStreamRequest** | [**UpdateLiveStreamRequest**](UpdateLiveStreamRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateLiveStreamEmbeddedSubtitles

> LiveStreamResponse updateLiveStreamEmbeddedSubtitles(LIVE_STREAM_ID, updateLiveStreamEmbeddedSubtitlesRequest)

Update a live stream&#39;s embedded subtitles

Configures a live stream to receive embedded closed captions. The resulting Asset&#39;s subtitle text track will have &#x60;closed_captions: true&#x60; set. 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
let updateLiveStreamEmbeddedSubtitlesRequest = {"embedded_subtitles":[{"passthrough":"Example"}]}; // UpdateLiveStreamEmbeddedSubtitlesRequest | 
apiInstance.updateLiveStreamEmbeddedSubtitles(LIVE_STREAM_ID, updateLiveStreamEmbeddedSubtitlesRequest, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 
 **updateLiveStreamEmbeddedSubtitlesRequest** | [**UpdateLiveStreamEmbeddedSubtitlesRequest**](UpdateLiveStreamEmbeddedSubtitlesRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateLiveStreamGeneratedSubtitles

> LiveStreamResponse updateLiveStreamGeneratedSubtitles(LIVE_STREAM_ID, updateLiveStreamGeneratedSubtitlesRequest)

Update a live stream&#39;s generated subtitles

Updates a live stream&#39;s automatic-speech-recognition-generated subtitle configuration. Automatic speech recognition subtitles can be removed by sending an empty array in the request payload. 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.LiveStreamsApi();
let LIVE_STREAM_ID = "LIVE_STREAM_ID_example"; // String | The live stream ID
let updateLiveStreamGeneratedSubtitlesRequest = {"generated_subtitles":[{"language":"en","name":"English CC (ASR)","passthrough":"Example"}]}; // UpdateLiveStreamGeneratedSubtitlesRequest | 
apiInstance.updateLiveStreamGeneratedSubtitles(LIVE_STREAM_ID, updateLiveStreamGeneratedSubtitlesRequest, (error, data, response) => {
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
 **LIVE_STREAM_ID** | **String**| The live stream ID | 
 **updateLiveStreamGeneratedSubtitlesRequest** | [**UpdateLiveStreamGeneratedSubtitlesRequest**](UpdateLiveStreamGeneratedSubtitlesRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

