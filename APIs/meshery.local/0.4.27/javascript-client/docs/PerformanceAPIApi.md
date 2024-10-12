# MesheryApi.PerformanceAPIApi

All URIs are relative to *http://meshery.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idDeletePerformanceProfile**](PerformanceAPIApi.md#idDeletePerformanceProfile) | **DELETE** /api/user/performance/profiles/{id} | Handle Delete requests for performance profiles
[**idGETProfileResults**](PerformanceAPIApi.md#idGETProfileResults) | **GET** /api/user/performance/profiles/{id}/results | Handle GET request for results of a profile
[**idGetAllPerformanceResults**](PerformanceAPIApi.md#idGetAllPerformanceResults) | **GET** /api/user/performance/profiles/results | Handles GET requests for performance results
[**idGetPerformanceProfiles**](PerformanceAPIApi.md#idGetPerformanceProfiles) | **GET** /api/user/performance/profiles | Handle GET requests for performance profiles
[**idGetSinglePerformanceProfile**](PerformanceAPIApi.md#idGetSinglePerformanceProfile) | **GET** /api/user/performance/profiles/{id} | Handle GET requests for performance results of a profile
[**idRunPerformanceTest**](PerformanceAPIApi.md#idRunPerformanceTest) | **GET** /api/user/performance/profiles/{id}/run | Handle GET request to run a performance test
[**idSavePerformanceProfile**](PerformanceAPIApi.md#idSavePerformanceProfile) | **POST** /api/user/performance/profiles | Handle POST requests for saving performance profile



## idDeletePerformanceProfile

> idDeletePerformanceProfile(id)

Handle Delete requests for performance profiles

Deletes a performance profile with the given id

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PerformanceAPIApi();
let id = "id_example"; // String | id for a specific
apiInstance.idDeletePerformanceProfile(id, (error, data, response) => {
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
 **id** | **String**| id for a specific | 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idGETProfileResults

> PerformanceResultsAPIResponse idGETProfileResults(id)

Handle GET request for results of a profile

Fetchs pages of results from Remote Provider for the given id

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PerformanceAPIApi();
let id = "id_example"; // String | id for a specific
apiInstance.idGETProfileResults(id, (error, data, response) => {
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
 **id** | **String**| id for a specific | 

### Return type

[**PerformanceResultsAPIResponse**](PerformanceResultsAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetAllPerformanceResults

> PerformanceResultsAPIResponse idGetAllPerformanceResults()

Handles GET requests for performance results

Returns pages of all the performance results from Remote Provider

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PerformanceAPIApi();
apiInstance.idGetAllPerformanceResults((error, data, response) => {
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


## idGetPerformanceProfiles

> PerformanceProfilesAPIResponse idGetPerformanceProfiles()

Handle GET requests for performance profiles

Returns the list of all the performance profiles saved by the current user

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PerformanceAPIApi();
apiInstance.idGetPerformanceProfiles((error, data, response) => {
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

[**PerformanceProfilesAPIResponse**](PerformanceProfilesAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetSinglePerformanceProfile

> PerformanceProfile idGetSinglePerformanceProfile(id)

Handle GET requests for performance results of a profile

Returns single performance profile with the given id

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PerformanceAPIApi();
let id = "id_example"; // String | id for a specific
apiInstance.idGetSinglePerformanceProfile(id, (error, data, response) => {
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
 **id** | **String**| id for a specific | 

### Return type

[**PerformanceProfile**](PerformanceProfile.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idRunPerformanceTest

> idRunPerformanceTest(id)

Handle GET request to run a performance test

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

let apiInstance = new MesheryApi.PerformanceAPIApi();
let id = "id_example"; // String | Automatically added
apiInstance.idRunPerformanceTest(id, (error, data, response) => {
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
 **id** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idSavePerformanceProfile

> PerformanceProfile idSavePerformanceProfile(opts)

Handle POST requests for saving performance profile

Save performance profile using the current provider&#39;s persistence mechanism

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PerformanceAPIApi();
let opts = {
  'performanceProfileParameters': new MesheryApi.PerformanceProfileParameters() // PerformanceProfileParameters | 
};
apiInstance.idSavePerformanceProfile(opts, (error, data, response) => {
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
 **performanceProfileParameters** | [**PerformanceProfileParameters**](PerformanceProfileParameters.md)|  | [optional] 

### Return type

[**PerformanceProfile**](PerformanceProfile.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

