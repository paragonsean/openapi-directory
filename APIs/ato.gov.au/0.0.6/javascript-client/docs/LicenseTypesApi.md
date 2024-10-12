# BusinessRegistries.LicenseTypesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classificationsLicenseTypesGet**](LicenseTypesApi.md#classificationsLicenseTypesGet) | **GET** /classifications/license-types | Retrieve a list of license types



## classificationsLicenseTypesGet

> [LicenseType] classificationsLicenseTypesGet(apiKey)

Retrieve a list of license types

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.LicenseTypesApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.classificationsLicenseTypesGet(apiKey, (error, data, response) => {
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

[**[LicenseType]**](LicenseType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

