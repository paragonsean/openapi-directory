# BatchService.JobSchedulesApi

All URIs are relative to *https://batch.core.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobScheduleAdd**](JobSchedulesApi.md#jobScheduleAdd) | **POST** /jobschedules | 
[**jobScheduleDelete**](JobSchedulesApi.md#jobScheduleDelete) | **DELETE** /jobschedules/{jobScheduleId} | 
[**jobScheduleDisable**](JobSchedulesApi.md#jobScheduleDisable) | **POST** /jobschedules/{jobScheduleId}/disable | 
[**jobScheduleEnable**](JobSchedulesApi.md#jobScheduleEnable) | **POST** /jobschedules/{jobScheduleId}/enable | 
[**jobScheduleExists**](JobSchedulesApi.md#jobScheduleExists) | **HEAD** /jobschedules/{jobScheduleId} | 
[**jobScheduleGet**](JobSchedulesApi.md#jobScheduleGet) | **GET** /jobschedules/{jobScheduleId} | 
[**jobScheduleList**](JobSchedulesApi.md#jobScheduleList) | **GET** /jobschedules | 
[**jobSchedulePatch**](JobSchedulesApi.md#jobSchedulePatch) | **PATCH** /jobschedules/{jobScheduleId} | 
[**jobScheduleTerminate**](JobSchedulesApi.md#jobScheduleTerminate) | **POST** /jobschedules/{jobScheduleId}/terminate | 
[**jobScheduleUpdate**](JobSchedulesApi.md#jobScheduleUpdate) | **PUT** /jobschedules/{jobScheduleId} | 



## jobScheduleAdd

> jobScheduleAdd(apiVersion, jobScheduleAddParameter, opts)



Adds a job schedule to the specified account.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.JobSchedulesApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let jobScheduleAddParameter = new BatchService.JobScheduleAddParameter(); // JobScheduleAddParameter | The job schedule to be added.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.jobScheduleAdd(apiVersion, jobScheduleAddParameter, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **jobScheduleAddParameter** | [**JobScheduleAddParameter**](JobScheduleAddParameter.md)| The job schedule to be added. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## jobScheduleDelete

> jobScheduleDelete(jobScheduleId, apiVersion, opts)



Deletes a job schedule from the specified account.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.JobSchedulesApi();
let jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to delete.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.jobScheduleDelete(jobScheduleId, apiVersion, opts, (error, data, response) => {
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
 **jobScheduleId** | **String**| The id of the job schedule to delete. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobScheduleDisable

> jobScheduleDisable(jobScheduleId, apiVersion, opts)



Disables a job schedule.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.JobSchedulesApi();
let jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to disable.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.jobScheduleDisable(jobScheduleId, apiVersion, opts, (error, data, response) => {
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
 **jobScheduleId** | **String**| The id of the job schedule to disable. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobScheduleEnable

> jobScheduleEnable(jobScheduleId, apiVersion, opts)



Enables a job schedule.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.JobSchedulesApi();
let jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to enable.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.jobScheduleEnable(jobScheduleId, apiVersion, opts, (error, data, response) => {
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
 **jobScheduleId** | **String**| The id of the job schedule to enable. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobScheduleExists

> jobScheduleExists(jobScheduleId, apiVersion, opts)



Checks the specified job schedule exists.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.JobSchedulesApi();
let jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule which you want to check.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.jobScheduleExists(jobScheduleId, apiVersion, opts, (error, data, response) => {
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
 **jobScheduleId** | **String**| The id of the job schedule which you want to check. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobScheduleGet

> CloudJobSchedule jobScheduleGet(jobScheduleId, apiVersion, opts)



Gets information about the specified job schedule.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.JobSchedulesApi();
let jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to get.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'select': "select_example", // String | An OData $select clause.
  'expand': "expand_example", // String | An OData $expand clause.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.jobScheduleGet(jobScheduleId, apiVersion, opts, (error, data, response) => {
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
 **jobScheduleId** | **String**| The id of the job schedule to get. | 
 **apiVersion** | **String**| Client API Version. | 
 **select** | **String**| An OData $select clause. | [optional] 
 **expand** | **String**| An OData $expand clause. | [optional] 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

[**CloudJobSchedule**](CloudJobSchedule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobScheduleList

> CloudJobScheduleListResult jobScheduleList(apiVersion, opts)



Lists all of the job schedules in the specified account.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.JobSchedulesApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | An OData $filter clause.
  'select': "select_example", // String | An OData $select clause.
  'expand': "expand_example", // String | An OData $expand clause.
  'maxresults': 56, // Number | The maximum number of items to return in the response.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.jobScheduleList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **filter** | **String**| An OData $filter clause. | [optional] 
 **select** | **String**| An OData $select clause. | [optional] 
 **expand** | **String**| An OData $expand clause. | [optional] 
 **maxresults** | **Number**| The maximum number of items to return in the response. | [optional] 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**CloudJobScheduleListResult**](CloudJobScheduleListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobSchedulePatch

> jobSchedulePatch(jobScheduleId, apiVersion, jobSchedulePatchParameter, opts)



Updates the properties of the specified job schedule.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.JobSchedulesApi();
let jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to update.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let jobSchedulePatchParameter = new BatchService.JobSchedulePatchParameter(); // JobSchedulePatchParameter | The parameters for the request.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.jobSchedulePatch(jobScheduleId, apiVersion, jobSchedulePatchParameter, opts, (error, data, response) => {
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
 **jobScheduleId** | **String**| The id of the job schedule to update. | 
 **apiVersion** | **String**| Client API Version. | 
 **jobSchedulePatchParameter** | [**JobSchedulePatchParameter**](JobSchedulePatchParameter.md)| The parameters for the request. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## jobScheduleTerminate

> jobScheduleTerminate(jobScheduleId, apiVersion, opts)



Terminates a job schedule.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.JobSchedulesApi();
let jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to terminates.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.jobScheduleTerminate(jobScheduleId, apiVersion, opts, (error, data, response) => {
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
 **jobScheduleId** | **String**| The id of the job schedule to terminates. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobScheduleUpdate

> jobScheduleUpdate(jobScheduleId, apiVersion, jobScheduleUpdateParameter, opts)



Updates the properties of the specified job schedule.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.JobSchedulesApi();
let jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to update.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let jobScheduleUpdateParameter = new BatchService.JobScheduleUpdateParameter(); // JobScheduleUpdateParameter | The parameters for the request.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.jobScheduleUpdate(jobScheduleId, apiVersion, jobScheduleUpdateParameter, opts, (error, data, response) => {
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
 **jobScheduleId** | **String**| The id of the job schedule to update. | 
 **apiVersion** | **String**| Client API Version. | 
 **jobScheduleUpdateParameter** | [**JobScheduleUpdateParameter**](JobScheduleUpdateParameter.md)| The parameters for the request. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json

