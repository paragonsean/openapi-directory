# InfermedicaApi.LookupApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMatchingObservation**](LookupApi.md#getMatchingObservation) | **GET** /lookup | Find observation matching given phrase



## getMatchingObservation

> SearchResult getMatchingObservation(phrase, opts)

Find observation matching given phrase

Returns a single observation matching given phrase.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.LookupApi();
let phrase = "phrase_example"; // String | phrase to match
let opts = {
  'sex': "sex_example", // String | sex filter
  'ageValue': 18, // Number | age value
  'ageUnit': "year" // String | unit in which age value was provided
};
apiInstance.getMatchingObservation(phrase, opts, (error, data, response) => {
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
 **phrase** | **String**| phrase to match | 
 **sex** | **String**| sex filter | [optional] 
 **ageValue** | **Number**| age value | [optional] 
 **ageUnit** | **String**| unit in which age value was provided | [optional] [default to &#39;year&#39;]

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

