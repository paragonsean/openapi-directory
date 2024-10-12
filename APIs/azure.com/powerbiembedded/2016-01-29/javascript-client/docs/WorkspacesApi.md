# PowerBiEmbeddedManagementClient.WorkspacesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspacesList**](WorkspacesApi.md#workspacesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName}/workspaces | 



## workspacesList

> WorkspaceList workspacesList(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion)



Retrieves all existing Power BI workspaces in the specified workspace collection.

### Example

```javascript
import PowerBiEmbeddedManagementClient from 'power_bi_embedded_management_client';

let apiInstance = new PowerBiEmbeddedManagementClient.WorkspacesApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
let workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.workspacesList(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Azure resource group | 
 **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**WorkspaceList**](WorkspaceList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

