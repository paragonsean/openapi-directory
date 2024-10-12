# RunscopeApi.SharedEnvironmentsApi

All URIs are relative to *https://api.runscope.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bucketsBucketKeyEnvironmentsEnvironmentIdPut**](SharedEnvironmentsApi.md#bucketsBucketKeyEnvironmentsEnvironmentIdPut) | **PUT** /buckets/{bucketKey}/environments/{environmentId} | Update the details of a shared environment.
[**bucketsBucketKeyEnvironmentsGet**](SharedEnvironmentsApi.md#bucketsBucketKeyEnvironmentsGet) | **GET** /buckets/{bucketKey}/environments | Returns list of shared environments for a specified bucket.
[**bucketsBucketKeyEnvironmentsPost**](SharedEnvironmentsApi.md#bucketsBucketKeyEnvironmentsPost) | **POST** /buckets/{bucketKey}/environments | Create new shared environment.



## bucketsBucketKeyEnvironmentsEnvironmentIdPut

> bucketsBucketKeyEnvironmentsEnvironmentIdPut(bucketKey, environmentId, modifiedEnvironment)

Update the details of a shared environment.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.SharedEnvironmentsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let environmentId = "environmentId_example"; // String | Unique identifier for a test environment
let modifiedEnvironment = new RunscopeApi.Environment(); // Environment | 
apiInstance.bucketsBucketKeyEnvironmentsEnvironmentIdPut(bucketKey, environmentId, modifiedEnvironment, (error, data, response) => {
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
 **environmentId** | **String**| Unique identifier for a test environment | 
 **modifiedEnvironment** | [**Environment**](Environment.md)|  | 

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## bucketsBucketKeyEnvironmentsGet

> bucketsBucketKeyEnvironmentsGet(bucketKey)

Returns list of shared environments for a specified bucket.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.SharedEnvironmentsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
apiInstance.bucketsBucketKeyEnvironmentsGet(bucketKey, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## bucketsBucketKeyEnvironmentsPost

> bucketsBucketKeyEnvironmentsPost(bucketKey, newEnvironment)

Create new shared environment.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.SharedEnvironmentsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let newEnvironment = new RunscopeApi.Environment(); // Environment | 
apiInstance.bucketsBucketKeyEnvironmentsPost(bucketKey, newEnvironment, (error, data, response) => {
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
 **newEnvironment** | [**Environment**](Environment.md)|  | 

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

