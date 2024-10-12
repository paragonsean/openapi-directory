# MagentoB2B.CustomersMeActivateApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1ActivateByIdPut**](CustomersMeActivateApi.md#customerAccountManagementV1ActivateByIdPut) | **PUT** /V1/customers/me/activate | customers/me/activate



## customerAccountManagementV1ActivateByIdPut

> CustomerDataCustomerInterface customerAccountManagementV1ActivateByIdPut(opts)

customers/me/activate

Activate a customer account using a key that was sent in a confirmation email.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersMeActivateApi();
let opts = {
  'customerAccountManagementV1ActivateByIdPutRequest': new MagentoB2B.CustomerAccountManagementV1ActivateByIdPutRequest() // CustomerAccountManagementV1ActivateByIdPutRequest | 
};
apiInstance.customerAccountManagementV1ActivateByIdPut(opts, (error, data, response) => {
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
 **customerAccountManagementV1ActivateByIdPutRequest** | [**CustomerAccountManagementV1ActivateByIdPutRequest**](CustomerAccountManagementV1ActivateByIdPutRequest.md)|  | [optional] 

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

