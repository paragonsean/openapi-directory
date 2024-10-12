# SqlManagementClient.JobsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobsCreateOrUpdate**](JobsApi.md#jobsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName} | 
[**jobsDelete**](JobsApi.md#jobsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName} | 
[**jobsGet**](JobsApi.md#jobsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName} | 
[**jobsListByAgent**](JobsApi.md#jobsListByAgent) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs | 



## jobsCreateOrUpdate

> Job jobsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion, parameters)



Creates or updates a job.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let jobName = "jobName_example"; // String | The name of the job to get.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.Job(); // Job | The requested job state.
apiInstance.jobsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **jobAgentName** | **String**| The name of the job agent. | 
 **jobName** | **String**| The name of the job to get. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**Job**](Job.md)| The requested job state. | 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jobsDelete

> jobsDelete(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion)



Deletes a job.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let jobName = "jobName_example"; // String | The name of the job to delete.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobsDelete(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **jobAgentName** | **String**| The name of the job agent. | 
 **jobName** | **String**| The name of the job to delete. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## jobsGet

> Job jobsGet(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion)



Gets a job.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let jobName = "jobName_example"; // String | The name of the job to get.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobsGet(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **jobAgentName** | **String**| The name of the job agent. | 
 **jobName** | **String**| The name of the job to get. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsListByAgent

> JobListResult jobsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion)



Gets a list of jobs.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **jobAgentName** | **String**| The name of the job agent. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**JobListResult**](JobListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

