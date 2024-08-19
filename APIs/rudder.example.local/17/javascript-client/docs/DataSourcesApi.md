# RudderApi.DataSourcesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDataSource**](DataSourcesApi.md#createDataSource) | **PUT** /datasources | Create a data source
[**deleteDataSource**](DataSourcesApi.md#deleteDataSource) | **DELETE** /datasources/{datasourceId} | Delete a data source
[**getAllDataSources**](DataSourcesApi.md#getAllDataSources) | **GET** /datasources | List all data sources
[**getDataSource**](DataSourcesApi.md#getDataSource) | **GET** /datasources/{datasourceId} | Get data source configuration
[**reloadAllDatasourcesAllNodes**](DataSourcesApi.md#reloadAllDatasourcesAllNodes) | **POST** /datasources/reload | Update properties from data sources
[**reloadAllDatasourcesOneNode**](DataSourcesApi.md#reloadAllDatasourcesOneNode) | **POST** /nodes/{nodeId}/fetchData | Update properties for one node from all data sources
[**reloadOneDatasourceAllNodes**](DataSourcesApi.md#reloadOneDatasourceAllNodes) | **POST** /datasources/reload/{datasourceId} | Update properties from data sources
[**reloadOneDatasourceOneNode**](DataSourcesApi.md#reloadOneDatasourceOneNode) | **POST** /nodes/{nodeId}/fetchData/{datasourceId} | Update properties for one node from a data source
[**updateDataSource**](DataSourcesApi.md#updateDataSource) | **POST** /datasources/{datasourceId} | Update a data source configuration



## createDataSource

> CreateDataSource200Response createDataSource(opts)

Create a data source

Create a new data source

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DataSourcesApi();
let opts = {
  'datasource': new RudderApi.Datasource() // Datasource | 
};
apiInstance.createDataSource(opts, (error, data, response) => {
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
 **datasource** | [**Datasource**](Datasource.md)|  | [optional] 

### Return type

[**CreateDataSource200Response**](CreateDataSource200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDataSource

> DeleteDataSource200Response deleteDataSource(datasourceId)

Delete a data source

Delete a data source configuration

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DataSourcesApi();
let datasourceId = "test-data-source"; // String | Id of the data source
apiInstance.deleteDataSource(datasourceId, (error, data, response) => {
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
 **datasourceId** | **String**| Id of the data source | 

### Return type

[**DeleteDataSource200Response**](DeleteDataSource200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllDataSources

> GetAllDataSources200Response getAllDataSources()

List all data sources

Get the configuration of all present data sources

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DataSourcesApi();
apiInstance.getAllDataSources((error, data, response) => {
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

[**GetAllDataSources200Response**](GetAllDataSources200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDataSource

> GetDataSource200Response getDataSource(datasourceId)

Get data source configuration

Get the configuration of a data source

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DataSourcesApi();
let datasourceId = "test-data-source"; // String | Id of the data source
apiInstance.getDataSource(datasourceId, (error, data, response) => {
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
 **datasourceId** | **String**| Id of the data source | 

### Return type

[**GetDataSource200Response**](GetDataSource200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reloadAllDatasourcesAllNodes

> ReloadAllDatasourcesAllNodes200Response reloadAllDatasourcesAllNodes()

Update properties from data sources

Update properties from all data source on all nodes. The call is asynchronous.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DataSourcesApi();
apiInstance.reloadAllDatasourcesAllNodes((error, data, response) => {
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

[**ReloadAllDatasourcesAllNodes200Response**](ReloadAllDatasourcesAllNodes200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reloadAllDatasourcesOneNode

> ReloadAllDatasourcesOneNode200Response reloadAllDatasourcesOneNode(nodeId)

Update properties for one node from all data sources

Update properties from all data sources on one nodes. The call is asynchronous.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DataSourcesApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
apiInstance.reloadAllDatasourcesOneNode(nodeId, (error, data, response) => {
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
 **nodeId** | **String**| Id of the target node | 

### Return type

[**ReloadAllDatasourcesOneNode200Response**](ReloadAllDatasourcesOneNode200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reloadOneDatasourceAllNodes

> ReloadOneDatasourceAllNodes200Response reloadOneDatasourceAllNodes(datasourceId)

Update properties from data sources

Update properties from all data source on all nodes. The call is asynchronous.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DataSourcesApi();
let datasourceId = "test-data-source"; // String | Id of the data source
apiInstance.reloadOneDatasourceAllNodes(datasourceId, (error, data, response) => {
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
 **datasourceId** | **String**| Id of the data source | 

### Return type

[**ReloadOneDatasourceAllNodes200Response**](ReloadOneDatasourceAllNodes200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reloadOneDatasourceOneNode

> ReloadOneDatasourceOneNode200Response reloadOneDatasourceOneNode(nodeId, datasourceId)

Update properties for one node from a data source

Update properties from a data source on one nodes. The call is asynchronous.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DataSourcesApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
let datasourceId = "test-data-source"; // String | Id of the data source
apiInstance.reloadOneDatasourceOneNode(nodeId, datasourceId, (error, data, response) => {
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
 **nodeId** | **String**| Id of the target node | 
 **datasourceId** | **String**| Id of the data source | 

### Return type

[**ReloadOneDatasourceOneNode200Response**](ReloadOneDatasourceOneNode200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDataSource

> UpdateDataSource200Response updateDataSource(datasourceId, opts)

Update a data source configuration

Update the configuration of a data source

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DataSourcesApi();
let datasourceId = "test-data-source"; // String | Id of the data source
let opts = {
  'datasource': new RudderApi.Datasource() // Datasource | 
};
apiInstance.updateDataSource(datasourceId, opts, (error, data, response) => {
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
 **datasourceId** | **String**| Id of the data source | 
 **datasource** | [**Datasource**](Datasource.md)|  | [optional] 

### Return type

[**UpdateDataSource200Response**](UpdateDataSource200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

