# MagentoB2B.CustomersAddressesAddressIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAddressRepositoryV1GetByIdGet**](CustomersAddressesAddressIdApi.md#customerAddressRepositoryV1GetByIdGet) | **GET** /V1/customers/addresses/{addressId} | customers/addresses/{addressId}



## customerAddressRepositoryV1GetByIdGet

> CustomerDataAddressInterface customerAddressRepositoryV1GetByIdGet(addressId)

customers/addresses/{addressId}

Retrieve customer address.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersAddressesAddressIdApi();
let addressId = 56; // Number | 
apiInstance.customerAddressRepositoryV1GetByIdGet(addressId, (error, data, response) => {
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
 **addressId** | **Number**|  | 

### Return type

[**CustomerDataAddressInterface**](CustomerDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

