# AzureMachineLearningWorkspaces.UsageApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usagesList**](UsageApi.md#usagesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/locations/{location}/usages | 



## usagesList

> ListUsagesResult usagesList(apiVersion, subscriptionId, location, opts)



Gets the current usage information as well as limits for AML resources for given subscription and location.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.UsageApi();
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let location = "location_example"; // String | The location for which resource usage is queried.
let opts = {
  'expandChildren': "expandChildren_example" // String | Specifies if detailed usages of child resources are required.
};
apiInstance.usagesList(apiVersion, subscriptionId, location, opts, (error, data, response) => {
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
 **expandChildren** | **String**| Specifies if detailed usages of child resources are required. | [optional] 

### Return type

[**ListUsagesResult**](ListUsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

