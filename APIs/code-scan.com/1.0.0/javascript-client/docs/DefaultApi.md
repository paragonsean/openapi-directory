# CodeScanApi.DefaultApi

All URIs are relative to *https://app.code-scan.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobGet**](DefaultApi.md#jobGet) | **GET** /job | Get the status of a job
[**jobPost**](DefaultApi.md#jobPost) | **POST** /job | Queues a job



## jobGet

> Job jobGet(jobId)

Get the status of a job

Fetches the status of a job

### Example

```javascript
import CodeScanApi from 'code_scan_api';
let defaultClient = CodeScanApi.ApiClient.instance;
// Configure HTTP basic authorization: codescan_auth
let codescan_auth = defaultClient.authentications['codescan_auth'];
codescan_auth.username = 'YOUR USERNAME';
codescan_auth.password = 'YOUR PASSWORD';

let apiInstance = new CodeScanApi.DefaultApi();
let jobId = "jobId_example"; // String | Id of the Job to retrieve
apiInstance.jobGet(jobId, (error, data, response) => {
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
 **jobId** | **String**| Id of the Job to retrieve | 

### Return type

[**Job**](Job.md)

### Authorization

[codescan_auth](../README.md#codescan_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobPost

> Job jobPost(job)

Queues a job

Creates a new job

### Example

```javascript
import CodeScanApi from 'code_scan_api';
let defaultClient = CodeScanApi.ApiClient.instance;
// Configure HTTP basic authorization: codescan_auth
let codescan_auth = defaultClient.authentications['codescan_auth'];
codescan_auth.username = 'YOUR USERNAME';
codescan_auth.password = 'YOUR PASSWORD';

let apiInstance = new CodeScanApi.DefaultApi();
let job = new CodeScanApi.NewJob(); // NewJob | Id of the Job to retrieve
apiInstance.jobPost(job, (error, data, response) => {
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
 **job** | [**NewJob**](NewJob.md)| Id of the Job to retrieve | 

### Return type

[**Job**](Job.md)

### Authorization

[codescan_auth](../README.md#codescan_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

