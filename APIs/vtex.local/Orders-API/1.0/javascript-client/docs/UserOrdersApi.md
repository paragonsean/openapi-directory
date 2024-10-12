# OrdersApi.UserOrdersApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userorderdetails**](UserOrdersApi.md#userorderdetails) | **GET** /api/oms/user/orders/{orderId} | Retrieve user order details
[**userorderslist**](UserOrdersApi.md#userorderslist) | **GET** /api/oms/user/orders | Retrieve user&#39;s orders



## userorderdetails

> Userorderdetails userorderdetails(clientEmail, contentType, accept, orderId)

Retrieve user order details

Lists all details from a user&#39;s order, through client&#39;s perspective.     &gt; Note that these requests are meant to be made by **Call center operator** profiles. Otherwise, they will return only orders from the same email making the request.

### Example

```javascript
import OrdersApi from 'orders_api';
let defaultClient = OrdersApi.ApiClient.instance;
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

let apiInstance = new OrdersApi.UserOrdersApi();
let clientEmail = "customer@mail.com"; // String | Customer email.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let orderId = "1172452900788-01"; // String | Order ID is a unique code that identifies an order.
apiInstance.userorderdetails(clientEmail, contentType, accept, orderId, (error, data, response) => {
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
 **clientEmail** | **String**| Customer email. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **orderId** | **String**| Order ID is a unique code that identifies an order. | 

### Return type

[**Userorderdetails**](Userorderdetails.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userorderslist

> Userorderslist userorderslist(clientEmail, page, perPage, contentType, accept)

Retrieve user&#39;s orders

Lists all orders from a given client, filtering by their email.     &gt; Note that these requests are meant to be made by **Call center operator** profiles. Otherwise, they will return only orders from the same email making the request.

### Example

```javascript
import OrdersApi from 'orders_api';
let defaultClient = OrdersApi.ApiClient.instance;
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

let apiInstance = new OrdersApi.UserOrdersApi();
let clientEmail = "customer@mail.com"; // String | Customer email.
let page = "15"; // String | Page number for result pagination.
let perPage = "15"; // String | Page quantity for result pagination.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.userorderslist(clientEmail, page, perPage, contentType, accept, (error, data, response) => {
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
 **clientEmail** | **String**| Customer email. | 
 **page** | **String**| Page number for result pagination. | 
 **perPage** | **String**| Page quantity for result pagination. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

[**Userorderslist**](Userorderslist.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

