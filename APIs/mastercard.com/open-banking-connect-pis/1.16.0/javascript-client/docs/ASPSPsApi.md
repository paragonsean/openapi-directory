# OpenBankingPaymentsInitiationService.ASPSPsApi

All URIs are relative to */openbanking/sandbox/connect/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsAspspsPost**](ASPSPsApi.md#paymentsAspspsPost) | **POST** /payments/aspsps | Get list of ASPSPs



## paymentsAspspsPost

> PostAspspsOKBody paymentsAspspsPost(body)

Get list of ASPSPs

Get the list of all active ASPSPs supported by the Open Banking Connect platform at this time with possibility to filter by id, name or country. This list is updated regularly as new ASPSPs are connected.

### Example

```javascript
import OpenBankingPaymentsInitiationService from 'open_banking_payments_initiation_service';

let apiInstance = new OpenBankingPaymentsInitiationService.ASPSPsApi();
let body = new OpenBankingPaymentsInitiationService.PostAspspsParamsBody(); // PostAspspsParamsBody | Request Body
apiInstance.paymentsAspspsPost(body, (error, data, response) => {
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
 **body** | [**PostAspspsParamsBody**](PostAspspsParamsBody.md)| Request Body | 

### Return type

[**PostAspspsOKBody**](PostAspspsOKBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

