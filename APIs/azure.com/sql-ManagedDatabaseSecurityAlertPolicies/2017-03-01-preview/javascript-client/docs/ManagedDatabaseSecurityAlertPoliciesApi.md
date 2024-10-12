# SqlManagementClient.ManagedDatabaseSecurityAlertPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managedDatabaseSecurityAlertPoliciesCreateOrUpdate**](ManagedDatabaseSecurityAlertPoliciesApi.md#managedDatabaseSecurityAlertPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/securityAlertPolicies/{securityAlertPolicyName} | 
[**managedDatabaseSecurityAlertPoliciesGet**](ManagedDatabaseSecurityAlertPoliciesApi.md#managedDatabaseSecurityAlertPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/securityAlertPolicies/{securityAlertPolicyName} | 
[**managedDatabaseSecurityAlertPoliciesListByDatabase**](ManagedDatabaseSecurityAlertPoliciesApi.md#managedDatabaseSecurityAlertPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/securityAlertPolicies | 



## managedDatabaseSecurityAlertPoliciesCreateOrUpdate

> ManagedDatabaseSecurityAlertPolicy managedDatabaseSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, managedInstanceName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates a database&#39;s security alert policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedDatabaseSecurityAlertPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let databaseName = "databaseName_example"; // String | The name of the managed database for which the security alert policy is defined.
let securityAlertPolicyName = "securityAlertPolicyName_example"; // String | The name of the security alert policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.ManagedDatabaseSecurityAlertPolicy(); // ManagedDatabaseSecurityAlertPolicy | The database security alert policy.
apiInstance.managedDatabaseSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, managedInstanceName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **managedInstanceName** | **String**| The name of the managed instance. | 
 **databaseName** | **String**| The name of the managed database for which the security alert policy is defined. | 
 **securityAlertPolicyName** | **String**| The name of the security alert policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**ManagedDatabaseSecurityAlertPolicy**](ManagedDatabaseSecurityAlertPolicy.md)| The database security alert policy. | 

### Return type

[**ManagedDatabaseSecurityAlertPolicy**](ManagedDatabaseSecurityAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## managedDatabaseSecurityAlertPoliciesGet

> ManagedDatabaseSecurityAlertPolicy managedDatabaseSecurityAlertPoliciesGet(resourceGroupName, managedInstanceName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion)



Gets a managed database&#39;s security alert policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedDatabaseSecurityAlertPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let databaseName = "databaseName_example"; // String | The name of the managed database for which the security alert policy is defined.
let securityAlertPolicyName = "securityAlertPolicyName_example"; // String | The name of the security alert policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.managedDatabaseSecurityAlertPoliciesGet(resourceGroupName, managedInstanceName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **managedInstanceName** | **String**| The name of the managed instance. | 
 **databaseName** | **String**| The name of the managed database for which the security alert policy is defined. | 
 **securityAlertPolicyName** | **String**| The name of the security alert policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ManagedDatabaseSecurityAlertPolicy**](ManagedDatabaseSecurityAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managedDatabaseSecurityAlertPoliciesListByDatabase

> ManagedDatabaseSecurityAlertPolicyListResult managedDatabaseSecurityAlertPoliciesListByDatabase(resourceGroupName, managedInstanceName, databaseName, subscriptionId, apiVersion)



Gets a list of managed database&#39;s security alert policies.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedDatabaseSecurityAlertPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let databaseName = "databaseName_example"; // String | The name of the managed database for which the security alert policies are defined.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.managedDatabaseSecurityAlertPoliciesListByDatabase(resourceGroupName, managedInstanceName, databaseName, subscriptionId, apiVersion, (error, data, response) => {
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
 **managedInstanceName** | **String**| The name of the managed instance. | 
 **databaseName** | **String**| The name of the managed database for which the security alert policies are defined. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ManagedDatabaseSecurityAlertPolicyListResult**](ManagedDatabaseSecurityAlertPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

