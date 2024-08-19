# OpenBankingPaymentsInitiationService.SEPAPaymentsApi

All URIs are relative to */openbanking/sandbox/connect/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsSepaCreditTransfersPost**](SEPAPaymentsApi.md#paymentsSepaCreditTransfersPost) | **POST** /payments/sepa-credit-transfers | Redeem the payment



## paymentsSepaCreditTransfersPost

> PostPaymentsSepaCreditTransfersOKBody paymentsSepaCreditTransfersPost(body)

Redeem the payment

Redeem a SEPA credit transfer previously consented by the PSU.

### Example

```javascript
import OpenBankingPaymentsInitiationService from 'open_banking_payments_initiation_service';

let apiInstance = new OpenBankingPaymentsInitiationService.SEPAPaymentsApi();
let body = new OpenBankingPaymentsInitiationService.PostPaymentsSepaCreditTransfersParamsBody(); // PostPaymentsSepaCreditTransfersParamsBody | Request Body
apiInstance.paymentsSepaCreditTransfersPost(body, (error, data, response) => {
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
 **body** | [**PostPaymentsSepaCreditTransfersParamsBody**](PostPaymentsSepaCreditTransfersParamsBody.md)| Request Body | 

### Return type

[**PostPaymentsSepaCreditTransfersOKBody**](PostPaymentsSepaCreditTransfersOKBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

