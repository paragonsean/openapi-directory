# AzureSqlServerApiSpec.ConnectionPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serverConnectionPoliciesCreateOrUpdate**](ConnectionPoliciesApi.md#serverConnectionPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/connectionPolicies/{connectionPolicyName} | 
[**serverConnectionPoliciesGet**](ConnectionPoliciesApi.md#serverConnectionPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/connectionPolicies/{connectionPolicyName} | 



## serverConnectionPoliciesCreateOrUpdate

> ServerConnectionPolicy serverConnectionPoliciesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, connectionPolicyName, parameters)



Creates or updates the server&#39;s connection policy.

### Example

```javascript
import AzureSqlServerApiSpec from 'azure_sql_server_api_spec';

let apiInstance = new AzureSqlServerApiSpec.ConnectionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let connectionPolicyName = "connectionPolicyName_example"; // String | The name of the connection policy.
let parameters = new AzureSqlServerApiSpec.ServerConnectionPolicy(); // ServerConnectionPolicy | The required parameters for updating a secure connection policy.
apiInstance.serverConnectionPoliciesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, connectionPolicyName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **connectionPolicyName** | **String**| The name of the connection policy. | 
 **parameters** | [**ServerConnectionPolicy**](ServerConnectionPolicy.md)| The required parameters for updating a secure connection policy. | 

### Return type

[**ServerConnectionPolicy**](ServerConnectionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serverConnectionPoliciesGet

> ServerConnectionPolicy serverConnectionPoliciesGet(apiVersion, subscriptionId, resourceGroupName, serverName, connectionPolicyName)



Gets the server&#39;s secure connection policy.

### Example

```javascript
import AzureSqlServerApiSpec from 'azure_sql_server_api_spec';

let apiInstance = new AzureSqlServerApiSpec.ConnectionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let connectionPolicyName = "connectionPolicyName_example"; // String | The name of the connection policy.
apiInstance.serverConnectionPoliciesGet(apiVersion, subscriptionId, resourceGroupName, serverName, connectionPolicyName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **connectionPolicyName** | **String**| The name of the connection policy. | 

### Return type

[**ServerConnectionPolicy**](ServerConnectionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

