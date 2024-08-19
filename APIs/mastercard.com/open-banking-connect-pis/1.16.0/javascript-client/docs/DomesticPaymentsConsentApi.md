# OpenBankingPaymentsInitiationService.DomesticPaymentsConsentApi

All URIs are relative to */openbanking/sandbox/connect/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsDomesticCreditTransfersConsentsPost**](DomesticPaymentsConsentApi.md#paymentsDomesticCreditTransfersConsentsPost) | **POST** /payments/domestic-credit-transfers/consents | Request consent initiation via redirect



## paymentsDomesticCreditTransfersConsentsPost

> PostPaymentsDomesticCreditTransfersConsentsOKBody paymentsDomesticCreditTransfersConsentsPost(body)

Request consent initiation via redirect

Request Payment Initiation Consent for a domestic credit transfer on behalf of the PSU.

### Example

```javascript
import OpenBankingPaymentsInitiationService from 'open_banking_payments_initiation_service';

let apiInstance = new OpenBankingPaymentsInitiationService.DomesticPaymentsConsentApi();
let body = new OpenBankingPaymentsInitiationService.PostPaymentsDomesticCreditTransfersConsentsParamsBody(); // PostPaymentsDomesticCreditTransfersConsentsParamsBody | Domestic Payment consent to be wired via Faster Payment System
apiInstance.paymentsDomesticCreditTransfersConsentsPost(body, (error, data, response) => {
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
 **body** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBody**](PostPaymentsDomesticCreditTransfersConsentsParamsBody.md)| Domestic Payment consent to be wired via Faster Payment System | 

### Return type

[**PostPaymentsDomesticCreditTransfersConsentsOKBody**](PostPaymentsDomesticCreditTransfersConsentsOKBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

