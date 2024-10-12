# PeerTube.VideosApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoPlaylistVideo**](VideosApi.md#addVideoPlaylistVideo) | **POST** /api/v1/video-playlists/{playlistId}/videos | Add a video in a playlist
[**apiV1UsersMeSubscriptionsVideosGet_0**](VideosApi.md#apiV1UsersMeSubscriptionsVideosGet_0) | **GET** /api/v1/users/me/subscriptions/videos | List videos of subscriptions of my user
[**apiV1UsersMeVideosGet_0**](VideosApi.md#apiV1UsersMeVideosGet_0) | **GET** /api/v1/users/me/videos | Get videos of my user
[**apiV1UsersMeVideosImportsGet**](VideosApi.md#apiV1UsersMeVideosImportsGet) | **GET** /api/v1/users/me/videos/imports | Get video imports of my user
[**getVideoPlaylistVideos**](VideosApi.md#getVideoPlaylistVideos) | **GET** /api/v1/video-playlists/{playlistId}/videos | List videos of a playlist



## addVideoPlaylistVideo

> AddVideoPlaylistVideo200Response addVideoPlaylistVideo(playlistId, opts)

Add a video in a playlist

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideosApi();
let playlistId = 56; // Number | Playlist id
let opts = {
  'addVideoPlaylistVideoRequest': new PeerTube.AddVideoPlaylistVideoRequest() // AddVideoPlaylistVideoRequest | 
};
apiInstance.addVideoPlaylistVideo(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **Number**| Playlist id | 
 **addVideoPlaylistVideoRequest** | [**AddVideoPlaylistVideoRequest**](AddVideoPlaylistVideoRequest.md)|  | [optional] 

### Return type

[**AddVideoPlaylistVideo200Response**](AddVideoPlaylistVideo200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiV1UsersMeSubscriptionsVideosGet_0

> VideoListResponse apiV1UsersMeSubscriptionsVideosGet_0(opts)

List videos of subscriptions of my user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideosApi();
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
apiInstance.apiV1UsersMeSubscriptionsVideosGet_0(opts, (error, data, response) => {
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1UsersMeVideosGet_0

> VideoListResponse apiV1UsersMeVideosGet_0(opts)

Get videos of my user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideosApi();
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1UsersMeVideosGet_0(opts, (error, data, response) => {
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
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1UsersMeVideosImportsGet

> VideoImportsList apiV1UsersMeVideosImportsGet(opts)

Get video imports of my user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideosApi();
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt", // String | Sort column
  'targetUrl': "targetUrl_example", // String | Filter on import target URL
  'videoChannelSyncId': 3.4, // Number | Filter on imports created by a specific channel synchronization
  'search': "search_example" // String | Search in video names
};
apiInstance.apiV1UsersMeVideosImportsGet(opts, (error, data, response) => {
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
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 
 **targetUrl** | **String**| Filter on import target URL | [optional] 
 **videoChannelSyncId** | **Number**| Filter on imports created by a specific channel synchronization | [optional] 
 **search** | **String**| Search in video names | [optional] 

### Return type

[**VideoImportsList**](VideoImportsList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoPlaylistVideos

> VideoListResponse getVideoPlaylistVideos(playlistId, opts)

List videos of a playlist

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideosApi();
let playlistId = 56; // Number | Playlist id
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15 // Number | Number of items to return
};
apiInstance.getVideoPlaylistVideos(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **Number**| Playlist id | 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

