# SwaggerApi2Cart.OrderApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orderAbandonedList**](OrderApi.md#orderAbandonedList) | **GET** /order.abandoned.list.json | 
[**orderAdd**](OrderApi.md#orderAdd) | **POST** /order.add.json | 
[**orderCount**](OrderApi.md#orderCount) | **GET** /order.count.json | 
[**orderFinancialStatusList**](OrderApi.md#orderFinancialStatusList) | **GET** /order.financial_status.list.json | 
[**orderFind**](OrderApi.md#orderFind) | **GET** /order.find.json | 
[**orderFulfillmentStatusList**](OrderApi.md#orderFulfillmentStatusList) | **GET** /order.fulfillment_status.list.json | 
[**orderInfo**](OrderApi.md#orderInfo) | **GET** /order.info.json | 
[**orderList**](OrderApi.md#orderList) | **GET** /order.list.json | 
[**orderPreestimateShippingList**](OrderApi.md#orderPreestimateShippingList) | **POST** /order.preestimate_shipping.list.json | 
[**orderRefundAdd**](OrderApi.md#orderRefundAdd) | **POST** /order.refund.add.json | 
[**orderShipmentAdd**](OrderApi.md#orderShipmentAdd) | **POST** /order.shipment.add.json | 
[**orderShipmentDelete**](OrderApi.md#orderShipmentDelete) | **DELETE** /order.shipment.delete.json | 
[**orderShipmentInfo**](OrderApi.md#orderShipmentInfo) | **GET** /order.shipment.info.json | 
[**orderShipmentList**](OrderApi.md#orderShipmentList) | **GET** /order.shipment.list.json | 
[**orderShipmentTrackingAdd**](OrderApi.md#orderShipmentTrackingAdd) | **POST** /order.shipment.tracking.add.json | 
[**orderShipmentUpdate**](OrderApi.md#orderShipmentUpdate) | **PUT** /order.shipment.update.json | 
[**orderStatusList**](OrderApi.md#orderStatusList) | **GET** /order.status.list.json | 
[**orderTransactionList**](OrderApi.md#orderTransactionList) | **GET** /order.transaction.list.json | 
[**orderUpdate**](OrderApi.md#orderUpdate) | **PUT** /order.update.json | 



## orderAbandonedList

> ModelResponseOrderAbandonedList orderAbandonedList(opts)



Get list of orders that were left by customers before completing the order.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let opts = {
  'customerId': "customerId_example", // String | Retrieves orders specified by customer id
  'customerEmail': "customerEmail_example", // String | Retrieves orders specified by customer email
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'skipEmptyEmail': false, // Boolean | Filter empty emails
  'storeId': "storeId_example", // String | Store Id
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'params': "'customer,totals,items'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example" // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
};
apiInstance.orderAbandonedList(opts, (error, data, response) => {
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
 **customerId** | **String**| Retrieves orders specified by customer id | [optional] 
 **customerEmail** | **String**| Retrieves orders specified by customer email | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **skipEmptyEmail** | **Boolean**| Filter empty emails | [optional] [default to false]
 **storeId** | **String**| Store Id | [optional] 
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;customer,totals,items&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseOrderAbandonedList**](ModelResponseOrderAbandonedList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderAdd

> OrderAdd200Response orderAdd(orderAdd)



Add a new order to the cart.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let orderAdd = new SwaggerApi2Cart.OrderAdd(); // OrderAdd | 
apiInstance.orderAdd(orderAdd, (error, data, response) => {
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
 **orderAdd** | [**OrderAdd**](OrderAdd.md)|  | 

### Return type

[**OrderAdd200Response**](OrderAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orderCount

> OrderCount200Response orderCount(opts)



Count orders in store

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let opts = {
  'customerId': "customerId_example", // String | Counts orders quantity specified by customer id
  'customerEmail': "customerEmail_example", // String | Counts orders quantity specified by customer email
  'orderStatus': "orderStatus_example", // String | Counts orders quantity specified by order status
  'orderStatusIds': ["null"], // [String] | Retrieves orders specified by order statuses
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'storeId': "storeId_example", // String | Counts orders quantity specified by store id
  'ids': "ids_example", // String | Counts orders specified by ids
  'orderIds': "orderIds_example", // String | Counts orders specified by order ids
  'ebayOrderStatus': "ebayOrderStatus_example", // String | Counts orders quantity specified by order status
  'financialStatus': "financialStatus_example", // String | Counts orders quantity specified by financial status
  'fulfillmentStatus': "fulfillmentStatus_example", // String | Create order with fulfillment status
  'shippingMethod': "shippingMethod_example", // String | Retrieve entities according to shipping method
  'deliveryMethod': "deliveryMethod_example", // String | Retrieves order with delivery method
  'shipNodeType': "shipNodeType_example" // String | Retrieves order with ship node type
};
apiInstance.orderCount(opts, (error, data, response) => {
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
 **customerId** | **String**| Counts orders quantity specified by customer id | [optional] 
 **customerEmail** | **String**| Counts orders quantity specified by customer email | [optional] 
 **orderStatus** | **String**| Counts orders quantity specified by order status | [optional] 
 **orderStatusIds** | [**[String]**](String.md)| Retrieves orders specified by order statuses | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **storeId** | **String**| Counts orders quantity specified by store id | [optional] 
 **ids** | **String**| Counts orders specified by ids | [optional] 
 **orderIds** | **String**| Counts orders specified by order ids | [optional] 
 **ebayOrderStatus** | **String**| Counts orders quantity specified by order status | [optional] 
 **financialStatus** | **String**| Counts orders quantity specified by financial status | [optional] 
 **fulfillmentStatus** | **String**| Create order with fulfillment status | [optional] 
 **shippingMethod** | **String**| Retrieve entities according to shipping method | [optional] 
 **deliveryMethod** | **String**| Retrieves order with delivery method | [optional] 
 **shipNodeType** | **String**| Retrieves order with ship node type | [optional] 

### Return type

[**OrderCount200Response**](OrderCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderFinancialStatusList

> OrderFinancialStatusList200Response orderFinancialStatusList()



Retrieve list of financial statuses

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
apiInstance.orderFinancialStatusList((error, data, response) => {
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

[**OrderFinancialStatusList200Response**](OrderFinancialStatusList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderFind

> OrderFind200Response orderFind(opts)



This method is deprecated and won&#39;t be supported in the future. Please use \&quot;order.list\&quot; instead.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let opts = {
  'customerId': "customerId_example", // String | Retrieves orders specified by customer id
  'customerEmail': "customerEmail_example", // String | Retrieves orders specified by customer email
  'orderStatus': "orderStatus_example", // String | Retrieves orders specified by order status
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'params': "'order_id,customer,totals,address,items,bundles,status'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'financialStatus': "financialStatus_example" // String | Retrieves orders specified by financial status
};
apiInstance.orderFind(opts, (error, data, response) => {
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
 **customerId** | **String**| Retrieves orders specified by customer id | [optional] 
 **customerEmail** | **String**| Retrieves orders specified by customer email | [optional] 
 **orderStatus** | **String**| Retrieves orders specified by order status | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;order_id,customer,totals,address,items,bundles,status&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **financialStatus** | **String**| Retrieves orders specified by financial status | [optional] 

### Return type

[**OrderFind200Response**](OrderFind200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderFulfillmentStatusList

> OrderFulfillmentStatusList200Response orderFulfillmentStatusList()



Retrieve list of fulfillment statuses

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
apiInstance.orderFulfillmentStatusList((error, data, response) => {
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

[**OrderFulfillmentStatusList200Response**](OrderFulfillmentStatusList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderInfo

> OrderInfo200Response orderInfo(opts)



Info about a specific order by ID

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let opts = {
  'orderId': "orderId_example", // String | Retrieves order’s info specified by order id
  'id': "id_example", // String | Retrieves order info specified by id
  'params': "'order_id,customer,totals,address,items,bundles,status'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'storeId': "storeId_example", // String | Defines store id where the order should be found
  'enableCache': false // Boolean | If the value is 'true' and order exist in our cache, we will return order.info response from cache
};
apiInstance.orderInfo(opts, (error, data, response) => {
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
 **orderId** | **String**| Retrieves order’s info specified by order id | [optional] 
 **id** | **String**| Retrieves order info specified by id | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;order_id,customer,totals,address,items,bundles,status&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **storeId** | **String**| Defines store id where the order should be found | [optional] 
 **enableCache** | **Boolean**| If the value is &#39;true&#39; and order exist in our cache, we will return order.info response from cache | [optional] [default to false]

### Return type

[**OrderInfo200Response**](OrderInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderList

> ModelResponseOrderList orderList(opts)



Get list of orders from store.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let opts = {
  'customerId': "customerId_example", // String | Retrieves orders specified by customer id
  'customerEmail': "customerEmail_example", // String | Retrieves orders specified by customer email
  'phone': "phone_example", // String | Filter orders by customer's phone number
  'orderStatus': "orderStatus_example", // String | Retrieves orders specified by order status
  'orderStatusIds': ["null"], // [String] | Retrieves orders specified by order statuses
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'pageCursor': "pageCursor_example", // String | Used to retrieve orders via cursor-based pagination (it can't be used with any other filtering parameter)
  'sortBy': "'order_id'", // String | Set field to sort by
  'sortDirection': "'asc'", // String | Set sorting direction
  'params': "'order_id,customer,totals,address,items,bundles,status'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'storeId': "storeId_example", // String | Store Id
  'ids': "ids_example", // String | Retrieves orders specified by ids
  'orderIds': "orderIds_example", // String | Retrieves orders specified by order ids
  'ebayOrderStatus': "ebayOrderStatus_example", // String | Retrieves orders specified by order status
  'basketId': "basketId_example", // String | Retrieves order’s info specified by basket id.
  'financialStatus': "financialStatus_example", // String | Retrieves orders specified by financial status
  'fulfillmentStatus': "fulfillmentStatus_example", // String | Create order with fulfillment status
  'shippingMethod': "shippingMethod_example", // String | Retrieve entities according to shipping method
  'skipOrderIds': "skipOrderIds_example", // String | Skipped orders by ids
  'sinceId': 56, // Number | Retrieve entities starting from the specified id.
  'isDeleted': true, // Boolean | Filter deleted orders
  'shippingCountryIso3': "shippingCountryIso3_example", // String | Retrieve entities according to shipping country
  'enableCache': false, // Boolean | If the value is 'true', we will cache orders for a 15 minutes in order to increase speed and reduce requests throttling for some methods and shoping platforms (for example order.shipment.add)
  'deliveryMethod': "deliveryMethod_example", // String | Retrieves order with delivery method
  'shipNodeType': "shipNodeType_example", // String | Retrieves order with ship node type
  'currencyId': "currencyId_example" // String | Currency Id
};
apiInstance.orderList(opts, (error, data, response) => {
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
 **customerId** | **String**| Retrieves orders specified by customer id | [optional] 
 **customerEmail** | **String**| Retrieves orders specified by customer email | [optional] 
 **phone** | **String**| Filter orders by customer&#39;s phone number | [optional] 
 **orderStatus** | **String**| Retrieves orders specified by order status | [optional] 
 **orderStatusIds** | [**[String]**](String.md)| Retrieves orders specified by order statuses | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **pageCursor** | **String**| Used to retrieve orders via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **sortBy** | **String**| Set field to sort by | [optional] [default to &#39;order_id&#39;]
 **sortDirection** | **String**| Set sorting direction | [optional] [default to &#39;asc&#39;]
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;order_id,customer,totals,address,items,bundles,status&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **ids** | **String**| Retrieves orders specified by ids | [optional] 
 **orderIds** | **String**| Retrieves orders specified by order ids | [optional] 
 **ebayOrderStatus** | **String**| Retrieves orders specified by order status | [optional] 
 **basketId** | **String**| Retrieves order’s info specified by basket id. | [optional] 
 **financialStatus** | **String**| Retrieves orders specified by financial status | [optional] 
 **fulfillmentStatus** | **String**| Create order with fulfillment status | [optional] 
 **shippingMethod** | **String**| Retrieve entities according to shipping method | [optional] 
 **skipOrderIds** | **String**| Skipped orders by ids | [optional] 
 **sinceId** | **Number**| Retrieve entities starting from the specified id. | [optional] 
 **isDeleted** | **Boolean**| Filter deleted orders | [optional] 
 **shippingCountryIso3** | **String**| Retrieve entities according to shipping country | [optional] 
 **enableCache** | **Boolean**| If the value is &#39;true&#39;, we will cache orders for a 15 minutes in order to increase speed and reduce requests throttling for some methods and shoping platforms (for example order.shipment.add) | [optional] [default to false]
 **deliveryMethod** | **String**| Retrieves order with delivery method | [optional] 
 **shipNodeType** | **String**| Retrieves order with ship node type | [optional] 
 **currencyId** | **String**| Currency Id | [optional] 

### Return type

[**ModelResponseOrderList**](ModelResponseOrderList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderPreestimateShippingList

> ModelResponseOrderPreestimateShippingList orderPreestimateShippingList(orderPreestimateShippingList)



Retrieve list of order preestimated shipping methods

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let orderPreestimateShippingList = new SwaggerApi2Cart.OrderPreestimateShippingList(); // OrderPreestimateShippingList | 
apiInstance.orderPreestimateShippingList(orderPreestimateShippingList, (error, data, response) => {
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
 **orderPreestimateShippingList** | [**OrderPreestimateShippingList**](OrderPreestimateShippingList.md)|  | 

### Return type

[**ModelResponseOrderPreestimateShippingList**](ModelResponseOrderPreestimateShippingList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orderRefundAdd

> OrderRefundAdd200Response orderRefundAdd(orderRefundAdd)



Add a refund to the order.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let orderRefundAdd = new SwaggerApi2Cart.OrderRefundAdd(); // OrderRefundAdd | 
apiInstance.orderRefundAdd(orderRefundAdd, (error, data, response) => {
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
 **orderRefundAdd** | [**OrderRefundAdd**](OrderRefundAdd.md)|  | 

### Return type

[**OrderRefundAdd200Response**](OrderRefundAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orderShipmentAdd

> OrderShipmentAdd200Response orderShipmentAdd(orderShipmentAdd)



Add a shipment to the order.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let orderShipmentAdd = new SwaggerApi2Cart.OrderShipmentAdd(); // OrderShipmentAdd | 
apiInstance.orderShipmentAdd(orderShipmentAdd, (error, data, response) => {
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
 **orderShipmentAdd** | [**OrderShipmentAdd**](OrderShipmentAdd.md)|  | 

### Return type

[**OrderShipmentAdd200Response**](OrderShipmentAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orderShipmentDelete

> OrderShipmentDelete200Response orderShipmentDelete(shipmentId, orderId, opts)



Delete order&#39;s shipment.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let shipmentId = "shipmentId_example"; // String | Shipment id indicates the number of delivery
let orderId = "orderId_example"; // String | Defines the order for which the shipment will be deleted
let opts = {
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.orderShipmentDelete(shipmentId, orderId, opts, (error, data, response) => {
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
 **shipmentId** | **String**| Shipment id indicates the number of delivery | 
 **orderId** | **String**| Defines the order for which the shipment will be deleted | 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**OrderShipmentDelete200Response**](OrderShipmentDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderShipmentInfo

> ModelResponseOrderShipmentList orderShipmentInfo(id, orderId, opts)



Get information of shipment.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let id = "id_example"; // String | Entity id
let orderId = "orderId_example"; // String | Defines the order id
let opts = {
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'params': "'id,order_id,items,tracking_numbers'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.orderShipmentInfo(id, orderId, opts, (error, data, response) => {
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
 **id** | **String**| Entity id | 
 **orderId** | **String**| Defines the order id | 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,order_id,items,tracking_numbers&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**ModelResponseOrderShipmentList**](ModelResponseOrderShipmentList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderShipmentList

> ModelResponseOrderShipmentList orderShipmentList(orderId, opts)



Get list of shipments by orders.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let orderId = "orderId_example"; // String | Retrieves shipments specified by order id
let opts = {
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'params': "'id,order_id,items,tracking_numbers'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.orderShipmentList(orderId, opts, (error, data, response) => {
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
 **orderId** | **String**| Retrieves shipments specified by order id | 
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,order_id,items,tracking_numbers&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**ModelResponseOrderShipmentList**](ModelResponseOrderShipmentList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderShipmentTrackingAdd

> OrderShipmentTrackingAdd200Response orderShipmentTrackingAdd(orderShipmentTrackingAdd)



Add order shipment&#39;s tracking info.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let orderShipmentTrackingAdd = new SwaggerApi2Cart.OrderShipmentTrackingAdd(); // OrderShipmentTrackingAdd | 
apiInstance.orderShipmentTrackingAdd(orderShipmentTrackingAdd, (error, data, response) => {
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
 **orderShipmentTrackingAdd** | [**OrderShipmentTrackingAdd**](OrderShipmentTrackingAdd.md)|  | 

### Return type

[**OrderShipmentTrackingAdd200Response**](OrderShipmentTrackingAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orderShipmentUpdate

> AccountConfigUpdate200Response orderShipmentUpdate(orderShipmentUpdate)



Update order&#39;s shipment information.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let orderShipmentUpdate = new SwaggerApi2Cart.OrderShipmentUpdate(); // OrderShipmentUpdate | 
apiInstance.orderShipmentUpdate(orderShipmentUpdate, (error, data, response) => {
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
 **orderShipmentUpdate** | [**OrderShipmentUpdate**](OrderShipmentUpdate.md)|  | 

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orderStatusList

> OrderStatusList200Response orderStatusList(opts)



Retrieve list of statuses

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let opts = {
  'storeId': "storeId_example", // String | Store Id
  'responseFields': "responseFields_example" // String | Set this parameter in order to choose which entity fields you want to retrieve
};
apiInstance.orderStatusList(opts, (error, data, response) => {
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
 **storeId** | **String**| Store Id | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 

### Return type

[**OrderStatusList200Response**](OrderStatusList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderTransactionList

> ModelResponseOrderTransactionList orderTransactionList(orderIds, opts)



Retrieve list of order transaction

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let orderIds = "orderIds_example"; // String | Retrieves order transactions specified by order ids
let opts = {
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'storeId': "storeId_example", // String | Store Id
  'params': "'id,order_id,amount,description'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'pageCursor': "pageCursor_example" // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
};
apiInstance.orderTransactionList(orderIds, opts, (error, data, response) => {
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
 **orderIds** | **String**| Retrieves order transactions specified by order ids | 
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **storeId** | **String**| Store Id | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,order_id,amount,description&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 

### Return type

[**ModelResponseOrderTransactionList**](ModelResponseOrderTransactionList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderUpdate

> AccountConfigUpdate200Response orderUpdate(orderId, opts)



Update existing order.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.OrderApi();
let orderId = "orderId_example"; // String | Defines the orders specified by order id
let opts = {
  'storeId': "storeId_example", // String | Defines store id where the order should be found
  'orderStatus': "orderStatus_example", // String | Defines new order's status
  'comment': "comment_example", // String | Specifies order comment
  'adminComment': "adminComment_example", // String | Specifies admin's order comment
  'adminPrivateComment': "adminPrivateComment_example", // String | Specifies private admin's order comment
  'dateModified': "dateModified_example", // String | Specifies order's  modification date
  'dateFinished': "dateFinished_example", // String | Specifies order's  finished date
  'financialStatus': "financialStatus_example", // String | Update order financial status to specified
  'fulfillmentStatus': "fulfillmentStatus_example", // String | Create order with fulfillment status
  'orderPaymentMethod': "orderPaymentMethod_example", // String | Defines order payment method.<br/>Setting order_payment_method on Shopify will also change financial_status field value to 'paid'
  'sendNotifications': false // Boolean | Send notifications to customer after order was created
};
apiInstance.orderUpdate(orderId, opts, (error, data, response) => {
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
 **orderId** | **String**| Defines the orders specified by order id | 
 **storeId** | **String**| Defines store id where the order should be found | [optional] 
 **orderStatus** | **String**| Defines new order&#39;s status | [optional] 
 **comment** | **String**| Specifies order comment | [optional] 
 **adminComment** | **String**| Specifies admin&#39;s order comment | [optional] 
 **adminPrivateComment** | **String**| Specifies private admin&#39;s order comment | [optional] 
 **dateModified** | **String**| Specifies order&#39;s  modification date | [optional] 
 **dateFinished** | **String**| Specifies order&#39;s  finished date | [optional] 
 **financialStatus** | **String**| Update order financial status to specified | [optional] 
 **fulfillmentStatus** | **String**| Create order with fulfillment status | [optional] 
 **orderPaymentMethod** | **String**| Defines order payment method.&lt;br/&gt;Setting order_payment_method on Shopify will also change financial_status field value to &#39;paid&#39; | [optional] 
 **sendNotifications** | **Boolean**| Send notifications to customer after order was created | [optional] [default to false]

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

