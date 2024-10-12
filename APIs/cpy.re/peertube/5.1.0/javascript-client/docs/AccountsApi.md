# PeerTube.AccountsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1AccountsNameRatingsGet**](AccountsApi.md#apiV1AccountsNameRatingsGet) | **GET** /api/v1/accounts/{name}/ratings | List ratings of an account
[**apiV1AccountsNameVideoChannelSyncsGet_1**](AccountsApi.md#apiV1AccountsNameVideoChannelSyncsGet_1) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
[**apiV1AccountsNameVideoChannelsGet_0**](AccountsApi.md#apiV1AccountsNameVideoChannelsGet_0) | **GET** /api/v1/accounts/{name}/video-channels | List video channels of an account
[**apiV1AccountsNameVideoPlaylistsGet_0**](AccountsApi.md#apiV1AccountsNameVideoPlaylistsGet_0) | **GET** /api/v1/accounts/{name}/video-playlists | List playlists of an account
[**getAccount**](AccountsApi.md#getAccount) | **GET** /api/v1/accounts/{name} | Get an account
[**getAccountFollowers**](AccountsApi.md#getAccountFollowers) | **GET** /api/v1/accounts/{name}/followers | List followers of an account
[**getAccountVideos**](AccountsApi.md#getAccountVideos) | **GET** /api/v1/accounts/{name}/videos | List videos of an account
[**getAccounts**](AccountsApi.md#getAccounts) | **GET** /api/v1/accounts | List accounts



## apiV1AccountsNameRatingsGet

> [VideoRating] apiV1AccountsNameRatingsGet(name, opts)

List ratings of an account

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AccountsApi();
let name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt", // String | Sort column
  'rating': "rating_example" // String | Optionally filter which ratings to retrieve
};
apiInstance.apiV1AccountsNameRatingsGet(name, opts, (error, data, response) => {
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
 **rating** | **String**| Optionally filter which ratings to retrieve | [optional] 

### Return type

[**[VideoRating]**](VideoRating.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsNameVideoChannelSyncsGet_1

> VideoChannelSyncList apiV1AccountsNameVideoChannelSyncsGet_1(name, opts)

List the synchronizations of video channels of an account

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.AccountsApi();
let name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1AccountsNameVideoChannelSyncsGet_1(name, opts, (error, data, response) => {
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


## apiV1AccountsNameVideoChannelsGet_0

> VideoChannelList apiV1AccountsNameVideoChannelsGet_0(name, opts)

List video channels of an account

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.AccountsApi();
let name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
let opts = {
  'withStats': true, // Boolean | include daily view statistics for the last 30 days and total views (only if authentified as the account user)
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1AccountsNameVideoChannelsGet_0(name, opts, (error, data, response) => {
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


## apiV1AccountsNameVideoPlaylistsGet_0

> ApiV1AccountsNameVideoPlaylistsGet200Response apiV1AccountsNameVideoPlaylistsGet_0(name, opts)

List playlists of an account

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.AccountsApi();
let name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt", // String | Sort column
  'search': "search_example", // String | Plain text search, applied to various parts of the model depending on endpoint
  'playlistType': new PeerTube.VideoPlaylistTypeSet() // VideoPlaylistTypeSet | 
};
apiInstance.apiV1AccountsNameVideoPlaylistsGet_0(name, opts, (error, data, response) => {
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
 **search** | **String**| Plain text search, applied to various parts of the model depending on endpoint | [optional] 
 **playlistType** | [**VideoPlaylistTypeSet**](.md)|  | [optional] 

### Return type

[**ApiV1AccountsNameVideoPlaylistsGet200Response**](ApiV1AccountsNameVideoPlaylistsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccount

> Account getAccount(name)

Get an account

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.AccountsApi();
let name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
apiInstance.getAccount(name, (error, data, response) => {
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

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccountFollowers

> GetAccountFollowers200Response getAccountFollowers(name, opts)

List followers of an account

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AccountsApi();
let name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "sort_example", // String | Sort followers by criteria
  'search': "search_example" // String | Plain text search, applied to various parts of the model depending on endpoint
};
apiInstance.getAccountFollowers(name, opts, (error, data, response) => {
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
 **sort** | **String**| Sort followers by criteria | [optional] 
 **search** | **String**| Plain text search, applied to various parts of the model depending on endpoint | [optional] 

### Return type

[**GetAccountFollowers200Response**](GetAccountFollowers200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccountVideos

> VideoListResponse getAccountVideos(name, opts)

List videos of an account

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.AccountsApi();
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
apiInstance.getAccountVideos(name, opts, (error, data, response) => {
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


## getAccounts

> [Account] getAccounts(opts)

List accounts

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.AccountsApi();
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.getAccounts(opts, (error, data, response) => {
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

[**[Account]**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

