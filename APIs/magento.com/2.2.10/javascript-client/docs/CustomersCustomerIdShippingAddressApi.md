# MagentoB2B.CustomersCustomerIdShippingAddressApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CustomersCustomerIdShippingAddressGet**](CustomersCustomerIdShippingAddressApi.md#v1CustomersCustomerIdShippingAddressGet) | **GET** /V1/customers/{customerId}/shippingAddress | customers/{customerId}/shippingAddress



## v1CustomersCustomerIdShippingAddressGet

> CustomerDataAddressInterface v1CustomersCustomerIdShippingAddressGet(customerId)

customers/{customerId}/shippingAddress

Retrieve default shipping address for the given customerId.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersCustomerIdShippingAddressApi();
let customerId = 56; // Number | 
apiInstance.v1CustomersCustomerIdShippingAddressGet(customerId, (error, data, response) => {
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

