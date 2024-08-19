# AppVeyorRestApi.DeploymentApi

All URIs are relative to *https://ci.appveyor.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelDeployment**](DeploymentApi.md#cancelDeployment) | **PUT** /deployments/stop | Cancel deployment
[**getDeployment**](DeploymentApi.md#getDeployment) | **GET** /deployments/{deploymentId} | Get deployment
[**startDeployment**](DeploymentApi.md#startDeployment) | **POST** /deployments | Start deployment



## cancelDeployment

> cancelDeployment(body)

Cancel deployment

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.DeploymentApi();
let body = new AppVeyorRestApi.DeploymentCancellation(); // DeploymentCancellation | 
apiInstance.cancelDeployment(body, (error, data, response) => {
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
 **body** | [**DeploymentCancellation**](DeploymentCancellation.md)|  | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## getDeployment

> ProjectDeployment getDeployment(deploymentId)

Get deployment

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.DeploymentApi();
let deploymentId = 56; // Number | Deployment ID (`deploymentId` property of `Deployment`)
apiInstance.getDeployment(deploymentId, (error, data, response) => {
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
 **deploymentId** | **Number**| Deployment ID (&#x60;deploymentId&#x60; property of &#x60;Deployment&#x60;) | 

### Return type

[**ProjectDeployment**](ProjectDeployment.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## startDeployment

> Deployment startDeployment(body)

Start deployment

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.DeploymentApi();
let body = new AppVeyorRestApi.DeploymentStartRequest(); // DeploymentStartRequest | 
apiInstance.startDeployment(body, (error, data, response) => {
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
 **body** | [**DeploymentStartRequest**](DeploymentStartRequest.md)|  | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml

