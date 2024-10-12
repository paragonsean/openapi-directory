# RunscopeApi.TestEnvironmentsApi

All URIs are relative to *https://api.runscope.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bucketsBucketKeyTestsTestIdEnvironmentsEnvironmentIdPut**](TestEnvironmentsApi.md#bucketsBucketKeyTestsTestIdEnvironmentsEnvironmentIdPut) | **PUT** /buckets/{bucketKey}/tests/{testId}/environments/{environmentId} | Update the details of a test environment.
[**bucketsBucketKeyTestsTestIdEnvironmentsGet**](TestEnvironmentsApi.md#bucketsBucketKeyTestsTestIdEnvironmentsGet) | **GET** /buckets/{bucketKey}/tests/{testId}/environments | Return details of the test&#39;s environments (only those that belong to the specified test)
[**bucketsBucketKeyTestsTestIdEnvironmentsPost**](TestEnvironmentsApi.md#bucketsBucketKeyTestsTestIdEnvironmentsPost) | **POST** /buckets/{bucketKey}/tests/{testId}/environments | Create new test environment.



## bucketsBucketKeyTestsTestIdEnvironmentsEnvironmentIdPut

> bucketsBucketKeyTestsTestIdEnvironmentsEnvironmentIdPut(bucketKey, testId, environmentId, modifiedEnvironment)

Update the details of a test environment.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestEnvironmentsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let testId = "testId_example"; // String | Unique identifier for a test
let environmentId = "environmentId_example"; // String | Unique identifier for a test environment
let modifiedEnvironment = new RunscopeApi.Environment(); // Environment | 
apiInstance.bucketsBucketKeyTestsTestIdEnvironmentsEnvironmentIdPut(bucketKey, testId, environmentId, modifiedEnvironment, (error, data, response) => {
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
 **bucketKey** | **String**| Unique identifier for a bucket | 
 **testId** | **String**| Unique identifier for a test | 
 **environmentId** | **String**| Unique identifier for a test environment | 
 **modifiedEnvironment** | [**Environment**](Environment.md)|  | 

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## bucketsBucketKeyTestsTestIdEnvironmentsGet

> BucketsBucketKeyTestsTestIdEnvironmentsGet200Response bucketsBucketKeyTestsTestIdEnvironmentsGet(bucketKey, testId)

Return details of the test&#39;s environments (only those that belong to the specified test)

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestEnvironmentsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let testId = "testId_example"; // String | Unique identifier for a test
apiInstance.bucketsBucketKeyTestsTestIdEnvironmentsGet(bucketKey, testId, (error, data, response) => {
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
 **bucketKey** | **String**| Unique identifier for a bucket | 
 **testId** | **String**| Unique identifier for a test | 

### Return type

[**BucketsBucketKeyTestsTestIdEnvironmentsGet200Response**](BucketsBucketKeyTestsTestIdEnvironmentsGet200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bucketsBucketKeyTestsTestIdEnvironmentsPost

> bucketsBucketKeyTestsTestIdEnvironmentsPost(bucketKey, testId, newEnvironment)

Create new test environment.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestEnvironmentsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let testId = "testId_example"; // String | Unique identifier for a test
let newEnvironment = new RunscopeApi.Environment(); // Environment | 
apiInstance.bucketsBucketKeyTestsTestIdEnvironmentsPost(bucketKey, testId, newEnvironment, (error, data, response) => {
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
 **bucketKey** | **String**| Unique identifier for a bucket | 
 **testId** | **String**| Unique identifier for a test | 
 **newEnvironment** | [**Environment**](Environment.md)|  | 

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

