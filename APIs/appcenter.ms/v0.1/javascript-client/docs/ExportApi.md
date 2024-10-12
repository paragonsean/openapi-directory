# AppCenterClient.ExportApi

All URIs are relative to *https://api.appcenter.ms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exportConfigurationsCreate**](ExportApi.md#exportConfigurationsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/export_configurations | 
[**exportConfigurationsDelete**](ExportApi.md#exportConfigurationsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id} | 
[**exportConfigurationsDisable**](ExportApi.md#exportConfigurationsDisable) | **POST** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id}/disable | 
[**exportConfigurationsEnable**](ExportApi.md#exportConfigurationsEnable) | **POST** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id}/enable | 
[**exportConfigurationsGet**](ExportApi.md#exportConfigurationsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id} | 
[**exportConfigurationsList**](ExportApi.md#exportConfigurationsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/export_configurations | 
[**exportConfigurationsPartialUpdate**](ExportApi.md#exportConfigurationsPartialUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id} | 



## exportConfigurationsCreate

> ExportConfigurationsList200ResponseValuesInner exportConfigurationsCreate(ownerName, appName, exportConfigurationsList200ResponseValuesInnerExportConfiguration)



Create new export configuration

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ExportApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let exportConfigurationsList200ResponseValuesInnerExportConfiguration = new AppCenterClient.ExportConfigurationsList200ResponseValuesInnerExportConfiguration(); // ExportConfigurationsList200ResponseValuesInnerExportConfiguration | Export configurations.
apiInstance.exportConfigurationsCreate(ownerName, appName, exportConfigurationsList200ResponseValuesInnerExportConfiguration, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **exportConfigurationsList200ResponseValuesInnerExportConfiguration** | [**ExportConfigurationsList200ResponseValuesInnerExportConfiguration**](ExportConfigurationsList200ResponseValuesInnerExportConfiguration.md)| Export configurations. | 

### Return type

[**ExportConfigurationsList200ResponseValuesInner**](ExportConfigurationsList200ResponseValuesInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## exportConfigurationsDelete

> exportConfigurationsDelete(exportConfigurationId, ownerName, appName)



Delete export configuration.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ExportApi();
let exportConfigurationId = "exportConfigurationId_example"; // String | The id of the export configuration.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.exportConfigurationsDelete(exportConfigurationId, ownerName, appName, (error, data, response) => {
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
 **exportConfigurationId** | **String**| The id of the export configuration. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportConfigurationsDisable

> exportConfigurationsDisable(exportConfigurationId, ownerName, appName)



Disable export configuration.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ExportApi();
let exportConfigurationId = "exportConfigurationId_example"; // String | The id of the export configuration.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.exportConfigurationsDisable(exportConfigurationId, ownerName, appName, (error, data, response) => {
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
 **exportConfigurationId** | **String**| The id of the export configuration. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportConfigurationsEnable

> exportConfigurationsEnable(exportConfigurationId, ownerName, appName)



Enable export configuration.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ExportApi();
let exportConfigurationId = "exportConfigurationId_example"; // String | The id of the export configuration.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.exportConfigurationsEnable(exportConfigurationId, ownerName, appName, (error, data, response) => {
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
 **exportConfigurationId** | **String**| The id of the export configuration. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportConfigurationsGet

> ExportConfigurationsList200ResponseValuesInner exportConfigurationsGet(exportConfigurationId, ownerName, appName)



Get export configuration.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ExportApi();
let exportConfigurationId = "exportConfigurationId_example"; // String | The id of the export configuration.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.exportConfigurationsGet(exportConfigurationId, ownerName, appName, (error, data, response) => {
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
 **exportConfigurationId** | **String**| The id of the export configuration. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**ExportConfigurationsList200ResponseValuesInner**](ExportConfigurationsList200ResponseValuesInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportConfigurationsList

> ExportConfigurationsList200Response exportConfigurationsList(ownerName, appName)



List export configurations.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ExportApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.exportConfigurationsList(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**ExportConfigurationsList200Response**](ExportConfigurationsList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportConfigurationsPartialUpdate

> ExportConfigurationsList200ResponseValuesInner exportConfigurationsPartialUpdate(exportConfigurationId, ownerName, appName, exportConfigurationsList200ResponseValuesInnerExportConfiguration)



Partially update export configuration.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.ExportApi();
let exportConfigurationId = "exportConfigurationId_example"; // String | The id of the export configuration.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let exportConfigurationsList200ResponseValuesInnerExportConfiguration = new AppCenterClient.ExportConfigurationsList200ResponseValuesInnerExportConfiguration(); // ExportConfigurationsList200ResponseValuesInnerExportConfiguration | Export configurations.
apiInstance.exportConfigurationsPartialUpdate(exportConfigurationId, ownerName, appName, exportConfigurationsList200ResponseValuesInnerExportConfiguration, (error, data, response) => {
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
 **exportConfigurationId** | **String**| The id of the export configuration. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **exportConfigurationsList200ResponseValuesInnerExportConfiguration** | [**ExportConfigurationsList200ResponseValuesInnerExportConfiguration**](ExportConfigurationsList200ResponseValuesInnerExportConfiguration.md)| Export configurations. | 

### Return type

[**ExportConfigurationsList200ResponseValuesInner**](ExportConfigurationsList200ResponseValuesInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

