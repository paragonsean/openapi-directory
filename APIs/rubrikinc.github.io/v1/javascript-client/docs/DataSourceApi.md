# RubrikRestApi.DataSourceApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkDeleteSnapshots**](DataSourceApi.md#bulkDeleteSnapshots) | **POST** /data_source/snapshot/bulk_delete | Bulk delete all snapshots for the given objects
[**bulkDeleteSnapshotsForObject**](DataSourceApi.md#bulkDeleteSnapshotsForObject) | **POST** /data_source/{id}/snapshot/bulk_delete | Bulk delete specified snapshots for the given object
[**expiredCustomRetentionSnapshots**](DataSourceApi.md#expiredCustomRetentionSnapshots) | **GET** /data_source/{id}/expired_custom_retention_snapshots | Returns a list of snapshots that have expired according to their snapshot-level SLA Domain assignments 



## bulkDeleteSnapshots

> bulkDeleteSnapshots(bulkDeleteSnapshotsConfig)

Bulk delete all snapshots for the given objects

This endpoint deletes all snapshots from all locations for the objects with the IDs specified by the &#39;objectIds&#39; parameter. API returning success does not guarantee that the snapshots will be expired. 

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

let apiInstance = new RubrikRestApi.DataSourceApi();
let bulkDeleteSnapshotsConfig = new RubrikRestApi.BulkDeleteSnapshotsConfig(); // BulkDeleteSnapshotsConfig | A list of object IDs. 
apiInstance.bulkDeleteSnapshots(bulkDeleteSnapshotsConfig, (error, data, response) => {
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
 **bulkDeleteSnapshotsConfig** | [**BulkDeleteSnapshotsConfig**](BulkDeleteSnapshotsConfig.md)| A list of object IDs.  | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bulkDeleteSnapshotsForObject

> bulkDeleteSnapshotsForObject(id, bulkDeleteObjectSnapshotsConfig)

Bulk delete specified snapshots for the given object

Bulk deletion of the snapshots specified by a list of snapshot IDs for a given object. Object type is required. Location ID is optional. API returning success does not guarantee that the snapshot will be expired. 

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

let apiInstance = new RubrikRestApi.DataSourceApi();
let id = "id_example"; // String | ID of the object.
let bulkDeleteObjectSnapshotsConfig = new RubrikRestApi.BulkDeleteObjectSnapshotsConfig(); // BulkDeleteObjectSnapshotsConfig | A list of snapshot IDs specifying snapshots to delete. Optionally specifies a location ID. Snapshot deletion is global when the location ID is absent. 
apiInstance.bulkDeleteSnapshotsForObject(id, bulkDeleteObjectSnapshotsConfig, (error, data, response) => {
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
 **id** | **String**| ID of the object. | 
 **bulkDeleteObjectSnapshotsConfig** | [**BulkDeleteObjectSnapshotsConfig**](BulkDeleteObjectSnapshotsConfig.md)| A list of snapshot IDs specifying snapshots to delete. Optionally specifies a location ID. Snapshot deletion is global when the location ID is absent.  | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## expiredCustomRetentionSnapshots

> ExpiredCustomRetentionSnapshots expiredCustomRetentionSnapshots(id)

Returns a list of snapshots that have expired according to their snapshot-level SLA Domain assignments 

Gets a list of the snapshots of a specified data source that have expired according to the snapshot-level SLA Domain assignments. This list does not include remote snapshots. 

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

let apiInstance = new RubrikRestApi.DataSourceApi();
let id = "id_example"; // String | The object ID.
apiInstance.expiredCustomRetentionSnapshots(id, (error, data, response) => {
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
 **id** | **String**| The object ID. | 

### Return type

[**ExpiredCustomRetentionSnapshots**](ExpiredCustomRetentionSnapshots.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

