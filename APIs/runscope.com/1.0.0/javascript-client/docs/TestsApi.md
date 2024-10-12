# RunscopeApi.TestsApi

All URIs are relative to *https://api.runscope.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bucketsBucketKeyTestsGet**](TestsApi.md#bucketsBucketKeyTestsGet) | **GET** /buckets/{bucketKey}/tests | Returns a list of tests.
[**bucketsBucketKeyTestsPost**](TestsApi.md#bucketsBucketKeyTestsPost) | **POST** /buckets/{bucketKey}/tests | Create a test.
[**bucketsBucketKeyTestsTestIdDelete**](TestsApi.md#bucketsBucketKeyTestsTestIdDelete) | **DELETE** /buckets/{bucketKey}/tests/{testId} | Delete a test, including all steps, schedules, test-specific environments and results.
[**bucketsBucketKeyTestsTestIdGet**](TestsApi.md#bucketsBucketKeyTestsTestIdGet) | **GET** /buckets/{bucketKey}/tests/{testId} | Retrieve the details of a given test by ID.
[**bucketsBucketKeyTestsTestIdMetricsGet**](TestsApi.md#bucketsBucketKeyTestsTestIdMetricsGet) | **GET** /buckets/{bucketKey}/tests/{testId}/metrics | Return details of the test metrics for the specified timeframe.
[**bucketsBucketKeyTestsTestIdPut**](TestsApi.md#bucketsBucketKeyTestsTestIdPut) | **PUT** /buckets/{bucketKey}/tests/{testId} | Modify a test&#39;s name, description, default environment and its steps. To modify other individual properties of a test, make requests to the steps, environments, and schedules subresources of the test.



## bucketsBucketKeyTestsGet

> BucketsBucketKeyTestsGet200Response bucketsBucketKeyTestsGet(bucketKey)

Returns a list of tests.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
apiInstance.bucketsBucketKeyTestsGet(bucketKey, (error, data, response) => {
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

### Return type

[**BucketsBucketKeyTestsGet200Response**](BucketsBucketKeyTestsGet200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bucketsBucketKeyTestsPost

> BucketsBucketKeyTestsGet200Response bucketsBucketKeyTestsPost(bucketKey, newTest)

Create a test.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let newTest = new RunscopeApi.Test(); // Test | 
apiInstance.bucketsBucketKeyTestsPost(bucketKey, newTest, (error, data, response) => {
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
 **newTest** | [**Test**](Test.md)|  | 

### Return type

[**BucketsBucketKeyTestsGet200Response**](BucketsBucketKeyTestsGet200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bucketsBucketKeyTestsTestIdDelete

> bucketsBucketKeyTestsTestIdDelete(bucketKey, testId)

Delete a test, including all steps, schedules, test-specific environments and results.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let testId = "testId_example"; // String | Unique identifier for a test
apiInstance.bucketsBucketKeyTestsTestIdDelete(bucketKey, testId, (error, data, response) => {
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


## bucketsBucketKeyTestsTestIdGet

> TestDetail bucketsBucketKeyTestsTestIdGet(bucketKey, testId)

Retrieve the details of a given test by ID.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let testId = "testId_example"; // String | Unique identifier for a test
apiInstance.bucketsBucketKeyTestsTestIdGet(bucketKey, testId, (error, data, response) => {
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

[**TestDetail**](TestDetail.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bucketsBucketKeyTestsTestIdMetricsGet

> Metrics bucketsBucketKeyTestsTestIdMetricsGet(bucketKey, testId)

Return details of the test metrics for the specified timeframe.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let testId = "testId_example"; // String | Unique identifier for a test
apiInstance.bucketsBucketKeyTestsTestIdMetricsGet(bucketKey, testId, (error, data, response) => {
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

[**Metrics**](Metrics.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bucketsBucketKeyTestsTestIdPut

> TestDetail bucketsBucketKeyTestsTestIdPut(bucketKey, testId)

Modify a test&#39;s name, description, default environment and its steps. To modify other individual properties of a test, make requests to the steps, environments, and schedules subresources of the test.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.TestsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let testId = "testId_example"; // String | Unique identifier for a test
apiInstance.bucketsBucketKeyTestsTestIdPut(bucketKey, testId, (error, data, response) => {
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

[**TestDetail**](TestDetail.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

