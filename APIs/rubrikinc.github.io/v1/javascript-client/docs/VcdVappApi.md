# RubrikRestApi.VcdVappApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOnDemandSnapshotV1**](VcdVappApi.md#createOnDemandSnapshotV1) | **POST** /vcd/vapp/{id}/snapshot | Create an on-demand snapshot for a vApp
[**createVappExportV1**](VcdVappApi.md#createVappExportV1) | **POST** /vcd/vapp/snapshot/{snapshot_id}/export | Export vApp snapshot
[**createVappInstantRecoveryV1**](VcdVappApi.md#createVappInstantRecoveryV1) | **POST** /vcd/vapp/snapshot/{snapshot_id}/instant_recover | Instant Recovery of vApp virtual machines
[**createVappTemplateSnapshotExport**](VcdVappApi.md#createVappTemplateSnapshotExport) | **POST** /vcd/vapp/template/snapshot/{snapshot_id}/export | Export of a vApp template snapshot
[**createVcdVappDownloadSnapshotFromCloudV1**](VcdVappApi.md#createVcdVappDownloadSnapshotFromCloudV1) | **POST** /vcd/vapp/snapshot/{id}/download | Download snapshot from archive
[**deleteVappSnapshotV1**](VcdVappApi.md#deleteVappSnapshotV1) | **DELETE** /vcd/vapp/snapshot/{id} | Delete a vApp snapshot
[**deleteVappSnapshotsV1**](VcdVappApi.md#deleteVappSnapshotsV1) | **DELETE** /vcd/vapp/{id}/snapshot | Delete all snapshots of vApp
[**getVappAsyncRequestStatusV1**](VcdVappApi.md#getVappAsyncRequestStatusV1) | **GET** /vcd/vapp/request/{id} | Get vApp job status
[**getVappSnapshotExportOptionsV1**](VcdVappApi.md#getVappSnapshotExportOptionsV1) | **GET** /vcd/vapp/snapshot/{snapshot_id}/export/options | Get exportable network configurations
[**getVappSnapshotInstantRecoveryOptionsV1**](VcdVappApi.md#getVappSnapshotInstantRecoveryOptionsV1) | **GET** /vcd/vapp/snapshot/{snapshot_id}/instant_recover/options | Get Instant Recovery information
[**getVappSnapshotV1**](VcdVappApi.md#getVappSnapshotV1) | **GET** /vcd/vapp/snapshot/{id} | Get vApp snapshot details
[**getVappTemplateSnapshotExportOptions**](VcdVappApi.md#getVappTemplateSnapshotExportOptions) | **GET** /vcd/vapp/template/snapshot/{snapshot_id}/export/options | Get Export information for a vApp template snapshot
[**getVcdVappV1**](VcdVappApi.md#getVcdVappV1) | **GET** /vcd/vapp/{id} | Get details of a specific vApp
[**queryVappSnapshotV1**](VcdVappApi.md#queryVappSnapshotV1) | **GET** /vcd/vapp/{id}/snapshot | Get list of snapshots of vApp
[**queryVcdVappsV1**](VcdVappApi.md#queryVcdVappsV1) | **GET** /vcd/vapp | Get summary for vApps
[**searchVappV1**](VcdVappApi.md#searchVappV1) | **GET** /vcd/vapp/{id}/search | Search for a file in a vApp
[**updateVcdVappV1**](VcdVappApi.md#updateVcdVappV1) | **PATCH** /vcd/vapp/{id} | Update vApp
[**vcdMissedSnapshotsV1**](VcdVappApi.md#vcdMissedSnapshotsV1) | **GET** /vcd/vapp/{id}/missed_snapshot | Get details about missed snapshots for a vApp



## createOnDemandSnapshotV1

> AsyncRequestStatus createOnDemandSnapshotV1(id, opts)

Create an on-demand snapshot for a vApp

Start an asynchronous job to create an on-demand snapshot for a specified vApp object.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let id = "id_example"; // String | ID assigned to a vApp object.
let opts = {
  'baseOnDemandSnapshotConfig': new RubrikRestApi.BaseOnDemandSnapshotConfig() // BaseOnDemandSnapshotConfig | Configuration for the on-demand backup of a specified vApp object.
};
apiInstance.createOnDemandSnapshotV1(id, opts, (error, data, response) => {
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
 **id** | **String**| ID assigned to a vApp object. | 
 **baseOnDemandSnapshotConfig** | [**BaseOnDemandSnapshotConfig**](BaseOnDemandSnapshotConfig.md)| Configuration for the on-demand backup of a specified vApp object. | [optional] 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVappExportV1

> AsyncRequestStatus createVappExportV1(snapshotId, vappExportSnapshotJobConfig)

Export vApp snapshot

Export the specified vApp snapshot into a new vApp or an existing vApp.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let snapshotId = "snapshotId_example"; // String | ID assigned to the vApp snapshot object.
let vappExportSnapshotJobConfig = new RubrikRestApi.VappExportSnapshotJobConfig(); // VappExportSnapshotJobConfig | Configuration for the request to export the specified vApp snapshot.
apiInstance.createVappExportV1(snapshotId, vappExportSnapshotJobConfig, (error, data, response) => {
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
 **snapshotId** | **String**| ID assigned to the vApp snapshot object. | 
 **vappExportSnapshotJobConfig** | [**VappExportSnapshotJobConfig**](VappExportSnapshotJobConfig.md)| Configuration for the request to export the specified vApp snapshot. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVappInstantRecoveryV1

> AsyncRequestStatus createVappInstantRecoveryV1(snapshotId, vappInstantRecoveryJobConfig)

Instant Recovery of vApp virtual machines

Use Instant Recovery to recover specified vApp virtual machines.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let snapshotId = "snapshotId_example"; // String | ID assigned to the vApp snapshot object.
let vappInstantRecoveryJobConfig = new RubrikRestApi.VappInstantRecoveryJobConfig(); // VappInstantRecoveryJobConfig | Configuration for a request to recover specified virtual machines from a vApp snapshot.
apiInstance.createVappInstantRecoveryV1(snapshotId, vappInstantRecoveryJobConfig, (error, data, response) => {
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
 **snapshotId** | **String**| ID assigned to the vApp snapshot object. | 
 **vappInstantRecoveryJobConfig** | [**VappInstantRecoveryJobConfig**](VappInstantRecoveryJobConfig.md)| Configuration for a request to recover specified virtual machines from a vApp snapshot. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVappTemplateSnapshotExport

> AsyncRequestStatus createVappTemplateSnapshotExport(snapshotId, vappTemplateExportJobConfig)

Export of a vApp template snapshot

Export a vApp template snapashot to a catalog. Use the options endpoint to confirm that exporting to the catalog defaults or the original organization vDC storage profile is possible.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let snapshotId = "snapshotId_example"; // String | ID assigned to a vApp snapshot object.
let vappTemplateExportJobConfig = new RubrikRestApi.VappTemplateExportJobConfig(); // VappTemplateExportJobConfig | Configuration for a request to export a vApp template snapshot to a specific catalog.
apiInstance.createVappTemplateSnapshotExport(snapshotId, vappTemplateExportJobConfig, (error, data, response) => {
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
 **snapshotId** | **String**| ID assigned to a vApp snapshot object. | 
 **vappTemplateExportJobConfig** | [**VappTemplateExportJobConfig**](VappTemplateExportJobConfig.md)| Configuration for a request to export a vApp template snapshot to a specific catalog. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVcdVappDownloadSnapshotFromCloudV1

> AsyncRequestStatus createVcdVappDownloadSnapshotFromCloudV1(id)

Download snapshot from archive

Provides a method for retrieving a snapshot that is not available locally, from an archival location.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let id = "id_example"; // String | ID of snapshot.
apiInstance.createVcdVappDownloadSnapshotFromCloudV1(id, (error, data, response) => {
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


## deleteVappSnapshotV1

> deleteVappSnapshotV1(id, location)

Delete a vApp snapshot

Designate a vApp snapshot as expired and available for garbage collection. The snapshot must be an on-demand snapshot or a snapshot from a vApp that is not assigned to an SLA Domain.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let id = "id_example"; // String | ID assigned to a snapshot object.
let location = "location_example"; // String | Location of the snapshot to delete. Use _local_ to delete only the local copy of the snapshot. Use _all_ to delete the snapshot locally, on a replication target, and at an archival location.
apiInstance.deleteVappSnapshotV1(id, location, (error, data, response) => {
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
 **id** | **String**| ID assigned to a snapshot object. | 
 **location** | **String**| Location of the snapshot to delete. Use _local_ to delete only the local copy of the snapshot. Use _all_ to delete the snapshot locally, on a replication target, and at an archival location. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteVappSnapshotsV1

> deleteVappSnapshotsV1(id)

Delete all snapshots of vApp

Delete all snapshots for a specified vApp object.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let id = "id_example"; // String | ID assigned to a vApp object.
apiInstance.deleteVappSnapshotsV1(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to a vApp object. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVappAsyncRequestStatusV1

> AsyncRequestStatus getVappAsyncRequestStatusV1(id)

Get vApp job status

Retrieve the details of a specified asynchronous job for a vApp.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let id = "id_example"; // String | ID assigned to an asynchronous job.
apiInstance.getVappAsyncRequestStatusV1(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to an asynchronous job. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVappSnapshotExportOptionsV1

> VappExportOptions getVappSnapshotExportOptionsV1(snapshotId, exportMode, opts)

Get exportable network configurations

Retrieve summary information for the vApp networks that are available for network connections from the virtual machines in the exported vApp snapshot. The summary also specifies the default vApp network for each virtual machine network connection.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let snapshotId = "snapshotId_example"; // String | ID assigned to the vApp snapshot object to export.
let exportMode = "exportMode_example"; // String | Target type for the specified vApp export.
let opts = {
  'targetVappId': "targetVappId_example", // String | ID assigned to the target vApp object, when the export is into an existing vApp. When the export is not into a target vApp, remove the 'target_vapp_id' member.
  'targetOrgVdcId': "targetOrgVdcId_example" // String | ID assigned to a target organization VDC object. Use the ID when exporting a vApp snapshot to create a new vApp on the specified target organization VDC. When the exported vApp snapshot is not used to create a new vApp on a target organization VDC, remove the 'target_org_vdc_id' member.
};
apiInstance.getVappSnapshotExportOptionsV1(snapshotId, exportMode, opts, (error, data, response) => {
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
 **snapshotId** | **String**| ID assigned to the vApp snapshot object to export. | 
 **exportMode** | **String**| Target type for the specified vApp export. | 
 **targetVappId** | **String**| ID assigned to the target vApp object, when the export is into an existing vApp. When the export is not into a target vApp, remove the &#39;target_vapp_id&#39; member. | [optional] 
 **targetOrgVdcId** | **String**| ID assigned to a target organization VDC object. Use the ID when exporting a vApp snapshot to create a new vApp on the specified target organization VDC. When the exported vApp snapshot is not used to create a new vApp on a target organization VDC, remove the &#39;target_org_vdc_id&#39; member. | [optional] 

### Return type

[**VappExportOptions**](VappExportOptions.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVappSnapshotInstantRecoveryOptionsV1

> VappInstantRecoveryOptions getVappSnapshotInstantRecoveryOptionsV1(snapshotId)

Get Instant Recovery information

Retrieve the available vApp network connections and the default vApp network connection for the virtual machines in a vApp snapshot. Use this information to configure an Instant Recovery of specified virtual machines in the vApp snapshot.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let snapshotId = "snapshotId_example"; // String | ID assigned to a vApp snapshot object.
apiInstance.getVappSnapshotInstantRecoveryOptionsV1(snapshotId, (error, data, response) => {
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
 **snapshotId** | **String**| ID assigned to a vApp snapshot object. | 

### Return type

[**VappInstantRecoveryOptions**](VappInstantRecoveryOptions.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVappSnapshotV1

> VcdVappSnapshotDetail getVappSnapshotV1(id)

Get vApp snapshot details

Retrieve detailed information about a specified snapshot for a vApp object.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let id = "id_example"; // String | ID assigned to a snapshot object.
apiInstance.getVappSnapshotV1(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to a snapshot object. | 

### Return type

[**VcdVappSnapshotDetail**](VcdVappSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVappTemplateSnapshotExportOptions

> VappTemplateExportOptionsUnion getVappTemplateSnapshotExportOptions(snapshotId, catalogId, name, opts)

Get Export information for a vApp template snapshot

Retrieve the available choices vApp template storage profile and organization vDC choices in case of exporting to either original organization vDC defaults of the target catalog. In case advanced option of manually deciding org vdc is preferred, this also provides available storage profile choices.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let snapshotId = "snapshotId_example"; // String | ID assigned to a vApp snapshot object.
let catalogId = "catalogId_example"; // String | ID of the target catalog object.
let name = "name_example"; // String | Name of template object to create. This is used to verify the existence of a template with the given name. Templates must have unique names.
let opts = {
  'orgVdcId': "orgVdcId_example" // String | ID assigned to a target organization vDC object. Use the ID when exporting a vApp template snapshot to a specified organization VDC. This ID is used to fetch the avaiable choices to pick the storage profile of the template. Leave this field empty to use the options from the original organization vDC or the target catalog defaults.
};
apiInstance.getVappTemplateSnapshotExportOptions(snapshotId, catalogId, name, opts, (error, data, response) => {
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
 **snapshotId** | **String**| ID assigned to a vApp snapshot object. | 
 **catalogId** | **String**| ID of the target catalog object. | 
 **name** | **String**| Name of template object to create. This is used to verify the existence of a template with the given name. Templates must have unique names. | 
 **orgVdcId** | **String**| ID assigned to a target organization vDC object. Use the ID when exporting a vApp template snapshot to a specified organization VDC. This ID is used to fetch the avaiable choices to pick the storage profile of the template. Leave this field empty to use the options from the original organization vDC or the target catalog defaults. | [optional] 

### Return type

[**VappTemplateExportOptionsUnion**](VappTemplateExportOptionsUnion.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVcdVappV1

> VcdVappDetail getVcdVappV1(id)

Get details of a specific vApp

Retrieve detailed information for a specified vApp.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let id = "id_example"; // String | ID assigned to a vApp object.
apiInstance.getVcdVappV1(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to a vApp object. | 

### Return type

[**VcdVappDetail**](VcdVappDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryVappSnapshotV1

> VcdVappSnapshotSummaryListResponse queryVappSnapshotV1(id)

Get list of snapshots of vApp

Retrieve summary information for each of the snapshot objects of a specified vApp object.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let id = "id_example"; // String | ID assigned to a vApp object.
apiInstance.queryVappSnapshotV1(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to a vApp object. | 

### Return type

[**VcdVappSnapshotSummaryListResponse**](VcdVappSnapshotSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryVcdVappsV1

> VcdVappSummaryListResponse queryVcdVappsV1(opts)

Get summary for vApps

Retrieve summary information for all vCD vApp objects.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let opts = {
  'sortBy': "sortBy_example", // String | Attribute to sort the vCD vApp list on.
  'sortOrder': "'asc'", // String | Order for sorting the results, either ascending or descending.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | Number of matches to ignore from the beginning of the results.
  'name': "name_example", // String | Search for a vCD vApp object by name.
  'isRelic': true, // Boolean | Filter by isRelic field of vCD vApp object. Return both relic and non-relic vApps when this value is not specified.
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filter by ID of the effective SLA domain.
  'primaryClusterId': "primaryClusterId_example", // String | Filter by primary cluster ID, or **local**.
  'slaAssignment': "slaAssignment_example", // String | Filter by SLA assignment type.
  'includeBackupTaskInfo': false // Boolean | Include backup task information in response.
};
apiInstance.queryVcdVappsV1(opts, (error, data, response) => {
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
 **sortBy** | **String**| Attribute to sort the vCD vApp list on. | [optional] 
 **sortOrder** | **String**| Order for sorting the results, either ascending or descending. | [optional] [default to &#39;asc&#39;]
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| Number of matches to ignore from the beginning of the results. | [optional] 
 **name** | **String**| Search for a vCD vApp object by name. | [optional] 
 **isRelic** | **Boolean**| Filter by isRelic field of vCD vApp object. Return both relic and non-relic vApps when this value is not specified. | [optional] 
 **effectiveSlaDomainId** | **String**| Filter by ID of the effective SLA domain. | [optional] 
 **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] 
 **slaAssignment** | **String**| Filter by SLA assignment type. | [optional] 
 **includeBackupTaskInfo** | **Boolean**| Include backup task information in response. | [optional] [default to false]

### Return type

[**VcdVappSummaryListResponse**](VcdVappSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchVappV1

> AppSearchResponseListResponse searchVappV1(id, path)

Search for a file in a vApp

Aggregated search for a file through snapshots of all virtual machines that are presently part of the vApp. Specify the file using a full path prefix or a filename prefix.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let id = "id_example"; // String | ID of the vApp.
let path = "path_example"; // String | The path query. Use either a path prefix or a filename prefix.
apiInstance.searchVappV1(id, path, (error, data, response) => {
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
 **id** | **String**| ID of the vApp. | 
 **path** | **String**| The path query. Use either a path prefix or a filename prefix. | 

### Return type

[**AppSearchResponseListResponse**](AppSearchResponseListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateVcdVappV1

> VcdVappDetail updateVcdVappV1(id, vcdVappPatch)

Update vApp

Make changes to the parameters of a specified vApp object.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let id = "id_example"; // String | ID assigned to a vApp object.
let vcdVappPatch = new RubrikRestApi.VcdVappPatch(); // VcdVappPatch | Parameters to use to update the specified vApp object.
apiInstance.updateVcdVappV1(id, vcdVappPatch, (error, data, response) => {
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
 **id** | **String**| ID assigned to a vApp object. | 
 **vcdVappPatch** | [**VcdVappPatch**](VcdVappPatch.md)| Parameters to use to update the specified vApp object. | 

### Return type

[**VcdVappDetail**](VcdVappDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## vcdMissedSnapshotsV1

> MissedSnapshotListResponse vcdMissedSnapshotsV1(id)

Get details about missed snapshots for a vApp

Retrieve the timestamp for each missed snapshot for a specified vApp.

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

let apiInstance = new RubrikRestApi.VcdVappApi();
let id = "id_example"; // String | ID of the vApp.
apiInstance.vcdMissedSnapshotsV1(id, (error, data, response) => {
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
 **id** | **String**| ID of the vApp. | 

### Return type

[**MissedSnapshotListResponse**](MissedSnapshotListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

