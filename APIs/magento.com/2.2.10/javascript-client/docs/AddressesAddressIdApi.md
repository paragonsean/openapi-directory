# MagentoB2B.AddressesAddressIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAddressRepositoryV1DeleteByIdDelete**](AddressesAddressIdApi.md#customerAddressRepositoryV1DeleteByIdDelete) | **DELETE** /V1/addresses/{addressId} | addresses/{addressId}



## customerAddressRepositoryV1DeleteByIdDelete

> Boolean customerAddressRepositoryV1DeleteByIdDelete(addressId)

addresses/{addressId}

Delete customer address by ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.AddressesAddressIdApi();
let addressId = 56; // Number | 
apiInstance.customerAddressRepositoryV1DeleteByIdDelete(addressId, (error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

