# SqlManagementClient.LongTermRetentionBackupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**longTermRetentionBackupsDelete**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups/{backupName} | 
[**longTermRetentionBackupsDeleteByResourceGroup**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsDeleteByResourceGroup) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups/{backupName} | 
[**longTermRetentionBackupsGet**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups/{backupName} | 
[**longTermRetentionBackupsGetByResourceGroup**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsGetByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups/{backupName} | 
[**longTermRetentionBackupsListByDatabase**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsListByDatabase) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups | 
[**longTermRetentionBackupsListByLocation**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsListByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionBackups | 
[**longTermRetentionBackupsListByResourceGroupDatabase**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsListByResourceGroupDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups | 
[**longTermRetentionBackupsListByResourceGroupLocation**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsListByResourceGroupLocation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionBackups | 
[**longTermRetentionBackupsListByResourceGroupServer**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsListByResourceGroupServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionBackups | 
[**longTermRetentionBackupsListByServer**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsListByServer) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionBackups | 



## longTermRetentionBackupsDelete

> longTermRetentionBackupsDelete(locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion)



Deletes a long term retention backup.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.LongTermRetentionBackupsApi();
let locationName = "locationName_example"; // String | The location of the database
let longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
let longTermRetentionDatabaseName = "longTermRetentionDatabaseName_example"; // String | The name of the database
let backupName = "backupName_example"; // String | The backup name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.longTermRetentionBackupsDelete(locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locationName** | **String**| The location of the database | 
 **longTermRetentionServerName** | **String**| The name of the server | 
 **longTermRetentionDatabaseName** | **String**| The name of the database | 
 **backupName** | **String**| The backup name. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## longTermRetentionBackupsDeleteByResourceGroup

> longTermRetentionBackupsDeleteByResourceGroup(resourceGroupName, locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion)



Deletes a long term retention backup.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.LongTermRetentionBackupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let locationName = "locationName_example"; // String | The location of the database
let longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
let longTermRetentionDatabaseName = "longTermRetentionDatabaseName_example"; // String | The name of the database
let backupName = "backupName_example"; // String | The backup name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.longTermRetentionBackupsDeleteByResourceGroup(resourceGroupName, locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **locationName** | **String**| The location of the database | 
 **longTermRetentionServerName** | **String**| The name of the server | 
 **longTermRetentionDatabaseName** | **String**| The name of the database | 
 **backupName** | **String**| The backup name. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## longTermRetentionBackupsGet

> LongTermRetentionBackup longTermRetentionBackupsGet(locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion)



Gets a long term retention backup.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.LongTermRetentionBackupsApi();
let locationName = "locationName_example"; // String | The location of the database.
let longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
let longTermRetentionDatabaseName = "longTermRetentionDatabaseName_example"; // String | The name of the database
let backupName = "backupName_example"; // String | The backup name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.longTermRetentionBackupsGet(locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **locationName** | **String**| The location of the database. | 
 **longTermRetentionServerName** | **String**| The name of the server | 
 **longTermRetentionDatabaseName** | **String**| The name of the database | 
 **backupName** | **String**| The backup name. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**LongTermRetentionBackup**](LongTermRetentionBackup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## longTermRetentionBackupsGetByResourceGroup

> LongTermRetentionBackup longTermRetentionBackupsGetByResourceGroup(resourceGroupName, locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion)



Gets a long term retention backup.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.LongTermRetentionBackupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let locationName = "locationName_example"; // String | The location of the database.
let longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
let longTermRetentionDatabaseName = "longTermRetentionDatabaseName_example"; // String | The name of the database
let backupName = "backupName_example"; // String | The backup name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.longTermRetentionBackupsGetByResourceGroup(resourceGroupName, locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **locationName** | **String**| The location of the database. | 
 **longTermRetentionServerName** | **String**| The name of the server | 
 **longTermRetentionDatabaseName** | **String**| The name of the database | 
 **backupName** | **String**| The backup name. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**LongTermRetentionBackup**](LongTermRetentionBackup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## longTermRetentionBackupsListByDatabase

> LongTermRetentionBackupListResult longTermRetentionBackupsListByDatabase(locationName, longTermRetentionServerName, longTermRetentionDatabaseName, subscriptionId, apiVersion, opts)



Lists all long term retention backups for a database.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.LongTermRetentionBackupsApi();
let locationName = "locationName_example"; // String | The location of the database
let longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
let longTermRetentionDatabaseName = "longTermRetentionDatabaseName_example"; // String | The name of the database
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'onlyLatestPerDatabase': true, // Boolean | Whether or not to only get the latest backup for each database.
  'databaseState': "databaseState_example" // String | Whether to query against just live databases, just deleted databases, or all databases.
};
apiInstance.longTermRetentionBackupsListByDatabase(locationName, longTermRetentionServerName, longTermRetentionDatabaseName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **locationName** | **String**| The location of the database | 
 **longTermRetentionServerName** | **String**| The name of the server | 
 **longTermRetentionDatabaseName** | **String**| The name of the database | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **onlyLatestPerDatabase** | **Boolean**| Whether or not to only get the latest backup for each database. | [optional] 
 **databaseState** | **String**| Whether to query against just live databases, just deleted databases, or all databases. | [optional] 

### Return type

[**LongTermRetentionBackupListResult**](LongTermRetentionBackupListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## longTermRetentionBackupsListByLocation

> LongTermRetentionBackupListResult longTermRetentionBackupsListByLocation(locationName, subscriptionId, apiVersion, opts)



Lists the long term retention backups for a given location.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.LongTermRetentionBackupsApi();
let locationName = "locationName_example"; // String | The location of the database
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'onlyLatestPerDatabase': true, // Boolean | Whether or not to only get the latest backup for each database.
  'databaseState': "databaseState_example" // String | Whether to query against just live databases, just deleted databases, or all databases.
};
apiInstance.longTermRetentionBackupsListByLocation(locationName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **locationName** | **String**| The location of the database | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **onlyLatestPerDatabase** | **Boolean**| Whether or not to only get the latest backup for each database. | [optional] 
 **databaseState** | **String**| Whether to query against just live databases, just deleted databases, or all databases. | [optional] 

### Return type

[**LongTermRetentionBackupListResult**](LongTermRetentionBackupListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## longTermRetentionBackupsListByResourceGroupDatabase

> LongTermRetentionBackupListResult longTermRetentionBackupsListByResourceGroupDatabase(resourceGroupName, locationName, longTermRetentionServerName, longTermRetentionDatabaseName, subscriptionId, apiVersion, opts)



Lists all long term retention backups for a database.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.LongTermRetentionBackupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let locationName = "locationName_example"; // String | The location of the database
let longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
let longTermRetentionDatabaseName = "longTermRetentionDatabaseName_example"; // String | The name of the database
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'onlyLatestPerDatabase': true, // Boolean | Whether or not to only get the latest backup for each database.
  'databaseState': "databaseState_example" // String | Whether to query against just live databases, just deleted databases, or all databases.
};
apiInstance.longTermRetentionBackupsListByResourceGroupDatabase(resourceGroupName, locationName, longTermRetentionServerName, longTermRetentionDatabaseName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **locationName** | **String**| The location of the database | 
 **longTermRetentionServerName** | **String**| The name of the server | 
 **longTermRetentionDatabaseName** | **String**| The name of the database | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **onlyLatestPerDatabase** | **Boolean**| Whether or not to only get the latest backup for each database. | [optional] 
 **databaseState** | **String**| Whether to query against just live databases, just deleted databases, or all databases. | [optional] 

### Return type

[**LongTermRetentionBackupListResult**](LongTermRetentionBackupListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## longTermRetentionBackupsListByResourceGroupLocation

> LongTermRetentionBackupListResult longTermRetentionBackupsListByResourceGroupLocation(resourceGroupName, locationName, subscriptionId, apiVersion, opts)



Lists the long term retention backups for a given location.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.LongTermRetentionBackupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let locationName = "locationName_example"; // String | The location of the database
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'onlyLatestPerDatabase': true, // Boolean | Whether or not to only get the latest backup for each database.
  'databaseState': "databaseState_example" // String | Whether to query against just live databases, just deleted databases, or all databases.
};
apiInstance.longTermRetentionBackupsListByResourceGroupLocation(resourceGroupName, locationName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **locationName** | **String**| The location of the database | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **onlyLatestPerDatabase** | **Boolean**| Whether or not to only get the latest backup for each database. | [optional] 
 **databaseState** | **String**| Whether to query against just live databases, just deleted databases, or all databases. | [optional] 

### Return type

[**LongTermRetentionBackupListResult**](LongTermRetentionBackupListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## longTermRetentionBackupsListByResourceGroupServer

> LongTermRetentionBackupListResult longTermRetentionBackupsListByResourceGroupServer(resourceGroupName, locationName, longTermRetentionServerName, subscriptionId, apiVersion, opts)



Lists the long term retention backups for a given server.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.LongTermRetentionBackupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let locationName = "locationName_example"; // String | The location of the database
let longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'onlyLatestPerDatabase': true, // Boolean | Whether or not to only get the latest backup for each database.
  'databaseState': "databaseState_example" // String | Whether to query against just live databases, just deleted databases, or all databases.
};
apiInstance.longTermRetentionBackupsListByResourceGroupServer(resourceGroupName, locationName, longTermRetentionServerName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **locationName** | **String**| The location of the database | 
 **longTermRetentionServerName** | **String**| The name of the server | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **onlyLatestPerDatabase** | **Boolean**| Whether or not to only get the latest backup for each database. | [optional] 
 **databaseState** | **String**| Whether to query against just live databases, just deleted databases, or all databases. | [optional] 

### Return type

[**LongTermRetentionBackupListResult**](LongTermRetentionBackupListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## longTermRetentionBackupsListByServer

> LongTermRetentionBackupListResult longTermRetentionBackupsListByServer(locationName, longTermRetentionServerName, subscriptionId, apiVersion, opts)



Lists the long term retention backups for a given server.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.LongTermRetentionBackupsApi();
let locationName = "locationName_example"; // String | The location of the database
let longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'onlyLatestPerDatabase': true, // Boolean | Whether or not to only get the latest backup for each database.
  'databaseState': "databaseState_example" // String | Whether to query against just live databases, just deleted databases, or all databases.
};
apiInstance.longTermRetentionBackupsListByServer(locationName, longTermRetentionServerName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **locationName** | **String**| The location of the database | 
 **longTermRetentionServerName** | **String**| The name of the server | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **onlyLatestPerDatabase** | **Boolean**| Whether or not to only get the latest backup for each database. | [optional] 
 **databaseState** | **String**| Whether to query against just live databases, just deleted databases, or all databases. | [optional] 

### Return type

[**LongTermRetentionBackupListResult**](LongTermRetentionBackupListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

