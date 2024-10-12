# MagentoB2B.CustomersMeShippingAddressApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1GetDefaultShippingAddressGet**](CustomersMeShippingAddressApi.md#customerAccountManagementV1GetDefaultShippingAddressGet) | **GET** /V1/customers/me/shippingAddress | customers/me/shippingAddress



## customerAccountManagementV1GetDefaultShippingAddressGet

> CustomerDataAddressInterface customerAccountManagementV1GetDefaultShippingAddressGet()

customers/me/shippingAddress

Retrieve default shipping address for the given customerId.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersMeShippingAddressApi();
apiInstance.customerAccountManagementV1GetDefaultShippingAddressGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CustomerDataAddressInterface**](CustomerDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

