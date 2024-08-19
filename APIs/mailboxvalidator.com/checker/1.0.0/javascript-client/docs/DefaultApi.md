# MailboxValidatorFreeEmailChecker.DefaultApi

All URIs are relative to *https://api.mailboxvalidator.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1EmailFreeGet**](DefaultApi.md#v1EmailFreeGet) | **GET** /v1/email/free | 



## v1EmailFreeGet

> String v1EmailFreeGet(email, key, opts)



The Free Email Checker API does validation on a single email address and returns if it is from a free email provider in either JSON or XML format.

### Example

```javascript
import MailboxValidatorFreeEmailChecker from 'mailbox_validator_free_email_checker';

let apiInstance = new MailboxValidatorFreeEmailChecker.DefaultApi();
let email = "email_example"; // String | The email address to check if is from a free email provider.
let key = "key_example"; // String | API key.
let opts = {
  'format': "format_example" // String | Return the result in json (default) or xml format.
};
apiInstance.v1EmailFreeGet(email, key, opts, (error, data, response) => {
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
 **email** | **String**| The email address to check if is from a free email provider. | 
 **key** | **String**| API key. | 
 **format** | **String**| Return the result in json (default) or xml format. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

