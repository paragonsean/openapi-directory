# PeerTube.ConfigApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delCustomConfig**](ConfigApi.md#delCustomConfig) | **DELETE** /api/v1/config/custom | Delete instance runtime configuration
[**getAbout**](ConfigApi.md#getAbout) | **GET** /api/v1/config/about | Get instance \&quot;About\&quot; information
[**getConfig**](ConfigApi.md#getConfig) | **GET** /api/v1/config | Get instance public configuration
[**getCustomConfig**](ConfigApi.md#getCustomConfig) | **GET** /api/v1/config/custom | Get instance runtime configuration
[**putCustomConfig**](ConfigApi.md#putCustomConfig) | **PUT** /api/v1/config/custom | Set instance runtime configuration



## delCustomConfig

> delCustomConfig()

Delete instance runtime configuration

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.ConfigApi();
apiInstance.delCustomConfig((error, data, response) => {
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


## getAbout

> ServerConfigAbout getAbout()

Get instance \&quot;About\&quot; information

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.ConfigApi();
apiInstance.getAbout((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ServerConfigAbout**](ServerConfigAbout.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfig

> ServerConfig getConfig()

Get instance public configuration

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.ConfigApi();
apiInstance.getConfig((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ServerConfig**](ServerConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCustomConfig

> ServerConfigCustom getCustomConfig()

Get instance runtime configuration

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.ConfigApi();
apiInstance.getCustomConfig((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ServerConfigCustom**](ServerConfigCustom.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putCustomConfig

> putCustomConfig()

Set instance runtime configuration

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.ConfigApi();
apiInstance.putCustomConfig((error, data, response) => {
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

