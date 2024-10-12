# Semantria.FeaturesApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFeatures**](FeaturesApi.md#getFeatures) | **GET** /features.{content_type} | Retrieve supported features



## getFeatures

> [Feature] getFeatures(contentType, opts)

Retrieve supported features

This method returns list of supported features per languages supported by Semantria API. Let the users know about API capabilities.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.FeaturesApi();
let contentType = "contentType_example"; // String | 
let opts = {
  'language': "language_example" // String | Filter features by specified language
};
apiInstance.getFeatures(contentType, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **language** | **String**| Filter features by specified language | [optional] 

### Return type

[**[Feature]**](Feature.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

