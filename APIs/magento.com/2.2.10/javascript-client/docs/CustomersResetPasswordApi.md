# MagentoB2B.CustomersResetPasswordApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1ResetPasswordPost**](CustomersResetPasswordApi.md#customerAccountManagementV1ResetPasswordPost) | **POST** /V1/customers/resetPassword | customers/resetPassword



## customerAccountManagementV1ResetPasswordPost

> Boolean customerAccountManagementV1ResetPasswordPost(opts)

customers/resetPassword

Reset customer password.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersResetPasswordApi();
let opts = {
  'customerAccountManagementV1ResetPasswordPostRequest': new MagentoB2B.CustomerAccountManagementV1ResetPasswordPostRequest() // CustomerAccountManagementV1ResetPasswordPostRequest | 
};
apiInstance.customerAccountManagementV1ResetPasswordPost(opts, (error, data, response) => {
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
 **customerAccountManagementV1ResetPasswordPostRequest** | [**CustomerAccountManagementV1ResetPasswordPostRequest**](CustomerAccountManagementV1ResetPasswordPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

