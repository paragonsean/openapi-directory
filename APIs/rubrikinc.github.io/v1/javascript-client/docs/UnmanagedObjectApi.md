# RubrikRestApi.UnmanagedObjectApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignToRetentionSlaAsync**](UnmanagedObjectApi.md#assignToRetentionSlaAsync) | **POST** /unmanaged_object/assign_retention_sla | Assign relic/unmanaged entities to an SLA Domain for managing retention asynchronously
[**bulkTierExistingSnapshots**](UnmanagedObjectApi.md#bulkTierExistingSnapshots) | **POST** /unmanaged_object/snapshot/bulk_archive_tier | Bulk tier existing snapshots to cold storage
[**queryUnmanagedObjectSnapshotsV1**](UnmanagedObjectApi.md#queryUnmanagedObjectSnapshotsV1) | **GET** /unmanaged_object/{id}/snapshot | Get summary of all the snapshots for a given object
[**queryUnmanagedObjectV1**](UnmanagedObjectApi.md#queryUnmanagedObjectV1) | **GET** /unmanaged_object | Get summary of all the objects with unmanaged snapshots
[**queryUnmanagedReaderObject**](UnmanagedObjectApi.md#queryUnmanagedReaderObject) | **GET** /unmanaged_object/reader_object | Get summary of all unmanaged reader objects



## assignToRetentionSlaAsync

> [ManagedObjectPendingSlaInfo] assignToRetentionSlaAsync(unmanagedObjectSlaAssignmentInfo)

Assign relic/unmanaged entities to an SLA Domain for managing retention asynchronously

Assign relic/unmanaged entities to the specified SLA Domain for managing retention. The assignment event runs asynchronously.

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

let apiInstance = new RubrikRestApi.UnmanagedObjectApi();
let unmanagedObjectSlaAssignmentInfo = new RubrikRestApi.UnmanagedObjectSlaAssignmentInfo(); // UnmanagedObjectSlaAssignmentInfo | Object with SLA Domain ID and a comma-separated list of the IDs of the relic/unmanaged entities being assigned to the SLA Domain.
apiInstance.assignToRetentionSlaAsync(unmanagedObjectSlaAssignmentInfo, (error, data, response) => {
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
 **unmanagedObjectSlaAssignmentInfo** | [**UnmanagedObjectSlaAssignmentInfo**](UnmanagedObjectSlaAssignmentInfo.md)| Object with SLA Domain ID and a comma-separated list of the IDs of the relic/unmanaged entities being assigned to the SLA Domain. | 

### Return type

[**[ManagedObjectPendingSlaInfo]**](ManagedObjectPendingSlaInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bulkTierExistingSnapshots

> AsyncRequestStatus bulkTierExistingSnapshots(bulkTierSnapshotsConfig)

Bulk tier existing snapshots to cold storage

Schedules a job to tier existing snapshots of the specified objects to cold storage.

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

let apiInstance = new RubrikRestApi.UnmanagedObjectApi();
let bulkTierSnapshotsConfig = new RubrikRestApi.BulkTierSnapshotsConfig(); // BulkTierSnapshotsConfig | A list of object IDs to tier. Optionally specifies a location ID.
apiInstance.bulkTierExistingSnapshots(bulkTierSnapshotsConfig, (error, data, response) => {
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
 **bulkTierSnapshotsConfig** | [**BulkTierSnapshotsConfig**](BulkTierSnapshotsConfig.md)| A list of object IDs to tier. Optionally specifies a location ID. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryUnmanagedObjectSnapshotsV1

> SnapshotSummaryListResponse queryUnmanagedObjectSnapshotsV1(id, opts)

Get summary of all the snapshots for a given object

Gets summary information for all snapshots of the object with the specified object ID.

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

let apiInstance = new RubrikRestApi.UnmanagedObjectApi();
let id = "id_example"; // String | ID of a object.
let opts = {
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | Ignore these many matches in the beginning.
  'searchValue': "searchValue_example", // String | Search snapshot by date and time.
  'snapshotType': "snapshotType_example", // String | Filter by snapshot type. Valid types are OnDemand, PolicyBased, Retrieved.
  'beforeDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter all the snapshots before a date.
  'afterDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter all the snapshots after a date.
  'sortBy': "sortBy_example", // String | Sort by given attribute.
  'sortOrder': "sortOrder_example" // String | The sort order. The default sort order is ascending.
};
apiInstance.queryUnmanagedObjectSnapshotsV1(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of a object. | 
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| Ignore these many matches in the beginning. | [optional] 
 **searchValue** | **String**| Search snapshot by date and time. | [optional] 
 **snapshotType** | **String**| Filter by snapshot type. Valid types are OnDemand, PolicyBased, Retrieved. | [optional] 
 **beforeDate** | **Date**| Filter all the snapshots before a date. | [optional] 
 **afterDate** | **Date**| Filter all the snapshots after a date. | [optional] 
 **sortBy** | **String**| Sort by given attribute. | [optional] 
 **sortOrder** | **String**| The sort order. The default sort order is ascending. | [optional] 

### Return type

[**SnapshotSummaryListResponse**](SnapshotSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryUnmanagedObjectV1

> UnmanagedObjectDetailsListResponse queryUnmanagedObjectV1(opts)

Get summary of all the objects with unmanaged snapshots

Get summary of all the objects with unmanaged snapshots.

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

let apiInstance = new RubrikRestApi.UnmanagedObjectApi();
let opts = {
  'limit': 56, // Number | Limit the number of matches returned.
  'afterId': "afterId_example", // String | First unmanaged object after which objects should be retrieved.
  'searchValue': "searchValue_example", // String | Filters by the object name using infix search.
  'unmanagedStatus': "unmanagedStatus_example", // String | Filters by object status. Valid status are Protected, Unprotected, and Relic.
  'objectType': "objectType_example", // String | Filter by the type of the unmanaged object.
  'sortBy': "sortBy_example", // String | Sort the result by given attribute.
  'sortOrder': "sortOrder_example" // String | The sort order. The default sort order is ascending.
};
apiInstance.queryUnmanagedObjectV1(opts, (error, data, response) => {
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
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **afterId** | **String**| First unmanaged object after which objects should be retrieved. | [optional] 
 **searchValue** | **String**| Filters by the object name using infix search. | [optional] 
 **unmanagedStatus** | **String**| Filters by object status. Valid status are Protected, Unprotected, and Relic. | [optional] 
 **objectType** | **String**| Filter by the type of the unmanaged object. | [optional] 
 **sortBy** | **String**| Sort the result by given attribute. | [optional] 
 **sortOrder** | **String**| The sort order. The default sort order is ascending. | [optional] 

### Return type

[**UnmanagedObjectDetailsListResponse**](UnmanagedObjectDetailsListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryUnmanagedReaderObject

> UnmanagedObjectSummaryListResponse queryUnmanagedReaderObject(opts)

Get summary of all unmanaged reader objects

A summary of all unmanaged objects recovered from reader archival locations.

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

let apiInstance = new RubrikRestApi.UnmanagedObjectApi();
let opts = {
  'limit': 56, // Number | Limit the number of matches returned.
  'afterId': "afterId_example", // String | Retrieve objects after the unmanaged object with the specified ID.
  'objectName': "objectName_example", // String | Search object by object name.
  'unmanagedStatus': "unmanagedStatus_example", // String | Filters by object status. Valid status are Protected, Unprotected, and Relic.
  'objectType': "objectType_example", // String | Filter by the type of the unmanaged object.
  'sortBy': "sortBy_example", // String | Sort the result by given attribute.
  'sortOrder': "sortOrder_example" // String | The sort order. The default sort order is ascending.
};
apiInstance.queryUnmanagedReaderObject(opts, (error, data, response) => {
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
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **afterId** | **String**| Retrieve objects after the unmanaged object with the specified ID. | [optional] 
 **objectName** | **String**| Search object by object name. | [optional] 
 **unmanagedStatus** | **String**| Filters by object status. Valid status are Protected, Unprotected, and Relic. | [optional] 
 **objectType** | **String**| Filter by the type of the unmanaged object. | [optional] 
 **sortBy** | **String**| Sort the result by given attribute. | [optional] 
 **sortOrder** | **String**| The sort order. The default sort order is ascending. | [optional] 

### Return type

[**UnmanagedObjectSummaryListResponse**](UnmanagedObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

