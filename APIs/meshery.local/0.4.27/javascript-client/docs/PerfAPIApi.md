# MesheryApi.PerfAPIApi

All URIs are relative to *http://meshery.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idGetAllPerfResults**](PerfAPIApi.md#idGetAllPerfResults) | **GET** /api/perf/profile/result | Handles GET requests for perf results
[**idGetSinglePerfResult**](PerfAPIApi.md#idGetSinglePerfResult) | **GET** /api/perf/profile/result/{id} | Handles GET requests for perf result
[**idRunPerfTest**](PerfAPIApi.md#idRunPerfTest) | **GET** /api/perf/profile | Handle GET request to run a test



## idGetAllPerfResults

> PerformanceResultsAPIResponse idGetAllPerfResults()

Handles GET requests for perf results

Returns pages of all the perf results from Remote Provider

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PerfAPIApi();
apiInstance.idGetAllPerfResults((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**PerformanceResultsAPIResponse**](PerformanceResultsAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetSinglePerfResult

> PerformanceSpec idGetSinglePerfResult(id)

Handles GET requests for perf result

Returns an individual result from provider

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PerfAPIApi();
let id = "id_example"; // String | Automatically added
apiInstance.idGetSinglePerfResult(id, (error, data, response) => {
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
 **id** | **String**| Automatically added | 

### Return type

[**PerformanceSpec**](PerformanceSpec.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idRunPerfTest

> idRunPerfTest(opts)

Handle GET request to run a test

Runs the load test with the given parameters

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PerfAPIApi();
let opts = {
  'performanceTestConfig': new MesheryApi.PerformanceTestConfig() // PerformanceTestConfig | 
};
apiInstance.idRunPerfTest(opts, (error, data, response) => {
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
 **performanceTestConfig** | [**PerformanceTestConfig**](PerformanceTestConfig.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: Not defined

