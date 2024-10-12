# HandwryttenApi.OrdersApi

All URIs are relative to *https://api.handwrytten.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**singleStepOrder**](OrdersApi.md#singleStepOrder) | **POST** /orders/singleStepOrder | sends an order in a single step.  This is much easier than using other order commands



## singleStepOrder

> SingleStepOrder200Response singleStepOrder(body)

sends an order in a single step.  This is much easier than using other order commands

Sends an order in one step.  No need to create then process order.  Optionally include a gift card.

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.OrdersApi();
let body = new HandwryttenApi.SingleStepOrderRequest(); // SingleStepOrderRequest | additional parameters
apiInstance.singleStepOrder(body, (error, data, response) => {
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
 **body** | [**SingleStepOrderRequest**](SingleStepOrderRequest.md)| additional parameters | 

### Return type

[**SingleStepOrder200Response**](SingleStepOrder200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

