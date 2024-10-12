# LogisticsApi.WarehousesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateWarehouse**](WarehousesApi.md#activateWarehouse) | **POST** /api/logistics/pvt/configuration/warehouses/{warehouseId}/activation | Activate warehouse
[**allWarehouses**](WarehousesApi.md#allWarehouses) | **GET** /api/logistics/pvt/configuration/warehouses | List all warehouses
[**createUpdateWarehouse**](WarehousesApi.md#createUpdateWarehouse) | **POST** /api/logistics/pvt/configuration/warehouses | Create/update warehouse
[**deactivateWarehouse**](WarehousesApi.md#deactivateWarehouse) | **POST** /api/logistics/pvt/configuration/warehouses/{warehouseId}/deactivation | Deactivate warehouse
[**removeWarehouse**](WarehousesApi.md#removeWarehouse) | **DELETE** /api/logistics/pvt/configuration/warehouses/{warehouseId} | Remove warehouse
[**warehouseById**](WarehousesApi.md#warehouseById) | **GET** /api/logistics/pvt/configuration/warehouses/{warehouseId} | List warehouse by ID



## activateWarehouse

> activateWarehouse(contentType, accept, warehouseId)

Activate warehouse

Activates a given warehouse, by warehouse ID.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.WarehousesApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let warehouseId = "warehouseId_example"; // String | 
apiInstance.activateWarehouse(contentType, accept, warehouseId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **warehouseId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## allWarehouses

> [AllWarehouses200ResponseInner] allWarehouses(contentType, accept)

List all warehouses

Lists information about all warehouses set up in your store.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.WarehousesApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
apiInstance.allWarehouses(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]

### Return type

[**[AllWarehouses200ResponseInner]**](AllWarehouses200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## createUpdateWarehouse

> createUpdateWarehouse(accept, contentType, createUpdateWarehouseRequest)

Create/update warehouse

Creates or updates your store&#39;s warehouses

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.WarehousesApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let createUpdateWarehouseRequest = {"id":"15bfc76","name":"Estoque Principal","warehouseDocks":[{"cost":"5.00","costToDisplay":"5,00","dockId":"1a8bce3","name":"Centro de Distribui├º├úo Principal","time":"3.00:00:00","translateDays":"dias"}]}; // CreateUpdateWarehouseRequest | 
apiInstance.createUpdateWarehouse(accept, contentType, createUpdateWarehouseRequest, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **createUpdateWarehouseRequest** | [**CreateUpdateWarehouseRequest**](CreateUpdateWarehouseRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: Not defined


## deactivateWarehouse

> deactivateWarehouse(contentType, accept, warehouseId)

Deactivate warehouse

Deactivates a given warehouse by warehouse ID.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.WarehousesApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let warehouseId = "warehouseId_example"; // String | 
apiInstance.deactivateWarehouse(contentType, accept, warehouseId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **warehouseId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeWarehouse

> removeWarehouse(contentType, accept, warehouseId)

Remove warehouse

Deletes given warehouse by warehouse ID.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.WarehousesApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let warehouseId = "warehouseId_example"; // String | 
apiInstance.removeWarehouse(contentType, accept, warehouseId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **warehouseId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## warehouseById

> WarehouseById200Response warehouseById(contentType, accept, warehouseId)

List warehouse by ID

Lists the information of a given warehouse, searching by warehouse ID.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.WarehousesApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let warehouseId = "warehouseId_example"; // String | 
apiInstance.warehouseById(contentType, accept, warehouseId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **warehouseId** | **String**|  | 

### Return type

[**WarehouseById200Response**](WarehouseById200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

