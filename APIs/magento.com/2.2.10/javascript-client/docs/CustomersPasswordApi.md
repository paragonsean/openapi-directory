# MagentoB2B.CustomersPasswordApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1InitiatePasswordResetPut**](CustomersPasswordApi.md#customerAccountManagementV1InitiatePasswordResetPut) | **PUT** /V1/customers/password | customers/password



## customerAccountManagementV1InitiatePasswordResetPut

> Boolean customerAccountManagementV1InitiatePasswordResetPut(opts)

customers/password

Send an email to the customer with a password reset link.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersPasswordApi();
let opts = {
  'customerAccountManagementV1InitiatePasswordResetPutRequest': new MagentoB2B.CustomerAccountManagementV1InitiatePasswordResetPutRequest() // CustomerAccountManagementV1InitiatePasswordResetPutRequest | 
};
apiInstance.customerAccountManagementV1InitiatePasswordResetPut(opts, (error, data, response) => {
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
 **customerAccountManagementV1InitiatePasswordResetPutRequest** | [**CustomerAccountManagementV1InitiatePasswordResetPutRequest**](CustomerAccountManagementV1InitiatePasswordResetPutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

