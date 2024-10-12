# MagentoB2B.CustomersCustomerIdCartsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CustomersCustomerIdCartsPost**](CustomersCustomerIdCartsApi.md#v1CustomersCustomerIdCartsPost) | **POST** /V1/customers/{customerId}/carts | customers/{customerId}/carts



## v1CustomersCustomerIdCartsPost

> Number v1CustomersCustomerIdCartsPost(customerId)

customers/{customerId}/carts

Creates an empty cart and quote for a specified customer if customer does not have a cart yet.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersCustomerIdCartsApi();
let customerId = 56; // Number | The customer ID.
apiInstance.v1CustomersCustomerIdCartsPost(customerId, (error, data, response) => {
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
 **customerId** | **Number**| The customer ID. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

