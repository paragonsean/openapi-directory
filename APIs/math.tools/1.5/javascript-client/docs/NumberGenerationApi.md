# NumbersApi.NumberGenerationApi

All URIs are relative to *https://api.math.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numbersRandomGet**](NumberGenerationApi.md#numbersRandomGet) | **GET** /numbers/random | 



## numbersRandomGet

> numbersRandomGet(opts)



Generate random number(s)

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberGenerationApi();
let opts = {
  'min': 56, // Number | Minimum Number value in the range
  'max': 56, // Number | Maximum Number value
  'total': 56 // Number | Total number of random numbers to generate. Defaults to 1
};
apiInstance.numbersRandomGet(opts, (error, data, response) => {
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
 **min** | **Number**| Minimum Number value in the range | [optional] 
 **max** | **Number**| Maximum Number value | [optional] 
 **total** | **Number**| Total number of random numbers to generate. Defaults to 1 | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

