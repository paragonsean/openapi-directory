# FulfillmentComApiv2.OrdersApi

All URIs are relative to *https://api.fulfillment.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteOrdersId**](OrdersApi.md#deleteOrdersId) | **DELETE** /orders/{id} | Cancel an Order
[**getOrder**](OrdersApi.md#getOrder) | **GET** /orders/{id} | Order Details
[**getOrders**](OrdersApi.md#getOrders) | **GET** /orders | List of Orders
[**postOrders**](OrdersApi.md#postOrders) | **POST** /orders | New Order



## deleteOrdersId

> Object deleteOrdersId(id)

Cancel an Order

Request an order is canceled to prevent shipment.

### Example

```javascript
import FulfillmentComApiv2 from 'fulfillment_com_apiv2';
let defaultClient = FulfillmentComApiv2.ApiClient.instance;
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FulfillmentComApiv2.OrdersApi();
let id = 56; // Number | ID of order that needs to be canceled
apiInstance.deleteOrdersId(id, (error, data, response) => {
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
 **id** | **Number**| ID of order that needs to be canceled | 

### Return type

**Object**

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrder

> Object getOrder(id, opts)

Order Details

For the fastest results use the FDC provided &#x60;id&#x60; however you can use your &#x60;merchantOrderId&#x60; as the &#x60;id&#x60;.

### Example

```javascript
import FulfillmentComApiv2 from 'fulfillment_com_apiv2';
let defaultClient = FulfillmentComApiv2.ApiClient.instance;
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FulfillmentComApiv2.OrdersApi();
let id = "id_example"; // String | The FDC order Id
let opts = {
  'merchantId': 56, // Number | Providing your `merchantId` indicates the `id` is your `merchantOrderId`. Although it is not necessary to provide this it will speed up your results when using your `merchantOrderId` however it will slow your results when using the FDC provided `id`
  'hydrate': ["null"] // [String] | Adds additional information to the response, uses a CSV format for multiple values.'
};
apiInstance.getOrder(id, opts, (error, data, response) => {
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
 **id** | **String**| The FDC order Id | 
 **merchantId** | **Number**| Providing your &#x60;merchantId&#x60; indicates the &#x60;id&#x60; is your &#x60;merchantOrderId&#x60;. Although it is not necessary to provide this it will speed up your results when using your &#x60;merchantOrderId&#x60; however it will slow your results when using the FDC provided &#x60;id&#x60; | [optional] 
 **hydrate** | [**[String]**](String.md)| Adds additional information to the response, uses a CSV format for multiple values.&#39; | [optional] 

### Return type

**Object**

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrders

> OrderResponseOneOfV2 getOrders(fromDate, toDate, opts)

List of Orders

Retrieve many orders at once

### Example

```javascript
import FulfillmentComApiv2 from 'fulfillment_com_apiv2';
let defaultClient = FulfillmentComApiv2.ApiClient.instance;
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FulfillmentComApiv2.OrdersApi();
let fromDate = "fromDate_example"; // String | Date-time in ISO 8601 format for selecting orders after, or at, the specified time
let toDate = "toDate_example"; // String | Date-time in ISO 8601 format for selecting orders before, or at, the specified time
let opts = {
  'merchantIds': [null], // [Number] | A CSV of merchant id, '123' or '1,2,3'
  'warehouseIds': [null], // [Number] | A CSV of warehouse id, '123' or '1,2,3'
  'page': 1, // Number | A multiplier of the number of items (limit parameter) to skip before returning results
  'limit': 80, // Number | The numbers of items to return
  'hydrate': ["null"] // [String] | Adds additional information to the response, uses a CSV format for multiple values.'
};
apiInstance.getOrders(fromDate, toDate, opts, (error, data, response) => {
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
 **fromDate** | **String**| Date-time in ISO 8601 format for selecting orders after, or at, the specified time | 
 **toDate** | **String**| Date-time in ISO 8601 format for selecting orders before, or at, the specified time | 
 **merchantIds** | [**[Number]**](Number.md)| A CSV of merchant id, &#39;123&#39; or &#39;1,2,3&#39; | [optional] 
 **warehouseIds** | [**[Number]**](Number.md)| A CSV of warehouse id, &#39;123&#39; or &#39;1,2,3&#39; | [optional] 
 **page** | **Number**| A multiplier of the number of items (limit parameter) to skip before returning results | [optional] [default to 1]
 **limit** | **Number**| The numbers of items to return | [optional] [default to 80]
 **hydrate** | [**[String]**](String.md)| Adds additional information to the response, uses a CSV format for multiple values.&#39; | [optional] 

### Return type

[**OrderResponseOneOfV2**](OrderResponseOneOfV2.md)

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postOrders

> OrderResponseV2 postOrders(body)

New Order

Error Notes&amp;#58; * When &#x60;409 Conflict&#x60; is a &#39;Duplicate Order&#39; the &#x60;context&#x60; will include the FDC &#x60;id&#x60;, see samples. 

### Example

```javascript
import FulfillmentComApiv2 from 'fulfillment_com_apiv2';
let defaultClient = FulfillmentComApiv2.ApiClient.instance;
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FulfillmentComApiv2.OrdersApi();
let body = new FulfillmentComApiv2.OrderRequestV2(); // OrderRequestV2 | The order to create
apiInstance.postOrders(body, (error, data, response) => {
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
 **body** | [**OrderRequestV2**](OrderRequestV2.md)| The order to create | 

### Return type

[**OrderResponseV2**](OrderResponseV2.md)

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

