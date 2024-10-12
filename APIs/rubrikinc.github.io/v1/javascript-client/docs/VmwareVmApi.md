# RubrikRestApi.VmwareVmApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchMountSnapshot**](VmwareVmApi.md#batchMountSnapshot) | **POST** /vmware/vm/batch_mount | Live mount a snapshot each from a set of virtual machines
[**browseVmwareSnapshot**](VmwareVmApi.md#browseVmwareSnapshot) | **GET** /vmware/vm/snapshot/{id}/browse | List files in VM snapshot
[**bulkCreateOnDemandBackup**](VmwareVmApi.md#bulkCreateOnDemandBackup) | **POST** /vmware/vm/snapshot/bulk | Take an on-demand snapshot of multiple virtual machines
[**createDownloadFileJob**](VmwareVmApi.md#createDownloadFileJob) | **POST** /vmware/vm/snapshot/{id}/download_file | Download file from VM snapshot
[**createDownloadSnapshotFromCloud**](VmwareVmApi.md#createDownloadSnapshotFromCloud) | **POST** /vmware/vm/snapshot/{id}/download | Download snapshot from archive
[**createExportV1**](VmwareVmApi.md#createExportV1) | **POST** /vmware/vm/snapshot/{id}/export | Export VM snapshot
[**createExportWithDownloadFromCloudV1**](VmwareVmApi.md#createExportWithDownloadFromCloudV1) | **POST** /vmware/vm/snapshot/{id}/export_with_download | Download a snapshot from an archival location, then export a virtual machine using the downloaded snapshot
[**createInstantRecovery**](VmwareVmApi.md#createInstantRecovery) | **POST** /vmware/vm/snapshot/{id}/instant_recover | Instantly recover a VM
[**createMountV1**](VmwareVmApi.md#createMountV1) | **POST** /vmware/vm/snapshot/{id}/mount | Live mount a VM from a snapshot
[**createOnDemandBackup**](VmwareVmApi.md#createOnDemandBackup) | **POST** /vmware/vm/{id}/snapshot | Create an on-demand snapshot for a VM
[**createRestoreFileJob**](VmwareVmApi.md#createRestoreFileJob) | **POST** /vmware/vm/snapshot/{id}/restore_file | Restore file from VM snapshot
[**createUnmount**](VmwareVmApi.md#createUnmount) | **DELETE** /vmware/vm/snapshot/mount/{id} | Delete a Live Mount VM
[**deleteVmwareSnapshot**](VmwareVmApi.md#deleteVmwareSnapshot) | **DELETE** /vmware/vm/snapshot/{id} | Delete VM snapshot
[**deleteVmwareSnapshots**](VmwareVmApi.md#deleteVmwareSnapshots) | **DELETE** /vmware/vm/{id}/snapshot | Delete all snapshots of VM
[**getAsyncRequestStatus**](VmwareVmApi.md#getAsyncRequestStatus) | **GET** /vmware/vm/request/{id} | Get asynchronous request details for VM
[**getMountV1**](VmwareVmApi.md#getMountV1) | **GET** /vmware/vm/snapshot/mount/{id} | Get information for a Live Mount
[**getSnapshot**](VmwareVmApi.md#getSnapshot) | **GET** /vmware/vm/snapshot/{id} | Get VM snapshot details
[**getVirtualDisk**](VmwareVmApi.md#getVirtualDisk) | **GET** /vmware/vm/virtual_disk/{id} | Details about the specific Virtual Disk
[**getVm**](VmwareVmApi.md#getVm) | **GET** /vmware/vm/{id} | Get VM details
[**getVmForceFullSpec**](VmwareVmApi.md#getVmForceFullSpec) | **GET** /vmware/vm/{id}/request/force_full_snapshot | Retrieve the configuration for forcing a full snapshot of a VMware virtual machine
[**getVmwareCdpLiveInfo**](VmwareVmApi.md#getVmwareCdpLiveInfo) | **POST** /vmware/vm/cdp | Returns the live CDP info for a set of CDP-enabled virtual machines
[**getVmwareCdpStateInfo**](VmwareVmApi.md#getVmwareCdpStateInfo) | **POST** /vmware/vm/cdp_state | Returns CDP state info for a set of virtual machines
[**getVmwareMissedRecoverableRanges**](VmwareVmApi.md#getVmwareMissedRecoverableRanges) | **GET** /vmware/vm/{id}/missed_recoverable_range | Get missed time ranges for point in time recovery
[**getVmwareRecoverableRanges**](VmwareVmApi.md#getVmwareRecoverableRanges) | **GET** /vmware/vm/{id}/recoverable_range | Get available time ranges for point in time recovery
[**getVmwareVmMissedRecoverableRangesInBatch**](VmwareVmApi.md#getVmwareVmMissedRecoverableRangesInBatch) | **POST** /vmware/vm/missed_recoverable_range | Returns the recoverable ranges that were missed for a set of CDP-enabled virtual machines
[**getVmwareVmRecoverableRangesInBatch**](VmwareVmApi.md#getVmwareVmRecoverableRangesInBatch) | **POST** /vmware/vm/recoverable_range | Returns the recoverable ranges for a set of CDP-enabled virtual machines
[**missedSnapshots**](VmwareVmApi.md#missedSnapshots) | **GET** /vmware/vm/{id}/missed_snapshot | Get details about missed snapshots for a VM
[**queryMountV1**](VmwareVmApi.md#queryMountV1) | **GET** /vmware/vm/snapshot/mount | Get Live Mount information
[**querySnapshot**](VmwareVmApi.md#querySnapshot) | **GET** /vmware/vm/{id}/snapshot | Get list of snapshots of VM
[**querySnapshotsForVms**](VmwareVmApi.md#querySnapshotsForVms) | **POST** /vmware/vm/snapshots | Get snapshot information for a list of virtual machines
[**queryVm**](VmwareVmApi.md#queryVm) | **GET** /vmware/vm | Get list of VMs
[**relocateMount**](VmwareVmApi.md#relocateMount) | **POST** /vmware/vm/snapshot/mount/{id}/relocate | Relocate a virtual machine to another datastore
[**requestVmForceFullSnapshot**](VmwareVmApi.md#requestVmForceFullSnapshot) | **POST** /vmware/vm/{id}/request/force_full_snapshot | Request a full snapshot for the next backup job of a VMware virtual machine
[**runGuestOsScript**](VmwareVmApi.md#runGuestOsScript) | **POST** /vmware/vm/{id}/guest_script/run | Run guest OS script
[**searchVm**](VmwareVmApi.md#searchVm) | **GET** /vmware/vm/{id}/search | Search for a file from a VM
[**updateMount**](VmwareVmApi.md#updateMount) | **PATCH** /vmware/vm/snapshot/mount/{id} | Power a Live Mount on and off
[**updateVirtualDisk**](VmwareVmApi.md#updateVirtualDisk) | **PATCH** /vmware/vm/virtual_disk/{id} | Update a specific Virtual Disk
[**updateVm**](VmwareVmApi.md#updateVm) | **PATCH** /vmware/vm/{id} | Update VM
[**vmMakePrimary**](VmwareVmApi.md#vmMakePrimary) | **POST** /vmware/vm/make_primary | Make this cluster the primary for agents on a set of VMs
[**vmRegisterAgent**](VmwareVmApi.md#vmRegisterAgent) | **POST** /vmware/vm/{id}/register_agent | Register Rubrik Backup Service



## batchMountSnapshot

> BatchAsyncRequestStatus batchMountSnapshot(batchMountSnapshotJobConfig)

Live mount a snapshot each from a set of virtual machines

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let batchMountSnapshotJobConfig = new RubrikRestApi.BatchMountSnapshotJobConfig(); // BatchMountSnapshotJobConfig | Configuration object containing an array of virtual machine IDs, a way to indicate the snapshot to be chosen and mount configs.
apiInstance.batchMountSnapshot(batchMountSnapshotJobConfig, (error, data, response) => {
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
 **batchMountSnapshotJobConfig** | [**BatchMountSnapshotJobConfig**](BatchMountSnapshotJobConfig.md)| Configuration object containing an array of virtual machine IDs, a way to indicate the snapshot to be chosen and mount configs. | 

### Return type

[**BatchAsyncRequestStatus**](BatchAsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## browseVmwareSnapshot

> BrowseResponseListResponse browseVmwareSnapshot(id, path, opts)

List files in VM snapshot

For a virtual machine snapshot, list the directories and files that are beneath a specified file system path.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of snapshot.
let path = "path_example"; // String | The absolute path of the starting point for the directory listing.
let opts = {
  'offset': 56, // Number | Starting position in the list of path entries contained in the query results, sorted by lexicographical order. The response includes the specified numbered entry and all higher numbered entries.
  'limit': 56 // Number | Maximum number of entries in the response.
};
apiInstance.browseVmwareSnapshot(id, path, opts, (error, data, response) => {
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


## bulkCreateOnDemandBackup

> BatchAsyncRequestStatus bulkCreateOnDemandBackup(bulkOnDemandSnapshotJobConfig)

Take an on-demand snapshot of multiple virtual machines

Bulk operation of taking on-demand snapshot for given virtual machines.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let bulkOnDemandSnapshotJobConfig = new RubrikRestApi.BulkOnDemandSnapshotJobConfig(); // BulkOnDemandSnapshotJobConfig | The IDs of the virtual machines for which to take an on-demand snapshot and the ID of the SLA Domain to assign to the resulting snapshot.
apiInstance.bulkCreateOnDemandBackup(bulkOnDemandSnapshotJobConfig, (error, data, response) => {
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
 **bulkOnDemandSnapshotJobConfig** | [**BulkOnDemandSnapshotJobConfig**](BulkOnDemandSnapshotJobConfig.md)| The IDs of the virtual machines for which to take an on-demand snapshot and the ID of the SLA Domain to assign to the resulting snapshot. | 

### Return type

[**BatchAsyncRequestStatus**](BatchAsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDownloadFileJob

> AsyncRequestStatus createDownloadFileJob(id, downloadFileJobConfig)

Download file from VM snapshot

Create a request to download a file from a virtual machine snapshot.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of a snapshot.
let downloadFileJobConfig = new RubrikRestApi.DownloadFileJobConfig(); // DownloadFileJobConfig | Configuration for the file download request.
apiInstance.createDownloadFileJob(id, downloadFileJobConfig, (error, data, response) => {
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
 **id** | **String**| ID of a snapshot. | 
 **downloadFileJobConfig** | [**DownloadFileJobConfig**](DownloadFileJobConfig.md)| Configuration for the file download request. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDownloadSnapshotFromCloud

> AsyncRequestStatus createDownloadSnapshotFromCloud(id)

Download snapshot from archive

Provides a method for retrieving a snapshot, that is not available locally, from an archival location.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of snapshot.
apiInstance.createDownloadSnapshotFromCloud(id, (error, data, response) => {
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


## createExportV1

> AsyncRequestStatus createExportV1(id, exportSnapshotJobConfigV1)

Export VM snapshot

Export a virtual machine from a snapshot, using a specified hypervisor host as the datastore.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of a snapshot.
let exportSnapshotJobConfigV1 = new RubrikRestApi.ExportSnapshotJobConfigV1(); // ExportSnapshotJobConfigV1 | Configuration for the export request.
apiInstance.createExportV1(id, exportSnapshotJobConfigV1, (error, data, response) => {
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
 **id** | **String**| ID of a snapshot. | 
 **exportSnapshotJobConfigV1** | [**ExportSnapshotJobConfigV1**](ExportSnapshotJobConfigV1.md)| Configuration for the export request. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createExportWithDownloadFromCloudV1

> AsyncRequestStatus createExportWithDownloadFromCloudV1(id, exportSnapshotJobConfigV1)

Download a snapshot from an archival location, then export a virtual machine using the downloaded snapshot

Download a snapshot from an archival location and then export a virtual machine using the downloaded snapshot.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of a snapshot.
let exportSnapshotJobConfigV1 = new RubrikRestApi.ExportSnapshotJobConfigV1(); // ExportSnapshotJobConfigV1 | Configuration for the export request.
apiInstance.createExportWithDownloadFromCloudV1(id, exportSnapshotJobConfigV1, (error, data, response) => {
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
 **id** | **String**| ID of a snapshot. | 
 **exportSnapshotJobConfigV1** | [**ExportSnapshotJobConfigV1**](ExportSnapshotJobConfigV1.md)| Configuration for the export request. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createInstantRecovery

> AsyncRequestStatus createInstantRecovery(id, instantRecoveryJobConfig)

Instantly recover a VM

Instantly recovery a virtual machine from a snapshot. The Instant Recovery request starts the virtual machine with networking enabled and renames and powers off the source virtual machine, if it still exists.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of Snapshot.
let instantRecoveryJobConfig = new RubrikRestApi.InstantRecoveryJobConfig(); // InstantRecoveryJobConfig | Configuration for the Instant Recovery request.
apiInstance.createInstantRecovery(id, instantRecoveryJobConfig, (error, data, response) => {
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
 **id** | **String**| ID of Snapshot. | 
 **instantRecoveryJobConfig** | [**InstantRecoveryJobConfig**](InstantRecoveryJobConfig.md)| Configuration for the Instant Recovery request. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMountV1

> AsyncRequestStatus createMountV1(id, opts)

Live mount a VM from a snapshot

Create a request to Live Mount a virtual machine from a snapshot using a specified configuration.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of a snapshot.
let opts = {
  'mountSnapshotJobConfigV1': new RubrikRestApi.MountSnapshotJobConfigV1() // MountSnapshotJobConfigV1 | Configuration for the Live Mount request.
};
apiInstance.createMountV1(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of a snapshot. | 
 **mountSnapshotJobConfigV1** | [**MountSnapshotJobConfigV1**](MountSnapshotJobConfigV1.md)| Configuration for the Live Mount request. | [optional] 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOnDemandBackup

> AsyncRequestStatus createOnDemandBackup(id, opts)

Create an on-demand snapshot for a VM

Use the ID of a virtual machine to create an on-demand snapshot.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of the virtual machine.
let opts = {
  'baseOnDemandSnapshotConfig': new RubrikRestApi.BaseOnDemandSnapshotConfig() // BaseOnDemandSnapshotConfig | Configuration for the on-demand snapshot.
};
apiInstance.createOnDemandBackup(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the virtual machine. | 
 **baseOnDemandSnapshotConfig** | [**BaseOnDemandSnapshotConfig**](BaseOnDemandSnapshotConfig.md)| Configuration for the on-demand snapshot. | [optional] 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRestoreFileJob

> AsyncRequestStatus createRestoreFileJob(id, restoreFileJobConfig)

Restore file from VM snapshot

Create a request to restore a file or folder to the source virtual machine.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of a snapshot.
let restoreFileJobConfig = new RubrikRestApi.RestoreFileJobConfig(); // RestoreFileJobConfig | Configuration for the restore request.
apiInstance.createRestoreFileJob(id, restoreFileJobConfig, (error, data, response) => {
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
 **id** | **String**| ID of a snapshot. | 
 **restoreFileJobConfig** | [**RestoreFileJobConfig**](RestoreFileJobConfig.md)| Configuration for the restore request. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUnmount

> AsyncRequestStatus createUnmount(id, opts)

Delete a Live Mount VM

Create a request to delete a Live Mount virtual machine.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of a Live Mount.
let opts = {
  'force': true // Boolean | Force unmount to remove metadata when the datastore of the Live Mount virtual machine was moved off of the Rubrik cluster.
};
apiInstance.createUnmount(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of a Live Mount. | 
 **force** | **Boolean**| Force unmount to remove metadata when the datastore of the Live Mount virtual machine was moved off of the Rubrik cluster. | [optional] 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVmwareSnapshot

> deleteVmwareSnapshot(id, location)

Delete VM snapshot

Designate a snapshot as expired and available for garbage collection. The snapshot must be an on-demand snapshot or a snapshot from a virtual machine that is not assigned to an SLA Domain.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of snapshot.
let location = "location_example"; // String | Location of the snapshot. Use **_local_** to delete only the local copy of the snapshot. Or use **_all_** to delete the snapshot locally, on a replication target, and at an archival location.
apiInstance.deleteVmwareSnapshot(id, location, (error, data, response) => {
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
 **location** | **String**| Location of the snapshot. Use **_local_** to delete only the local copy of the snapshot. Or use **_all_** to delete the snapshot locally, on a replication target, and at an archival location. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteVmwareSnapshots

> deleteVmwareSnapshots(id)

Delete all snapshots of VM

Delete all of the snapshots from a virtual machine.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | Virtual machine ID.
apiInstance.deleteVmwareSnapshots(id, (error, data, response) => {
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
 **id** | **String**| Virtual machine ID. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAsyncRequestStatus

> AsyncRequestStatus getAsyncRequestStatus(id)

Get asynchronous request details for VM

Get the details of an asynchronous request that involves a VMware virtual machine.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of an asynchronous request.
apiInstance.getAsyncRequestStatus(id, (error, data, response) => {
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
 **id** | **String**| ID of an asynchronous request. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMountV1

> VmwareVmMountDetailV1 getMountV1(id)

Get information for a Live Mount

Retrieve detailed information for a specified Live Mount.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of a Live Mount.
apiInstance.getMountV1(id, (error, data, response) => {
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
 **id** | **String**| ID of a Live Mount. | 

### Return type

[**VmwareVmMountDetailV1**](VmwareVmMountDetailV1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSnapshot

> VmSnapshotDetail getSnapshot(id)

Get VM snapshot details

Retrieve detailed information about a virtual machine snapshot.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of a snapshot.
apiInstance.getSnapshot(id, (error, data, response) => {
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
 **id** | **String**| ID of a snapshot. | 

### Return type

[**VmSnapshotDetail**](VmSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVirtualDisk

> VirtualDiskDetail getVirtualDisk(id)

Details about the specific Virtual Disk

Detailed about the specific Virtual Disk.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of the Virtual Disk.
apiInstance.getVirtualDisk(id, (error, data, response) => {
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
 **id** | **String**| ID of the Virtual Disk. | 

### Return type

[**VirtualDiskDetail**](VirtualDiskDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVm

> VirtualMachineDetail getVm(id)

Get VM details

Retrieve details for a virtual machine.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of the virtual machine.
apiInstance.getVm(id, (error, data, response) => {
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
 **id** | **String**| ID of the virtual machine. | 

### Return type

[**VirtualMachineDetail**](VirtualMachineDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVmForceFullSpec

> VmForceFullResponse getVmForceFullSpec(id)

Retrieve the configuration for forcing a full snapshot of a VMware virtual machine

Retrieve the configuration that has been set for forcing a full snapshot for a VMware virtual machine.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of the VMware virtual machine.
apiInstance.getVmForceFullSpec(id, (error, data, response) => {
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
 **id** | **String**| ID of the VMware virtual machine. | 

### Return type

[**VmForceFullResponse**](VmForceFullResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVmwareCdpLiveInfo

> BatchVmwareCdpLiveInfo getVmwareCdpLiveInfo(requestBody)

Returns the live CDP info for a set of CDP-enabled virtual machines

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let requestBody = ["null"]; // [String] | The ID of each CDP-enabled virtual machine for which live info is being retrieved.
apiInstance.getVmwareCdpLiveInfo(requestBody, (error, data, response) => {
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
 **requestBody** | [**[String]**](String.md)| The ID of each CDP-enabled virtual machine for which live info is being retrieved. | 

### Return type

[**BatchVmwareCdpLiveInfo**](BatchVmwareCdpLiveInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getVmwareCdpStateInfo

> BatchVmwareCdpStateInfo getVmwareCdpStateInfo(requestBody)

Returns CDP state info for a set of virtual machines

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let requestBody = ["null"]; // [String] | The ID of each virtual machine for which CDP state info is being retrieved.
apiInstance.getVmwareCdpStateInfo(requestBody, (error, data, response) => {
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
 **requestBody** | [**[String]**](String.md)| The ID of each virtual machine for which CDP state info is being retrieved. | 

### Return type

[**BatchVmwareCdpStateInfo**](BatchVmwareCdpStateInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getVmwareMissedRecoverableRanges

> VmwareRecoverableRangeListResponse getVmwareMissedRecoverableRanges(id, opts)

Get missed time ranges for point in time recovery

Gets a list of time ranges to which a CDP-enabled virtual machine cannot perform a point-in-time recovery. The time ranges are indicated by start and end timestamps listed as date-time strings.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | The virtual machine ID.
let opts = {
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as `2018-01-01T01:23:45.678Z`.
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as `2018-01-01T01:23:45.678Z`.
};
apiInstance.getVmwareMissedRecoverableRanges(id, opts, (error, data, response) => {
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
 **id** | **String**| The virtual machine ID. | 
 **afterTime** | **Date**| Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;. | [optional] 
 **beforeTime** | **Date**| Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;. | [optional] 

### Return type

[**VmwareRecoverableRangeListResponse**](VmwareRecoverableRangeListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVmwareRecoverableRanges

> VmwareRecoverableRangeListResponse getVmwareRecoverableRanges(id, opts)

Get available time ranges for point in time recovery

Gets time ranges available for point-in-time recovery. The time ranges are indicated by start and end date-time strings.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | The virtual machine ID.
let opts = {
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as `2018-01-01T01:23:45.678Z`.
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as `2018-01-01T01:23:45.678Z`.
};
apiInstance.getVmwareRecoverableRanges(id, opts, (error, data, response) => {
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
 **id** | **String**| The virtual machine ID. | 
 **afterTime** | **Date**| Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;. | [optional] 
 **beforeTime** | **Date**| Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;. | [optional] 

### Return type

[**VmwareRecoverableRangeListResponse**](VmwareRecoverableRangeListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVmwareVmMissedRecoverableRangesInBatch

> BatchVmwareVmMissedRecoverableRanges getVmwareVmMissedRecoverableRangesInBatch(batchVmwareVmMissedRecoverableRangesRequest)

Returns the recoverable ranges that were missed for a set of CDP-enabled virtual machines

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let batchVmwareVmMissedRecoverableRangesRequest = new RubrikRestApi.BatchVmwareVmMissedRecoverableRangesRequest(); // BatchVmwareVmMissedRecoverableRangesRequest | The batch request and the date ranges (optional) as a filter. The batch request includes the ID of each CDP-enabled virtual machine for which missed recoverable ranges are being retrieved.
apiInstance.getVmwareVmMissedRecoverableRangesInBatch(batchVmwareVmMissedRecoverableRangesRequest, (error, data, response) => {
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
 **batchVmwareVmMissedRecoverableRangesRequest** | [**BatchVmwareVmMissedRecoverableRangesRequest**](BatchVmwareVmMissedRecoverableRangesRequest.md)| The batch request and the date ranges (optional) as a filter. The batch request includes the ID of each CDP-enabled virtual machine for which missed recoverable ranges are being retrieved. | 

### Return type

[**BatchVmwareVmMissedRecoverableRanges**](BatchVmwareVmMissedRecoverableRanges.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getVmwareVmRecoverableRangesInBatch

> BatchVmwareVmRecoverableRanges getVmwareVmRecoverableRangesInBatch(batchVmwareVmRecoverableRangesRequest)

Returns the recoverable ranges for a set of CDP-enabled virtual machines

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let batchVmwareVmRecoverableRangesRequest = new RubrikRestApi.BatchVmwareVmRecoverableRangesRequest(); // BatchVmwareVmRecoverableRangesRequest | The batch request, which includes the ID of each CDP-enabled virtual machine for which recoverable ranges are being retrieved, and optionally the date ranges as a filter.
apiInstance.getVmwareVmRecoverableRangesInBatch(batchVmwareVmRecoverableRangesRequest, (error, data, response) => {
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
 **batchVmwareVmRecoverableRangesRequest** | [**BatchVmwareVmRecoverableRangesRequest**](BatchVmwareVmRecoverableRangesRequest.md)| The batch request, which includes the ID of each CDP-enabled virtual machine for which recoverable ranges are being retrieved, and optionally the date ranges as a filter. | 

### Return type

[**BatchVmwareVmRecoverableRanges**](BatchVmwareVmRecoverableRanges.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## missedSnapshots

> MissedSnapshotListResponse missedSnapshots(id)

Get details about missed snapshots for a VM

Retrieve details about the missed snapshots for a virtual machine.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of a virtual machine.
apiInstance.missedSnapshots(id, (error, data, response) => {
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
 **id** | **String**| ID of a virtual machine. | 

### Return type

[**MissedSnapshotListResponse**](MissedSnapshotListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryMountV1

> VmwareVmMountSummaryV1ListResponse queryMountV1(opts)

Get Live Mount information

Retrieve summary information about Live Mount activity.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let opts = {
  'vmId': "vmId_example", // String | Filters information by virtual machine ID.
  'offset': 56, // Number | Starting position in the list of Live Mount entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as smaller groups of entries, e.g. for paging of the results.
  'limit': 56 // Number | Limit the summary information to a specified maximum number of entries. Optionally, use with **_offset_** to start the count at a specified point. Default is 25.
};
apiInstance.queryMountV1(opts, (error, data, response) => {
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
 **vmId** | **String**| Filters information by virtual machine ID. | [optional] 
 **offset** | **Number**| Starting position in the list of Live Mount entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as smaller groups of entries, e.g. for paging of the results. | [optional] 
 **limit** | **Number**| Limit the summary information to a specified maximum number of entries. Optionally, use with **_offset_** to start the count at a specified point. Default is 25. | [optional] 

### Return type

[**VmwareVmMountSummaryV1ListResponse**](VmwareVmMountSummaryV1ListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## querySnapshot

> VmSnapshotSummaryListResponse querySnapshot(id)

Get list of snapshots of VM

Retrieve summary information for the snapshots of a virtual machine.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of the virtual machine.
apiInstance.querySnapshot(id, (error, data, response) => {
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
 **id** | **String**| ID of the virtual machine. | 

### Return type

[**VmSnapshotSummaryListResponse**](VmSnapshotSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## querySnapshotsForVms

> BatchVmSnapshotSummaries querySnapshotsForVms(requestBody)

Get snapshot information for a list of virtual machines

Retrieve snapshot summaries for a list of virtual machines.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let requestBody = ["null"]; // [String] | IDs of the virtual machines.
apiInstance.querySnapshotsForVms(requestBody, (error, data, response) => {
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
 **requestBody** | [**[String]**](String.md)| IDs of the virtual machines. | 

### Return type

[**BatchVmSnapshotSummaries**](BatchVmSnapshotSummaries.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryVm

> VirtualMachineSummaryListResponse queryVm(opts)

Get list of VMs

Get summary of all the VMs.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let opts = {
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filter by ID of effective SLA Domain.
  'primaryClusterId': "primaryClusterId_example", // String | Filter by primary cluster ID, or **local**.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | Ignore these many matches in the beginning.
  'isRelic': true, // Boolean | Filter by the isRelic field of the virtual machine. When this parameter is not set, return both relic and non-relic virtual machines.
  'name': "name_example", // String | Search by using a virtual machine name.
  'moid': "moid_example", // String | Search by using a virtual machine managed object ID.
  'slaAssignment': "slaAssignment_example", // String | Filter by SLA Domain assignment type.
  'guestOsName': "guestOsName_example", // String | Filters by the name of operating system using infix search.
  'sortBy': "sortBy_example", // String | Sort results based on the specified attribute.
  'sortOrder': "sortOrder_example" // String | Sort order, either ascending or descending.
};
apiInstance.queryVm(opts, (error, data, response) => {
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
 **effectiveSlaDomainId** | **String**| Filter by ID of effective SLA Domain. | [optional] 
 **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] 
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| Ignore these many matches in the beginning. | [optional] 
 **isRelic** | **Boolean**| Filter by the isRelic field of the virtual machine. When this parameter is not set, return both relic and non-relic virtual machines. | [optional] 
 **name** | **String**| Search by using a virtual machine name. | [optional] 
 **moid** | **String**| Search by using a virtual machine managed object ID. | [optional] 
 **slaAssignment** | **String**| Filter by SLA Domain assignment type. | [optional] 
 **guestOsName** | **String**| Filters by the name of operating system using infix search. | [optional] 
 **sortBy** | **String**| Sort results based on the specified attribute. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] 

### Return type

[**VirtualMachineSummaryListResponse**](VirtualMachineSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## relocateMount

> AsyncRequestStatus relocateMount(id, relocateMountConfig)

Relocate a virtual machine to another datastore

Run storage VMotion to relocate a specified Live Mount into another data store.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of the live mount.
let relocateMountConfig = new RubrikRestApi.RelocateMountConfig(); // RelocateMountConfig | Configuration for the RelocateMount request to another data store.
apiInstance.relocateMount(id, relocateMountConfig, (error, data, response) => {
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
 **id** | **String**| ID of the live mount. | 
 **relocateMountConfig** | [**RelocateMountConfig**](RelocateMountConfig.md)| Configuration for the RelocateMount request to another data store. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## requestVmForceFullSnapshot

> VmForceFullResponse requestVmForceFullSnapshot(id, vmForceFullRequest)

Request a full snapshot for the next backup job of a VMware virtual machine

Request a full snapshot to be taken for the next backup job of a VMware virtual machine.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of the VMware virtual machine.
let vmForceFullRequest = new RubrikRestApi.VmForceFullRequest(); // VmForceFullRequest | Configuration for forcing a full snapshot on the VMware virtual machine.
apiInstance.requestVmForceFullSnapshot(id, vmForceFullRequest, (error, data, response) => {
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
 **id** | **String**| ID of the VMware virtual machine. | 
 **vmForceFullRequest** | [**VmForceFullRequest**](VmForceFullRequest.md)| Configuration for forcing a full snapshot on the VMware virtual machine. | 

### Return type

[**VmForceFullResponse**](VmForceFullResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## runGuestOsScript

> runGuestOsScript(id, vmGuestScriptRunConfig)

Run guest OS script

Run the specified preBackup, postSnap, or postBackup script in the guest OS of a virtual machine. The script must exist and meet requirements.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of the virtual machine.
let vmGuestScriptRunConfig = new RubrikRestApi.VmGuestScriptRunConfig(); // VmGuestScriptRunConfig | Configuration used to run the specified preBackup, postSnap, or postBackup guest OS script.
apiInstance.runGuestOsScript(id, vmGuestScriptRunConfig, (error, data, response) => {
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
 **id** | **String**| ID of the virtual machine. | 
 **vmGuestScriptRunConfig** | [**VmGuestScriptRunConfig**](VmGuestScriptRunConfig.md)| Configuration used to run the specified preBackup, postSnap, or postBackup guest OS script. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## searchVm

> SearchResponseListResponse searchVm(id, path, opts)

Search for a file from a VM

Search for a file in the snapshots of a a virtual machine. Specify the file by full path prefix or filename prefix.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of the virtual machine.
let path = "path_example"; // String | The path query. Use either a path prefix or a filename prefix.
let opts = {
  'limit': 56, // Number | Maximum number of entries in the response.
  'cursor': "cursor_example" // String | Pagination cursor returned by the previous request.
};
apiInstance.searchVm(id, path, opts, (error, data, response) => {
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
 **id** | **String**| ID of the virtual machine. | 
 **path** | **String**| The path query. Use either a path prefix or a filename prefix. | 
 **limit** | **Number**| Maximum number of entries in the response. | [optional] 
 **cursor** | **String**| Pagination cursor returned by the previous request. | [optional] 

### Return type

[**SearchResponseListResponse**](SearchResponseListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMount

> VmwareVmMountDetailV1 updateMount(id, updateMountConfig)

Power a Live Mount on and off

Power a specified Live Mount virtual machine on or off. Pass **_true_** to power the virtual machine on and pass **_false_** to power the virtual machine off.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of a Live Mount.
let updateMountConfig = new RubrikRestApi.UpdateMountConfig(); // UpdateMountConfig | Power state configuration.
apiInstance.updateMount(id, updateMountConfig, (error, data, response) => {
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
 **id** | **String**| ID of a Live Mount. | 
 **updateMountConfig** | [**UpdateMountConfig**](UpdateMountConfig.md)| Power state configuration. | 

### Return type

[**VmwareVmMountDetailV1**](VmwareVmMountDetailV1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVirtualDisk

> VirtualDiskDetail updateVirtualDisk(id, virtualDiskUpdate)

Update a specific Virtual Disk

Update a specific Virtual Disk.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of the Virtual Disk.
let virtualDiskUpdate = new RubrikRestApi.VirtualDiskUpdate(); // VirtualDiskUpdate | Virtual Disk update information.
apiInstance.updateVirtualDisk(id, virtualDiskUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the Virtual Disk. | 
 **virtualDiskUpdate** | [**VirtualDiskUpdate**](VirtualDiskUpdate.md)| Virtual Disk update information. | 

### Return type

[**VirtualDiskDetail**](VirtualDiskDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVm

> VirtualMachineDetail updateVm(id, virtualMachineUpdateWithSecret)

Update VM

Update a virtual machine with specified properties. Use the guestCredential field to update the guest credential for a specified virtual machine.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID of virtual machine.
let virtualMachineUpdateWithSecret = new RubrikRestApi.VirtualMachineUpdateWithSecret(); // VirtualMachineUpdateWithSecret | Properties to update.
apiInstance.updateVm(id, virtualMachineUpdateWithSecret, (error, data, response) => {
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
 **id** | **String**| ID of virtual machine. | 
 **virtualMachineUpdateWithSecret** | [**VirtualMachineUpdateWithSecret**](VirtualMachineUpdateWithSecret.md)| Properties to update. | 

### Return type

[**VirtualMachineDetail**](VirtualMachineDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## vmMakePrimary

> AsyncRequestStatus vmMakePrimary(requestBody)

Make this cluster the primary for agents on a set of VMs

Migrate the primary cluster with which the agent is able to communicate. For disaster recovery when migrating everything over from another cluster, the /host/make_primary endpoint can be used with the oldPrimaryClusterUuid parameter.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let requestBody = ["null"]; // [String] | IDs of hosts to migrate.
apiInstance.vmMakePrimary(requestBody, (error, data, response) => {
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
 **requestBody** | [**[String]**](String.md)| IDs of hosts to migrate. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## vmRegisterAgent

> vmRegisterAgent(id)

Register Rubrik Backup Service

Register the Rubrik Backup Service that is running on a specified host with the specified Rubrik cluster.

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

let apiInstance = new RubrikRestApi.VmwareVmApi();
let id = "id_example"; // String | ID assigned to a virtual machine object.
apiInstance.vmRegisterAgent(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to a virtual machine object. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

