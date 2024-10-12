# SqlManagementClient.BackupShortTermRetentionPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupShortTermRetentionPoliciesCreateOrUpdate**](BackupShortTermRetentionPoliciesApi.md#backupShortTermRetentionPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupShortTermRetentionPolicies/{policyName} | 
[**backupShortTermRetentionPoliciesGet**](BackupShortTermRetentionPoliciesApi.md#backupShortTermRetentionPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupShortTermRetentionPolicies/{policyName} | 
[**backupShortTermRetentionPoliciesListByDatabase**](BackupShortTermRetentionPoliciesApi.md#backupShortTermRetentionPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupShortTermRetentionPolicies | 
[**backupShortTermRetentionPoliciesUpdate**](BackupShortTermRetentionPoliciesApi.md#backupShortTermRetentionPoliciesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupShortTermRetentionPolicies/{policyName} | 



## backupShortTermRetentionPoliciesCreateOrUpdate

> BackupShortTermRetentionPolicy backupShortTermRetentionPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion, parameters)



Updates a database&#39;s short term retention policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BackupShortTermRetentionPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let policyName = "policyName_example"; // String | The policy name. Should always be \"default\".
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.BackupShortTermRetentionPolicy(); // BackupShortTermRetentionPolicy | The short term retention policy info.
apiInstance.backupShortTermRetentionPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **policyName** | **String**| The policy name. Should always be \&quot;default\&quot;. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**BackupShortTermRetentionPolicy**](BackupShortTermRetentionPolicy.md)| The short term retention policy info. | 

### Return type

[**BackupShortTermRetentionPolicy**](BackupShortTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## backupShortTermRetentionPoliciesGet

> BackupShortTermRetentionPolicy backupShortTermRetentionPoliciesGet(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion)



Gets a database&#39;s short term retention policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BackupShortTermRetentionPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let policyName = "policyName_example"; // String | The policy name. Should always be \"default\".
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.backupShortTermRetentionPoliciesGet(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **policyName** | **String**| The policy name. Should always be \&quot;default\&quot;. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**BackupShortTermRetentionPolicy**](BackupShortTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## backupShortTermRetentionPoliciesListByDatabase

> BackupShortTermRetentionPolicyListResult backupShortTermRetentionPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion)



Gets a database&#39;s short term retention policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BackupShortTermRetentionPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.backupShortTermRetentionPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**BackupShortTermRetentionPolicyListResult**](BackupShortTermRetentionPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## backupShortTermRetentionPoliciesUpdate

> BackupShortTermRetentionPolicy backupShortTermRetentionPoliciesUpdate(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion, parameters)



Updates a database&#39;s short term retention policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BackupShortTermRetentionPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let policyName = "policyName_example"; // String | The policy name. Should always be \"default\".
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.BackupShortTermRetentionPolicy(); // BackupShortTermRetentionPolicy | The short term retention policy info.
apiInstance.backupShortTermRetentionPoliciesUpdate(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **policyName** | **String**| The policy name. Should always be \&quot;default\&quot;. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**BackupShortTermRetentionPolicy**](BackupShortTermRetentionPolicy.md)| The short term retention policy info. | 

### Return type

[**BackupShortTermRetentionPolicy**](BackupShortTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

