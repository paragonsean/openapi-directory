# PeerTube.ServerBlocksApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1BlocklistStatusGet_0**](ServerBlocksApi.md#apiV1BlocklistStatusGet_0) | **GET** /api/v1/blocklist/status | Get block status of accounts/hosts
[**apiV1ServerBlocklistServersGet**](ServerBlocksApi.md#apiV1ServerBlocklistServersGet) | **GET** /api/v1/server/blocklist/servers | List server blocks
[**apiV1ServerBlocklistServersHostDelete**](ServerBlocksApi.md#apiV1ServerBlocklistServersHostDelete) | **DELETE** /api/v1/server/blocklist/servers/{host} | Unblock a server by its domain
[**apiV1ServerBlocklistServersPost**](ServerBlocksApi.md#apiV1ServerBlocklistServersPost) | **POST** /api/v1/server/blocklist/servers | Block a server



## apiV1BlocklistStatusGet_0

> BlockStatus apiV1BlocklistStatusGet_0(opts)

Get block status of accounts/hosts

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.ServerBlocksApi();
let opts = {
  'accounts': ["null"], // [String] | Check if these accounts are blocked
  'hosts': ["null"] // [String] | Check if these hosts are blocked
};
apiInstance.apiV1BlocklistStatusGet_0(opts, (error, data, response) => {
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
 **accounts** | [**[String]**](String.md)| Check if these accounts are blocked | [optional] 
 **hosts** | [**[String]**](String.md)| Check if these hosts are blocked | [optional] 

### Return type

[**BlockStatus**](BlockStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1ServerBlocklistServersGet

> apiV1ServerBlocklistServersGet(opts)

List server blocks

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.ServerBlocksApi();
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1ServerBlocklistServersGet(opts, (error, data, response) => {
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
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1ServerBlocklistServersHostDelete

> apiV1ServerBlocklistServersHostDelete(host)

Unblock a server by its domain

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.ServerBlocksApi();
let host = "host_example"; // String | server domain to unblock
apiInstance.apiV1ServerBlocklistServersHostDelete(host, (error, data, response) => {
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
 **host** | **String**| server domain to unblock | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1ServerBlocklistServersPost

> apiV1ServerBlocklistServersPost(opts)

Block a server

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.ServerBlocksApi();
let opts = {
  'apiV1ServerBlocklistServersPostRequest': new PeerTube.ApiV1ServerBlocklistServersPostRequest() // ApiV1ServerBlocklistServersPostRequest | 
};
apiInstance.apiV1ServerBlocklistServersPost(opts, (error, data, response) => {
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
 **apiV1ServerBlocklistServersPostRequest** | [**ApiV1ServerBlocklistServersPostRequest**](ApiV1ServerBlocklistServersPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

