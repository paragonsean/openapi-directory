# SqlManagementClient.ManagedBackupShortTermRetentionPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managedBackupShortTermRetentionPoliciesCreateOrUpdate**](ManagedBackupShortTermRetentionPoliciesApi.md#managedBackupShortTermRetentionPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/backupShortTermRetentionPolicies/{policyName} | 
[**managedBackupShortTermRetentionPoliciesGet**](ManagedBackupShortTermRetentionPoliciesApi.md#managedBackupShortTermRetentionPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/backupShortTermRetentionPolicies/{policyName} | 
[**managedBackupShortTermRetentionPoliciesListByDatabase**](ManagedBackupShortTermRetentionPoliciesApi.md#managedBackupShortTermRetentionPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/backupShortTermRetentionPolicies | 
[**managedBackupShortTermRetentionPoliciesUpdate**](ManagedBackupShortTermRetentionPoliciesApi.md#managedBackupShortTermRetentionPoliciesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/backupShortTermRetentionPolicies/{policyName} | 



## managedBackupShortTermRetentionPoliciesCreateOrUpdate

> ManagedBackupShortTermRetentionPolicy managedBackupShortTermRetentionPoliciesCreateOrUpdate(resourceGroupName, managedInstanceName, databaseName, policyName, subscriptionId, apiVersion, parameters)



Updates a managed database&#39;s short term retention policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedBackupShortTermRetentionPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let databaseName = "databaseName_example"; // String | The name of the database.
let policyName = "policyName_example"; // String | The policy name. Should always be \"default\".
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.ManagedBackupShortTermRetentionPolicy(); // ManagedBackupShortTermRetentionPolicy | The short term retention policy info.
apiInstance.managedBackupShortTermRetentionPoliciesCreateOrUpdate(resourceGroupName, managedInstanceName, databaseName, policyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **policyName** | **String**| The policy name. Should always be \&quot;default\&quot;. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**ManagedBackupShortTermRetentionPolicy**](ManagedBackupShortTermRetentionPolicy.md)| The short term retention policy info. | 

### Return type

[**ManagedBackupShortTermRetentionPolicy**](ManagedBackupShortTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## managedBackupShortTermRetentionPoliciesGet

> ManagedBackupShortTermRetentionPolicy managedBackupShortTermRetentionPoliciesGet(resourceGroupName, managedInstanceName, databaseName, policyName, subscriptionId, apiVersion)



Gets a managed database&#39;s short term retention policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedBackupShortTermRetentionPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let databaseName = "databaseName_example"; // String | The name of the database.
let policyName = "policyName_example"; // String | The policy name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.managedBackupShortTermRetentionPoliciesGet(resourceGroupName, managedInstanceName, databaseName, policyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **policyName** | **String**| The policy name. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ManagedBackupShortTermRetentionPolicy**](ManagedBackupShortTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managedBackupShortTermRetentionPoliciesListByDatabase

> ManagedBackupShortTermRetentionPolicyListResult managedBackupShortTermRetentionPoliciesListByDatabase(resourceGroupName, managedInstanceName, databaseName, subscriptionId, apiVersion)



Gets a managed database&#39;s short term retention policy list.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedBackupShortTermRetentionPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let databaseName = "databaseName_example"; // String | The name of the database.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.managedBackupShortTermRetentionPoliciesListByDatabase(resourceGroupName, managedInstanceName, databaseName, subscriptionId, apiVersion, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ManagedBackupShortTermRetentionPolicyListResult**](ManagedBackupShortTermRetentionPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managedBackupShortTermRetentionPoliciesUpdate

> ManagedBackupShortTermRetentionPolicy managedBackupShortTermRetentionPoliciesUpdate(resourceGroupName, managedInstanceName, databaseName, policyName, subscriptionId, apiVersion, parameters)



Updates a managed database&#39;s short term retention policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedBackupShortTermRetentionPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let databaseName = "databaseName_example"; // String | The name of the database.
let policyName = "policyName_example"; // String | The policy name. Should always be \"default\".
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.ManagedBackupShortTermRetentionPolicy(); // ManagedBackupShortTermRetentionPolicy | The short term retention policy info.
apiInstance.managedBackupShortTermRetentionPoliciesUpdate(resourceGroupName, managedInstanceName, databaseName, policyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **policyName** | **String**| The policy name. Should always be \&quot;default\&quot;. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**ManagedBackupShortTermRetentionPolicy**](ManagedBackupShortTermRetentionPolicy.md)| The short term retention policy info. | 

### Return type

[**ManagedBackupShortTermRetentionPolicy**](ManagedBackupShortTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

