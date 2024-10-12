# MagentoB2B.CustomersMeBillingAddressApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1GetDefaultBillingAddressGet**](CustomersMeBillingAddressApi.md#customerAccountManagementV1GetDefaultBillingAddressGet) | **GET** /V1/customers/me/billingAddress | customers/me/billingAddress



## customerAccountManagementV1GetDefaultBillingAddressGet

> CustomerDataAddressInterface customerAccountManagementV1GetDefaultBillingAddressGet()

customers/me/billingAddress

Retrieve default billing address for the given customerId.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersMeBillingAddressApi();
apiInstance.customerAccountManagementV1GetDefaultBillingAddressGet((error, data, response) => {
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

