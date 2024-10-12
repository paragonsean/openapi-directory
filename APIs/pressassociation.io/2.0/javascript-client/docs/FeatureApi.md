# TvApi.FeatureApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFeature**](FeatureApi.md#getFeature) | **GET** /feature/{featureId} | Feature Detail
[**listFeatureTypes**](FeatureApi.md#listFeatureTypes) | **GET** /feature-type | Feature Type Collection
[**listFeatures**](FeatureApi.md#listFeatures) | **GET** /feature | Feature Collection



## getFeature

> Object getFeature(featureId)

Feature Detail

Return the content of the selected feature.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.FeatureApi();
let featureId = "featureId_example"; // String | The identifier for the selected feature.
apiInstance.getFeature(featureId, (error, data, response) => {
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
 **featureId** | **String**| The identifier for the selected feature. | 

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFeatureTypes

> Object listFeatureTypes()

Feature Type Collection

Return a collection of Feature Types.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.FeatureApi();
apiInstance.listFeatureTypes((error, data, response) => {
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

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFeatures

> Object listFeatures(opts)

Feature Collection

Return a collection of Feature.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.FeatureApi();
let opts = {
  'type': "'netflix-monthly'", // String | The namespace of the feature type.
  'date': "'2018-09-15'", // String | Date of the collection of feature items.
  'start': "'2018-09-15'", // String | Start date for a range of features.
  'end': "'2018-10-15'" // String | End date for a range of features.
};
apiInstance.listFeatures(opts, (error, data, response) => {
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
 **type** | **String**| The namespace of the feature type. | [optional] [default to &#39;netflix-monthly&#39;]
 **date** | **String**| Date of the collection of feature items. | [optional] [default to &#39;2018-09-15&#39;]
 **start** | **String**| Start date for a range of features. | [optional] [default to &#39;2018-09-15&#39;]
 **end** | **String**| End date for a range of features. | [optional] [default to &#39;2018-10-15&#39;]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

