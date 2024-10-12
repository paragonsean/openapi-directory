# SqlManagementClient.JobExecutionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobExecutionsCancel**](JobExecutionsApi.md#jobExecutionsCancel) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/cancel | 
[**jobExecutionsCreate**](JobExecutionsApi.md#jobExecutionsCreate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/start | 
[**jobExecutionsCreateOrUpdate**](JobExecutionsApi.md#jobExecutionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId} | 
[**jobExecutionsGet**](JobExecutionsApi.md#jobExecutionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId} | 
[**jobExecutionsListByAgent**](JobExecutionsApi.md#jobExecutionsListByAgent) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/executions | 
[**jobExecutionsListByJob**](JobExecutionsApi.md#jobExecutionsListByJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions | 



## jobExecutionsCancel

> jobExecutionsCancel(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion)



Requests cancellation of a job execution.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobExecutionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let jobName = "jobName_example"; // String | The name of the job.
let jobExecutionId = "jobExecutionId_example"; // String | The id of the job execution to cancel.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobExecutionsCancel(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion, (error, data, response) => {
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
 **jobName** | **String**| The name of the job. | 
 **jobExecutionId** | **String**| The id of the job execution to cancel. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## jobExecutionsCreate

> JobExecution jobExecutionsCreate(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion)



Starts an elastic job execution.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobExecutionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let jobName = "jobName_example"; // String | The name of the job to get.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobExecutionsCreate(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion, (error, data, response) => {
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

[**JobExecution**](JobExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobExecutionsCreateOrUpdate

> JobExecution jobExecutionsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion)



Creates or updates a job execution.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobExecutionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let jobName = "jobName_example"; // String | The name of the job to get.
let jobExecutionId = "jobExecutionId_example"; // String | The job execution id to create the job execution under.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobExecutionsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion, (error, data, response) => {
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
 **jobExecutionId** | **String**| The job execution id to create the job execution under. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**JobExecution**](JobExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobExecutionsGet

> JobExecution jobExecutionsGet(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion)



Gets a job execution.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobExecutionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let jobName = "jobName_example"; // String | The name of the job.
let jobExecutionId = "jobExecutionId_example"; // String | The id of the job execution
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobExecutionsGet(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion, (error, data, response) => {
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
 **jobName** | **String**| The name of the job. | 
 **jobExecutionId** | **String**| The id of the job execution | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**JobExecution**](JobExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobExecutionsListByAgent

> JobExecutionListResult jobExecutionsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion, opts)



Lists all executions in a job agent.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobExecutionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'createTimeMin': new Date("2013-10-20T19:20:30+01:00"), // Date | If specified, only job executions created at or after the specified time are included.
  'createTimeMax': new Date("2013-10-20T19:20:30+01:00"), // Date | If specified, only job executions created before the specified time are included.
  'endTimeMin': new Date("2013-10-20T19:20:30+01:00"), // Date | If specified, only job executions completed at or after the specified time are included.
  'endTimeMax': new Date("2013-10-20T19:20:30+01:00"), // Date | If specified, only job executions completed before the specified time are included.
  'isActive': true, // Boolean | If specified, only active or only completed job executions are included.
  'skip': 56, // Number | The number of elements in the collection to skip.
  'top': 56 // Number | The number of elements to return from the collection.
};
apiInstance.jobExecutionsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **createTimeMin** | **Date**| If specified, only job executions created at or after the specified time are included. | [optional] 
 **createTimeMax** | **Date**| If specified, only job executions created before the specified time are included. | [optional] 
 **endTimeMin** | **Date**| If specified, only job executions completed at or after the specified time are included. | [optional] 
 **endTimeMax** | **Date**| If specified, only job executions completed before the specified time are included. | [optional] 
 **isActive** | **Boolean**| If specified, only active or only completed job executions are included. | [optional] 
 **skip** | **Number**| The number of elements in the collection to skip. | [optional] 
 **top** | **Number**| The number of elements to return from the collection. | [optional] 

### Return type

[**JobExecutionListResult**](JobExecutionListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobExecutionsListByJob

> JobExecutionListResult jobExecutionsListByJob(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion, opts)



Lists a job&#39;s executions.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobExecutionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let jobName = "jobName_example"; // String | The name of the job to get.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'createTimeMin': new Date("2013-10-20T19:20:30+01:00"), // Date | If specified, only job executions created at or after the specified time are included.
  'createTimeMax': new Date("2013-10-20T19:20:30+01:00"), // Date | If specified, only job executions created before the specified time are included.
  'endTimeMin': new Date("2013-10-20T19:20:30+01:00"), // Date | If specified, only job executions completed at or after the specified time are included.
  'endTimeMax': new Date("2013-10-20T19:20:30+01:00"), // Date | If specified, only job executions completed before the specified time are included.
  'isActive': true, // Boolean | If specified, only active or only completed job executions are included.
  'skip': 56, // Number | The number of elements in the collection to skip.
  'top': 56 // Number | The number of elements to return from the collection.
};
apiInstance.jobExecutionsListByJob(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **createTimeMin** | **Date**| If specified, only job executions created at or after the specified time are included. | [optional] 
 **createTimeMax** | **Date**| If specified, only job executions created before the specified time are included. | [optional] 
 **endTimeMin** | **Date**| If specified, only job executions completed at or after the specified time are included. | [optional] 
 **endTimeMax** | **Date**| If specified, only job executions completed before the specified time are included. | [optional] 
 **isActive** | **Boolean**| If specified, only active or only completed job executions are included. | [optional] 
 **skip** | **Number**| The number of elements in the collection to skip. | [optional] 
 **top** | **Number**| The number of elements to return from the collection. | [optional] 

### Return type

[**JobExecutionListResult**](JobExecutionListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

