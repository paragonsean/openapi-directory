# SalesLoftPlatform.BulkJobsJobDataApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2BulkJobsBulkJobsIdJobDataGet**](BulkJobsJobDataApi.md#v2BulkJobsBulkJobsIdJobDataGet) | **GET** /v2/bulk_jobs/{bulk_jobs_id}/job_data | List job data for a bulk job
[**v2BulkJobsBulkJobsIdJobDataPost**](BulkJobsJobDataApi.md#v2BulkJobsBulkJobsIdJobDataPost) | **POST** /v2/bulk_jobs/{bulk_jobs_id}/job_data | Create job data for a bulk job



## v2BulkJobsBulkJobsIdJobDataGet

> [BulkJobResult] v2BulkJobsBulkJobsIdJobDataGet(bulkJobsId, opts)

List job data for a bulk job

Fetches multiple job data records for a given bulk job. Pagination is not supported, but cursor based polling is via use of the &#x60;id[gt]&#x60; filter. Pass the last id seen (i.e. &#x60;id[gt]&#x3D;1234&#x60;) in order to get the next batch of records.

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.BulkJobsJobDataApi();
let bulkJobsId = 56; // Number | The id for the bulk job to which the job data relates
let opts = {
  'status': ["null"], // [String] | Filter by result status. Accepts multiple statuses. Each status must be one of pending, success, error, retrying
  'id': {key: null}, // Object | Filter by id using comparison operators. Only supports greater than (gt) comparison (i.e. id[gt]=123)
  'perPage': 56 // Number | How many records to show per page in the range [1, 100]. Defaults to 25
};
apiInstance.v2BulkJobsBulkJobsIdJobDataGet(bulkJobsId, opts, (error, data, response) => {
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
 **bulkJobsId** | **Number**| The id for the bulk job to which the job data relates | 
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


## v2BulkJobsBulkJobsIdJobDataPost

> JobDataCreationResult v2BulkJobsBulkJobsIdJobDataPost(bulkJobsId, data)

Create job data for a bulk job

Upload job data for the specified bulk job. Upload an array of objects, where element contains the parameters necessary to execute the individual calls. Each call to this endpoint can handle up to 5,000 records at a time. There is no limit to how many times you can create job data for a given bulk job.  For additional information on creating bulk jobs, the types of supported bulk jobs, and examples of the bulk job flow, visit the &lt;a href&#x3D;\&quot;/bulk.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;bulk job details page&lt;/a&gt;. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.BulkJobsJobDataApi();
let bulkJobsId = 56; // Number | The id for the bulk job to which the job data relates
let data = ["null"]; // [String] | Array of objects containing parameters to be used to execute an instance of each. Array must be 5,000 records or less.
apiInstance.v2BulkJobsBulkJobsIdJobDataPost(bulkJobsId, data, (error, data, response) => {
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
 **bulkJobsId** | **Number**| The id for the bulk job to which the job data relates | 
 **data** | [**[String]**](String.md)| Array of objects containing parameters to be used to execute an instance of each. Array must be 5,000 records or less. | 

### Return type

[**JobDataCreationResult**](JobDataCreationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

