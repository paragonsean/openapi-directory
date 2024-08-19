# AzureMigrateHub.DatabaseInstancesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**databaseInstancesEnumerateDatabaseInstances**](DatabaseInstancesApi.md#databaseInstancesEnumerateDatabaseInstances) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/databaseInstances | Gets a list of database instances in the migrate project.
[**databaseInstancesGetDatabaseInstance**](DatabaseInstancesApi.md#databaseInstancesGetDatabaseInstance) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/databaseInstances/{databaseInstanceName} | Gets a database instance in the migrate project.



## databaseInstancesEnumerateDatabaseInstances

> DatabaseInstanceCollection databaseInstancesEnumerateDatabaseInstances(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, opts)

Gets a list of database instances in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.DatabaseInstancesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'continuationToken': "continuationToken_example", // String | The continuation token.
  'pageSize': 56, // Number | The number of items to be returned in a single page. This value is honored only if it is less than the 100.
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.databaseInstancesEnumerateDatabaseInstances(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | 
 **migrateProjectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **continuationToken** | **String**| The continuation token. | [optional] 
 **pageSize** | **Number**| The number of items to be returned in a single page. This value is honored only if it is less than the 100. | [optional] 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**DatabaseInstanceCollection**](DatabaseInstanceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseInstancesGetDatabaseInstance

> DatabaseInstance databaseInstancesGetDatabaseInstance(subscriptionId, resourceGroupName, migrateProjectName, databaseInstanceName, apiVersion, opts)

Gets a database instance in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.DatabaseInstancesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let databaseInstanceName = "databaseInstanceName_example"; // String | Unique name of a database instance in Azure migration hub.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.databaseInstancesGetDatabaseInstance(subscriptionId, resourceGroupName, migrateProjectName, databaseInstanceName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | 
 **migrateProjectName** | **String**| Name of the Azure Migrate project. | 
 **databaseInstanceName** | **String**| Unique name of a database instance in Azure migration hub. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**DatabaseInstance**](DatabaseInstance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

