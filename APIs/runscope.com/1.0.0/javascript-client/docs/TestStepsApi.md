# RunscopeApi.TestStepsApi

All URIs are relative to *https://api.runscope.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bucketsBucketKeyTestsTestIdStepsGet**](TestStepsApi.md#bucketsBucketKeyTestsTestIdStepsGet) | **GET** /buckets/{bucketKey}/tests/{testId}/steps | List test steps for a test.
[**bucketsBucketKeyTestsTestIdStepsPost**](TestStepsApi.md#bucketsBucketKeyTestsTestIdStepsPost) | **POST** /buckets/{bucketKey}/tests/{testId}/steps | Add new test step.
[**bucketsBucketKeyTestsTestIdStepsStepIdDelete**](TestStepsApi.md#bucketsBucketKeyTestsTestIdStepsStepIdDelete) | **DELETE** /buckets/{bucketKey}/tests/{testId}/steps/{stepId} | Delete a step from a test.
[**bucketsBucketKeyTestsTestIdStepsStepIdPut**](TestStepsApi.md#bucketsBucketKeyTestsTestIdStepsStepIdPut) | **PUT** /buckets/{bucketKey}/tests/{testId}/steps/{stepId} | Update the details of a single test step.



## bucketsBucketKeyTestsTestIdStepsGet

> bucketsBucketKeyTestsTestIdStepsGet(bucketKey, testId)

List test steps for a test.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestStepsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let testId = "testId_example"; // String | Unique identifier for a test
apiInstance.bucketsBucketKeyTestsTestIdStepsGet(bucketKey, testId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## bucketsBucketKeyTestsTestIdStepsPost

> bucketsBucketKeyTestsTestIdStepsPost(bucketKey, testId, testStep)

Add new test step.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestStepsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let testId = "testId_example"; // String | Unique identifier for a test
let testStep = new RunscopeApi.TestStep(); // TestStep | 
apiInstance.bucketsBucketKeyTestsTestIdStepsPost(bucketKey, testId, testStep, (error, data, response) => {
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
 **testStep** | [**TestStep**](TestStep.md)|  | 

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bucketsBucketKeyTestsTestIdStepsStepIdDelete

> bucketsBucketKeyTestsTestIdStepsStepIdDelete(bucketKey, testId, stepId)

Delete a step from a test.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestStepsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let testId = "testId_example"; // String | Unique identifier for a test
let stepId = "stepId_example"; // String | Unique identifier for a test step
apiInstance.bucketsBucketKeyTestsTestIdStepsStepIdDelete(bucketKey, testId, stepId, (error, data, response) => {
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
 **stepId** | **String**| Unique identifier for a test step | 

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## bucketsBucketKeyTestsTestIdStepsStepIdPut

> bucketsBucketKeyTestsTestIdStepsStepIdPut(bucketKey, testId, stepId, testStep)

Update the details of a single test step.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestStepsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let testId = "testId_example"; // String | Unique identifier for a test
let stepId = "stepId_example"; // String | Unique identifier for a test step
let testStep = new RunscopeApi.TestStep(); // TestStep | 
apiInstance.bucketsBucketKeyTestsTestIdStepsStepIdPut(bucketKey, testId, stepId, testStep, (error, data, response) => {
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
 **stepId** | **String**| Unique identifier for a test step | 
 **testStep** | [**TestStep**](TestStep.md)|  | 

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

