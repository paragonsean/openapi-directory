# AzureMachineLearningModelManagementService.KeysApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicesListServiceKeys_0**](KeysApi.md#servicesListServiceKeys_0) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/listkeys | Lists Service keys.
[**servicesRegenerateServiceKeys_0**](KeysApi.md#servicesRegenerateServiceKeys_0) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/regenerateKeys | Regenerate Service Keys.



## servicesListServiceKeys_0

> AuthKeys servicesListServiceKeys_0(subscriptionId, resourceGroup, workspace, id)

Lists Service keys.

Gets a list of Service keys.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.KeysApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Service Id.
apiInstance.servicesListServiceKeys_0(subscriptionId, resourceGroup, workspace, id, (error, data, response) => {
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


## servicesRegenerateServiceKeys_0

> AuthKeys servicesRegenerateServiceKeys_0(subscriptionId, resourceGroup, workspace, id, request)

Regenerate Service Keys.

Regenerate and return the Service keys.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.KeysApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Service Id.
let request = new AzureMachineLearningModelManagementService.RegenerateServiceKeysRequest(); // RegenerateServiceKeysRequest | The payload that is used to regenerate keys.
apiInstance.servicesRegenerateServiceKeys_0(subscriptionId, resourceGroup, workspace, id, request, (error, data, response) => {
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

