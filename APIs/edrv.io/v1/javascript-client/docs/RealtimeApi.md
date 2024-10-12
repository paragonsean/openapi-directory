# EDrvApi.RealtimeApi

All URIs are relative to *http://api.edrv.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRealtime**](RealtimeApi.md#getRealtime) | **GET** /v1/realtime | 



## getRealtime

> getRealtime(secWebsocketProtocol)



Use to request a Websockets handshake

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.RealtimeApi();
let secWebsocketProtocol = "secWebsocketProtocol_example"; // String | The JWT token to use for auth
apiInstance.getRealtime(secWebsocketProtocol, (error, data, response) => {
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
 **secWebsocketProtocol** | **String**| The JWT token to use for auth | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

