# FilesComApi.UsageDailySnapshotsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUsageDailySnapshots**](UsageDailySnapshotsApi.md#getUsageDailySnapshots) | **GET** /usage_daily_snapshots | List Usage Daily Snapshots



## getUsageDailySnapshots

> [UsageDailySnapshotEntity] getUsageDailySnapshots(opts)

List Usage Daily Snapshots

List Usage Daily Snapshots

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsageDailySnapshotsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[date]=desc`). Valid fields are `date` and `usage_snapshot_id`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `date` and `usage_snapshot_id`. Valid field combinations are `[ usage_snapshot_id, date ]`.
  'filterGt': {key: null}, // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `date`.
  'filterGteq': {key: null}, // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `date`.
  'filterLt': {key: null}, // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `date`.
  'filterLteq': {key: null} // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `date`.
};
apiInstance.getUsageDailySnapshots(opts, (error, data, response) => {
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
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[date]&#x3D;desc&#x60;). Valid fields are &#x60;date&#x60; and &#x60;usage_snapshot_id&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;date&#x60; and &#x60;usage_snapshot_id&#x60;. Valid field combinations are &#x60;[ usage_snapshot_id, date ]&#x60;. | [optional] 
 **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;date&#x60;. | [optional] 
 **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;date&#x60;. | [optional] 
 **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;date&#x60;. | [optional] 
 **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;date&#x60;. | [optional] 

### Return type

[**[UsageDailySnapshotEntity]**](UsageDailySnapshotEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

