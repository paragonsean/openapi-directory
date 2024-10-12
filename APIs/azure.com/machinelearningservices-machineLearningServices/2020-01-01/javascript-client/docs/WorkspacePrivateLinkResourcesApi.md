# AzureMachineLearningWorkspaces.WorkspacePrivateLinkResourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateLinkResourcesListByWorkspace**](WorkspacePrivateLinkResourcesApi.md#privateLinkResourcesListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/privateLinkResources | 



## privateLinkResourcesListByWorkspace

> PrivateLinkResourceListResult privateLinkResourcesListByWorkspace(subscriptionId, resourceGroupName, workspaceName, apiVersion)



Gets the private link resources that need to be created for a workspace.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspacePrivateLinkResourcesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
apiInstance.privateLinkResourcesListByWorkspace(subscriptionId, resourceGroupName, workspaceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 

### Return type

[**PrivateLinkResourceListResult**](PrivateLinkResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

