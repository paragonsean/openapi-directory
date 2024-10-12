# AzureSqlDatabaseImportExportSpec.ImportExportApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**databasesCreateImportOperation**](ImportExportApi.md#databasesCreateImportOperation) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/extensions/{extensionName} | 
[**databasesExport**](ImportExportApi.md#databasesExport) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/export | 
[**databasesImport**](ImportExportApi.md#databasesImport) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/import | 



## databasesCreateImportOperation

> ImportExportResponse databasesCreateImportOperation(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, extensionName, parameters)



Creates an import operation that imports a bacpac into an existing database. The existing database must be empty.

### Example

```javascript
import AzureSqlDatabaseImportExportSpec from 'azure_sql_database_import_export_spec';

let apiInstance = new AzureSqlDatabaseImportExportSpec.ImportExportApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database to import into
let extensionName = "extensionName_example"; // String | The name of the operation to perform
let parameters = new AzureSqlDatabaseImportExportSpec.ImportExtensionRequest(); // ImportExtensionRequest | The required parameters for importing a Bacpac into a database.
apiInstance.databasesCreateImportOperation(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, extensionName, parameters, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database to import into | 
 **extensionName** | **String**| The name of the operation to perform | 
 **parameters** | [**ImportExtensionRequest**](ImportExtensionRequest.md)| The required parameters for importing a Bacpac into a database. | 

### Return type

[**ImportExportResponse**](ImportExportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databasesExport

> ImportExportResponse databasesExport(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, parameters)



Exports a database to a bacpac.

### Example

```javascript
import AzureSqlDatabaseImportExportSpec from 'azure_sql_database_import_export_spec';

let apiInstance = new AzureSqlDatabaseImportExportSpec.ImportExportApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database to be exported.
let parameters = new AzureSqlDatabaseImportExportSpec.ExportRequest(); // ExportRequest | The required parameters for exporting a database.
apiInstance.databasesExport(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, parameters, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database to be exported. | 
 **parameters** | [**ExportRequest**](ExportRequest.md)| The required parameters for exporting a database. | 

### Return type

[**ImportExportResponse**](ImportExportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databasesImport

> ImportExportResponse databasesImport(apiVersion, subscriptionId, resourceGroupName, serverName, parameters)



Imports a bacpac into a new database. 

### Example

```javascript
import AzureSqlDatabaseImportExportSpec from 'azure_sql_database_import_export_spec';

let apiInstance = new AzureSqlDatabaseImportExportSpec.ImportExportApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let parameters = new AzureSqlDatabaseImportExportSpec.ImportRequest(); // ImportRequest | The required parameters for importing a Bacpac into a database.
apiInstance.databasesImport(apiVersion, subscriptionId, resourceGroupName, serverName, parameters, (error, data, response) => {
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
 **parameters** | [**ImportRequest**](ImportRequest.md)| The required parameters for importing a Bacpac into a database. | 

### Return type

[**ImportExportResponse**](ImportExportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

