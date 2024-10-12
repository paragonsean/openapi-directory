# MagentoB2B.CustomersValidateApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1ValidatePut**](CustomersValidateApi.md#customerAccountManagementV1ValidatePut) | **PUT** /V1/customers/validate | customers/validate



## customerAccountManagementV1ValidatePut

> CustomerDataValidationResultsInterface customerAccountManagementV1ValidatePut(opts)

customers/validate

Validate customer data.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersValidateApi();
let opts = {
  'customerAccountManagementV1ValidatePutRequest': new MagentoB2B.CustomerAccountManagementV1ValidatePutRequest() // CustomerAccountManagementV1ValidatePutRequest | 
};
apiInstance.customerAccountManagementV1ValidatePut(opts, (error, data, response) => {
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
 **customerAccountManagementV1ValidatePutRequest** | [**CustomerAccountManagementV1ValidatePutRequest**](CustomerAccountManagementV1ValidatePutRequest.md)|  | [optional] 

### Return type

[**CustomerDataValidationResultsInterface**](CustomerDataValidationResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

