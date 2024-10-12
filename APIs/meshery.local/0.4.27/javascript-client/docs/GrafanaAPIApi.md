# MesheryApi.GrafanaAPIApi

All URIs are relative to *http://meshery.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idDeleteGrafanaConfig**](GrafanaAPIApi.md#idDeleteGrafanaConfig) | **DELETE** /api/telemetry/metrics/grafana/config | Handle DELETE request for Grafana configuration
[**idGetGrafana**](GrafanaAPIApi.md#idGetGrafana) | **GET** /api/telemetry/metrics/grafana/scan | Handle GET request for Grafana
[**idGetGrafanaBoards**](GrafanaAPIApi.md#idGetGrafanaBoards) | **GET** /api/telemetry/metrics/grafana/boards | Handle GET request for Grafana boards
[**idGetGrafanaConfig**](GrafanaAPIApi.md#idGetGrafanaConfig) | **GET** /api/telemetry/metrics/grafana/config | Handle GET request for Grafana configuration
[**idGetGrafanaPing**](GrafanaAPIApi.md#idGetGrafanaPing) | **GET** /api/telemetry/metrics/grafana/ping | Handle GET request for Grafana ping
[**idGetGrafanaQuery**](GrafanaAPIApi.md#idGetGrafanaQuery) | **GET** /api/telemetry/metrics/grafana/query | Handle GET request for Grafana queries
[**idPostGrafanaBoards**](GrafanaAPIApi.md#idPostGrafanaBoards) | **POST** /api/telemetry/metrics/grafana/boards | Handle POST request for Grafana boards
[**idPostGrafanaConfig**](GrafanaAPIApi.md#idPostGrafanaConfig) | **POST** /api/telemetry/metrics/grafana/config | Handle POST request for Grafana configuration



## idDeleteGrafanaConfig

> idDeleteGrafanaConfig()

Handle DELETE request for Grafana configuration

Used for Delete Grafana configuration

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.GrafanaAPIApi();
apiInstance.idDeleteGrafanaConfig((error, data, response) => {
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


## idGetGrafana

> {String: [Service]} idGetGrafana()

Handle GET request for Grafana

Fetches and returns Grafana

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.GrafanaAPIApi();
apiInstance.idGetGrafana((error, data, response) => {
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


## idGetGrafanaBoards

> [GrafanaBoard] idGetGrafanaBoards(opts)

Handle GET request for Grafana boards

Used for fetching Grafana boards and panels

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.GrafanaAPIApi();
let opts = {
  'dashboardSearch': "dashboardSearch_example" // String | 
};
apiInstance.idGetGrafanaBoards(opts, (error, data, response) => {
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
 **dashboardSearch** | **String**|  | [optional] 

### Return type

[**[GrafanaBoard]**](GrafanaBoard.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetGrafanaConfig

> Grafana idGetGrafanaConfig()

Handle GET request for Grafana configuration

Used for fetching Grafana configuration

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.GrafanaAPIApi();
apiInstance.idGetGrafanaConfig((error, data, response) => {
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

[**Grafana**](Grafana.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetGrafanaPing

> idGetGrafanaPing()

Handle GET request for Grafana ping

Used to initiate a Grafana ping

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.GrafanaAPIApi();
apiInstance.idGetGrafanaPing((error, data, response) => {
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


## idGetGrafanaQuery

> idGetGrafanaQuery()

Handle GET request for Grafana queries

Used for handling Grafana queries

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.GrafanaAPIApi();
apiInstance.idGetGrafanaQuery((error, data, response) => {
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


## idPostGrafanaBoards

> idPostGrafanaBoards()

Handle POST request for Grafana boards

Used for persist Grafana boards and panel selections

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.GrafanaAPIApi();
apiInstance.idPostGrafanaBoards((error, data, response) => {
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


## idPostGrafanaConfig

> idPostGrafanaConfig(grafanaConfigParams)

Handle POST request for Grafana configuration

Used for persisting Grafana configuration

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.GrafanaAPIApi();
let grafanaConfigParams = new MesheryApi.GrafanaConfigParams(); // GrafanaConfigParams | 
apiInstance.idPostGrafanaConfig(grafanaConfigParams, (error, data, response) => {
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
 **grafanaConfigParams** | [**GrafanaConfigParams**](GrafanaConfigParams.md)|  | 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: Not defined

