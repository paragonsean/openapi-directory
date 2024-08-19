# BusinessRegistries.NameTypesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classificationsNameTypesGet**](NameTypesApi.md#classificationsNameTypesGet) | **GET** /classifications/name-types | Retrieve a list of name types



## classificationsNameTypesGet

> [NameType] classificationsNameTypesGet(apiKey)

Retrieve a list of name types

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.NameTypesApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.classificationsNameTypesGet(apiKey, (error, data, response) => {
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

[**[NameType]**](NameType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

