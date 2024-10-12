# LogicManagementClient.WorkflowRunOperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflowRunOperationsGet**](WorkflowRunOperationsApi.md#workflowRunOperationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/operations/{operationId} | 



## workflowRunOperationsGet

> WorkflowRun workflowRunOperationsGet(subscriptionId, resourceGroupName, workflowName, runName, operationId, apiVersion)



Gets an operation for a run.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunOperationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let operationId = "operationId_example"; // String | The workflow operation id.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowRunOperationsGet(subscriptionId, resourceGroupName, workflowName, runName, operationId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **workflowName** | **String**| The workflow name. | 
 **runName** | **String**| The workflow run name. | 
 **operationId** | **String**| The workflow operation id. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowRun**](WorkflowRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

