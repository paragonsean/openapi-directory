# BusinessRegistries.BusinessNamesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**businessNamesGet**](BusinessNamesApi.md#businessNamesGet) | **GET** /business-names | Retrieve a list of business names



## businessNamesGet

> [BusinessName] businessNamesGet(apiKey)

Retrieve a list of business names

Retrieve a list of business names 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.BusinessNamesApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.businessNamesGet(apiKey, (error, data, response) => {
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

[**[BusinessName]**](BusinessName.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

