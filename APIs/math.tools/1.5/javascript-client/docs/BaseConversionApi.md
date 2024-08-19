# NumbersApi.BaseConversionApi

All URIs are relative to *https://api.math.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numbersBaseBinaryGet**](BaseConversionApi.md#numbersBaseBinaryGet) | **GET** /numbers/base/binary | 
[**numbersBaseGet**](BaseConversionApi.md#numbersBaseGet) | **GET** /numbers/base | 
[**numbersBaseHexGet**](BaseConversionApi.md#numbersBaseHexGet) | **GET** /numbers/base/hex | 
[**numbersBaseOctalGet**](BaseConversionApi.md#numbersBaseOctalGet) | **GET** /numbers/base/octal | 



## numbersBaseBinaryGet

> numbersBaseBinaryGet(number, opts)



Convert a given number to binary

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.BaseConversionApi();
let number = 56; // Number | Number to convert to binary
let opts = {
  'from': 56 // Number | Base of the supplied number (Optional base 10 assumed by default)
};
apiInstance.numbersBaseBinaryGet(number, opts, (error, data, response) => {
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
 **number** | **Number**| Number to convert to binary | 
 **from** | **Number**| Base of the supplied number (Optional base 10 assumed by default) | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersBaseGet

> numbersBaseGet(number, to, opts)



Convert a given number from one base to another base

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.BaseConversionApi();
let number = 56; // Number | Number to convert to the target base
let to = 56; // Number | Target base to convert to
let opts = {
  'from': 56 // Number | Base of the supplied number (Optional base 10 assumed by default)
};
apiInstance.numbersBaseGet(number, to, opts, (error, data, response) => {
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
 **number** | **Number**| Number to convert to the target base | 
 **to** | **Number**| Target base to convert to | 
 **from** | **Number**| Base of the supplied number (Optional base 10 assumed by default) | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersBaseHexGet

> numbersBaseHexGet(number, opts)



Convert a given number to hexadecimal

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.BaseConversionApi();
let number = 56; // Number | Number to convert to hex
let opts = {
  'from': 56 // Number | Base of the supplied number (Optional base 10 assumed by default)
};
apiInstance.numbersBaseHexGet(number, opts, (error, data, response) => {
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
 **number** | **Number**| Number to convert to hex | 
 **from** | **Number**| Base of the supplied number (Optional base 10 assumed by default) | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersBaseOctalGet

> numbersBaseOctalGet(number, opts)



Convert a given number to octal

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.BaseConversionApi();
let number = 56; // Number | Number to convert to octal
let opts = {
  'from': 56 // Number | Base of the supplied number (Optional base 10 assumed by default)
};
apiInstance.numbersBaseOctalGet(number, opts, (error, data, response) => {
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
 **number** | **Number**| Number to convert to octal | 
 **from** | **Number**| Base of the supplied number (Optional base 10 assumed by default) | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

