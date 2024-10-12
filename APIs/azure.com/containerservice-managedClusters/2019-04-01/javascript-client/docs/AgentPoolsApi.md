# ContainerServiceClient.AgentPoolsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agentPoolsCreateOrUpdate**](AgentPoolsApi.md#agentPoolsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/agentPools/{agentPoolName} | Creates or updates an agent pool.
[**agentPoolsDelete**](AgentPoolsApi.md#agentPoolsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/agentPools/{agentPoolName} | Deletes an agent pool.
[**agentPoolsGet**](AgentPoolsApi.md#agentPoolsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/agentPools/{agentPoolName} | Gets the agent pool.
[**agentPoolsList**](AgentPoolsApi.md#agentPoolsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/agentPools | Gets a list of agent pools in the specified managed cluster.



## agentPoolsCreateOrUpdate

> AgentPool agentPoolsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, agentPoolName, parameters)

Creates or updates an agent pool.

Creates or updates an agent pool in the specified managed cluster.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.AgentPoolsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
let agentPoolName = "agentPoolName_example"; // String | The name of the agent pool.
let parameters = new ContainerServiceClient.AgentPool(); // AgentPool | Parameters supplied to the Create or Update an agent pool operation.
apiInstance.agentPoolsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, agentPoolName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceName** | **String**| The name of the managed cluster resource. | 
 **agentPoolName** | **String**| The name of the agent pool. | 
 **parameters** | [**AgentPool**](AgentPool.md)| Parameters supplied to the Create or Update an agent pool operation. | 

### Return type

[**AgentPool**](AgentPool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## agentPoolsDelete

> agentPoolsDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, agentPoolName)

Deletes an agent pool.

Deletes the agent pool in the specified managed cluster.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.AgentPoolsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
let agentPoolName = "agentPoolName_example"; // String | The name of the agent pool.
apiInstance.agentPoolsDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, agentPoolName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceName** | **String**| The name of the managed cluster resource. | 
 **agentPoolName** | **String**| The name of the agent pool. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## agentPoolsGet

> AgentPool agentPoolsGet(apiVersion, subscriptionId, resourceGroupName, resourceName, agentPoolName)

Gets the agent pool.

Gets the details of the agent pool by managed cluster and resource group.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.AgentPoolsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
let agentPoolName = "agentPoolName_example"; // String | The name of the agent pool.
apiInstance.agentPoolsGet(apiVersion, subscriptionId, resourceGroupName, resourceName, agentPoolName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceName** | **String**| The name of the managed cluster resource. | 
 **agentPoolName** | **String**| The name of the agent pool. | 

### Return type

[**AgentPool**](AgentPool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## agentPoolsList

> AgentPoolListResult agentPoolsList(apiVersion, subscriptionId, resourceGroupName, resourceName)

Gets a list of agent pools in the specified managed cluster.

Gets a list of agent pools in the specified managed cluster. The operation returns properties of each agent pool.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.AgentPoolsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
apiInstance.agentPoolsList(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceName** | **String**| The name of the managed cluster resource. | 

### Return type

[**AgentPoolListResult**](AgentPoolListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

