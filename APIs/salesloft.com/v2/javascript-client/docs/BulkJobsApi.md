# SalesLoftPlatform.BulkJobsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2BulkJobsGet**](BulkJobsApi.md#v2BulkJobsGet) | **GET** /v2/bulk_jobs | List bulk jobs
[**v2BulkJobsIdGet**](BulkJobsApi.md#v2BulkJobsIdGet) | **GET** /v2/bulk_jobs/{id} | Fetch a bulk job
[**v2BulkJobsIdPut**](BulkJobsApi.md#v2BulkJobsIdPut) | **PUT** /v2/bulk_jobs/{id} | Update a bulk job
[**v2BulkJobsPost**](BulkJobsApi.md#v2BulkJobsPost) | **POST** /v2/bulk_jobs | Create a bulk job



## v2BulkJobsGet

> [BulkJob] v2BulkJobsGet(opts)

List bulk jobs

Fetches multiple bulk job records. The records can be filtered, paged, and sorted according to the respective parameters.

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.BulkJobsApi();
let opts = {
  'state': ["null"], // [String] | The state of the bulk job. Accepts multiple states. Each state must be one of: open, executing, done
  'id': {key: null}, // Object | Filter by id using comparison operators. Only supports greater than (gt) comparison (i.e. id[gt]=123)
  'perPage': 56 // Number | How many records to show per page in the range [1, 100]. Defaults to 25
};
apiInstance.v2BulkJobsGet(opts, (error, data, response) => {
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
 **state** | [**[String]**](String.md)| The state of the bulk job. Accepts multiple states. Each state must be one of: open, executing, done | [optional] 
 **id** | [**Object**](.md)| Filter by id using comparison operators. Only supports greater than (gt) comparison (i.e. id[gt]&#x3D;123) | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 

### Return type

[**[BulkJob]**](BulkJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2BulkJobsIdGet

> BulkJob v2BulkJobsIdGet(id)

Fetch a bulk job

Fetches a bulk job, by ID only.

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.BulkJobsApi();
let id = 56; // Number | The id for the Bulk Job
apiInstance.v2BulkJobsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The id for the Bulk Job | 

### Return type

[**BulkJob**](BulkJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2BulkJobsIdPut

> BulkJob v2BulkJobsIdPut(id, opts)

Update a bulk job

Updates a bulk job&#39;s name and / or marks a bulk job as &#39;ready_to_execute&#39;.  May only be updated if the bulk job is still in an \&quot;open\&quot; state.  For additional information on creating bulk jobs, the types of supported bulk jobs, and examples of the bulk job flow, visit the &lt;a href&#x3D;\&quot;/bulk.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;bulk job details page&lt;/a&gt;. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.BulkJobsApi();
let id = 56; // Number | The id for the bulk job to which the job data relates
let opts = {
  'name': "name_example", // String | Name for your bulk job
  'readyToExecute': true // Boolean | Whether the job is ready to be executed. Must be true or false.
};
apiInstance.v2BulkJobsIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| The id for the bulk job to which the job data relates | 
 **name** | **String**| Name for your bulk job | [optional] 
 **readyToExecute** | **Boolean**| Whether the job is ready to be executed. Must be true or false. | [optional] 

### Return type

[**BulkJob**](BulkJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2BulkJobsPost

> BulkJob v2BulkJobsPost(type, opts)

Create a bulk job

Creates a bulk job. The type of the bulk job must be included when created.  For additional information on creating bulk jobs, the types of supported bulk jobs, and examples of the bulk job flow, visit the &lt;a href&#x3D;\&quot;/bulk.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;bulk job details page&lt;/a&gt;. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.BulkJobsApi();
let type = "type_example"; // String | Type of bulk job. Must be a valid type. Follow link to the bulk job details page above to view supported types.
let opts = {
  'name': "name_example" // String | Name for your bulk job
};
apiInstance.v2BulkJobsPost(type, opts, (error, data, response) => {
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
 **type** | **String**| Type of bulk job. Must be a valid type. Follow link to the bulk job details page above to view supported types. | 
 **name** | **String**| Name for your bulk job | [optional] 

### Return type

[**BulkJob**](BulkJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

