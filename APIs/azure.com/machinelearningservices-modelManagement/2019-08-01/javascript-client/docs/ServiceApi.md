# AzureMachineLearningModelManagementService.ServiceApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicesCreate**](ServiceApi.md#servicesCreate) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services | Create a Service.
[**servicesDelete**](ServiceApi.md#servicesDelete) | **DELETE** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id} | Delete a Service.
[**servicesGetServiceToken**](ServiceApi.md#servicesGetServiceToken) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/token | Generate Service Access Token.
[**servicesListQuery**](ServiceApi.md#servicesListQuery) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services | Query the list of Services in a Workspace.
[**servicesListServiceKeys**](ServiceApi.md#servicesListServiceKeys) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/listkeys | Lists Service keys.
[**servicesPatch**](ServiceApi.md#servicesPatch) | **PATCH** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id} | Patch a Service.
[**servicesQueryById**](ServiceApi.md#servicesQueryById) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id} | Get a Service.
[**servicesRegenerateServiceKeys**](ServiceApi.md#servicesRegenerateServiceKeys) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/regenerateKeys | Regenerate Service Keys.



## servicesCreate

> servicesCreate(subscriptionId, resourceGroup, workspace, request)

Create a Service.

Create a Service with the specified payload.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let request = new AzureMachineLearningModelManagementService.CreateServiceRequest(); // CreateServiceRequest | The payload that is used to create the Service.
apiInstance.servicesCreate(subscriptionId, resourceGroup, workspace, request, (error, data, response) => {
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
 **request** | [**CreateServiceRequest**](CreateServiceRequest.md)| The payload that is used to create the Service. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicesDelete

> servicesDelete(subscriptionId, resourceGroup, workspace, id)

Delete a Service.

Delete a specific Service.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Service Id.
apiInstance.servicesDelete(subscriptionId, resourceGroup, workspace, id, (error, data, response) => {
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
 **id** | **String**| The Service Id. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesGetServiceToken

> AuthToken servicesGetServiceToken(subscriptionId, resourceGroup, workspace, id)

Generate Service Access Token.

Gets access token that can be used for calling service.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Service Id.
apiInstance.servicesGetServiceToken(subscriptionId, resourceGroup, workspace, id, (error, data, response) => {
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
 **id** | **String**| The Service Id. | 

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListQuery

> PaginatedServiceList servicesListQuery(subscriptionId, resourceGroup, workspace, opts)

Query the list of Services in a Workspace.

If no filter is passed, the query lists all Services in the Workspace. The returned list is paginated and the count of item in each page is an optional parameter.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let opts = {
  'imageId': "imageId_example", // String | The Image Id.
  'imageName': "imageName_example", // String | The Image name.
  'modelId': "modelId_example", // String | The Model Id.
  'modelName': "modelName_example", // String | The Model name.
  'name': "name_example", // String | The object name.
  'count': 56, // Number | The number of items to retrieve in a page.
  'computeType': "computeType_example", // String | The compute environment type.
  'skipToken': "skipToken_example", // String | The continuation token to retrieve the next page.
  'tags': "tags_example", // String | A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key=value              Example: tagKey1,tagKey2,tagKey3=value3
  'properties': "properties_example", // String | A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key=value              Example: propKey1,propKey2,propKey3=value3
  'expand': false, // Boolean | Set to True to include Model details.
  'orderby': "'UpdatedAtDesc'" // String | The option to order the response.
};
apiInstance.servicesListQuery(subscriptionId, resourceGroup, workspace, opts, (error, data, response) => {
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
 **imageId** | **String**| The Image Id. | [optional] 
 **imageName** | **String**| The Image name. | [optional] 
 **modelId** | **String**| The Model Id. | [optional] 
 **modelName** | **String**| The Model name. | [optional] 
 **name** | **String**| The object name. | [optional] 
 **count** | **Number**| The number of items to retrieve in a page. | [optional] 
 **computeType** | **String**| The compute environment type. | [optional] 
 **skipToken** | **String**| The continuation token to retrieve the next page. | [optional] 
 **tags** | **String**| A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key&#x3D;value              Example: tagKey1,tagKey2,tagKey3&#x3D;value3 | [optional] 
 **properties** | **String**| A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key&#x3D;value              Example: propKey1,propKey2,propKey3&#x3D;value3 | [optional] 
 **expand** | **Boolean**| Set to True to include Model details. | [optional] [default to false]
 **orderby** | **String**| The option to order the response. | [optional] [default to &#39;UpdatedAtDesc&#39;]

### Return type

[**PaginatedServiceList**](PaginatedServiceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListServiceKeys

> AuthKeys servicesListServiceKeys(subscriptionId, resourceGroup, workspace, id)

Lists Service keys.

Gets a list of Service keys.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Service Id.
apiInstance.servicesListServiceKeys(subscriptionId, resourceGroup, workspace, id, (error, data, response) => {
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
 **id** | **String**| The Service Id. | 

### Return type

[**AuthKeys**](AuthKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesPatch

> servicesPatch(subscriptionId, resourceGroup, workspace, id, patch)

Patch a Service.

Patch a specific Service.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Service Id.
let patch = [new AzureMachineLearningModelManagementService.JsonPatchOperation()]; // [JsonPatchOperation] | The payload that is used to patch the Service.
apiInstance.servicesPatch(subscriptionId, resourceGroup, workspace, id, patch, (error, data, response) => {
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
 **id** | **String**| The Service Id. | 
 **patch** | [**[JsonPatchOperation]**](JsonPatchOperation.md)| The payload that is used to patch the Service. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json


## servicesQueryById

> ServiceResponseBase servicesQueryById(subscriptionId, resourceGroup, workspace, id, opts)

Get a Service.

Get a Service by Id.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Service Id.
let opts = {
  'expand': false // Boolean | Set to True to include Model details.
};
apiInstance.servicesQueryById(subscriptionId, resourceGroup, workspace, id, opts, (error, data, response) => {
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
 **id** | **String**| The Service Id. | 
 **expand** | **Boolean**| Set to True to include Model details. | [optional] [default to false]

### Return type

[**ServiceResponseBase**](ServiceResponseBase.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesRegenerateServiceKeys

> AuthKeys servicesRegenerateServiceKeys(subscriptionId, resourceGroup, workspace, id, request)

Regenerate Service Keys.

Regenerate and return the Service keys.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Service Id.
let request = new AzureMachineLearningModelManagementService.RegenerateServiceKeysRequest(); // RegenerateServiceKeysRequest | The payload that is used to regenerate keys.
apiInstance.servicesRegenerateServiceKeys(subscriptionId, resourceGroup, workspace, id, request, (error, data, response) => {
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
 **id** | **String**| The Service Id. | 
 **request** | [**RegenerateServiceKeysRequest**](RegenerateServiceKeysRequest.md)| The payload that is used to regenerate keys. | 

### Return type

[**AuthKeys**](AuthKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

