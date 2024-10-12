# BusinessRegistries.LicenseLifecycleStatesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classificationsLicenseLifecycleStatesGet**](LicenseLifecycleStatesApi.md#classificationsLicenseLifecycleStatesGet) | **GET** /classifications/license-lifecycle-states | Retrieve a list of license lifecycle states



## classificationsLicenseLifecycleStatesGet

> [LicenseLifecycleState] classificationsLicenseLifecycleStatesGet(apiKey)

Retrieve a list of license lifecycle states

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.LicenseLifecycleStatesApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.classificationsLicenseLifecycleStatesGet(apiKey, (error, data, response) => {
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

[**[LicenseLifecycleState]**](LicenseLifecycleState.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

