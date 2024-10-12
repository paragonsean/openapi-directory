# PeerTube.InstanceFollowsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1ServerFollowersGet**](InstanceFollowsApi.md#apiV1ServerFollowersGet) | **GET** /api/v1/server/followers | List instances following the server
[**apiV1ServerFollowersNameWithHostAcceptPost**](InstanceFollowsApi.md#apiV1ServerFollowersNameWithHostAcceptPost) | **POST** /api/v1/server/followers/{nameWithHost}/accept | Accept a pending follower to your server
[**apiV1ServerFollowersNameWithHostDelete**](InstanceFollowsApi.md#apiV1ServerFollowersNameWithHostDelete) | **DELETE** /api/v1/server/followers/{nameWithHost} | Remove or reject a follower to your server
[**apiV1ServerFollowersNameWithHostRejectPost**](InstanceFollowsApi.md#apiV1ServerFollowersNameWithHostRejectPost) | **POST** /api/v1/server/followers/{nameWithHost}/reject | Reject a pending follower to your server
[**apiV1ServerFollowingGet**](InstanceFollowsApi.md#apiV1ServerFollowingGet) | **GET** /api/v1/server/following | List instances followed by the server
[**apiV1ServerFollowingHostOrHandleDelete**](InstanceFollowsApi.md#apiV1ServerFollowingHostOrHandleDelete) | **DELETE** /api/v1/server/following/{hostOrHandle} | Unfollow an actor (PeerTube instance, channel or account)
[**apiV1ServerFollowingPost**](InstanceFollowsApi.md#apiV1ServerFollowingPost) | **POST** /api/v1/server/following | Follow a list of actors (PeerTube instance, channel or account)



## apiV1ServerFollowersGet

> GetAccountFollowers200Response apiV1ServerFollowersGet(opts)

List instances following the server

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.InstanceFollowsApi();
let opts = {
  'state': "state_example", // String | 
  'actorType': "actorType_example", // String | 
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1ServerFollowersGet(opts, (error, data, response) => {
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
 **state** | **String**|  | [optional] 
 **actorType** | **String**|  | [optional] 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 

### Return type

[**GetAccountFollowers200Response**](GetAccountFollowers200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1ServerFollowersNameWithHostAcceptPost

> apiV1ServerFollowersNameWithHostAcceptPost(nameWithHost)

Accept a pending follower to your server

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.InstanceFollowsApi();
let nameWithHost = "nameWithHost_example"; // String | The remote actor handle to remove from your followers
apiInstance.apiV1ServerFollowersNameWithHostAcceptPost(nameWithHost, (error, data, response) => {
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
 **nameWithHost** | **String**| The remote actor handle to remove from your followers | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1ServerFollowersNameWithHostDelete

> apiV1ServerFollowersNameWithHostDelete(nameWithHost)

Remove or reject a follower to your server

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.InstanceFollowsApi();
let nameWithHost = "nameWithHost_example"; // String | The remote actor handle to remove from your followers
apiInstance.apiV1ServerFollowersNameWithHostDelete(nameWithHost, (error, data, response) => {
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
 **nameWithHost** | **String**| The remote actor handle to remove from your followers | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1ServerFollowersNameWithHostRejectPost

> apiV1ServerFollowersNameWithHostRejectPost(nameWithHost)

Reject a pending follower to your server

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.InstanceFollowsApi();
let nameWithHost = "nameWithHost_example"; // String | The remote actor handle to remove from your followers
apiInstance.apiV1ServerFollowersNameWithHostRejectPost(nameWithHost, (error, data, response) => {
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
 **nameWithHost** | **String**| The remote actor handle to remove from your followers | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1ServerFollowingGet

> GetAccountFollowers200Response apiV1ServerFollowingGet(opts)

List instances followed by the server

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.InstanceFollowsApi();
let opts = {
  'state': "state_example", // String | 
  'actorType': "actorType_example", // String | 
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1ServerFollowingGet(opts, (error, data, response) => {
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
 **state** | **String**|  | [optional] 
 **actorType** | **String**|  | [optional] 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 

### Return type

[**GetAccountFollowers200Response**](GetAccountFollowers200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1ServerFollowingHostOrHandleDelete

> apiV1ServerFollowingHostOrHandleDelete(hostOrHandle)

Unfollow an actor (PeerTube instance, channel or account)

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.InstanceFollowsApi();
let hostOrHandle = "hostOrHandle_example"; // String | The hostOrHandle to unfollow
apiInstance.apiV1ServerFollowingHostOrHandleDelete(hostOrHandle, (error, data, response) => {
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
 **hostOrHandle** | **String**| The hostOrHandle to unfollow | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1ServerFollowingPost

> apiV1ServerFollowingPost(opts)

Follow a list of actors (PeerTube instance, channel or account)

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.InstanceFollowsApi();
let opts = {
  'apiV1ServerFollowingPostRequest': new PeerTube.ApiV1ServerFollowingPostRequest() // ApiV1ServerFollowingPostRequest | 
};
apiInstance.apiV1ServerFollowingPost(opts, (error, data, response) => {
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
 **apiV1ServerFollowingPostRequest** | [**ApiV1ServerFollowingPostRequest**](ApiV1ServerFollowingPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

