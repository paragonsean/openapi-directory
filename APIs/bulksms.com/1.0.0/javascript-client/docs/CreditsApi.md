# BulkSmsJsonRestApi.CreditsApi

All URIs are relative to *https://api.bulksms.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**creditTransferPost**](CreditsApi.md#creditTransferPost) | **POST** /credit/transfer | Transfer credits to another account



## creditTransferPost

> creditTransferPost(transferEntry)

Transfer credits to another account

Before you can use the transfer credits endpoint, the _credit-transfer facility_ must be activated for your account.  You can request activation from &#x60;support@bulksms.com&#x60;.   The recipient must be an enabled account that uses the same currency as your account. 

### Example

```javascript
import BulkSmsJsonRestApi from 'bulk_sms_json_rest_api';
let defaultClient = BulkSmsJsonRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new BulkSmsJsonRestApi.CreditsApi();
let transferEntry = new BulkSmsJsonRestApi.TransferEntry(); // TransferEntry | Contains details of the transfer request. 
apiInstance.creditTransferPost(transferEntry, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferEntry** | [**TransferEntry**](TransferEntry.md)| Contains details of the transfer request.  | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

