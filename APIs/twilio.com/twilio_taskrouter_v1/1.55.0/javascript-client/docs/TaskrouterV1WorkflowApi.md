# TwilioTaskrouter.TaskrouterV1WorkflowApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWorkflow**](TaskrouterV1WorkflowApi.md#createWorkflow) | **POST** /v1/Workspaces/{WorkspaceSid}/Workflows | 
[**deleteWorkflow**](TaskrouterV1WorkflowApi.md#deleteWorkflow) | **DELETE** /v1/Workspaces/{WorkspaceSid}/Workflows/{Sid} | 
[**fetchWorkflow**](TaskrouterV1WorkflowApi.md#fetchWorkflow) | **GET** /v1/Workspaces/{WorkspaceSid}/Workflows/{Sid} | 
[**listWorkflow**](TaskrouterV1WorkflowApi.md#listWorkflow) | **GET** /v1/Workspaces/{WorkspaceSid}/Workflows | 
[**updateWorkflow**](TaskrouterV1WorkflowApi.md#updateWorkflow) | **POST** /v1/Workspaces/{WorkspaceSid}/Workflows/{Sid} | 



## createWorkflow

> TaskrouterV1WorkspaceWorkflow createWorkflow(workspaceSid, configuration, friendlyName, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkflowApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace that the new Workflow to create belongs to.
let configuration = "configuration_example"; // String | A JSON string that contains the rules to apply to the Workflow. See [Configuring Workflows](https://www.twilio.com/docs/taskrouter/workflow-configuration) for more information.
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Workflow resource. For example, `Inbound Call Workflow` or `2014 Outbound Campaign`.
let opts = {
  'assignmentCallbackUrl': "assignmentCallbackUrl_example", // String | The URL from your application that will process task assignment events. See [Handling Task Assignment Callback](https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks) for more details.
  'fallbackAssignmentCallbackUrl': "fallbackAssignmentCallbackUrl_example", // String | The URL that we should call when a call to the `assignment_callback_url` fails.
  'taskReservationTimeout': 56 // Number | How long TaskRouter will wait for a confirmation response from your application after it assigns a Task to a Worker. Can be up to `86,400` (24 hours) and the default is `120`.
};
apiInstance.createWorkflow(workspaceSid, configuration, friendlyName, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace that the new Workflow to create belongs to. | 
 **configuration** | **String**| A JSON string that contains the rules to apply to the Workflow. See [Configuring Workflows](https://www.twilio.com/docs/taskrouter/workflow-configuration) for more information. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the Workflow resource. For example, &#x60;Inbound Call Workflow&#x60; or &#x60;2014 Outbound Campaign&#x60;. | 
 **assignmentCallbackUrl** | **String**| The URL from your application that will process task assignment events. See [Handling Task Assignment Callback](https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks) for more details. | [optional] 
 **fallbackAssignmentCallbackUrl** | **String**| The URL that we should call when a call to the &#x60;assignment_callback_url&#x60; fails. | [optional] 
 **taskReservationTimeout** | **Number**| How long TaskRouter will wait for a confirmation response from your application after it assigns a Task to a Worker. Can be up to &#x60;86,400&#x60; (24 hours) and the default is &#x60;120&#x60;. | [optional] 

### Return type

[**TaskrouterV1WorkspaceWorkflow**](TaskrouterV1WorkspaceWorkflow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteWorkflow

> deleteWorkflow(workspaceSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkflowApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workflow to delete.
let sid = "sid_example"; // String | The SID of the Workflow resource to delete.
apiInstance.deleteWorkflow(workspaceSid, sid, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Workflow to delete. | 
 **sid** | **String**| The SID of the Workflow resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchWorkflow

> TaskrouterV1WorkspaceWorkflow fetchWorkflow(workspaceSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkflowApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workflow to fetch.
let sid = "sid_example"; // String | The SID of the Workflow resource to fetch.
apiInstance.fetchWorkflow(workspaceSid, sid, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Workflow to fetch. | 
 **sid** | **String**| The SID of the Workflow resource to fetch. | 

### Return type

[**TaskrouterV1WorkspaceWorkflow**](TaskrouterV1WorkspaceWorkflow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWorkflow

> ListWorkflowResponse listWorkflow(workspaceSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkflowApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workflow to read.
let opts = {
  'friendlyName': "friendlyName_example", // String | The `friendly_name` of the Workflow resources to read.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listWorkflow(workspaceSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Workflow to read. | 
 **friendlyName** | **String**| The &#x60;friendly_name&#x60; of the Workflow resources to read. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListWorkflowResponse**](ListWorkflowResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWorkflow

> TaskrouterV1WorkspaceWorkflow updateWorkflow(workspaceSid, sid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkflowApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workflow to update.
let sid = "sid_example"; // String | The SID of the Workflow resource to update.
let opts = {
  'assignmentCallbackUrl': "assignmentCallbackUrl_example", // String | The URL from your application that will process task assignment events. See [Handling Task Assignment Callback](https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks) for more details.
  'configuration': "configuration_example", // String | A JSON string that contains the rules to apply to the Workflow. See [Configuring Workflows](https://www.twilio.com/docs/taskrouter/workflow-configuration) for more information.
  'fallbackAssignmentCallbackUrl': "fallbackAssignmentCallbackUrl_example", // String | The URL that we should call when a call to the `assignment_callback_url` fails.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the Workflow resource. For example, `Inbound Call Workflow` or `2014 Outbound Campaign`.
  'reEvaluateTasks': "reEvaluateTasks_example", // String | Whether or not to re-evaluate Tasks. The default is `false`, which means Tasks in the Workflow will not be processed through the assignment loop again.
  'taskReservationTimeout': 56 // Number | How long TaskRouter will wait for a confirmation response from your application after it assigns a Task to a Worker. Can be up to `86,400` (24 hours) and the default is `120`.
};
apiInstance.updateWorkflow(workspaceSid, sid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Workflow to update. | 
 **sid** | **String**| The SID of the Workflow resource to update. | 
 **assignmentCallbackUrl** | **String**| The URL from your application that will process task assignment events. See [Handling Task Assignment Callback](https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks) for more details. | [optional] 
 **configuration** | **String**| A JSON string that contains the rules to apply to the Workflow. See [Configuring Workflows](https://www.twilio.com/docs/taskrouter/workflow-configuration) for more information. | [optional] 
 **fallbackAssignmentCallbackUrl** | **String**| The URL that we should call when a call to the &#x60;assignment_callback_url&#x60; fails. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the Workflow resource. For example, &#x60;Inbound Call Workflow&#x60; or &#x60;2014 Outbound Campaign&#x60;. | [optional] 
 **reEvaluateTasks** | **String**| Whether or not to re-evaluate Tasks. The default is &#x60;false&#x60;, which means Tasks in the Workflow will not be processed through the assignment loop again. | [optional] 
 **taskReservationTimeout** | **Number**| How long TaskRouter will wait for a confirmation response from your application after it assigns a Task to a Worker. Can be up to &#x60;86,400&#x60; (24 hours) and the default is &#x60;120&#x60;. | [optional] 

### Return type

[**TaskrouterV1WorkspaceWorkflow**](TaskrouterV1WorkspaceWorkflow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

