# PeerTube.StaticVideoFilesApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**staticStreamingPlaylistsHlsFilenameGet**](StaticVideoFilesApi.md#staticStreamingPlaylistsHlsFilenameGet) | **GET** /static/streaming-playlists/hls/{filename} | Get public HLS video file
[**staticStreamingPlaylistsHlsPrivateFilenameGet**](StaticVideoFilesApi.md#staticStreamingPlaylistsHlsPrivateFilenameGet) | **GET** /static/streaming-playlists/hls/private/{filename} | Get private HLS video file
[**staticWebseedFilenameGet**](StaticVideoFilesApi.md#staticWebseedFilenameGet) | **GET** /static/webseed/{filename} | Get public WebTorrent video file
[**staticWebseedPrivateFilenameGet**](StaticVideoFilesApi.md#staticWebseedPrivateFilenameGet) | **GET** /static/webseed/private/{filename} | Get private WebTorrent video file



## staticStreamingPlaylistsHlsFilenameGet

> staticStreamingPlaylistsHlsFilenameGet(filename)

Get public HLS video file

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.StaticVideoFilesApi();
let filename = "filename_example"; // String | Filename
apiInstance.staticStreamingPlaylistsHlsFilenameGet(filename, (error, data, response) => {
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
 **filename** | **String**| Filename | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## staticStreamingPlaylistsHlsPrivateFilenameGet

> staticStreamingPlaylistsHlsPrivateFilenameGet(filename, opts)

Get private HLS video file

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.StaticVideoFilesApi();
let filename = "filename_example"; // String | Filename
let opts = {
  'videoFileToken': "videoFileToken_example", // String | Video file token [generated](#operation/requestVideoToken) by PeerTube so you don't need to provide an OAuth token in the request header.
  'reinjectVideoFileToken': true // Boolean | Ask the server to reinject videoFileToken in URLs in m3u8 playlist
};
apiInstance.staticStreamingPlaylistsHlsPrivateFilenameGet(filename, opts, (error, data, response) => {
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
 **filename** | **String**| Filename | 
 **videoFileToken** | **String**| Video file token [generated](#operation/requestVideoToken) by PeerTube so you don&#39;t need to provide an OAuth token in the request header. | [optional] 
 **reinjectVideoFileToken** | **Boolean**| Ask the server to reinject videoFileToken in URLs in m3u8 playlist | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## staticWebseedFilenameGet

> staticWebseedFilenameGet(filename)

Get public WebTorrent video file

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.StaticVideoFilesApi();
let filename = "filename_example"; // String | Filename
apiInstance.staticWebseedFilenameGet(filename, (error, data, response) => {
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
 **filename** | **String**| Filename | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## staticWebseedPrivateFilenameGet

> staticWebseedPrivateFilenameGet(filename, opts)

Get private WebTorrent video file

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.StaticVideoFilesApi();
let filename = "filename_example"; // String | Filename
let opts = {
  'videoFileToken': "videoFileToken_example" // String | Video file token [generated](#operation/requestVideoToken) by PeerTube so you don't need to provide an OAuth token in the request header.
};
apiInstance.staticWebseedPrivateFilenameGet(filename, opts, (error, data, response) => {
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
 **filename** | **String**| Filename | 
 **videoFileToken** | **String**| Video file token [generated](#operation/requestVideoToken) by PeerTube so you don&#39;t need to provide an OAuth token in the request header. | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

