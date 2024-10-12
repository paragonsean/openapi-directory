# MesheryApi.SystemAPIApi

All URIs are relative to *http://meshery.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idDeleteAdapterConfig**](SystemAPIApi.md#idDeleteAdapterConfig) | **DELETE** /api/system/adapter/manage | Handle DELETE requests to delete adapter config
[**idDeleteK8SConfig**](SystemAPIApi.md#idDeleteK8SConfig) | **DELETE** /api/system/kubernetes | Handle DELETE request for Kubernetes Config
[**idGetKubernetesPing**](SystemAPIApi.md#idGetKubernetesPing) | **GET** /api/system/kubernetes/ping | Handle GET request for Kubernetes ping
[**idGetSystemAdapters**](SystemAPIApi.md#idGetSystemAdapters) | **GET** /api/system/adapters | Handle GET request for adapters
[**idGetSystemVersion**](SystemAPIApi.md#idGetSystemVersion) | **GET** /api/system/version | Handle GET request for system/server version
[**idMeshSyncGrafana**](SystemAPIApi.md#idMeshSyncGrafana) | **GET** /api/system/meshsync/grafana | Handle GET request for mesh-sync grafana
[**idMeshSyncPrometheus**](SystemAPIApi.md#idMeshSyncPrometheus) | **GET** /api/system/meshsync/prometheus | Handle GET request for fetching prometheus
[**idPostAdapterConfig**](SystemAPIApi.md#idPostAdapterConfig) | **POST** /api/system/adapter/manage | Handle POST requests to persist adapter config
[**idPostAdapterOperation**](SystemAPIApi.md#idPostAdapterOperation) | **POST** /api/system/adapter/operation | Handle POST requests for Adapter Operations
[**idPostK8SConfig**](SystemAPIApi.md#idPostK8SConfig) | **POST** /api/system/kubernetes | Handle POST request for Kubernetes Config
[**idPostK8SContexts**](SystemAPIApi.md#idPostK8SContexts) | **POST** /api/system/kubernetes/contexts | Handle POST requests for Kubernetes Context list
[**idSystemSync**](SystemAPIApi.md#idSystemSync) | **GET** /api/system/sync | Handle GET request for config sync



## idDeleteAdapterConfig

> idDeleteAdapterConfig(opts)

Handle DELETE requests to delete adapter config

Used to delete adapter configuration

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SystemAPIApi();
let opts = {
  'adapter': "adapter_example" // String | 
};
apiInstance.idDeleteAdapterConfig(opts, (error, data, response) => {
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
 **adapter** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idDeleteK8SConfig

> idDeleteK8SConfig()

Handle DELETE request for Kubernetes Config

Used to delete kubernetes config to System

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SystemAPIApi();
apiInstance.idDeleteK8SConfig((error, data, response) => {
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


## idGetKubernetesPing

> idGetKubernetesPing()

Handle GET request for Kubernetes ping

Fetches server version to simulate ping

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SystemAPIApi();
apiInstance.idGetKubernetesPing((error, data, response) => {
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


## idGetSystemAdapters

> [Adapter] idGetSystemAdapters(opts)

Handle GET request for adapters

Fetches and returns all the adapters and ping adapters

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SystemAPIApi();
let opts = {
  'adapter': "adapter_example" // String | 
};
apiInstance.idGetSystemAdapters(opts, (error, data, response) => {
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
 **adapter** | **String**|  | [optional] 

### Return type

[**[Adapter]**](Adapter.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetSystemVersion

> Version idGetSystemVersion()

Handle GET request for system/server version

Returns the running Meshery version

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SystemAPIApi();
apiInstance.idGetSystemVersion((error, data, response) => {
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

[**Version**](Version.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idMeshSyncGrafana

> {String: [Service]} idMeshSyncGrafana()

Handle GET request for mesh-sync grafana

Fetches Prometheus and Grafana

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SystemAPIApi();
apiInstance.idMeshSyncGrafana((error, data, response) => {
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

**{String: [Service]}**

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idMeshSyncPrometheus

> {String: [Service]} idMeshSyncPrometheus()

Handle GET request for fetching prometheus

Fetches Prometheus

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SystemAPIApi();
apiInstance.idMeshSyncPrometheus((error, data, response) => {
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

**{String: [Service]}**

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idPostAdapterConfig

> [Adapter] idPostAdapterConfig(opts)

Handle POST requests to persist adapter config

Used to persist adapter config

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SystemAPIApi();
let opts = {
  'body': "body_example" // String | 
};
apiInstance.idPostAdapterConfig(opts, (error, data, response) => {
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
 **body** | **String**|  | [optional] 

### Return type

[**[Adapter]**](Adapter.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json


## idPostAdapterOperation

> idPostAdapterOperation(opts)

Handle POST requests for Adapter Operations

Used to send operations to the adapters

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SystemAPIApi();
let opts = {
  'adapter': "adapter_example", // String | 
  'query': "query_example", // String | 
  'customBody': "customBody_example", // String | 
  'namespace': "namespace_example", // String | 
  'deleteOp': "deleteOp_example" // String | 
};
apiInstance.idPostAdapterOperation(opts, (error, data, response) => {
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
 **adapter** | **String**|  | [optional] 
 **query** | **String**|  | [optional] 
 **customBody** | **String**|  | [optional] 
 **namespace** | **String**|  | [optional] 
 **deleteOp** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idPostK8SConfig

> K8SConfig idPostK8SConfig()

Handle POST request for Kubernetes Config

Used to add kubernetes config to System

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SystemAPIApi();
apiInstance.idPostK8SConfig((error, data, response) => {
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

[**K8SConfig**](K8SConfig.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idPostK8SContexts

> [K8SContext] idPostK8SContexts()

Handle POST requests for Kubernetes Context list

Returns the context list for a given k8s config

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SystemAPIApi();
apiInstance.idPostK8SContexts((error, data, response) => {
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

[**[K8SContext]**](K8SContext.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idSystemSync

> Preference idSystemSync()

Handle GET request for config sync

Used to send session data to the UI for initial sync

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SystemAPIApi();
apiInstance.idSystemSync((error, data, response) => {
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

[**Preference**](Preference.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

