# AzureDevOps.PipelineTemplateDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipelineTemplateDefinitionsList**](PipelineTemplateDefinitionsApi.md#pipelineTemplateDefinitionsList) | **GET** /providers/Microsoft.DevOps/pipelineTemplateDefinitions | 



## pipelineTemplateDefinitionsList

> PipelineTemplateDefinitionListResult pipelineTemplateDefinitionsList(apiVersion)



Lists all pipeline templates which can be used to configure an Azure Pipeline.

### Example

```javascript
import AzureDevOps from 'azure_dev_ops';
let defaultClient = AzureDevOps.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDevOps.PipelineTemplateDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
apiInstance.pipelineTemplateDefinitionsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| API version to be used with the HTTP request. | 

### Return type

[**PipelineTemplateDefinitionListResult**](PipelineTemplateDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

