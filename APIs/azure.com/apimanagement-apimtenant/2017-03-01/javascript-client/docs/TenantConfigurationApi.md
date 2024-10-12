# ApiManagementClient.TenantConfigurationApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenantConfigurationDeploy**](TenantConfigurationApi.md#tenantConfigurationDeploy) | **POST** /tenant/{configurationName}/deploy | 
[**tenantConfigurationSave**](TenantConfigurationApi.md#tenantConfigurationSave) | **POST** /tenant/{configurationName}/save | 
[**tenantConfigurationValidate**](TenantConfigurationApi.md#tenantConfigurationValidate) | **POST** /tenant/{configurationName}/validate | 



## tenantConfigurationDeploy

> OperationResultContract tenantConfigurationDeploy(apiVersion, configurationName, parameters)



This operation applies changes from the specified Git branch to the configuration database. This is a long running operation and could take several minutes to complete.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.TenantConfigurationApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let configurationName = "configurationName_example"; // String | The identifier of the Git Configuration Operation.
let parameters = new ApiManagementClient.DeployConfigurationParameters(); // DeployConfigurationParameters | Deploy Configuration parameters.
apiInstance.tenantConfigurationDeploy(apiVersion, configurationName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **configurationName** | **String**| The identifier of the Git Configuration Operation. | 
 **parameters** | [**DeployConfigurationParameters**](DeployConfigurationParameters.md)| Deploy Configuration parameters. | 

### Return type

[**OperationResultContract**](OperationResultContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tenantConfigurationSave

> OperationResultContract tenantConfigurationSave(apiVersion, configurationName, parameters)



This operation creates a commit with the current configuration snapshot to the specified branch in the repository. This is a long running operation and could take several minutes to complete.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.TenantConfigurationApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let configurationName = "configurationName_example"; // String | The identifier of the Git Configuration Operation.
let parameters = new ApiManagementClient.SaveConfigurationParameter(); // SaveConfigurationParameter | Save Configuration parameters.
apiInstance.tenantConfigurationSave(apiVersion, configurationName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **configurationName** | **String**| The identifier of the Git Configuration Operation. | 
 **parameters** | [**SaveConfigurationParameter**](SaveConfigurationParameter.md)| Save Configuration parameters. | 

### Return type

[**OperationResultContract**](OperationResultContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tenantConfigurationValidate

> OperationResultContract tenantConfigurationValidate(apiVersion, configurationName, parameters)



This operation validates the changes in the specified Git branch. This is a long running operation and could take several minutes to complete.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.TenantConfigurationApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let configurationName = "configurationName_example"; // String | The identifier of the Git Configuration Operation.
let parameters = new ApiManagementClient.DeployConfigurationParameters(); // DeployConfigurationParameters | Validate Configuration parameters.
apiInstance.tenantConfigurationValidate(apiVersion, configurationName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **configurationName** | **String**| The identifier of the Git Configuration Operation. | 
 **parameters** | [**DeployConfigurationParameters**](DeployConfigurationParameters.md)| Validate Configuration parameters. | 

### Return type

[**OperationResultContract**](OperationResultContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

