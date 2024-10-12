# PeerTube.VideoBlocksApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoBlock**](VideoBlocksApi.md#addVideoBlock) | **POST** /api/v1/videos/{id}/blacklist | Block a video
[**delVideoBlock**](VideoBlocksApi.md#delVideoBlock) | **DELETE** /api/v1/videos/{id}/blacklist | Unblock a video by its id
[**getVideoBlocks**](VideoBlocksApi.md#getVideoBlocks) | **GET** /api/v1/videos/blacklist | List video blocks



## addVideoBlock

> addVideoBlock(id)

Block a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoBlocksApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.addVideoBlock(id, (error, data, response) => {
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


## delVideoBlock

> delVideoBlock(id)

Unblock a video by its id

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoBlocksApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.delVideoBlock(id, (error, data, response) => {
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


## getVideoBlocks

> GetVideoBlocks200Response getVideoBlocks(opts)

List video blocks

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoBlocksApi();
let opts = {
  'type': 56, // Number | list only blocks that match this type: - `1`: manual block - `2`: automatic block that needs review 
  'search': "search_example", // String | plain search that will match with video titles, and more
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "sort_example" // String | Sort blocklists by criteria
};
apiInstance.getVideoBlocks(opts, (error, data, response) => {
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
 **type** | **Number**| list only blocks that match this type: - &#x60;1&#x60;: manual block - &#x60;2&#x60;: automatic block that needs review  | [optional] 
 **search** | **String**| plain search that will match with video titles, and more | [optional] 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort blocklists by criteria | [optional] 

### Return type

[**GetVideoBlocks200Response**](GetVideoBlocks200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

