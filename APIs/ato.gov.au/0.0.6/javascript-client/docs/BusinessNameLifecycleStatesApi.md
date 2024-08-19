# BusinessRegistries.BusinessNameLifecycleStatesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classificationsBusinessNameLifecycleStatesGet**](BusinessNameLifecycleStatesApi.md#classificationsBusinessNameLifecycleStatesGet) | **GET** /classifications/business-name-lifecycle-states | Retrieve a list of business name lifecycle states



## classificationsBusinessNameLifecycleStatesGet

> [BusinessNameLifecycleState] classificationsBusinessNameLifecycleStatesGet(apiKey)

Retrieve a list of business name lifecycle states

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.BusinessNameLifecycleStatesApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.classificationsBusinessNameLifecycleStatesGet(apiKey, (error, data, response) => {
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

[**[BusinessNameLifecycleState]**](BusinessNameLifecycleState.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

