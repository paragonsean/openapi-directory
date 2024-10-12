# AdyenCheckoutApi.ClassicCheckoutSDKApi

All URIs are relative to *https://checkout-test.adyen.com/v41*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postPaymentSession**](ClassicCheckoutSDKApi.md#postPaymentSession) | **POST** /paymentSession | Create a payment session
[**postPaymentsResult**](ClassicCheckoutSDKApi.md#postPaymentsResult) | **POST** /payments/result | Verify a payment result



## postPaymentSession

> PaymentSetupResponse postPaymentSession(opts)

Create a payment session

Provides the data object that can be used to start the Checkout SDK. To set up the payment, pass its amount, currency, and other required parameters. We use this to optimise the payment flow and perform better risk assessment of the transaction.  For more information, refer to [How it works](https://docs.adyen.com/online-payments#howitworks).

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

let apiInstance = new AdyenCheckoutApi.ClassicCheckoutSDKApi();
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'paymentSetupRequest': new AdyenCheckoutApi.PaymentSetupRequest() // PaymentSetupRequest | 
};
apiInstance.postPaymentSession(opts, (error, data, response) => {
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
 **paymentSetupRequest** | [**PaymentSetupRequest**](PaymentSetupRequest.md)|  | [optional] 

### Return type

[**PaymentSetupResponse**](PaymentSetupResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPaymentsResult

> PaymentVerificationResponse postPaymentsResult(opts)

Verify a payment result

Verifies the payment result using the payload returned from the Checkout SDK.  For more information, refer to [How it works](https://docs.adyen.com/online-payments#howitworks).

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

let apiInstance = new AdyenCheckoutApi.ClassicCheckoutSDKApi();
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'paymentVerificationRequest': new AdyenCheckoutApi.PaymentVerificationRequest() // PaymentVerificationRequest | 
};
apiInstance.postPaymentsResult(opts, (error, data, response) => {
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
 **paymentVerificationRequest** | [**PaymentVerificationRequest**](PaymentVerificationRequest.md)|  | [optional] 

### Return type

[**PaymentVerificationResponse**](PaymentVerificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

