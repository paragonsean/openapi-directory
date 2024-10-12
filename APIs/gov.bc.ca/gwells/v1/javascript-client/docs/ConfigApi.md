# GroundwaterWellsAquifersAndRegistryApi.ConfigApi

All URIs are relative to *https://apps.nrs.gov.bc.ca/gwells/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configList**](ConfigApi.md#configList) | **GET** /config | 



## configList

> configList()



serves general configuration

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.ConfigApi();
apiInstance.configList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

