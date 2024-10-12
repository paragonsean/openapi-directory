# PostgreSqlManagementClient.ServerSecurityAlertPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serverSecurityAlertPoliciesCreateOrUpdate**](ServerSecurityAlertPoliciesApi.md#serverSecurityAlertPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/servers/{serverName}/securityAlertPolicies/{securityAlertPolicyName} | 
[**serverSecurityAlertPoliciesGet**](ServerSecurityAlertPoliciesApi.md#serverSecurityAlertPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/servers/{serverName}/securityAlertPolicies/{securityAlertPolicyName} | 



## serverSecurityAlertPoliciesCreateOrUpdate

> ServerSecurityAlertPolicy serverSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, serverName, securityAlertPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates a threat detection policy.

### Example

```javascript
import PostgreSqlManagementClient from 'postgre_sql_management_client';
let defaultClient = PostgreSqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PostgreSqlManagementClient.ServerSecurityAlertPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let securityAlertPolicyName = "securityAlertPolicyName_example"; // String | The name of the threat detection policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new PostgreSqlManagementClient.ServerSecurityAlertPolicy(); // ServerSecurityAlertPolicy | The server security alert policy.
apiInstance.serverSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, serverName, securityAlertPolicyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **securityAlertPolicyName** | **String**| The name of the threat detection policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**ServerSecurityAlertPolicy**](ServerSecurityAlertPolicy.md)| The server security alert policy. | 

### Return type

[**ServerSecurityAlertPolicy**](ServerSecurityAlertPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serverSecurityAlertPoliciesGet

> ServerSecurityAlertPolicy serverSecurityAlertPoliciesGet(resourceGroupName, serverName, securityAlertPolicyName, subscriptionId, apiVersion)



Get a server&#39;s security alert policy.

### Example

```javascript
import PostgreSqlManagementClient from 'postgre_sql_management_client';
let defaultClient = PostgreSqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PostgreSqlManagementClient.ServerSecurityAlertPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let securityAlertPolicyName = "securityAlertPolicyName_example"; // String | The name of the security alert policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.serverSecurityAlertPoliciesGet(resourceGroupName, serverName, securityAlertPolicyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **securityAlertPolicyName** | **String**| The name of the security alert policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ServerSecurityAlertPolicy**](ServerSecurityAlertPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

