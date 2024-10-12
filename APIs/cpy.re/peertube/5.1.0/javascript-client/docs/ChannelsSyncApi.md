# PeerTube.ChannelsSyncApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoChannelSync**](ChannelsSyncApi.md#addVideoChannelSync) | **POST** /api/v1/video-channel-syncs | Create a synchronization for a video channel
[**apiV1AccountsNameVideoChannelSyncsGet_0**](ChannelsSyncApi.md#apiV1AccountsNameVideoChannelSyncsGet_0) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
[**apiV1VideoChannelsChannelHandleImportVideosPost_0**](ChannelsSyncApi.md#apiV1VideoChannelsChannelHandleImportVideosPost_0) | **POST** /api/v1/video-channels/{channelHandle}/import-videos | Import videos in channel
[**delVideoChannelSync**](ChannelsSyncApi.md#delVideoChannelSync) | **DELETE** /api/v1/video-channel-syncs/{channelSyncId} | Delete a video channel synchronization
[**triggerVideoChannelSync**](ChannelsSyncApi.md#triggerVideoChannelSync) | **POST** /api/v1/video-channel-syncs/{channelSyncId}/sync | Triggers the channel synchronization job, fetching all the videos from the remote channel



## addVideoChannelSync

> AddVideoChannelSync200Response addVideoChannelSync(opts)

Create a synchronization for a video channel

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.ChannelsSyncApi();
let opts = {
  'videoChannelSyncCreate': new PeerTube.VideoChannelSyncCreate() // VideoChannelSyncCreate | 
};
apiInstance.addVideoChannelSync(opts, (error, data, response) => {
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
 **videoChannelSyncCreate** | [**VideoChannelSyncCreate**](VideoChannelSyncCreate.md)|  | [optional] 

### Return type

[**AddVideoChannelSync200Response**](AddVideoChannelSync200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiV1AccountsNameVideoChannelSyncsGet_0

> VideoChannelSyncList apiV1AccountsNameVideoChannelSyncsGet_0(name, opts)

List the synchronizations of video channels of an account

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.ChannelsSyncApi();
let name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1AccountsNameVideoChannelSyncsGet_0(name, opts, (error, data, response) => {
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


## apiV1VideoChannelsChannelHandleImportVideosPost_0

> apiV1VideoChannelsChannelHandleImportVideosPost_0(channelHandle, opts)

Import videos in channel

Import a remote channel/playlist videos into a channel

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.ChannelsSyncApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
let opts = {
  'importVideosInChannelCreate': new PeerTube.ImportVideosInChannelCreate() // ImportVideosInChannelCreate | 
};
apiInstance.apiV1VideoChannelsChannelHandleImportVideosPost_0(channelHandle, opts, (error, data, response) => {
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


## delVideoChannelSync

> delVideoChannelSync(channelSyncId)

Delete a video channel synchronization

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.ChannelsSyncApi();
let channelSyncId = 56; // Number | Channel Sync id
apiInstance.delVideoChannelSync(channelSyncId, (error, data, response) => {
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
 **channelSyncId** | **Number**| Channel Sync id | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## triggerVideoChannelSync

> triggerVideoChannelSync(channelSyncId)

Triggers the channel synchronization job, fetching all the videos from the remote channel

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.ChannelsSyncApi();
let channelSyncId = 56; // Number | Channel Sync id
apiInstance.triggerVideoChannelSync(channelSyncId, (error, data, response) => {
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
 **channelSyncId** | **Number**| Channel Sync id | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

