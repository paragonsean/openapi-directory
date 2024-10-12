# AwsIoTJobsDataPlane.DefaultApi

All URIs are relative to *http://data.jobs.iot.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describeJobExecution**](DefaultApi.md#describeJobExecution) | **GET** /things/{thingName}/jobs/{jobId} | 
[**getPendingJobExecutions**](DefaultApi.md#getPendingJobExecutions) | **GET** /things/{thingName}/jobs | 
[**startNextPendingJobExecution**](DefaultApi.md#startNextPendingJobExecution) | **PUT** /things/{thingName}/jobs/$next | 
[**updateJobExecution**](DefaultApi.md#updateJobExecution) | **POST** /things/{thingName}/jobs/{jobId} | 



## describeJobExecution

> DescribeJobExecutionResponse describeJobExecution(jobId, thingName, opts)



Gets details of a job execution.

### Example

```javascript
import AwsIoTJobsDataPlane from 'aws_io_t_jobs_data_plane';
let defaultClient = AwsIoTJobsDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTJobsDataPlane.DefaultApi();
let jobId = "jobId_example"; // String | The unique identifier assigned to this job when it was created.
let thingName = "thingName_example"; // String | The thing name associated with the device the job execution is running on.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'includeJobDocument': true, // Boolean | Optional. When set to true, the response contains the job document. The default is false.
  'executionNumber': 56 // Number | Optional. A number that identifies a particular job execution on a particular device. If not specified, the latest job execution is returned.
};
apiInstance.describeJobExecution(jobId, thingName, opts, (error, data, response) => {
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
 **jobId** | **String**| The unique identifier assigned to this job when it was created. | 
 **thingName** | **String**| The thing name associated with the device the job execution is running on. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **includeJobDocument** | **Boolean**| Optional. When set to true, the response contains the job document. The default is false. | [optional] 
 **executionNumber** | **Number**| Optional. A number that identifies a particular job execution on a particular device. If not specified, the latest job execution is returned. | [optional] 

### Return type

[**DescribeJobExecutionResponse**](DescribeJobExecutionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPendingJobExecutions

> GetPendingJobExecutionsResponse getPendingJobExecutions(thingName, opts)



Gets the list of all jobs for a thing that are not in a terminal status.

### Example

```javascript
import AwsIoTJobsDataPlane from 'aws_io_t_jobs_data_plane';
let defaultClient = AwsIoTJobsDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTJobsDataPlane.DefaultApi();
let thingName = "thingName_example"; // String | The name of the thing that is executing the job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPendingJobExecutions(thingName, opts, (error, data, response) => {
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
 **thingName** | **String**| The name of the thing that is executing the job. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPendingJobExecutionsResponse**](GetPendingJobExecutionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startNextPendingJobExecution

> StartNextPendingJobExecutionResponse startNextPendingJobExecution(thingName, startNextPendingJobExecutionRequest, opts)



Gets and starts the next pending (status IN_PROGRESS or QUEUED) job execution for a thing.

### Example

```javascript
import AwsIoTJobsDataPlane from 'aws_io_t_jobs_data_plane';
let defaultClient = AwsIoTJobsDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTJobsDataPlane.DefaultApi();
let thingName = "thingName_example"; // String | The name of the thing associated with the device.
let startNextPendingJobExecutionRequest = new AwsIoTJobsDataPlane.StartNextPendingJobExecutionRequest(); // StartNextPendingJobExecutionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startNextPendingJobExecution(thingName, startNextPendingJobExecutionRequest, opts, (error, data, response) => {
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
 **thingName** | **String**| The name of the thing associated with the device. | 
 **startNextPendingJobExecutionRequest** | [**StartNextPendingJobExecutionRequest**](StartNextPendingJobExecutionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartNextPendingJobExecutionResponse**](StartNextPendingJobExecutionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateJobExecution

> UpdateJobExecutionResponse updateJobExecution(jobId, thingName, updateJobExecutionRequest, opts)



Updates the status of a job execution.

### Example

```javascript
import AwsIoTJobsDataPlane from 'aws_io_t_jobs_data_plane';
let defaultClient = AwsIoTJobsDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTJobsDataPlane.DefaultApi();
let jobId = "jobId_example"; // String | The unique identifier assigned to this job when it was created.
let thingName = "thingName_example"; // String | The name of the thing associated with the device.
let updateJobExecutionRequest = new AwsIoTJobsDataPlane.UpdateJobExecutionRequest(); // UpdateJobExecutionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateJobExecution(jobId, thingName, updateJobExecutionRequest, opts, (error, data, response) => {
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
 **jobId** | **String**| The unique identifier assigned to this job when it was created. | 
 **thingName** | **String**| The name of the thing associated with the device. | 
 **updateJobExecutionRequest** | [**UpdateJobExecutionRequest**](UpdateJobExecutionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateJobExecutionResponse**](UpdateJobExecutionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

