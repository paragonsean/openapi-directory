# RubrikRestApi.HdfsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browseHdfsSnapshot**](HdfsApi.md#browseHdfsSnapshot) | **GET** /hdfs/snapshot/{id}/browse | Lists all files and directories in a given path
[**createHdfs**](HdfsApi.md#createHdfs) | **POST** /hdfs | Create one HDFS directory for a host
[**createHdfsBackupJob**](HdfsApi.md#createHdfsBackupJob) | **POST** /hdfs/{id}/snapshot | Initiate an on-demand backup for a HDFS directory
[**createHdfsExportFileJob**](HdfsApi.md#createHdfsExportFileJob) | **POST** /hdfs/snapshot/{id}/export_file | Create export job
[**createHdfsRestoreFileJob**](HdfsApi.md#createHdfsRestoreFileJob) | **POST** /hdfs/snapshot/{id}/restore_file | Create restore job
[**deleteHdfs**](HdfsApi.md#deleteHdfs) | **DELETE** /hdfs/{id} | Delete a HDFS directory
[**deleteHdfsSnapshot**](HdfsApi.md#deleteHdfsSnapshot) | **DELETE** /hdfs/snapshot/{id} | Delete a HDFS directory snapshot
[**deleteHdfsSnapshots**](HdfsApi.md#deleteHdfsSnapshots) | **DELETE** /hdfs/{id}/snapshot | Delete all snapshots of a HDFS directory
[**getHdfs**](HdfsApi.md#getHdfs) | **GET** /hdfs/{id} | Get information for a single HDFS directory
[**getHdfsAsyncRequestStatus**](HdfsApi.md#getHdfsAsyncRequestStatus) | **GET** /hdfs/request/{id} | Get details about an asynchronous request
[**getHdfsSnapshot**](HdfsApi.md#getHdfsSnapshot) | **GET** /hdfs/snapshot/{id} | Get information for a HDFS directory snapshot
[**getMissedHdfsSnapshots**](HdfsApi.md#getMissedHdfsSnapshots) | **GET** /hdfs/{id}/missed_snapshot | Get missed snapshots for a HDFS directory
[**queryHdfs**](HdfsApi.md#queryHdfs) | **GET** /hdfs | Get summary information for all HDFS directories
[**searchHdfs**](HdfsApi.md#searchHdfs) | **GET** /hdfs/{id}/search | Search for a file within the HDFS directory
[**updateHdfs**](HdfsApi.md#updateHdfs) | **PATCH** /hdfs/{id} | Update a HDFS directory



## browseHdfsSnapshot

> BrowseResponseListResponse browseHdfsSnapshot(id, path, opts)

Lists all files and directories in a given path

Lists all files and directories in a given path.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | ID of snapshot.
let path = "path_example"; // String | The absolute path of the starting point for the directory listing.
let opts = {
  'offset': 56, // Number | Starting position in the list of path entries contained in the query results, sorted by lexicographical order. The response includes the specified numbered entry and all higher numbered entries.
  'limit': 56 // Number | Maximum number of entries in the response.
};
apiInstance.browseHdfsSnapshot(id, path, opts, (error, data, response) => {
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
 **path** | **String**| The absolute path of the starting point for the directory listing. | 
 **offset** | **Number**| Starting position in the list of path entries contained in the query results, sorted by lexicographical order. The response includes the specified numbered entry and all higher numbered entries. | [optional] 
 **limit** | **Number**| Maximum number of entries in the response. | [optional] 

### Return type

[**BrowseResponseListResponse**](BrowseResponseListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createHdfs

> HdfsDetail createHdfs(hdfsCreate)

Create one HDFS directory for a host

Create a HDFS directory for a network host. A HDFS directory is a HDFS directory template applied to a host.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let hdfsCreate = new RubrikRestApi.HdfsCreate(); // HdfsCreate | Specify a template ID and a host ID.
apiInstance.createHdfs(hdfsCreate, (error, data, response) => {
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
 **hdfsCreate** | [**HdfsCreate**](HdfsCreate.md)| Specify a template ID and a host ID. | 

### Return type

[**HdfsDetail**](HdfsDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createHdfsBackupJob

> AsyncRequestStatus createHdfsBackupJob(id, opts)

Initiate an on-demand backup for a HDFS directory

Create on-demand backup request for HDFS directory.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | ID of the HDFS directory.
let opts = {
  'baseOnDemandSnapshotConfig': new RubrikRestApi.BaseOnDemandSnapshotConfig() // BaseOnDemandSnapshotConfig | Configuration for the on-demand backup.
};
apiInstance.createHdfsBackupJob(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the HDFS directory. | 
 **baseOnDemandSnapshotConfig** | [**BaseOnDemandSnapshotConfig**](BaseOnDemandSnapshotConfig.md)| Configuration for the on-demand backup. | [optional] 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createHdfsExportFileJob

> AsyncRequestStatus createHdfsExportFileJob(id, hdfsExportFileJobConfig)

Create export job

Initiate a job to copy a file or folder from a hdfs backup to a destination host other than the source host. Returns the job instance ID.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | ID of snapshot.
let hdfsExportFileJobConfig = new RubrikRestApi.HdfsExportFileJobConfig(); // HdfsExportFileJobConfig | Configuration for job to export a file or folder from a hdfs backup.
apiInstance.createHdfsExportFileJob(id, hdfsExportFileJobConfig, (error, data, response) => {
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
 **hdfsExportFileJobConfig** | [**HdfsExportFileJobConfig**](HdfsExportFileJobConfig.md)| Configuration for job to export a file or folder from a hdfs backup. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createHdfsRestoreFileJob

> AsyncRequestStatus createHdfsRestoreFileJob(id, hdfsRestoreFileJobConfig)

Create restore job

Initiate a job to copy a file or folder from a HDFS directory backup to the source host. Returns the job instance ID.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | ID of snapshot.
let hdfsRestoreFileJobConfig = new RubrikRestApi.HdfsRestoreFileJobConfig(); // HdfsRestoreFileJobConfig | Configuration for job to restore a file or folder from a HDFS directory backup.
apiInstance.createHdfsRestoreFileJob(id, hdfsRestoreFileJobConfig, (error, data, response) => {
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
 **hdfsRestoreFileJobConfig** | [**HdfsRestoreFileJobConfig**](HdfsRestoreFileJobConfig.md)| Configuration for job to restore a file or folder from a HDFS directory backup. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteHdfs

> deleteHdfs(id, opts)

Delete a HDFS directory

Delete a HDFS directory by specifying the HDFS directory ID.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | Provide a HDFS directory ID to delete.
let opts = {
  'preserveSnapshots': true // Boolean | A flag that indicates whether the snapshots of the HDFS directory are preserved or deleted. By default, snapshots are preserved.
};
apiInstance.deleteHdfs(id, opts, (error, data, response) => {
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
 **id** | **String**| Provide a HDFS directory ID to delete. | 
 **preserveSnapshots** | **Boolean**| A flag that indicates whether the snapshots of the HDFS directory are preserved or deleted. By default, snapshots are preserved. | [optional] 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteHdfsSnapshot

> deleteHdfsSnapshot(id)

Delete a HDFS directory snapshot

Delete a HDFS directory snapshot. A snapshot is deleted only if it is an on-demand snapshot, or a snapshot of an unprotected HDFS directory.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | ID of snapshot.
apiInstance.deleteHdfsSnapshot(id, (error, data, response) => {
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
 **id** | **String**| ID of snapshot. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteHdfsSnapshots

> deleteHdfsSnapshots(id)

Delete all snapshots of a HDFS directory

Delete all snapshots that were created based on a hdfs by providing the HDFS directory ID. Requires an unprotected HDFS directory. Remove the HDFS directory from all SLA Domains.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | ID of the HDFS directory.
apiInstance.deleteHdfsSnapshots(id, (error, data, response) => {
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
 **id** | **String**| ID of the HDFS directory. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getHdfs

> HdfsDetail getHdfs(id)

Get information for a single HDFS directory

Retrieve summary information for a HDFS directory by specifying the HDFS directory ID.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | Specify the HDFS directory ID.
apiInstance.getHdfs(id, (error, data, response) => {
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
 **id** | **String**| Specify the HDFS directory ID. | 

### Return type

[**HdfsDetail**](HdfsDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHdfsAsyncRequestStatus

> AsyncRequestStatus getHdfsAsyncRequestStatus(id)

Get details about an asynchronous request

Get details about a hdfs related asynchronous request.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | ID of the request.
apiInstance.getHdfsAsyncRequestStatus(id, (error, data, response) => {
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


## getHdfsSnapshot

> HdfsSnapshotDetail getHdfsSnapshot(id)

Get information for a HDFS directory snapshot

Retrieve summary information for a HDFS directory snapshot by specifying the snapshot ID.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | ID of snapshot.
apiInstance.getHdfsSnapshot(id, (error, data, response) => {
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

[**HdfsSnapshotDetail**](HdfsSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMissedHdfsSnapshots

> MissedSnapshotListResponse getMissedHdfsSnapshots(id)

Get missed snapshots for a HDFS directory

Retrieve summary information about all missed snapshots for a HDFS directory.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | ID of the HDFS directory.
apiInstance.getMissedHdfsSnapshots(id, (error, data, response) => {
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
 **id** | **String**| ID of the HDFS directory. | 

### Return type

[**MissedSnapshotListResponse**](MissedSnapshotListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryHdfs

> HdfsSummaryListResponse queryHdfs(opts)

Get summary information for all HDFS directories

Retrieve summary information for each HDFS directory. Optionally, filter the retrieved information.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let opts = {
  'primaryClusterId': "primaryClusterId_example", // String | Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session.
  'hostId': "hostId_example", // String | Filter the summary information based on the ID of the host referenced by the HDFS directory (name node).
  'isRelic': true, // Boolean | Filter the summary information based on the relic status of the HDFS directory. When this parameter is not set, the returned HDFS directory summary information is not filtered by relic status.
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filter the summary information based on the ID of the effective SLA Domain inherited by a HDFS directory. Use **_UNPROTECTED_** to only return information for HDFS directories that do not have an effective SLA Domain. Use **_PROTECTED_** to only return information for HDFS directories that have an effective SLA Domain.
  'templateId': "templateId_example", // String | Filter the summary information based on the ID of a HDFS directory template. Use **_NONE_** to only return information for HDFS directories that were not created from a HDFS directory template. Use **_ANY_** to only return information for HDFS directories that were created from a HDFS directory template.
  'limit': 56, // Number | Limit the summary information to a specified maximum number of HDFS directories. Optionally, use with **_offset_** to start the count at a specified point. Optionally, use with **_sort_by_** to perform sort on given attributes. Include **_sort_order_** to determine the ascending or descending direction of sort.
  'offset': 56, // Number | Starting position in the list of HDFS directory entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as a collection of grouped entries for paging.
  'name': "name_example", // String | Retrieve HDFS directories with a name matching the provided name. The search is performed as a case-insensitive infix search.
  'hostName': "hostName_example", // String | Retrieve HDFS directories with a host name (name node) matching the provided name. The search is performed as a case-insensitive infix search.
  'sortBy': "'name'", // String | Specifies a comma-separated list of HDFS directory attributes to use in sorting the HDFS directory summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified. Valid attributes are: **_name_**, **_hostName_**, **_templateType_**, **_slaName_**, **_includes_**, **_excludes_**, and **_exceptions_**. Requires **_sort_order_**.
  'sortOrder': "'asc'" // String | Sort order, either ascending or descending.
};
apiInstance.queryHdfs(opts, (error, data, response) => {
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
 **primaryClusterId** | **String**| Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session. | [optional] 
 **hostId** | **String**| Filter the summary information based on the ID of the host referenced by the HDFS directory (name node). | [optional] 
 **isRelic** | **Boolean**| Filter the summary information based on the relic status of the HDFS directory. When this parameter is not set, the returned HDFS directory summary information is not filtered by relic status. | [optional] 
 **effectiveSlaDomainId** | **String**| Filter the summary information based on the ID of the effective SLA Domain inherited by a HDFS directory. Use **_UNPROTECTED_** to only return information for HDFS directories that do not have an effective SLA Domain. Use **_PROTECTED_** to only return information for HDFS directories that have an effective SLA Domain. | [optional] 
 **templateId** | **String**| Filter the summary information based on the ID of a HDFS directory template. Use **_NONE_** to only return information for HDFS directories that were not created from a HDFS directory template. Use **_ANY_** to only return information for HDFS directories that were created from a HDFS directory template. | [optional] 
 **limit** | **Number**| Limit the summary information to a specified maximum number of HDFS directories. Optionally, use with **_offset_** to start the count at a specified point. Optionally, use with **_sort_by_** to perform sort on given attributes. Include **_sort_order_** to determine the ascending or descending direction of sort. | [optional] 
 **offset** | **Number**| Starting position in the list of HDFS directory entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as a collection of grouped entries for paging. | [optional] 
 **name** | **String**| Retrieve HDFS directories with a name matching the provided name. The search is performed as a case-insensitive infix search. | [optional] 
 **hostName** | **String**| Retrieve HDFS directories with a host name (name node) matching the provided name. The search is performed as a case-insensitive infix search. | [optional] 
 **sortBy** | **String**| Specifies a comma-separated list of HDFS directory attributes to use in sorting the HDFS directory summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified. Valid attributes are: **_name_**, **_hostName_**, **_templateType_**, **_slaName_**, **_includes_**, **_excludes_**, and **_exceptions_**. Requires **_sort_order_**. | [optional] [default to &#39;name&#39;]
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [default to &#39;asc&#39;]

### Return type

[**HdfsSummaryListResponse**](HdfsSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchHdfs

> SearchResponseListResponse searchHdfs(id, path, opts)

Search for a file within the HDFS directory

Search for a file within the HDFS directory. Search using full path prefix or filename prefix.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | HDFS directory ID to search.
let path = "path_example"; // String | The path query. The query can be a path refix or a filename prefix.
let opts = {
  'limit': 56, // Number | Maximum number of entries in the response.
  'cursor': "cursor_example" // String | Pagination cursor returned by the previous request.
};
apiInstance.searchHdfs(id, path, opts, (error, data, response) => {
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
 **id** | **String**| HDFS directory ID to search. | 
 **path** | **String**| The path query. The query can be a path refix or a filename prefix. | 
 **limit** | **Number**| Maximum number of entries in the response. | [optional] 
 **cursor** | **String**| Pagination cursor returned by the previous request. | [optional] 

### Return type

[**SearchResponseListResponse**](SearchResponseListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateHdfs

> HdfsDetail updateHdfs(id, hdfsUpdate)

Update a HDFS directory

Update a HDFS directory with the specified properties.

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

let apiInstance = new RubrikRestApi.HdfsApi();
let id = "id_example"; // String | ID of the HDFS directory to update.
let hdfsUpdate = new RubrikRestApi.HdfsUpdate(); // HdfsUpdate | Properties to update.
apiInstance.updateHdfs(id, hdfsUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the HDFS directory to update. | 
 **hdfsUpdate** | [**HdfsUpdate**](HdfsUpdate.md)| Properties to update. | 

### Return type

[**HdfsDetail**](HdfsDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

