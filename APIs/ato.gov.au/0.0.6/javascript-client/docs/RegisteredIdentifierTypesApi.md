# BusinessRegistries.RegisteredIdentifierTypesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classificationsRegisteredIdentifierTypesGet**](RegisteredIdentifierTypesApi.md#classificationsRegisteredIdentifierTypesGet) | **GET** /classifications/registered-identifier-types | Retrieve a list of registered identifier types



## classificationsRegisteredIdentifierTypesGet

> [RegisteredIdentifierType] classificationsRegisteredIdentifierTypesGet(apiKey)

Retrieve a list of registered identifier types

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.RegisteredIdentifierTypesApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.classificationsRegisteredIdentifierTypesGet(apiKey, (error, data, response) => {
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

[**[RegisteredIdentifierType]**](RegisteredIdentifierType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

