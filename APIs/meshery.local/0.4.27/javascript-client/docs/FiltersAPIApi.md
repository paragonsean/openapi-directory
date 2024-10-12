# MesheryApi.FiltersAPIApi

All URIs are relative to *http://meshery.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idDeleteMesheryFilter**](FiltersAPIApi.md#idDeleteMesheryFilter) | **DELETE** /api/filter/{id} | Handle Delete for a Meshery Filter
[**idGetFilterFile**](FiltersAPIApi.md#idGetFilterFile) | **GET** /api/filter | Handle GET request for all filters
[**idGetFilterFiles**](FiltersAPIApi.md#idGetFilterFiles) | **GET** /api/filter/file/{id} | Handle GET request for filter file with given id
[**idGetMesheryFilter**](FiltersAPIApi.md#idGetMesheryFilter) | **GET** /api/filter/{id} | Handle GET request for a Meshery Filter
[**idPostFilterFile**](FiltersAPIApi.md#idPostFilterFile) | **POST** /api/filter | Handle POST requests for Meshery Filters



## idDeleteMesheryFilter

> idDeleteMesheryFilter(id)

Handle Delete for a Meshery Filter

Deletes a meshery filter with ID: id

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.FiltersAPIApi();
let id = "id_example"; // String | id for a specific
apiInstance.idDeleteMesheryFilter(id, (error, data, response) => {
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


## idGetFilterFile

> FiltersAPIResponse idGetFilterFile()

Handle GET request for all filters

Returns all the Meshery Filters saved by the current user

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.FiltersAPIApi();
apiInstance.idGetFilterFile((error, data, response) => {
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

[**FiltersAPIResponse**](FiltersAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetFilterFiles

> MesheryFilter idGetFilterFiles(id)

Handle GET request for filter file with given id

Returns the Meshery Filter file saved by the current user with the given id

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.FiltersAPIApi();
let id = "id_example"; // String | Automatically added
apiInstance.idGetFilterFiles(id, (error, data, response) => {
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

[**MesheryFilter**](MesheryFilter.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetMesheryFilter

> MesheryFilter idGetMesheryFilter(id)

Handle GET request for a Meshery Filter

Fetches the Meshery Filter with the given id

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.FiltersAPIApi();
let id = "id_example"; // String | id for a specific
apiInstance.idGetMesheryFilter(id, (error, data, response) => {
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

[**MesheryFilter**](MesheryFilter.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idPostFilterFile

> MesheryFilter idPostFilterFile()

Handle POST requests for Meshery Filters

Used to save/update a Meshery Filter

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.FiltersAPIApi();
apiInstance.idPostFilterFile((error, data, response) => {
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

[**MesheryFilter**](MesheryFilter.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

