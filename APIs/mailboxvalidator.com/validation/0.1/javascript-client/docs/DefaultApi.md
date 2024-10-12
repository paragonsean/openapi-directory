# MailboxValidatorEmailValidation.DefaultApi

All URIs are relative to *https://api.mailboxvalidator.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1ValidationSingleGet**](DefaultApi.md#v1ValidationSingleGet) | **GET** /v1/validation/single | 



## v1ValidationSingleGet

> String v1ValidationSingleGet(email, key, opts)



The Single Validation API does validation on a single email address and returns all the validation results in either JSON or XML format.

### Example

```javascript
import MailboxValidatorEmailValidation from 'mailbox_validator_email_validation';

let apiInstance = new MailboxValidatorEmailValidation.DefaultApi();
let email = "email_example"; // String | The email address to be validated.
let key = "key_example"; // String | API key.
let opts = {
  'format': "format_example" // String | Return the result in json (default) or xml format.
};
apiInstance.v1ValidationSingleGet(email, key, opts, (error, data, response) => {
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
 **email** | **String**| The email address to be validated. | 
 **key** | **String**| API key. | 
 **format** | **String**| Return the result in json (default) or xml format. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

