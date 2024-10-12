# SqlManagementClient.DatabaseSecurityAlertPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**databaseSecurityAlertPoliciesCreateOrUpdate**](DatabaseSecurityAlertPoliciesApi.md#databaseSecurityAlertPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/securityAlertPolicies/{securityAlertPolicyName} | 
[**databaseSecurityAlertPoliciesGet**](DatabaseSecurityAlertPoliciesApi.md#databaseSecurityAlertPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/securityAlertPolicies/{securityAlertPolicyName} | 
[**databaseSecurityAlertPoliciesListByDatabase**](DatabaseSecurityAlertPoliciesApi.md#databaseSecurityAlertPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/securityAlertPolicies | 



## databaseSecurityAlertPoliciesCreateOrUpdate

> DatabaseSecurityAlertPolicy databaseSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates a database&#39;s security alert policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.DatabaseSecurityAlertPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the  server.
let databaseName = "databaseName_example"; // String | The name of the  database for which the security alert policy is defined.
let securityAlertPolicyName = "securityAlertPolicyName_example"; // String | The name of the security alert policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.DatabaseSecurityAlertPolicy(); // DatabaseSecurityAlertPolicy | The database security alert policy.
apiInstance.databaseSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **serverName** | **String**| The name of the  server. | 
 **databaseName** | **String**| The name of the  database for which the security alert policy is defined. | 
 **securityAlertPolicyName** | **String**| The name of the security alert policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**DatabaseSecurityAlertPolicy**](DatabaseSecurityAlertPolicy.md)| The database security alert policy. | 

### Return type

[**DatabaseSecurityAlertPolicy**](DatabaseSecurityAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseSecurityAlertPoliciesGet

> DatabaseSecurityAlertPolicy databaseSecurityAlertPoliciesGet(resourceGroupName, serverName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion)



Gets a  database&#39;s security alert policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.DatabaseSecurityAlertPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the  server.
let databaseName = "databaseName_example"; // String | The name of the  database for which the security alert policy is defined.
let securityAlertPolicyName = "securityAlertPolicyName_example"; // String | The name of the security alert policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.databaseSecurityAlertPoliciesGet(resourceGroupName, serverName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **serverName** | **String**| The name of the  server. | 
 **databaseName** | **String**| The name of the  database for which the security alert policy is defined. | 
 **securityAlertPolicyName** | **String**| The name of the security alert policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**DatabaseSecurityAlertPolicy**](DatabaseSecurityAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseSecurityAlertPoliciesListByDatabase

> DatabaseSecurityAlertListResult databaseSecurityAlertPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion)



Gets a list of database&#39;s security alert policies.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.DatabaseSecurityAlertPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the  server.
let databaseName = "databaseName_example"; // String | The name of the  database for which the security alert policy is defined.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.databaseSecurityAlertPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion, (error, data, response) => {
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
 **serverName** | **String**| The name of the  server. | 
 **databaseName** | **String**| The name of the  database for which the security alert policy is defined. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**DatabaseSecurityAlertListResult**](DatabaseSecurityAlertListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

