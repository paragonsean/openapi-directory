# KlarnaPaymentsApiV1.OrdersApi

All URIs are relative to *https://api.klarna.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelAuthorization**](OrdersApi.md#cancelAuthorization) | **DELETE** /payments/v1/authorizations/{authorizationToken} | Cancel an existing authorization
[**createOrder**](OrdersApi.md#createOrder) | **POST** /payments/v1/authorizations/{authorizationToken}/order | Create a new order
[**purchaseToken**](OrdersApi.md#purchaseToken) | **POST** /payments/v1/authorizations/{authorizationToken}/customer-token | Generate a consumer token



## cancelAuthorization

> cancelAuthorization(authorizationToken)

Cancel an existing authorization

Use this API call to cancel/release an authorization. If the &#x60;authorization_token&#x60; received during a Klarna Payments won’t be used to place an order immediately you could release the authorization. Read more on **[Cancel an existing authorization](https://docs.klarna.com/klarna-payments/other-actions/cancel-an-authorization/)**.

### Example

```javascript
import KlarnaPaymentsApiV1 from 'klarna_payments_api_v1';

let apiInstance = new KlarnaPaymentsApiV1.OrdersApi();
let authorizationToken = "authorizationToken_example"; // String | 
apiInstance.cancelAuthorization(authorizationToken, (error, data, response) => {
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
 **authorizationToken** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createOrder

> Order createOrder(authorizationToken, opts)

Create a new order

Use this API call to create a new order. Placing an order towards Klarna means that the Klarna Payments session will be closed and that an order will be created in Klarna&#39;s system.&lt;br/&gt;When you have received the &#x60;authorization_token&#x60; for a successful authorization you can place the order. Among the other order details in this request, you include a URL to the confirmation page for the customer.&lt;br/&gt;When the Order has been successfully placed at Klarna, you need to handle it either through the Merchant Portal or using [Klarna’s Order Management API](#order-management-api). Read more on **[Create a new order](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-3-create-an-order/)**.

### Example

```javascript
import KlarnaPaymentsApiV1 from 'klarna_payments_api_v1';

let apiInstance = new KlarnaPaymentsApiV1.OrdersApi();
let authorizationToken = "authorizationToken_example"; // String | 
let opts = {
  'createOrderRequest': new KlarnaPaymentsApiV1.CreateOrderRequest() // CreateOrderRequest | 
};
apiInstance.createOrder(authorizationToken, opts, (error, data, response) => {
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
 **authorizationToken** | **String**|  | 
 **createOrderRequest** | [**CreateOrderRequest**](CreateOrderRequest.md)|  | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## purchaseToken

> CustomerTokenCreationResponse purchaseToken(authorizationToken, opts)

Generate a consumer token

Use this API call to create a Klarna Customer Token.&lt;br/&gt;After having obtained an &#x60;authorization_token&#x60; for a successful authorization, this can be used to create a purchase token instead of placing the order. Creating a Klarna Customer Token results in Klarna storing customer and payment method details. Read more on **[Generate a consumer token](https://docs.klarna.com/klarna-payments/in-depth-knowledge/customer-token/)**.

### Example

```javascript
import KlarnaPaymentsApiV1 from 'klarna_payments_api_v1';

let apiInstance = new KlarnaPaymentsApiV1.OrdersApi();
let authorizationToken = "authorizationToken_example"; // String | 
let opts = {
  'customerTokenCreationRequest': new KlarnaPaymentsApiV1.CustomerTokenCreationRequest() // CustomerTokenCreationRequest | 
};
apiInstance.purchaseToken(authorizationToken, opts, (error, data, response) => {
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
 **authorizationToken** | **String**|  | 
 **customerTokenCreationRequest** | [**CustomerTokenCreationRequest**](CustomerTokenCreationRequest.md)|  | [optional] 

### Return type

[**CustomerTokenCreationResponse**](CustomerTokenCreationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

