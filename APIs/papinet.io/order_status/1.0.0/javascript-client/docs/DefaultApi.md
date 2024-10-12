# PapiNetApi.DefaultApi

All URIs are relative to *https://papinet.papinet.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ordersGet**](DefaultApi.md#ordersGet) | **GET** /orders | List &#x60;orders&#x60;
[**ordersOrderIdGet**](DefaultApi.md#ordersOrderIdGet) | **GET** /orders/{orderId} | Get an &#x60;order&#x60;



## ordersGet

> ListOfOrders ordersGet(opts)

List &#x60;orders&#x60;

Gets a paginated list of all &#x60;orders&#x60;.

### Example

```javascript
import PapiNetApi from 'papi_net_api';

let apiInstance = new PapiNetApi.DefaultApi();
let opts = {
  'orderStatus': "orderStatus_example", // String | Filter by status
  'offset': "offset_example", // String | The number of items to skip before starting to collect the result set.
  'limit': "limit_example" // String | The maximum number of items to return. If the value exceeds the maximum, then the maximum value will be used.
};
apiInstance.ordersGet(opts, (error, data, response) => {
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
 **orderStatus** | **String**| Filter by status | [optional] 
 **offset** | **String**| The number of items to skip before starting to collect the result set. | [optional] 
 **limit** | **String**| The maximum number of items to return. If the value exceeds the maximum, then the maximum value will be used. | [optional] 

### Return type

[**ListOfOrders**](ListOfOrders.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersOrderIdGet

> Order ordersOrderIdGet(orderId)

Get an &#x60;order&#x60;

Gets the details of a specific &#x60;order&#x60;, including a paginated list of all its lines.

### Example

```javascript
import PapiNetApi from 'papi_net_api';

let apiInstance = new PapiNetApi.DefaultApi();
let orderId = "orderId_example"; // String | UUID of the `order` to get
apiInstance.ordersOrderIdGet(orderId, (error, data, response) => {
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
 **orderId** | **String**| UUID of the &#x60;order&#x60; to get | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

