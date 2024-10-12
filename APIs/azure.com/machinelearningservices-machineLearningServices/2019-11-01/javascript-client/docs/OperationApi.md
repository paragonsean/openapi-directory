# AzureMachineLearningWorkspaces.OperationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationApi.md#operationsList) | **GET** /providers/Microsoft.MachineLearningServices/operations | 



## operationsList

> OperationListResult operationsList(apiVersion)



Lists all of the available Azure Machine Learning Workspaces REST API operations.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.OperationApi();
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

