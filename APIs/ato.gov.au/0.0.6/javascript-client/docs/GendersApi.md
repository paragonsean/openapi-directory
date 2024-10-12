# BusinessRegistries.GendersApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classificationsGendersGet**](GendersApi.md#classificationsGendersGet) | **GET** /classifications/genders | Retrieve a list of genders



## classificationsGendersGet

> [Gender] classificationsGendersGet(apiKey)

Retrieve a list of genders

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.GendersApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.classificationsGendersGet(apiKey, (error, data, response) => {
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

[**[Gender]**](Gender.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

