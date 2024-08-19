# AzureMigrateHub.DatabasesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**databasesEnumerateDatabases**](DatabasesApi.md#databasesEnumerateDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/databases | Gets a list of databases in the migrate project.
[**databasesGetDatabase**](DatabasesApi.md#databasesGetDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/databases/{databaseName} | Gets a database in the migrate project.



## databasesEnumerateDatabases

> DatabaseCollection databasesEnumerateDatabases(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, opts)

Gets a list of databases in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.DatabasesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'continuationToken': "continuationToken_example", // String | The continuation token.
  'pageSize': 56, // Number | The number of items to be returned in a single page. This value is honored only if it is less than the 100.
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.databasesEnumerateDatabases(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, opts, (error, data, response) => {
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

[**DatabaseCollection**](DatabaseCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databasesGetDatabase

> Database databasesGetDatabase(subscriptionId, resourceGroupName, migrateProjectName, databaseName, apiVersion, opts)

Gets a database in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.DatabasesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let databaseName = "databaseName_example"; // String | Unique name of a database in Azure migration hub.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.databasesGetDatabase(subscriptionId, resourceGroupName, migrateProjectName, databaseName, apiVersion, opts, (error, data, response) => {
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
 **databaseName** | **String**| Unique name of a database in Azure migration hub. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**Database**](Database.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

