# Ecwid.OrdersApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrder**](OrdersApi.md#createOrder) | **POST** /orders | Create an order in the eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Order&#39; model are those required to create a new order.The paymentStatus can only be AWAITING_PAYMENT or INCOMPLETE.The fulfillmentStatus can only be AWAITING_PROCESSING
[**deleteOrderById**](OrdersApi.md#deleteOrderById) | **DELETE** /orders/{id} | Delete an order associated with a given ID from your eCommerce system. Specifying an order associated with a given ID that does not exist will result in an error message
[**getOrderById**](OrdersApi.md#getOrderById) | **GET** /orders/{id} | Retrieve an order associated with a given ID from the eCommerce system. Specifying an order with an ID that does not exist will result in an error response
[**getOrders**](OrdersApi.md#getOrders) | **GET** /orders | Find orders in the eCommerce system, using the provided CEQL search expression. If no search expression is provided, all records will be retrieved
[**getOrdersPayments**](OrdersApi.md#getOrdersPayments) | **GET** /orders/{orderId}/payments | Retrieve the payments in the eCommerce system for the specified order
[**getOrdersRefunds**](OrdersApi.md#getOrdersRefunds) | **GET** /orders/{orderId}/refunds | Retrieve the refunds in the eCommerce system for the specified order
[**updateOrderById**](OrdersApi.md#updateOrderById) | **PATCH** /orders/{id} | Update an order associated with a given ID in the eCommerce system. The update API uses the PATCH HTTP verb, so only those fields provided in the order object will be updated, and those fields not provided will be left alone. Updating an order with a specified ID that does not exist will result in an error response&lt;/strong&gt;



## createOrder

> Order createOrder(authorization, order)

Create an order in the eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Order&#39; model are those required to create a new order.The paymentStatus can only be AWAITING_PAYMENT or INCOMPLETE.The fulfillmentStatus can only be AWAITING_PROCESSING

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.OrdersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let order = new Ecwid.OrderPost(); // OrderPost | The order object to be created
apiInstance.createOrder(authorization, order, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **order** | [**OrderPost**](OrderPost.md)| The order object to be created | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## deleteOrderById

> deleteOrderById(authorization, id)

Delete an order associated with a given ID from your eCommerce system. Specifying an order associated with a given ID that does not exist will result in an error message

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.OrdersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the order to delete from the eCommerce system
apiInstance.deleteOrderById(authorization, id, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the order to delete from the eCommerce system | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrderById

> Order getOrderById(authorization, id)

Retrieve an order associated with a given ID from the eCommerce system. Specifying an order with an ID that does not exist will result in an error response

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.OrdersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the order to retrieve from the eCommerce system
apiInstance.getOrderById(authorization, id, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the order to retrieve from the eCommerce system | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getOrders

> [Order] getOrders(authorization, opts)

Find orders in the eCommerce system, using the provided CEQL search expression. If no search expression is provided, all records will be retrieved

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.OrdersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let opts = {
  'where': "where_example", // String | The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field='value'). <p>Supported search terms: date, from_date, to_date, from_update_date, to_update_date, order, from_order, to_order, customer_id, customer_email and statuses. All other search criteria are ignored
  'pageSize': 789, // Number | The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
  'nextPage': "nextPage_example", // String | The next page cursor, taken from the response header: `elements-next-page-token`
  'fields': "fields_example" // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
};
apiInstance.getOrders(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **where** | **String**| The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field&#x3D;&#39;value&#39;). &lt;p&gt;Supported search terms: date, from_date, to_date, from_update_date, to_update_date, order, from_order, to_order, customer_id, customer_email and statuses. All other search criteria are ignored | [optional] 
 **pageSize** | **Number**| The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned | [optional] 
 **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] 
 **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] 

### Return type

[**[Order]**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getOrdersPayments

> [Payment] getOrdersPayments(authorization, orderId, opts)

Retrieve the payments in the eCommerce system for the specified order

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.OrdersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let orderId = "orderId_example"; // String | The ID of the order to retrieve payments from in the eCommerce system
let opts = {
  'pageSize': 789, // Number | The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
  'nextPage': "nextPage_example", // String | The next page cursor, taken from the response header: `elements-next-page-token`
  'fields': "fields_example" // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
};
apiInstance.getOrdersPayments(authorization, orderId, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **orderId** | **String**| The ID of the order to retrieve payments from in the eCommerce system | 
 **pageSize** | **Number**| The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned | [optional] 
 **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] 
 **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] 

### Return type

[**[Payment]**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getOrdersRefunds

> [Payment] getOrdersRefunds(authorization, orderId, opts)

Retrieve the refunds in the eCommerce system for the specified order

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.OrdersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let orderId = "orderId_example"; // String | The ID of the order to retrieve refunds from in the eCommerce system
let opts = {
  'pageSize': 789, // Number | The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
  'nextPage': "nextPage_example", // String | The next page cursor, taken from the response header: `elements-next-page-token`
  'fields': "fields_example" // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
};
apiInstance.getOrdersRefunds(authorization, orderId, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **orderId** | **String**| The ID of the order to retrieve refunds from in the eCommerce system | 
 **pageSize** | **Number**| The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned | [optional] 
 **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] 
 **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] 

### Return type

[**[Payment]**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateOrderById

> Order updateOrderById(authorization, id, order, opts)

Update an order associated with a given ID in the eCommerce system. The update API uses the PATCH HTTP verb, so only those fields provided in the order object will be updated, and those fields not provided will be left alone. Updating an order with a specified ID that does not exist will result in an error response&lt;/strong&gt;

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.OrdersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the order to update in the eCommerce system
let order = new Ecwid.OrderPatch(); // OrderPatch | The order object, with those fields that are to be updated
let opts = {
  'action': "action_example" // String | An action to perform on the order: cancel, reopen or close. If left blank then the order is updated but no action is taken
};
apiInstance.updateOrderById(authorization, id, order, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the order to update in the eCommerce system | 
 **order** | [**OrderPatch**](OrderPatch.md)| The order object, with those fields that are to be updated | 
 **action** | **String**| An action to perform on the order: cancel, reopen or close. If left blank then the order is updated but no action is taken | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

