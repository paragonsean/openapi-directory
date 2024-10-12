# HybridDataManagementClient.JobDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobDefinitionsCreateOrUpdate**](JobDefinitionsApi.md#jobDefinitionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName} | 
[**jobDefinitionsDelete**](JobDefinitionsApi.md#jobDefinitionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName} | 
[**jobDefinitionsGet**](JobDefinitionsApi.md#jobDefinitionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName} | 
[**jobDefinitionsListByDataManager**](JobDefinitionsApi.md#jobDefinitionsListByDataManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/jobDefinitions | 
[**jobDefinitionsListByDataService**](JobDefinitionsApi.md#jobDefinitionsListByDataService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions | 
[**jobDefinitionsRun**](JobDefinitionsApi.md#jobDefinitionsRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}/run | 



## jobDefinitionsCreateOrUpdate

> JobDefinition jobDefinitionsCreateOrUpdate(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, jobDefinition)



Creates or updates a job definition.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.JobDefinitionsApi();
let dataServiceName = "dataServiceName_example"; // String | The data service type of the job definition.
let jobDefinitionName = "jobDefinitionName_example"; // String | The job definition name to be created or updated.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let jobDefinition = new HybridDataManagementClient.JobDefinition(); // JobDefinition | Job Definition object to be created or updated.
apiInstance.jobDefinitionsCreateOrUpdate(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, jobDefinition, (error, data, response) => {
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
 **dataServiceName** | **String**| The data service type of the job definition. | 
 **jobDefinitionName** | **String**| The job definition name to be created or updated. | 
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 
 **jobDefinition** | [**JobDefinition**](JobDefinition.md)| Job Definition object to be created or updated. | 

### Return type

[**JobDefinition**](JobDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jobDefinitionsDelete

> jobDefinitionsDelete(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



This method deletes the given job definition.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.JobDefinitionsApi();
let dataServiceName = "dataServiceName_example"; // String | The data service type of the job definition.
let jobDefinitionName = "jobDefinitionName_example"; // String | The job definition name to be deleted.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.jobDefinitionsDelete(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, (error, data, response) => {
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
 **dataServiceName** | **String**| The data service type of the job definition. | 
 **jobDefinitionName** | **String**| The job definition name to be deleted. | 
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## jobDefinitionsGet

> JobDefinition jobDefinitionsGet(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



This method gets job definition object by name.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.JobDefinitionsApi();
let dataServiceName = "dataServiceName_example"; // String | The data service name of the job definition
let jobDefinitionName = "jobDefinitionName_example"; // String | The job definition name that is being queried.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.jobDefinitionsGet(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, (error, data, response) => {
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
 **dataServiceName** | **String**| The data service name of the job definition | 
 **jobDefinitionName** | **String**| The job definition name that is being queried. | 
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 

### Return type

[**JobDefinition**](JobDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobDefinitionsListByDataManager

> JobDefinitionList jobDefinitionsListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, opts)



This method gets all the job definitions of the given data manager resource.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.JobDefinitionsApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let opts = {
  'filter': "filter_example" // String | OData Filter options
};
apiInstance.jobDefinitionsListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 
 **filter** | **String**| OData Filter options | [optional] 

### Return type

[**JobDefinitionList**](JobDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobDefinitionsListByDataService

> JobDefinitionList jobDefinitionsListByDataService(dataServiceName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, opts)



This method gets all the job definitions of the given data service name.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.JobDefinitionsApi();
let dataServiceName = "dataServiceName_example"; // String | The data service type of interest.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let opts = {
  'filter': "filter_example" // String | OData Filter options
};
apiInstance.jobDefinitionsListByDataService(dataServiceName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, opts, (error, data, response) => {
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
 **dataServiceName** | **String**| The data service type of interest. | 
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 
 **filter** | **String**| OData Filter options | [optional] 

### Return type

[**JobDefinitionList**](JobDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobDefinitionsRun

> jobDefinitionsRun(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, runParameters)



This method runs a job instance of the given job definition.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.JobDefinitionsApi();
let dataServiceName = "dataServiceName_example"; // String | The data service type of the job definition.
let jobDefinitionName = "jobDefinitionName_example"; // String | Name of the job definition.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let runParameters = new HybridDataManagementClient.RunParameters(); // RunParameters | Run time parameters for the job definition.
apiInstance.jobDefinitionsRun(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, runParameters, (error, data, response) => {
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
 **dataServiceName** | **String**| The data service type of the job definition. | 
 **jobDefinitionName** | **String**| Name of the job definition. | 
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 
 **runParameters** | [**RunParameters**](RunParameters.md)| Run time parameters for the job definition. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

