# RubrikRestApi.SapHanaApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addSapHanaSystem**](SapHanaApi.md#addSapHanaSystem) | **POST** /sap_hana/system | Add a SAP HANA system
[**configureSapHanaRestore**](SapHanaApi.md#configureSapHanaRestore) | **POST** /sap_hana/db/{id}/configure_restore | Configure the target database for system copy restore
[**createOnDemandSapHanaBackup**](SapHanaApi.md#createOnDemandSapHanaBackup) | **POST** /sap_hana/db/{id}/snapshot | Create on demand database snapshot
[**createSapHanaSystemRefresh**](SapHanaApi.md#createSapHanaSystemRefresh) | **POST** /sap_hana/system/{id}/refresh | Refresh SAP HANA system metadata
[**deleteSapHanaDbSnapshot**](SapHanaApi.md#deleteSapHanaDbSnapshot) | **DELETE** /sap_hana/db/snapshot/{id} | Delete a particular full snapshot of a SAP HANA database
[**deleteSapHanaSystem**](SapHanaApi.md#deleteSapHanaSystem) | **DELETE** /sap_hana/system/{id} | Delete a SAP HANA system
[**getMissedSapHanaDbSnapshots**](SapHanaApi.md#getMissedSapHanaDbSnapshots) | **GET** /sap_hana/db/{id}/missed_snapshot | Retrieve summary information for missed snapshots of a SAP HANA database
[**getSapHanaDatabase**](SapHanaApi.md#getSapHanaDatabase) | **GET** /sap_hana/db/{id} | Get detailed information for an SAP HANA database
[**getSapHanaDbAsyncRequestStatus**](SapHanaApi.md#getSapHanaDbAsyncRequestStatus) | **GET** /sap_hana/db/request/{id} | Get the status of a SAP HANA database request
[**getSapHanaDbRecoverableRanges**](SapHanaApi.md#getSapHanaDbRecoverableRanges) | **GET** /sap_hana/db/{id}/recoverable_range | Get recoverable ranges of a SAP HANA database
[**getSapHanaDbSnapshot**](SapHanaApi.md#getSapHanaDbSnapshot) | **GET** /sap_hana/db/snapshot/{id} | Get SAP HANA database snapshot details
[**getSapHanaSystem**](SapHanaApi.md#getSapHanaSystem) | **GET** /sap_hana/system/{id} | Get summary information for a SAP HANA system
[**getSapHanaSystemAsyncRequestStatus**](SapHanaApi.md#getSapHanaSystemAsyncRequestStatus) | **GET** /sap_hana/system/request/{id} | Get the status of a SAP HANA system request
[**patchSapHanaDatabase**](SapHanaApi.md#patchSapHanaDatabase) | **PATCH** /sap_hana/db/{id} | Update the SLA Domain for an SAP HANA database
[**patchSapHanaSystem**](SapHanaApi.md#patchSapHanaSystem) | **PATCH** /sap_hana/system/{id} | Update the SLA Domain for a SAP HANA system
[**querySapHanaDatabases**](SapHanaApi.md#querySapHanaDatabases) | **GET** /sap_hana/db | Get summary information for discovered SAP HANA databases
[**querySapHanaDbSnapshot**](SapHanaApi.md#querySapHanaDbSnapshot) | **GET** /sap_hana/db/{id}/snapshot | Get a summary list of snapshots for a SAP HANA database
[**querySapHanaSystems**](SapHanaApi.md#querySapHanaSystems) | **GET** /sap_hana/system | Get summary information for added SAP HANA systems
[**unconfigureSapHanaRestore**](SapHanaApi.md#unconfigureSapHanaRestore) | **POST** /sap_hana/db/{id}/unconfigure_restore | Reset the configuration for system copy restore on target database



## addSapHanaSystem

> SapHanaAddSystemResponse addSapHanaSystem(sapHanaSystemConfig)

Add a SAP HANA system

Add a SAP HANA system to the Rubrik cluster.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let sapHanaSystemConfig = new RubrikRestApi.SapHanaSystemConfig(); // SapHanaSystemConfig | Add a SAP HANA system to the Rubrik cluster. Contains parameters like username, list of hosts, password required while adding a SAP HANA system.
apiInstance.addSapHanaSystem(sapHanaSystemConfig, (error, data, response) => {
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
 **sapHanaSystemConfig** | [**SapHanaSystemConfig**](SapHanaSystemConfig.md)| Add a SAP HANA system to the Rubrik cluster. Contains parameters like username, list of hosts, password required while adding a SAP HANA system. | 

### Return type

[**SapHanaAddSystemResponse**](SapHanaAddSystemResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## configureSapHanaRestore

> AsyncRequestStatus configureSapHanaRestore(id, sapHanaRestoreSourceConfig)

Configure the target database for system copy restore

Initiates a job to configure the specified target database for a system copy restore by sending metadata about the source database. System copy restore in SAP HANA is done across different databases.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | ID of the target SAP HANA database to be configured.
let sapHanaRestoreSourceConfig = new RubrikRestApi.SapHanaRestoreSourceConfig(); // SapHanaRestoreSourceConfig | The object containing configuration related metadata for the source SAP HANA database.
apiInstance.configureSapHanaRestore(id, sapHanaRestoreSourceConfig, (error, data, response) => {
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
 **id** | **String**| ID of the target SAP HANA database to be configured. | 
 **sapHanaRestoreSourceConfig** | [**SapHanaRestoreSourceConfig**](SapHanaRestoreSourceConfig.md)| The object containing configuration related metadata for the source SAP HANA database. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOnDemandSapHanaBackup

> AsyncRequestStatus createOnDemandSapHanaBackup(id, opts)

Create on demand database snapshot

Initiates a job to take an on demand full snapshot of a specified SAP HANA database object. The GET /sap_hana/db/request/{id} endpoint can be used to monitor the progress of the job.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | ID assigned to a SAP HANA database object.
let opts = {
  'baseOnDemandSnapshotConfig': new RubrikRestApi.BaseOnDemandSnapshotConfig() // BaseOnDemandSnapshotConfig | Configuration for the on demand backup.
};
apiInstance.createOnDemandSapHanaBackup(id, opts, (error, data, response) => {
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
 **id** | **String**| ID assigned to a SAP HANA database object. | 
 **baseOnDemandSnapshotConfig** | [**BaseOnDemandSnapshotConfig**](BaseOnDemandSnapshotConfig.md)| Configuration for the on demand backup. | [optional] 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSapHanaSystemRefresh

> AsyncRequestStatus createSapHanaSystemRefresh(id)

Refresh SAP HANA system metadata

Initiates a job to refresh metadata of a SAP HANA system object. The GET /sap_hana/system/request/{id} endpoint can be used to monitor the progress of the job.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | The ID of the SAP HANA system.
apiInstance.createSapHanaSystemRefresh(id, (error, data, response) => {
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
 **id** | **String**| The ID of the SAP HANA system. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSapHanaDbSnapshot

> deleteSapHanaDbSnapshot(id)

Delete a particular full snapshot of a SAP HANA database

Initiates a request to delete a particular full snapshot of a SAP HANA database. If the log retention period for the database is still in effect, the snapshot will be deleted when the log retention period ends.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | ID assigned to a SAP HANA database full snapshot.
apiInstance.deleteSapHanaDbSnapshot(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to a SAP HANA database full snapshot. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSapHanaSystem

> AsyncRequestStatus deleteSapHanaSystem(id)

Delete a SAP HANA system

Initiates a job to delete a SAP HANA system object. GET /sap_hana/system/request/{id} endpoint can be used to monitor the progress of the job.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | The ID of the SAP HANA system.
apiInstance.deleteSapHanaSystem(id, (error, data, response) => {
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
 **id** | **String**| The ID of the SAP HANA system. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMissedSapHanaDbSnapshots

> MissedSnapshotListResponse getMissedSapHanaDbSnapshots(id, opts)

Retrieve summary information for missed snapshots of a SAP HANA database

Returns a summary of information for the missed snapshots of a SAP HANA database. Retrieve only the missed snapshots that occur between the beginning and ending timestamps.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | ID of the SAP HANA database.
let opts = {
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter for snapshots that are missed on or after this time. The date-time string must be in ISO8601 format, for example, \"2016-01-01T01:23:45.678\".
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | Filter for snapshots that are missed on or before this time. The date-time string must be in ISO8601 format, for example, \"2016-01-01T01:23:45.678\".
};
apiInstance.getMissedSapHanaDbSnapshots(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the SAP HANA database. | 
 **afterTime** | **Date**| Filter for snapshots that are missed on or after this time. The date-time string must be in ISO8601 format, for example, \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 
 **beforeTime** | **Date**| Filter for snapshots that are missed on or before this time. The date-time string must be in ISO8601 format, for example, \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 

### Return type

[**MissedSnapshotListResponse**](MissedSnapshotListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSapHanaDatabase

> SapHanaDatabaseDetail getSapHanaDatabase(id)

Get detailed information for an SAP HANA database

Returns a detailed view of the SAP HANA database.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | The ID of the SAP HANA database.
apiInstance.getSapHanaDatabase(id, (error, data, response) => {
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
 **id** | **String**| The ID of the SAP HANA database. | 

### Return type

[**SapHanaDatabaseDetail**](SapHanaDatabaseDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSapHanaDbAsyncRequestStatus

> AsyncRequestStatus getSapHanaDbAsyncRequestStatus(id)

Get the status of a SAP HANA database request

Get details about a SAP HANA database related request which includes the status of data backup job.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | ID of the request.
apiInstance.getSapHanaDbAsyncRequestStatus(id, (error, data, response) => {
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
 **id** | **String**| ID of the request. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSapHanaDbRecoverableRanges

> SapHanaRecoverableRangeListResponse getSapHanaDbRecoverableRanges(id, opts)

Get recoverable ranges of a SAP HANA database

Retrieve the recoverable ranges for a specified SAP HANA database. Provide a beginning and/or ending timestamp to retrieve only the recoverable ranges that fall within this period of time.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | ID of the SAP HANA database.
let opts = {
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter ranges to end after this time. The date-time string should be in an ISO8601 format. For example, \"2016-01-01T01:23:45.678Z\".
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | Filter ranges to start before this time. The date-time string should be in an ISO8601 format. For example, \"2016-01-01T01:23:45.678Z\".
};
apiInstance.getSapHanaDbRecoverableRanges(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the SAP HANA database. | 
 **afterTime** | **Date**| Filter ranges to end after this time. The date-time string should be in an ISO8601 format. For example, \&quot;2016-01-01T01:23:45.678Z\&quot;. | [optional] 
 **beforeTime** | **Date**| Filter ranges to start before this time. The date-time string should be in an ISO8601 format. For example, \&quot;2016-01-01T01:23:45.678Z\&quot;. | [optional] 

### Return type

[**SapHanaRecoverableRangeListResponse**](SapHanaRecoverableRangeListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSapHanaDbSnapshot

> SapHanaDatabaseSnapshotDetail getSapHanaDbSnapshot(id)

Get SAP HANA database snapshot details

Retrieve detailed information about a full or an incremental snapshot of a SAP HANA database.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | ID of snapshot.
apiInstance.getSapHanaDbSnapshot(id, (error, data, response) => {
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
 **id** | **String**| ID of snapshot. | 

### Return type

[**SapHanaDatabaseSnapshotDetail**](SapHanaDatabaseSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSapHanaSystem

> SapHanaSystemSummary getSapHanaSystem(id)

Get summary information for a SAP HANA system

Returns a summary view of a SAP HANA system.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | The ID of the SAP HANA system.
apiInstance.getSapHanaSystem(id, (error, data, response) => {
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
 **id** | **String**| The ID of the SAP HANA system. | 

### Return type

[**SapHanaSystemSummary**](SapHanaSystemSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSapHanaSystemAsyncRequestStatus

> AsyncRequestStatus getSapHanaSystemAsyncRequestStatus(id)

Get the status of a SAP HANA system request

Get details about a SAP HANA system related request which includes the status of delete or refresh system job.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | The ID of the request object used to poll the status.
apiInstance.getSapHanaSystemAsyncRequestStatus(id, (error, data, response) => {
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
 **id** | **String**| The ID of the request object used to poll the status. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchSapHanaDatabase

> SapHanaDatabaseDetail patchSapHanaDatabase(id, sapHanaDatabasePatch)

Update the SLA Domain for an SAP HANA database

Update the SLA Domain that is configured for an SAP HANA database.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | The ID of the SAP HANA database.
let sapHanaDatabasePatch = new RubrikRestApi.SapHanaDatabasePatch(); // SapHanaDatabasePatch | Object containing updated SAP HANA database SLA Domain ID.
apiInstance.patchSapHanaDatabase(id, sapHanaDatabasePatch, (error, data, response) => {
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
 **id** | **String**| The ID of the SAP HANA database. | 
 **sapHanaDatabasePatch** | [**SapHanaDatabasePatch**](SapHanaDatabasePatch.md)| Object containing updated SAP HANA database SLA Domain ID. | 

### Return type

[**SapHanaDatabaseDetail**](SapHanaDatabaseDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchSapHanaSystem

> SapHanaPatchSystemResponse patchSapHanaSystem(id, sapHanaSystemPatch)

Update the SLA Domain for a SAP HANA system

Update the SLA Domain that is configured for a SAP HANA system.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | The ID of the SAP HANA system.
let sapHanaSystemPatch = new RubrikRestApi.SapHanaSystemPatch(); // SapHanaSystemPatch | An object that contains the updated SLA Domain ID for the SAP HANA system.
apiInstance.patchSapHanaSystem(id, sapHanaSystemPatch, (error, data, response) => {
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
 **id** | **String**| The ID of the SAP HANA system. | 
 **sapHanaSystemPatch** | [**SapHanaSystemPatch**](SapHanaSystemPatch.md)| An object that contains the updated SLA Domain ID for the SAP HANA system. | 

### Return type

[**SapHanaPatchSystemResponse**](SapHanaPatchSystemResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## querySapHanaDatabases

> SapHanaDatabaseSummaryListResponse querySapHanaDatabases(opts)

Get summary information for discovered SAP HANA databases

Returns summary information for SAP HANA databases connected to the CDM cluster.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let opts = {
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | The ID of the SLA Domain that controls the protection of the host.
  'primaryClusterId': "primaryClusterId_example", // String | The ID of the Rubrik cluster that provides primary protection for the SAP HANA databases.
  'name': "name_example", // String | The name of the SAP HANA database.
  'slaAssignment': "slaAssignment_example", // String | The name of the SLA Domain that controls the protection of the SAP HANA database.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | An integer that specifies a number of initial matches to ignore.
  'isRelic': true, // Boolean | Specify whether the SAP HANA database is accessible on the Rubrik cluster.
  'sortBy': "sortBy_example", // String | Specifies the SAP HANA Database attribute to use in sorting the summary information.
  'sortOrder': "sortOrder_example" // String | The order to sort the responses by. Valid choices are asc (ascending) and desc (descending).
};
apiInstance.querySapHanaDatabases(opts, (error, data, response) => {
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
 **effectiveSlaDomainId** | **String**| The ID of the SLA Domain that controls the protection of the host. | [optional] 
 **primaryClusterId** | **String**| The ID of the Rubrik cluster that provides primary protection for the SAP HANA databases. | [optional] 
 **name** | **String**| The name of the SAP HANA database. | [optional] 
 **slaAssignment** | **String**| The name of the SLA Domain that controls the protection of the SAP HANA database. | [optional] 
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| An integer that specifies a number of initial matches to ignore. | [optional] 
 **isRelic** | **Boolean**| Specify whether the SAP HANA database is accessible on the Rubrik cluster. | [optional] 
 **sortBy** | **String**| Specifies the SAP HANA Database attribute to use in sorting the summary information. | [optional] 
 **sortOrder** | **String**| The order to sort the responses by. Valid choices are asc (ascending) and desc (descending). | [optional] 

### Return type

[**SapHanaDatabaseSummaryListResponse**](SapHanaDatabaseSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## querySapHanaDbSnapshot

> SapHanaDatabaseSnapshotSummaryListResponse querySapHanaDbSnapshot(id, opts)

Get a summary list of snapshots for a SAP HANA database

Retrieve summary information about the full and incremental snapshots of a specified SAP HANA database.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | ID assigned to a SAP HANA database object.
let opts = {
  'backupType': "backupType_example", // String | Filter snapshots to those of a particular backup type.
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter snapshots to those taken on or after this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | Filter snapshots to those taken before or on this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
};
apiInstance.querySapHanaDbSnapshot(id, opts, (error, data, response) => {
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
 **id** | **String**| ID assigned to a SAP HANA database object. | 
 **backupType** | **String**| Filter snapshots to those of a particular backup type. | [optional] 
 **afterTime** | **Date**| Filter snapshots to those taken on or after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 
 **beforeTime** | **Date**| Filter snapshots to those taken before or on this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 

### Return type

[**SapHanaDatabaseSnapshotSummaryListResponse**](SapHanaDatabaseSnapshotSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## querySapHanaSystems

> SapHanaSystemSummaryListResponse querySapHanaSystems(opts)

Get summary information for added SAP HANA systems

Returns summary information for SAP HANA systems.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let opts = {
  'primaryClusterId': "primaryClusterId_example", // String | The ID of the Rubrik cluster that provides primary protection for the SAP HANA databases.
  'sid': "sid_example", // String | The SAP System Identification (SID) code for the SAP HANA system.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | An integer that specifies a number of initial matches to ignore.
  'sortBy': "sortBy_example", // String | The SAP HANA system attribute to use in sorting the responses.
  'sortOrder': "sortOrder_example" // String | The order to sort the responses by. Valid choices are asc (ascending) and desc (descending).
};
apiInstance.querySapHanaSystems(opts, (error, data, response) => {
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
 **primaryClusterId** | **String**| The ID of the Rubrik cluster that provides primary protection for the SAP HANA databases. | [optional] 
 **sid** | **String**| The SAP System Identification (SID) code for the SAP HANA system. | [optional] 
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| An integer that specifies a number of initial matches to ignore. | [optional] 
 **sortBy** | **String**| The SAP HANA system attribute to use in sorting the responses. | [optional] 
 **sortOrder** | **String**| The order to sort the responses by. Valid choices are asc (ascending) and desc (descending). | [optional] 

### Return type

[**SapHanaSystemSummaryListResponse**](SapHanaSystemSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unconfigureSapHanaRestore

> AsyncRequestStatus unconfigureSapHanaRestore(id)

Reset the configuration for system copy restore on target database

Initiates a job to reset the configuration for the system copy restore on the specified target database. System copy restore in SAP HANA is done across different databases.

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

let apiInstance = new RubrikRestApi.SapHanaApi();
let id = "id_example"; // String | ID assigned to target SAP HANA database object.
apiInstance.unconfigureSapHanaRestore(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to target SAP HANA database object. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

