# BusinessRegistries.ElectronicAddressTypesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classificationsElectronicAddressTypesGet**](ElectronicAddressTypesApi.md#classificationsElectronicAddressTypesGet) | **GET** /classifications/electronic-address-types | Retrieve a list of electronic address types



## classificationsElectronicAddressTypesGet

> [ElectronicAddressType] classificationsElectronicAddressTypesGet(apiKey)

Retrieve a list of electronic address types

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.ElectronicAddressTypesApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.classificationsElectronicAddressTypesGet(apiKey, (error, data, response) => {
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

[**[ElectronicAddressType]**](ElectronicAddressType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

