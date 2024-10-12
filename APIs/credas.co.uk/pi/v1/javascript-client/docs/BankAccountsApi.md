# CredasApi.BankAccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify**](BankAccountsApi.md#verify) | **POST** /api/bank-accounts/verify | Verifies bank account details.



## verify

> CredasApiModelsBankAccountsAccountVerificationResponse verify(apikey, opts)

Verifies bank account details.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.BankAccountsApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsBankAccountsAccountVerificationRequest': new CredasApi.CredasApiModelsBankAccountsAccountVerificationRequest() // CredasApiModelsBankAccountsAccountVerificationRequest | Object containing data required to perform bank account verification.
};
apiInstance.verify(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsBankAccountsAccountVerificationRequest** | [**CredasApiModelsBankAccountsAccountVerificationRequest**](CredasApiModelsBankAccountsAccountVerificationRequest.md)| Object containing data required to perform bank account verification. | [optional] 

### Return type

[**CredasApiModelsBankAccountsAccountVerificationResponse**](CredasApiModelsBankAccountsAccountVerificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

