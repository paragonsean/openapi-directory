# NumbersApi.NumberFactsApi

All URIs are relative to *https://api.math.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numbersFactGet**](NumberFactsApi.md#numbersFactGet) | **GET** /numbers/fact | 



## numbersFactGet

> numbersFactGet(number)



Get a random fact about a number

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberFactsApi();
let number = 56; // Number | Number value
apiInstance.numbersFactGet(number, (error, data, response) => {
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
 **number** | **Number**| Number value | 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

