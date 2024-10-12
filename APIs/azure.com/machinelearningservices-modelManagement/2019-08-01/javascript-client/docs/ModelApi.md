# AzureMachineLearningModelManagementService.ModelApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mLModelsDelete**](ModelApi.md#mLModelsDelete) | **DELETE** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models/{id} | Delete the specified Model.
[**mLModelsGetMetrics**](ModelApi.md#mLModelsGetMetrics) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models/{id}/metrics | Retrieve the metrics for a Model.
[**mLModelsListQuery**](ModelApi.md#mLModelsListQuery) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models | Query the list of Models in a workspace.
[**mLModelsPatch**](ModelApi.md#mLModelsPatch) | **PATCH** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models/{id} | Patch a specific model.
[**mLModelsQueryById**](ModelApi.md#mLModelsQueryById) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models/{id} | Gets a model.
[**mLModelsRegister**](ModelApi.md#mLModelsRegister) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models | Register a model.



## mLModelsDelete

> mLModelsDelete(subscriptionId, resourceGroup, workspace, id)

Delete the specified Model.

Deletes a model if it exists.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ModelApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The model id.
apiInstance.mLModelsDelete(subscriptionId, resourceGroup, workspace, id, (error, data, response) => {
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
 **id** | **String**| The model id. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mLModelsGetMetrics

> ModelOperationalState mLModelsGetMetrics(subscriptionId, resourceGroup, workspace, id, opts)

Retrieve the metrics for a Model.

The operational events collected for the Model are returned.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ModelApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Model Id.
let opts = {
  'startDate': "startDate_example", // String | The start date from which to retrieve metrics, ISO 8601 literal format.
  'endDate': "endDate_example" // String | The end date from which to retrieve metrics, ISO 8601 literal format.
};
apiInstance.mLModelsGetMetrics(subscriptionId, resourceGroup, workspace, id, opts, (error, data, response) => {
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
 **id** | **String**| The Model Id. | 
 **startDate** | **String**| The start date from which to retrieve metrics, ISO 8601 literal format. | [optional] 
 **endDate** | **String**| The end date from which to retrieve metrics, ISO 8601 literal format. | [optional] 

### Return type

[**ModelOperationalState**](ModelOperationalState.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mLModelsListQuery

> PaginatedModelList mLModelsListQuery(subscriptionId, resourceGroup, workspace, opts)

Query the list of Models in a workspace.

The result list can be filtered using tag and name. If no filter is passed, the query lists all the Models in the given workspace. The returned list is paginated and the count of items in each page is an optional parameter.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ModelApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let opts = {
  'name': "name_example", // String | The object name.
  'framework': "framework_example", // String | The framework.
  'description': "description_example", // String | The object description.
  'count': 56, // Number | The number of items to retrieve in a page.
  'skipToken': "skipToken_example", // String | The continuation token to retrieve the next page.
  'tags': "tags_example", // String | A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key=value              Example: tagKey1,tagKey2,tagKey3=value3
  'properties': "properties_example", // String | A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key=value              Example: propKey1,propKey2,propKey3=value3
  'runId': "runId_example", // String | The runId which created the model.
  'orderBy': "'CreatedAtDesc'" // String | An option to specify how the models are ordered in the response.
};
apiInstance.mLModelsListQuery(subscriptionId, resourceGroup, workspace, opts, (error, data, response) => {
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
 **name** | **String**| The object name. | [optional] 
 **framework** | **String**| The framework. | [optional] 
 **description** | **String**| The object description. | [optional] 
 **count** | **Number**| The number of items to retrieve in a page. | [optional] 
 **skipToken** | **String**| The continuation token to retrieve the next page. | [optional] 
 **tags** | **String**| A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key&#x3D;value              Example: tagKey1,tagKey2,tagKey3&#x3D;value3 | [optional] 
 **properties** | **String**| A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key&#x3D;value              Example: propKey1,propKey2,propKey3&#x3D;value3 | [optional] 
 **runId** | **String**| The runId which created the model. | [optional] 
 **orderBy** | **String**| An option to specify how the models are ordered in the response. | [optional] [default to &#39;CreatedAtDesc&#39;]

### Return type

[**PaginatedModelList**](PaginatedModelList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mLModelsPatch

> Model mLModelsPatch(subscriptionId, resourceGroup, workspace, id, patch)

Patch a specific model.

Updates an existing model with the specified patch.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ModelApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The model id.
let patch = [new AzureMachineLearningModelManagementService.JsonPatchOperation()]; // [JsonPatchOperation] | The payload that is used to patch the model.
apiInstance.mLModelsPatch(subscriptionId, resourceGroup, workspace, id, patch, (error, data, response) => {
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
 **id** | **String**| The model id. | 
 **patch** | [**[JsonPatchOperation]**](JsonPatchOperation.md)| The payload that is used to patch the model. | 

### Return type

[**Model**](Model.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json


## mLModelsQueryById

> Model mLModelsQueryById(subscriptionId, resourceGroup, workspace, id)

Gets a model.

Gets a model by model id.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ModelApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The model id.
apiInstance.mLModelsQueryById(subscriptionId, resourceGroup, workspace, id, (error, data, response) => {
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
 **id** | **String**| The model id. | 

### Return type

[**Model**](Model.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mLModelsRegister

> Model mLModelsRegister(subscriptionId, resourceGroup, workspace, model)

Register a model.

Register the model provided.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ModelApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let model = new AzureMachineLearningModelManagementService.Model(); // Model | The payload that is used to register the model.
apiInstance.mLModelsRegister(subscriptionId, resourceGroup, workspace, model, (error, data, response) => {
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
 **model** | [**Model**](Model.md)| The payload that is used to register the model. | 

### Return type

[**Model**](Model.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

