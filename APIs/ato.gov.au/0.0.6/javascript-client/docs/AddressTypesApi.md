# BusinessRegistries.AddressTypesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classificationsAddressTypesGet**](AddressTypesApi.md#classificationsAddressTypesGet) | **GET** /classifications/address-types | Retrieve a list of address types



## classificationsAddressTypesGet

> [AddressType] classificationsAddressTypesGet(apiKey)

Retrieve a list of address types

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.AddressTypesApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.classificationsAddressTypesGet(apiKey, (error, data, response) => {
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
 **apiKey** | **String**| The API key. | 

### Return type

[**[AddressType]**](AddressType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

