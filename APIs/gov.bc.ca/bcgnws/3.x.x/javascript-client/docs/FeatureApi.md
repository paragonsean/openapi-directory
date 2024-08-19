# BcGeographicalNamesWebServiceRestApi.FeatureApi

All URIs are relative to *https://apps.gov.bc.ca/pub/bcgnws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**featuresFeatureIdGet**](FeatureApi.md#featuresFeatureIdGet) | **GET** /features/{featureId} | Get a feature by its featureId



## featuresFeatureIdGet

> featuresFeatureIdGet(featureId)

Get a feature by its featureId

Get information about the geographical feature with the specified featureId.

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.FeatureApi();
let featureId = 8879; // Number | The unique identifier for a feature
apiInstance.featuresFeatureIdGet(featureId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featureId** | **Number**| The unique identifier for a feature | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

