# OpenBankingPaymentsInitiationService.CrossBorderPaymentsStatusApi

All URIs are relative to */openbanking/sandbox/connect/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsCrossBorderCreditTransfersPaymentStatusPost**](CrossBorderPaymentsStatusApi.md#paymentsCrossBorderCreditTransfersPaymentStatusPost) | **POST** /payments/cross-border-credit-transfers/payment-status | Get payment status



## paymentsCrossBorderCreditTransfersPaymentStatusPost

> PostPaymentsCrossBorderCreditTransfersPaymentStatusOKBody paymentsCrossBorderCreditTransfersPaymentStatusPost(body)

Get payment status

### Example

```javascript
import OpenBankingPaymentsInitiationService from 'open_banking_payments_initiation_service';

let apiInstance = new OpenBankingPaymentsInitiationService.CrossBorderPaymentsStatusApi();
let body = new OpenBankingPaymentsInitiationService.PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody(); // PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody | Request Body
apiInstance.paymentsCrossBorderCreditTransfersPaymentStatusPost(body, (error, data, response) => {
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
 **body** | [**PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody**](PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody.md)| Request Body | 

### Return type

[**PostPaymentsCrossBorderCreditTransfersPaymentStatusOKBody**](PostPaymentsCrossBorderCreditTransfersPaymentStatusOKBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

