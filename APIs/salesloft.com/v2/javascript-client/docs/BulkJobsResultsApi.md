# SalesLoftPlatform.BulkJobsResultsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2BulkJobsBulkJobsIdResultsGet**](BulkJobsResultsApi.md#v2BulkJobsBulkJobsIdResultsGet) | **GET** /v2/bulk_jobs/{bulk_jobs_id}/results | List job data for a completed bulk job.



## v2BulkJobsBulkJobsIdResultsGet

> [BulkJobResult] v2BulkJobsBulkJobsIdResultsGet(bulkJobsId, opts)

List job data for a completed bulk job.

Fetches multiple job data records for a completed bulk job. Note that until a bulk job&#39;s state is set to &#x60;done&#x60; the returned &#x60;data&#x60; will be an empty array. Pagination is not supported, but cursor based polling is via use of the &#x60;id[gt]&#x60; filter. Pass the last id seen (i.e. &#x60;id[gt]&#x3D;1234&#x60;) in order to get the next batch of records.

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.BulkJobsResultsApi();
let bulkJobsId = 56; // Number | The id for the Bulk Job
let opts = {
  'status': ["null"], // [String] | Filter by result status. Accepts multiple statuses. Each status must be one of pending, success, error, retrying
  'id': {key: null}, // Object | Filter by id using comparison operators. Only supports greater than (gt) comparison (i.e. id[gt]=123)
  'perPage': 56 // Number | How many records to show per page in the range [1, 100]. Defaults to 25
};
apiInstance.v2BulkJobsBulkJobsIdResultsGet(bulkJobsId, opts, (error, data, response) => {
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
 **bulkJobsId** | **Number**| The id for the Bulk Job | 
 **status** | [**[String]**](String.md)| Filter by result status. Accepts multiple statuses. Each status must be one of pending, success, error, retrying | [optional] 
 **id** | [**Object**](.md)| Filter by id using comparison operators. Only supports greater than (gt) comparison (i.e. id[gt]&#x3D;123) | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 

### Return type

[**[BulkJobResult]**](BulkJobResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

