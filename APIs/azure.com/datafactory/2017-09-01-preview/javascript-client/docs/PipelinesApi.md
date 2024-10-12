# DataFactoryManagementClient.PipelinesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipelinesCreateOrUpdate**](PipelinesApi.md#pipelinesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines/{pipelineName} | 
[**pipelinesCreateRun**](PipelinesApi.md#pipelinesCreateRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines/{pipelineName}/createRun | 
[**pipelinesDelete**](PipelinesApi.md#pipelinesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines/{pipelineName} | 
[**pipelinesGet**](PipelinesApi.md#pipelinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines/{pipelineName} | 
[**pipelinesListByFactory**](PipelinesApi.md#pipelinesListByFactory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines | 



## pipelinesCreateOrUpdate

> PipelineResource pipelinesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion, pipeline, opts)



Creates or updates a pipeline.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.PipelinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let pipelineName = "pipelineName_example"; // String | The pipeline name.
let apiVersion = "apiVersion_example"; // String | The API version.
let pipeline = new DataFactoryManagementClient.PipelineResource(); // PipelineResource | Pipeline resource definition.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the pipeline entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
};
apiInstance.pipelinesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion, pipeline, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **pipelineName** | **String**| The pipeline name. | 
 **apiVersion** | **String**| The API version. | 
 **pipeline** | [**PipelineResource**](PipelineResource.md)| Pipeline resource definition. | 
 **ifMatch** | **String**| ETag of the pipeline entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update. | [optional] 

### Return type

[**PipelineResource**](PipelineResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pipelinesCreateRun

> CreateRunResponse pipelinesCreateRun(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion, opts)



Creates a run of a pipeline.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.PipelinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let pipelineName = "pipelineName_example"; // String | The pipeline name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'parameters': {key: null} // {String: Object} | Parameters of the pipeline run.
};
apiInstance.pipelinesCreateRun(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **pipelineName** | **String**| The pipeline name. | 
 **apiVersion** | **String**| The API version. | 
 **parameters** | [**{String: Object}**](Object.md)| Parameters of the pipeline run. | [optional] 

### Return type

[**CreateRunResponse**](CreateRunResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pipelinesDelete

> pipelinesDelete(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion)



Deletes a pipeline.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.PipelinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let pipelineName = "pipelineName_example"; // String | The pipeline name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.pipelinesDelete(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **pipelineName** | **String**| The pipeline name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pipelinesGet

> PipelineResource pipelinesGet(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion)



Gets a pipeline.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.PipelinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let pipelineName = "pipelineName_example"; // String | The pipeline name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.pipelinesGet(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **pipelineName** | **String**| The pipeline name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**PipelineResource**](PipelineResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pipelinesListByFactory

> PipelineListResponse pipelinesListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion)



Lists pipelines.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.PipelinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.pipelinesListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**PipelineListResponse**](PipelineListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

