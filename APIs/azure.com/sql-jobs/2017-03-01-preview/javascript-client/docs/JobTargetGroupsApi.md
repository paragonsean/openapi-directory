# SqlManagementClient.JobTargetGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobTargetGroupsCreateOrUpdate**](JobTargetGroupsApi.md#jobTargetGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/targetGroups/{targetGroupName} | 
[**jobTargetGroupsDelete**](JobTargetGroupsApi.md#jobTargetGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/targetGroups/{targetGroupName} | 
[**jobTargetGroupsGet**](JobTargetGroupsApi.md#jobTargetGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/targetGroups/{targetGroupName} | 
[**jobTargetGroupsListByAgent**](JobTargetGroupsApi.md#jobTargetGroupsListByAgent) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/targetGroups | 



## jobTargetGroupsCreateOrUpdate

> JobTargetGroup jobTargetGroupsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, targetGroupName, subscriptionId, apiVersion, parameters)



Creates or updates a target group.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobTargetGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let targetGroupName = "targetGroupName_example"; // String | The name of the target group.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.JobTargetGroup(); // JobTargetGroup | The requested state of the target group.
apiInstance.jobTargetGroupsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, targetGroupName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **targetGroupName** | **String**| The name of the target group. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**JobTargetGroup**](JobTargetGroup.md)| The requested state of the target group. | 

### Return type

[**JobTargetGroup**](JobTargetGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jobTargetGroupsDelete

> jobTargetGroupsDelete(resourceGroupName, serverName, jobAgentName, targetGroupName, subscriptionId, apiVersion)



Deletes a target group.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobTargetGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let targetGroupName = "targetGroupName_example"; // String | The name of the target group.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobTargetGroupsDelete(resourceGroupName, serverName, jobAgentName, targetGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **targetGroupName** | **String**| The name of the target group. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## jobTargetGroupsGet

> JobTargetGroup jobTargetGroupsGet(resourceGroupName, serverName, jobAgentName, targetGroupName, subscriptionId, apiVersion)



Gets a target group.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobTargetGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let targetGroupName = "targetGroupName_example"; // String | The name of the target group.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobTargetGroupsGet(resourceGroupName, serverName, jobAgentName, targetGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **targetGroupName** | **String**| The name of the target group. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**JobTargetGroup**](JobTargetGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobTargetGroupsListByAgent

> JobTargetGroupListResult jobTargetGroupsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion)



Gets all target groups in an agent.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobTargetGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobTargetGroupsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion, (error, data, response) => {
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

[**JobTargetGroupListResult**](JobTargetGroupListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

