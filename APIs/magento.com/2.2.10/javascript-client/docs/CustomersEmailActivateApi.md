# MagentoB2B.CustomersEmailActivateApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1ActivatePut**](CustomersEmailActivateApi.md#customerAccountManagementV1ActivatePut) | **PUT** /V1/customers/{email}/activate | customers/{email}/activate



## customerAccountManagementV1ActivatePut

> CustomerDataCustomerInterface customerAccountManagementV1ActivatePut(email, opts)

customers/{email}/activate

Activate a customer account using a key that was sent in a confirmation email.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersEmailActivateApi();
let email = "email_example"; // String | 
let opts = {
  'customerAccountManagementV1ActivateByIdPutRequest': new MagentoB2B.CustomerAccountManagementV1ActivateByIdPutRequest() // CustomerAccountManagementV1ActivateByIdPutRequest | 
};
apiInstance.customerAccountManagementV1ActivatePut(email, opts, (error, data, response) => {
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
 **email** | **String**|  | 
 **customerAccountManagementV1ActivateByIdPutRequest** | [**CustomerAccountManagementV1ActivateByIdPutRequest**](CustomerAccountManagementV1ActivateByIdPutRequest.md)|  | [optional] 

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

