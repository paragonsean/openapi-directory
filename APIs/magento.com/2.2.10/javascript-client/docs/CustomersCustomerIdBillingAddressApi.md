# MagentoB2B.CustomersCustomerIdBillingAddressApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CustomersCustomerIdBillingAddressGet**](CustomersCustomerIdBillingAddressApi.md#v1CustomersCustomerIdBillingAddressGet) | **GET** /V1/customers/{customerId}/billingAddress | customers/{customerId}/billingAddress



## v1CustomersCustomerIdBillingAddressGet

> CustomerDataAddressInterface v1CustomersCustomerIdBillingAddressGet(customerId)

customers/{customerId}/billingAddress

Retrieve default billing address for the given customerId.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersCustomerIdBillingAddressApi();
let customerId = 56; // Number | 
apiInstance.v1CustomersCustomerIdBillingAddressGet(customerId, (error, data, response) => {
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

[**CustomerDataAddressInterface**](CustomerDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

