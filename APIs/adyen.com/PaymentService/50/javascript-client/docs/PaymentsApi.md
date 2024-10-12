# AdyenPaymentApi.PaymentsApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/Payment/v50*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postAuthorise**](PaymentsApi.md#postAuthorise) | **POST** /authorise | Create an authorisation
[**postAuthorise3d**](PaymentsApi.md#postAuthorise3d) | **POST** /authorise3d | Complete a 3DS authorisation
[**postAuthorise3ds2**](PaymentsApi.md#postAuthorise3ds2) | **POST** /authorise3ds2 | Complete a 3DS2 authorisation
[**postRetrieve3ds2Result**](PaymentsApi.md#postRetrieve3ds2Result) | **POST** /retrieve3ds2Result | Get the 3DS2 authentication result



## postAuthorise

> PaymentResult postAuthorise(opts)

Create an authorisation

Creates a payment with a unique reference (&#x60;pspReference&#x60;) and attempts to obtain an authorisation hold. For cards, this amount can be captured or cancelled later. Non-card payment methods typically don&#39;t support this and will automatically capture as part of the authorisation. &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments) endpoint under Checkout API instead.

### Example

```javascript
import AdyenPaymentApi from 'adyen_payment_api';
let defaultClient = AdyenPaymentApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenPaymentApi.PaymentsApi();
let opts = {
  'paymentRequest': new AdyenPaymentApi.PaymentRequest() // PaymentRequest | 
};
apiInstance.postAuthorise(opts, (error, data, response) => {
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
 **paymentRequest** | [**PaymentRequest**](PaymentRequest.md)|  | [optional] 

### Return type

[**PaymentResult**](PaymentResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postAuthorise3d

> PaymentResult postAuthorise3d(opts)

Complete a 3DS authorisation

For an authenticated 3D Secure session, completes the payment authorisation. This endpoint must receive the &#x60;md&#x60; and &#x60;paResponse&#x60; parameters that you get from the card issuer after a shopper pays via 3D Secure.  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce/3d-secure). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/details&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments/details) endpoint under Checkout API instead.

### Example

```javascript
import AdyenPaymentApi from 'adyen_payment_api';
let defaultClient = AdyenPaymentApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenPaymentApi.PaymentsApi();
let opts = {
  'paymentRequest3d': new AdyenPaymentApi.PaymentRequest3d() // PaymentRequest3d | 
};
apiInstance.postAuthorise3d(opts, (error, data, response) => {
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
 **paymentRequest3d** | [**PaymentRequest3d**](PaymentRequest3d.md)|  | [optional] 

### Return type

[**PaymentResult**](PaymentResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postAuthorise3ds2

> PaymentResult postAuthorise3ds2(opts)

Complete a 3DS2 authorisation

For an authenticated 3D Secure 2 session, completes the payment authorisation. This endpoint must receive the &#x60;threeDS2Token&#x60; and &#x60;threeDS2Result&#x60; parameters.  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce/3d-secure). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/details&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments/details) endpoint under Checkout API instead.

### Example

```javascript
import AdyenPaymentApi from 'adyen_payment_api';
let defaultClient = AdyenPaymentApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenPaymentApi.PaymentsApi();
let opts = {
  'paymentRequest3ds2': new AdyenPaymentApi.PaymentRequest3ds2() // PaymentRequest3ds2 | 
};
apiInstance.postAuthorise3ds2(opts, (error, data, response) => {
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
 **paymentRequest3ds2** | [**PaymentRequest3ds2**](PaymentRequest3ds2.md)|  | [optional] 

### Return type

[**PaymentResult**](PaymentResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postRetrieve3ds2Result

> ThreeDS2ResultResponse postRetrieve3ds2Result(opts)

Get the 3DS2 authentication result

Retrieves the &#x60;threeDS2Result&#x60; after doing a 3D Secure 2 authentication only.

### Example

```javascript
import AdyenPaymentApi from 'adyen_payment_api';
let defaultClient = AdyenPaymentApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenPaymentApi.PaymentsApi();
let opts = {
  'threeDS2ResultRequest': new AdyenPaymentApi.ThreeDS2ResultRequest() // ThreeDS2ResultRequest | 
};
apiInstance.postRetrieve3ds2Result(opts, (error, data, response) => {
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
 **threeDS2ResultRequest** | [**ThreeDS2ResultRequest**](ThreeDS2ResultRequest.md)|  | [optional] 

### Return type

[**ThreeDS2ResultResponse**](ThreeDS2ResultResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

