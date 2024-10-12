# AzureMachineLearningWorkspaces.WorkspaceSkusApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listSkus**](WorkspaceSkusApi.md#listSkus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/workspaces/skus | 



## listSkus

> SkuListResult listSkus(apiVersion, subscriptionId)



Lists all skus with associated features

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspaceSkusApi();
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
apiInstance.listSkus(apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription identifier. | 

### Return type

[**SkuListResult**](SkuListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

