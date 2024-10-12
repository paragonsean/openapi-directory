# SqlManagementClient.JobCredentialsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobCredentialsCreateOrUpdate**](JobCredentialsApi.md#jobCredentialsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/credentials/{credentialName} | 
[**jobCredentialsDelete**](JobCredentialsApi.md#jobCredentialsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/credentials/{credentialName} | 
[**jobCredentialsGet**](JobCredentialsApi.md#jobCredentialsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/credentials/{credentialName} | 
[**jobCredentialsListByAgent**](JobCredentialsApi.md#jobCredentialsListByAgent) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/credentials | 



## jobCredentialsCreateOrUpdate

> JobCredential jobCredentialsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, credentialName, subscriptionId, apiVersion, parameters)



Creates or updates a job credential.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobCredentialsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let credentialName = "credentialName_example"; // String | The name of the credential.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.JobCredential(); // JobCredential | The requested job credential state.
apiInstance.jobCredentialsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, credentialName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **credentialName** | **String**| The name of the credential. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**JobCredential**](JobCredential.md)| The requested job credential state. | 

### Return type

[**JobCredential**](JobCredential.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jobCredentialsDelete

> jobCredentialsDelete(resourceGroupName, serverName, jobAgentName, credentialName, subscriptionId, apiVersion)



Deletes a job credential.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobCredentialsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let credentialName = "credentialName_example"; // String | The name of the credential.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobCredentialsDelete(resourceGroupName, serverName, jobAgentName, credentialName, subscriptionId, apiVersion, (error, data, response) => {
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
 **credentialName** | **String**| The name of the credential. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## jobCredentialsGet

> JobCredential jobCredentialsGet(resourceGroupName, serverName, jobAgentName, credentialName, subscriptionId, apiVersion)



Gets a jobs credential.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobCredentialsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let credentialName = "credentialName_example"; // String | The name of the credential.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobCredentialsGet(resourceGroupName, serverName, jobAgentName, credentialName, subscriptionId, apiVersion, (error, data, response) => {
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
 **credentialName** | **String**| The name of the credential. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**JobCredential**](JobCredential.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobCredentialsListByAgent

> JobCredentialListResult jobCredentialsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion)



Gets a list of jobs credentials.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.JobCredentialsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.jobCredentialsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion, (error, data, response) => {
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

[**JobCredentialListResult**](JobCredentialListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

