# LogicManagementClient.WorkflowTriggerHistoriesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflowTriggerHistoriesGet**](WorkflowTriggerHistoriesApi.md#workflowTriggerHistoriesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/histories/{historyName} | 
[**workflowTriggerHistoriesList**](WorkflowTriggerHistoriesApi.md#workflowTriggerHistoriesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/histories | 



## workflowTriggerHistoriesGet

> WorkflowTriggerHistory workflowTriggerHistoriesGet(subscriptionId, resourceGroupName, workflowName, triggerName, historyName, apiVersion)



Gets a workflow trigger history.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowTriggerHistoriesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let triggerName = "triggerName_example"; // String | The workflow trigger name.
let historyName = "historyName_example"; // String | The workflow trigger history name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowTriggerHistoriesGet(subscriptionId, resourceGroupName, workflowName, triggerName, historyName, apiVersion, (error, data, response) => {
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
 **triggerName** | **String**| The workflow trigger name. | 
 **historyName** | **String**| The workflow trigger history name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowTriggerHistory**](WorkflowTriggerHistory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## workflowTriggerHistoriesList

> WorkflowTriggerHistoryListResult workflowTriggerHistoriesList(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, opts)



Gets a list of workflow trigger histories.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowTriggerHistoriesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let triggerName = "triggerName_example"; // String | The workflow trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.workflowTriggerHistoriesList(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, opts, (error, data, response) => {
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
 **triggerName** | **String**| The workflow trigger name. | 
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**WorkflowTriggerHistoryListResult**](WorkflowTriggerHistoryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

