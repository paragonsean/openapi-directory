# OpenBankingPaymentsInitiationService.CrossBorderPaymentsConsentApi

All URIs are relative to */openbanking/sandbox/connect/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsCrossBorderCreditTransfersConsentsPost**](CrossBorderPaymentsConsentApi.md#paymentsCrossBorderCreditTransfersConsentsPost) | **POST** /payments/cross-border-credit-transfers/consents | Request consent initiation via redirect



## paymentsCrossBorderCreditTransfersConsentsPost

> PostPaymentsCrossBorderCreditTransfersConsentsOKBody paymentsCrossBorderCreditTransfersConsentsPost(body)

Request consent initiation via redirect

### Example

```javascript
import OpenBankingPaymentsInitiationService from 'open_banking_payments_initiation_service';

let apiInstance = new OpenBankingPaymentsInitiationService.CrossBorderPaymentsConsentApi();
let body = new OpenBankingPaymentsInitiationService.PostPaymentsCrossBorderCreditTransfersConsentsParamsBody(); // PostPaymentsCrossBorderCreditTransfersConsentsParamsBody | Cross border payment consent
apiInstance.paymentsCrossBorderCreditTransfersConsentsPost(body, (error, data, response) => {
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
 **body** | [**PostPaymentsCrossBorderCreditTransfersConsentsParamsBody**](PostPaymentsCrossBorderCreditTransfersConsentsParamsBody.md)| Cross border payment consent | 

### Return type

[**PostPaymentsCrossBorderCreditTransfersConsentsOKBody**](PostPaymentsCrossBorderCreditTransfersConsentsOKBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

