# VoodooManufacturing3DPrintApi.OrderApi

All URIs are relative to */api/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orderConfirmPost**](OrderApi.md#orderConfirmPost) | **POST** /order/confirm | Confirms an order from a quote_id and submits it to the Voodoo factory. 
[**orderCreatePost**](OrderApi.md#orderCreatePost) | **POST** /order/create | Quotes an order and returns a quote_id that is used to confirm the order. 
[**orderGet**](OrderApi.md#orderGet) | **GET** /order | Lists all orders. 
[**orderOrderIdGet**](OrderApi.md#orderOrderIdGet) | **GET** /order/{order_id} | Retrieve a previously created model by its id. 
[**orderShippingPost**](OrderApi.md#orderShippingPost) | **POST** /order/shipping | List shipping options and prices for a given shipment. 



## orderConfirmPost

> OrderConfirmPost200Response orderConfirmPost(body)

Confirms an order from a quote_id and submits it to the Voodoo factory. 

After generating a quote for an order, you can choose to confirm the order for manufacturing by hitting this endpoint with the quote_id returned by the /order/quote endpoint. Returns the order with a unique order_id in place of the quote_id. 

### Example

```javascript
import VoodooManufacturing3DPrintApi from 'voodoo_manufacturing_3_d_print_api';
let defaultClient = VoodooManufacturing3DPrintApi.ApiClient.instance;
// Configure API key authorization: Voodoo Manufacturing API Key
let Voodoo Manufacturing API Key = defaultClient.authentications['Voodoo Manufacturing API Key'];
Voodoo Manufacturing API Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Voodoo Manufacturing API Key.apiKeyPrefix = 'Token';

let apiInstance = new VoodooManufacturing3DPrintApi.OrderApi();
let body = new VoodooManufacturing3DPrintApi.ConfirmOrderBody(); // ConfirmOrderBody | 
apiInstance.orderConfirmPost(body, (error, data, response) => {
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
 **body** | [**ConfirmOrderBody**](ConfirmOrderBody.md)|  | 

### Return type

[**OrderConfirmPost200Response**](OrderConfirmPost200Response.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderCreatePost

> OrderCreatePost200Response orderCreatePost(body)

Quotes an order and returns a quote_id that is used to confirm the order. 

Creates an order for the requested items, shipping address, and shipping method. This method returns the order along with a quote_id, which needs to be confirmed with /order/confirm prior to the order actually being started. quote_ids are only valid for 15 minutes. 

### Example

```javascript
import VoodooManufacturing3DPrintApi from 'voodoo_manufacturing_3_d_print_api';
let defaultClient = VoodooManufacturing3DPrintApi.ApiClient.instance;
// Configure API key authorization: Voodoo Manufacturing API Key
let Voodoo Manufacturing API Key = defaultClient.authentications['Voodoo Manufacturing API Key'];
Voodoo Manufacturing API Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Voodoo Manufacturing API Key.apiKeyPrefix = 'Token';

let apiInstance = new VoodooManufacturing3DPrintApi.OrderApi();
let body = new VoodooManufacturing3DPrintApi.CreateOrderBody(); // CreateOrderBody | 
apiInstance.orderCreatePost(body, (error, data, response) => {
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
 **body** | [**CreateOrderBody**](CreateOrderBody.md)|  | 

### Return type

[**OrderCreatePost200Response**](OrderCreatePost200Response.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderGet

> [Order] orderGet()

Lists all orders. 

Gets all of orders that you&#39;ve confirmed. 

### Example

```javascript
import VoodooManufacturing3DPrintApi from 'voodoo_manufacturing_3_d_print_api';
let defaultClient = VoodooManufacturing3DPrintApi.ApiClient.instance;
// Configure API key authorization: Voodoo Manufacturing API Key
let Voodoo Manufacturing API Key = defaultClient.authentications['Voodoo Manufacturing API Key'];
Voodoo Manufacturing API Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Voodoo Manufacturing API Key.apiKeyPrefix = 'Token';

let apiInstance = new VoodooManufacturing3DPrintApi.OrderApi();
apiInstance.orderGet((error, data, response) => {
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

[**[Order]**](Order.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderOrderIdGet

> Order orderOrderIdGet(orderId)

Retrieve a previously created model by its id. 

In cases where you&#39;re ordering models you&#39;ve created previously, you can fetch a specific model by its id. 

### Example

```javascript
import VoodooManufacturing3DPrintApi from 'voodoo_manufacturing_3_d_print_api';
let defaultClient = VoodooManufacturing3DPrintApi.ApiClient.instance;
// Configure API key authorization: Voodoo Manufacturing API Key
let Voodoo Manufacturing API Key = defaultClient.authentications['Voodoo Manufacturing API Key'];
Voodoo Manufacturing API Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Voodoo Manufacturing API Key.apiKeyPrefix = 'Token';

let apiInstance = new VoodooManufacturing3DPrintApi.OrderApi();
let orderId = "orderId_example"; // String | 
apiInstance.orderOrderIdGet(orderId, (error, data, response) => {
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
 **orderId** | **String**|  | 

### Return type

[**Order**](Order.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderShippingPost

> OrderShippingPost200Response orderShippingPost(body)

List shipping options and prices for a given shipment. 

Get quotes for shipping your order to the given shipping address. Because shipping quotes depend on the items being shipped, you should use the same array of print descriptions here that you do to create the order.  This endpoint should allow you to select the appropriate shipping method using the \&quot;service\&quot; field of the desired shipping method. 

### Example

```javascript
import VoodooManufacturing3DPrintApi from 'voodoo_manufacturing_3_d_print_api';
let defaultClient = VoodooManufacturing3DPrintApi.ApiClient.instance;
// Configure API key authorization: Voodoo Manufacturing API Key
let Voodoo Manufacturing API Key = defaultClient.authentications['Voodoo Manufacturing API Key'];
Voodoo Manufacturing API Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Voodoo Manufacturing API Key.apiKeyPrefix = 'Token';

let apiInstance = new VoodooManufacturing3DPrintApi.OrderApi();
let body = new VoodooManufacturing3DPrintApi.ShippingOptionsBody(); // ShippingOptionsBody | 
apiInstance.orderShippingPost(body, (error, data, response) => {
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
 **body** | [**ShippingOptionsBody**](ShippingOptionsBody.md)|  | 

### Return type

[**OrderShippingPost200Response**](OrderShippingPost200Response.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

