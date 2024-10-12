# PeerTube.VideoChannelsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoChannel**](VideoChannelsApi.md#addVideoChannel) | **POST** /api/v1/video-channels | Create a video channel
[**apiV1AccountsNameVideoChannelSyncsGet**](VideoChannelsApi.md#apiV1AccountsNameVideoChannelSyncsGet) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
[**apiV1AccountsNameVideoChannelsGet**](VideoChannelsApi.md#apiV1AccountsNameVideoChannelsGet) | **GET** /api/v1/accounts/{name}/video-channels | List video channels of an account
[**apiV1VideoChannelsChannelHandleAvatarDelete**](VideoChannelsApi.md#apiV1VideoChannelsChannelHandleAvatarDelete) | **DELETE** /api/v1/video-channels/{channelHandle}/avatar | Delete channel avatar
[**apiV1VideoChannelsChannelHandleAvatarPickPost**](VideoChannelsApi.md#apiV1VideoChannelsChannelHandleAvatarPickPost) | **POST** /api/v1/video-channels/{channelHandle}/avatar/pick | Update channel avatar
[**apiV1VideoChannelsChannelHandleBannerDelete**](VideoChannelsApi.md#apiV1VideoChannelsChannelHandleBannerDelete) | **DELETE** /api/v1/video-channels/{channelHandle}/banner | Delete channel banner
[**apiV1VideoChannelsChannelHandleBannerPickPost**](VideoChannelsApi.md#apiV1VideoChannelsChannelHandleBannerPickPost) | **POST** /api/v1/video-channels/{channelHandle}/banner/pick | Update channel banner
[**apiV1VideoChannelsChannelHandleImportVideosPost**](VideoChannelsApi.md#apiV1VideoChannelsChannelHandleImportVideosPost) | **POST** /api/v1/video-channels/{channelHandle}/import-videos | Import videos in channel
[**apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0**](VideoChannelsApi.md#apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0) | **GET** /api/v1/video-channels/{channelHandle}/video-playlists | List playlists of a channel
[**delVideoChannel**](VideoChannelsApi.md#delVideoChannel) | **DELETE** /api/v1/video-channels/{channelHandle} | Delete a video channel
[**getVideoChannel**](VideoChannelsApi.md#getVideoChannel) | **GET** /api/v1/video-channels/{channelHandle} | Get a video channel
[**getVideoChannelFollowers**](VideoChannelsApi.md#getVideoChannelFollowers) | **GET** /api/v1/video-channels/{channelHandle}/followers | List followers of a video channel
[**getVideoChannelVideos_0**](VideoChannelsApi.md#getVideoChannelVideos_0) | **GET** /api/v1/video-channels/{channelHandle}/videos | List videos of a video channel
[**getVideoChannels**](VideoChannelsApi.md#getVideoChannels) | **GET** /api/v1/video-channels | List video channels
[**putVideoChannel**](VideoChannelsApi.md#putVideoChannel) | **PUT** /api/v1/video-channels/{channelHandle} | Update a video channel



## addVideoChannel

> AddVideoChannel200Response addVideoChannel(opts)

Create a video channel

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoChannelsApi();
let opts = {
  'videoChannelCreate': new PeerTube.VideoChannelCreate() // VideoChannelCreate | 
};
apiInstance.addVideoChannel(opts, (error, data, response) => {
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
 **videoChannelCreate** | [**VideoChannelCreate**](VideoChannelCreate.md)|  | [optional] 

### Return type

[**AddVideoChannel200Response**](AddVideoChannel200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiV1AccountsNameVideoChannelSyncsGet

> VideoChannelSyncList apiV1AccountsNameVideoChannelSyncsGet(name, opts)

List the synchronizations of video channels of an account

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoChannelsApi();
let name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1AccountsNameVideoChannelSyncsGet(name, opts, (error, data, response) => {
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
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 

### Return type

[**VideoChannelSyncList**](VideoChannelSyncList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsNameVideoChannelsGet

> VideoChannelList apiV1AccountsNameVideoChannelsGet(name, opts)

List video channels of an account

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoChannelsApi();
let name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
let opts = {
  'withStats': true, // Boolean | include daily view statistics for the last 30 days and total views (only if authentified as the account user)
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1AccountsNameVideoChannelsGet(name, opts, (error, data, response) => {
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
 **withStats** | **Boolean**| include daily view statistics for the last 30 days and total views (only if authentified as the account user) | [optional] 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 

### Return type

[**VideoChannelList**](VideoChannelList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1VideoChannelsChannelHandleAvatarDelete

> apiV1VideoChannelsChannelHandleAvatarDelete(channelHandle)

Delete channel avatar

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoChannelsApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
apiInstance.apiV1VideoChannelsChannelHandleAvatarDelete(channelHandle, (error, data, response) => {
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
 **channelHandle** | **String**| The video channel handle | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1VideoChannelsChannelHandleAvatarPickPost

> ApiV1UsersMeAvatarPickPost200Response apiV1VideoChannelsChannelHandleAvatarPickPost(channelHandle, opts)

Update channel avatar

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoChannelsApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
let opts = {
  'avatarfile': "/path/to/file" // File | The file to upload.
};
apiInstance.apiV1VideoChannelsChannelHandleAvatarPickPost(channelHandle, opts, (error, data, response) => {
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
 **avatarfile** | **File**| The file to upload. | [optional] 

### Return type

[**ApiV1UsersMeAvatarPickPost200Response**](ApiV1UsersMeAvatarPickPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## apiV1VideoChannelsChannelHandleBannerDelete

> apiV1VideoChannelsChannelHandleBannerDelete(channelHandle)

Delete channel banner

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoChannelsApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
apiInstance.apiV1VideoChannelsChannelHandleBannerDelete(channelHandle, (error, data, response) => {
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
 **channelHandle** | **String**| The video channel handle | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1VideoChannelsChannelHandleBannerPickPost

> ApiV1VideoChannelsChannelHandleBannerPickPost200Response apiV1VideoChannelsChannelHandleBannerPickPost(channelHandle, opts)

Update channel banner

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoChannelsApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
let opts = {
  'bannerfile': "/path/to/file" // File | The file to upload.
};
apiInstance.apiV1VideoChannelsChannelHandleBannerPickPost(channelHandle, opts, (error, data, response) => {
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
 **bannerfile** | **File**| The file to upload. | [optional] 

### Return type

[**ApiV1VideoChannelsChannelHandleBannerPickPost200Response**](ApiV1VideoChannelsChannelHandleBannerPickPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## apiV1VideoChannelsChannelHandleImportVideosPost

> apiV1VideoChannelsChannelHandleImportVideosPost(channelHandle, opts)

Import videos in channel

Import a remote channel/playlist videos into a channel

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoChannelsApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
let opts = {
  'importVideosInChannelCreate': new PeerTube.ImportVideosInChannelCreate() // ImportVideosInChannelCreate | 
};
apiInstance.apiV1VideoChannelsChannelHandleImportVideosPost(channelHandle, opts, (error, data, response) => {
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
 **channelHandle** | **String**| The video channel handle | 
 **importVideosInChannelCreate** | [**ImportVideosInChannelCreate**](ImportVideosInChannelCreate.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0

> ApiV1AccountsNameVideoPlaylistsGet200Response apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0(channelHandle, opts)

List playlists of a channel

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoChannelsApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt", // String | Sort column
  'playlistType': new PeerTube.VideoPlaylistTypeSet() // VideoPlaylistTypeSet | 
};
apiInstance.apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0(channelHandle, opts, (error, data, response) => {
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
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 
 **playlistType** | [**VideoPlaylistTypeSet**](.md)|  | [optional] 

### Return type

[**ApiV1AccountsNameVideoPlaylistsGet200Response**](ApiV1AccountsNameVideoPlaylistsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## delVideoChannel

> delVideoChannel(channelHandle)

Delete a video channel

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoChannelsApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
apiInstance.delVideoChannel(channelHandle, (error, data, response) => {
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
 **channelHandle** | **String**| The video channel handle | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVideoChannel

> VideoChannel getVideoChannel(channelHandle)

Get a video channel

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoChannelsApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
apiInstance.getVideoChannel(channelHandle, (error, data, response) => {
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

### Return type

[**VideoChannel**](VideoChannel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoChannelFollowers

> GetAccountFollowers200Response getVideoChannelFollowers(channelHandle, opts)

List followers of a video channel

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoChannelsApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "sort_example", // String | Sort followers by criteria
  'search': "search_example" // String | Plain text search, applied to various parts of the model depending on endpoint
};
apiInstance.getVideoChannelFollowers(channelHandle, opts, (error, data, response) => {
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
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort followers by criteria | [optional] 
 **search** | **String**| Plain text search, applied to various parts of the model depending on endpoint | [optional] 

### Return type

[**GetAccountFollowers200Response**](GetAccountFollowers200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoChannelVideos_0

> VideoListResponse getVideoChannelVideos_0(channelHandle, opts)

List videos of a video channel

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoChannelsApi();
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
apiInstance.getVideoChannelVideos_0(channelHandle, opts, (error, data, response) => {
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


## getVideoChannels

> VideoChannelList getVideoChannels(opts)

List video channels

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoChannelsApi();
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.getVideoChannels(opts, (error, data, response) => {
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

[**VideoChannelList**](VideoChannelList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putVideoChannel

> putVideoChannel(channelHandle, opts)

Update a video channel

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoChannelsApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
let opts = {
  'videoChannelUpdate': new PeerTube.VideoChannelUpdate() // VideoChannelUpdate | 
};
apiInstance.putVideoChannel(channelHandle, opts, (error, data, response) => {
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
 **channelHandle** | **String**| The video channel handle | 
 **videoChannelUpdate** | [**VideoChannelUpdate**](VideoChannelUpdate.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

