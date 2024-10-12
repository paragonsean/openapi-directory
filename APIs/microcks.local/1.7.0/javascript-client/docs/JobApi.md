# MicrocksApiV17.JobApi

All URIs are relative to *http://microcks.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateImportJob**](JobApi.md#activateImportJob) | **PUT** /jobs/{id}/activate | Activate an ImportJob
[**createImportJob**](JobApi.md#createImportJob) | **POST** /jobs | Create ImportJob
[**deleteImportJob**](JobApi.md#deleteImportJob) | **DELETE** /jobs/{id} | Delete ImportJob
[**getImportJobCounter**](JobApi.md#getImportJobCounter) | **GET** /jobs/count | Get the ImportJobs counter
[**getImportJobs**](JobApi.md#getImportJobs) | **GET** /jobs | Get ImportJobs
[**jobsIdGet**](JobApi.md#jobsIdGet) | **GET** /jobs/{id} | Get ImportJob
[**jobsIdPost**](JobApi.md#jobsIdPost) | **POST** /jobs/{id} | Update ImportJob
[**startImportJob**](JobApi.md#startImportJob) | **PUT** /jobs/{id}/start | Start an ImportJob
[**stopImportJob**](JobApi.md#stopImportJob) | **PUT** /jobs/{id}/stop | Stop an ImportJob
[**uploadArtifact**](JobApi.md#uploadArtifact) | **POST** /artifact/upload | Upload an artifact



## activateImportJob

> ImportJob activateImportJob(id)

Activate an ImportJob

Make an ImportJob active, so that it is executed

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.JobApi();
let id = "id_example"; // String | Unique identifier of ImportJob to manage
apiInstance.activateImportJob(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of ImportJob to manage | 

### Return type

[**ImportJob**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createImportJob

> ImportJob createImportJob(importJob)

Create ImportJob

Create a new ImportJob

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.JobApi();
let importJob = new MicrocksApiV17.ImportJob(); // ImportJob | 
apiInstance.createImportJob(importJob, (error, data, response) => {
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
 **importJob** | [**ImportJob**](ImportJob.md)|  | 

### Return type

[**ImportJob**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteImportJob

> deleteImportJob(id)

Delete ImportJob

Delete an ImportJob

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.JobApi();
let id = "id_example"; // String | Unique identifier of ImportJob to manage
apiInstance.deleteImportJob(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of ImportJob to manage | 

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImportJobCounter

> Counter getImportJobCounter()

Get the ImportJobs counter

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.JobApi();
apiInstance.getImportJobCounter((error, data, response) => {
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

[**Counter**](Counter.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImportJobs

> [ImportJob] getImportJobs(opts)

Get ImportJobs

Retrieve a list of ImportJobs

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.JobApi();
let opts = {
  'page': 56, // Number | Page of ImportJobs to retrieve (starts at and defaults to 0)
  'size': 56, // Number | Size of a page. Maximum number of ImportJobs to include in a response (defaults to 20)
  'name': "name_example" // String | Name like criterion for query
};
apiInstance.getImportJobs(opts, (error, data, response) => {
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
 **page** | **Number**| Page of ImportJobs to retrieve (starts at and defaults to 0) | [optional] 
 **size** | **Number**| Size of a page. Maximum number of ImportJobs to include in a response (defaults to 20) | [optional] 
 **name** | **String**| Name like criterion for query | [optional] 

### Return type

[**[ImportJob]**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsIdGet

> ImportJob jobsIdGet(id)

Get ImportJob

Retrieve an ImportJob using its identifier

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.JobApi();
let id = "id_example"; // String | Unique identifier of ImportJob to manage
apiInstance.jobsIdGet(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of ImportJob to manage | 

### Return type

[**ImportJob**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsIdPost

> ImportJob jobsIdPost(id, importJob)

Update ImportJob

Update an ImportJob

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.JobApi();
let id = "id_example"; // String | Unique identifier of ImportJob to manage
let importJob = new MicrocksApiV17.ImportJob(); // ImportJob | 
apiInstance.jobsIdPost(id, importJob, (error, data, response) => {
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
 **id** | **String**| Unique identifier of ImportJob to manage | 
 **importJob** | [**ImportJob**](ImportJob.md)|  | 

### Return type

[**ImportJob**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startImportJob

> ImportJob startImportJob(id)

Start an ImportJob

Starting an ImportJob forces it to immediatly import mock definitions

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.JobApi();
let id = "id_example"; // String | Unique identifier of ImportJob to manage
apiInstance.startImportJob(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of ImportJob to manage | 

### Return type

[**ImportJob**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopImportJob

> ImportJob stopImportJob(id)

Stop an ImportJob

Stopping an ImportJob desactivate it, so that it won&#39;t execute at next schedule

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.JobApi();
let id = "id_example"; // String | Unique identifier of ImportJob to manage
apiInstance.stopImportJob(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of ImportJob to manage | 

### Return type

[**ImportJob**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadArtifact

> String uploadArtifact(mainArtifact, file)

Upload an artifact

Uploads an artifact to be imported by Microcks.

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.JobApi();
let mainArtifact = true; // Boolean | Flag telling if this should be considered as primary or secondary artifact. Default to 'true'
let file = "/path/to/file"; // File | The artifact to upload
apiInstance.uploadArtifact(mainArtifact, file, (error, data, response) => {
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
 **mainArtifact** | **Boolean**| Flag telling if this should be considered as primary or secondary artifact. Default to &#39;true&#39; | 
 **file** | **File**| The artifact to upload | 

### Return type

**String**

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: text/plain

