# TurbineLabsApi.SharedRulesApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedRulesGet**](SharedRulesApi.md#sharedRulesGet) | **GET** /shared_rules | get shared_rules
[**sharedRulesPost**](SharedRulesApi.md#sharedRulesPost) | **POST** /shared_rules | create shared_rules
[**sharedRulesSharedRulesKeyGet**](SharedRulesApi.md#sharedRulesSharedRulesKeyGet) | **GET** /shared_rules/{sharedRulesKey} | get shared_rules object
[**sharedRulesSharedRulesKeyPut**](SharedRulesApi.md#sharedRulesSharedRulesKeyPut) | **PUT** /shared_rules/{sharedRulesKey} | modify shared_rules object



## sharedRulesGet

> MultiSharedRulesResult sharedRulesGet(opts)

get shared_rules

Get a list of shared_rules

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.SharedRulesApi();
let opts = {
  'filters': "filters_example" // String | A JSON encoded array of SharedRulesFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any SharedRulesFilter will be included. 
};
apiInstance.sharedRulesGet(opts, (error, data, response) => {
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
 **filters** | **String**| A JSON encoded array of SharedRulesFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any SharedRulesFilter will be included.  | [optional] 

### Return type

[**MultiSharedRulesResult**](MultiSharedRulesResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharedRulesPost

> SharedRulesResult sharedRulesPost(sharedRules)

create shared_rules

Create a new shared_rules object

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.SharedRulesApi();
let sharedRules = new TurbineLabsApi.SharedRulesCreate(); // SharedRulesCreate | the shared_rules object to create
apiInstance.sharedRulesPost(sharedRules, (error, data, response) => {
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
 **sharedRules** | [**SharedRulesCreate**](SharedRulesCreate.md)| the shared_rules object to create | 

### Return type

[**SharedRulesResult**](SharedRulesResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sharedRulesSharedRulesKeyGet

> SharedRulesResult sharedRulesSharedRulesKeyGet(sharedRulesKey)

get shared_rules object

Get details for an existing shared_rules object

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.SharedRulesApi();
let sharedRulesKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the shared_rules key
apiInstance.sharedRulesSharedRulesKeyGet(sharedRulesKey, (error, data, response) => {
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
 **sharedRulesKey** | **String**| the shared_rules key | 

### Return type

[**SharedRulesResult**](SharedRulesResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharedRulesSharedRulesKeyPut

> SharedRulesResult sharedRulesSharedRulesKeyPut(sharedRulesKey, sharedRules)

modify shared_rules object

Modify an existing shared_rules object

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.SharedRulesApi();
let sharedRulesKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the shared_rules key
let sharedRules = new TurbineLabsApi.SharedRules(); // SharedRules | the shared_rules object to modify
apiInstance.sharedRulesSharedRulesKeyPut(sharedRulesKey, sharedRules, (error, data, response) => {
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
 **sharedRulesKey** | **String**| the shared_rules key | 
 **sharedRules** | [**SharedRules**](SharedRules.md)| the shared_rules object to modify | 

### Return type

[**SharedRulesResult**](SharedRulesResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

