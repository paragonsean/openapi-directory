# OpenBankingPaymentsInitiationService.SEPAPaymentsConsentApi

All URIs are relative to */openbanking/sandbox/connect/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsSepaCreditTransfersConsentsPost**](SEPAPaymentsConsentApi.md#paymentsSepaCreditTransfersConsentsPost) | **POST** /payments/sepa-credit-transfers/consents | Request consent initiation via redirect



## paymentsSepaCreditTransfersConsentsPost

> PostPaymentsSepaCreditTransfersConsentsOKBody paymentsSepaCreditTransfersConsentsPost(body)

Request consent initiation via redirect

Request a SEPA credit transfer consent on behalf of the PSU via a URL redirect to the ASPSP.

### Example

```javascript
import OpenBankingPaymentsInitiationService from 'open_banking_payments_initiation_service';

let apiInstance = new OpenBankingPaymentsInitiationService.SEPAPaymentsConsentApi();
let body = new OpenBankingPaymentsInitiationService.PostPaymentsSepaCreditTransfersConsentsParamsBody(); // PostPaymentsSepaCreditTransfersConsentsParamsBody | 
apiInstance.paymentsSepaCreditTransfersConsentsPost(body, (error, data, response) => {
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
 **body** | [**PostPaymentsSepaCreditTransfersConsentsParamsBody**](PostPaymentsSepaCreditTransfersConsentsParamsBody.md)|  | 

### Return type

[**PostPaymentsSepaCreditTransfersConsentsOKBody**](PostPaymentsSepaCreditTransfersConsentsOKBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

