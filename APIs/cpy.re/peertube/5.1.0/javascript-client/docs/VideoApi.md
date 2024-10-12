# PeerTube.VideoApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addLive_0**](VideoApi.md#addLive_0) | **POST** /api/v1/videos/live | Create a live
[**addView**](VideoApi.md#addView) | **POST** /api/v1/videos/{id}/views | Notify user is watching a video
[**apiV1VideosIdStudioEditPost_0**](VideoApi.md#apiV1VideosIdStudioEditPost_0) | **POST** /api/v1/videos/{id}/studio/edit | Create a studio task
[**apiV1VideosIdWatchingPut**](VideoApi.md#apiV1VideosIdWatchingPut) | **PUT** /api/v1/videos/{id}/watching | Set watching progress of a video
[**delVideo**](VideoApi.md#delVideo) | **DELETE** /api/v1/videos/{id} | Delete a video
[**getAccountVideos_0**](VideoApi.md#getAccountVideos_0) | **GET** /api/v1/accounts/{name}/videos | List videos of an account
[**getCategories**](VideoApi.md#getCategories) | **GET** /api/v1/videos/categories | List available video categories
[**getLanguages**](VideoApi.md#getLanguages) | **GET** /api/v1/videos/languages | List available video languages
[**getLicences**](VideoApi.md#getLicences) | **GET** /api/v1/videos/licences | List available video licences
[**getLiveId_0**](VideoApi.md#getLiveId_0) | **GET** /api/v1/videos/live/{id} | Get information about a live
[**getVideo**](VideoApi.md#getVideo) | **GET** /api/v1/videos/{id} | Get a video
[**getVideoChannelVideos**](VideoApi.md#getVideoChannelVideos) | **GET** /api/v1/video-channels/{channelHandle}/videos | List videos of a video channel
[**getVideoDesc**](VideoApi.md#getVideoDesc) | **GET** /api/v1/videos/{id}/description | Get complete video description
[**getVideoPrivacyPolicies**](VideoApi.md#getVideoPrivacyPolicies) | **GET** /api/v1/videos/privacies | List available video privacy policies
[**getVideoSource**](VideoApi.md#getVideoSource) | **POST** /api/v1/videos/{id}/source | Get video source file metadata
[**getVideos**](VideoApi.md#getVideos) | **GET** /api/v1/videos | List videos
[**putVideo**](VideoApi.md#putVideo) | **PUT** /api/v1/videos/{id} | Update a video
[**requestVideoToken**](VideoApi.md#requestVideoToken) | **POST** /api/v1/videos/{id}/token | Request video token
[**updateLiveId_0**](VideoApi.md#updateLiveId_0) | **PUT** /api/v1/videos/live/{id} | Update information about a live
[**uploadLegacy**](VideoApi.md#uploadLegacy) | **POST** /api/v1/videos/upload | Upload a video
[**uploadResumable**](VideoApi.md#uploadResumable) | **PUT** /api/v1/videos/upload-resumable | Send chunk for the resumable upload of a video
[**uploadResumableCancel**](VideoApi.md#uploadResumableCancel) | **DELETE** /api/v1/videos/upload-resumable | Cancel the resumable upload of a video, deleting any data uploaded so far
[**uploadResumableInit**](VideoApi.md#uploadResumableInit) | **POST** /api/v1/videos/upload-resumable | Initialize the resumable upload of a video



## addLive_0

> VideoUploadResponse addLive_0(channelId, name, opts)

Create a live

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoApi();
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
apiInstance.addLive_0(channelId, name, opts, (error, data, response) => {
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


## addView

> addView(id, userViewingVideo)

Notify user is watching a video

Call this endpoint regularly (every 5-10 seconds for example) to notify the server the user is watching the video. After a while, PeerTube will increase video&#39;s viewers counter. If the user is authenticated, PeerTube will also store the current player time.

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let userViewingVideo = new PeerTube.UserViewingVideo(); // UserViewingVideo | 
apiInstance.addView(id, userViewingVideo, (error, data, response) => {
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
 **userViewingVideo** | [**UserViewingVideo**](UserViewingVideo.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV1VideosIdStudioEditPost_0

> apiV1VideosIdStudioEditPost_0(id)

Create a studio task

Create a task to edit a video  (cut, add intro/outro etc)

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.apiV1VideosIdStudioEditPost_0(id, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## apiV1VideosIdWatchingPut

> apiV1VideosIdWatchingPut(id, userViewingVideo)

Set watching progress of a video

This endpoint has been deprecated. Use &#x60;/videos/{id}/views&#x60; instead

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let userViewingVideo = new PeerTube.UserViewingVideo(); // UserViewingVideo | 
apiInstance.apiV1VideosIdWatchingPut(id, userViewingVideo, (error, data, response) => {
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
 **userViewingVideo** | [**UserViewingVideo**](UserViewingVideo.md)|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## delVideo

> delVideo(id)

Delete a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.delVideo(id, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAccountVideos_0

> VideoListResponse getAccountVideos_0(name, opts)

List videos of an account

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoApi();
let name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
let opts = {
  'categoryOneOf': new PeerTube.GetAccountVideosCategoryOneOfParameter(), // GetAccountVideosCategoryOneOfParameter | category id of the video (see [/videos/categories](#operation/getCategories))
  'isLive': true, // Boolean | whether or not the video is a live
  'tagsOneOf': new PeerTube.GetAccountVideosTagsOneOfParameter(), // GetAccountVideosTagsOneOfParameter | tag(s) of the video
  'tagsAllOf': new PeerTube.GetAccountVideosTagsAllOfParameter(), // GetAccountVideosTagsAllOfParameter | tag(s) of the video, where all should be present in the video
  'licenceOneOf': new PeerTube.GetAccountVideosLicenceOneOfParameter(), // GetAccountVideosLicenceOneOfParameter | licence id of the video (see [/videos/licences](#operation/getLicences))
  'languageOneOf': new PeerTube.GetAccountVideosLanguageOneOfParameter(), // GetAccountVideosLanguageOneOfParameter | language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language
  'nsfw': "nsfw_example", // String | whether to include nsfw videos, if any
  'isLocal': true, // Boolean | **PeerTube >= 4.0** Display only local or remote videos
  'include': 56, // Number | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
  'privacyOneOf': new PeerTube.VideoPrivacySet(), // VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
  'hasHLSFiles': true, // Boolean | **PeerTube >= 4.0** Display only videos that have HLS files
  'hasWebtorrentFiles': true, // Boolean | **PeerTube >= 4.0** Display only videos that have WebTorrent files
  'skipCount': "'false'", // String | if you don't need the `total` in the response
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "sort_example", // String | 
  'excludeAlreadyWatched': true // Boolean | Whether or not to exclude videos that are in the user's video history
};
apiInstance.getAccountVideos_0(name, opts, (error, data, response) => {
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
 **name** | **String**| The username or handle of the account | 
 **categoryOneOf** | [**GetAccountVideosCategoryOneOfParameter**](.md)| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **isLive** | **Boolean**| whether or not the video is a live | [optional] 
 **tagsOneOf** | [**GetAccountVideosTagsOneOfParameter**](.md)| tag(s) of the video | [optional] 
 **tagsAllOf** | [**GetAccountVideosTagsAllOfParameter**](.md)| tag(s) of the video, where all should be present in the video | [optional] 
 **licenceOneOf** | [**GetAccountVideosLicenceOneOfParameter**](.md)| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **languageOneOf** | [**GetAccountVideosLanguageOneOfParameter**](.md)| language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language | [optional] 
 **nsfw** | **String**| whether to include nsfw videos, if any | [optional] 
 **isLocal** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] 
 **include** | **Number**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] 
 **privacyOneOf** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] 
 **hasHLSFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] 
 **hasWebtorrentFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] 
 **skipCount** | **String**| if you don&#39;t need the &#x60;total&#x60; in the response | [optional] [default to &#39;false&#39;]
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**|  | [optional] 
 **excludeAlreadyWatched** | **Boolean**| Whether or not to exclude videos that are in the user&#39;s video history | [optional] 

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCategories

> [String] getCategories()

List available video categories

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoApi();
apiInstance.getCategories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLanguages

> [String] getLanguages()

List available video languages

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoApi();
apiInstance.getLanguages((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLicences

> [String] getLicences()

List available video licences

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoApi();
apiInstance.getLicences((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLiveId_0

> LiveVideoResponse getLiveId_0(id)

Get information about a live

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.getLiveId_0(id, (error, data, response) => {
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


## getVideo

> VideoDetails getVideo(id)

Get a video

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.getVideo(id, (error, data, response) => {
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

[**VideoDetails**](VideoDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoChannelVideos

> VideoListResponse getVideoChannelVideos(channelHandle, opts)

List videos of a video channel

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
let opts = {
  'categoryOneOf': new PeerTube.GetAccountVideosCategoryOneOfParameter(), // GetAccountVideosCategoryOneOfParameter | category id of the video (see [/videos/categories](#operation/getCategories))
  'isLive': true, // Boolean | whether or not the video is a live
  'tagsOneOf': new PeerTube.GetAccountVideosTagsOneOfParameter(), // GetAccountVideosTagsOneOfParameter | tag(s) of the video
  'tagsAllOf': new PeerTube.GetAccountVideosTagsAllOfParameter(), // GetAccountVideosTagsAllOfParameter | tag(s) of the video, where all should be present in the video
  'licenceOneOf': new PeerTube.GetAccountVideosLicenceOneOfParameter(), // GetAccountVideosLicenceOneOfParameter | licence id of the video (see [/videos/licences](#operation/getLicences))
  'languageOneOf': new PeerTube.GetAccountVideosLanguageOneOfParameter(), // GetAccountVideosLanguageOneOfParameter | language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language
  'nsfw': "nsfw_example", // String | whether to include nsfw videos, if any
  'isLocal': true, // Boolean | **PeerTube >= 4.0** Display only local or remote videos
  'include': 56, // Number | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
  'privacyOneOf': new PeerTube.VideoPrivacySet(), // VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
  'hasHLSFiles': true, // Boolean | **PeerTube >= 4.0** Display only videos that have HLS files
  'hasWebtorrentFiles': true, // Boolean | **PeerTube >= 4.0** Display only videos that have WebTorrent files
  'skipCount': "'false'", // String | if you don't need the `total` in the response
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "sort_example", // String | 
  'excludeAlreadyWatched': true // Boolean | Whether or not to exclude videos that are in the user's video history
};
apiInstance.getVideoChannelVideos(channelHandle, opts, (error, data, response) => {
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
 **channelHandle** | **String**| The video channel handle | 
 **categoryOneOf** | [**GetAccountVideosCategoryOneOfParameter**](.md)| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **isLive** | **Boolean**| whether or not the video is a live | [optional] 
 **tagsOneOf** | [**GetAccountVideosTagsOneOfParameter**](.md)| tag(s) of the video | [optional] 
 **tagsAllOf** | [**GetAccountVideosTagsAllOfParameter**](.md)| tag(s) of the video, where all should be present in the video | [optional] 
 **licenceOneOf** | [**GetAccountVideosLicenceOneOfParameter**](.md)| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **languageOneOf** | [**GetAccountVideosLanguageOneOfParameter**](.md)| language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language | [optional] 
 **nsfw** | **String**| whether to include nsfw videos, if any | [optional] 
 **isLocal** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] 
 **include** | **Number**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] 
 **privacyOneOf** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] 
 **hasHLSFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] 
 **hasWebtorrentFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] 
 **skipCount** | **String**| if you don&#39;t need the &#x60;total&#x60; in the response | [optional] [default to &#39;false&#39;]
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**|  | [optional] 
 **excludeAlreadyWatched** | **Boolean**| Whether or not to exclude videos that are in the user&#39;s video history | [optional] 

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoDesc

> String getVideoDesc(id)

Get complete video description

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.getVideoDesc(id, (error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoPrivacyPolicies

> [String] getVideoPrivacyPolicies()

List available video privacy policies

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoApi();
apiInstance.getVideoPrivacyPolicies((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoSource

> VideoSource getVideoSource(id)

Get video source file metadata

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.getVideoSource(id, (error, data, response) => {
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

[**VideoSource**](VideoSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideos

> VideoListResponse getVideos(opts)

List videos

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoApi();
let opts = {
  'categoryOneOf': new PeerTube.GetAccountVideosCategoryOneOfParameter(), // GetAccountVideosCategoryOneOfParameter | category id of the video (see [/videos/categories](#operation/getCategories))
  'isLive': true, // Boolean | whether or not the video is a live
  'tagsOneOf': new PeerTube.GetAccountVideosTagsOneOfParameter(), // GetAccountVideosTagsOneOfParameter | tag(s) of the video
  'tagsAllOf': new PeerTube.GetAccountVideosTagsAllOfParameter(), // GetAccountVideosTagsAllOfParameter | tag(s) of the video, where all should be present in the video
  'licenceOneOf': new PeerTube.GetAccountVideosLicenceOneOfParameter(), // GetAccountVideosLicenceOneOfParameter | licence id of the video (see [/videos/licences](#operation/getLicences))
  'languageOneOf': new PeerTube.GetAccountVideosLanguageOneOfParameter(), // GetAccountVideosLanguageOneOfParameter | language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language
  'nsfw': "nsfw_example", // String | whether to include nsfw videos, if any
  'isLocal': true, // Boolean | **PeerTube >= 4.0** Display only local or remote videos
  'include': 56, // Number | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
  'privacyOneOf': new PeerTube.VideoPrivacySet(), // VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
  'hasHLSFiles': true, // Boolean | **PeerTube >= 4.0** Display only videos that have HLS files
  'hasWebtorrentFiles': true, // Boolean | **PeerTube >= 4.0** Display only videos that have WebTorrent files
  'skipCount': "'false'", // String | if you don't need the `total` in the response
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "sort_example", // String | 
  'excludeAlreadyWatched': true // Boolean | Whether or not to exclude videos that are in the user's video history
};
apiInstance.getVideos(opts, (error, data, response) => {
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
 **categoryOneOf** | [**GetAccountVideosCategoryOneOfParameter**](.md)| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **isLive** | **Boolean**| whether or not the video is a live | [optional] 
 **tagsOneOf** | [**GetAccountVideosTagsOneOfParameter**](.md)| tag(s) of the video | [optional] 
 **tagsAllOf** | [**GetAccountVideosTagsAllOfParameter**](.md)| tag(s) of the video, where all should be present in the video | [optional] 
 **licenceOneOf** | [**GetAccountVideosLicenceOneOfParameter**](.md)| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **languageOneOf** | [**GetAccountVideosLanguageOneOfParameter**](.md)| language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language | [optional] 
 **nsfw** | **String**| whether to include nsfw videos, if any | [optional] 
 **isLocal** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] 
 **include** | **Number**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] 
 **privacyOneOf** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] 
 **hasHLSFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] 
 **hasWebtorrentFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] 
 **skipCount** | **String**| if you don&#39;t need the &#x60;total&#x60; in the response | [optional] [default to &#39;false&#39;]
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**|  | [optional] 
 **excludeAlreadyWatched** | **Boolean**| Whether or not to exclude videos that are in the user&#39;s video history | [optional] 

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putVideo

> putVideo(id, opts)

Update a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let opts = {
  'category': 56, // Number | category id of the video (see [/videos/categories](#operation/getCategories))
  'commentsEnabled': true, // Boolean | Enable or disable comments for this video
  'description': "description_example", // String | Video description
  'downloadEnabled': true, // Boolean | Enable or disable downloading for this video
  'language': "language_example", // String | language id of the video (see [/videos/languages](#operation/getLanguages))
  'licence': 56, // Number | licence id of the video (see [/videos/licences](#operation/getLicences))
  'name': "name_example", // String | Video name
  'nsfw': true, // Boolean | Whether or not this video contains sensitive content
  'originallyPublishedAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Date when the content was originally published
  'previewfile': "/path/to/file", // File | Video preview file
  'privacy': new PeerTube.VideoPrivacySet(), // VideoPrivacySet | 
  'scheduleUpdate': new PeerTube.VideoScheduledUpdate(), // VideoScheduledUpdate | 
  'support': "support_example", // String | A text tell the audience how to support the video creator
  'tags': ["null"], // [String] | Video tags (maximum 5 tags each between 2 and 30 characters)
  'thumbnailfile': "/path/to/file", // File | Video thumbnail file
  'waitTranscoding': "waitTranscoding_example" // String | Whether or not we wait transcoding before publish the video
};
apiInstance.putVideo(id, opts, (error, data, response) => {
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
 **category** | **Number**| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **commentsEnabled** | **Boolean**| Enable or disable comments for this video | [optional] 
 **description** | **String**| Video description | [optional] 
 **downloadEnabled** | **Boolean**| Enable or disable downloading for this video | [optional] 
 **language** | **String**| language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] 
 **licence** | **Number**| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **name** | **String**| Video name | [optional] 
 **nsfw** | **Boolean**| Whether or not this video contains sensitive content | [optional] 
 **originallyPublishedAt** | **Date**| Date when the content was originally published | [optional] 
 **previewfile** | **File**| Video preview file | [optional] 
 **privacy** | [**VideoPrivacySet**](VideoPrivacySet.md)|  | [optional] 
 **scheduleUpdate** | [**VideoScheduledUpdate**](VideoScheduledUpdate.md)|  | [optional] 
 **support** | **String**| A text tell the audience how to support the video creator | [optional] 
 **tags** | [**[String]**](String.md)| Video tags (maximum 5 tags each between 2 and 30 characters) | [optional] 
 **thumbnailfile** | **File**| Video thumbnail file | [optional] 
 **waitTranscoding** | **String**| Whether or not we wait transcoding before publish the video | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## requestVideoToken

> VideoTokenResponse requestVideoToken(id)

Request video token

Request special tokens that expire quickly to use them in some context (like accessing private static files)

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.requestVideoToken(id, (error, data, response) => {
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

[**VideoTokenResponse**](VideoTokenResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateLiveId_0

> updateLiveId_0(id, opts)

Update information about a live

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let opts = {
  'liveVideoUpdate': new PeerTube.LiveVideoUpdate() // LiveVideoUpdate | 
};
apiInstance.updateLiveId_0(id, opts, (error, data, response) => {
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


## uploadLegacy

> VideoUploadResponse uploadLegacy(channelId, name, videofile, opts)

Upload a video

Uses a single request to upload a video.

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoApi();
let channelId = 56; // Number | Channel id that will contain this video
let name = "name_example"; // String | Video name
let videofile = "/path/to/file"; // File | Video file
let opts = {
  'category': 56, // Number | category id of the video (see [/videos/categories](#operation/getCategories))
  'commentsEnabled': true, // Boolean | Enable or disable comments for this video
  'description': "description_example", // String | Video description
  'downloadEnabled': true, // Boolean | Enable or disable downloading for this video
  'language': "language_example", // String | language id of the video (see [/videos/languages](#operation/getLanguages))
  'licence': 56, // Number | licence id of the video (see [/videos/licences](#operation/getLicences))
  'nsfw': true, // Boolean | Whether or not this video contains sensitive content
  'originallyPublishedAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Date when the content was originally published
  'previewfile': "/path/to/file", // File | Video preview file
  'privacy': new PeerTube.VideoPrivacySet(), // VideoPrivacySet | 
  'scheduleUpdate': new PeerTube.VideoScheduledUpdate(), // VideoScheduledUpdate | 
  'support': "support_example", // String | A text tell the audience how to support the video creator
  'tags': ["null"], // [String] | Video tags (maximum 5 tags each between 2 and 30 characters)
  'thumbnailfile': "/path/to/file", // File | Video thumbnail file
  'waitTranscoding': true // Boolean | Whether or not we wait transcoding before publish the video
};
apiInstance.uploadLegacy(channelId, name, videofile, opts, (error, data, response) => {
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
 **channelId** | **Number**| Channel id that will contain this video | 
 **name** | **String**| Video name | 
 **videofile** | **File**| Video file | 
 **category** | **Number**| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **commentsEnabled** | **Boolean**| Enable or disable comments for this video | [optional] 
 **description** | **String**| Video description | [optional] 
 **downloadEnabled** | **Boolean**| Enable or disable downloading for this video | [optional] 
 **language** | **String**| language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] 
 **licence** | **Number**| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **nsfw** | **Boolean**| Whether or not this video contains sensitive content | [optional] 
 **originallyPublishedAt** | **Date**| Date when the content was originally published | [optional] 
 **previewfile** | **File**| Video preview file | [optional] 
 **privacy** | [**VideoPrivacySet**](VideoPrivacySet.md)|  | [optional] 
 **scheduleUpdate** | [**VideoScheduledUpdate**](VideoScheduledUpdate.md)|  | [optional] 
 **support** | **String**| A text tell the audience how to support the video creator | [optional] 
 **tags** | [**[String]**](String.md)| Video tags (maximum 5 tags each between 2 and 30 characters) | [optional] 
 **thumbnailfile** | **File**| Video thumbnail file | [optional] 
 **waitTranscoding** | **Boolean**| Whether or not we wait transcoding before publish the video | [optional] 

### Return type

[**VideoUploadResponse**](VideoUploadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## uploadResumable

> VideoUploadResponse uploadResumable(uploadId, contentRange, contentLength, opts)

Send chunk for the resumable upload of a video

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to continue, pause or resume the upload of a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoApi();
let uploadId = "uploadId_example"; // String | Created session id to proceed with. If you didn't send chunks in the last hour, it is not valid anymore and you need to initialize a new upload. 
let contentRange = "bytes 0-262143/2469036"; // String | Specifies the bytes in the file that the request is uploading.  For example, a value of `bytes 0-262143/1000000` shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file. 
let contentLength = 262144; // Number | Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube's web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health. 
let opts = {
  'body': "/path/to/file" // File | 
};
apiInstance.uploadResumable(uploadId, contentRange, contentLength, opts, (error, data, response) => {
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
 **uploadId** | **String**| Created session id to proceed with. If you didn&#39;t send chunks in the last hour, it is not valid anymore and you need to initialize a new upload.  | 
 **contentRange** | **String**| Specifies the bytes in the file that the request is uploading.  For example, a value of &#x60;bytes 0-262143/1000000&#x60; shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file.  | 
 **contentLength** | **Number**| Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube&#39;s web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health.  | 
 **body** | **File**|  | [optional] 

### Return type

[**VideoUploadResponse**](VideoUploadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## uploadResumableCancel

> uploadResumableCancel(uploadId, contentLength)

Cancel the resumable upload of a video, deleting any data uploaded so far

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoApi();
let uploadId = "uploadId_example"; // String | Created session id to proceed with. If you didn't send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-) 
let contentLength = 0; // Number | 
apiInstance.uploadResumableCancel(uploadId, contentLength, (error, data, response) => {
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
 **uploadId** | **String**| Created session id to proceed with. If you didn&#39;t send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-)  | 
 **contentLength** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## uploadResumableInit

> uploadResumableInit(xUploadContentLength, xUploadContentType, opts)

Initialize the resumable upload of a video

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to initialize the upload of a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoApi();
let xUploadContentLength = 2469036; // Number | Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading.
let xUploadContentType = "video/mp4"; // String | MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary.
let opts = {
  'videoUploadRequestResumable': new PeerTube.VideoUploadRequestResumable() // VideoUploadRequestResumable | 
};
apiInstance.uploadResumableInit(xUploadContentLength, xUploadContentType, opts, (error, data, response) => {
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
 **xUploadContentLength** | **Number**| Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading. | 
 **xUploadContentType** | **String**| MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary. | 
 **videoUploadRequestResumable** | [**VideoUploadRequestResumable**](VideoUploadRequestResumable.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

