# AppVeyorRestApi.EnvironmentApi

All URIs are relative to *https://ci.appveyor.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addEnvironment**](EnvironmentApi.md#addEnvironment) | **POST** /environments | Add environment
[**deleteEnvironment**](EnvironmentApi.md#deleteEnvironment) | **DELETE** /environments/{deploymentEnvironmentId} | Delete environment
[**getEnvironmentDeployments**](EnvironmentApi.md#getEnvironmentDeployments) | **GET** /environments/{deploymentEnvironmentId}/deployments | Get environment deployments
[**getEnvironmentSettings**](EnvironmentApi.md#getEnvironmentSettings) | **GET** /environments/{deploymentEnvironmentId}/settings | Get environment settings
[**getEnvironments**](EnvironmentApi.md#getEnvironments) | **GET** /environments | Get environments
[**updateEnvironment**](EnvironmentApi.md#updateEnvironment) | **PUT** /environments | Update environment



## addEnvironment

> DeploymentEnvironmentWithSettings addEnvironment(body)

Add environment

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.EnvironmentApi();
let body = new AppVeyorRestApi.DeploymentEnvironmentAddition(); // DeploymentEnvironmentAddition | 
apiInstance.addEnvironment(body, (error, data, response) => {
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
 **body** | [**DeploymentEnvironmentAddition**](DeploymentEnvironmentAddition.md)|  | 

### Return type

[**DeploymentEnvironmentWithSettings**](DeploymentEnvironmentWithSettings.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## deleteEnvironment

> deleteEnvironment(deploymentEnvironmentId)

Delete environment

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.EnvironmentApi();
let deploymentEnvironmentId = 56; // Number | Deployment Environment ID (`deploymentEnvironmentId` property of `DeploymentEnvironment`) 
apiInstance.deleteEnvironment(deploymentEnvironmentId, (error, data, response) => {
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
 **deploymentEnvironmentId** | **Number**| Deployment Environment ID (&#x60;deploymentEnvironmentId&#x60; property of &#x60;DeploymentEnvironment&#x60;)  | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getEnvironmentDeployments

> DeploymentEnvironmentDeploymentsResults getEnvironmentDeployments(deploymentEnvironmentId)

Get environment deployments

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.EnvironmentApi();
let deploymentEnvironmentId = 56; // Number | Deployment Environment ID (`deploymentEnvironmentId` property of `DeploymentEnvironment`) 
apiInstance.getEnvironmentDeployments(deploymentEnvironmentId, (error, data, response) => {
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
 **deploymentEnvironmentId** | **Number**| Deployment Environment ID (&#x60;deploymentEnvironmentId&#x60; property of &#x60;DeploymentEnvironment&#x60;)  | 

### Return type

[**DeploymentEnvironmentDeploymentsResults**](DeploymentEnvironmentDeploymentsResults.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getEnvironmentSettings

> DeploymentEnvironmentSettingsResults getEnvironmentSettings(deploymentEnvironmentId)

Get environment settings

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.EnvironmentApi();
let deploymentEnvironmentId = 56; // Number | Deployment Environment ID (`deploymentEnvironmentId` property of `DeploymentEnvironment`) 
apiInstance.getEnvironmentSettings(deploymentEnvironmentId, (error, data, response) => {
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
 **deploymentEnvironmentId** | **Number**| Deployment Environment ID (&#x60;deploymentEnvironmentId&#x60; property of &#x60;DeploymentEnvironment&#x60;)  | 

### Return type

[**DeploymentEnvironmentSettingsResults**](DeploymentEnvironmentSettingsResults.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getEnvironments

> [DeploymentEnvironmentLookupModel] getEnvironments()

Get environments

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.EnvironmentApi();
apiInstance.getEnvironments((error, data, response) => {
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

[**[DeploymentEnvironmentLookupModel]**](DeploymentEnvironmentLookupModel.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateEnvironment

> DeploymentEnvironmentWithSettings updateEnvironment(body)

Update environment

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.EnvironmentApi();
let body = new AppVeyorRestApi.DeploymentEnvironmentWithSettings(); // DeploymentEnvironmentWithSettings | 
apiInstance.updateEnvironment(body, (error, data, response) => {
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
 **body** | [**DeploymentEnvironmentWithSettings**](DeploymentEnvironmentWithSettings.md)|  | 

### Return type

[**DeploymentEnvironmentWithSettings**](DeploymentEnvironmentWithSettings.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml

