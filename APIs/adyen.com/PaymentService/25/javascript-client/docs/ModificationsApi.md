# AdyenPaymentApi.ModificationsApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/Payment/v25*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postCancel**](ModificationsApi.md#postCancel) | **POST** /cancel | Cancel an authorisation
[**postCancelOrRefund**](ModificationsApi.md#postCancelOrRefund) | **POST** /cancelOrRefund | Cancel or refund a payment
[**postCapture**](ModificationsApi.md#postCapture) | **POST** /capture | Capture an authorisation
[**postRefund**](ModificationsApi.md#postRefund) | **POST** /refund | Refund a captured payment
[**postVoidPendingRefund**](ModificationsApi.md#postVoidPendingRefund) | **POST** /voidPendingRefund | Cancel an in-person refund



## postCancel

> ModificationResult postCancel(opts)

Cancel an authorisation

Cancels the authorisation hold on a payment, returning a unique reference for this request. You can cancel payments after authorisation only for payment methods that support distinct authorisations and captures.  For more information, refer to [Cancel](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel).  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/{paymentPspReference}/cancels&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments/{paymentPspReference}/cancels) endpoint under Checkout API instead.

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

let apiInstance = new AdyenPaymentApi.ModificationsApi();
let opts = {
  'cancelRequest': new AdyenPaymentApi.CancelRequest() // CancelRequest | 
};
apiInstance.postCancel(opts, (error, data, response) => {
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
 **cancelRequest** | [**CancelRequest**](CancelRequest.md)|  | [optional] 

### Return type

[**ModificationResult**](ModificationResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCancelOrRefund

> ModificationResult postCancelOrRefund(opts)

Cancel or refund a payment

Cancels a payment if it has not been captured yet, or refunds it if it has already been captured. This is useful when it is not certain if the payment has been captured or not (for example, when using auto-capture).  Do not use this endpoint for payments that involve:  * [Multiple partial captures](https://docs.adyen.com/online-payments/capture).  * [Split data](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information) either at time of payment or capture for Adyen for Platforms.   Instead, check if the payment has been captured and make a corresponding [&#x60;/refund&#x60;](https://docs.adyen.com/api-explorer/#/Payment/refund) or [&#x60;/cancel&#x60;](https://docs.adyen.com/api-explorer/#/Payment/cancel) call.  For more information, refer to [Cancel or refund](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel-or-refund).  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/{paymentPspReference}/reversals&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments/{paymentPspReference}/reversals) endpoint under Checkout API instead.

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

let apiInstance = new AdyenPaymentApi.ModificationsApi();
let opts = {
  'cancelOrRefundRequest': new AdyenPaymentApi.CancelOrRefundRequest() // CancelOrRefundRequest | 
};
apiInstance.postCancelOrRefund(opts, (error, data, response) => {
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
 **cancelOrRefundRequest** | [**CancelOrRefundRequest**](CancelOrRefundRequest.md)|  | [optional] 

### Return type

[**ModificationResult**](ModificationResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCapture

> ModificationResult postCapture(opts)

Capture an authorisation

Captures the authorisation hold on a payment, returning a unique reference for this request. Usually the full authorisation amount is captured, however it&#39;s also possible to capture a smaller amount, which results in cancelling the remaining authorisation balance.  Payment methods that are captured automatically after authorisation don&#39;t need to be captured. However, submitting a capture request on these transactions will not result in double charges. If immediate or delayed auto-capture is enabled, calling the capture method is not neccessary.  For more information refer to [Capture](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/capture).  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/{paymentPspReference}/captures&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/v67/post/payments/{paymentPspReference}/captures) endpoint on Checkout API instead.  

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

let apiInstance = new AdyenPaymentApi.ModificationsApi();
let opts = {
  'captureRequest': new AdyenPaymentApi.CaptureRequest() // CaptureRequest | 
};
apiInstance.postCapture(opts, (error, data, response) => {
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
 **captureRequest** | [**CaptureRequest**](CaptureRequest.md)|  | [optional] 

### Return type

[**ModificationResult**](ModificationResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postRefund

> ModificationResult postRefund(opts)

Refund a captured payment

Refunds a payment that has previously been captured, returning a unique reference for this request. Refunding can be done on the full captured amount or a partial amount. Multiple (partial) refunds will be accepted as long as their sum doesn&#39;t exceed the captured amount. Payments which have been authorised, but not captured, cannot be refunded, use the /cancel method instead.  Some payment methods/gateways do not support partial/multiple refunds. A margin above the captured limit can be configured to cover shipping/handling costs.  For more information, refer to [Refund](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/refund).  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/{paymentPspReference}/refunds&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments/{paymentPspReference}/refunds) endpoint under Checkout API instead.

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

let apiInstance = new AdyenPaymentApi.ModificationsApi();
let opts = {
  'refundRequest': new AdyenPaymentApi.RefundRequest() // RefundRequest | 
};
apiInstance.postRefund(opts, (error, data, response) => {
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
 **refundRequest** | [**RefundRequest**](RefundRequest.md)|  | [optional] 

### Return type

[**ModificationResult**](ModificationResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postVoidPendingRefund

> ModificationResult postVoidPendingRefund(opts)

Cancel an in-person refund

This endpoint allows you to cancel an unreferenced refund request before it has been completed.  In your call, you can refer to the original refund request either by using the &#x60;tenderReference&#x60;, or the &#x60;pspReference&#x60;. We recommend implementing based on the &#x60;tenderReference&#x60;, as this is generated for both offline and online transactions.  For more information, refer to [Cancel an unreferenced refund](https://docs.adyen.com/point-of-sale/refund-payment/cancel-unreferenced).

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

let apiInstance = new AdyenPaymentApi.ModificationsApi();
let opts = {
  'voidPendingRefundRequest': new AdyenPaymentApi.VoidPendingRefundRequest() // VoidPendingRefundRequest | 
};
apiInstance.postVoidPendingRefund(opts, (error, data, response) => {
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
 **voidPendingRefundRequest** | [**VoidPendingRefundRequest**](VoidPendingRefundRequest.md)|  | [optional] 

### Return type

[**ModificationResult**](ModificationResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

