# AdyenCheckoutApi.OrdersApi

All URIs are relative to *https://checkout-test.adyen.com/v52*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postOrders**](OrdersApi.md#postOrders) | **POST** /orders | Create an order
[**postOrdersCancel**](OrdersApi.md#postOrdersCancel) | **POST** /orders/cancel | Cancel an order
[**postPaymentMethodsBalance**](OrdersApi.md#postPaymentMethodsBalance) | **POST** /paymentMethods/balance | Get the balance of a gift card



## postOrders

> CreateOrderResponse postOrders(opts)

Create an order

Creates an order to be used for partial payments. Make a POST &#x60;/orders&#x60; call before making a &#x60;/payments&#x60; call when processing payments with different payment methods.

### Example

```javascript
import AdyenCheckoutApi from 'adyen_checkout_api';
let defaultClient = AdyenCheckoutApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenCheckoutApi.OrdersApi();
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'createOrderRequest': new AdyenCheckoutApi.CreateOrderRequest() // CreateOrderRequest | 
};
apiInstance.postOrders(opts, (error, data, response) => {
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
 **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] 
 **createOrderRequest** | [**CreateOrderRequest**](CreateOrderRequest.md)|  | [optional] 

### Return type

[**CreateOrderResponse**](CreateOrderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postOrdersCancel

> CancelOrderResponse postOrdersCancel(opts)

Cancel an order

Cancels an order. Cancellation of an order results in an automatic rollback of all payments made in the order, either by canceling or refunding the payment, depending on the type of payment method.

### Example

```javascript
import AdyenCheckoutApi from 'adyen_checkout_api';
let defaultClient = AdyenCheckoutApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenCheckoutApi.OrdersApi();
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'cancelOrderRequest': new AdyenCheckoutApi.CancelOrderRequest() // CancelOrderRequest | 
};
apiInstance.postOrdersCancel(opts, (error, data, response) => {
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
 **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] 
 **cancelOrderRequest** | [**CancelOrderRequest**](CancelOrderRequest.md)|  | [optional] 

### Return type

[**CancelOrderResponse**](CancelOrderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPaymentMethodsBalance

> BalanceCheckResponse postPaymentMethodsBalance(opts)

Get the balance of a gift card

Retrieves the balance remaining on a shopper&#39;s gift card. To check a gift card&#39;s balance, make a POST &#x60;/paymentMethods/balance&#x60; call and include the gift card&#39;s details inside a &#x60;paymentMethod&#x60; object.

### Example

```javascript
import AdyenCheckoutApi from 'adyen_checkout_api';
let defaultClient = AdyenCheckoutApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenCheckoutApi.OrdersApi();
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'balanceCheckRequest': new AdyenCheckoutApi.BalanceCheckRequest() // BalanceCheckRequest | 
};
apiInstance.postPaymentMethodsBalance(opts, (error, data, response) => {
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
 **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] 
 **balanceCheckRequest** | [**BalanceCheckRequest**](BalanceCheckRequest.md)|  | [optional] 

### Return type

[**BalanceCheckResponse**](BalanceCheckResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

