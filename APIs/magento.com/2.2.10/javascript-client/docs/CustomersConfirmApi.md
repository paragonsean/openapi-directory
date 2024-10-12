# MagentoB2B.CustomersConfirmApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1ResendConfirmationPost**](CustomersConfirmApi.md#customerAccountManagementV1ResendConfirmationPost) | **POST** /V1/customers/confirm | customers/confirm



## customerAccountManagementV1ResendConfirmationPost

> Boolean customerAccountManagementV1ResendConfirmationPost(opts)

customers/confirm

Resend confirmation email.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersConfirmApi();
let opts = {
  'customerAccountManagementV1ResendConfirmationPostRequest': new MagentoB2B.CustomerAccountManagementV1ResendConfirmationPostRequest() // CustomerAccountManagementV1ResendConfirmationPostRequest | 
};
apiInstance.customerAccountManagementV1ResendConfirmationPost(opts, (error, data, response) => {
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
 **customerAccountManagementV1ResendConfirmationPostRequest** | [**CustomerAccountManagementV1ResendConfirmationPostRequest**](CustomerAccountManagementV1ResendConfirmationPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

