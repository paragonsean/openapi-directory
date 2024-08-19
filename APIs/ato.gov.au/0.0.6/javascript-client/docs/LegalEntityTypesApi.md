# BusinessRegistries.LegalEntityTypesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classificationsLegalEntityTypesGet**](LegalEntityTypesApi.md#classificationsLegalEntityTypesGet) | **GET** /classifications/legal-entity-types | Retrieve a list of legal entity types



## classificationsLegalEntityTypesGet

> [LegalEntityType] classificationsLegalEntityTypesGet(apiKey)

Retrieve a list of legal entity types

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.LegalEntityTypesApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.classificationsLegalEntityTypesGet(apiKey, (error, data, response) => {
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

[**[LegalEntityType]**](LegalEntityType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

