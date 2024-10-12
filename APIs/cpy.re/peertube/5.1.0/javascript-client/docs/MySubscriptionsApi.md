# PeerTube.MySubscriptionsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1UsersMeSubscriptionsExistGet**](MySubscriptionsApi.md#apiV1UsersMeSubscriptionsExistGet) | **GET** /api/v1/users/me/subscriptions/exist | Get if subscriptions exist for my user
[**apiV1UsersMeSubscriptionsGet**](MySubscriptionsApi.md#apiV1UsersMeSubscriptionsGet) | **GET** /api/v1/users/me/subscriptions | Get my user subscriptions
[**apiV1UsersMeSubscriptionsPost**](MySubscriptionsApi.md#apiV1UsersMeSubscriptionsPost) | **POST** /api/v1/users/me/subscriptions | Add subscription to my user
[**apiV1UsersMeSubscriptionsSubscriptionHandleDelete**](MySubscriptionsApi.md#apiV1UsersMeSubscriptionsSubscriptionHandleDelete) | **DELETE** /api/v1/users/me/subscriptions/{subscriptionHandle} | Delete subscription of my user
[**apiV1UsersMeSubscriptionsSubscriptionHandleGet**](MySubscriptionsApi.md#apiV1UsersMeSubscriptionsSubscriptionHandleGet) | **GET** /api/v1/users/me/subscriptions/{subscriptionHandle} | Get subscription of my user
[**apiV1UsersMeSubscriptionsVideosGet**](MySubscriptionsApi.md#apiV1UsersMeSubscriptionsVideosGet) | **GET** /api/v1/users/me/subscriptions/videos | List videos of subscriptions of my user



## apiV1UsersMeSubscriptionsExistGet

> Object apiV1UsersMeSubscriptionsExistGet(uris)

Get if subscriptions exist for my user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MySubscriptionsApi();
let uris = ["null"]; // [String] | list of uris to check if each is part of the user subscriptions
apiInstance.apiV1UsersMeSubscriptionsExistGet(uris, (error, data, response) => {
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
 **uris** | [**[String]**](String.md)| list of uris to check if each is part of the user subscriptions | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1UsersMeSubscriptionsGet

> VideoChannelList apiV1UsersMeSubscriptionsGet(opts)

Get my user subscriptions

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MySubscriptionsApi();
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1UsersMeSubscriptionsGet(opts, (error, data, response) => {
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1UsersMeSubscriptionsPost

> apiV1UsersMeSubscriptionsPost(opts)

Add subscription to my user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MySubscriptionsApi();
let opts = {
  'apiV1UsersMeSubscriptionsPostRequest': {"uri":"008a0e54-375d-49d0-8379-143202e24152@video.lqdn.fr"} // ApiV1UsersMeSubscriptionsPostRequest | 
};
apiInstance.apiV1UsersMeSubscriptionsPost(opts, (error, data, response) => {
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
 **apiV1UsersMeSubscriptionsPostRequest** | [**ApiV1UsersMeSubscriptionsPostRequest**](ApiV1UsersMeSubscriptionsPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV1UsersMeSubscriptionsSubscriptionHandleDelete

> apiV1UsersMeSubscriptionsSubscriptionHandleDelete(subscriptionHandle)

Delete subscription of my user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MySubscriptionsApi();
let subscriptionHandle = "my_username | my_username@example.com"; // String | The subscription handle
apiInstance.apiV1UsersMeSubscriptionsSubscriptionHandleDelete(subscriptionHandle, (error, data, response) => {
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
 **subscriptionHandle** | **String**| The subscription handle | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1UsersMeSubscriptionsSubscriptionHandleGet

> VideoChannel apiV1UsersMeSubscriptionsSubscriptionHandleGet(subscriptionHandle)

Get subscription of my user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MySubscriptionsApi();
let subscriptionHandle = "my_username | my_username@example.com"; // String | The subscription handle
apiInstance.apiV1UsersMeSubscriptionsSubscriptionHandleGet(subscriptionHandle, (error, data, response) => {
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
 **subscriptionHandle** | **String**| The subscription handle | 

### Return type

[**VideoChannel**](VideoChannel.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1UsersMeSubscriptionsVideosGet

> VideoListResponse apiV1UsersMeSubscriptionsVideosGet(opts)

List videos of subscriptions of my user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MySubscriptionsApi();
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
apiInstance.apiV1UsersMeSubscriptionsVideosGet(opts, (error, data, response) => {
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

