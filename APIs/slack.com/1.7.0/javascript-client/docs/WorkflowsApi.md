# SlackWebApi.WorkflowsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflowsStepCompleted**](WorkflowsApi.md#workflowsStepCompleted) | **GET** /workflows.stepCompleted | 
[**workflowsStepFailed**](WorkflowsApi.md#workflowsStepFailed) | **GET** /workflows.stepFailed | 
[**workflowsUpdateStep**](WorkflowsApi.md#workflowsUpdateStep) | **GET** /workflows.updateStep | 



## workflowsStepCompleted

> DefaultSuccessTemplate workflowsStepCompleted(token, workflowStepExecuteId, opts)



Indicate that an app&#39;s step in a workflow completed execution.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.WorkflowsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `workflow.steps:execute`
let workflowStepExecuteId = "workflowStepExecuteId_example"; // String | Context identifier that maps to the correct workflow step execution.
let opts = {
  'outputs': "outputs_example" // String | Key-value object of outputs from your step. Keys of this object reflect the configured `key` properties of your [`outputs`](/reference/workflows/workflow_step#output) array from your `workflow_step` object.
};
apiInstance.workflowsStepCompleted(token, workflowStepExecuteId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;workflow.steps:execute&#x60; | 
 **workflowStepExecuteId** | **String**| Context identifier that maps to the correct workflow step execution. | 
 **outputs** | **String**| Key-value object of outputs from your step. Keys of this object reflect the configured &#x60;key&#x60; properties of your [&#x60;outputs&#x60;](/reference/workflows/workflow_step#output) array from your &#x60;workflow_step&#x60; object. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowsStepFailed

> DefaultSuccessTemplate workflowsStepFailed(token, workflowStepExecuteId, error)



Indicate that an app&#39;s step in a workflow failed to execute.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.WorkflowsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `workflow.steps:execute`
let workflowStepExecuteId = "workflowStepExecuteId_example"; // String | Context identifier that maps to the correct workflow step execution.
let error = "error_example"; // String | A JSON-based object with a `message` property that should contain a human readable error message.
apiInstance.workflowsStepFailed(token, workflowStepExecuteId, error, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;workflow.steps:execute&#x60; | 
 **workflowStepExecuteId** | **String**| Context identifier that maps to the correct workflow step execution. | 
 **error** | **String**| A JSON-based object with a &#x60;message&#x60; property that should contain a human readable error message. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowsUpdateStep

> DefaultSuccessTemplate workflowsUpdateStep(token, workflowStepEditId, opts)



Update the configuration for a workflow extension step.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.WorkflowsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `workflow.steps:execute`
let workflowStepEditId = "workflowStepEditId_example"; // String | A context identifier provided with `view_submission` payloads used to call back to `workflows.updateStep`.
let opts = {
  'inputs': "inputs_example", // String | A JSON key-value map of inputs required from a user during configuration. This is the data your app expects to receive when the workflow step starts. **Please note**: the embedded variable format is set and replaced by the workflow system. You cannot create custom variables that will be replaced at runtime. [Read more about variables in workflow steps here](/workflows/steps#variables).
  'outputs': "outputs_example", // String | An JSON array of output objects used during step execution. This is the data your app agrees to provide when your workflow step was executed.
  'stepName': "stepName_example", // String | An optional field that can be used to override the step name that is shown in the Workflow Builder.
  'stepImageUrl': "stepImageUrl_example" // String | An optional field that can be used to override app image that is shown in the Workflow Builder.
};
apiInstance.workflowsUpdateStep(token, workflowStepEditId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;workflow.steps:execute&#x60; | 
 **workflowStepEditId** | **String**| A context identifier provided with &#x60;view_submission&#x60; payloads used to call back to &#x60;workflows.updateStep&#x60;. | 
 **inputs** | **String**| A JSON key-value map of inputs required from a user during configuration. This is the data your app expects to receive when the workflow step starts. **Please note**: the embedded variable format is set and replaced by the workflow system. You cannot create custom variables that will be replaced at runtime. [Read more about variables in workflow steps here](/workflows/steps#variables). | [optional] 
 **outputs** | **String**| An JSON array of output objects used during step execution. This is the data your app agrees to provide when your workflow step was executed. | [optional] 
 **stepName** | **String**| An optional field that can be used to override the step name that is shown in the Workflow Builder. | [optional] 
 **stepImageUrl** | **String**| An optional field that can be used to override app image that is shown in the Workflow Builder. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

