# BeanstreamPayments.PaymentsApi

All URIs are relative to *https://www.beanstream.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsPost**](PaymentsApi.md#paymentsPost) | **POST** /payments | Make Payment
[**paymentsTransIdCompletionsPost**](PaymentsApi.md#paymentsTransIdCompletionsPost) | **POST** /payments/{transId}/completions | Complete pre-auth
[**paymentsTransIdGet**](PaymentsApi.md#paymentsTransIdGet) | **GET** /payments/{transId} | Get payment
[**paymentsTransIdReturnsPost**](PaymentsApi.md#paymentsTransIdReturnsPost) | **POST** /payments/{transId}/returns | Return payment
[**paymentsTransIdVoidPost**](PaymentsApi.md#paymentsTransIdVoidPost) | **POST** /payments/{transId}/void | Void Transaction



## paymentsPost

> PaymentResponse paymentsPost(opts)

Make Payment

Make a payment using credit card, cash, cheque, profile, or token. Each payment type has its own json definition passed in the body. For all payments you have the standard Billing, Shipping, Comments, etc. fields that are optional. Only the amount is required along with the payment data for card, cash, cheque, profile, and token. You must change the payment_method for each payment type. Credit Card - \&quot;card\&quot;, Payment Profile - \&quot;payment_profile\&quot;, Legato Token - \&quot;token\&quot;, Cash - \&quot;cash\&quot;, Cheque - \&quot;cheque\&quot;, Interac - \&quot;interac\&quot;

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.PaymentsApi();
let opts = {
  'paymentRequest': new BeanstreamPayments.PaymentRequest() // PaymentRequest | 
};
apiInstance.paymentsPost(opts, (error, data, response) => {
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

[**PaymentResponse**](PaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## paymentsTransIdCompletionsPost

> PaymentResponse paymentsTransIdCompletionsPost(transId, opts)

Complete pre-auth

Complete a pre-authorized payment. The amount of the transaction to complete must be less than or equal to the original pre-auth amount. Complete must be set to true.

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.PaymentsApi();
let transId = 3.4; // Number | The transaction id.
let opts = {
  'paymentRequest': new BeanstreamPayments.PaymentRequest() // PaymentRequest | 
};
apiInstance.paymentsTransIdCompletionsPost(transId, opts, (error, data, response) => {
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
 **transId** | **Number**| The transaction id. | 
 **paymentRequest** | [**PaymentRequest**](PaymentRequest.md)|  | [optional] 

### Return type

[**PaymentResponse**](PaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## paymentsTransIdGet

> Transaction paymentsTransIdGet(transId)

Get payment

Get a previous payment (transaction).

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.PaymentsApi();
let transId = 3.4; // Number | The transaction id.
apiInstance.paymentsTransIdGet(transId, (error, data, response) => {
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
 **transId** | **Number**| The transaction id. | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## paymentsTransIdReturnsPost

> PaymentResponse paymentsTransIdReturnsPost(transId, _return)

Return payment

Return payment.

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.PaymentsApi();
let transId = 3.4; // Number | The transaction id.
let _return = new BeanstreamPayments.Return(); // Return | 
apiInstance.paymentsTransIdReturnsPost(transId, _return, (error, data, response) => {
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
 **transId** | **Number**| The transaction id. | 
 **_return** | [**Return**](Return.md)|  | 

### Return type

[**PaymentResponse**](PaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## paymentsTransIdVoidPost

> PaymentResponse paymentsTransIdVoidPost(transId, _void)

Void Transaction

Void a transaction. You can void payments, returns, pre-auths, and completions. It will cancel that transaction.

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.PaymentsApi();
let transId = 3.4; // Number | The transaction id to void.
let _void = new BeanstreamPayments.Void(); // Void | 
apiInstance.paymentsTransIdVoidPost(transId, _void, (error, data, response) => {
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
 **transId** | **Number**| The transaction id to void. | 
 **_void** | [**Void**](Void.md)|  | 

### Return type

[**PaymentResponse**](PaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

