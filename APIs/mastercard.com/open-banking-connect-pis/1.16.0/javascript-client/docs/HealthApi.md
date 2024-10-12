# OpenBankingPaymentsInitiationService.HealthApi

All URIs are relative to */openbanking/sandbox/connect/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsHealthGet**](HealthApi.md#paymentsHealthGet) | **GET** /payments/health | Returns the status of each connectivity provider



## paymentsHealthGet

> ApiHealth paymentsHealthGet()

Returns the status of each connectivity provider

Returns the status of each connectivity provider

### Example

```javascript
import OpenBankingPaymentsInitiationService from 'open_banking_payments_initiation_service';

let apiInstance = new OpenBankingPaymentsInitiationService.HealthApi();
apiInstance.paymentsHealthGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiHealth**](ApiHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

