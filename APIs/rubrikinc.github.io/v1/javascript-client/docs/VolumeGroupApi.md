# RubrikRestApi.VolumeGroupApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOnDemandVolumeGroupBackup**](VolumeGroupApi.md#createOnDemandVolumeGroupBackup) | **POST** /volume_group/{id}/snapshot | Create on-demand snapshot for the Volume Group
[**getVolumeGroup**](VolumeGroupApi.md#getVolumeGroup) | **GET** /volume_group/{id} | Get Volume Group details
[**getVolumeGroupForceFullSpec**](VolumeGroupApi.md#getVolumeGroupForceFullSpec) | **GET** /volume_group/{id}/request/force_full_snapshot | Retrieve the configuration for forcing a full snapshot
[**getVolumeGroupSnapshot**](VolumeGroupApi.md#getVolumeGroupSnapshot) | **GET** /volume_group/snapshot/{id} | Get Volume Group snapshot details
[**getVolumeGroupSnapshotMount**](VolumeGroupApi.md#getVolumeGroupSnapshotMount) | **GET** /volume_group/snapshot/mount/{id} | Get summary information for a mount
[**patchVolumeGroup**](VolumeGroupApi.md#patchVolumeGroup) | **PATCH** /volume_group/{id} | Update Volume Group properties
[**queryVolumeGroup**](VolumeGroupApi.md#queryVolumeGroup) | **GET** /volume_group | Get list of Volume Groups
[**queryVolumeGroupLatestSnapshot**](VolumeGroupApi.md#queryVolumeGroupLatestSnapshot) | **GET** /volume_group/{id}/latest_snapshot | Get the latest snapshot of the Volume Group
[**queryVolumeGroupSnapshot**](VolumeGroupApi.md#queryVolumeGroupSnapshot) | **GET** /volume_group/{id}/snapshot | Get list of snapshots of the Volume Group
[**queryVolumeGroupSnapshotMount**](VolumeGroupApi.md#queryVolumeGroupSnapshotMount) | **GET** /volume_group/snapshot/mount | Get summary information for all mounts
[**requestVolumeGroupForceFullSnapshot**](VolumeGroupApi.md#requestVolumeGroupForceFullSnapshot) | **POST** /volume_group/{id}/request/force_full_snapshot | Request a full snapshot on the next backup job of a Volume Group



## createOnDemandVolumeGroupBackup

> AsyncRequestStatus createOnDemandVolumeGroupBackup(id, opts)

Create on-demand snapshot for the Volume Group

Create an on-demand snapshot for the given Volume Group ID.

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

let apiInstance = new RubrikRestApi.VolumeGroupApi();
let id = "id_example"; // String | The ID of the Volume Group.
let opts = {
  'volumeGroupOnDemandSnapshotConfig': new RubrikRestApi.VolumeGroupOnDemandSnapshotConfig() // VolumeGroupOnDemandSnapshotConfig | Configuration for the on-demand backup. Configuration values are `volumeIdsIncludedInSnapshot`, which specifies the unique ID of each volume that is part of this snapshot of the Volume Group, and `slaID`, the ID of the SLA Domain for the snapshot.
};
apiInstance.createOnDemandVolumeGroupBackup(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the Volume Group. | 
 **volumeGroupOnDemandSnapshotConfig** | [**VolumeGroupOnDemandSnapshotConfig**](VolumeGroupOnDemandSnapshotConfig.md)| Configuration for the on-demand backup. Configuration values are &#x60;volumeIdsIncludedInSnapshot&#x60;, which specifies the unique ID of each volume that is part of this snapshot of the Volume Group, and &#x60;slaID&#x60;, the ID of the SLA Domain for the snapshot. | [optional] 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getVolumeGroup

> VolumeGroupDetail getVolumeGroup(id)

Get Volume Group details

Detailed view of a Volume Group.

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

let apiInstance = new RubrikRestApi.VolumeGroupApi();
let id = "id_example"; // String | The ID of the Volume Group.
apiInstance.getVolumeGroup(id, (error, data, response) => {
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
 **id** | **String**| The ID of the Volume Group. | 

### Return type

[**VolumeGroupDetail**](VolumeGroupDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVolumeGroupForceFullSpec

> VolumeGroupForceFullResponse getVolumeGroupForceFullSpec(id)

Retrieve the configuration for forcing a full snapshot

Retrieve the configuration for forcing a full snapshot for a Volume Group.

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

let apiInstance = new RubrikRestApi.VolumeGroupApi();
let id = "id_example"; // String | The ID of the Volume Group.
apiInstance.getVolumeGroupForceFullSpec(id, (error, data, response) => {
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
 **id** | **String**| The ID of the Volume Group. | 

### Return type

[**VolumeGroupForceFullResponse**](VolumeGroupForceFullResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVolumeGroupSnapshot

> VolumeGroupSnapshotDetail getVolumeGroupSnapshot(id)

Get Volume Group snapshot details

Retrieve detailed information about a snapshot.

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

let apiInstance = new RubrikRestApi.VolumeGroupApi();
let id = "id_example"; // String | The ID of the Volume Group snapshot.
apiInstance.getVolumeGroupSnapshot(id, (error, data, response) => {
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
 **id** | **String**| The ID of the Volume Group snapshot. | 

### Return type

[**VolumeGroupSnapshotDetail**](VolumeGroupSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVolumeGroupSnapshotMount

> VolumeGroupMountSummary getVolumeGroupSnapshotMount(id)

Get summary information for a mount

Retrieve information on a Volume Group mount. The information returned includes the following items, when available. id (the unique ID of the mount), name (the name of the Volume Group), snapshotDate (the snapshot date), sourceVolumeGroupId (The ID of the Volume Group from which this snapshot was created), sourceHostId (the ID of the source host), sourceHostName (the name of the source host), mountedDate (the date when the mount was created), mountedVolumes (the mounted volumes information), targetHostId (the ID of the mounted volumes host), targetHostName (the name of the mounted volumes host), mountRequestId (the ID of the job instance that initiated the mount), unmountRequestId (the ID of the job instance that intiated the request to remove the mount), isReady (whether the Volume Group mount is ready to use), and restoreScriptSmbPath (the link to the script that can perform bare-metal recovery).

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

let apiInstance = new RubrikRestApi.VolumeGroupApi();
let id = "id_example"; // String | The ID of the Volume Group mount.
apiInstance.getVolumeGroupSnapshotMount(id, (error, data, response) => {
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
 **id** | **String**| The ID of the Volume Group mount. | 

### Return type

[**VolumeGroupMountSummary**](VolumeGroupMountSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchVolumeGroup

> VolumeGroupDetail patchVolumeGroup(id, volumeGroupPatch)

Update Volume Group properties

Patch Volume Group with specified properties.

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

let apiInstance = new RubrikRestApi.VolumeGroupApi();
let id = "id_example"; // String | The ID of Volume Group.
let volumeGroupPatch = new RubrikRestApi.VolumeGroupPatch(); // VolumeGroupPatch | Properties to update for this Volume Group.
apiInstance.patchVolumeGroup(id, volumeGroupPatch, (error, data, response) => {
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
 **id** | **String**| The ID of Volume Group. | 
 **volumeGroupPatch** | [**VolumeGroupPatch**](VolumeGroupPatch.md)| Properties to update for this Volume Group. | 

### Return type

[**VolumeGroupDetail**](VolumeGroupDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryVolumeGroup

> VolumeGroupSummaryListResponse queryVolumeGroup(opts)

Get list of Volume Groups

Get summary of all Volume Groups.

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

let apiInstance = new RubrikRestApi.VolumeGroupApi();
let opts = {
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | The ID of the SLA Domain that controls the protection of the Volume Group.
  'primaryClusterId': "primaryClusterId_example", // String | The ID of the Rubrik cluster that provides primary protection for the Volume Group.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | Ignore these many matches in the beginning.
  'isRelic': true, // Boolean | Specifies whether the results should contain only Volume Groups that are accessible on the Rubrik cluster.
  'name': "name_example", // String | The name of the Volume Group.
  'slaAssignment': "slaAssignment_example", // String | The type of SLA assigned to the Volume Group.
  'sortBy': "'name'", // String | The Volume Group attribute to use in storing the responses. Valid attributes are `name` and `effectiveSlaDomainName`.
  'sortOrder': "'asc'" // String | The order to sort the responses. Valid choices are asc (ascending) or desc (descending).
};
apiInstance.queryVolumeGroup(opts, (error, data, response) => {
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
 **effectiveSlaDomainId** | **String**| The ID of the SLA Domain that controls the protection of the Volume Group. | [optional] 
 **primaryClusterId** | **String**| The ID of the Rubrik cluster that provides primary protection for the Volume Group. | [optional] 
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| Ignore these many matches in the beginning. | [optional] 
 **isRelic** | **Boolean**| Specifies whether the results should contain only Volume Groups that are accessible on the Rubrik cluster. | [optional] 
 **name** | **String**| The name of the Volume Group. | [optional] 
 **slaAssignment** | **String**| The type of SLA assigned to the Volume Group. | [optional] 
 **sortBy** | **String**| The Volume Group attribute to use in storing the responses. Valid attributes are &#x60;name&#x60; and &#x60;effectiveSlaDomainName&#x60;. | [optional] [default to &#39;name&#39;]
 **sortOrder** | **String**| The order to sort the responses. Valid choices are asc (ascending) or desc (descending). | [optional] [default to &#39;asc&#39;]

### Return type

[**VolumeGroupSummaryListResponse**](VolumeGroupSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryVolumeGroupLatestSnapshot

> [VolumeGroupSnapshotSummary] queryVolumeGroupLatestSnapshot(id)

Get the latest snapshot of the Volume Group

Retrieve the latest snapshot summary of a Volume Group.

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

let apiInstance = new RubrikRestApi.VolumeGroupApi();
let id = "id_example"; // String | ID of the Volume Group.
apiInstance.queryVolumeGroupLatestSnapshot(id, (error, data, response) => {
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
 **id** | **String**| ID of the Volume Group. | 

### Return type

[**[VolumeGroupSnapshotSummary]**](VolumeGroupSnapshotSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryVolumeGroupSnapshot

> VolumeGroupSnapshotSummaryListResponse queryVolumeGroupSnapshot(id)

Get list of snapshots of the Volume Group

Retrieve snapshot details for a Volume Group.

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

let apiInstance = new RubrikRestApi.VolumeGroupApi();
let id = "id_example"; // String | The ID of the Volume Group.
apiInstance.queryVolumeGroupSnapshot(id, (error, data, response) => {
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
 **id** | **String**| The ID of the Volume Group. | 

### Return type

[**VolumeGroupSnapshotSummaryListResponse**](VolumeGroupSnapshotSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryVolumeGroupSnapshotMount

> VolumeGroupMountSummaryListResponse queryVolumeGroupSnapshotMount(opts)

Get summary information for all mounts

Retrieves information for each Volume Group mount. The information returned includes the following items, when available. id (the unique ID of the mount), name (the name of the Volume Group), snapshotDate (the snapshot date), sourceVolumeGroupId (the ID of the Volume Group from which this snapshot was created), sourceHostId (the ID of the source host), sourceHostName (the name of the source host), mountedDate (the date when the mount was created), mountedVolumes (information on the mounted volumes), targetHostId (the ID of the mounted volumes host), targetHostName (the name of the mounted volumes host), mountRequestId (the ID of the job instance that initiated the mount), unmountRequestId (the ID of the job instance that initiated the request to remove the mount), isReady (whether the Volume Group mount is ready to use), and restoreScriptSmbPath (the link to the script that can perform bare-metal recovery).

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

let apiInstance = new RubrikRestApi.VolumeGroupApi();
let opts = {
  'sourceVolumeGroupId': "sourceVolumeGroupId_example", // String | The ID of the source Volume Group.
  'sourceHostName': "sourceHostName_example", // String | A prefix of the source host name. The prefix is used as a response filter when available.
  'sortBy': "sortBy_example", // String | The Volume Group mount attribute used in sorting the responses. Valid choices are name, sourceHostName, snapshotDate, and mountedDate.
  'sortOrder': "'asc'", // String | The order to sort the responses. Valid choices are asc (ascending) or desc (descending).
  'offset': 56, // Number | Ignore these many matches in the beginning.
  'limit': 56 // Number | Limit the number of matches returned. The default value is 25.
};
apiInstance.queryVolumeGroupSnapshotMount(opts, (error, data, response) => {
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
 **sourceVolumeGroupId** | **String**| The ID of the source Volume Group. | [optional] 
 **sourceHostName** | **String**| A prefix of the source host name. The prefix is used as a response filter when available. | [optional] 
 **sortBy** | **String**| The Volume Group mount attribute used in sorting the responses. Valid choices are name, sourceHostName, snapshotDate, and mountedDate. | [optional] 
 **sortOrder** | **String**| The order to sort the responses. Valid choices are asc (ascending) or desc (descending). | [optional] [default to &#39;asc&#39;]
 **offset** | **Number**| Ignore these many matches in the beginning. | [optional] 
 **limit** | **Number**| Limit the number of matches returned. The default value is 25. | [optional] 

### Return type

[**VolumeGroupMountSummaryListResponse**](VolumeGroupMountSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestVolumeGroupForceFullSnapshot

> VolumeGroupForceFullResponse requestVolumeGroupForceFullSnapshot(id, volumeGroupForceFullRequest)

Request a full snapshot on the next backup job of a Volume Group

Request a full snapshot to be taken during the next backup job of a Volume Group.

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

let apiInstance = new RubrikRestApi.VolumeGroupApi();
let id = "id_example"; // String | The ID of the Volume Group.
let volumeGroupForceFullRequest = new RubrikRestApi.VolumeGroupForceFullRequest(); // VolumeGroupForceFullRequest | Configuration for forcing a full snapshot on the Volume Group.
apiInstance.requestVolumeGroupForceFullSnapshot(id, volumeGroupForceFullRequest, (error, data, response) => {
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
 **id** | **String**| The ID of the Volume Group. | 
 **volumeGroupForceFullRequest** | [**VolumeGroupForceFullRequest**](VolumeGroupForceFullRequest.md)| Configuration for forcing a full snapshot on the Volume Group. | 

### Return type

[**VolumeGroupForceFullResponse**](VolumeGroupForceFullResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

