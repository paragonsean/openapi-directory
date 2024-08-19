# AzureDevOps.PipelinesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipelinesCreateOrUpdate**](PipelinesApi.md#pipelinesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName} | 
[**pipelinesDelete**](PipelinesApi.md#pipelinesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName} | 
[**pipelinesGet**](PipelinesApi.md#pipelinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName} | 
[**pipelinesListByResourceGroup**](PipelinesApi.md#pipelinesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines | 
[**pipelinesListBySubscription**](PipelinesApi.md#pipelinesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DevOps/pipelines | 
[**pipelinesUpdate**](PipelinesApi.md#pipelinesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName} | 



## pipelinesCreateOrUpdate

> Pipeline pipelinesCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, pipelineName, createOperationParameters)



Creates or updates an Azure Pipeline.

### Example

```javascript
import AzureDevOps from 'azure_dev_ops';
let defaultClient = AzureDevOps.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDevOps.PipelinesApi();
let subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
let pipelineName = "pipelineName_example"; // String | The name of the Azure Pipeline resource in ARM.
let createOperationParameters = new AzureDevOps.Pipeline(); // Pipeline | The request payload to create the Azure Pipeline.
apiInstance.pipelinesCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, pipelineName, createOperationParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **apiVersion** | **String**| API version to be used with the HTTP request. | 
 **pipelineName** | **String**| The name of the Azure Pipeline resource in ARM. | 
 **createOperationParameters** | [**Pipeline**](Pipeline.md)| The request payload to create the Azure Pipeline. | 

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pipelinesDelete

> pipelinesDelete(subscriptionId, resourceGroupName, apiVersion, pipelineName)



Deletes an Azure Pipeline.

### Example

```javascript
import AzureDevOps from 'azure_dev_ops';
let defaultClient = AzureDevOps.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDevOps.PipelinesApi();
let subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
let pipelineName = "pipelineName_example"; // String | The name of the Azure Pipeline resource.
apiInstance.pipelinesDelete(subscriptionId, resourceGroupName, apiVersion, pipelineName, (error, data, response) => {
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
 **subscriptionId** | **String**| Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **apiVersion** | **String**| API version to be used with the HTTP request. | 
 **pipelineName** | **String**| The name of the Azure Pipeline resource. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pipelinesGet

> Pipeline pipelinesGet(subscriptionId, resourceGroupName, apiVersion, pipelineName)



Gets an existing Azure Pipeline.

### Example

```javascript
import AzureDevOps from 'azure_dev_ops';
let defaultClient = AzureDevOps.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDevOps.PipelinesApi();
let subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
let pipelineName = "pipelineName_example"; // String | The name of the Azure Pipeline resource in ARM.
apiInstance.pipelinesGet(subscriptionId, resourceGroupName, apiVersion, pipelineName, (error, data, response) => {
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
 **subscriptionId** | **String**| Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **apiVersion** | **String**| API version to be used with the HTTP request. | 
 **pipelineName** | **String**| The name of the Azure Pipeline resource in ARM. | 

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pipelinesListByResourceGroup

> PipelineListResult pipelinesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all Azure Pipelines under the specified resource group.

### Example

```javascript
import AzureDevOps from 'azure_dev_ops';
let defaultClient = AzureDevOps.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDevOps.PipelinesApi();
let subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
apiInstance.pipelinesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **apiVersion** | **String**| API version to be used with the HTTP request. | 

### Return type

[**PipelineListResult**](PipelineListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pipelinesListBySubscription

> PipelineListResult pipelinesListBySubscription(subscriptionId, apiVersion)



Lists all Azure Pipelines under the specified subscription.

### Example

```javascript
import AzureDevOps from 'azure_dev_ops';
let defaultClient = AzureDevOps.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDevOps.PipelinesApi();
let subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
apiInstance.pipelinesListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API version to be used with the HTTP request. | 

### Return type

[**PipelineListResult**](PipelineListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pipelinesUpdate

> Pipeline pipelinesUpdate(subscriptionId, resourceGroupName, apiVersion, pipelineName, updateOperationParameters)



Updates the properties of an Azure Pipeline. Currently, only tags can be updated.

### Example

```javascript
import AzureDevOps from 'azure_dev_ops';
let defaultClient = AzureDevOps.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDevOps.PipelinesApi();
let subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
let pipelineName = "pipelineName_example"; // String | The name of the Azure Pipeline resource.
let updateOperationParameters = new AzureDevOps.PipelineUpdateParameters(); // PipelineUpdateParameters | The request payload containing the properties to update in the Azure Pipeline.
apiInstance.pipelinesUpdate(subscriptionId, resourceGroupName, apiVersion, pipelineName, updateOperationParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **apiVersion** | **String**| API version to be used with the HTTP request. | 
 **pipelineName** | **String**| The name of the Azure Pipeline resource. | 
 **updateOperationParameters** | [**PipelineUpdateParameters**](PipelineUpdateParameters.md)| The request payload containing the properties to update in the Azure Pipeline. | 

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

