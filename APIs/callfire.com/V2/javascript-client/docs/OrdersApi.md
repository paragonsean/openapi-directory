# CallFireApiDocumentation.OrdersApi

All URIs are relative to *https://api.callfire.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findOrders**](OrdersApi.md#findOrders) | **GET** /orders | Find orders
[**getOrder**](OrdersApi.md#getOrder) | **GET** /orders/{id} | Find a specific order
[**orderKeywords**](OrdersApi.md#orderKeywords) | **POST** /orders/keywords | Purchase keywords
[**orderNumbers**](OrdersApi.md#orderNumbers) | **POST** /orders/numbers | Purchase numbers



## findOrders

> PageNumberOrder findOrders(opts)

Find orders

Searches for account orders

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.OrdersApi();
let opts = {
  'limit': 20, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'status': ["null"], // [String] | Filter by order status, accepts multiple values in comma separated string, available values: [PROCESSING, FINISHED, PAYMENT_ERROR, VOID, WAIT_FOR_PAYMENT, PARTIALLY_ADJUSTED, ADJUSTED]
  'intervalBegin': 789, // Number | Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000
  'intervalEnd': 789 // Number | End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000
};
apiInstance.findOrders(opts, (error, data, response) => {
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
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 20]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **status** | [**[String]**](String.md)| Filter by order status, accepts multiple values in comma separated string, available values: [PROCESSING, FINISHED, PAYMENT_ERROR, VOID, WAIT_FOR_PAYMENT, PARTIALLY_ADJUSTED, ADJUSTED] | [optional] 
 **intervalBegin** | **Number**| Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 | [optional] 
 **intervalEnd** | **Number**| End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 | [optional] 

### Return type

[**PageNumberOrder**](PageNumberOrder.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrder

> NumberOrder getOrder(id, opts)

Find a specific order

Returns a single NumberOrder instance for a given order id. Order contains information about purchased keywords, local, toll-free numbers

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.OrdersApi();
let id = 789; // Number | An id of an order
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
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
 **id** | **Number**| An id of an order | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**NumberOrder**](NumberOrder.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderKeywords

> ResourceId orderKeywords(opts)

Purchase keywords

Purchase keywords. Send a list of available keywords into this API to purchase them using CallFire credits. Make sure the account has enough credits before trying to purchase the keywords. Keyword should only consist of uppercase and lowercase letters and numbers. Number of characters must be greater than 2, but less than 65.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.OrdersApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'keywordPurchaseRequest': new CallFireApiDocumentation.KeywordPurchaseRequest() // KeywordPurchaseRequest | Request object which contains a list of keywords to buy
};
apiInstance.orderKeywords(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **keywordPurchaseRequest** | [**KeywordPurchaseRequest**](KeywordPurchaseRequest.md)| Request object which contains a list of keywords to buy | [optional] 

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orderNumbers

> ResourceId orderNumbers(opts)

Purchase numbers

Purchase numbers. There are many ways to purchase a number. Set either &#39;tollFreeCount&#39; or &#39;localCount&#39; along with some querying fields to purchase numbers by bulk query. Set the list of numbers to purchase by list. Available numbers will be purchased using CallFire credits owned by the user. Make sure the account has enough credits before trying to purchase

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.OrdersApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'numberPurchaseRequest': new CallFireApiDocumentation.NumberPurchaseRequest() // NumberPurchaseRequest | Request object contains a list of numbers to buy, you can filter the numbers by their region information: city, state, zipcode, etc
};
apiInstance.orderNumbers(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **numberPurchaseRequest** | [**NumberPurchaseRequest**](NumberPurchaseRequest.md)| Request object contains a list of numbers to buy, you can filter the numbers by their region information: city, state, zipcode, etc | [optional] 

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

