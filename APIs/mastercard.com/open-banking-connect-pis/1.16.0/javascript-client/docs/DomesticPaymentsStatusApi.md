# OpenBankingPaymentsInitiationService.DomesticPaymentsStatusApi

All URIs are relative to */openbanking/sandbox/connect/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsDomesticCreditTransfersPaymentStatusPost**](DomesticPaymentsStatusApi.md#paymentsDomesticCreditTransfersPaymentStatusPost) | **POST** /payments/domestic-credit-transfers/payment-status | Get payment status



## paymentsDomesticCreditTransfersPaymentStatusPost

> PostPaymentsDomesticCreditTransfersPaymentStatusOKBody paymentsDomesticCreditTransfersPaymentStatusPost(body)

Get payment status

Get the status for an existing domestic credit transfer payment.

### Example

```javascript
import OpenBankingPaymentsInitiationService from 'open_banking_payments_initiation_service';

let apiInstance = new OpenBankingPaymentsInitiationService.DomesticPaymentsStatusApi();
let body = new OpenBankingPaymentsInitiationService.PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody(); // PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody | Request Body
apiInstance.paymentsDomesticCreditTransfersPaymentStatusPost(body, (error, data, response) => {
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
 **body** | [**PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody**](PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody.md)| Request Body | 

### Return type

[**PostPaymentsDomesticCreditTransfersPaymentStatusOKBody**](PostPaymentsDomesticCreditTransfersPaymentStatusOKBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

