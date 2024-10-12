# VisualStudioProjectsResourceProviderClient.PipelineTemplatesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipelineTemplatesList**](PipelineTemplatesApi.md#pipelineTemplatesList) | **GET** /providers/microsoft.visualstudio/pipelineTemplates | PipelineTemplates_List



## pipelineTemplatesList

> PipelineTemplateResourceListResult pipelineTemplatesList(apiVersion)

PipelineTemplates_List

Gets all pipeline templates which can be used to configure a CI/CD pipeline in a new or an existing Team Services project.

### Example

```javascript
import VisualStudioProjectsResourceProviderClient from 'visual_studio_projects_resource_provider_client';
let defaultClient = VisualStudioProjectsResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioProjectsResourceProviderClient.PipelineTemplatesApi();
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.pipelineTemplatesList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| API Version | 

### Return type

[**PipelineTemplateResourceListResult**](PipelineTemplateResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

