# PeerTube.VideoOwnershipChangeApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1VideosIdGiveOwnershipPost**](VideoOwnershipChangeApi.md#apiV1VideosIdGiveOwnershipPost) | **POST** /api/v1/videos/{id}/give-ownership | Request ownership change
[**apiV1VideosOwnershipGet**](VideoOwnershipChangeApi.md#apiV1VideosOwnershipGet) | **GET** /api/v1/videos/ownership | List video ownership changes
[**apiV1VideosOwnershipIdAcceptPost**](VideoOwnershipChangeApi.md#apiV1VideosOwnershipIdAcceptPost) | **POST** /api/v1/videos/ownership/{id}/accept | Accept ownership change request
[**apiV1VideosOwnershipIdRefusePost**](VideoOwnershipChangeApi.md#apiV1VideosOwnershipIdRefusePost) | **POST** /api/v1/videos/ownership/{id}/refuse | Refuse ownership change request



## apiV1VideosIdGiveOwnershipPost

> apiV1VideosIdGiveOwnershipPost(id, username)

Request ownership change

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoOwnershipChangeApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let username = "username_example"; // String | 
apiInstance.apiV1VideosIdGiveOwnershipPost(id, username, (error, data, response) => {
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
 **username** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## apiV1VideosOwnershipGet

> apiV1VideosOwnershipGet()

List video ownership changes

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoOwnershipChangeApi();
apiInstance.apiV1VideosOwnershipGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1VideosOwnershipIdAcceptPost

> apiV1VideosOwnershipIdAcceptPost(id)

Accept ownership change request

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoOwnershipChangeApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.apiV1VideosOwnershipIdAcceptPost(id, (error, data, response) => {
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


## apiV1VideosOwnershipIdRefusePost

> apiV1VideosOwnershipIdRefusePost(id)

Refuse ownership change request

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoOwnershipChangeApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.apiV1VideosOwnershipIdRefusePost(id, (error, data, response) => {
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

