# MesheryApi.PrometheusAPIApi

All URIs are relative to *http://meshery.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idDeletePrometheusConfig**](PrometheusAPIApi.md#idDeletePrometheusConfig) | **DELETE** /api/telemetry/metrics/config | Handle DELETE for Prometheus configuration
[**idGetPrometheusConfig**](PrometheusAPIApi.md#idGetPrometheusConfig) | **GET** /api/telemetry/metrics/config | Handle GET for Prometheus configuration
[**idGetPrometheusPing**](PrometheusAPIApi.md#idGetPrometheusPing) | **GET** /api/telemetry/metrics/ping | Handle GET request for Prometheus Ping
[**idGetPrometheusQuery**](PrometheusAPIApi.md#idGetPrometheusQuery) | **GET** /api/telemetry/metrics/query | Handle GET request for Prometheus Query
[**idGetPrometheusStaticBoard**](PrometheusAPIApi.md#idGetPrometheusStaticBoard) | **GET** /api/telemetry/metrics/static-board | Handle GET request for Prometheus static board
[**idPostPrometheusBoard**](PrometheusAPIApi.md#idPostPrometheusBoard) | **POST** /api/telemetry/metrics/boards | Handle POST request for Prometheus board
[**idPostPrometheusBoardImport**](PrometheusAPIApi.md#idPostPrometheusBoardImport) | **POST** /api/telemetry/metrics/board_import | Handle POST request for Prometheus board import
[**idPostPrometheusConfig**](PrometheusAPIApi.md#idPostPrometheusConfig) | **POST** /api/telemetry/metrics/config | Handle POST for Prometheus configuration



## idDeletePrometheusConfig

> idDeletePrometheusConfig()

Handle DELETE for Prometheus configuration

Used for deleting Prometheus configuration

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PrometheusAPIApi();
apiInstance.idDeletePrometheusConfig((error, data, response) => {
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


## idGetPrometheusConfig

> Prometheus idGetPrometheusConfig()

Handle GET for Prometheus configuration

Used for fetching Prometheus configuration

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PrometheusAPIApi();
apiInstance.idGetPrometheusConfig((error, data, response) => {
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

[**Prometheus**](Prometheus.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetPrometheusPing

> idGetPrometheusPing()

Handle GET request for Prometheus Ping

Used to ping prometheus

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PrometheusAPIApi();
apiInstance.idGetPrometheusPing((error, data, response) => {
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


## idGetPrometheusQuery

> idGetPrometheusQuery()

Handle GET request for Prometheus Query

Used to prometheus queries

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PrometheusAPIApi();
apiInstance.idGetPrometheusQuery((error, data, response) => {
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


## idGetPrometheusStaticBoard

> {String: GrafanaBoard} idGetPrometheusStaticBoard()

Handle GET request for Prometheus static board

Used to fetch the static board

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PrometheusAPIApi();
apiInstance.idGetPrometheusStaticBoard((error, data, response) => {
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

[**{String: GrafanaBoard}**](GrafanaBoard.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idPostPrometheusBoard

> idPostPrometheusBoard(selectedGrafanaConfig)

Handle POST request for Prometheus board

Used to persist selected board and panels

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PrometheusAPIApi();
let selectedGrafanaConfig = [new MesheryApi.SelectedGrafanaConfig()]; // [SelectedGrafanaConfig] | 
apiInstance.idPostPrometheusBoard(selectedGrafanaConfig, (error, data, response) => {
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
 **selectedGrafanaConfig** | [**[SelectedGrafanaConfig]**](SelectedGrafanaConfig.md)|  | 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: Not defined


## idPostPrometheusBoardImport

> GrafanaBoard idPostPrometheusBoardImport()

Handle POST request for Prometheus board import

Used for importing Grafana board for Prometheus

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PrometheusAPIApi();
apiInstance.idPostPrometheusBoardImport((error, data, response) => {
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

[**GrafanaBoard**](GrafanaBoard.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idPostPrometheusConfig

> idPostPrometheusConfig(opts)

Handle POST for Prometheus configuration

Used for persisting Prometheus configuration

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.PrometheusAPIApi();
let opts = {
  'body': "body_example" // String | 
};
apiInstance.idPostPrometheusConfig(opts, (error, data, response) => {
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
 **body** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: Not defined

