# LogicManagementClient.WorkflowVersionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflowVersionsGet**](WorkflowVersionsApi.md#workflowVersionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/versions/{versionId} | 
[**workflowVersionsList**](WorkflowVersionsApi.md#workflowVersionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/versions | 



## workflowVersionsGet

> WorkflowVersion workflowVersionsGet(subscriptionId, resourceGroupName, workflowName, versionId, apiVersion)



Gets a workflow version.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowVersionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let versionId = "versionId_example"; // String | The workflow versionId.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowVersionsGet(subscriptionId, resourceGroupName, workflowName, versionId, apiVersion, (error, data, response) => {
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
 **versionId** | **String**| The workflow versionId. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowVersion**](WorkflowVersion.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowVersionsList

> WorkflowVersionListResult workflowVersionsList(subscriptionId, resourceGroupName, workflowName, apiVersion, opts)



Gets a list of workflow versions.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowVersionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56 // Number | The number of items to be included in the result.
};
apiInstance.workflowVersionsList(subscriptionId, resourceGroupName, workflowName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 

### Return type

[**WorkflowVersionListResult**](WorkflowVersionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

