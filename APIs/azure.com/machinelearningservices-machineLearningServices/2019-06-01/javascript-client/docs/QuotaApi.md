# AzureMachineLearningWorkspaces.QuotaApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotasList**](QuotaApi.md#quotasList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/locations/{location}/Quotas | 
[**quotasUpdate**](QuotaApi.md#quotasUpdate) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/locations/{location}/updateQuotas | 



## quotasList

> ListWorkspaceQuotas quotasList(apiVersion, subscriptionId, location)



Gets the currently assigned Workspace Quotas based on VMFamily.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.QuotaApi();
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let location = "location_example"; // String | The location for which resource usage is queried.
apiInstance.quotasList(apiVersion, subscriptionId, location, (error, data, response) => {
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
 **location** | **String**| The location for which resource usage is queried. | 

### Return type

[**ListWorkspaceQuotas**](ListWorkspaceQuotas.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quotasUpdate

> UpdateWorkspaceQuotasResult quotasUpdate(location, apiVersion, subscriptionId, parameters)



Update quota for each VM family in workspace.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.QuotaApi();
let location = "location_example"; // String | The location for update quota is queried.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let parameters = new AzureMachineLearningWorkspaces.QuotaUpdateParameters(); // QuotaUpdateParameters | Quota update parameters.
apiInstance.quotasUpdate(location, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **location** | **String**| The location for update quota is queried. | 
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **parameters** | [**QuotaUpdateParameters**](QuotaUpdateParameters.md)| Quota update parameters. | 

### Return type

[**UpdateWorkspaceQuotasResult**](UpdateWorkspaceQuotasResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

