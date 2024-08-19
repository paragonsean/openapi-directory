# OpenBankingPaymentsInitiationService.CrossBorderPaymentsApi

All URIs are relative to */openbanking/sandbox/connect/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsCrossBorderCreditTransfersPost**](CrossBorderPaymentsApi.md#paymentsCrossBorderCreditTransfersPost) | **POST** /payments/cross-border-credit-transfers | Redeem the payment



## paymentsCrossBorderCreditTransfersPost

> PostPaymentsCrossBorderCreditTransfersOKBody paymentsCrossBorderCreditTransfersPost(body)

Redeem the payment

### Example

```javascript
import OpenBankingPaymentsInitiationService from 'open_banking_payments_initiation_service';

let apiInstance = new OpenBankingPaymentsInitiationService.CrossBorderPaymentsApi();
let body = new OpenBankingPaymentsInitiationService.PostPaymentsCrossBorderCreditTransfersParamsBody(); // PostPaymentsCrossBorderCreditTransfersParamsBody | Request Body
apiInstance.paymentsCrossBorderCreditTransfersPost(body, (error, data, response) => {
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
 **body** | [**PostPaymentsCrossBorderCreditTransfersParamsBody**](PostPaymentsCrossBorderCreditTransfersParamsBody.md)| Request Body | 

### Return type

[**PostPaymentsCrossBorderCreditTransfersOKBody**](PostPaymentsCrossBorderCreditTransfersOKBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

