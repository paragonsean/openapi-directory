# ConfigCatPublicManagementApi.ConfigsApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConfig**](ConfigsApi.md#createConfig) | **POST** /v1/products/{productId}/configs | Create Config
[**deleteConfig**](ConfigsApi.md#deleteConfig) | **DELETE** /v1/configs/{configId} | Delete Config
[**getConfig**](ConfigsApi.md#getConfig) | **GET** /v1/configs/{configId} | Get Config
[**getConfigs**](ConfigsApi.md#getConfigs) | **GET** /v1/products/{productId}/configs | List Configs
[**updateConfig**](ConfigsApi.md#updateConfig) | **PUT** /v1/configs/{configId} | Update Config



## createConfig

> ConfigModelHaljson createConfig(productId, createConfigRequest)

Create Config

This endpoint creates a new Config in a specified Product  identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.ConfigsApi();
let productId = "productId_example"; // String | The identifier of the Product.
let createConfigRequest = new ConfigCatPublicManagementApi.CreateConfigRequest(); // CreateConfigRequest | 
apiInstance.createConfig(productId, createConfigRequest, (error, data, response) => {
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
 **createConfigRequest** | [**CreateConfigRequest**](CreateConfigRequest.md)|  | 

### Return type

[**ConfigModelHaljson**](ConfigModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json


## deleteConfig

> deleteConfig(configId)

Delete Config

This endpoint removes a Config identified by the &#x60;configId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.ConfigsApi();
let configId = "configId_example"; // String | The identifier of the Config.
apiInstance.deleteConfig(configId, (error, data, response) => {
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
 **configId** | **String**| The identifier of the Config. | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getConfig

> ConfigModelHaljson getConfig(configId)

Get Config

This endpoint returns the metadata of a Config identified by the &#x60;configId&#x60;.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.ConfigsApi();
let configId = "configId_example"; // String | The identifier of the Config.
apiInstance.getConfig(configId, (error, data, response) => {
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
 **configId** | **String**| The identifier of the Config. | 

### Return type

[**ConfigModelHaljson**](ConfigModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getConfigs

> [ConfigModelHaljson] getConfigs(productId)

List Configs

This endpoint returns the list of the Configs that belongs to the given Product identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.ConfigsApi();
let productId = "productId_example"; // String | The identifier of the Product.
apiInstance.getConfigs(productId, (error, data, response) => {
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

[**[ConfigModelHaljson]**](ConfigModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## updateConfig

> ConfigModelHaljson updateConfig(configId, updateConfigRequest)

Update Config

This endpoint updates a Config identified by the &#x60;configId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.ConfigsApi();
let configId = "configId_example"; // String | The identifier of the Config.
let updateConfigRequest = new ConfigCatPublicManagementApi.UpdateConfigRequest(); // UpdateConfigRequest | 
apiInstance.updateConfig(configId, updateConfigRequest, (error, data, response) => {
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
 **configId** | **String**| The identifier of the Config. | 
 **updateConfigRequest** | [**UpdateConfigRequest**](UpdateConfigRequest.md)|  | 

### Return type

[**ConfigModelHaljson**](ConfigModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json

