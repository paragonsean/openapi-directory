# PeerTube.MyHistoryApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1UsersMeHistoryVideosGet**](MyHistoryApi.md#apiV1UsersMeHistoryVideosGet) | **GET** /api/v1/users/me/history/videos | List watched videos history
[**apiV1UsersMeHistoryVideosRemovePost**](MyHistoryApi.md#apiV1UsersMeHistoryVideosRemovePost) | **POST** /api/v1/users/me/history/videos/remove | Clear video history
[**apiV1UsersMeHistoryVideosVideoIdDelete**](MyHistoryApi.md#apiV1UsersMeHistoryVideosVideoIdDelete) | **DELETE** /api/v1/users/me/history/videos/{videoId} | Delete history element



## apiV1UsersMeHistoryVideosGet

> VideoListResponse apiV1UsersMeHistoryVideosGet(opts)

List watched videos history

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyHistoryApi();
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'search': "search_example" // String | Plain text search, applied to various parts of the model depending on endpoint
};
apiInstance.apiV1UsersMeHistoryVideosGet(opts, (error, data, response) => {
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
 **search** | **String**| Plain text search, applied to various parts of the model depending on endpoint | [optional] 

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1UsersMeHistoryVideosRemovePost

> apiV1UsersMeHistoryVideosRemovePost(opts)

Clear video history

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyHistoryApi();
let opts = {
  'beforeDate': new Date("2013-10-20T19:20:30+01:00") // Date | history before this date will be deleted
};
apiInstance.apiV1UsersMeHistoryVideosRemovePost(opts, (error, data, response) => {
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
 **beforeDate** | **Date**| history before this date will be deleted | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## apiV1UsersMeHistoryVideosVideoIdDelete

> apiV1UsersMeHistoryVideosVideoIdDelete(videoId)

Delete history element

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyHistoryApi();
let videoId = 56; // Number | 
apiInstance.apiV1UsersMeHistoryVideosVideoIdDelete(videoId, (error, data, response) => {
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
 **videoId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

