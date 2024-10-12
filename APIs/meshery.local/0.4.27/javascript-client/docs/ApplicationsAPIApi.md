# MesheryApi.ApplicationsAPIApi

All URIs are relative to *http://meshery.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idDeleteApplicationFile**](ApplicationsAPIApi.md#idDeleteApplicationFile) | **DELETE** /api/application/deploy | Handle DELETE request for Application File Deploy
[**idDeleteMesheryApplicationFile**](ApplicationsAPIApi.md#idDeleteMesheryApplicationFile) | **DELETE** /api/application/{id} | Handle Delete for a Meshery Application File
[**idGetApplicationFileRequest**](ApplicationsAPIApi.md#idGetApplicationFileRequest) | **GET** /api/application/ | Handle GET request for Application Files
[**idGetMesheryApplication**](ApplicationsAPIApi.md#idGetMesheryApplication) | **GET** /api/application/{id} | Handle GET request for Meshery Application with the given id
[**idPostApplicationFileRequest**](ApplicationsAPIApi.md#idPostApplicationFileRequest) | **POST** /api/application/ | Handle POST request for Application Files
[**idPostDeployApplicationFile**](ApplicationsAPIApi.md#idPostDeployApplicationFile) | **POST** /api/application/deploy | Handle POST request for Application File Deploy



## idDeleteApplicationFile

> idDeleteApplicationFile()

Handle DELETE request for Application File Deploy

Delete a deployed application file with the request

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.ApplicationsAPIApi();
apiInstance.idDeleteApplicationFile((error, data, response) => {
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


## idDeleteMesheryApplicationFile

> idDeleteMesheryApplicationFile(id)

Handle Delete for a Meshery Application File

Deletes a meshery application file with ID: id

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.ApplicationsAPIApi();
let id = "id_example"; // String | id for a specific
apiInstance.idDeleteMesheryApplicationFile(id, (error, data, response) => {
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


## idGetApplicationFileRequest

> ApplicationsAPIResponse idGetApplicationFileRequest()

Handle GET request for Application Files

Returns requests for all Meshery Applications

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.ApplicationsAPIApi();
apiInstance.idGetApplicationFileRequest((error, data, response) => {
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

[**ApplicationsAPIResponse**](ApplicationsAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetMesheryApplication

> MesheryApplication idGetMesheryApplication(id)

Handle GET request for Meshery Application with the given id

Fetches the list of all applications saved by the current user

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.ApplicationsAPIApi();
let id = "id_example"; // String | id for a specific
apiInstance.idGetMesheryApplication(id, (error, data, response) => {
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

[**MesheryApplication**](MesheryApplication.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idPostApplicationFileRequest

> MesheryApplication idPostApplicationFileRequest()

Handle POST request for Application Files

Save attached Meshery Application File

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.ApplicationsAPIApi();
apiInstance.idPostApplicationFileRequest((error, data, response) => {
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

[**MesheryApplication**](MesheryApplication.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idPostDeployApplicationFile

> MesheryApplication idPostDeployApplicationFile(opts)

Handle POST request for Application File Deploy

Deploy an attached application file with the request

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.ApplicationsAPIApi();
let opts = {
  'uploadYamlYmlFile': "/path/to/file" // File | 
};
apiInstance.idPostDeployApplicationFile(opts, (error, data, response) => {
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
 **uploadYamlYmlFile** | **File**|  | [optional] 

### Return type

[**MesheryApplication**](MesheryApplication.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

