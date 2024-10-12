# DataFactoryManagementClient.PipelinerunsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**factoriesCancelPipelineRun**](PipelinerunsApi.md#factoriesCancelPipelineRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/cancelpipelinerun/{runId} | 
[**pipelineRunsGet**](PipelinerunsApi.md#pipelineRunsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelineruns/{runId} | 
[**pipelineRunsQueryByFactory**](PipelinerunsApi.md#pipelineRunsQueryByFactory) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelineruns | 



## factoriesCancelPipelineRun

> factoriesCancelPipelineRun(subscriptionId, resourceGroupName, factoryName, runId, apiVersion)



Cancel a pipeline run by its run ID.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.PipelinerunsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let runId = "runId_example"; // String | The pipeline run identifier.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.factoriesCancelPipelineRun(subscriptionId, resourceGroupName, factoryName, runId, apiVersion, (error, data, response) => {
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
 **runId** | **String**| The pipeline run identifier. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pipelineRunsGet

> PipelineRun pipelineRunsGet(subscriptionId, resourceGroupName, factoryName, runId, apiVersion)



Get a pipeline run by its run ID.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.PipelinerunsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let runId = "runId_example"; // String | The pipeline run identifier.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.pipelineRunsGet(subscriptionId, resourceGroupName, factoryName, runId, apiVersion, (error, data, response) => {
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
 **runId** | **String**| The pipeline run identifier. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**PipelineRun**](PipelineRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pipelineRunsQueryByFactory

> PipelineRunQueryResponse pipelineRunsQueryByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, filterParameters)



Query pipeline runs in the factory based on input filter conditions.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.PipelinerunsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
let filterParameters = new DataFactoryManagementClient.PipelineRunFilterParameters(); // PipelineRunFilterParameters | Parameters to filter the pipeline run.
apiInstance.pipelineRunsQueryByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, filterParameters, (error, data, response) => {
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
 **filterParameters** | [**PipelineRunFilterParameters**](PipelineRunFilterParameters.md)| Parameters to filter the pipeline run. | 

### Return type

[**PipelineRunQueryResponse**](PipelineRunQueryResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

