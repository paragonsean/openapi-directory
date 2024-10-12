# PeerTube.LiveVideosApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addLive**](LiveVideosApi.md#addLive) | **POST** /api/v1/videos/live | Create a live
[**apiV1VideosIdLiveSessionGet**](LiveVideosApi.md#apiV1VideosIdLiveSessionGet) | **GET** /api/v1/videos/{id}/live-session | Get live session of a replay
[**apiV1VideosLiveIdSessionsGet**](LiveVideosApi.md#apiV1VideosLiveIdSessionsGet) | **GET** /api/v1/videos/live/{id}/sessions | List live sessions
[**getLiveId**](LiveVideosApi.md#getLiveId) | **GET** /api/v1/videos/live/{id} | Get information about a live
[**updateLiveId**](LiveVideosApi.md#updateLiveId) | **PUT** /api/v1/videos/live/{id} | Update information about a live



## addLive

> VideoUploadResponse addLive(channelId, name, opts)

Create a live

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.LiveVideosApi();
let channelId = 56; // Number | Channel id that will contain this live video
let name = "name_example"; // String | Live video/replay name
let opts = {
  'category': 56, // Number | category id of the video (see [/videos/categories](#operation/getCategories))
  'commentsEnabled': true, // Boolean | Enable or disable comments for this live video/replay
  'description': "description_example", // String | Live video/replay description
  'downloadEnabled': true, // Boolean | Enable or disable downloading for the replay of this live video
  'language': "language_example", // String | language id of the video (see [/videos/languages](#operation/getLanguages))
  'latencyMode': new PeerTube.LiveVideoLatencyMode(), // LiveVideoLatencyMode | 
  'licence': 56, // Number | licence id of the video (see [/videos/licences](#operation/getLicences))
  'nsfw': true, // Boolean | Whether or not this live video/replay contains sensitive content
  'permanentLive': true, // Boolean | User can stream multiple times in a permanent live
  'previewfile': "/path/to/file", // File | Live video/replay preview file
  'privacy': new PeerTube.VideoPrivacySet(), // VideoPrivacySet | 
  'replaySettings': new PeerTube.LiveVideoReplaySettings(), // LiveVideoReplaySettings | 
  'saveReplay': true, // Boolean | 
  'support': "support_example", // String | A text tell the audience how to support the creator
  'tags': ["null"], // [String] | Live video/replay tags (maximum 5 tags each between 2 and 30 characters)
  'thumbnailfile': "/path/to/file" // File | Live video/replay thumbnail file
};
apiInstance.addLive(channelId, name, opts, (error, data, response) => {
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
 **channelId** | **Number**| Channel id that will contain this live video | 
 **name** | **String**| Live video/replay name | 
 **category** | **Number**| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **commentsEnabled** | **Boolean**| Enable or disable comments for this live video/replay | [optional] 
 **description** | **String**| Live video/replay description | [optional] 
 **downloadEnabled** | **Boolean**| Enable or disable downloading for the replay of this live video | [optional] 
 **language** | **String**| language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] 
 **latencyMode** | [**LiveVideoLatencyMode**](LiveVideoLatencyMode.md)|  | [optional] 
 **licence** | **Number**| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **nsfw** | **Boolean**| Whether or not this live video/replay contains sensitive content | [optional] 
 **permanentLive** | **Boolean**| User can stream multiple times in a permanent live | [optional] 
 **previewfile** | **File**| Live video/replay preview file | [optional] 
 **privacy** | [**VideoPrivacySet**](VideoPrivacySet.md)|  | [optional] 
 **replaySettings** | [**LiveVideoReplaySettings**](LiveVideoReplaySettings.md)|  | [optional] 
 **saveReplay** | **Boolean**|  | [optional] 
 **support** | **String**| A text tell the audience how to support the creator | [optional] 
 **tags** | [**[String]**](String.md)| Live video/replay tags (maximum 5 tags each between 2 and 30 characters) | [optional] 
 **thumbnailfile** | **File**| Live video/replay thumbnail file | [optional] 

### Return type

[**VideoUploadResponse**](VideoUploadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## apiV1VideosIdLiveSessionGet

> LiveVideoSessionResponse apiV1VideosIdLiveSessionGet(id)

Get live session of a replay

If the video is a replay of a live, you can find the associated live session using this endpoint

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.LiveVideosApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.apiV1VideosIdLiveSessionGet(id, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

[**LiveVideoSessionResponse**](LiveVideoSessionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1VideosLiveIdSessionsGet

> ApiV1VideosLiveIdSessionsGet200Response apiV1VideosLiveIdSessionsGet(id)

List live sessions

List all sessions created in a particular live

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.LiveVideosApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.apiV1VideosLiveIdSessionsGet(id, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

[**ApiV1VideosLiveIdSessionsGet200Response**](ApiV1VideosLiveIdSessionsGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLiveId

> LiveVideoResponse getLiveId(id)

Get information about a live

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.LiveVideosApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.getLiveId(id, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

[**LiveVideoResponse**](LiveVideoResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateLiveId

> updateLiveId(id, opts)

Update information about a live

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.LiveVideosApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let opts = {
  'liveVideoUpdate': new PeerTube.LiveVideoUpdate() // LiveVideoUpdate | 
};
apiInstance.updateLiveId(id, opts, (error, data, response) => {
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
 **liveVideoUpdate** | [**LiveVideoUpdate**](LiveVideoUpdate.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

