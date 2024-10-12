# MagentoB2B.CustomersCustomerIdConfirmApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1GetConfirmationStatusGet**](CustomersCustomerIdConfirmApi.md#customerAccountManagementV1GetConfirmationStatusGet) | **GET** /V1/customers/{customerId}/confirm | customers/{customerId}/confirm



## customerAccountManagementV1GetConfirmationStatusGet

> String customerAccountManagementV1GetConfirmationStatusGet(customerId)

customers/{customerId}/confirm

Gets the account confirmation status.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersCustomerIdConfirmApi();
let customerId = 56; // Number | 
apiInstance.customerAccountManagementV1GetConfirmationStatusGet(customerId, (error, data, response) => {
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
 **customerId** | **Number**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

