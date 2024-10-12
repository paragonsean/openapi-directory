# MesheryApi.PatternsAPIApi

All URIs are relative to *http://meshery.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idDeleteDeployPattern**](PatternsAPIApi.md#idDeleteDeployPattern) | **DELETE** /api/pattern/deploy | Handle DELETE request for Pattern Deploy
[**idDeleteMesheryPattern**](PatternsAPIApi.md#idDeleteMesheryPattern) | **DELETE** /api/pattern/{id} | Handle Delete for a Meshery Pattern
[**idGETOAMMesheryPattern**](PatternsAPIApi.md#idGETOAMMesheryPattern) | **GET** /api/oam/{type} | Handles the get requests for the OAM objects
[**idGetMesheryPattern**](PatternsAPIApi.md#idGetMesheryPattern) | **GET** /api/pattern/{id} | Handle GET for a Meshery Pattern
[**idGetPatternFiles**](PatternsAPIApi.md#idGetPatternFiles) | **GET** /api/pattern | Handle GET request for patterns
[**idPOSTOAMMesheryPattern**](PatternsAPIApi.md#idPOSTOAMMesheryPattern) | **POST** /api/oam/{type} | Handles registering OMA objects
[**idPostDeployPattern**](PatternsAPIApi.md#idPostDeployPattern) | **POST** /api/pattern/deploy | Handle POST request for Pattern Deploy
[**idPostPatternFile**](PatternsAPIApi.md#idPostPatternFile) | **POST** /api/pattern | Handle POST requests for patterns



## idDeleteDeployPattern

> idDeleteDeployPattern()

Handle DELETE request for Pattern Deploy

Delete a deployed pattern with the request

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PatternsAPIApi();
apiInstance.idDeleteDeployPattern((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idDeleteMesheryPattern

> idDeleteMesheryPattern(id)

Handle Delete for a Meshery Pattern

Deletes a meshery pattern with ID: id

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PatternsAPIApi();
let id = "id_example"; // String | id for a specific
apiInstance.idDeleteMesheryPattern(id, (error, data, response) => {
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


## idGETOAMMesheryPattern

> idGETOAMMesheryPattern(type)

Handles the get requests for the OAM objects

Getting list of workloads/traits/scopes  {type} being of either trait, scope, workload; registration of adapter capabilities.

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PatternsAPIApi();
let type = "type_example"; // String | Automatically added
apiInstance.idGETOAMMesheryPattern(type, (error, data, response) => {
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
 **type** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idGetMesheryPattern

> MesheryPattern idGetMesheryPattern(id)

Handle GET for a Meshery Pattern

Fetches the pattern with the given id

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PatternsAPIApi();
let id = "id_example"; // String | id for a specific
apiInstance.idGetMesheryPattern(id, (error, data, response) => {
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

[**MesheryPattern**](MesheryPattern.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetPatternFiles

> PatternsAPIResponse idGetPatternFiles()

Handle GET request for patterns

Returns the list of all the patterns saved by the current user This will return all the patterns with their details

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PatternsAPIApi();
apiInstance.idGetPatternFiles((error, data, response) => {
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

[**PatternsAPIResponse**](PatternsAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idPOSTOAMMesheryPattern

> idPOSTOAMMesheryPattern(type)

Handles registering OMA objects

Adding a workload/trait/scope  {type} being of either trait, scope, workload; registration of adapter capabilities.

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PatternsAPIApi();
let type = "type_example"; // String | Automatically added
apiInstance.idPOSTOAMMesheryPattern(type, (error, data, response) => {
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
 **type** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idPostDeployPattern

> idPostDeployPattern(opts)

Handle POST request for Pattern Deploy

Deploy an attached pattern with the request

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PatternsAPIApi();
let opts = {
  'uploadYamlYmlFile': "/path/to/file" // File | 
};
apiInstance.idPostDeployPattern(opts, (error, data, response) => {
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
 **uploadYamlYmlFile** | **File**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## idPostPatternFile

> MesheryPattern idPostPatternFile()

Handle POST requests for patterns

Edit/update a meshery pattern

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PatternsAPIApi();
apiInstance.idPostPatternFile((error, data, response) => {
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

[**MesheryPattern**](MesheryPattern.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

