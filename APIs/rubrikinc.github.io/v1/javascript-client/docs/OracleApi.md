# RubrikRestApi.OracleApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkUpdateOracleDb**](OracleApi.md#bulkUpdateOracleDb) | **PATCH** /oracle/db/bulk | Update Oracle Databases
[**bulkUpdateOracleHost**](OracleApi.md#bulkUpdateOracleHost) | **PATCH** /oracle/host/bulk | Update Oracle Hosts
[**bulkUpdateOracleRac**](OracleApi.md#bulkUpdateOracleRac) | **PATCH** /oracle/rac/bulk | Update Oracle RACs
[**createOracleValidateBackupJob**](OracleApi.md#createOracleValidateBackupJob) | **POST** /oracle/db/{id}/validate | Validate Oracle database backups
[**deleteDownloadedSnapshots**](OracleApi.md#deleteDownloadedSnapshots) | **DELETE** /oracle/db/{id}/downloaded_snapshots | Delete downloaded Oracle database snapshots and log snapshots
[**getAcoParameterList**](OracleApi.md#getAcoParameterList) | **GET** /oracle/aco_parameter_list | List of supported Advanced Cloning Options
[**getExampleAcoDownloadLink**](OracleApi.md#getExampleAcoDownloadLink) | **GET** /oracle/aco_example_download_link | Link to download the Advanced Recovery Options example file
[**getOracleDbV1**](OracleApi.md#getOracleDbV1) | **GET** /oracle/db/{id} | Get Oracle database information
[**oracleRestoreEstimate**](OracleApi.md#oracleRestoreEstimate) | **GET** /oracle/db/{id}/restore_estimate | Get a size estimate for a restore or export
[**queryOracleDbV1**](OracleApi.md#queryOracleDbV1) | **GET** /oracle/db | Get summary information for Oracle databases
[**updateOracleDataGuardGroup**](OracleApi.md#updateOracleDataGuardGroup) | **PATCH** /oracle/data_guard_group/{id} | Update an Oracle Data Guard group
[**updateOracleDbV1**](OracleApi.md#updateOracleDbV1) | **PATCH** /oracle/db/{id} | Update an Oracle database
[**validateOracleAcoFile**](OracleApi.md#validateOracleAcoFile) | **POST** /oracle/validate_aco_file | Validate Oracle ACO file



## bulkUpdateOracleDb

> BulkOracleDbDetails bulkUpdateOracleDb(oracleBulkUpdate)

Update Oracle Databases

Update the properties of the objects that represent the specified Oracle Databases.

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

let apiInstance = new RubrikRestApi.OracleApi();
let oracleBulkUpdate = new RubrikRestApi.OracleBulkUpdate(); // OracleBulkUpdate | Properties to use for the update of Oracle Database objects.
apiInstance.bulkUpdateOracleDb(oracleBulkUpdate, (error, data, response) => {
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
 **oracleBulkUpdate** | [**OracleBulkUpdate**](OracleBulkUpdate.md)| Properties to use for the update of Oracle Database objects. | 

### Return type

[**BulkOracleDbDetails**](BulkOracleDbDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bulkUpdateOracleHost

> BulkOracleHostDetails bulkUpdateOracleHost(oracleBulkUpdate)

Update Oracle Hosts

Update properties to Oracle Host objects.

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

let apiInstance = new RubrikRestApi.OracleApi();
let oracleBulkUpdate = new RubrikRestApi.OracleBulkUpdate(); // OracleBulkUpdate | Properties to use for the update of Oracle Host objects.
apiInstance.bulkUpdateOracleHost(oracleBulkUpdate, (error, data, response) => {
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
 **oracleBulkUpdate** | [**OracleBulkUpdate**](OracleBulkUpdate.md)| Properties to use for the update of Oracle Host objects. | 

### Return type

[**BulkOracleHostDetails**](BulkOracleHostDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bulkUpdateOracleRac

> BulkOracleRacDetails bulkUpdateOracleRac(oracleBulkUpdate)

Update Oracle RACs

Update the properties of the objects that represent the specified Oracle RAC.

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

let apiInstance = new RubrikRestApi.OracleApi();
let oracleBulkUpdate = new RubrikRestApi.OracleBulkUpdate(); // OracleBulkUpdate | Properties to use for the update of Oracle RAC objects.
apiInstance.bulkUpdateOracleRac(oracleBulkUpdate, (error, data, response) => {
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
 **oracleBulkUpdate** | [**OracleBulkUpdate**](OracleBulkUpdate.md)| Properties to use for the update of Oracle RAC objects. | 

### Return type

[**BulkOracleRacDetails**](BulkOracleRacDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOracleValidateBackupJob

> AsyncRequestStatus createOracleValidateBackupJob(id, oracleValidateConfig)

Validate Oracle database backups

Queue a job to validate Oracle backups for a database snapshot or a specified timestamp.

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

let apiInstance = new RubrikRestApi.OracleApi();
let id = "id_example"; // String | ID of the database to be validated.
let oracleValidateConfig = new RubrikRestApi.OracleValidateConfig(); // OracleValidateConfig | Configuration parameters for a job to validate an Oracle backups.
apiInstance.createOracleValidateBackupJob(id, oracleValidateConfig, (error, data, response) => {
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
 **id** | **String**| ID of the database to be validated. | 
 **oracleValidateConfig** | [**OracleValidateConfig**](OracleValidateConfig.md)| Configuration parameters for a job to validate an Oracle backups. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDownloadedSnapshots

> AsyncRequestStatus deleteDownloadedSnapshots(id, opts)

Delete downloaded Oracle database snapshots and log snapshots

Requests an asynchronous job to expire downloaded database snapshots taken during a specified time period as well as log snapshots that contain any logs with timestamps within that time period.

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

let apiInstance = new RubrikRestApi.OracleApi();
let id = "id_example"; // String | ID of the Oracle database.
let opts = {
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Uses the ISO 8601 format to specify the start of the time period used by the asynchronous snapshot expiration job, as in the example \"2016-01-01T01:23:45.678\".
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | Uses the ISO 8601 format to specify the end of the time period used by the asynchronous snapshot expiration job, as in the example \"2016-01-01T01:23:45.678\".
};
apiInstance.deleteDownloadedSnapshots(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Oracle database. | 
 **afterTime** | **Date**| Uses the ISO 8601 format to specify the start of the time period used by the asynchronous snapshot expiration job, as in the example \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 
 **beforeTime** | **Date**| Uses the ISO 8601 format to specify the end of the time period used by the asynchronous snapshot expiration job, as in the example \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAcoParameterList

> OracleAcoParameterList getAcoParameterList()

List of supported Advanced Cloning Options

Get the list of supported Advanced Cloning Options (ACO) parameters.

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

let apiInstance = new RubrikRestApi.OracleApi();
apiInstance.getAcoParameterList((error, data, response) => {
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

[**OracleAcoParameterList**](OracleAcoParameterList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExampleAcoDownloadLink

> OracleFileDownloadLink getExampleAcoDownloadLink()

Link to download the Advanced Recovery Options example file

Link to download the Advanced Recovery Options example file which can be used to customize Oracle recoveries.

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

let apiInstance = new RubrikRestApi.OracleApi();
apiInstance.getExampleAcoDownloadLink((error, data, response) => {
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

[**OracleFileDownloadLink**](OracleFileDownloadLink.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOracleDbV1

> OracleDbDetail getOracleDbV1(id)

Get Oracle database information

Retrieves detailed information for a specified Oracle database object.

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

let apiInstance = new RubrikRestApi.OracleApi();
let id = "id_example"; // String | ID of an Oracle database object.
apiInstance.getOracleDbV1(id, (error, data, response) => {
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
 **id** | **String**| ID of an Oracle database object. | 

### Return type

[**OracleDbDetail**](OracleDbDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## oracleRestoreEstimate

> OracleRestoreEstimateResult oracleRestoreEstimate(id, opts)

Get a size estimate for a restore or export

The estimated size of the data to download from an archival location in order to perform a specified restore or export operation.

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

let apiInstance = new RubrikRestApi.OracleApi();
let id = "id_example"; // String | ID of the Oracle database.
let opts = {
  'snapshotId': "snapshotId_example", // String | ID of the snapshot to recover to.
  'recoveryTime': new Date("2013-10-20T19:20:30+01:00") // Date | The date and time for the recovery restore point, specified in the ISO 8601 format, as in the example \"2016-01-01T01:23:45.678\".
};
apiInstance.oracleRestoreEstimate(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Oracle database. | 
 **snapshotId** | **String**| ID of the snapshot to recover to. | [optional] 
 **recoveryTime** | **Date**| The date and time for the recovery restore point, specified in the ISO 8601 format, as in the example \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] 

### Return type

[**OracleRestoreEstimateResult**](OracleRestoreEstimateResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryOracleDbV1

> OracleDbSummaryListResponse queryOracleDbV1(opts)

Get summary information for Oracle databases

Retrieves an array containing summary information about the Oracle database objects in the Rubrik cluster.

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

let apiInstance = new RubrikRestApi.OracleApi();
let opts = {
  'name': "name_example", // String | Filters a response by making an infix comparison of the database name, SID, and tablespaces in the response with the specified value.
  'slaAssignment': "slaAssignment_example", // String | Limits the response to Oracle databases that are protected by the specified type of SLA Domain assignment.
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filters by effective SLA Domain ID.
  'primaryClusterId': "primaryClusterId_example", // String | Limits the response to Oracle databases that have the specified primary cluster value.
  'isRelic': true, // Boolean | Limits the response to Oracle databases that have the specified isRelic value.
  'isLiveMount': true, // Boolean | Limits the response to Oracle databases that have the specified isLiveMount value.
  'limit': 56, // Number | Limits the summary information to the specified number of matches. Optionally, it can be used with offset to begin the count of matches at the number specified in the offset parameter, and with sort_by to sort the results by the specified attribute.
  'offset': 56, // Number | Determines the elements to include in the response starting with the element at the index number specified here. Optionally used with limit to enable paging of the results by retrieving a smaller number of elements in the response.
  'sortBy': "sortBy_example", // String | Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified.
  'sortOrder': "sortOrder_example", // String | Specifies the ascending or descending order to sort the elements in the response by the attributes specified in the sort_by parameter.
  'includeBackupTaskInfo': false, // Boolean | Specifies whether to include the backup task information in the response.
  'isDataGuardGroup': true // Boolean | Limits the response to Oracle databases that have the specified value for the isDataGuardGroup flag.
};
apiInstance.queryOracleDbV1(opts, (error, data, response) => {
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
 **name** | **String**| Filters a response by making an infix comparison of the database name, SID, and tablespaces in the response with the specified value. | [optional] 
 **slaAssignment** | **String**| Limits the response to Oracle databases that are protected by the specified type of SLA Domain assignment. | [optional] 
 **effectiveSlaDomainId** | **String**| Filters by effective SLA Domain ID. | [optional] 
 **primaryClusterId** | **String**| Limits the response to Oracle databases that have the specified primary cluster value. | [optional] 
 **isRelic** | **Boolean**| Limits the response to Oracle databases that have the specified isRelic value. | [optional] 
 **isLiveMount** | **Boolean**| Limits the response to Oracle databases that have the specified isLiveMount value. | [optional] 
 **limit** | **Number**| Limits the summary information to the specified number of matches. Optionally, it can be used with offset to begin the count of matches at the number specified in the offset parameter, and with sort_by to sort the results by the specified attribute. | [optional] 
 **offset** | **Number**| Determines the elements to include in the response starting with the element at the index number specified here. Optionally used with limit to enable paging of the results by retrieving a smaller number of elements in the response. | [optional] 
 **sortBy** | **String**| Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified. | [optional] 
 **sortOrder** | **String**| Specifies the ascending or descending order to sort the elements in the response by the attributes specified in the sort_by parameter. | [optional] 
 **includeBackupTaskInfo** | **Boolean**| Specifies whether to include the backup task information in the response. | [optional] [default to false]
 **isDataGuardGroup** | **Boolean**| Limits the response to Oracle databases that have the specified value for the isDataGuardGroup flag. | [optional] 

### Return type

[**OracleDbSummaryListResponse**](OracleDbSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateOracleDataGuardGroup

> OracleDbDetail updateOracleDataGuardGroup(id, oracleDataGuardGroupUpdate)

Update an Oracle Data Guard group

Update properties of an Oracle Data Guard group object.

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

let apiInstance = new RubrikRestApi.OracleApi();
let id = "id_example"; // String | ID assigned to an Oracle Data Guard group object.
let oracleDataGuardGroupUpdate = new RubrikRestApi.OracleDataGuardGroupUpdate(); // OracleDataGuardGroupUpdate | Properties to use for the update of an Oracle Data Guard group object.
apiInstance.updateOracleDataGuardGroup(id, oracleDataGuardGroupUpdate, (error, data, response) => {
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
 **id** | **String**| ID assigned to an Oracle Data Guard group object. | 
 **oracleDataGuardGroupUpdate** | [**OracleDataGuardGroupUpdate**](OracleDataGuardGroupUpdate.md)| Properties to use for the update of an Oracle Data Guard group object. | 

### Return type

[**OracleDbDetail**](OracleDbDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOracleDbV1

> OracleDbDetail updateOracleDbV1(id, oracleUpdate)

Update an Oracle database

Updates the properties of a specified Oracle database object.

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

let apiInstance = new RubrikRestApi.OracleApi();
let id = "id_example"; // String | ID of an Oracle database object.
let oracleUpdate = new RubrikRestApi.OracleUpdate(); // OracleUpdate | Properties of the Oracle database object to be updated. object.
apiInstance.updateOracleDbV1(id, oracleUpdate, (error, data, response) => {
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
 **id** | **String**| ID of an Oracle database object. | 
 **oracleUpdate** | [**OracleUpdate**](OracleUpdate.md)| Properties of the Oracle database object to be updated. object. | 

### Return type

[**OracleDbDetail**](OracleDbDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## validateOracleAcoFile

> OracleAcoValidationResult validateOracleAcoFile(isLiveMount, body)

Validate Oracle ACO file

Validate the provided Oracle ACO (Advanced Cloning Options) file.

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

let apiInstance = new RubrikRestApi.OracleApi();
let isLiveMount = true; // Boolean | Boolean that determines whether the ACO file is being used for a Live Mount.
let body = "body_example"; // String | Contents of the Advanced Cloning Options file in base64 encoded format.
apiInstance.validateOracleAcoFile(isLiveMount, body, (error, data, response) => {
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
 **isLiveMount** | **Boolean**| Boolean that determines whether the ACO file is being used for a Live Mount. | 
 **body** | **String**| Contents of the Advanced Cloning Options file in base64 encoded format. | 

### Return type

[**OracleAcoValidationResult**](OracleAcoValidationResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

