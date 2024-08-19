# MdesCustomerService.SystemStatusApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systemstatusGet**](SystemStatusApi.md#systemstatusGet) | **GET** /systemstatus | 



## systemstatusGet

> SystemStatusResponseSchema systemstatusGet()



Returns the overall system status of the Mastercard Digital Enablement Service.

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.SystemStatusApi();
apiInstance.systemstatusGet((error, data, response) => {
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

[**SystemStatusResponseSchema**](SystemStatusResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

