# LogisticsApi.InventoryApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSupplyLots**](InventoryApi.md#getSupplyLots) | **GET** /api/logistics/pvt/inventory/items/{skuId}/warehouses/{warehouseId}/supplyLots | List supply lots
[**getinventorywithdispatchedreservations**](InventoryApi.md#getinventorywithdispatchedreservations) | **GET** /api/logistics/pvt/inventory/items/{itemId}/warehouses/{warehouseId}/dispatched | List inventory with dispatched reservations
[**inventoryBySku**](InventoryApi.md#inventoryBySku) | **GET** /api/logistics/pvt/inventory/skus/{skuId} | List inventory by SKU
[**inventoryperdock**](InventoryApi.md#inventoryperdock) | **GET** /api/logistics/pvt/inventory/items/{skuId}/docks/{dockId} | List inventory per dock
[**inventoryperdockandwarehouse**](InventoryApi.md#inventoryperdockandwarehouse) | **GET** /api/logistics/pvt/inventory/items/{skuId}/docks/{dockId}/warehouses/{warehouseId} | List inventory per dock and warehouse
[**inventoryperwarehouse**](InventoryApi.md#inventoryperwarehouse) | **GET** /api/logistics/pvt/inventory/items/{skuId}/warehouses/{warehouseId} | List inventory per warehouse
[**saveSupplyLot**](InventoryApi.md#saveSupplyLot) | **PUT** /api/logistics/pvt/inventory/items/{skuId}/warehouses/{warehouseId}/supplyLots/{supplyLotId} | Save supply lot
[**transferSupplyLot**](InventoryApi.md#transferSupplyLot) | **POST** /api/logistics/pvt/inventory/items/{skuId}/warehouses/{warehouseId}/supplyLots/{supplyLotId}/transfer | Transfer supply lot
[**updateInventoryBySkuandWarehouse**](InventoryApi.md#updateInventoryBySkuandWarehouse) | **PUT** /api/logistics/pvt/inventory/skus/{skuId}/warehouses/{warehouseId} | Update inventory by SKU and warehouse



## getSupplyLots

> getSupplyLots(accept, contentType, skuId, warehouseId)

List supply lots

Returns a list of the supply lots of an SKU in a specific warehouse.

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

let apiInstance = new LogisticsApi.InventoryApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json; charset=utf-8"; // String | Type of the content being sent.
let skuId = "skuId_example"; // String | ID of the SKU.
let warehouseId = "warehouseId_example"; // String | ID of the warehouse where the SKU is located.
apiInstance.getSupplyLots(accept, contentType, skuId, warehouseId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Type of the content being sent. | 
 **skuId** | **String**| ID of the SKU. | 
 **warehouseId** | **String**| ID of the warehouse where the SKU is located. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getinventorywithdispatchedreservations

> [Getinventorywithdispatchedreservations200ResponseInner] getinventorywithdispatchedreservations(contentType, accept, itemId, warehouseId)

List inventory with dispatched reservations

Lists inventory with dispatched reservations. When the number of active reservations is more than 2000 the return is an error with status code 400 (BadRequest) and the message: Too many active reservations.

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

let apiInstance = new LogisticsApi.InventoryApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let itemId = "itemId_example"; // String | 
let warehouseId = "warehouseId_example"; // String | 
apiInstance.getinventorywithdispatchedreservations(contentType, accept, itemId, warehouseId, (error, data, response) => {
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
 **itemId** | **String**|  | 
 **warehouseId** | **String**|  | 

### Return type

[**[Getinventorywithdispatchedreservations200ResponseInner]**](Getinventorywithdispatchedreservations200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## inventoryBySku

> InventoryBySku200Response inventoryBySku(contentType, accept, skuId)

List inventory by SKU

Lists your store&#39;s inventory by SKU ID

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

let apiInstance = new LogisticsApi.InventoryApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let skuId = "skuId_example"; // String | 
apiInstance.inventoryBySku(contentType, accept, skuId, (error, data, response) => {
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
 **skuId** | **String**|  | 

### Return type

[**InventoryBySku200Response**](InventoryBySku200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## inventoryperdock

> [Inventoryperdock200ResponseInner] inventoryperdock(contentType, accept, skuId, dockId)

List inventory per dock

Lists inventory information per dock set up in your store.

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

let apiInstance = new LogisticsApi.InventoryApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let skuId = "skuId_example"; // String | 
let dockId = "dockId_example"; // String | 
apiInstance.inventoryperdock(contentType, accept, skuId, dockId, (error, data, response) => {
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
 **skuId** | **String**|  | 
 **dockId** | **String**|  | 

### Return type

[**[Inventoryperdock200ResponseInner]**](Inventoryperdock200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## inventoryperdockandwarehouse

> [Inventoryperdock200ResponseInner] inventoryperdockandwarehouse(contentType, accept, skuId, dockId, warehouseId)

List inventory per dock and warehouse

Lists information of inventory per dock and warehouse.

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

let apiInstance = new LogisticsApi.InventoryApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let skuId = "skuId_example"; // String | 
let dockId = "dockId_example"; // String | 
let warehouseId = "warehouseId_example"; // String | 
apiInstance.inventoryperdockandwarehouse(contentType, accept, skuId, dockId, warehouseId, (error, data, response) => {
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
 **skuId** | **String**|  | 
 **dockId** | **String**|  | 
 **warehouseId** | **String**|  | 

### Return type

[**[Inventoryperdock200ResponseInner]**](Inventoryperdock200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## inventoryperwarehouse

> [Inventoryperdock200ResponseInner] inventoryperwarehouse(contentType, accept, skuId, warehouseId)

List inventory per warehouse

Lists inventory information per warehouse on your store.

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

let apiInstance = new LogisticsApi.InventoryApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let skuId = "skuId_example"; // String | 
let warehouseId = "warehouseId_example"; // String | 
apiInstance.inventoryperwarehouse(contentType, accept, skuId, warehouseId, (error, data, response) => {
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
 **skuId** | **String**|  | 
 **warehouseId** | **String**|  | 

### Return type

[**[Inventoryperdock200ResponseInner]**](Inventoryperdock200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveSupplyLot

> saveSupplyLot(accept, contentType, skuId, warehouseId, supplyLotId, saveSupplyLot)

Save supply lot

Creates a new Supply Lot. A Supply Lot lets the store sell products that are not currently available in stock but whose arrival is already scheduled.  Check out our [documentation](https://help.vtex.com/en/tutorial/setting-up-future-inventory--UMSGjooqRfkRbeoh94kS4) about this feature.

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

let apiInstance = new LogisticsApi.InventoryApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let skuId = "skuId_example"; // String | ID of the SKU whose availability is being scheduled.
let warehouseId = "warehouseId_example"; // String | ID of the warehouse where the SKU will arrive.
let supplyLotId = "supplyLotId_example"; // String | ID of the Supply Lot in which the SKU's scheduling should be considered.
let saveSupplyLot = {"dateOfSupplyUtc":"2020-04-05T00:00:00+00:00","keepSellingAfterExpiration":true,"quantity":1000}; // SaveSupplyLot | 
apiInstance.saveSupplyLot(accept, contentType, skuId, warehouseId, supplyLotId, saveSupplyLot, (error, data, response) => {
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
 **skuId** | **String**| ID of the SKU whose availability is being scheduled. | 
 **warehouseId** | **String**| ID of the warehouse where the SKU will arrive. | 
 **supplyLotId** | **String**| ID of the Supply Lot in which the SKU&#39;s scheduling should be considered. | 
 **saveSupplyLot** | [**SaveSupplyLot**](SaveSupplyLot.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: Not defined


## transferSupplyLot

> transferSupplyLot(accept, contentType, skuId, warehouseId, supplyLotId)

Transfer supply lot

Transfers an SKU from a Supply Lot to the currently available inventory.  Check out how this transfer works in further detail by reading our [documentation](https://help.vtex.com/pt/tutorial/configurar-estoque-futuro--UMSGjooqRfkRbeoh94kS4) about this feature.

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

let apiInstance = new LogisticsApi.InventoryApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let skuId = "skuId_example"; // String | ID of the SKU.
let warehouseId = "warehouseId_example"; // String | ID of the warehouse where the SKU is located.
let supplyLotId = "supplyLotId_example"; // String | ID of the Supply Lot in which the SKU is currently located and from where it will be transfered.
apiInstance.transferSupplyLot(accept, contentType, skuId, warehouseId, supplyLotId, (error, data, response) => {
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
 **skuId** | **String**| ID of the SKU. | 
 **warehouseId** | **String**| ID of the warehouse where the SKU is located. | 
 **supplyLotId** | **String**| ID of the Supply Lot in which the SKU is currently located and from where it will be transfered. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateInventoryBySkuandWarehouse

> updateInventoryBySkuandWarehouse(accept, contentType, skuId, warehouseId, updateInventoryBySkuandWarehouseRequest1)

Update inventory by SKU and warehouse

Updates inventory for a given SKU and warehouse.

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

let apiInstance = new LogisticsApi.InventoryApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent.
let skuId = "skuId_example"; // String | 
let warehouseId = "warehouseId_example"; // String | 
let updateInventoryBySkuandWarehouseRequest1 = {"dateUtcOnBalanceSystem":"null","quantity":101,"timeToRefill (deprecated)":"00:00:00","unlimitedQuantity":false}; // UpdateInventoryBySkuandWarehouseRequest1 | 
apiInstance.updateInventoryBySkuandWarehouse(accept, contentType, skuId, warehouseId, updateInventoryBySkuandWarehouseRequest1, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **skuId** | **String**|  | 
 **warehouseId** | **String**|  | 
 **updateInventoryBySkuandWarehouseRequest1** | [**UpdateInventoryBySkuandWarehouseRequest1**](UpdateInventoryBySkuandWarehouseRequest1.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: Not defined

