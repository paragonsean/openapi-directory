# BusinessRegistries.NamePrefixesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classificationsNamePrefixesGet**](NamePrefixesApi.md#classificationsNamePrefixesGet) | **GET** /classifications/name-prefixes | Retrieve a list of name prefixes



## classificationsNamePrefixesGet

> [NamePrefix] classificationsNamePrefixesGet(apiKey)

Retrieve a list of name prefixes

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.NamePrefixesApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.classificationsNamePrefixesGet(apiKey, (error, data, response) => {
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

[**[NamePrefix]**](NamePrefix.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

