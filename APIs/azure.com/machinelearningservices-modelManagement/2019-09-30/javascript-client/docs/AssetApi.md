# AzureMachineLearningModelManagementService.AssetApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assetsCreate**](AssetApi.md#assetsCreate) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets | Create an Asset.
[**assetsDelete**](AssetApi.md#assetsDelete) | **DELETE** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets/{id} | Delete an Asset.
[**assetsListQuery**](AssetApi.md#assetsListQuery) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets | Query the list of Assets in a workspace.
[**assetsPatch**](AssetApi.md#assetsPatch) | **PATCH** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets/{id} | Update an Asset.
[**assetsQueryById**](AssetApi.md#assetsQueryById) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets/{id} | Get an Asset.



## assetsCreate

> Asset assetsCreate(subscriptionId, resourceGroup, workspace, opts)

Create an Asset.

Create an Asset from the provided payload.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.AssetApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let opts = {
  'asset': new AzureMachineLearningModelManagementService.Asset() // Asset | The Asset to be created.
};
apiInstance.assetsCreate(subscriptionId, resourceGroup, workspace, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspace** | **String**| The name of the workspace. | 
 **asset** | [**Asset**](Asset.md)| The Asset to be created. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assetsDelete

> assetsDelete(subscriptionId, resourceGroup, workspace, id)

Delete an Asset.

Delete the specified Asset.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.AssetApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Id of the Asset to delete.
apiInstance.assetsDelete(subscriptionId, resourceGroup, workspace, id, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspace** | **String**| The name of the workspace. | 
 **id** | **String**| The Id of the Asset to delete. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assetsListQuery

> PaginatedAssetList assetsListQuery(subscriptionId, resourceGroup, workspace, opts)

Query the list of Assets in a workspace.

If no filter is passed, the query lists all the Assets in the given workspace. The returned list is paginated and the count of items in each page is an optional parameter.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.AssetApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let opts = {
  'runId': "runId_example", // String | The run Id associated with the Assets.
  'name': "name_example", // String | The object name.
  'count': 56, // Number | The number of items to retrieve in a page.
  'skipToken': "skipToken_example", // String | The continuation token to retrieve the next page.
  'tags': "tags_example", // String | A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key=value              Example: tagKey1,tagKey2,tagKey3=value3
  'properties': "properties_example", // String | A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key=value              Example: propKey1,propKey2,propKey3=value3
  'orderby': "'CreatedAtDesc'" // String | An option for specifying how to order the list.
};
apiInstance.assetsListQuery(subscriptionId, resourceGroup, workspace, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspace** | **String**| The name of the workspace. | 
 **runId** | **String**| The run Id associated with the Assets. | [optional] 
 **name** | **String**| The object name. | [optional] 
 **count** | **Number**| The number of items to retrieve in a page. | [optional] 
 **skipToken** | **String**| The continuation token to retrieve the next page. | [optional] 
 **tags** | **String**| A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key&#x3D;value              Example: tagKey1,tagKey2,tagKey3&#x3D;value3 | [optional] 
 **properties** | **String**| A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key&#x3D;value              Example: propKey1,propKey2,propKey3&#x3D;value3 | [optional] 
 **orderby** | **String**| An option for specifying how to order the list. | [optional] [default to &#39;CreatedAtDesc&#39;]

### Return type

[**PaginatedAssetList**](PaginatedAssetList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assetsPatch

> Asset assetsPatch(subscriptionId, resourceGroup, workspace, id, patch)

Update an Asset.

Patch a specific Asset.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.AssetApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Id of the Asset to patch.
let patch = [new AzureMachineLearningModelManagementService.JsonPatchOperation()]; // [JsonPatchOperation] | The payload that is used to patch an Asset.
apiInstance.assetsPatch(subscriptionId, resourceGroup, workspace, id, patch, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspace** | **String**| The name of the workspace. | 
 **id** | **String**| The Id of the Asset to patch. | 
 **patch** | [**[JsonPatchOperation]**](JsonPatchOperation.md)| The payload that is used to patch an Asset. | 

### Return type

[**Asset**](Asset.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json


## assetsQueryById

> Asset assetsQueryById(subscriptionId, resourceGroup, workspace, id)

Get an Asset.

Get an Asset by Id.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.AssetApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Asset Id.
apiInstance.assetsQueryById(subscriptionId, resourceGroup, workspace, id, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspace** | **String**| The name of the workspace. | 
 **id** | **String**| The Asset Id. | 

### Return type

[**Asset**](Asset.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

