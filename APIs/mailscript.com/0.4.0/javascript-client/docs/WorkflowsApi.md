# Mailscript.WorkflowsApi

All URIs are relative to *https://api.mailscript.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addWorkflow**](WorkflowsApi.md#addWorkflow) | **POST** /workflows | Setup workflow
[**deleteWorkflow**](WorkflowsApi.md#deleteWorkflow) | **DELETE** /workflows/{workflow} | Delete a workflow
[**getAllWorkflows**](WorkflowsApi.md#getAllWorkflows) | **GET** /workflows | Get all workflows you have access to
[**setWorkflow**](WorkflowsApi.md#setWorkflow) | **POST** /workflows/set | Set a property on a workflow
[**updateWorkflow**](WorkflowsApi.md#updateWorkflow) | **PUT** /workflows/{workflow} | Update an workflow



## addWorkflow

> addWorkflow(addWorkflowRequest)

Setup workflow



### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.WorkflowsApi();
let addWorkflowRequest = new Mailscript.AddWorkflowRequest(); // AddWorkflowRequest | Workflow body
apiInstance.addWorkflow(addWorkflowRequest, (error, data, response) => {
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
 **addWorkflowRequest** | [**AddWorkflowRequest**](AddWorkflowRequest.md)| Workflow body | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteWorkflow

> deleteWorkflow(workflow)

Delete a workflow

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.WorkflowsApi();
let workflow = "workflow_example"; // String | ID of the workflow
apiInstance.deleteWorkflow(workflow, (error, data, response) => {
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
 **workflow** | **String**| ID of the workflow | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllWorkflows

> GetAllWorkflowsResponse getAllWorkflows()

Get all workflows you have access to



### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.WorkflowsApi();
apiInstance.getAllWorkflows((error, data, response) => {
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

[**GetAllWorkflowsResponse**](GetAllWorkflowsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setWorkflow

> setWorkflow(setWorkflowRequest)

Set a property on a workflow

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.WorkflowsApi();
let setWorkflowRequest = new Mailscript.SetWorkflowRequest(); // SetWorkflowRequest | Set Workflow body
apiInstance.setWorkflow(setWorkflowRequest, (error, data, response) => {
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
 **setWorkflowRequest** | [**SetWorkflowRequest**](SetWorkflowRequest.md)| Set Workflow body | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWorkflow

> updateWorkflow(workflow, addWorkflowRequest)

Update an workflow

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.WorkflowsApi();
let workflow = "workflow_example"; // String | ID of the workflow
let addWorkflowRequest = new Mailscript.AddWorkflowRequest(); // AddWorkflowRequest | Workflow body
apiInstance.updateWorkflow(workflow, addWorkflowRequest, (error, data, response) => {
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
 **workflow** | **String**| ID of the workflow | 
 **addWorkflowRequest** | [**AddWorkflowRequest**](AddWorkflowRequest.md)| Workflow body | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

