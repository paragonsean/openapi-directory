# MagentoB2B.CustomersMePasswordApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1ChangePasswordByIdPut**](CustomersMePasswordApi.md#customerAccountManagementV1ChangePasswordByIdPut) | **PUT** /V1/customers/me/password | customers/me/password



## customerAccountManagementV1ChangePasswordByIdPut

> Boolean customerAccountManagementV1ChangePasswordByIdPut(opts)

customers/me/password

Change customer password.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersMePasswordApi();
let opts = {
  'customerAccountManagementV1ChangePasswordByIdPutRequest': new MagentoB2B.CustomerAccountManagementV1ChangePasswordByIdPutRequest() // CustomerAccountManagementV1ChangePasswordByIdPutRequest | 
};
apiInstance.customerAccountManagementV1ChangePasswordByIdPut(opts, (error, data, response) => {
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
 **customerAccountManagementV1ChangePasswordByIdPutRequest** | [**CustomerAccountManagementV1ChangePasswordByIdPutRequest**](CustomerAccountManagementV1ChangePasswordByIdPutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

