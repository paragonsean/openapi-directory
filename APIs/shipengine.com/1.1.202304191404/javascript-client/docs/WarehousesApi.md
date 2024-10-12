# ShipEngineApi.WarehousesApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWarehouse**](WarehousesApi.md#createWarehouse) | **POST** /v1/warehouses | Create Warehouse
[**deleteWarehouse**](WarehousesApi.md#deleteWarehouse) | **DELETE** /v1/warehouses/{warehouse_id} | Delete Warehouse By ID
[**getWarehouseById**](WarehousesApi.md#getWarehouseById) | **GET** /v1/warehouses/{warehouse_id} | Get Warehouse By Id
[**listWarehouses**](WarehousesApi.md#listWarehouses) | **GET** /v1/warehouses | List Warehouses
[**updateWarehouse**](WarehousesApi.md#updateWarehouse) | **PUT** /v1/warehouses/{warehouse_id} | Update Warehouse By Id
[**updateWarehouseSettings**](WarehousesApi.md#updateWarehouseSettings) | **PUT** /v1/warehouses/{warehouse_id}/settings | Update Warehouse Settings



## createWarehouse

> CreateWarehouseResponseBody createWarehouse(createWarehouseRequestBody)

Create Warehouse

Create a warehouse location that you can use to create shipping items by simply passing in the generated warehouse id. If the return address is not supplied in the request body then it is assumed that the origin address is the return address as well 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.WarehousesApi();
let createWarehouseRequestBody = new ShipEngineApi.CreateWarehouseRequestBody(); // CreateWarehouseRequestBody | 
apiInstance.createWarehouse(createWarehouseRequestBody, (error, data, response) => {
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
 **createWarehouseRequestBody** | [**CreateWarehouseRequestBody**](CreateWarehouseRequestBody.md)|  | 

### Return type

[**CreateWarehouseResponseBody**](CreateWarehouseResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteWarehouse

> String deleteWarehouse(warehouseId)

Delete Warehouse By ID

Delete a warehouse by ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.WarehousesApi();
let warehouseId = "warehouseId_example"; // String | Warehouse ID
apiInstance.deleteWarehouse(warehouseId, (error, data, response) => {
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
 **warehouseId** | **String**| Warehouse ID | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## getWarehouseById

> GetWarehouseByIdResponseBody getWarehouseById(warehouseId)

Get Warehouse By Id

Retrieve warehouse data based on the warehouse ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.WarehousesApi();
let warehouseId = "warehouseId_example"; // String | Warehouse ID
apiInstance.getWarehouseById(warehouseId, (error, data, response) => {
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
 **warehouseId** | **String**| Warehouse ID | 

### Return type

[**GetWarehouseByIdResponseBody**](GetWarehouseByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWarehouses

> ListWarehousesResponseBody listWarehouses()

List Warehouses

Retrieve a list of warehouses associated with this account.

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.WarehousesApi();
apiInstance.listWarehouses((error, data, response) => {
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

[**ListWarehousesResponseBody**](ListWarehousesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWarehouse

> String updateWarehouse(warehouseId, updateWarehouseRequestBody)

Update Warehouse By Id

Update Warehouse object information

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.WarehousesApi();
let warehouseId = "warehouseId_example"; // String | Warehouse ID
let updateWarehouseRequestBody = new ShipEngineApi.UpdateWarehouseRequestBody(); // UpdateWarehouseRequestBody | 
apiInstance.updateWarehouse(warehouseId, updateWarehouseRequestBody, (error, data, response) => {
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
 **warehouseId** | **String**| Warehouse ID | 
 **updateWarehouseRequestBody** | [**UpdateWarehouseRequestBody**](UpdateWarehouseRequestBody.md)|  | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain


## updateWarehouseSettings

> String updateWarehouseSettings(warehouseId, updateWarehouseSettingsRequestBody)

Update Warehouse Settings

Update Warehouse settings object information

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.WarehousesApi();
let warehouseId = "warehouseId_example"; // String | Warehouse ID
let updateWarehouseSettingsRequestBody = new ShipEngineApi.UpdateWarehouseSettingsRequestBody(); // UpdateWarehouseSettingsRequestBody | 
apiInstance.updateWarehouseSettings(warehouseId, updateWarehouseSettingsRequestBody, (error, data, response) => {
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
 **warehouseId** | **String**| Warehouse ID | 
 **updateWarehouseSettingsRequestBody** | [**UpdateWarehouseSettingsRequestBody**](UpdateWarehouseSettingsRequestBody.md)|  | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain

