# TwilioTaskrouter.TaskrouterV1WorkerApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWorker**](TaskrouterV1WorkerApi.md#createWorker) | **POST** /v1/Workspaces/{WorkspaceSid}/Workers | 
[**deleteWorker**](TaskrouterV1WorkerApi.md#deleteWorker) | **DELETE** /v1/Workspaces/{WorkspaceSid}/Workers/{Sid} | 
[**fetchWorker**](TaskrouterV1WorkerApi.md#fetchWorker) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/{Sid} | 
[**listWorker**](TaskrouterV1WorkerApi.md#listWorker) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers | 
[**updateWorker**](TaskrouterV1WorkerApi.md#updateWorker) | **POST** /v1/Workspaces/{WorkspaceSid}/Workers/{Sid} | 



## createWorker

> TaskrouterV1WorkspaceWorker createWorker(workspaceSid, friendlyName, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkerApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace that the new Worker belongs to.
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the new Worker. It can be up to 64 characters long.
let opts = {
  'activitySid': "activitySid_example", // String | The SID of a valid Activity that will describe the new Worker's initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information. If not provided, the new Worker's initial state is the `default_activity_sid` configured on the Workspace.
  'attributes': "attributes_example" // String | A valid JSON string that describes the new Worker. For example: `{ \\\"email\\\": \\\"Bob@example.com\\\", \\\"phone\\\": \\\"+5095551234\\\" }`. This data is passed to the `assignment_callback_url` when TaskRouter assigns a Task to the Worker. Defaults to {}.
};
apiInstance.createWorker(workspaceSid, friendlyName, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace that the new Worker belongs to. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the new Worker. It can be up to 64 characters long. | 
 **activitySid** | **String**| The SID of a valid Activity that will describe the new Worker&#39;s initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information. If not provided, the new Worker&#39;s initial state is the &#x60;default_activity_sid&#x60; configured on the Workspace. | [optional] 
 **attributes** | **String**| A valid JSON string that describes the new Worker. For example: &#x60;{ \\\&quot;email\\\&quot;: \\\&quot;Bob@example.com\\\&quot;, \\\&quot;phone\\\&quot;: \\\&quot;+5095551234\\\&quot; }&#x60;. This data is passed to the &#x60;assignment_callback_url&#x60; when TaskRouter assigns a Task to the Worker. Defaults to {}. | [optional] 

### Return type

[**TaskrouterV1WorkspaceWorker**](TaskrouterV1WorkspaceWorker.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteWorker

> deleteWorker(workspaceSid, sid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkerApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Worker to delete.
let sid = "sid_example"; // String | The SID of the Worker resource to delete.
let opts = {
  'ifMatch': "ifMatch_example" // String | The If-Match HTTP request header
};
apiInstance.deleteWorker(workspaceSid, sid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Worker to delete. | 
 **sid** | **String**| The SID of the Worker resource to delete. | 
 **ifMatch** | **String**| The If-Match HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchWorker

> TaskrouterV1WorkspaceWorker fetchWorker(workspaceSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkerApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Worker to fetch.
let sid = "sid_example"; // String | The SID of the Worker resource to fetch.
apiInstance.fetchWorker(workspaceSid, sid, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Worker to fetch. | 
 **sid** | **String**| The SID of the Worker resource to fetch. | 

### Return type

[**TaskrouterV1WorkspaceWorker**](TaskrouterV1WorkspaceWorker.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWorker

> ListWorkerResponse listWorker(workspaceSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkerApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workers to read.
let opts = {
  'activityName': "activityName_example", // String | The `activity_name` of the Worker resources to read.
  'activitySid': "activitySid_example", // String | The `activity_sid` of the Worker resources to read.
  'available': "available_example", // String | Whether to return only Worker resources that are available or unavailable. Can be `true`, `1`, or `yes` to return Worker resources that are available, and `false`, or any value returns the Worker resources that are not available.
  'friendlyName': "friendlyName_example", // String | The `friendly_name` of the Worker resources to read.
  'targetWorkersExpression': "targetWorkersExpression_example", // String | Filter by Workers that would match an expression. In addition to fields in the workers' attributes, the expression can include the following worker fields: `sid`, `friendly_name`, `activity_sid`, or `activity_name`
  'taskQueueName': "taskQueueName_example", // String | The `friendly_name` of the TaskQueue that the Workers to read are eligible for.
  'taskQueueSid': "taskQueueSid_example", // String | The SID of the TaskQueue that the Workers to read are eligible for.
  'ordering': "ordering_example", // String | Sorting parameter for Workers
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listWorker(workspaceSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Workers to read. | 
 **activityName** | **String**| The &#x60;activity_name&#x60; of the Worker resources to read. | [optional] 
 **activitySid** | **String**| The &#x60;activity_sid&#x60; of the Worker resources to read. | [optional] 
 **available** | **String**| Whether to return only Worker resources that are available or unavailable. Can be &#x60;true&#x60;, &#x60;1&#x60;, or &#x60;yes&#x60; to return Worker resources that are available, and &#x60;false&#x60;, or any value returns the Worker resources that are not available. | [optional] 
 **friendlyName** | **String**| The &#x60;friendly_name&#x60; of the Worker resources to read. | [optional] 
 **targetWorkersExpression** | **String**| Filter by Workers that would match an expression. In addition to fields in the workers&#39; attributes, the expression can include the following worker fields: &#x60;sid&#x60;, &#x60;friendly_name&#x60;, &#x60;activity_sid&#x60;, or &#x60;activity_name&#x60; | [optional] 
 **taskQueueName** | **String**| The &#x60;friendly_name&#x60; of the TaskQueue that the Workers to read are eligible for. | [optional] 
 **taskQueueSid** | **String**| The SID of the TaskQueue that the Workers to read are eligible for. | [optional] 
 **ordering** | **String**| Sorting parameter for Workers | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListWorkerResponse**](ListWorkerResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWorker

> TaskrouterV1WorkspaceWorker updateWorker(workspaceSid, sid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkerApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Worker to update.
let sid = "sid_example"; // String | The SID of the Worker resource to update.
let opts = {
  'ifMatch': "ifMatch_example", // String | The If-Match HTTP request header
  'activitySid': "activitySid_example", // String | The SID of a valid Activity that will describe the Worker's initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information.
  'attributes': "attributes_example", // String | The JSON string that describes the Worker. For example: `{ \\\"email\\\": \\\"Bob@example.com\\\", \\\"phone\\\": \\\"+5095551234\\\" }`. This data is passed to the `assignment_callback_url` when TaskRouter assigns a Task to the Worker. Defaults to {}.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the Worker. It can be up to 64 characters long.
  'rejectPendingReservations': true // Boolean | Whether to reject the Worker's pending reservations. This option is only valid if the Worker's new [Activity](https://www.twilio.com/docs/taskrouter/api/activity) resource has its `availability` property set to `False`.
};
apiInstance.updateWorker(workspaceSid, sid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Worker to update. | 
 **sid** | **String**| The SID of the Worker resource to update. | 
 **ifMatch** | **String**| The If-Match HTTP request header | [optional] 
 **activitySid** | **String**| The SID of a valid Activity that will describe the Worker&#39;s initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information. | [optional] 
 **attributes** | **String**| The JSON string that describes the Worker. For example: &#x60;{ \\\&quot;email\\\&quot;: \\\&quot;Bob@example.com\\\&quot;, \\\&quot;phone\\\&quot;: \\\&quot;+5095551234\\\&quot; }&#x60;. This data is passed to the &#x60;assignment_callback_url&#x60; when TaskRouter assigns a Task to the Worker. Defaults to {}. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the Worker. It can be up to 64 characters long. | [optional] 
 **rejectPendingReservations** | **Boolean**| Whether to reject the Worker&#39;s pending reservations. This option is only valid if the Worker&#39;s new [Activity](https://www.twilio.com/docs/taskrouter/api/activity) resource has its &#x60;availability&#x60; property set to &#x60;False&#x60;. | [optional] 

### Return type

[**TaskrouterV1WorkspaceWorker**](TaskrouterV1WorkspaceWorker.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

