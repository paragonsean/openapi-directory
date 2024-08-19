# OpenBankingPaymentsInitiationService.PIConsentsRawApi

All URIs are relative to */openbanking/sandbox/connect/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsConsentsRawPost**](PIConsentsRawApi.md#paymentsConsentsRawPost) | **POST** /payments/consents/raw | Extracts the original raw consent given by the aspsp



## paymentsConsentsRawPost

> PostPaymentsConsentsRawOKBody paymentsConsentsRawPost(body)

Extracts the original raw consent given by the aspsp

Extracts the original raw consent given by the aspsp

### Example

```javascript
import OpenBankingPaymentsInitiationService from 'open_banking_payments_initiation_service';

let apiInstance = new OpenBankingPaymentsInitiationService.PIConsentsRawApi();
let body = new OpenBankingPaymentsInitiationService.PostPaymentsConsentsRawParamsBody(); // PostPaymentsConsentsRawParamsBody | Request Body
apiInstance.paymentsConsentsRawPost(body, (error, data, response) => {
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
 **body** | [**PostPaymentsConsentsRawParamsBody**](PostPaymentsConsentsRawParamsBody.md)| Request Body | 

### Return type

[**PostPaymentsConsentsRawOKBody**](PostPaymentsConsentsRawOKBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

