# RubrikRestApi.FilesetApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browseFilesetSnapshot**](FilesetApi.md#browseFilesetSnapshot) | **GET** /fileset/snapshot/{id}/browse | Lists all files and directories in a given path
[**createDownloadFilesetSnapshotFromCloud**](FilesetApi.md#createDownloadFilesetSnapshotFromCloud) | **POST** /fileset/snapshot/{id}/download | Create a download fileset snapshot from archival request
[**createFileset**](FilesetApi.md#createFileset) | **POST** /fileset | Create one fileset for a host
[**createFilesetBackupJob**](FilesetApi.md#createFilesetBackupJob) | **POST** /fileset/{id}/snapshot | Initiate an on-demand backup for a fileset
[**createFilesetDownloadFileJob**](FilesetApi.md#createFilesetDownloadFileJob) | **POST** /fileset/snapshot/{id}/download_file | Create a file download job from a fileset backup
[**createFilesetExportFileJob**](FilesetApi.md#createFilesetExportFileJob) | **POST** /fileset/snapshot/{id}/export_file | Create export job
[**createFilesetRestoreFileJob**](FilesetApi.md#createFilesetRestoreFileJob) | **POST** /fileset/snapshot/{id}/restore_file | Create restore job
[**deleteFileset**](FilesetApi.md#deleteFileset) | **DELETE** /fileset/{id} | Delete a fileset
[**deleteFilesetSnapshot**](FilesetApi.md#deleteFilesetSnapshot) | **DELETE** /fileset/snapshot/{id} | Delete a fileset snapshot
[**deleteFilesetSnapshots**](FilesetApi.md#deleteFilesetSnapshots) | **DELETE** /fileset/{id}/snapshot | Delete all snapshots of a fileset
[**getFileset**](FilesetApi.md#getFileset) | **GET** /fileset/{id} | Get information for a single fileset
[**getFilesetAsyncRequestStatus**](FilesetApi.md#getFilesetAsyncRequestStatus) | **GET** /fileset/request/{id} | Get details about an async request
[**getFilesetSnapshot**](FilesetApi.md#getFilesetSnapshot) | **GET** /fileset/snapshot/{id} | Get information for a fileset snapshot
[**getMissedFilesetSnapshots**](FilesetApi.md#getMissedFilesetSnapshots) | **GET** /fileset/{id}/missed_snapshot | Get missed snapshots for a fileset
[**queryFileset**](FilesetApi.md#queryFileset) | **GET** /fileset | Get summary information for all filesets
[**searchFileset**](FilesetApi.md#searchFileset) | **GET** /fileset/{id}/search | Search for a file within the fileset
[**updateFileset**](FilesetApi.md#updateFileset) | **PATCH** /fileset/{id} | Update a Fileset



## browseFilesetSnapshot

> BrowseResponseListResponse browseFilesetSnapshot(id, path, opts)

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | ID of snapshot.
let path = "path_example"; // String | The absolute path of the starting point for the directory listing.
let opts = {
  'offset': 56, // Number | Starting position in the list of path entries contained in the query results, sorted by lexicographical order. The response includes the specified numbered entry and all higher numbered entries.
  'limit': 56 // Number | Maximum number of entries in the response.
};
apiInstance.browseFilesetSnapshot(id, path, opts, (error, data, response) => {
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


## createDownloadFilesetSnapshotFromCloud

> AsyncRequestStatus createDownloadFilesetSnapshotFromCloud(id)

Create a download fileset snapshot from archival request

Create a download fileset snapshot from archival request.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | ID of snapshot.
apiInstance.createDownloadFilesetSnapshotFromCloud(id, (error, data, response) => {
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

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createFileset

> FilesetDetail createFileset(filesetCreate)

Create one fileset for a host

Create a fileset for a network host. A fileset is a fileset template applied to a host.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let filesetCreate = new RubrikRestApi.FilesetCreate(); // FilesetCreate | Specify a template ID and either a host ID or a share ID. When a share ID is provided, the host ID is derived from the host share. Also specify whether or not this backup is a direct archive backup.
apiInstance.createFileset(filesetCreate, (error, data, response) => {
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
 **filesetCreate** | [**FilesetCreate**](FilesetCreate.md)| Specify a template ID and either a host ID or a share ID. When a share ID is provided, the host ID is derived from the host share. Also specify whether or not this backup is a direct archive backup. | 

### Return type

[**FilesetDetail**](FilesetDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createFilesetBackupJob

> AsyncRequestStatus createFilesetBackupJob(id, opts)

Initiate an on-demand backup for a fileset

Create an on-demand backup request for the given fileset.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | ID of the Fileset.
let opts = {
  'baseOnDemandSnapshotConfig': new RubrikRestApi.BaseOnDemandSnapshotConfig() // BaseOnDemandSnapshotConfig | Configuration for the on-demand backup.
};
apiInstance.createFilesetBackupJob(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Fileset. | 
 **baseOnDemandSnapshotConfig** | [**BaseOnDemandSnapshotConfig**](BaseOnDemandSnapshotConfig.md)| Configuration for the on-demand backup. | [optional] 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createFilesetDownloadFileJob

> AsyncRequestStatus createFilesetDownloadFileJob(id, filesetDownloadFileJobConfig)

Create a file download job from a fileset backup

Initiate a job to download a file from a backup of a fileset. Returns a job instance ID. An email notification will be sent out when the download is ready. When the download is ready, the file can be downloaded from the corresponding event which includes the job instance ID as the value of **jobInstanceId**.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | ID of snapshot.
let filesetDownloadFileJobConfig = new RubrikRestApi.FilesetDownloadFileJobConfig(); // FilesetDownloadFileJobConfig | Configuration for a download job.
apiInstance.createFilesetDownloadFileJob(id, filesetDownloadFileJobConfig, (error, data, response) => {
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
 **filesetDownloadFileJobConfig** | [**FilesetDownloadFileJobConfig**](FilesetDownloadFileJobConfig.md)| Configuration for a download job. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createFilesetExportFileJob

> AsyncRequestStatus createFilesetExportFileJob(id, filesetExportFileJobConfig)

Create export job

Initiate a job to copy a file or folder from a fileset backup to a destination host other than the source host. Returns the job instance ID.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | ID of snapshot.
let filesetExportFileJobConfig = new RubrikRestApi.FilesetExportFileJobConfig(); // FilesetExportFileJobConfig | Configuration for job to export a file or folder from a fileset backup.
apiInstance.createFilesetExportFileJob(id, filesetExportFileJobConfig, (error, data, response) => {
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
 **filesetExportFileJobConfig** | [**FilesetExportFileJobConfig**](FilesetExportFileJobConfig.md)| Configuration for job to export a file or folder from a fileset backup. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createFilesetRestoreFileJob

> AsyncRequestStatus createFilesetRestoreFileJob(id, filesetRestoreFileJobConfig)

Create restore job

Initiate a job to copy a file or folder from a fileset backup to the source host. Returns the job instance ID.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | ID of snapshot.
let filesetRestoreFileJobConfig = new RubrikRestApi.FilesetRestoreFileJobConfig(); // FilesetRestoreFileJobConfig | Configuration for job to restore a file or folder from a fileset backup.
apiInstance.createFilesetRestoreFileJob(id, filesetRestoreFileJobConfig, (error, data, response) => {
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
 **filesetRestoreFileJobConfig** | [**FilesetRestoreFileJobConfig**](FilesetRestoreFileJobConfig.md)| Configuration for job to restore a file or folder from a fileset backup. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteFileset

> deleteFileset(id, opts)

Delete a fileset

Delete a fileset by specifying the fileset ID.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | Provide a fileset ID to delete.
let opts = {
  'preserveSnapshots': true // Boolean | Flag to indicate whether to preserve snapshots of the fileset or to delete them. Default behavior is to preserve them.
};
apiInstance.deleteFileset(id, opts, (error, data, response) => {
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
 **id** | **String**| Provide a fileset ID to delete. | 
 **preserveSnapshots** | **Boolean**| Flag to indicate whether to preserve snapshots of the fileset or to delete them. Default behavior is to preserve them. | [optional] 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteFilesetSnapshot

> deleteFilesetSnapshot(id, location)

Delete a fileset snapshot

Delete a fileset snapshot. A snapshot is deleted only if it is an on-demand snapshot, a snapshot of an unprotected fileset or a local snapshot that was downloaded from an archive location.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | ID of snapshot.
let location = "location_example"; // String | Snapshot location to delete. Use **_local_** to delete all local snapshots and **_all_** to delete the snapshot in all locations.
apiInstance.deleteFilesetSnapshot(id, location, (error, data, response) => {
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
 **location** | **String**| Snapshot location to delete. Use **_local_** to delete all local snapshots and **_all_** to delete the snapshot in all locations. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteFilesetSnapshots

> deleteFilesetSnapshots(id)

Delete all snapshots of a fileset

Delete all snapshots that were created based on a fileset by providing the fileset ID. Requires an unprotected fileset. Remove the fileset from all SLA Domains.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | ID of the fileset.
apiInstance.deleteFilesetSnapshots(id, (error, data, response) => {
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
 **id** | **String**| ID of the fileset. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFileset

> FilesetDetail getFileset(id)

Get information for a single fileset

Retrieve summary information for a fileset by specifying the fileset ID.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | Specify the fileset ID.
apiInstance.getFileset(id, (error, data, response) => {
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
 **id** | **String**| Specify the fileset ID. | 

### Return type

[**FilesetDetail**](FilesetDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFilesetAsyncRequestStatus

> AsyncRequestStatus getFilesetAsyncRequestStatus(id)

Get details about an async request

Get details about a fileset related async request.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | ID of the request.
apiInstance.getFilesetAsyncRequestStatus(id, (error, data, response) => {
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


## getFilesetSnapshot

> FilesetSnapshotDetail getFilesetSnapshot(id, opts)

Get information for a fileset snapshot

Retrieve summary information for a fileset snapshot by specifying the snapshot ID.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | ID of snapshot.
let opts = {
  'verbose': false // Boolean | Whether or not to fetch verbose fileset snapshot information. The performance of this endpoint will decrease if set to true.
};
apiInstance.getFilesetSnapshot(id, opts, (error, data, response) => {
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
 **verbose** | **Boolean**| Whether or not to fetch verbose fileset snapshot information. The performance of this endpoint will decrease if set to true. | [optional] [default to false]

### Return type

[**FilesetSnapshotDetail**](FilesetSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMissedFilesetSnapshots

> MissedSnapshotListResponse getMissedFilesetSnapshots(id)

Get missed snapshots for a fileset

Retrieve summary information about all missed snapshots for a fileset.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | ID of the fileset.
apiInstance.getMissedFilesetSnapshots(id, (error, data, response) => {
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
 **id** | **String**| ID of the fileset. | 

### Return type

[**MissedSnapshotListResponse**](MissedSnapshotListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryFileset

> FilesetSummaryListResponse queryFileset(opts)

Get summary information for all filesets

Retrieve summary information for each fileset. Optionally, filter the retrieved information.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let opts = {
  'primaryClusterId': "primaryClusterId_example", // String | Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session.
  'hostId': "hostId_example", // String | Filter the summary information based on the ID of the host referenced by the fileset.
  'shareId': "shareId_example", // String | Filter the summary information based on the ID of the host share referenced by the fileset. Use **_NONE_** to only return information for filesets that were not created based on a host share. Use **_ANY_** to only return information for filesets that were created based on a host share.
  'isRelic': true, // Boolean | Filter the summary information based on the relic status of the fileset. Returns both relic and non relic if the parameter is not set.
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filter the summary information based on the ID of the effective SLA Domain inherited by a fileset. Use **_UNPROTECTED_** to only return information for filesets that do not have an effective SLA Domain. Use **_PROTECTED_** to only return information for filesets that do have an effective SLA Domain.
  'templateId': "templateId_example", // String | Filter the summary information based on the ID of a fileset template.  Use **_NONE_** to only return information for filesets that were not created from a fileset template.  Use **_ANY_** to only return information for filesets that were created from a fileset template.
  'limit': 56, // Number | Limit the summary information to a specified maximum number of filesets.  Optionally, use with **_offset_** to start the count at a specified point.  Optionally, use with **_sort_by_** to perform sort on given attributes. Include **_sort_order_** to determine the ascending or descending direction of sort.
  'offset': 56, // Number | Starting position in the list of fileset entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as smaller groups of entries, e.g. for paging of results.
  'name': "name_example", // String | Retrieve filesets with a name matching the provided name. The search is performed as a case-insensitive infix search.
  'hostName': "hostName_example", // String | Retrieve filesets with a host name matching the provided name. The search is performed as a case-insensitive infix search.
  'sortBy': "sortBy_example", // String | Specifies a comma-separated list of fileset attributes to use in sorting the fileset summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified.  Valid attributes are: **_name_**, **_hostName_**, **_templateType_**, **_slaName_**, **_includes_**, **_excludes_**, and **_exceptions_**. Requires **_sort_order_**.
  'sortOrder': "sortOrder_example" // String | Sort order, either ascending or descending.
};
apiInstance.queryFileset(opts, (error, data, response) => {
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
 **hostId** | **String**| Filter the summary information based on the ID of the host referenced by the fileset. | [optional] 
 **shareId** | **String**| Filter the summary information based on the ID of the host share referenced by the fileset. Use **_NONE_** to only return information for filesets that were not created based on a host share. Use **_ANY_** to only return information for filesets that were created based on a host share. | [optional] 
 **isRelic** | **Boolean**| Filter the summary information based on the relic status of the fileset. Returns both relic and non relic if the parameter is not set. | [optional] 
 **effectiveSlaDomainId** | **String**| Filter the summary information based on the ID of the effective SLA Domain inherited by a fileset. Use **_UNPROTECTED_** to only return information for filesets that do not have an effective SLA Domain. Use **_PROTECTED_** to only return information for filesets that do have an effective SLA Domain. | [optional] 
 **templateId** | **String**| Filter the summary information based on the ID of a fileset template.  Use **_NONE_** to only return information for filesets that were not created from a fileset template.  Use **_ANY_** to only return information for filesets that were created from a fileset template. | [optional] 
 **limit** | **Number**| Limit the summary information to a specified maximum number of filesets.  Optionally, use with **_offset_** to start the count at a specified point.  Optionally, use with **_sort_by_** to perform sort on given attributes. Include **_sort_order_** to determine the ascending or descending direction of sort. | [optional] 
 **offset** | **Number**| Starting position in the list of fileset entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as smaller groups of entries, e.g. for paging of results. | [optional] 
 **name** | **String**| Retrieve filesets with a name matching the provided name. The search is performed as a case-insensitive infix search. | [optional] 
 **hostName** | **String**| Retrieve filesets with a host name matching the provided name. The search is performed as a case-insensitive infix search. | [optional] 
 **sortBy** | **String**| Specifies a comma-separated list of fileset attributes to use in sorting the fileset summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified.  Valid attributes are: **_name_**, **_hostName_**, **_templateType_**, **_slaName_**, **_includes_**, **_excludes_**, and **_exceptions_**. Requires **_sort_order_**. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] 

### Return type

[**FilesetSummaryListResponse**](FilesetSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchFileset

> SearchResponseListResponse searchFileset(id, path, opts)

Search for a file within the fileset

Search for a file within the fileset. Search via full path prefix or filename prefix.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | Fileset ID to search.
let path = "path_example"; // String | The path query. Either path prefix or filename prefix.
let opts = {
  'limit': 56, // Number | Maximum number of entries in the response.
  'cursor': "cursor_example" // String | Pagination cursor returned by the previous request.
};
apiInstance.searchFileset(id, path, opts, (error, data, response) => {
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
 **id** | **String**| Fileset ID to search. | 
 **path** | **String**| The path query. Either path prefix or filename prefix. | 
 **limit** | **Number**| Maximum number of entries in the response. | [optional] 
 **cursor** | **String**| Pagination cursor returned by the previous request. | [optional] 

### Return type

[**SearchResponseListResponse**](SearchResponseListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateFileset

> FilesetDetail updateFileset(id, filesetUpdate)

Update a Fileset

Update a Fileset with the specified properties.

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

let apiInstance = new RubrikRestApi.FilesetApi();
let id = "id_example"; // String | ID of the Fileset. to update.
let filesetUpdate = new RubrikRestApi.FilesetUpdate(); // FilesetUpdate | Properties to update.
apiInstance.updateFileset(id, filesetUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the Fileset. to update. | 
 **filesetUpdate** | [**FilesetUpdate**](FilesetUpdate.md)| Properties to update. | 

### Return type

[**FilesetDetail**](FilesetDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

