# SquareConnectApi.OrdersApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchRetrieveOrders**](OrdersApi.md#batchRetrieveOrders) | **POST** /v2/orders/batch-retrieve | BatchRetrieveOrders
[**calculateOrder**](OrdersApi.md#calculateOrder) | **POST** /v2/orders/calculate | CalculateOrder
[**createOrder**](OrdersApi.md#createOrder) | **POST** /v2/orders | CreateOrder
[**payOrder**](OrdersApi.md#payOrder) | **POST** /v2/orders/{order_id}/pay | PayOrder
[**searchOrders**](OrdersApi.md#searchOrders) | **POST** /v2/orders/search | SearchOrders
[**v2OrdersOrderIdGet**](OrdersApi.md#v2OrdersOrderIdGet) | **GET** /v2/orders/{order_id} | RetrieveOrder
[**v2OrdersOrderIdPut**](OrdersApi.md#v2OrdersOrderIdPut) | **PUT** /v2/orders/{order_id} | UpdateOrder



## batchRetrieveOrders

> BatchRetrieveOrdersResponse batchRetrieveOrders(batchRetrieveOrdersRequest)

BatchRetrieveOrders

Retrieves a set of [orders](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by their IDs.  If a given order ID does not exist, the ID is ignored instead of generating an error.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.OrdersApi();
let batchRetrieveOrdersRequest = new SquareConnectApi.BatchRetrieveOrdersRequest(); // BatchRetrieveOrdersRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.batchRetrieveOrders(batchRetrieveOrdersRequest, (error, data, response) => {
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
 **batchRetrieveOrdersRequest** | [**BatchRetrieveOrdersRequest**](BatchRetrieveOrdersRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**BatchRetrieveOrdersResponse**](BatchRetrieveOrdersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## calculateOrder

> CalculateOrderResponse calculateOrder(calculateOrderRequest)

CalculateOrder

Enables applications to preview order pricing without creating an order.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.OrdersApi();
let calculateOrderRequest = new SquareConnectApi.CalculateOrderRequest(); // CalculateOrderRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.calculateOrder(calculateOrderRequest, (error, data, response) => {
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
 **calculateOrderRequest** | [**CalculateOrderRequest**](CalculateOrderRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CalculateOrderResponse**](CalculateOrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrder

> CreateOrderResponse createOrder(createOrderRequest)

CreateOrder

Creates a new [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) that can include information about products for purchase and settings to apply to the purchase.  To pay for a created order, see  [Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).  You can modify open orders using the [UpdateOrder](https://developer.squareup.com/reference/square_2021-08-18/orders-api/update-order) endpoint.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.OrdersApi();
let createOrderRequest = new SquareConnectApi.CreateOrderRequest(); // CreateOrderRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createOrder(createOrderRequest, (error, data, response) => {
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
 **createOrderRequest** | [**CreateOrderRequest**](CreateOrderRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateOrderResponse**](CreateOrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## payOrder

> PayOrderResponse payOrder(orderId, payOrderRequest)

PayOrder

Pay for an [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) using one or more approved [payments](https://developer.squareup.com/reference/square_2021-08-18/objects/Payment) or settle an order with a total of &#x60;0&#x60;.  The total of the &#x60;payment_ids&#x60; listed in the request must be equal to the order total. Orders with a total amount of &#x60;0&#x60; can be marked as paid by specifying an empty array of &#x60;payment_ids&#x60; in the request.  To be used with &#x60;PayOrder&#x60;, a payment must:  - Reference the order by specifying the &#x60;order_id&#x60; when [creating the payment](https://developer.squareup.com/reference/square_2021-08-18/payments-api/create-payment). Any approved payments that reference the same &#x60;order_id&#x60; not specified in the &#x60;payment_ids&#x60; is canceled. - Be approved with [delayed capture](https://developer.squareup.com/docs/payments-api/take-payments#delayed-capture). Using a delayed capture payment with &#x60;PayOrder&#x60; completes the approved payment.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.OrdersApi();
let orderId = "orderId_example"; // String | The ID of the order being paid.
let payOrderRequest = new SquareConnectApi.PayOrderRequest(); // PayOrderRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.payOrder(orderId, payOrderRequest, (error, data, response) => {
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
 **orderId** | **String**| The ID of the order being paid. | 
 **payOrderRequest** | [**PayOrderRequest**](PayOrderRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**PayOrderResponse**](PayOrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchOrders

> SearchOrdersResponse searchOrders(searchOrdersRequest)

SearchOrders

Search all orders for one or more locations. Orders include all sales, returns, and exchanges regardless of how or when they entered the Square ecosystem (such as Point of Sale, Invoices, and Connect APIs).  &#x60;SearchOrders&#x60; requests need to specify which locations to search and define a [SearchOrdersQuery](https://developer.squareup.com/reference/square_2021-08-18/objects/SearchOrdersQuery) object that controls how to sort or filter the results. Your &#x60;SearchOrdersQuery&#x60; can:    Set filter criteria.   Set the sort order.   Determine whether to return results as complete &#x60;Order&#x60; objects or as [OrderEntry](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderEntry) objects.  Note that details for orders processed with Square Point of Sale while in offline mode might not be transmitted to Square for up to 72 hours. Offline orders have a &#x60;created_at&#x60; value that reflects the time the order was created, not the time it was subsequently transmitted to Square.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.OrdersApi();
let searchOrdersRequest = new SquareConnectApi.SearchOrdersRequest(); // SearchOrdersRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchOrders(searchOrdersRequest, (error, data, response) => {
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
 **searchOrdersRequest** | [**SearchOrdersRequest**](SearchOrdersRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchOrdersResponse**](SearchOrdersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v2OrdersOrderIdGet

> RetrieveOrderResponse v2OrdersOrderIdGet(orderId)

RetrieveOrder

Retrieves an [Order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by ID.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.OrdersApi();
let orderId = "orderId_example"; // String | The ID of the order to retrieve.
apiInstance.v2OrdersOrderIdGet(orderId, (error, data, response) => {
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
 **orderId** | **String**| The ID of the order to retrieve. | 

### Return type

[**RetrieveOrderResponse**](RetrieveOrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v2OrdersOrderIdPut

> UpdateOrderResponse v2OrdersOrderIdPut(orderId, updateOrderRequest)

UpdateOrder

Updates an open [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by adding, replacing, or deleting fields. Orders with a &#x60;COMPLETED&#x60; or &#x60;CANCELED&#x60; state cannot be updated.  An &#x60;UpdateOrder&#x60; request requires the following:  - The &#x60;order_id&#x60; in the endpoint path, identifying the order to update. - The latest &#x60;version&#x60; of the order to update. - The [sparse order](https://developer.squareup.com/docs/orders-api/manage-orders#sparse-order-objects) containing only the fields to update and the version to which the update is being applied. - If deleting fields, the [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-dot-notation) identifying the fields to clear.  To pay for an order, see  [Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.OrdersApi();
let orderId = "orderId_example"; // String | The ID of the order to update.
let updateOrderRequest = new SquareConnectApi.UpdateOrderRequest(); // UpdateOrderRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.v2OrdersOrderIdPut(orderId, updateOrderRequest, (error, data, response) => {
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
 **orderId** | **String**| The ID of the order to update. | 
 **updateOrderRequest** | [**UpdateOrderRequest**](UpdateOrderRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpdateOrderResponse**](UpdateOrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

