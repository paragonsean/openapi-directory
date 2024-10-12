# ConfigCatPublicManagementApi.EnvironmentsApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEnvironment**](EnvironmentsApi.md#createEnvironment) | **POST** /v1/products/{productId}/environments | Create Environment
[**deleteEnvironment**](EnvironmentsApi.md#deleteEnvironment) | **DELETE** /v1/environments/{environmentId} | Delete Environment
[**getEnvironment**](EnvironmentsApi.md#getEnvironment) | **GET** /v1/environments/{environmentId} | Get Environment
[**getEnvironments**](EnvironmentsApi.md#getEnvironments) | **GET** /v1/products/{productId}/environments | List Environments
[**updateEnvironment**](EnvironmentsApi.md#updateEnvironment) | **PUT** /v1/environments/{environmentId} | Update Environment



## createEnvironment

> EnvironmentModelHaljson createEnvironment(productId, createEnvironmentModel)

Create Environment

This endpoint creates a new Environment in a specified Product  identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.EnvironmentsApi();
let productId = "productId_example"; // String | The identifier of the Product.
let createEnvironmentModel = new ConfigCatPublicManagementApi.CreateEnvironmentModel(); // CreateEnvironmentModel | 
apiInstance.createEnvironment(productId, createEnvironmentModel, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 
 **createEnvironmentModel** | [**CreateEnvironmentModel**](CreateEnvironmentModel.md)|  | 

### Return type

[**EnvironmentModelHaljson**](EnvironmentModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json


## deleteEnvironment

> deleteEnvironment(environmentId)

Delete Environment

This endpoint removes an Environment identified by the &#x60;environmentId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.EnvironmentsApi();
let environmentId = "environmentId_example"; // String | The identifier of the Environment.
apiInstance.deleteEnvironment(environmentId, (error, data, response) => {
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
 **environmentId** | **String**| The identifier of the Environment. | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getEnvironment

> EnvironmentModelHaljson getEnvironment(environmentId)

Get Environment

This endpoint returns the metadata of an Environment  identified by the &#x60;environmentId&#x60;.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.EnvironmentsApi();
let environmentId = "environmentId_example"; // String | The identifier of the Environment.
apiInstance.getEnvironment(environmentId, (error, data, response) => {
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
 **environmentId** | **String**| The identifier of the Environment. | 

### Return type

[**EnvironmentModelHaljson**](EnvironmentModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getEnvironments

> [EnvironmentModelHaljson] getEnvironments(productId)

List Environments

This endpoint returns the list of the Environments that belongs to the given Product identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.EnvironmentsApi();
let productId = "productId_example"; // String | The identifier of the Product.
apiInstance.getEnvironments(productId, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 

### Return type

[**[EnvironmentModelHaljson]**](EnvironmentModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## updateEnvironment

> EnvironmentModelHaljson updateEnvironment(environmentId, updateEnvironmentModel)

Update Environment

This endpoint updates an Environment identified by the &#x60;environmentId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.EnvironmentsApi();
let environmentId = "environmentId_example"; // String | The identifier of the Environment.
let updateEnvironmentModel = new ConfigCatPublicManagementApi.UpdateEnvironmentModel(); // UpdateEnvironmentModel | 
apiInstance.updateEnvironment(environmentId, updateEnvironmentModel, (error, data, response) => {
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
 **environmentId** | **String**| The identifier of the Environment. | 
 **updateEnvironmentModel** | [**UpdateEnvironmentModel**](UpdateEnvironmentModel.md)|  | 

### Return type

[**EnvironmentModelHaljson**](EnvironmentModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json

