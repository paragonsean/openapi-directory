# MagentoB2B.CustomersCustomerIdPasswordResetLinkTokenResetPasswordLinkTokenApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1ValidateResetPasswordLinkTokenGet**](CustomersCustomerIdPasswordResetLinkTokenResetPasswordLinkTokenApi.md#customerAccountManagementV1ValidateResetPasswordLinkTokenGet) | **GET** /V1/customers/{customerId}/password/resetLinkToken/{resetPasswordLinkToken} | customers/{customerId}/password/resetLinkToken/{resetPasswordLinkToken}



## customerAccountManagementV1ValidateResetPasswordLinkTokenGet

> Boolean customerAccountManagementV1ValidateResetPasswordLinkTokenGet(customerId, resetPasswordLinkToken)

customers/{customerId}/password/resetLinkToken/{resetPasswordLinkToken}

Check if password reset token is valid.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersCustomerIdPasswordResetLinkTokenResetPasswordLinkTokenApi();
let customerId = 56; // Number | If 0 is given then a customer will be matched by the RP token.
let resetPasswordLinkToken = "resetPasswordLinkToken_example"; // String | 
apiInstance.customerAccountManagementV1ValidateResetPasswordLinkTokenGet(customerId, resetPasswordLinkToken, (error, data, response) => {
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
 **customerId** | **Number**| If 0 is given then a customer will be matched by the RP token. | 
 **resetPasswordLinkToken** | **String**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

