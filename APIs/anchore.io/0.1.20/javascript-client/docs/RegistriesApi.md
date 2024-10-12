# AnchoreEngineApiServer.RegistriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRegistry**](RegistriesApi.md#createRegistry) | **POST** /registries | Add a new registry
[**deleteRegistry**](RegistriesApi.md#deleteRegistry) | **DELETE** /registries/{registry} | Delete a registry configuration
[**getRegistry**](RegistriesApi.md#getRegistry) | **GET** /registries/{registry} | Get a specific registry configuration
[**listRegistries**](RegistriesApi.md#listRegistries) | **GET** /registries | List configured registries
[**updateRegistry**](RegistriesApi.md#updateRegistry) | **PUT** /registries/{registry} | Update/replace a registry configuration



## createRegistry

> [RegistryConfiguration] createRegistry(registryConfigurationRequest, opts)

Add a new registry

Adds a new registry to the system

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.RegistriesApi();
let registryConfigurationRequest = new AnchoreEngineApiServer.RegistryConfigurationRequest(); // RegistryConfigurationRequest | 
let opts = {
  'validate': true, // Boolean | flag to determine whether or not to validate registry/credential at registry add time
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.createRegistry(registryConfigurationRequest, opts, (error, data, response) => {
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
 **registryConfigurationRequest** | [**RegistryConfigurationRequest**](RegistryConfigurationRequest.md)|  | 
 **validate** | **Boolean**| flag to determine whether or not to validate registry/credential at registry add time | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[RegistryConfiguration]**](RegistryConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteRegistry

> deleteRegistry(registry, opts)

Delete a registry configuration

Delete a registry configuration record from the system. Does not remove any images.

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.RegistriesApi();
let registry = "registry_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.deleteRegistry(registry, opts, (error, data, response) => {
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
 **registry** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRegistry

> [RegistryConfiguration] getRegistry(registry, opts)

Get a specific registry configuration

Get information on a specific registry

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.RegistriesApi();
let registry = "registry_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getRegistry(registry, opts, (error, data, response) => {
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
 **registry** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[RegistryConfiguration]**](RegistryConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRegistries

> [RegistryConfiguration] listRegistries(opts)

List configured registries

List all configured registries the system can/will watch

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.RegistriesApi();
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.listRegistries(opts, (error, data, response) => {
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
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[RegistryConfiguration]**](RegistryConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRegistry

> [RegistryConfiguration] updateRegistry(registry, registryConfigurationRequest, opts)

Update/replace a registry configuration

Replaces an existing registry record with the given record

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.RegistriesApi();
let registry = "registry_example"; // String | 
let registryConfigurationRequest = new AnchoreEngineApiServer.RegistryConfigurationRequest(); // RegistryConfigurationRequest | 
let opts = {
  'validate': true, // Boolean | flag to determine whether or not to validate registry/credential at registry update time
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.updateRegistry(registry, registryConfigurationRequest, opts, (error, data, response) => {
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
 **registry** | **String**|  | 
 **registryConfigurationRequest** | [**RegistryConfigurationRequest**](RegistryConfigurationRequest.md)|  | 
 **validate** | **Boolean**| flag to determine whether or not to validate registry/credential at registry update time | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[RegistryConfiguration]**](RegistryConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

