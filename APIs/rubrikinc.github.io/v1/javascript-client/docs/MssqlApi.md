# RubrikRestApi.MssqlApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignMssqlSlaProperties**](MssqlApi.md#assignMssqlSlaProperties) | **POST** /mssql/sla_domain/assign | Assign SLA properties to SQL Server objects
[**browseMssqlBackupFiles**](MssqlApi.md#browseMssqlBackupFiles) | **POST** /mssql/db/{id}/browse | List snapshots and logs from a Microsoft SQL database
[**bulkUpdateMssqlDbV1**](MssqlApi.md#bulkUpdateMssqlDbV1) | **PATCH** /mssql/db/bulk | Update multiple Microsoft SQL databases
[**countMssqlDbV1**](MssqlApi.md#countMssqlDbV1) | **GET** /mssql/db/count | Returns a count of Microsoft SQL databases
[**countMssqlInstanceV1**](MssqlApi.md#countMssqlInstanceV1) | **GET** /mssql/instance/count | Returns a count of Microsoft SQL instances
[**createDownloadMssqlBackupFiles**](MssqlApi.md#createDownloadMssqlBackupFiles) | **POST** /mssql/db/{id}/download_files | Download snapshots and logs backups from a Microsoft SQL Database
[**createDownloadMssqlBackupFilesById**](MssqlApi.md#createDownloadMssqlBackupFilesById) | **POST** /mssql/db/{id}/download_files_by_id | Downloads a list of snapshot and log backups from a Microsoft SQL database
[**createExportMssqlDb**](MssqlApi.md#createExportMssqlDb) | **POST** /mssql/db/{id}/export | Export a Microsoft SQL database to a new location
[**createLogShippingConfiguration**](MssqlApi.md#createLogShippingConfiguration) | **POST** /mssql/db/{id}/log_shipping | Create a log shipping configuration
[**createMssqlHostConfig**](MssqlApi.md#createMssqlHostConfig) | **POST** /mssql/host/configuration | Create a SQL Server host configuration
[**createMssqlMount**](MssqlApi.md#createMssqlMount) | **POST** /mssql/db/{id}/mount | Live Mount SQL Server database from a point in time copy
[**createMssqlUnmount**](MssqlApi.md#createMssqlUnmount) | **DELETE** /mssql/db/mount/{id} | Delete a Live Mount of a SQL Server database
[**createOnDemandMssqlBackup**](MssqlApi.md#createOnDemandMssqlBackup) | **POST** /mssql/db/{id}/snapshot | Take an on-demand backup of a Microsoft SQL database
[**createOnDemandMssqlBatchBackupV1**](MssqlApi.md#createOnDemandMssqlBatchBackupV1) | **POST** /mssql/db/bulk/snapshot | Take an on-demand backup of multiple Microsoft SQL databases
[**createOnDemandMssqlLogBackup**](MssqlApi.md#createOnDemandMssqlLogBackup) | **POST** /mssql/db/{id}/log_backup | Take an on-demand log backup for a Microsoft SQL database
[**createRestoreMssqlDb**](MssqlApi.md#createRestoreMssqlDb) | **POST** /mssql/db/{id}/restore | Restore a Microsoft SQL database
[**deleteDownloadedMssqlDbRecoverableRangesV1**](MssqlApi.md#deleteDownloadedMssqlDbRecoverableRangesV1) | **DELETE** /mssql/db/{id}/recoverable_range/download | Delete downloaded recoverable ranges of a Microsoft SQL database
[**deleteLogShippingConfiguration**](MssqlApi.md#deleteLogShippingConfiguration) | **DELETE** /mssql/db/log_shipping/{id} | Delete a specified log shipping configuration
[**deleteMssqlDbSnapshots**](MssqlApi.md#deleteMssqlDbSnapshots) | **DELETE** /mssql/db/{id}/snapshot | Delete all snapshots of a Microsoft SQL database
[**deleteMssqlHostConfig**](MssqlApi.md#deleteMssqlHostConfig) | **DELETE** /mssql/host/configuration/{host_id} | Delete the SQL Server host configuration
[**downloadFromArchive**](MssqlApi.md#downloadFromArchive) | **POST** /mssql/db/{id}/download | Download snapshots and log backups from archival
[**getCompatibleMssqlInstancesV1**](MssqlApi.md#getCompatibleMssqlInstancesV1) | **GET** /mssql/db/{id}/compatible_instance | Get compatible instances for the recovery of a Microsoft SQL database
[**getDefaultDbPropertiesV1**](MssqlApi.md#getDefaultDbPropertiesV1) | **GET** /mssql/db/defaults | Returns the current default properties for Microsoft SQL databases
[**getDeleteMssqlDbRecoverableRangesStatusV1**](MssqlApi.md#getDeleteMssqlDbRecoverableRangesStatusV1) | **GET** /mssql/db/recoverable_range/download/{id} | Get the deletion status of downloaded recoverable ranges
[**getLogShippingConfiguration**](MssqlApi.md#getLogShippingConfiguration) | **GET** /mssql/db/log_shipping/{id} | Get a log shipping configuration
[**getMissedMssqlDbSnapshots**](MssqlApi.md#getMissedMssqlDbSnapshots) | **GET** /mssql/db/{id}/missed_snapshot | Get summary information for missed snapshots of a SQL database
[**getMssqlAsyncRequestStatus**](MssqlApi.md#getMssqlAsyncRequestStatus) | **GET** /mssql/request/{id} | Get details for an async request
[**getMssqlAvailabilityGroupV1**](MssqlApi.md#getMssqlAvailabilityGroupV1) | **GET** /mssql/availability_group/{id} | Returns detailed information for a Microsoft SQL availability group
[**getMssqlDb**](MssqlApi.md#getMssqlDb) | **GET** /mssql/db/{id} | Get detailed information for a Microsoft SQL database
[**getMssqlDbMissedRecoverableRanges**](MssqlApi.md#getMssqlDbMissedRecoverableRanges) | **GET** /mssql/db/{id}/missed_recoverable_range | Get missed recoverable ranges of a Microsoft SQL database
[**getMssqlDbRecoverableRanges**](MssqlApi.md#getMssqlDbRecoverableRanges) | **GET** /mssql/db/{id}/recoverable_range | Get recoverable ranges of a Microsoft SQL database
[**getMssqlDbSnapshot**](MssqlApi.md#getMssqlDbSnapshot) | **GET** /mssql/db/snapshot/{id} | Get details information about a Microsoft SQL database snapshot
[**getMssqlHierarchyChildren**](MssqlApi.md#getMssqlHierarchyChildren) | **GET** /mssql/hierarchy/{id}/children | Get list of immediate descendant objects
[**getMssqlHierarchyDescendants**](MssqlApi.md#getMssqlHierarchyDescendants) | **GET** /mssql/hierarchy/{id}/descendants | Get list of descendant objects
[**getMssqlHierarchyObject**](MssqlApi.md#getMssqlHierarchyObject) | **GET** /mssql/hierarchy/{id} | Get summary of a SQL Server hierarchy object
[**getMssqlHostConfig**](MssqlApi.md#getMssqlHostConfig) | **GET** /mssql/host/configuration/{host_id} | Get the configuration for a specific host
[**getMssqlInstance**](MssqlApi.md#getMssqlInstance) | **GET** /mssql/instance/{id} | Get detailed information for a Microsoft SQL instance
[**getMssqlMount**](MssqlApi.md#getMssqlMount) | **GET** /mssql/db/mount/{id} | Get detailed information for a Live Mount of a SQL Server database
[**getOnDemandMssqlBatchBackupResultV1**](MssqlApi.md#getOnDemandMssqlBatchBackupResultV1) | **GET** /mssql/db/bulk/snapshot/{id} | Returns details for an on-demand backup of multiple Microsoft SQL databases
[**mssqlGetRestoreFilesV1**](MssqlApi.md#mssqlGetRestoreFilesV1) | **GET** /mssql/db/{id}/restore_files | Returns a list all database files to be restored
[**mssqlGetSnappableIdV1**](MssqlApi.md#mssqlGetSnappableIdV1) | **GET** /mssql/db/{id}/snappable_id | Returns the snappableId for a Microsoft SQL database
[**mssqlRestoreEstimateV1**](MssqlApi.md#mssqlRestoreEstimateV1) | **GET** /mssql/db/{id}/restore_estimate | Returns a size estimate for a restore or export
[**queryLogShippingConfigurations**](MssqlApi.md#queryLogShippingConfigurations) | **GET** /mssql/db/log_shipping | Get log shipping configurations
[**queryMssqlAvailabilityGroupV1**](MssqlApi.md#queryMssqlAvailabilityGroupV1) | **GET** /mssql/availability_group | Returns summary information for Microsoft SQL availability groups
[**queryMssqlDb**](MssqlApi.md#queryMssqlDb) | **GET** /mssql/db | Get summary information for SQL Server databases
[**queryMssqlDbSnapshot**](MssqlApi.md#queryMssqlDbSnapshot) | **GET** /mssql/db/{id}/snapshot | Get summary information for snapshots of a Microsoft SQL database
[**queryMssqlHostConfig**](MssqlApi.md#queryMssqlHostConfig) | **GET** /mssql/host/configuration | Get the summary of SQL Server host configurations
[**queryMssqlInstance**](MssqlApi.md#queryMssqlInstance) | **GET** /mssql/instance | Get summary information for Microsoft SQL instances
[**queryMssqlMount**](MssqlApi.md#queryMssqlMount) | **GET** /mssql/db/mount | Get summary information for all Live Mounts SQL Server databases
[**reseedSecondary**](MssqlApi.md#reseedSecondary) | **POST** /mssql/db/log_shipping/{id}/reseed | Reseed a secondary database
[**updateDefaultDbPropertiesV1**](MssqlApi.md#updateDefaultDbPropertiesV1) | **PATCH** /mssql/db/defaults | Update the default properties for Microsoft SQL databases
[**updateLogShippingConfiguration**](MssqlApi.md#updateLogShippingConfiguration) | **PATCH** /mssql/db/log_shipping/{id} | Update a specified log shipping configuration
[**updateMssqlAvailabilityGroupV1**](MssqlApi.md#updateMssqlAvailabilityGroupV1) | **PATCH** /mssql/availability_group/{id} | Update a Microsoft SQL availability group
[**updateMssqlDb**](MssqlApi.md#updateMssqlDb) | **PATCH** /mssql/db/{id} | Update a Microsoft SQL database
[**updateMssqlHostConfig**](MssqlApi.md#updateMssqlHostConfig) | **PATCH** /mssql/host/configuration/{host_id} | Update host configuration
[**updateMssqlInstance**](MssqlApi.md#updateMssqlInstance) | **PATCH** /mssql/instance/{id} | Update a Microsoft SQL instance



## assignMssqlSlaProperties

> assignMssqlSlaProperties(mssqlSlaDomainAssignInfo)

Assign SLA properties to SQL Server objects

Assigns SLA Domain properties to SQL Server objects. Hosts and Windows clusters cannot be assigned SLA Domains directly. The SLA Domains are instead applied to the SQL Server child objects within the Host or Windows Cluster object. Newly discovered SQL Server objects within a given Host or Windows Cluster object do not inherit SLA Domain properties from other child SQL Server objects with the same parent object. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let mssqlSlaDomainAssignInfo = new RubrikRestApi.MssqlSlaDomainAssignInfo(); // MssqlSlaDomainAssignInfo | Update information.
apiInstance.assignMssqlSlaProperties(mssqlSlaDomainAssignInfo, (error, data, response) => {
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
 **mssqlSlaDomainAssignInfo** | [**MssqlSlaDomainAssignInfo**](MssqlSlaDomainAssignInfo.md)| Update information. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## browseMssqlBackupFiles

> MssqlBackups browseMssqlBackupFiles(id, mssqlBackupSelection)

List snapshots and logs from a Microsoft SQL database

When a recovery point is set, this API endpoint returns the snapshot and list of logs needed to restore the database to the recovery point. When a time range or LSN range is specified, this API endpoint returns the snapshots and logs that overlap the specified range. Specify only a recovery point or a range. Specify only LSNs or times. This endpoint is only used to fetch data, but uses POST instead of GET due to limitations on parameters used in the body of a GET request. The parameter set for this endpoint is shared with the download_file endpoint. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let mssqlBackupSelection = new RubrikRestApi.MssqlBackupSelection(); // MssqlBackupSelection | Configuration for the browse request.
apiInstance.browseMssqlBackupFiles(id, mssqlBackupSelection, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **mssqlBackupSelection** | [**MssqlBackupSelection**](MssqlBackupSelection.md)| Configuration for the browse request. | 

### Return type

[**MssqlBackups**](MssqlBackups.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bulkUpdateMssqlDbV1

> [MssqlDbDetail] bulkUpdateMssqlDbV1(mssqlDbUpdateId)

Update multiple Microsoft SQL databases

Update multiple Microsoft SQL databases with the specified properties.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let mssqlDbUpdateId = [new RubrikRestApi.MssqlDbUpdateId()]; // [MssqlDbUpdateId] | Properties to update for each database.
apiInstance.bulkUpdateMssqlDbV1(mssqlDbUpdateId, (error, data, response) => {
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
 **mssqlDbUpdateId** | [**[MssqlDbUpdateId]**](MssqlDbUpdateId.md)| Properties to update for each database. | 

### Return type

[**[MssqlDbDetail]**](MssqlDbDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## countMssqlDbV1

> ProtectedObjectsCount countMssqlDbV1(opts)

Returns a count of Microsoft SQL databases

Returns a count of Microsoft SQL databases.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let opts = {
  'rootId': "rootId_example" // String | Include only instances that belong to this root.
};
apiInstance.countMssqlDbV1(opts, (error, data, response) => {
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
 **rootId** | **String**| Include only instances that belong to this root. | [optional] 

### Return type

[**ProtectedObjectsCount**](ProtectedObjectsCount.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countMssqlInstanceV1

> CountResponse countMssqlInstanceV1()

Returns a count of Microsoft SQL instances

Returns a count of all Microsoft SQL instances.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
apiInstance.countMssqlInstanceV1((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CountResponse**](CountResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createDownloadMssqlBackupFiles

> AsyncRequestStatus createDownloadMssqlBackupFiles(id, mssqlBackupSelection)

Download snapshots and logs backups from a Microsoft SQL Database

Starts an asynchronous request to download a set of backup files as a single compressed zipfile. When a recovery point is set, this API endpoint returns the snapshot and list of logs that Rubrik CDM would use to restore the database to the recovery point. When a time range or LSN range is specified, this API endpoint returns the snapshots and logs that overlap the specified range. Specify only a point in time or a range. Specify only LSNs or times. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let mssqlBackupSelection = new RubrikRestApi.MssqlBackupSelection(); // MssqlBackupSelection | Configuration for a download files job.
apiInstance.createDownloadMssqlBackupFiles(id, mssqlBackupSelection, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **mssqlBackupSelection** | [**MssqlBackupSelection**](MssqlBackupSelection.md)| Configuration for a download files job. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDownloadMssqlBackupFilesById

> AsyncRequestStatus createDownloadMssqlBackupFilesById(id, downloadMssqlBackupFilesByIdJobConfig)

Downloads a list of snapshot and log backups from a Microsoft SQL database

Downloads a list of snapshot and log backups from a Microsoft SQL database.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let downloadMssqlBackupFilesByIdJobConfig = new RubrikRestApi.DownloadMssqlBackupFilesByIdJobConfig(); // DownloadMssqlBackupFilesByIdJobConfig | Configuration for a download files by id job.
apiInstance.createDownloadMssqlBackupFilesById(id, downloadMssqlBackupFilesByIdJobConfig, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **downloadMssqlBackupFilesByIdJobConfig** | [**DownloadMssqlBackupFilesByIdJobConfig**](DownloadMssqlBackupFilesByIdJobConfig.md)| Configuration for a download files by id job. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createExportMssqlDb

> AsyncRequestStatus createExportMssqlDb(id, exportMssqlDbJobConfig)

Export a Microsoft SQL database to a new location

Create a request to export a Microsoft SQL database. To check the result of the request, poll /mssql/request/{id}.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let exportMssqlDbJobConfig = new RubrikRestApi.ExportMssqlDbJobConfig(); // ExportMssqlDbJobConfig | Configuration for the export.
apiInstance.createExportMssqlDb(id, exportMssqlDbJobConfig, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **exportMssqlDbJobConfig** | [**ExportMssqlDbJobConfig**](ExportMssqlDbJobConfig.md)| Configuration for the export. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLogShippingConfiguration

> AsyncRequestStatus createLogShippingConfiguration(id, mssqlLogShippingCreateConfig)

Create a log shipping configuration

Create a log shipping configuration between a specified primary database and a specified secondary database. The transaction logs from the primary database are regularly restored to the secondary database in order to maintain the secondary database as a point-in-time copy of the primary database. The primary database must have log backups configured, and it must be in the full or bulk-logged recovery model.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the primary database object.
let mssqlLogShippingCreateConfig = new RubrikRestApi.MssqlLogShippingCreateConfig(); // MssqlLogShippingCreateConfig | Object containing the values of a log shipping configuration.
apiInstance.createLogShippingConfiguration(id, mssqlLogShippingCreateConfig, (error, data, response) => {
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
 **id** | **String**| ID of the primary database object. | 
 **mssqlLogShippingCreateConfig** | [**MssqlLogShippingCreateConfig**](MssqlLogShippingCreateConfig.md)| Object containing the values of a log shipping configuration. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMssqlHostConfig

> MssqlHostConfiguration createMssqlHostConfig(mssqlHostConfigurationWithHostId)

Create a SQL Server host configuration

Creates a SQL Server host configuration.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let mssqlHostConfigurationWithHostId = new RubrikRestApi.MssqlHostConfigurationWithHostId(); // MssqlHostConfigurationWithHostId | Parameters for creating a SQL Server host configuration.
apiInstance.createMssqlHostConfig(mssqlHostConfigurationWithHostId, (error, data, response) => {
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
 **mssqlHostConfigurationWithHostId** | [**MssqlHostConfigurationWithHostId**](MssqlHostConfigurationWithHostId.md)| Parameters for creating a SQL Server host configuration. | 

### Return type

[**MssqlHostConfiguration**](MssqlHostConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMssqlMount

> AsyncRequestStatus createMssqlMount(id, mountMssqlDbConfig)

Live Mount SQL Server database from a point in time copy

Create an asynchronous request to create a Live Mount SQL Server database. Poll the task status by using /mssql/request/{id}.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the SQL Server database.
let mountMssqlDbConfig = new RubrikRestApi.MountMssqlDbConfig(); // MountMssqlDbConfig | Configuration for the Live Mount.
apiInstance.createMssqlMount(id, mountMssqlDbConfig, (error, data, response) => {
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
 **id** | **String**| ID of the SQL Server database. | 
 **mountMssqlDbConfig** | [**MountMssqlDbConfig**](MountMssqlDbConfig.md)| Configuration for the Live Mount. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMssqlUnmount

> AsyncRequestStatus createMssqlUnmount(id, opts)

Delete a Live Mount of a SQL Server database

Create an async request to delete a Live Mount of a SQL Server database. Poll the task status by using /mssql/request/{id}.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Live Mount to delete.
let opts = {
  'force': true // Boolean | Remove all data within the Rubrik cluster related to the Live Mount, even if the SQL Server database cannot be contacted. Default value is false.
};
apiInstance.createMssqlUnmount(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Live Mount to delete. | 
 **force** | **Boolean**| Remove all data within the Rubrik cluster related to the Live Mount, even if the SQL Server database cannot be contacted. Default value is false. | [optional] 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createOnDemandMssqlBackup

> AsyncRequestStatus createOnDemandMssqlBackup(id, mssqlBackupJobConfig)

Take an on-demand backup of a Microsoft SQL database

Take an on-demand backup of a Microsoft SQL database. The forceFullSnapshot property can be set to true to force a full snapshot. To check the result of the request, poll /mssql/request/{id}.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let mssqlBackupJobConfig = new RubrikRestApi.MssqlBackupJobConfig(); // MssqlBackupJobConfig | Configuration for the on-demand backup.
apiInstance.createOnDemandMssqlBackup(id, mssqlBackupJobConfig, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **mssqlBackupJobConfig** | [**MssqlBackupJobConfig**](MssqlBackupJobConfig.md)| Configuration for the on-demand backup. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOnDemandMssqlBatchBackupV1

> AsyncRequestStatus createOnDemandMssqlBatchBackupV1(mssqlBatchBackupJobConfig)

Take an on-demand backup of multiple Microsoft SQL databases

Take an on-demand backup of one or more Microsoft SQL databases. Set the forceFullSnapshot property to true to force a full snapshot for every database that is specified. Only one snapshot will be taken for each database, even if a database is included multiple times in the fields of the request body. To check the result of the request, poll /mssql/request/{id}.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let mssqlBatchBackupJobConfig = new RubrikRestApi.MssqlBatchBackupJobConfig(); // MssqlBatchBackupJobConfig | Configuration for the on-demand backups.
apiInstance.createOnDemandMssqlBatchBackupV1(mssqlBatchBackupJobConfig, (error, data, response) => {
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
 **mssqlBatchBackupJobConfig** | [**MssqlBatchBackupJobConfig**](MssqlBatchBackupJobConfig.md)| Configuration for the on-demand backups. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOnDemandMssqlLogBackup

> AsyncRequestStatus createOnDemandMssqlLogBackup(id)

Take an on-demand log backup for a Microsoft SQL database

Take an on-demand log backup for a Microsoft SQL database.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
apiInstance.createOnDemandMssqlLogBackup(id, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createRestoreMssqlDb

> AsyncRequestStatus createRestoreMssqlDb(id, restoreMssqlDbJobConfig)

Restore a Microsoft SQL database

Create a request to restore a SQL Server database. To check the result of the request, poll /mssql/request/{id}.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let restoreMssqlDbJobConfig = new RubrikRestApi.RestoreMssqlDbJobConfig(); // RestoreMssqlDbJobConfig | Restore configuration.
apiInstance.createRestoreMssqlDb(id, restoreMssqlDbJobConfig, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **restoreMssqlDbJobConfig** | [**RestoreMssqlDbJobConfig**](RestoreMssqlDbJobConfig.md)| Restore configuration. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDownloadedMssqlDbRecoverableRangesV1

> JobScheduledResponse deleteDownloadedMssqlDbRecoverableRangesV1(id, opts)

Delete downloaded recoverable ranges of a Microsoft SQL database

Deletes all local snapshots and logs that have previously been downloaded. Provide a begin or end time to delete only the downloaded snapshots and logs that fall within this time frame. The time is relative to when the snapshot or log backup was originally taken, not downloaded. Parts of the window may not be deleted if certain log files must be kept to preserve times outside the window. Data is deleted in the background. To check the status of the deletion, poll /mssql/db/recoverable_range/download/{id}.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let opts = {
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Delete only the downloaded snapshots and logs taken after this time. The date-time string should be in ISO8601 format. For example, \"2016-01-01T01:23:45.678\".
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | Delete only the downloaded snapshots and logs taken before this time. The date-time string should be in ISO8601 format. For example, \"2016-01-01T01:23:45.678\".
};
apiInstance.deleteDownloadedMssqlDbRecoverableRangesV1(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **afterTime** | **Date**| Delete only the downloaded snapshots and logs taken after this time. The date-time string should be in ISO8601 format. For example, \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 
 **beforeTime** | **Date**| Delete only the downloaded snapshots and logs taken before this time. The date-time string should be in ISO8601 format. For example, \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 

### Return type

[**JobScheduledResponse**](JobScheduledResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteLogShippingConfiguration

> AsyncRequestStatus deleteLogShippingConfiguration(id, opts)

Delete a specified log shipping configuration

Deletes the specified log shipping configuration.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of a log shipping configuration object.
let opts = {
  'deleteSecondaryDatabase': true // Boolean | Boolean value that determines whether to attempt to delete the secondary database associated with the specified log shipping configuration. The default value is false. When set to false, no attempt is made to delete the secondary database. When set to true, starts an asynchronous job to delete the secondary database.
};
apiInstance.deleteLogShippingConfiguration(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of a log shipping configuration object. | 
 **deleteSecondaryDatabase** | **Boolean**| Boolean value that determines whether to attempt to delete the secondary database associated with the specified log shipping configuration. The default value is false. When set to false, no attempt is made to delete the secondary database. When set to true, starts an asynchronous job to delete the secondary database. | [optional] 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteMssqlDbSnapshots

> deleteMssqlDbSnapshots(id)

Delete all snapshots of a Microsoft SQL database

Deletes all snapshots of a Microsoft SQL database. The database must be unprotected for the operation to succeed.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
apiInstance.deleteMssqlDbSnapshots(id, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteMssqlHostConfig

> deleteMssqlHostConfig(hostId)

Delete the SQL Server host configuration

Deletes the SQL Server host configuration. The host falls back to use values from the global configuration.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let hostId = "hostId_example"; // String | ID of the host.
apiInstance.deleteMssqlHostConfig(hostId, (error, data, response) => {
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
 **hostId** | **String**| ID of the host. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## downloadFromArchive

> AsyncRequestStatus downloadFromArchive(id, mssqlDownloadFromArchiveConfig)

Download snapshots and log backups from archival

Starts an asynchronous request to download snapshots and logs from archival for a given database and recovery point. If the specified point in time is already available locally, this endpoint throws an error. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let mssqlDownloadFromArchiveConfig = new RubrikRestApi.MssqlDownloadFromArchiveConfig(); // MssqlDownloadFromArchiveConfig | Configuration for the archive download request.
apiInstance.downloadFromArchive(id, mssqlDownloadFromArchiveConfig, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **mssqlDownloadFromArchiveConfig** | [**MssqlDownloadFromArchiveConfig**](MssqlDownloadFromArchiveConfig.md)| Configuration for the archive download request. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCompatibleMssqlInstancesV1

> MssqlInstanceSummaryListResponse getCompatibleMssqlInstancesV1(id, recoveryType, opts)

Get compatible instances for the recovery of a Microsoft SQL database

Returns all compatible instances for export for the specified recovery time.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let recoveryType = "recoveryType_example"; // String | Recovery type.
let opts = {
  'recoveryTime': new Date("2013-10-20T19:20:30+01:00") // Date | Time, in ISO8601 format, to recover to. For example \"2016-01-01T01:23:45.678Z\". If this is not specified, the latest recoverable time is used.
};
apiInstance.getCompatibleMssqlInstancesV1(id, recoveryType, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **recoveryType** | **String**| Recovery type. | 
 **recoveryTime** | **Date**| Time, in ISO8601 format, to recover to. For example \&quot;2016-01-01T01:23:45.678Z\&quot;. If this is not specified, the latest recoverable time is used. | [optional] 

### Return type

[**MssqlInstanceSummaryListResponse**](MssqlInstanceSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDefaultDbPropertiesV1

> MssqlDbDefaults getDefaultDbPropertiesV1()

Returns the current default properties for Microsoft SQL databases

The default properties are Log Backup Frequency (in seconds), Log Retention Time (in hours) and CBT status. New databases added to the Rubrik cluster are provided the log backup frequency value and log backup retention value by default. New hosts added to the Rubrik cluster are provided the CBT status by default.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
apiInstance.getDefaultDbPropertiesV1((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**MssqlDbDefaults**](MssqlDbDefaults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeleteMssqlDbRecoverableRangesStatusV1

> InternalJobInstanceDetail getDeleteMssqlDbRecoverableRangesStatusV1(id)

Get the deletion status of downloaded recoverable ranges

Get the details of the progress made in deleting recoverable ranges. The recoverable ranges to delete are those specified by the DELETE request to /mssql/db/{id}/recoverable_range/download which yielded the response with the job id.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | Job ID of the deletion for which to check progress.
apiInstance.getDeleteMssqlDbRecoverableRangesStatusV1(id, (error, data, response) => {
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
 **id** | **String**| Job ID of the deletion for which to check progress. | 

### Return type

[**InternalJobInstanceDetail**](InternalJobInstanceDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLogShippingConfiguration

> MssqlLogShippingDetail getLogShippingConfiguration(id)

Get a log shipping configuration

Retrieves a particular log shipping configuration with all the details of the configuration.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of a log shipping configuration.
apiInstance.getLogShippingConfiguration(id, (error, data, response) => {
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
 **id** | **String**| ID of a log shipping configuration. | 

### Return type

[**MssqlLogShippingDetail**](MssqlLogShippingDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMissedMssqlDbSnapshots

> MissedSnapshotListResponse getMissedMssqlDbSnapshots(id, opts)

Get summary information for missed snapshots of a SQL database

Returns a list of summary information for the missed snapshots of a Microsoft SQL database, including the time of day and the locations where the snapshot was missed.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let opts = {
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter snapshots to those missed on or after this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | Filter snapshots to those missed on or before this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
};
apiInstance.getMissedMssqlDbSnapshots(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **afterTime** | **Date**| Filter snapshots to those missed on or after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 
 **beforeTime** | **Date**| Filter snapshots to those missed on or before this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 

### Return type

[**MissedSnapshotListResponse**](MissedSnapshotListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMssqlAsyncRequestStatus

> AsyncRequestStatus getMssqlAsyncRequestStatus(id)

Get details for an async request

Returns the task object for an async request related to SQL Server databases.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the async request.
apiInstance.getMssqlAsyncRequestStatus(id, (error, data, response) => {
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
 **id** | **String**| ID of the async request. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMssqlAvailabilityGroupV1

> MssqlAvailabilityGroupDetail getMssqlAvailabilityGroupV1(id)

Returns detailed information for a Microsoft SQL availability group

Returns a detailed view of a Microsoft SQL availability group.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL availability group to fetch.
apiInstance.getMssqlAvailabilityGroupV1(id, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL availability group to fetch. | 

### Return type

[**MssqlAvailabilityGroupDetail**](MssqlAvailabilityGroupDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMssqlDb

> MssqlDbDetail getMssqlDb(id)

Get detailed information for a Microsoft SQL database

Returns a detailed view of a Microsoft SQL database.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database to fetch.
apiInstance.getMssqlDb(id, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database to fetch. | 

### Return type

[**MssqlDbDetail**](MssqlDbDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMssqlDbMissedRecoverableRanges

> MssqlMissedRecoverableRangeListResponse getMssqlDbMissedRecoverableRanges(id, opts)

Get missed recoverable ranges of a Microsoft SQL database

Retrieve a list of missed recoverable ranges for a Microsoft SQL database. For each run of one type of error, the first and last occurrence of the error are given.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let opts = {
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter the missed ranges to end after this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | Filter the missed ranges to start before this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
};
apiInstance.getMssqlDbMissedRecoverableRanges(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **afterTime** | **Date**| Filter the missed ranges to end after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 
 **beforeTime** | **Date**| Filter the missed ranges to start before this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 

### Return type

[**MssqlMissedRecoverableRangeListResponse**](MssqlMissedRecoverableRangeListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMssqlDbRecoverableRanges

> MssqlRecoverableRangeListResponse getMssqlDbRecoverableRanges(id, opts)

Get recoverable ranges of a Microsoft SQL database

Retrieve the recoverable ranges for a specified Microsoft SQL database. A begin and/or end timestamp can be provided to retrieve only the ranges that fall within the window.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let opts = {
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678Z\".
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
};
apiInstance.getMssqlDbRecoverableRanges(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **afterTime** | **Date**| Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678Z\&quot;. | [optional] 
 **beforeTime** | **Date**| Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 

### Return type

[**MssqlRecoverableRangeListResponse**](MssqlRecoverableRangeListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMssqlDbSnapshot

> MssqlDbSnapshotDetail getMssqlDbSnapshot(id)

Get details information about a Microsoft SQL database snapshot

Returns detailed information about a Microsoft SQL database snapshot.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the snapshot.
apiInstance.getMssqlDbSnapshot(id, (error, data, response) => {
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
 **id** | **String**| ID of the snapshot. | 

### Return type

[**MssqlDbSnapshotDetail**](MssqlDbSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMssqlHierarchyChildren

> MssqlHierarchyObjectSummaryListResponse getMssqlHierarchyChildren(id, opts)

Get list of immediate descendant objects

Retrieve the list of immediate descendant objects for the specified parent.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the parent SQL Server hierarchy object. To get top-level nodes, use **root** as the ID. 
let opts = {
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filter by the ID of the effective SLA Domain.
  'objectType': ["null"], // [String] | Filter by a comma-separated list of node object types. 
  'primaryClusterId': "primaryClusterId_example", // String | Filter by primary cluster ID, or **local**.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | An integer that specifies the number of initial matches to ignore. 
  'name': "name_example", // String | Filter children by provided name.
  'isRelic': true, // Boolean | Filter by the value of the `isRelic` field for nodes with object type MssqlDatabase.
  'isLiveMount': true, // Boolean | Filter database by the value of the `isLiveMount` field for nodes with object type MssqlDatabase.
  'isLogShippingSecondary': true, // Boolean | Filter by the value of the `isLogShippingSecondary` field for nodes with object type MssqlDatabase.
  'isClustered': true, // Boolean | Filter by the value of the `isClustered` field for nodes with object type MssqlDatabase or MssqlInstance.
  'hasInstances': true, // Boolean | Boolean that filters top-level nodes with the Host or WindowsCluster object type by whether or not the nodes have children MssqlInstance nodes. When this value is 'true,' the filter shows only nodes with children MssqlInstance nodes. When this value is 'false,' the filter shows only nodes without children MssqlInstance nodes.
  'slaAssignment': "slaAssignment_example", // String | Filter by SLA assignment type.
  'sortBy': "sortBy_example", // String | Attribute to sort the results on.
  'sortOrder': "sortOrder_example", // String | Sort order, either ascending or descending.
  'snappableStatus': "snappableStatus_example" // String | Determines whether SQL Server instances are fetched with additional privilege checks.
};
apiInstance.getMssqlHierarchyChildren(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the parent SQL Server hierarchy object. To get top-level nodes, use **root** as the ID.  | 
 **effectiveSlaDomainId** | **String**| Filter by the ID of the effective SLA Domain. | [optional] 
 **objectType** | [**[String]**](String.md)| Filter by a comma-separated list of node object types.  | [optional] 
 **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] 
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| An integer that specifies the number of initial matches to ignore.  | [optional] 
 **name** | **String**| Filter children by provided name. | [optional] 
 **isRelic** | **Boolean**| Filter by the value of the &#x60;isRelic&#x60; field for nodes with object type MssqlDatabase. | [optional] 
 **isLiveMount** | **Boolean**| Filter database by the value of the &#x60;isLiveMount&#x60; field for nodes with object type MssqlDatabase. | [optional] 
 **isLogShippingSecondary** | **Boolean**| Filter by the value of the &#x60;isLogShippingSecondary&#x60; field for nodes with object type MssqlDatabase. | [optional] 
 **isClustered** | **Boolean**| Filter by the value of the &#x60;isClustered&#x60; field for nodes with object type MssqlDatabase or MssqlInstance. | [optional] 
 **hasInstances** | **Boolean**| Boolean that filters top-level nodes with the Host or WindowsCluster object type by whether or not the nodes have children MssqlInstance nodes. When this value is &#39;true,&#39; the filter shows only nodes with children MssqlInstance nodes. When this value is &#39;false,&#39; the filter shows only nodes without children MssqlInstance nodes. | [optional] 
 **slaAssignment** | **String**| Filter by SLA assignment type. | [optional] 
 **sortBy** | **String**| Attribute to sort the results on. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] 
 **snappableStatus** | **String**| Determines whether SQL Server instances are fetched with additional privilege checks. | [optional] 

### Return type

[**MssqlHierarchyObjectSummaryListResponse**](MssqlHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMssqlHierarchyDescendants

> MssqlHierarchyObjectSummaryListResponse getMssqlHierarchyDescendants(id, opts)

Get list of descendant objects

Retrieve the list of descendant objects for the specified parent.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the parent SQL server hierarchy object. To get top-level nodes, use **root** as the ID. 
let opts = {
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filter by the ID of the effective SLA Domain.
  'objectType': ["null"], // [String] | Filter by a comma-separated list of node object types. 
  'primaryClusterId': "primaryClusterId_example", // String | Filter by primary cluster ID, or **local**.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | An integer that specifies the number of initial matches to ignore. 
  'name': "name_example", // String | Filter descendants by provided name.
  'isRelic': true, // Boolean | Filter by the value of the `isRelic` field for nodes with MssqlDatabase as the value of the object type field.
  'isLiveMount': true, // Boolean | Filter database by the value of the `isLiveMount` field for nodes with MssqlDatabase as the value of the object type field.
  'isLogShippingSecondary': true, // Boolean | Filter by the value of the `isLogShippingSecondary` field for nodes with MssqlDatabase as the value of the object type field.
  'isClustered': true, // Boolean | Filter by the value of the `isClustered` field for nodes with object type MssqlDatabase or MssqlInstance.
  'hasInstances': true, // Boolean | Boolean that filters top-level nodes with the Host or WindowsCluster object type by whether or not the nodes have children MssqlInstance nodes. When this value is 'true,' the filter shows only nodes with children MssqlInstance nodes. When this value is 'false,' the filter shows only nodes without children MssqlInstance nodes.
  'slaAssignment': "slaAssignment_example", // String | Filter by SLA Domain assignment type.
  'sortBy': "sortBy_example", // String | Attribute to sort the results on.
  'sortOrder': "sortOrder_example", // String | Sort order, either ascending or descending.
  'snappableStatus': "snappableStatus_example" // String | Determines whether SQL Server instances are fetched with additional privilege checks.
};
apiInstance.getMssqlHierarchyDescendants(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the parent SQL server hierarchy object. To get top-level nodes, use **root** as the ID.  | 
 **effectiveSlaDomainId** | **String**| Filter by the ID of the effective SLA Domain. | [optional] 
 **objectType** | [**[String]**](String.md)| Filter by a comma-separated list of node object types.  | [optional] 
 **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] 
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| An integer that specifies the number of initial matches to ignore.  | [optional] 
 **name** | **String**| Filter descendants by provided name. | [optional] 
 **isRelic** | **Boolean**| Filter by the value of the &#x60;isRelic&#x60; field for nodes with MssqlDatabase as the value of the object type field. | [optional] 
 **isLiveMount** | **Boolean**| Filter database by the value of the &#x60;isLiveMount&#x60; field for nodes with MssqlDatabase as the value of the object type field. | [optional] 
 **isLogShippingSecondary** | **Boolean**| Filter by the value of the &#x60;isLogShippingSecondary&#x60; field for nodes with MssqlDatabase as the value of the object type field. | [optional] 
 **isClustered** | **Boolean**| Filter by the value of the &#x60;isClustered&#x60; field for nodes with object type MssqlDatabase or MssqlInstance. | [optional] 
 **hasInstances** | **Boolean**| Boolean that filters top-level nodes with the Host or WindowsCluster object type by whether or not the nodes have children MssqlInstance nodes. When this value is &#39;true,&#39; the filter shows only nodes with children MssqlInstance nodes. When this value is &#39;false,&#39; the filter shows only nodes without children MssqlInstance nodes. | [optional] 
 **slaAssignment** | **String**| Filter by SLA Domain assignment type. | [optional] 
 **sortBy** | **String**| Attribute to sort the results on. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] 
 **snappableStatus** | **String**| Determines whether SQL Server instances are fetched with additional privilege checks. | [optional] 

### Return type

[**MssqlHierarchyObjectSummaryListResponse**](MssqlHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMssqlHierarchyObject

> MssqlHierarchyObjectSummary getMssqlHierarchyObject(id)

Get summary of a SQL Server hierarchy object

Retrieve details for the specified object in the SQL Server hierarchy. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the SQL Server hierarchy object.
apiInstance.getMssqlHierarchyObject(id, (error, data, response) => {
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
 **id** | **String**| ID of the SQL Server hierarchy object. | 

### Return type

[**MssqlHierarchyObjectSummary**](MssqlHierarchyObjectSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMssqlHostConfig

> MssqlHostConfiguration getMssqlHostConfig(hostId)

Get the configuration for a specific host

Returns the configuration for the specified SQL Server host.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let hostId = "hostId_example"; // String | ID of the host.
apiInstance.getMssqlHostConfig(hostId, (error, data, response) => {
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
 **hostId** | **String**| ID of the host. | 

### Return type

[**MssqlHostConfiguration**](MssqlHostConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMssqlInstance

> MssqlInstanceDetail getMssqlInstance(id)

Get detailed information for a Microsoft SQL instance

Returns a detailed view of a Microsoft SQL instance.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL instance.
apiInstance.getMssqlInstance(id, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL instance. | 

### Return type

[**MssqlInstanceDetail**](MssqlInstanceDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMssqlMount

> MssqlMountDetail getMssqlMount(id)

Get detailed information for a Live Mount of a SQL Server database

Returns detailed information for the specified Live Mount of a SQL Server database.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Live Mount to fetch.
apiInstance.getMssqlMount(id, (error, data, response) => {
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
 **id** | **String**| ID of the Live Mount to fetch. | 

### Return type

[**MssqlMountDetail**](MssqlMountDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOnDemandMssqlBatchBackupResultV1

> MssqlBatchBackupSummary getOnDemandMssqlBatchBackupResultV1(id)

Returns details for an on-demand backup of multiple Microsoft SQL databases

Returns the details for an on-demand backup of multiple Microsoft SQL databases. This only returns details for requests that have finished successfully. To check the status of the request, poll /mssql/request/{id}.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the on-demand backup request.
apiInstance.getOnDemandMssqlBatchBackupResultV1(id, (error, data, response) => {
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
 **id** | **String**| ID of the on-demand backup request. | 

### Return type

[**MssqlBatchBackupSummary**](MssqlBatchBackupSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mssqlGetRestoreFilesV1

> [MssqlRestoreFile] mssqlGetRestoreFilesV1(id, opts)

Returns a list all database files to be restored

Provides a list of database files to be restored for the specified restore or export operation.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let opts = {
  'time': new Date("2013-10-20T19:20:30+01:00"), // Date | Time, in ISO8601 date-time format, to recover to. For example, \"2016-01-01T01:23:45.678\". This value or the LSN are required.
  'lsn': "lsn_example", // String | LSN to recover to. This value or the time are required.
  'recoveryForkGuid': "recoveryForkGuid_example" // String | Recovery fork GUID of LSN to recover to. Meaningful only when lsn is specified.
};
apiInstance.mssqlGetRestoreFilesV1(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **time** | **Date**| Time, in ISO8601 date-time format, to recover to. For example, \&quot;2016-01-01T01:23:45.678\&quot;. This value or the LSN are required. | [optional] 
 **lsn** | **String**| LSN to recover to. This value or the time are required. | [optional] 
 **recoveryForkGuid** | **String**| Recovery fork GUID of LSN to recover to. Meaningful only when lsn is specified. | [optional] 

### Return type

[**[MssqlRestoreFile]**](MssqlRestoreFile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mssqlGetSnappableIdV1

> MssqlSnappableId mssqlGetSnappableIdV1(id)

Returns the snappableId for a Microsoft SQL database

Returns the snappableId for a Microsoft SQL database.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
apiInstance.mssqlGetSnappableIdV1(id, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 

### Return type

[**MssqlSnappableId**](MssqlSnappableId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mssqlRestoreEstimateV1

> MssqlRestoreEstimateResult mssqlRestoreEstimateV1(id, opts)

Returns a size estimate for a restore or export

Provides an estimate of resources needed for the specified restore or export operation.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let opts = {
  'time': new Date("2013-10-20T19:20:30+01:00"), // Date | Time, in ISO8601 date-time format, to recover to. For example, \"2016-01-01T01:23:45.678\". This value or the LSN are required.
  'lsn': "lsn_example", // String | LSN to recover to. This value or the LSN are required.
  'recoveryForkGuid': "recoveryForkGuid_example" // String | Recovery fork GUID of LSN to recover to. Meaningful only when lsn is specified.
};
apiInstance.mssqlRestoreEstimateV1(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **time** | **Date**| Time, in ISO8601 date-time format, to recover to. For example, \&quot;2016-01-01T01:23:45.678\&quot;. This value or the LSN are required. | [optional] 
 **lsn** | **String**| LSN to recover to. This value or the LSN are required. | [optional] 
 **recoveryForkGuid** | **String**| Recovery fork GUID of LSN to recover to. Meaningful only when lsn is specified. | [optional] 

### Return type

[**MssqlRestoreEstimateResult**](MssqlRestoreEstimateResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryLogShippingConfigurations

> MssqlLogShippingSummaryListResponse queryLogShippingConfigurations(opts)

Get log shipping configurations

Retrieves all log shipping configuration objects. Results can be filtered and sorted.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let opts = {
  'primaryDatabaseId': "primaryDatabaseId_example", // String | ID of a primary database object.
  'primaryDatabaseName': "primaryDatabaseName_example", // String | Filter log shipping configuration objects by performing an infix search using the name of a primary database.
  'secondaryDatabaseName': "secondaryDatabaseName_example", // String | Filter log shipping configuration objects by performing an infix search using the name of a secondary database.
  'location': "location_example", // String | Filter log shipping configuration objects by performing an infix search using the location string value (host/instance) for a secondary database.
  'status': "status_example", // String | Filter log shipping configuration objects based on the status value for the secondary database.
  'limit': 56, // Number | Limit the summary information to a specified maximum number of results.
  'offset': 56, // Number | Starting position in the list of results contained in the response. The summary information includes the specified numbered result and all higher numbered results.
  'sortBy': "sortBy_example", // String | Specifies an attribute used to ASCII-sort the results. Sorting by the last_applied attribute represents the timestamp as an ISO 8601-encoded string.
  'sortOrder': "sortOrder_example" // String | Sort order, either ascending or descending.
};
apiInstance.queryLogShippingConfigurations(opts, (error, data, response) => {
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
 **primaryDatabaseId** | **String**| ID of a primary database object. | [optional] 
 **primaryDatabaseName** | **String**| Filter log shipping configuration objects by performing an infix search using the name of a primary database. | [optional] 
 **secondaryDatabaseName** | **String**| Filter log shipping configuration objects by performing an infix search using the name of a secondary database. | [optional] 
 **location** | **String**| Filter log shipping configuration objects by performing an infix search using the location string value (host/instance) for a secondary database. | [optional] 
 **status** | **String**| Filter log shipping configuration objects based on the status value for the secondary database. | [optional] 
 **limit** | **Number**| Limit the summary information to a specified maximum number of results. | [optional] 
 **offset** | **Number**| Starting position in the list of results contained in the response. The summary information includes the specified numbered result and all higher numbered results. | [optional] 
 **sortBy** | **String**| Specifies an attribute used to ASCII-sort the results. Sorting by the last_applied attribute represents the timestamp as an ISO 8601-encoded string. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] 

### Return type

[**MssqlLogShippingSummaryListResponse**](MssqlLogShippingSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryMssqlAvailabilityGroupV1

> MssqlAvailabilityGroupSummaryListResponse queryMssqlAvailabilityGroupV1(opts)

Returns summary information for Microsoft SQL availability groups

Returns a list of summary information for Microsoft SQL availability groups.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let opts = {
  'primaryClusterId': "primaryClusterId_example" // String | Filter by primary cluster.
};
apiInstance.queryMssqlAvailabilityGroupV1(opts, (error, data, response) => {
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
 **primaryClusterId** | **String**| Filter by primary cluster. | [optional] 

### Return type

[**MssqlAvailabilityGroupSummaryListResponse**](MssqlAvailabilityGroupSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryMssqlDb

> MssqlDbSummaryListResponse queryMssqlDb(opts)

Get summary information for SQL Server databases

Returns a list of summary information for Microsoft SQL databases.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let opts = {
  'instanceId': "instanceId_example", // String | Filter by Microsoft SQL instance.
  'availabilityGroupId': "availabilityGroupId_example", // String | Filter by the `id` of an Always On Availability Group.
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filter by effective SLA domain.
  'primaryClusterId': "primaryClusterId_example", // String | Filter by primary cluster.
  'name': "name_example", // String | Filter by a substring of the database name.
  'slaAssignment': "slaAssignment_example", // String | SLA Assignment of the database.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | An integer that specifies a number of initial matches to ignore.
  'isRelic': true, // Boolean | Filter database summary information by the value of the `isRelic` field.
  'isLiveMount': true, // Boolean | Filter database summary information by the value of the `isLiveMount` field.
  'isLogShippingSecondary': true, // Boolean | Filter database summary information by the value of the `isLogShippingSecondary` field.
  'sortBy': "sortBy_example", // String | Specifies the SQL Server Database attribute to use in sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order.
  'sortOrder': "sortOrder_example", // String | Sort order, either ascending or descending.
  'includeBackupTaskInfo': false // Boolean | Include backup task information in response.
};
apiInstance.queryMssqlDb(opts, (error, data, response) => {
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
 **instanceId** | **String**| Filter by Microsoft SQL instance. | [optional] 
 **availabilityGroupId** | **String**| Filter by the &#x60;id&#x60; of an Always On Availability Group. | [optional] 
 **effectiveSlaDomainId** | **String**| Filter by effective SLA domain. | [optional] 
 **primaryClusterId** | **String**| Filter by primary cluster. | [optional] 
 **name** | **String**| Filter by a substring of the database name. | [optional] 
 **slaAssignment** | **String**| SLA Assignment of the database. | [optional] 
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| An integer that specifies a number of initial matches to ignore. | [optional] 
 **isRelic** | **Boolean**| Filter database summary information by the value of the &#x60;isRelic&#x60; field. | [optional] 
 **isLiveMount** | **Boolean**| Filter database summary information by the value of the &#x60;isLiveMount&#x60; field. | [optional] 
 **isLogShippingSecondary** | **Boolean**| Filter database summary information by the value of the &#x60;isLogShippingSecondary&#x60; field. | [optional] 
 **sortBy** | **String**| Specifies the SQL Server Database attribute to use in sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] 
 **includeBackupTaskInfo** | **Boolean**| Include backup task information in response. | [optional] [default to false]

### Return type

[**MssqlDbSummaryListResponse**](MssqlDbSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryMssqlDbSnapshot

> MssqlDbSnapshotSummaryListResponse queryMssqlDbSnapshot(id, opts)

Get summary information for snapshots of a Microsoft SQL database

Returns a list of summary information for snapshots of a Microsoft SQL database.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database.
let opts = {
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter snapshots to those taken on or after this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | Filter snapshots to those taken before or on this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
};
apiInstance.queryMssqlDbSnapshot(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database. | 
 **afterTime** | **Date**| Filter snapshots to those taken on or after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 
 **beforeTime** | **Date**| Filter snapshots to those taken before or on this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 

### Return type

[**MssqlDbSnapshotSummaryListResponse**](MssqlDbSnapshotSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryMssqlHostConfig

> MssqlHostConfigurationWithHostIdListResponse queryMssqlHostConfig(opts)

Get the summary of SQL Server host configurations

Returns a list of customized SQL Server host configurations.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let opts = {
  'hostId': ["null"] // [String] | IDs of the hosts.
};
apiInstance.queryMssqlHostConfig(opts, (error, data, response) => {
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
 **hostId** | [**[String]**](String.md)| IDs of the hosts. | [optional] 

### Return type

[**MssqlHostConfigurationWithHostIdListResponse**](MssqlHostConfigurationWithHostIdListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryMssqlInstance

> MssqlInstanceSummaryListResponse queryMssqlInstance(opts)

Get summary information for Microsoft SQL instances

Returns a list of summary information for Microsoft SQL instances.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let opts = {
  'rootId': "rootId_example", // String | Include only instances that belong to this root.
  'primaryClusterId': "primaryClusterId_example", // String | Limits the instances returned within one cluster specified by primary_cluster_id.
  'snappableStatus': "snappableStatus_example" // String | Determines whether SQL Server instances are fetched with additional privilege checks.
};
apiInstance.queryMssqlInstance(opts, (error, data, response) => {
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
 **rootId** | **String**| Include only instances that belong to this root. | [optional] 
 **primaryClusterId** | **String**| Limits the instances returned within one cluster specified by primary_cluster_id. | [optional] 
 **snappableStatus** | **String**| Determines whether SQL Server instances are fetched with additional privilege checks. | [optional] 

### Return type

[**MssqlInstanceSummaryListResponse**](MssqlInstanceSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryMssqlMount

> MssqlMountSummaryListResponse queryMssqlMount(opts)

Get summary information for all Live Mounts SQL Server databases

Returns a list with summary information for all Live Mount SQL Server databases.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let opts = {
  'sourceDatabaseId': "sourceDatabaseId_example", // String | Filters by the ID of the source SQL Server database.
  'sourceDatabaseName': "sourceDatabaseName_example", // String | Filters by the name of the source SQL Server database using infix search.
  'targetInstanceId': "targetInstanceId_example", // String | Filters by the ID of the target SQL Server instance.
  'mountedDatabaseName': "mountedDatabaseName_example", // String | Filters by the name of the mounted SQL Server database using infix search.
  'sortBy': "sortBy_example", // String | Specifies the SQL Server Live Mount attribute to use in sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order.
  'sortOrder': "sortOrder_example", // String | Specifies the sort order, either ascending or descending. Default order is ascending.
  'offset': 56, // Number | Returns the portion of the ordered list that starts after the element specified by the offset number.
  'limit': 56 // Number | Sets the maximum number of a elements to include in the data array of the response.
};
apiInstance.queryMssqlMount(opts, (error, data, response) => {
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
 **sourceDatabaseId** | **String**| Filters by the ID of the source SQL Server database. | [optional] 
 **sourceDatabaseName** | **String**| Filters by the name of the source SQL Server database using infix search. | [optional] 
 **targetInstanceId** | **String**| Filters by the ID of the target SQL Server instance. | [optional] 
 **mountedDatabaseName** | **String**| Filters by the name of the mounted SQL Server database using infix search. | [optional] 
 **sortBy** | **String**| Specifies the SQL Server Live Mount attribute to use in sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order. | [optional] 
 **sortOrder** | **String**| Specifies the sort order, either ascending or descending. Default order is ascending. | [optional] 
 **offset** | **Number**| Returns the portion of the ordered list that starts after the element specified by the offset number. | [optional] 
 **limit** | **Number**| Sets the maximum number of a elements to include in the data array of the response. | [optional] 

### Return type

[**MssqlMountSummaryListResponse**](MssqlMountSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reseedSecondary

> AsyncRequestStatus reseedSecondary(id, mssqlLogShippingReseedConfig)

Reseed a secondary database

Starts an asynchronous job to reseed a secondary database. Reseeding restores the data in the secondary database based on a log shipping configuration.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the log shipping configuration object for the specified secondary database.
let mssqlLogShippingReseedConfig = new RubrikRestApi.MssqlLogShippingReseedConfig(); // MssqlLogShippingReseedConfig | Configuration parameters for the reseed operation.
apiInstance.reseedSecondary(id, mssqlLogShippingReseedConfig, (error, data, response) => {
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
 **id** | **String**| ID of the log shipping configuration object for the specified secondary database. | 
 **mssqlLogShippingReseedConfig** | [**MssqlLogShippingReseedConfig**](MssqlLogShippingReseedConfig.md)| Configuration parameters for the reseed operation. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDefaultDbPropertiesV1

> MssqlDbDefaults updateDefaultDbPropertiesV1(mssqlDbDefaultsUpdate)

Update the default properties for Microsoft SQL databases

The default properties are Log Backup Frequency (in seconds), Log Retention Time (in hours) and CBT status. New databases added to the Rubrik cluster are provided the log backup frequency value and log backup retention value by default. New hosts added to the Rubrik cluster are provided the CBT status by default.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let mssqlDbDefaultsUpdate = new RubrikRestApi.MssqlDbDefaultsUpdate(); // MssqlDbDefaultsUpdate | Updated default properties.
apiInstance.updateDefaultDbPropertiesV1(mssqlDbDefaultsUpdate, (error, data, response) => {
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
 **mssqlDbDefaultsUpdate** | [**MssqlDbDefaultsUpdate**](MssqlDbDefaultsUpdate.md)| Updated default properties. | 

### Return type

[**MssqlDbDefaults**](MssqlDbDefaults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateLogShippingConfiguration

> AsyncRequestStatus updateLogShippingConfiguration(id, mssqlLogShippingUpdate)

Update a specified log shipping configuration

Updates a specified log shipping configuration.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of a log shipping configuration object.
let mssqlLogShippingUpdate = new RubrikRestApi.MssqlLogShippingUpdate(); // MssqlLogShippingUpdate | Configuration parameters for the update operation.
apiInstance.updateLogShippingConfiguration(id, mssqlLogShippingUpdate, (error, data, response) => {
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
 **id** | **String**| ID of a log shipping configuration object. | 
 **mssqlLogShippingUpdate** | [**MssqlLogShippingUpdate**](MssqlLogShippingUpdate.md)| Configuration parameters for the update operation. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMssqlAvailabilityGroupV1

> MssqlAvailabilityGroupDetail updateMssqlAvailabilityGroupV1(id, mssqlAvailabilityGroupUpdate)

Update a Microsoft SQL availability group

Update a Microsoft SQL availability group with the specified properties.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL availability group to update.
let mssqlAvailabilityGroupUpdate = new RubrikRestApi.MssqlAvailabilityGroupUpdate(); // MssqlAvailabilityGroupUpdate | Properties to update.
apiInstance.updateMssqlAvailabilityGroupV1(id, mssqlAvailabilityGroupUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL availability group to update. | 
 **mssqlAvailabilityGroupUpdate** | [**MssqlAvailabilityGroupUpdate**](MssqlAvailabilityGroupUpdate.md)| Properties to update. | 

### Return type

[**MssqlAvailabilityGroupDetail**](MssqlAvailabilityGroupDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMssqlDb

> MssqlDbDetail updateMssqlDb(id, mssqlDbUpdate)

Update a Microsoft SQL database

Update a Microsoft SQL database with the specified properties.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL database to update.
let mssqlDbUpdate = new RubrikRestApi.MssqlDbUpdate(); // MssqlDbUpdate | Properties to update.
apiInstance.updateMssqlDb(id, mssqlDbUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL database to update. | 
 **mssqlDbUpdate** | [**MssqlDbUpdate**](MssqlDbUpdate.md)| Properties to update. | 

### Return type

[**MssqlDbDetail**](MssqlDbDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMssqlHostConfig

> MssqlHostConfiguration updateMssqlHostConfig(hostId, mssqlHostConfiguration)

Update host configuration

Updates the configuration for a specified host.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let hostId = "hostId_example"; // String | ID of the SQL Server host to update the host configuration.
let mssqlHostConfiguration = new RubrikRestApi.MssqlHostConfiguration(); // MssqlHostConfiguration | SQL Server host configuration properties to update.
apiInstance.updateMssqlHostConfig(hostId, mssqlHostConfiguration, (error, data, response) => {
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
 **hostId** | **String**| ID of the SQL Server host to update the host configuration. | 
 **mssqlHostConfiguration** | [**MssqlHostConfiguration**](MssqlHostConfiguration.md)| SQL Server host configuration properties to update. | 

### Return type

[**MssqlHostConfiguration**](MssqlHostConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMssqlInstance

> MssqlInstanceDetail updateMssqlInstance(id, mssqlInstanceUpdate)

Update a Microsoft SQL instance

Update a Microsoft SQL instance with specified properties.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MssqlApi();
let id = "id_example"; // String | ID of the Microsoft SQL instance.
let mssqlInstanceUpdate = new RubrikRestApi.MssqlInstanceUpdate(); // MssqlInstanceUpdate | Properties to update.
apiInstance.updateMssqlInstance(id, mssqlInstanceUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the Microsoft SQL instance. | 
 **mssqlInstanceUpdate** | [**MssqlInstanceUpdate**](MssqlInstanceUpdate.md)| Properties to update. | 

### Return type

[**MssqlInstanceDetail**](MssqlInstanceDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

