# TwilioTaskrouter.TaskrouterV1WorkerChannelApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchWorkerChannel**](TaskrouterV1WorkerChannelApi.md#fetchWorkerChannel) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels/{Sid} | 
[**listWorkerChannel**](TaskrouterV1WorkerChannelApi.md#listWorkerChannel) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels | 
[**updateWorkerChannel**](TaskrouterV1WorkerChannelApi.md#updateWorkerChannel) | **POST** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels/{Sid} | 



## fetchWorkerChannel

> TaskrouterV1WorkspaceWorkerWorkerChannel fetchWorkerChannel(workspaceSid, workerSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkerChannelApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerChannel to fetch.
let workerSid = "workerSid_example"; // String | The SID of the Worker with the WorkerChannel to fetch.
let sid = "sid_example"; // String | The SID of the WorkerChannel to fetch.
apiInstance.fetchWorkerChannel(workspaceSid, workerSid, sid, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the WorkerChannel to fetch. | 
 **workerSid** | **String**| The SID of the Worker with the WorkerChannel to fetch. | 
 **sid** | **String**| The SID of the WorkerChannel to fetch. | 

### Return type

[**TaskrouterV1WorkspaceWorkerWorkerChannel**](TaskrouterV1WorkspaceWorkerWorkerChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWorkerChannel

> ListWorkerChannelResponse listWorkerChannel(workspaceSid, workerSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkerChannelApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerChannels to read.
let workerSid = "workerSid_example"; // String | The SID of the Worker with the WorkerChannels to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listWorkerChannel(workspaceSid, workerSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the WorkerChannels to read. | 
 **workerSid** | **String**| The SID of the Worker with the WorkerChannels to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListWorkerChannelResponse**](ListWorkerChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWorkerChannel

> TaskrouterV1WorkspaceWorkerWorkerChannel updateWorkerChannel(workspaceSid, workerSid, sid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkerChannelApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerChannel to update.
let workerSid = "workerSid_example"; // String | The SID of the Worker with the WorkerChannel to update.
let sid = "sid_example"; // String | The SID of the WorkerChannel to update.
let opts = {
  'available': true, // Boolean | Whether the WorkerChannel is available. Set to `false` to prevent the Worker from receiving any new Tasks of this TaskChannel type.
  'capacity': 56 // Number | The total number of Tasks that the Worker should handle for the TaskChannel type. TaskRouter creates reservations for Tasks of this TaskChannel type up to the specified capacity. If the capacity is 0, no new reservations will be created.
};
apiInstance.updateWorkerChannel(workspaceSid, workerSid, sid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the WorkerChannel to update. | 
 **workerSid** | **String**| The SID of the Worker with the WorkerChannel to update. | 
 **sid** | **String**| The SID of the WorkerChannel to update. | 
 **available** | **Boolean**| Whether the WorkerChannel is available. Set to &#x60;false&#x60; to prevent the Worker from receiving any new Tasks of this TaskChannel type. | [optional] 
 **capacity** | **Number**| The total number of Tasks that the Worker should handle for the TaskChannel type. TaskRouter creates reservations for Tasks of this TaskChannel type up to the specified capacity. If the capacity is 0, no new reservations will be created. | [optional] 

### Return type

[**TaskrouterV1WorkspaceWorkerWorkerChannel**](TaskrouterV1WorkspaceWorkerWorkerChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

