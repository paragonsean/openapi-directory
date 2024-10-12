# SqlManagementClient.JobStepExecutionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobStepExecutionsGet**](JobStepExecutionsApi.md#jobStepExecutionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/steps/{stepName} | 
[**jobStepExecutionsListByJobExecution**](JobStepExecutionsApi.md#jobStepExecutionsListByJobExecution) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/steps | 



## jobStepExecutionsGet

> JobExecution jobStepExecutionsGet(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, stepName, subscriptionId, apiVersion)



Gets a step execution of a job execution.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobStepExecutionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let jobName = "jobName_example"; // String | The name of the job to get.
let jobExecutionId = "jobExecutionId_example"; // String | The unique id of the job execution
let stepName = "stepName_example"; // String | The name of the step.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobStepExecutionsGet(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, stepName, subscriptionId, apiVersion, (error, data, response) => {
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
 **jobExecutionId** | **String**| The unique id of the job execution | 
 **stepName** | **String**| The name of the step. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**JobExecution**](JobExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobStepExecutionsListByJobExecution

> JobExecutionListResult jobStepExecutionsListByJobExecution(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion, opts)



Lists the step executions of a job execution.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobStepExecutionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let jobName = "jobName_example"; // String | The name of the job to get.
let jobExecutionId = "jobExecutionId_example"; // String | The id of the job execution
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
apiInstance.jobStepExecutionsListByJobExecution(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **jobExecutionId** | **String**| The id of the job execution | 
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

