# SqlManagementClient.DatabaseColumnsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**databaseColumnsGet**](DatabaseColumnsApi.md#databaseColumnsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/columns/{columnName} | 
[**databaseColumnsListByTable**](DatabaseColumnsApi.md#databaseColumnsListByTable) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/columns | 



## databaseColumnsGet

> DatabaseColumn databaseColumnsGet(resourceGroupName, serverName, databaseName, schemaName, tableName, columnName, subscriptionId, apiVersion)



Get database column

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.DatabaseColumnsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let schemaName = "schemaName_example"; // String | The name of the schema.
let tableName = "tableName_example"; // String | The name of the table.
let columnName = "columnName_example"; // String | The name of the column.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.databaseColumnsGet(resourceGroupName, serverName, databaseName, schemaName, tableName, columnName, subscriptionId, apiVersion, (error, data, response) => {
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
 **schemaName** | **String**| The name of the schema. | 
 **tableName** | **String**| The name of the table. | 
 **columnName** | **String**| The name of the column. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**DatabaseColumn**](DatabaseColumn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseColumnsListByTable

> DatabaseColumnListResult databaseColumnsListByTable(resourceGroupName, serverName, databaseName, schemaName, tableName, subscriptionId, apiVersion, opts)



List database columns

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.DatabaseColumnsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let schemaName = "schemaName_example"; // String | The name of the schema.
let tableName = "tableName_example"; // String | The name of the table.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'filter': "filter_example" // String | An OData filter expression that filters elements in the collection.
};
apiInstance.databaseColumnsListByTable(resourceGroupName, serverName, databaseName, schemaName, tableName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **schemaName** | **String**| The name of the schema. | 
 **tableName** | **String**| The name of the table. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **filter** | **String**| An OData filter expression that filters elements in the collection. | [optional] 

### Return type

[**DatabaseColumnListResult**](DatabaseColumnListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

