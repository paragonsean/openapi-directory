# TwilioTaskrouter.TaskrouterV1TaskChannelApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTaskChannel**](TaskrouterV1TaskChannelApi.md#createTaskChannel) | **POST** /v1/Workspaces/{WorkspaceSid}/TaskChannels | 
[**deleteTaskChannel**](TaskrouterV1TaskChannelApi.md#deleteTaskChannel) | **DELETE** /v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid} | 
[**fetchTaskChannel**](TaskrouterV1TaskChannelApi.md#fetchTaskChannel) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid} | 
[**listTaskChannel**](TaskrouterV1TaskChannelApi.md#listTaskChannel) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskChannels | 
[**updateTaskChannel**](TaskrouterV1TaskChannelApi.md#updateTaskChannel) | **POST** /v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid} | 



## createTaskChannel

> TaskrouterV1WorkspaceTaskChannel createTaskChannel(workspaceSid, friendlyName, uniqueName, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskChannelApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace that the new Task Channel belongs to.
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long.
let uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the Task Channel, such as `voice` or `sms`.
let opts = {
  'channelOptimizedRouting': true // Boolean | Whether the Task Channel should prioritize Workers that have been idle. If `true`, Workers that have been idle the longest are prioritized.
};
apiInstance.createTaskChannel(workspaceSid, friendlyName, uniqueName, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace that the new Task Channel belongs to. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long. | 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the Task Channel, such as &#x60;voice&#x60; or &#x60;sms&#x60;. | 
 **channelOptimizedRouting** | **Boolean**| Whether the Task Channel should prioritize Workers that have been idle. If &#x60;true&#x60;, Workers that have been idle the longest are prioritized. | [optional] 

### Return type

[**TaskrouterV1WorkspaceTaskChannel**](TaskrouterV1WorkspaceTaskChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteTaskChannel

> deleteTaskChannel(workspaceSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskChannelApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task Channel to delete.
let sid = "sid_example"; // String | The SID of the Task Channel resource to delete.
apiInstance.deleteTaskChannel(workspaceSid, sid, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Task Channel to delete. | 
 **sid** | **String**| The SID of the Task Channel resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchTaskChannel

> TaskrouterV1WorkspaceTaskChannel fetchTaskChannel(workspaceSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskChannelApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task Channel to fetch.
let sid = "sid_example"; // String | The SID of the Task Channel resource to fetch.
apiInstance.fetchTaskChannel(workspaceSid, sid, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Task Channel to fetch. | 
 **sid** | **String**| The SID of the Task Channel resource to fetch. | 

### Return type

[**TaskrouterV1WorkspaceTaskChannel**](TaskrouterV1WorkspaceTaskChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTaskChannel

> ListTaskChannelResponse listTaskChannel(workspaceSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskChannelApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task Channel to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listTaskChannel(workspaceSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Task Channel to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListTaskChannelResponse**](ListTaskChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTaskChannel

> TaskrouterV1WorkspaceTaskChannel updateTaskChannel(workspaceSid, sid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskChannelApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task Channel to update.
let sid = "sid_example"; // String | The SID of the Task Channel resource to update.
let opts = {
  'channelOptimizedRouting': true, // Boolean | Whether the TaskChannel should prioritize Workers that have been idle. If `true`, Workers that have been idle the longest are prioritized.
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long.
};
apiInstance.updateTaskChannel(workspaceSid, sid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Task Channel to update. | 
 **sid** | **String**| The SID of the Task Channel resource to update. | 
 **channelOptimizedRouting** | **Boolean**| Whether the TaskChannel should prioritize Workers that have been idle. If &#x60;true&#x60;, Workers that have been idle the longest are prioritized. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long. | [optional] 

### Return type

[**TaskrouterV1WorkspaceTaskChannel**](TaskrouterV1WorkspaceTaskChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

