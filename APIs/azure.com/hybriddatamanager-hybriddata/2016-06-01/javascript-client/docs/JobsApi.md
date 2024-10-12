# HybridDataManagementClient.JobsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobsCancel**](JobsApi.md#jobsCancel) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}/jobs/{jobId}/cancel | 
[**jobsGet**](JobsApi.md#jobsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}/jobs/{jobId} | 
[**jobsListByDataManager**](JobsApi.md#jobsListByDataManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/jobs | 
[**jobsListByDataService**](JobsApi.md#jobsListByDataService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobs | 
[**jobsListByJobDefinition**](JobsApi.md#jobsListByJobDefinition) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}/jobs | 
[**jobsResume**](JobsApi.md#jobsResume) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}/jobs/{jobId}/resume | 



## jobsCancel

> jobsCancel(dataServiceName, jobDefinitionName, jobId, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



Cancels the given job.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.JobsApi();
let dataServiceName = "dataServiceName_example"; // String | The name of the data service of the job definition.
let jobDefinitionName = "jobDefinitionName_example"; // String | The name of the job definition of the job.
let jobId = "jobId_example"; // String | The job id of the job queried.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.jobsCancel(dataServiceName, jobDefinitionName, jobId, subscriptionId, resourceGroupName, dataManagerName, apiVersion, (error, data, response) => {
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
 **dataServiceName** | **String**| The name of the data service of the job definition. | 
 **jobDefinitionName** | **String**| The name of the job definition of the job. | 
 **jobId** | **String**| The job id of the job queried. | 
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


## jobsGet

> Job jobsGet(dataServiceName, jobDefinitionName, jobId, subscriptionId, resourceGroupName, dataManagerName, apiVersion, opts)



This method gets a data manager job given the jobId.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.JobsApi();
let dataServiceName = "dataServiceName_example"; // String | The name of the data service of the job definition.
let jobDefinitionName = "jobDefinitionName_example"; // String | The name of the job definition of the job.
let jobId = "jobId_example"; // String | The job id of the job queried.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let opts = {
  'expand': "expand_example" // String | $expand is supported on details parameter for job, which provides details on the job stages.
};
apiInstance.jobsGet(dataServiceName, jobDefinitionName, jobId, subscriptionId, resourceGroupName, dataManagerName, apiVersion, opts, (error, data, response) => {
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
 **dataServiceName** | **String**| The name of the data service of the job definition. | 
 **jobDefinitionName** | **String**| The name of the job definition of the job. | 
 **jobId** | **String**| The job id of the job queried. | 
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 
 **expand** | **String**| $expand is supported on details parameter for job, which provides details on the job stages. | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsListByDataManager

> JobList jobsListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, opts)



This method gets all the jobs at the data manager resource level.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let opts = {
  'filter': "filter_example" // String | OData Filter options
};
apiInstance.jobsListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, opts, (error, data, response) => {
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

[**JobList**](JobList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsListByDataService

> JobList jobsListByDataService(dataServiceName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, opts)



This method gets all the jobs of a data service type in a given resource.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.JobsApi();
let dataServiceName = "dataServiceName_example"; // String | The name of the data service of interest.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let opts = {
  'filter': "filter_example" // String | OData Filter options
};
apiInstance.jobsListByDataService(dataServiceName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, opts, (error, data, response) => {
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
 **dataServiceName** | **String**| The name of the data service of interest. | 
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 
 **filter** | **String**| OData Filter options | [optional] 

### Return type

[**JobList**](JobList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsListByJobDefinition

> JobList jobsListByJobDefinition(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, opts)



This method gets all the jobs of a given job definition.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.JobsApi();
let dataServiceName = "dataServiceName_example"; // String | The name of the data service of the job definition.
let jobDefinitionName = "jobDefinitionName_example"; // String | The name of the job definition for which jobs are needed.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let opts = {
  'filter': "filter_example" // String | OData Filter options
};
apiInstance.jobsListByJobDefinition(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, opts, (error, data, response) => {
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
 **dataServiceName** | **String**| The name of the data service of the job definition. | 
 **jobDefinitionName** | **String**| The name of the job definition for which jobs are needed. | 
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 
 **filter** | **String**| OData Filter options | [optional] 

### Return type

[**JobList**](JobList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsResume

> jobsResume(dataServiceName, jobDefinitionName, jobId, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



Resumes the given job.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.JobsApi();
let dataServiceName = "dataServiceName_example"; // String | The name of the data service of the job definition.
let jobDefinitionName = "jobDefinitionName_example"; // String | The name of the job definition of the job.
let jobId = "jobId_example"; // String | The job id of the job queried.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.jobsResume(dataServiceName, jobDefinitionName, jobId, subscriptionId, resourceGroupName, dataManagerName, apiVersion, (error, data, response) => {
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
 **dataServiceName** | **String**| The name of the data service of the job definition. | 
 **jobDefinitionName** | **String**| The name of the job definition of the job. | 
 **jobId** | **String**| The job id of the job queried. | 
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

