# OrdersApi.Version3Api

All URIs are relative to *https://developer.walmart.com/orderProxy/order-api-doc-app/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledgeOrders**](Version3Api.md#acknowledgeOrders) | **POST** /v3/orders/{purchaseOrderId}/acknowledge | Acknowledge orders
[**cancelOrder**](Version3Api.md#cancelOrder) | **POST** /v3/orders/{purchaseOrderId}/cancel | Cancel order lines
[**getAllOrders**](Version3Api.md#getAllOrders) | **GET** /v3/orders | Get all orders
[**getAllOrdersNext**](Version3Api.md#getAllOrdersNext) | **GET** /v3/orders{nextCursor} | Get orders for next page
[**getNextCursorReleasedOrders**](Version3Api.md#getNextCursorReleasedOrders) | **GET** /v3/orders/released{nextCursor} | Get released orders for next page
[**getOrderByPurchaseOrderId**](Version3Api.md#getOrderByPurchaseOrderId) | **GET** /v3/orders/{purchaseOrderId} | Get an order
[**getReleasedOrders**](Version3Api.md#getReleasedOrders) | **GET** /v3/orders/released | Get all released orders
[**refundOrder**](Version3Api.md#refundOrder) | **POST** /v3/orders/{purchaseOrderId}/refund | Refund order lines
[**shippingOrder**](Version3Api.md#shippingOrder) | **POST** /v3/orders/{purchaseOrderId}/shipping | Shipping updates



## acknowledgeOrders

> acknowledgeOrders(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, opts)

Acknowledge orders

You can acknowledge an entire order, including all of its order lines. Walmart business rules require to acknowledge orders within four hour of receipt of the order, except in extenuating circumstances.

### Example

```javascript
import OrdersApi from 'orders_api';

let apiInstance = new OrdersApi.Version3Api();
let purchaseOrderId = "purchaseOrderId_example"; // String | Purchase Order ID
let contentType = "'application/xml'"; // String | application/xml, application/json
let accept = "'application/xml'"; // String | application/xml, application/json
let WM_CONSUMER_CHANNEL_TYPE = "'SWAGGER_CHANNEL_TYPE'"; // String | Channel Type
let WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
let WM_SEC_TIMESTAMP = "'Auto populated'"; // String | Epoch timestamp
let WM_SEC_AUTH_SIGNATURE = "'Auto populated'"; // String | Authentication signature
let WM_SVC_NAME = "'Walmart Marketplace'"; // String | The Service name
let WM_QOS_CORRELATION_ID = "'123456abcdef'"; // String | A Transaction ID
let opts = {
  'shipNode': "shipNode_example" // String | Ship Node
};
apiInstance.acknowledgeOrders(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, opts, (error, data, response) => {
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
 **purchaseOrderId** | **String**| Purchase Order ID | 
 **contentType** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **accept** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to &#39;SWAGGER_CHANNEL_TYPE&#39;]
 **WM_CONSUMER_ID** | **String**| Your Consumer ID | 
 **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to &#39;Auto populated&#39;]
 **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to &#39;Auto populated&#39;]
 **WM_SVC_NAME** | **String**| The Service name | [default to &#39;Walmart Marketplace&#39;]
 **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to &#39;123456abcdef&#39;]
 **shipNode** | **String**| Ship Node | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## cancelOrder

> cancelOrder(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, requestBody, opts)

Cancel order lines

You can cancel one or more order lines. You must include a purchaseOrderLineNumber when cancelling an order. After cancelling your order, update the inventory for the cancelled order and send it in the next inventory feed.

### Example

```javascript
import OrdersApi from 'orders_api';

let apiInstance = new OrdersApi.Version3Api();
let purchaseOrderId = "purchaseOrderId_example"; // String | Purchase Order ID
let contentType = "'application/xml'"; // String | application/xml, application/json
let accept = "'application/xml'"; // String | application/xml, application/json
let WM_CONSUMER_CHANNEL_TYPE = "'SWAGGER_CHANNEL_TYPE'"; // String | Channel Type
let WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
let WM_SEC_TIMESTAMP = "'Auto populated'"; // String | Epoch timestamp
let WM_SEC_AUTH_SIGNATURE = "'Auto populated'"; // String | Authentication signature
let WM_SVC_NAME = "'Walmart Marketplace'"; // String | The Service name
let WM_QOS_CORRELATION_ID = "'123456abcdef'"; // String | A Transaction ID
let requestBody = "requestBody_example"; // String | Request body
let opts = {
  'shipNode': "shipNode_example" // String | Ship Node
};
apiInstance.cancelOrder(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, requestBody, opts, (error, data, response) => {
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
 **purchaseOrderId** | **String**| Purchase Order ID | 
 **contentType** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **accept** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to &#39;SWAGGER_CHANNEL_TYPE&#39;]
 **WM_CONSUMER_ID** | **String**| Your Consumer ID | 
 **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to &#39;Auto populated&#39;]
 **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to &#39;Auto populated&#39;]
 **WM_SVC_NAME** | **String**| The Service name | [default to &#39;Walmart Marketplace&#39;]
 **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to &#39;123456abcdef&#39;]
 **requestBody** | **String**| Request body | 
 **shipNode** | **String**| Ship Node | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/xml, application/json
- **Accept**: Not defined


## getAllOrders

> getAllOrders(contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, opts)

Get all orders

You can display a list of all orders with the query parameter filter criteria.

### Example

```javascript
import OrdersApi from 'orders_api';

let apiInstance = new OrdersApi.Version3Api();
let contentType = "'application/xml'"; // String | application/xml, application/json
let accept = "'application/xml'"; // String | application/xml, application/json
let WM_CONSUMER_CHANNEL_TYPE = "'SWAGGER_CHANNEL_TYPE'"; // String | Channel Type
let WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
let WM_SEC_TIMESTAMP = "'Auto populated'"; // String | Epoch timestamp
let WM_SEC_AUTH_SIGNATURE = "'Auto populated'"; // String | Authentication signature
let WM_SVC_NAME = "'Walmart Marketplace'"; // String | The Service name
let WM_QOS_CORRELATION_ID = "'123456abcdef'"; // String | A Transaction ID
let opts = {
  'shipNode': "shipNode_example", // String | Ship Node
  'sku': "sku_example", // String | Retrieves all orders with the specified SKU.
  'customerOrderId': "customerOrderId_example", // String | Retrives the details of the specified customerOrderId.
  'purchaseOrderId': "purchaseOrderId_example", // String | The purchase order ID associated with the order to retrieve. One customer order can have multiple purchase orders associated with it.
  'status': "status_example", // String | The list of orders corresponding to the requested status.
  'createdStartDate': "createdStartDate_example", // String | Limit orders to those created after this date or a timestamp.
  'createdEndDate': "createdEndDate_example", // String | Limit orders to those created before this date or timestamp.
  'fromExpectedShipDate': "fromExpectedShipDate_example", // String | Limit orders to those that have order lines with an expected ship date after this date.
  'toExpectedShipDate': "toExpectedShipDate_example", // String | Limit orders to those that have order lines with an expected ship date before this date. 
  'limit': 10 // Number | The number of orders to be returned. Do not set this parameter to over 200 orders.
};
apiInstance.getAllOrders(contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, opts, (error, data, response) => {
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
 **contentType** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **accept** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to &#39;SWAGGER_CHANNEL_TYPE&#39;]
 **WM_CONSUMER_ID** | **String**| Your Consumer ID | 
 **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to &#39;Auto populated&#39;]
 **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to &#39;Auto populated&#39;]
 **WM_SVC_NAME** | **String**| The Service name | [default to &#39;Walmart Marketplace&#39;]
 **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to &#39;123456abcdef&#39;]
 **shipNode** | **String**| Ship Node | [optional] 
 **sku** | **String**| Retrieves all orders with the specified SKU. | [optional] 
 **customerOrderId** | **String**| Retrives the details of the specified customerOrderId. | [optional] 
 **purchaseOrderId** | **String**| The purchase order ID associated with the order to retrieve. One customer order can have multiple purchase orders associated with it. | [optional] 
 **status** | **String**| The list of orders corresponding to the requested status. | [optional] 
 **createdStartDate** | **String**| Limit orders to those created after this date or a timestamp. | [optional] 
 **createdEndDate** | **String**| Limit orders to those created before this date or timestamp. | [optional] 
 **fromExpectedShipDate** | **String**| Limit orders to those that have order lines with an expected ship date after this date. | [optional] 
 **toExpectedShipDate** | **String**| Limit orders to those that have order lines with an expected ship date before this date.  | [optional] 
 **limit** | **Number**| The number of orders to be returned. Do not set this parameter to over 200 orders. | [optional] [default to 10]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllOrdersNext

> getAllOrdersNext(nextCursor, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID)

Get orders for next page

You can display a list of all orders with nextCursor path parameter pagination criteria.

### Example

```javascript
import OrdersApi from 'orders_api';

let apiInstance = new OrdersApi.Version3Api();
let nextCursor = "nextCursor_example"; // String | Used for pagination when there are more than 200 orders to retrieve. The nextCursor value of the returned response includes a link to another GET call to retrieve the next page. Copy the link and paste it in the next call.
let contentType = "'application/xml'"; // String | application/xml, application/json
let accept = "'application/xml'"; // String | application/xml, application/json
let WM_CONSUMER_CHANNEL_TYPE = "'SWAGGER_CHANNEL_TYPE'"; // String | Channel Type
let WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
let WM_SEC_TIMESTAMP = "'Auto populated'"; // String | Epoch timestamp
let WM_SEC_AUTH_SIGNATURE = "'Auto populated'"; // String | Authentication signature
let WM_SVC_NAME = "'Walmart Marketplace'"; // String | The Service name
let WM_QOS_CORRELATION_ID = "'123456abcdef'"; // String | A Transaction ID
apiInstance.getAllOrdersNext(nextCursor, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, (error, data, response) => {
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
 **nextCursor** | **String**| Used for pagination when there are more than 200 orders to retrieve. The nextCursor value of the returned response includes a link to another GET call to retrieve the next page. Copy the link and paste it in the next call. | 
 **contentType** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **accept** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to &#39;SWAGGER_CHANNEL_TYPE&#39;]
 **WM_CONSUMER_ID** | **String**| Your Consumer ID | 
 **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to &#39;Auto populated&#39;]
 **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to &#39;Auto populated&#39;]
 **WM_SVC_NAME** | **String**| The Service name | [default to &#39;Walmart Marketplace&#39;]
 **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to &#39;123456abcdef&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNextCursorReleasedOrders

> getNextCursorReleasedOrders(nextCursor, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID)

Get released orders for next page

You can display all released orders that have been created and are ready for fulfilment with nextCursor path parameter.

### Example

```javascript
import OrdersApi from 'orders_api';

let apiInstance = new OrdersApi.Version3Api();
let nextCursor = "nextCursor_example"; // String | Used for pagination when there are more than 200 orders to retrieve. The nextCursor value of the returned response includes a link to another GET call to retrieve the next page. Copy the link and paste it in the next call.
let contentType = "'application/xml'"; // String | application/xml, application/json
let accept = "'application/xml'"; // String | application/xml, application/json
let WM_CONSUMER_CHANNEL_TYPE = "'SWAGGER_CHANNEL_TYPE'"; // String | Channel Type
let WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
let WM_SEC_TIMESTAMP = "'Auto populated'"; // String | Epoch timestamp
let WM_SEC_AUTH_SIGNATURE = "'Auto populated'"; // String | Authentication signature
let WM_SVC_NAME = "'Walmart Marketplace'"; // String | The Service name
let WM_QOS_CORRELATION_ID = "'123456abcdef'"; // String | A Transaction ID
apiInstance.getNextCursorReleasedOrders(nextCursor, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, (error, data, response) => {
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
 **nextCursor** | **String**| Used for pagination when there are more than 200 orders to retrieve. The nextCursor value of the returned response includes a link to another GET call to retrieve the next page. Copy the link and paste it in the next call. | 
 **contentType** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **accept** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to &#39;SWAGGER_CHANNEL_TYPE&#39;]
 **WM_CONSUMER_ID** | **String**| Your Consumer ID | 
 **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to &#39;Auto populated&#39;]
 **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to &#39;Auto populated&#39;]
 **WM_SVC_NAME** | **String**| The Service name | [default to &#39;Walmart Marketplace&#39;]
 **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to &#39;123456abcdef&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrderByPurchaseOrderId

> getOrderByPurchaseOrderId(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, opts)

Get an order

You can display details of a specific order based on the purchaseOrderId.

### Example

```javascript
import OrdersApi from 'orders_api';

let apiInstance = new OrdersApi.Version3Api();
let purchaseOrderId = "purchaseOrderId_example"; // String | Purchase Order ID
let contentType = "'application/xml'"; // String | application/xml, application/json
let accept = "'application/xml'"; // String | application/xml, application/json
let WM_CONSUMER_CHANNEL_TYPE = "'SWAGGER_CHANNEL_TYPE'"; // String | Channel Type
let WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
let WM_SEC_TIMESTAMP = "'Auto populated'"; // String | Epoch timestamp
let WM_SEC_AUTH_SIGNATURE = "'Auto populated'"; // String | Authentication signature
let WM_SVC_NAME = "'Walmart Marketplace'"; // String | The Service name
let WM_QOS_CORRELATION_ID = "'123456abcdef'"; // String | A Transaction ID
let opts = {
  'shipNode': "shipNode_example" // String | Ship Node
};
apiInstance.getOrderByPurchaseOrderId(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, opts, (error, data, response) => {
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
 **purchaseOrderId** | **String**| Purchase Order ID | 
 **contentType** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **accept** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to &#39;SWAGGER_CHANNEL_TYPE&#39;]
 **WM_CONSUMER_ID** | **String**| Your Consumer ID | 
 **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to &#39;Auto populated&#39;]
 **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to &#39;Auto populated&#39;]
 **WM_SVC_NAME** | **String**| The Service name | [default to &#39;Walmart Marketplace&#39;]
 **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to &#39;123456abcdef&#39;]
 **shipNode** | **String**| Ship Node | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReleasedOrders

> getReleasedOrders(createdStartDate, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, opts)

Get all released orders

You can display all released orders that have been created and are ready for fulfilment.

### Example

```javascript
import OrdersApi from 'orders_api';

let apiInstance = new OrdersApi.Version3Api();
let createdStartDate = "createdStartDate_example"; // String | Limit orders to those created after this date or a timestamp.
let contentType = "'application/xml'"; // String | application/xml, application/json
let accept = "'application/xml'"; // String | application/xml, application/json
let WM_CONSUMER_CHANNEL_TYPE = "'SWAGGER_CHANNEL_TYPE'"; // String | Channel Type
let WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
let WM_SEC_TIMESTAMP = "'Auto populated'"; // String | Epoch timestamp
let WM_SEC_AUTH_SIGNATURE = "'Auto populated'"; // String | Authentication signature
let WM_SVC_NAME = "'Walmart Marketplace'"; // String | The Service name
let WM_QOS_CORRELATION_ID = "'123456abcdef'"; // String | A Transaction ID
let opts = {
  'shipNode': "shipNode_example", // String | Ship Node
  'limit': 56 // Number | The number of orders to be returned. Do not set this parameter to over 200 orders.
};
apiInstance.getReleasedOrders(createdStartDate, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, opts, (error, data, response) => {
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
 **createdStartDate** | **String**| Limit orders to those created after this date or a timestamp. | 
 **contentType** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **accept** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to &#39;SWAGGER_CHANNEL_TYPE&#39;]
 **WM_CONSUMER_ID** | **String**| Your Consumer ID | 
 **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to &#39;Auto populated&#39;]
 **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to &#39;Auto populated&#39;]
 **WM_SVC_NAME** | **String**| The Service name | [default to &#39;Walmart Marketplace&#39;]
 **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to &#39;123456abcdef&#39;]
 **shipNode** | **String**| Ship Node | [optional] 
 **limit** | **Number**| The number of orders to be returned. Do not set this parameter to over 200 orders. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## refundOrder

> refundOrder(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, requestBody, opts)

Refund order lines

You can refund one or more order lines that have been shipped. The response to a successful call contains the order with the refunded line item.

### Example

```javascript
import OrdersApi from 'orders_api';

let apiInstance = new OrdersApi.Version3Api();
let purchaseOrderId = "purchaseOrderId_example"; // String | Purchase Order ID
let contentType = "'application/xml'"; // String | application/xml, application/json
let accept = "'application/xml'"; // String | application/xml, application/json
let WM_CONSUMER_CHANNEL_TYPE = "'SWAGGER_CHANNEL_TYPE'"; // String | Channel Type
let WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
let WM_SEC_TIMESTAMP = "'Auto populated'"; // String | Epoch timestamp
let WM_SEC_AUTH_SIGNATURE = "'Auto populated'"; // String | Authentication signature
let WM_SVC_NAME = "'Walmart Marketplace'"; // String | The Service name
let WM_QOS_CORRELATION_ID = "'123456abcdef'"; // String | A Transaction ID
let requestBody = "requestBody_example"; // String | Request body
let opts = {
  'shipNode': "shipNode_example" // String | Ship Node
};
apiInstance.refundOrder(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, requestBody, opts, (error, data, response) => {
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
 **purchaseOrderId** | **String**| Purchase Order ID | 
 **contentType** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **accept** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to &#39;SWAGGER_CHANNEL_TYPE&#39;]
 **WM_CONSUMER_ID** | **String**| Your Consumer ID | 
 **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to &#39;Auto populated&#39;]
 **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to &#39;Auto populated&#39;]
 **WM_SVC_NAME** | **String**| The Service name | [default to &#39;Walmart Marketplace&#39;]
 **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to &#39;123456abcdef&#39;]
 **requestBody** | **String**| Request body | 
 **shipNode** | **String**| Ship Node | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/xml, application/json
- **Accept**: Not defined


## shippingOrder

> shippingOrder(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, requestBody, opts)

Shipping updates

You can change the status of order lines to \&quot;Shipped\&quot; and trigger the charge to a customer. You must acknowledge your orders before sending a shipping update to avoid underselling. An order line, once marked as shipped, cannot be updated.

### Example

```javascript
import OrdersApi from 'orders_api';

let apiInstance = new OrdersApi.Version3Api();
let purchaseOrderId = "purchaseOrderId_example"; // String | Purchase Order ID
let contentType = "'application/xml'"; // String | application/xml, application/json
let accept = "'application/xml'"; // String | application/xml, application/json
let WM_CONSUMER_CHANNEL_TYPE = "'SWAGGER_CHANNEL_TYPE'"; // String | Channel Type
let WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
let WM_SEC_TIMESTAMP = "'Auto populated'"; // String | Epoch timestamp
let WM_SEC_AUTH_SIGNATURE = "'Auto populated'"; // String | Authentication signature
let WM_SVC_NAME = "'Walmart Marketplace'"; // String | The Service name
let WM_QOS_CORRELATION_ID = "'123456abcdef'"; // String | A Transaction ID
let requestBody = "requestBody_example"; // String | Request body
let opts = {
  'shipNode': "shipNode_example" // String | Ship Node
};
apiInstance.shippingOrder(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, requestBody, opts, (error, data, response) => {
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
 **purchaseOrderId** | **String**| Purchase Order ID | 
 **contentType** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **accept** | **String**| application/xml, application/json | [default to &#39;application/xml&#39;]
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to &#39;SWAGGER_CHANNEL_TYPE&#39;]
 **WM_CONSUMER_ID** | **String**| Your Consumer ID | 
 **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to &#39;Auto populated&#39;]
 **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to &#39;Auto populated&#39;]
 **WM_SVC_NAME** | **String**| The Service name | [default to &#39;Walmart Marketplace&#39;]
 **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to &#39;123456abcdef&#39;]
 **requestBody** | **String**| Request body | 
 **shipNode** | **String**| Ship Node | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/xml, application/json
- **Accept**: Not defined

