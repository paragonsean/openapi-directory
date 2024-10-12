# PeerTube.LogsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInstanceAuditLogs**](LogsApi.md#getInstanceAuditLogs) | **GET** /api/v1/server/audit-logs | Get instance audit logs
[**getInstanceLogs**](LogsApi.md#getInstanceLogs) | **GET** /api/v1/server/logs | Get instance logs
[**sendClientLog**](LogsApi.md#sendClientLog) | **POST** /api/v1/server/logs/client | Send client log



## getInstanceAuditLogs

> [String] getInstanceAuditLogs()

Get instance audit logs

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.LogsApi();
apiInstance.getInstanceAuditLogs((error, data, response) => {
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

**[String]**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInstanceLogs

> [String] getInstanceLogs()

Get instance logs

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.LogsApi();
apiInstance.getInstanceLogs((error, data, response) => {
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

**[String]**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendClientLog

> sendClientLog(opts)

Send client log

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.LogsApi();
let opts = {
  'sendClientLog': new PeerTube.SendClientLog() // SendClientLog | 
};
apiInstance.sendClientLog(opts, (error, data, response) => {
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
 **sendClientLog** | [**SendClientLog**](SendClientLog.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

