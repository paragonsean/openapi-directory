# PeerTube.VideoFeedsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSyndicatedComments**](VideoFeedsApi.md#getSyndicatedComments) | **GET** /feeds/video-comments.{format} | List comments on videos
[**getSyndicatedSubscriptionVideos**](VideoFeedsApi.md#getSyndicatedSubscriptionVideos) | **GET** /feeds/subscriptions.{format} | List videos of subscriptions tied to a token
[**getSyndicatedVideos**](VideoFeedsApi.md#getSyndicatedVideos) | **GET** /feeds/videos.{format} | List videos



## getSyndicatedComments

> [VideoCommentsForXMLInner] getSyndicatedComments(format, opts)

List comments on videos

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoFeedsApi();
let format = "format_example"; // String | format expected (we focus on making `rss` the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss))
let opts = {
  'videoId': "videoId_example", // String | limit listing to a specific video
  'accountId': "accountId_example", // String | limit listing to a specific account
  'accountName': "accountName_example", // String | limit listing to a specific account
  'videoChannelId': "videoChannelId_example", // String | limit listing to a specific video channel
  'videoChannelName': "videoChannelName_example" // String | limit listing to a specific video channel
};
apiInstance.getSyndicatedComments(format, opts, (error, data, response) => {
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
 **format** | **String**| format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) | 
 **videoId** | **String**| limit listing to a specific video | [optional] 
 **accountId** | **String**| limit listing to a specific account | [optional] 
 **accountName** | **String**| limit listing to a specific account | [optional] 
 **videoChannelId** | **String**| limit listing to a specific video channel | [optional] 
 **videoChannelName** | **String**| limit listing to a specific video channel | [optional] 

### Return type

[**[VideoCommentsForXMLInner]**](VideoCommentsForXMLInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/atom+xml, application/json, application/rss+xml, application/xml, text/xml


## getSyndicatedSubscriptionVideos

> [VideosForXMLInner] getSyndicatedSubscriptionVideos(format, accountId, token, opts)

List videos of subscriptions tied to a token

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoFeedsApi();
let format = "format_example"; // String | format expected (we focus on making `rss` the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss))
let accountId = "accountId_example"; // String | limit listing to a specific account
let token = "token_example"; // String | private token allowing access
let opts = {
  'sort': "-createdAt", // String | Sort column
  'nsfw': "nsfw_example", // String | whether to include nsfw videos, if any
  'isLocal': true, // Boolean | **PeerTube >= 4.0** Display only local or remote videos
  'include': 56, // Number | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
  'privacyOneOf': new PeerTube.VideoPrivacySet(), // VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
  'hasHLSFiles': true, // Boolean | **PeerTube >= 4.0** Display only videos that have HLS files
  'hasWebtorrentFiles': true // Boolean | **PeerTube >= 4.0** Display only videos that have WebTorrent files
};
apiInstance.getSyndicatedSubscriptionVideos(format, accountId, token, opts, (error, data, response) => {
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
 **format** | **String**| format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) | 
 **accountId** | **String**| limit listing to a specific account | 
 **token** | **String**| private token allowing access | 
 **sort** | **String**| Sort column | [optional] 
 **nsfw** | **String**| whether to include nsfw videos, if any | [optional] 
 **isLocal** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] 
 **include** | **Number**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] 
 **privacyOneOf** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] 
 **hasHLSFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] 
 **hasWebtorrentFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] 

### Return type

[**[VideosForXMLInner]**](VideosForXMLInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/atom+xml, application/json, application/rss+xml, application/xml, text/xml


## getSyndicatedVideos

> [VideosForXMLInner] getSyndicatedVideos(format, opts)

List videos

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoFeedsApi();
let format = "format_example"; // String | format expected (we focus on making `rss` the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss))
let opts = {
  'accountId': "accountId_example", // String | limit listing to a specific account
  'accountName': "accountName_example", // String | limit listing to a specific account
  'videoChannelId': "videoChannelId_example", // String | limit listing to a specific video channel
  'videoChannelName': "videoChannelName_example", // String | limit listing to a specific video channel
  'sort': "-createdAt", // String | Sort column
  'nsfw': "nsfw_example", // String | whether to include nsfw videos, if any
  'isLocal': true, // Boolean | **PeerTube >= 4.0** Display only local or remote videos
  'include': 56, // Number | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
  'privacyOneOf': new PeerTube.VideoPrivacySet(), // VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
  'hasHLSFiles': true, // Boolean | **PeerTube >= 4.0** Display only videos that have HLS files
  'hasWebtorrentFiles': true // Boolean | **PeerTube >= 4.0** Display only videos that have WebTorrent files
};
apiInstance.getSyndicatedVideos(format, opts, (error, data, response) => {
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
 **format** | **String**| format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) | 
 **accountId** | **String**| limit listing to a specific account | [optional] 
 **accountName** | **String**| limit listing to a specific account | [optional] 
 **videoChannelId** | **String**| limit listing to a specific video channel | [optional] 
 **videoChannelName** | **String**| limit listing to a specific video channel | [optional] 
 **sort** | **String**| Sort column | [optional] 
 **nsfw** | **String**| whether to include nsfw videos, if any | [optional] 
 **isLocal** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] 
 **include** | **Number**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] 
 **privacyOneOf** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] 
 **hasHLSFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] 
 **hasWebtorrentFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] 

### Return type

[**[VideosForXMLInner]**](VideosForXMLInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/atom+xml, application/json, application/rss+xml, application/xml, text/xml

