# ShipEngineApi.PackageTypesApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPackageType**](PackageTypesApi.md#createPackageType) | **POST** /v1/packages | Create Custom Package Type
[**deletePackageType**](PackageTypesApi.md#deletePackageType) | **DELETE** /v1/packages/{package_id} | Delete A Custom Package By ID
[**getPackageTypeById**](PackageTypesApi.md#getPackageTypeById) | **GET** /v1/packages/{package_id} | Get Custom Package Type By ID
[**listPackageTypes**](PackageTypesApi.md#listPackageTypes) | **GET** /v1/packages | List Custom Package Types
[**updatePackageType**](PackageTypesApi.md#updatePackageType) | **PUT** /v1/packages/{package_id} | Update Custom Package Type By ID



## createPackageType

> CreatePackageTypeResponseBody createPackageType(createPackageTypeRequestBody)

Create Custom Package Type

Create a custom package type to better assist in getting accurate rate estimates

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.PackageTypesApi();
let createPackageTypeRequestBody = new ShipEngineApi.CreatePackageTypeRequestBody(); // CreatePackageTypeRequestBody | 
apiInstance.createPackageType(createPackageTypeRequestBody, (error, data, response) => {
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
 **createPackageTypeRequestBody** | [**CreatePackageTypeRequestBody**](CreatePackageTypeRequestBody.md)|  | 

### Return type

[**CreatePackageTypeResponseBody**](CreatePackageTypeResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deletePackageType

> String deletePackageType(packageId)

Delete A Custom Package By ID

Delete a custom package using the ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.PackageTypesApi();
let packageId = "packageId_example"; // String | Package ID
apiInstance.deletePackageType(packageId, (error, data, response) => {
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
 **packageId** | **String**| Package ID | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## getPackageTypeById

> GetPackageTypeByIdResponseBody getPackageTypeById(packageId)

Get Custom Package Type By ID

Get Custom Package Type by ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.PackageTypesApi();
let packageId = "packageId_example"; // String | Package ID
apiInstance.getPackageTypeById(packageId, (error, data, response) => {
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
 **packageId** | **String**| Package ID | 

### Return type

[**GetPackageTypeByIdResponseBody**](GetPackageTypeByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPackageTypes

> ListPackageTypesResponseBody listPackageTypes()

List Custom Package Types

List the custom package types associated with the account

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.PackageTypesApi();
apiInstance.listPackageTypes((error, data, response) => {
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

[**ListPackageTypesResponseBody**](ListPackageTypesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePackageType

> String updatePackageType(packageId, updatePackageTypeRequestBody)

Update Custom Package Type By ID

Update the custom package type object by ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.PackageTypesApi();
let packageId = "packageId_example"; // String | Package ID
let updatePackageTypeRequestBody = new ShipEngineApi.UpdatePackageTypeRequestBody(); // UpdatePackageTypeRequestBody | 
apiInstance.updatePackageType(packageId, updatePackageTypeRequestBody, (error, data, response) => {
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
 **packageId** | **String**| Package ID | 
 **updatePackageTypeRequestBody** | [**UpdatePackageTypeRequestBody**](UpdatePackageTypeRequestBody.md)|  | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain

