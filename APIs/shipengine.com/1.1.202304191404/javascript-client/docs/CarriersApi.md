# ShipEngineApi.CarriersApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addFundsToCarrier**](CarriersApi.md#addFundsToCarrier) | **PUT** /v1/carriers/{carrier_id}/add_funds | Add Funds To Carrier
[**getCarrierById**](CarriersApi.md#getCarrierById) | **GET** /v1/carriers/{carrier_id} | Get Carrier By ID
[**getCarrierOptions**](CarriersApi.md#getCarrierOptions) | **GET** /v1/carriers/{carrier_id}/options | Get Carrier Options
[**listCarrierPackageTypes**](CarriersApi.md#listCarrierPackageTypes) | **GET** /v1/carriers/{carrier_id}/packages | List Carrier Package Types
[**listCarrierServices**](CarriersApi.md#listCarrierServices) | **GET** /v1/carriers/{carrier_id}/services | List Carrier Services
[**listCarriers**](CarriersApi.md#listCarriers) | **GET** /v1/carriers | List Carriers



## addFundsToCarrier

> AddFundsToCarrierResponseBody addFundsToCarrier(carrierId, addFundsToCarrierRequestBody)

Add Funds To Carrier

Add Funds To A Carrier

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.CarriersApi();
let carrierId = "se-28529731"; // String | Carrier ID
let addFundsToCarrierRequestBody = new ShipEngineApi.AddFundsToCarrierRequestBody(); // AddFundsToCarrierRequestBody | 
apiInstance.addFundsToCarrier(carrierId, addFundsToCarrierRequestBody, (error, data, response) => {
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
 **carrierId** | **String**| Carrier ID | 
 **addFundsToCarrierRequestBody** | [**AddFundsToCarrierRequestBody**](AddFundsToCarrierRequestBody.md)|  | 

### Return type

[**AddFundsToCarrierResponseBody**](AddFundsToCarrierResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCarrierById

> GetCarrierByIdResponseBody getCarrierById(carrierId)

Get Carrier By ID

Retrive carrier info by ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.CarriersApi();
let carrierId = "se-28529731"; // String | Carrier ID
apiInstance.getCarrierById(carrierId, (error, data, response) => {
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
 **carrierId** | **String**| Carrier ID | 

### Return type

[**GetCarrierByIdResponseBody**](GetCarrierByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCarrierOptions

> GetCarrierOptionsResponseBody getCarrierOptions(carrierId)

Get Carrier Options

Get a list of the options available for the carrier

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.CarriersApi();
let carrierId = "se-28529731"; // String | Carrier ID
apiInstance.getCarrierOptions(carrierId, (error, data, response) => {
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
 **carrierId** | **String**| Carrier ID | 

### Return type

[**GetCarrierOptionsResponseBody**](GetCarrierOptionsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCarrierPackageTypes

> ListCarrierPackageTypesResponseBody listCarrierPackageTypes(carrierId)

List Carrier Package Types

List the package types associated with the carrier

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.CarriersApi();
let carrierId = "se-28529731"; // String | Carrier ID
apiInstance.listCarrierPackageTypes(carrierId, (error, data, response) => {
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
 **carrierId** | **String**| Carrier ID | 

### Return type

[**ListCarrierPackageTypesResponseBody**](ListCarrierPackageTypesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCarrierServices

> ListCarrierServicesResponseBody listCarrierServices(carrierId)

List Carrier Services

List the services associated with the carrier ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.CarriersApi();
let carrierId = "se-28529731"; // String | Carrier ID
apiInstance.listCarrierServices(carrierId, (error, data, response) => {
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
 **carrierId** | **String**| Carrier ID | 

### Return type

[**ListCarrierServicesResponseBody**](ListCarrierServicesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCarriers

> GetCarriersResponseBody listCarriers()

List Carriers

List all carriers that have been added to this account

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.CarriersApi();
apiInstance.listCarriers((error, data, response) => {
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

[**GetCarriersResponseBody**](GetCarriersResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

