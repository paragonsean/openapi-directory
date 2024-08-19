# NumbersApi.NumberChecksApi

All URIs are relative to *https://api.math.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numbersIsCubeGet**](NumberChecksApi.md#numbersIsCubeGet) | **GET** /numbers/is-cube | 
[**numbersIsPalindromeGet**](NumberChecksApi.md#numbersIsPalindromeGet) | **GET** /numbers/is-palindrome | 
[**numbersIsSquareGet**](NumberChecksApi.md#numbersIsSquareGet) | **GET** /numbers/is-square | 
[**numbersIsTriangleGet**](NumberChecksApi.md#numbersIsTriangleGet) | **GET** /numbers/is-triangle | 
[**numbersPrimeIsFermatPrimeGet_0**](NumberChecksApi.md#numbersPrimeIsFermatPrimeGet_0) | **GET** /numbers/prime/is-fermat-prime | 
[**numbersPrimeIsFibonacciPrimeGet_0**](NumberChecksApi.md#numbersPrimeIsFibonacciPrimeGet_0) | **GET** /numbers/prime/is-fibonacci-prime | 
[**numbersPrimeIsMersennePrimeGet_0**](NumberChecksApi.md#numbersPrimeIsMersennePrimeGet_0) | **GET** /numbers/prime/is-mersenne-prime | 
[**numbersPrimeIsPartitionPrimeGet_0**](NumberChecksApi.md#numbersPrimeIsPartitionPrimeGet_0) | **GET** /numbers/prime/is-partition-prime | 
[**numbersPrimeIsPellPrimeGet_0**](NumberChecksApi.md#numbersPrimeIsPellPrimeGet_0) | **GET** /numbers/prime/is-pell-prime | 
[**numbersPrimeIsPerfectGet_0**](NumberChecksApi.md#numbersPrimeIsPerfectGet_0) | **GET** /numbers/prime/is-perfect | 
[**numbersPrimeIsPrimeGet_0**](NumberChecksApi.md#numbersPrimeIsPrimeGet_0) | **GET** /numbers/prime/is-prime | 



## numbersIsCubeGet

> numbersIsCubeGet(opts)



Checks whether a given number is a cube number or not.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberChecksApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersIsCubeGet(opts, (error, data, response) => {
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
 **number** | **Number**| Number to check | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersIsPalindromeGet

> numbersIsPalindromeGet(opts)



Checks whether a given number is a palindrome number or not.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberChecksApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersIsPalindromeGet(opts, (error, data, response) => {
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
 **number** | **Number**| Number to check | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersIsSquareGet

> numbersIsSquareGet(opts)



Checks whether a given number is a square number or not.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberChecksApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersIsSquareGet(opts, (error, data, response) => {
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
 **number** | **Number**| Number to check | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersIsTriangleGet

> numbersIsTriangleGet(opts)



Checks whether a given number is a triangle number or not.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberChecksApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersIsTriangleGet(opts, (error, data, response) => {
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
 **number** | **Number**| Number to check | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersPrimeIsFermatPrimeGet_0

> numbersPrimeIsFermatPrimeGet_0(opts)



Checks whether a given number is a known fermat prime number or not.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberChecksApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsFermatPrimeGet_0(opts, (error, data, response) => {
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
 **number** | **Number**| Number to check | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersPrimeIsFibonacciPrimeGet_0

> numbersPrimeIsFibonacciPrimeGet_0(opts)



Checks whether a given number is a known fibonacci prime number or not.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberChecksApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsFibonacciPrimeGet_0(opts, (error, data, response) => {
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
 **number** | **Number**| Number to check | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersPrimeIsMersennePrimeGet_0

> numbersPrimeIsMersennePrimeGet_0(opts)



Checks whether a given number is a known mersenne prime number or not.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberChecksApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsMersennePrimeGet_0(opts, (error, data, response) => {
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
 **number** | **Number**| Number to check | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersPrimeIsPartitionPrimeGet_0

> numbersPrimeIsPartitionPrimeGet_0(opts)



Checks whether a given number is a known partition prime number or not.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberChecksApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsPartitionPrimeGet_0(opts, (error, data, response) => {
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
 **number** | **Number**| Number to check | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersPrimeIsPellPrimeGet_0

> numbersPrimeIsPellPrimeGet_0(opts)



Checks whether a given number is a known pell prime number or not.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberChecksApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsPellPrimeGet_0(opts, (error, data, response) => {
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
 **number** | **Number**| Number to check | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersPrimeIsPerfectGet_0

> numbersPrimeIsPerfectGet_0(opts)



Checks whether a given number is a perfect number or not.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberChecksApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsPerfectGet_0(opts, (error, data, response) => {
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
 **number** | **Number**| Number to check | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersPrimeIsPrimeGet_0

> numbersPrimeIsPrimeGet_0(opts)



Checks whether a given number is a known prime number or not.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.NumberChecksApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsPrimeGet_0(opts, (error, data, response) => {
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
 **number** | **Number**| Number to check | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

