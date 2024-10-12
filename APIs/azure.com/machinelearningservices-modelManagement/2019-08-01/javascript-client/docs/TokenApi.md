# AzureMachineLearningModelManagementService.TokenApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicesGetServiceToken_0**](TokenApi.md#servicesGetServiceToken_0) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/token | Generate Service Access Token.



## servicesGetServiceToken_0

> AuthToken servicesGetServiceToken_0(subscriptionId, resourceGroup, workspace, id)

Generate Service Access Token.

Gets access token that can be used for calling service.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.TokenApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let id = "id_example"; // String | The Service Id.
apiInstance.servicesGetServiceToken_0(subscriptionId, resourceGroup, workspace, id, (error, data, response) => {
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

