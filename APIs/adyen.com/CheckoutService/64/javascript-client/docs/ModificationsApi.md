# AdyenCheckoutApi.ModificationsApi

All URIs are relative to *https://checkout-test.adyen.com/v64*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postCancels**](ModificationsApi.md#postCancels) | **POST** /cancels | Cancel an authorised payment
[**postPaymentsPaymentPspReferenceAmountUpdates**](ModificationsApi.md#postPaymentsPaymentPspReferenceAmountUpdates) | **POST** /payments/{paymentPspReference}/amountUpdates | Update an authorised amount
[**postPaymentsPaymentPspReferenceCancels**](ModificationsApi.md#postPaymentsPaymentPspReferenceCancels) | **POST** /payments/{paymentPspReference}/cancels | Cancel an authorised payment
[**postPaymentsPaymentPspReferenceCaptures**](ModificationsApi.md#postPaymentsPaymentPspReferenceCaptures) | **POST** /payments/{paymentPspReference}/captures | Capture an authorised payment
[**postPaymentsPaymentPspReferenceRefunds**](ModificationsApi.md#postPaymentsPaymentPspReferenceRefunds) | **POST** /payments/{paymentPspReference}/refunds | Refund a captured payment
[**postPaymentsPaymentPspReferenceReversals**](ModificationsApi.md#postPaymentsPaymentPspReferenceReversals) | **POST** /payments/{paymentPspReference}/reversals | Refund or cancel a payment



## postCancels

> StandalonePaymentCancelResponse postCancels(opts)

Cancel an authorised payment

Cancels the authorisation on a payment that has not yet been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures), and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**TECHNICAL_CANCEL** webhook](https://docs.adyen.com/online-payments/cancel#cancellation-webhook).  If you want to cancel a payment using the [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference), use the [&#x60;/payments/{paymentPspReference}/cancels&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels) endpoint instead.  If you want to cancel a payment but are not sure whether it has been captured, use the [&#x60;/payments/{paymentPspReference}/reversals&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals) endpoint instead.  For more information, refer to [Cancel](https://docs.adyen.com/online-payments/cancel).

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

let apiInstance = new AdyenCheckoutApi.ModificationsApi();
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'standalonePaymentCancelRequest': new AdyenCheckoutApi.StandalonePaymentCancelRequest() // StandalonePaymentCancelRequest | 
};
apiInstance.postCancels(opts, (error, data, response) => {
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
 **standalonePaymentCancelRequest** | [**StandalonePaymentCancelRequest**](StandalonePaymentCancelRequest.md)|  | [optional] 

### Return type

[**StandalonePaymentCancelResponse**](StandalonePaymentCancelResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPaymentsPaymentPspReferenceAmountUpdates

> PaymentAmountUpdateResponse postPaymentsPaymentPspReferenceAmountUpdates(paymentPspReference, opts)

Update an authorised amount

Increases or decreases the authorised payment amount and returns a unique reference for this request. You get the outcome of the request asynchronously, in an [**AUTHORISATION_ADJUSTMENT** webhook](https://docs.adyen.com/development-resources/webhooks/understand-notifications#event-codes).  You can only update authorised amounts that have not yet been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures).  The amount you specify in the request is the updated amount, which is larger or smaller than the initial authorised amount.  For more information, refer to [Authorisation adjustment](https://docs.adyen.com/online-payments/adjust-authorisation#use-cases).

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

let apiInstance = new AdyenCheckoutApi.ModificationsApi();
let paymentPspReference = "paymentPspReference_example"; // String | The [`pspReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment.
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'paymentAmountUpdateRequest': new AdyenCheckoutApi.PaymentAmountUpdateRequest() // PaymentAmountUpdateRequest | 
};
apiInstance.postPaymentsPaymentPspReferenceAmountUpdates(paymentPspReference, opts, (error, data, response) => {
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
 **paymentPspReference** | **String**| The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment. | 
 **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] 
 **paymentAmountUpdateRequest** | [**PaymentAmountUpdateRequest**](PaymentAmountUpdateRequest.md)|  | [optional] 

### Return type

[**PaymentAmountUpdateResponse**](PaymentAmountUpdateResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPaymentsPaymentPspReferenceCancels

> PaymentCancelResponse postPaymentsPaymentPspReferenceCancels(paymentPspReference, opts)

Cancel an authorised payment

Cancels the authorisation on a payment that has not yet been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/paymentPspReference/captures), and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**CANCELLATION** webhook](https://docs.adyen.com/online-payments/cancel#cancellation-webhook).  If you want to cancel a payment but don&#39;t have the [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference), use the [&#x60;/cancels&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cancels) endpoint instead.  If you want to cancel a payment but are not sure whether it has been captured, use the [&#x60;/payments/{paymentPspReference}/reversals&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals) endpoint instead.  For more information, refer to [Cancel](https://docs.adyen.com/online-payments/cancel).

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

let apiInstance = new AdyenCheckoutApi.ModificationsApi();
let paymentPspReference = "paymentPspReference_example"; // String | The [`pspReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment that you want to cancel. 
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'paymentCancelRequest': new AdyenCheckoutApi.PaymentCancelRequest() // PaymentCancelRequest | 
};
apiInstance.postPaymentsPaymentPspReferenceCancels(paymentPspReference, opts, (error, data, response) => {
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
 **paymentPspReference** | **String**| The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment that you want to cancel.  | 
 **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] 
 **paymentCancelRequest** | [**PaymentCancelRequest**](PaymentCancelRequest.md)|  | [optional] 

### Return type

[**PaymentCancelResponse**](PaymentCancelResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPaymentsPaymentPspReferenceCaptures

> PaymentCaptureResponse postPaymentsPaymentPspReferenceCaptures(paymentPspReference, opts)

Capture an authorised payment

 Captures an authorised payment and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**CAPTURE** webhook](https://docs.adyen.com/online-payments/capture#capture-notification).  You can capture either the full authorised amount or a part of the authorised amount. By default, any unclaimed amount after a partial capture gets cancelled. This does not apply if you enabled multiple partial captures on your account and the payment method supports multiple partial captures.   [Automatic capture](https://docs.adyen.com/online-payments/capture#automatic-capture) is the default setting for most payment methods. In these cases, you don&#39;t need to make capture requests. However, making capture requests for payments that are captured automatically does not result in double charges.  For more information, refer to [Capture](https://docs.adyen.com/online-payments/capture).

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

let apiInstance = new AdyenCheckoutApi.ModificationsApi();
let paymentPspReference = "paymentPspReference_example"; // String | The [`pspReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment that you want to capture.
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'paymentCaptureRequest': new AdyenCheckoutApi.PaymentCaptureRequest() // PaymentCaptureRequest | 
};
apiInstance.postPaymentsPaymentPspReferenceCaptures(paymentPspReference, opts, (error, data, response) => {
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
 **paymentPspReference** | **String**| The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment that you want to capture. | 
 **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] 
 **paymentCaptureRequest** | [**PaymentCaptureRequest**](PaymentCaptureRequest.md)|  | [optional] 

### Return type

[**PaymentCaptureResponse**](PaymentCaptureResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPaymentsPaymentPspReferenceRefunds

> PaymentRefundResponse postPaymentsPaymentPspReferenceRefunds(paymentPspReference, opts)

Refund a captured payment

Refunds a payment that has been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures), and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**REFUND** webhook](https://docs.adyen.com/online-payments/refund#refund-webhook).  You can refund either the full captured amount or a part of the captured amount. You can also perform multiple partial refunds, as long as their sum doesn&#39;t exceed the captured amount.  &gt; Some payment methods do not support partial refunds. To learn if a payment method supports partial refunds, refer to the payment method page such as [cards](https://docs.adyen.com/payment-methods/cards#supported-cards), [iDEAL](https://docs.adyen.com/payment-methods/ideal), or [Klarna](https://docs.adyen.com/payment-methods/klarna).   If you want to refund a payment but are not sure whether it has been captured, use the [&#x60;/payments/{paymentPspReference}/reversals&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals) endpoint instead.  For more information, refer to [Refund](https://docs.adyen.com/online-payments/refund).

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

let apiInstance = new AdyenCheckoutApi.ModificationsApi();
let paymentPspReference = "paymentPspReference_example"; // String | The [`pspReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment that you want to refund.
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'paymentRefundRequest': new AdyenCheckoutApi.PaymentRefundRequest() // PaymentRefundRequest | 
};
apiInstance.postPaymentsPaymentPspReferenceRefunds(paymentPspReference, opts, (error, data, response) => {
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
 **paymentPspReference** | **String**| The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment that you want to refund. | 
 **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] 
 **paymentRefundRequest** | [**PaymentRefundRequest**](PaymentRefundRequest.md)|  | [optional] 

### Return type

[**PaymentRefundResponse**](PaymentRefundResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPaymentsPaymentPspReferenceReversals

> PaymentReversalResponse postPaymentsPaymentPspReferenceReversals(paymentPspReference, opts)

Refund or cancel a payment

[Refunds](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/refunds) a payment if it has already been captured, and [cancels](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels) a payment if it has not yet been captured. Returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**CANCEL_OR_REFUND** webhook](https://docs.adyen.com/online-payments/reverse#cancel-or-refund-webhook).  The reversed amount is always the full payment amount. &gt; Do not use this request for payments that involve multiple partial captures.  For more information, refer to [Reversal](https://docs.adyen.com/online-payments/reversal).

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

let apiInstance = new AdyenCheckoutApi.ModificationsApi();
let paymentPspReference = "paymentPspReference_example"; // String | The [`pspReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment that you want to reverse. 
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'paymentReversalRequest': new AdyenCheckoutApi.PaymentReversalRequest() // PaymentReversalRequest | 
};
apiInstance.postPaymentsPaymentPspReferenceReversals(paymentPspReference, opts, (error, data, response) => {
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
 **paymentPspReference** | **String**| The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment that you want to reverse.  | 
 **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] 
 **paymentReversalRequest** | [**PaymentReversalRequest**](PaymentReversalRequest.md)|  | [optional] 

### Return type

[**PaymentReversalResponse**](PaymentReversalResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

