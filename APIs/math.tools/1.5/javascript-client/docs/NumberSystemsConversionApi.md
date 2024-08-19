# NumbersApi.NumberSystemsConversionApi

All URIs are relative to *https://api.math.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numbersNumeralChineseGet**](NumberSystemsConversionApi.md#numbersNumeralChineseGet) | **GET** /numbers/numeral/chinese | 
[**numbersNumeralEgyptianGet**](NumberSystemsConversionApi.md#numbersNumeralEgyptianGet) | **GET** /numbers/numeral/egyptian | 
[**numbersNumeralRomanGet**](NumberSystemsConversionApi.md#numbersNumeralRomanGet) | **GET** /numbers/numeral/roman | 



## numbersNumeralChineseGet

> numbersNumeralChineseGet(opts)



Convert base 10 representation of a given number to chinese numeral.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberSystemsConversionApi();
let opts = {
  'number': 56 // Number | Number to convert
};
apiInstance.numbersNumeralChineseGet(opts, (error, data, response) => {
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
 **number** | **Number**| Number to convert | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersNumeralEgyptianGet

> numbersNumeralEgyptianGet(opts)



Convert base 10 representation of a given number to egyptian numeral.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberSystemsConversionApi();
let opts = {
  'number': 56 // Number | Number to convert
};
apiInstance.numbersNumeralEgyptianGet(opts, (error, data, response) => {
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
 **number** | **Number**| Number to convert | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersNumeralRomanGet

> numbersNumeralRomanGet(opts)



Convert base 10 representation of a given number to roman numeral.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberSystemsConversionApi();
let opts = {
  'number': 56 // Number | Number to convert
};
apiInstance.numbersNumeralRomanGet(opts, (error, data, response) => {
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
 **number** | **Number**| Number to convert | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

