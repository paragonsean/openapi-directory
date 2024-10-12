# MagentoB2B.CustomersApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1CreateAccountPost**](CustomersApi.md#customerAccountManagementV1CreateAccountPost) | **POST** /V1/customers | customers



## customerAccountManagementV1CreateAccountPost

> CustomerDataCustomerInterface customerAccountManagementV1CreateAccountPost(opts)

customers

Create customer account. Perform necessary business operations like sending email.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersApi();
let opts = {
  'customerAccountManagementV1CreateAccountPostRequest': new MagentoB2B.CustomerAccountManagementV1CreateAccountPostRequest() // CustomerAccountManagementV1CreateAccountPostRequest | 
};
apiInstance.customerAccountManagementV1CreateAccountPost(opts, (error, data, response) => {
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
 **customerAccountManagementV1CreateAccountPostRequest** | [**CustomerAccountManagementV1CreateAccountPostRequest**](CustomerAccountManagementV1CreateAccountPostRequest.md)|  | [optional] 

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

