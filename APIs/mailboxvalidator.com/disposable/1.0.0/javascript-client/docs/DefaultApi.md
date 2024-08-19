# MailboxValidatorDisposableEmailChecker.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/mailboxvalidator/MailboxValidator-Disposable-Email-Checker/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1EmailDisposableGet**](DefaultApi.md#v1EmailDisposableGet) | **GET** /v1/email/disposable | 



## v1EmailDisposableGet

> String v1EmailDisposableGet(email, key, opts)



The Disposable Email Checker API does checking on a single email address and returns if it is from a disposable email provider in either JSON or XML format.

### Example

```javascript
import MailboxValidatorDisposableEmailChecker from 'mailbox_validator_disposable_email_checker';

let apiInstance = new MailboxValidatorDisposableEmailChecker.DefaultApi();
let email = "email_example"; // String | The email address to check if is from a disposable email provider.
let key = "key_example"; // String | API key.
let opts = {
  'format': "format_example" // String | Return the result in json (default) or xml format.
};
apiInstance.v1EmailDisposableGet(email, key, opts, (error, data, response) => {
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
 **email** | **String**| The email address to check if is from a disposable email provider. | 
 **key** | **String**| API key. | 
 **format** | **String**| Return the result in json (default) or xml format. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

