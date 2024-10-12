# CredasApi.RegTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAll**](RegTypesApi.md#getAll) | **GET** /api/reg-types | Gets all available RegTypes.



## getAll

> [CredasApiModelsRegTypesRegType] getAll(apikey)

Gets all available RegTypes.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegTypesApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getAll(apikey, (error, data, response) => {
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
 **apikey** | **String**| ApiKey supplied. | 

### Return type

[**[CredasApiModelsRegTypesRegType]**](CredasApiModelsRegTypesRegType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

