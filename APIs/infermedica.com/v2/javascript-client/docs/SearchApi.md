# InfermedicaApi.SearchApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMatchingObservations**](SearchApi.md#getMatchingObservations) | **GET** /search | Find observations matching given phrase



## getMatchingObservations

> [SearchResult] getMatchingObservations(phrase, opts)

Find observations matching given phrase

Returns list of observations matching the given phrase.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.SearchApi();
let phrase = "phrase_example"; // String | phrase to match
let opts = {
  'sex': "sex_example", // String | sex filter
  'ageValue': 18, // Number | age value
  'ageUnit': "year", // String | unit in which age value was provided
  'maxResults': 8, // Number | maximum number of results
  'type': ["null"] // [String] | type of results
};
apiInstance.getMatchingObservations(phrase, opts, (error, data, response) => {
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
 **maxResults** | **Number**| maximum number of results | [optional] [default to 8]
 **type** | [**[String]**](String.md)| type of results | [optional] 

### Return type

[**[SearchResult]**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

