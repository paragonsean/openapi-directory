# OpenBankingPaymentsInitiationService.SEPAPaymentsStatusApi

All URIs are relative to */openbanking/sandbox/connect/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsSepaCreditTransfersPaymentStatusPost**](SEPAPaymentsStatusApi.md#paymentsSepaCreditTransfersPaymentStatusPost) | **POST** /payments/sepa-credit-transfers/payment-status | Get payment status



## paymentsSepaCreditTransfersPaymentStatusPost

> PostPaymentsSepaCreditTransfersPaymentStatusOKBody paymentsSepaCreditTransfersPaymentStatusPost(body)

Get payment status

Get the status of an existing SEPA credit transfer

### Example

```javascript
import OpenBankingPaymentsInitiationService from 'open_banking_payments_initiation_service';

let apiInstance = new OpenBankingPaymentsInitiationService.SEPAPaymentsStatusApi();
let body = new OpenBankingPaymentsInitiationService.PostPaymentsSepaCreditTransfersPaymentStatusParamsBody(); // PostPaymentsSepaCreditTransfersPaymentStatusParamsBody | Request Body
apiInstance.paymentsSepaCreditTransfersPaymentStatusPost(body, (error, data, response) => {
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
 **body** | [**PostPaymentsSepaCreditTransfersPaymentStatusParamsBody**](PostPaymentsSepaCreditTransfersPaymentStatusParamsBody.md)| Request Body | 

### Return type

[**PostPaymentsSepaCreditTransfersPaymentStatusOKBody**](PostPaymentsSepaCreditTransfersPaymentStatusOKBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

