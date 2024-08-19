# OpenBankingPaymentsInitiationService.DomesticPaymentsApi

All URIs are relative to */openbanking/sandbox/connect/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsDomesticCreditTransfersPost**](DomesticPaymentsApi.md#paymentsDomesticCreditTransfersPost) | **POST** /payments/domestic-credit-transfers | Redeem the payment



## paymentsDomesticCreditTransfersPost

> PostPaymentsDomesticCreditTransfersOKBody paymentsDomesticCreditTransfersPost(body)

Redeem the payment

Redeem the payment which was previously consented by the PSU.

### Example

```javascript
import OpenBankingPaymentsInitiationService from 'open_banking_payments_initiation_service';

let apiInstance = new OpenBankingPaymentsInitiationService.DomesticPaymentsApi();
let body = new OpenBankingPaymentsInitiationService.PostPaymentsDomesticCreditTransfersParamsBody(); // PostPaymentsDomesticCreditTransfersParamsBody | Request Body
apiInstance.paymentsDomesticCreditTransfersPost(body, (error, data, response) => {
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
 **body** | [**PostPaymentsDomesticCreditTransfersParamsBody**](PostPaymentsDomesticCreditTransfersParamsBody.md)| Request Body | 

### Return type

[**PostPaymentsDomesticCreditTransfersOKBody**](PostPaymentsDomesticCreditTransfersOKBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

