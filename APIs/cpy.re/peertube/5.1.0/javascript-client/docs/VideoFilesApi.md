# PeerTube.VideoFilesApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delVideoHLS**](VideoFilesApi.md#delVideoHLS) | **DELETE** /api/v1/videos/{id}/hls | Delete video HLS files
[**delVideoWebTorrent**](VideoFilesApi.md#delVideoWebTorrent) | **DELETE** /api/v1/videos/{id}/webtorrent | Delete video WebTorrent files



## delVideoHLS

> delVideoHLS(id)

Delete video HLS files

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoFilesApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.delVideoHLS(id, (error, data, response) => {
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


## delVideoWebTorrent

> delVideoWebTorrent(id)

Delete video WebTorrent files

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoFilesApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.delVideoWebTorrent(id, (error, data, response) => {
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

