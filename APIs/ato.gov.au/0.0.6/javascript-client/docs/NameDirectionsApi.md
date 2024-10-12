# BusinessRegistries.NameDirectionsApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classificationsNameDirectionsGet**](NameDirectionsApi.md#classificationsNameDirectionsGet) | **GET** /classifications/name-directions | Retrieve a list of name directions



## classificationsNameDirectionsGet

> [NameDirection] classificationsNameDirectionsGet(apiKey)

Retrieve a list of name directions

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.NameDirectionsApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.classificationsNameDirectionsGet(apiKey, (error, data, response) => {
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

[**[NameDirection]**](NameDirection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

