# SalesLoftPlatform.ExternalEmailsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2ExternalEmailsJsonPost**](ExternalEmailsApi.md#v2ExternalEmailsJsonPost) | **POST** /v2/external_emails.json | Create an External Email



## v2ExternalEmailsJsonPost

> ExternalEmail v2ExternalEmailsJsonPost(mailbox, raw)

Create an External Email

Creates an external email object. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.ExternalEmailsApi();
let mailbox = "mailbox_example"; // String | Email address of mailbox email was sent to
let raw = "raw_example"; // String | Base64 encoded MIME email content
apiInstance.v2ExternalEmailsJsonPost(mailbox, raw, (error, data, response) => {
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
 **mailbox** | **String**| Email address of mailbox email was sent to | 
 **raw** | **String**| Base64 encoded MIME email content | 

### Return type

[**ExternalEmail**](ExternalEmail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

