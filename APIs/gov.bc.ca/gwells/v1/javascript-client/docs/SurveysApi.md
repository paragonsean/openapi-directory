# GroundwaterWellsAquifersAndRegistryApi.SurveysApi

All URIs are relative to *https://apps.nrs.gov.bc.ca/gwells/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**surveysList**](SurveysApi.md#surveysList) | **GET** /surveys/ | 



## surveysList

> [Survey] surveysList()



returns a list of active surveys

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.SurveysApi();
apiInstance.surveysList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Survey]**](Survey.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

