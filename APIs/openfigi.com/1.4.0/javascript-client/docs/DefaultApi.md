# OpenFigiApi.DefaultApi

All URIs are relative to *https://api.openfigi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mappingPost**](DefaultApi.md#mappingPost) | **POST** /mapping | 
[**mappingValuesKeyGet**](DefaultApi.md#mappingValuesKeyGet) | **GET** /mapping/values/{key} | 



## mappingPost

> [MappingJobResult] mappingPost(opts)



Allows mapping from third-party identifiers to FIGIs.

### Example

```javascript
import OpenFigiApi from 'open_figi_api';
let defaultClient = OpenFigiApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new OpenFigiApi.DefaultApi();
let opts = {
  'mappingJob': [new OpenFigiApi.MappingJob()] // [MappingJob] | A list of third-party identifiers and extra filters.
};
apiInstance.mappingPost(opts, (error, data, response) => {
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
 **mappingJob** | [**[MappingJob]**](MappingJob.md)| A list of third-party identifiers and extra filters. | [optional] 

### Return type

[**[MappingJobResult]**](MappingJobResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


## mappingValuesKeyGet

> MappingValuesKeyGet200Response mappingValuesKeyGet(key)



Get values for enum-like fields.

### Example

```javascript
import OpenFigiApi from 'open_figi_api';
let defaultClient = OpenFigiApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new OpenFigiApi.DefaultApi();
let key = "key_example"; // String | Key of MappingJob for which to get possible values.
apiInstance.mappingValuesKeyGet(key, (error, data, response) => {
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
 **key** | **String**| Key of MappingJob for which to get possible values. | 

### Return type

[**MappingValuesKeyGet200Response**](MappingValuesKeyGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*

