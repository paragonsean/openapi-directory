# NumbersApi.PrimeApi

All URIs are relative to *https://api.math.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numbersPrimeFactorsGet**](PrimeApi.md#numbersPrimeFactorsGet) | **GET** /numbers/prime/factors | 
[**numbersPrimeIsFermatPrimeGet**](PrimeApi.md#numbersPrimeIsFermatPrimeGet) | **GET** /numbers/prime/is-fermat-prime | 
[**numbersPrimeIsFibonacciPrimeGet**](PrimeApi.md#numbersPrimeIsFibonacciPrimeGet) | **GET** /numbers/prime/is-fibonacci-prime | 
[**numbersPrimeIsMersennePrimeGet**](PrimeApi.md#numbersPrimeIsMersennePrimeGet) | **GET** /numbers/prime/is-mersenne-prime | 
[**numbersPrimeIsPartitionPrimeGet**](PrimeApi.md#numbersPrimeIsPartitionPrimeGet) | **GET** /numbers/prime/is-partition-prime | 
[**numbersPrimeIsPellPrimeGet**](PrimeApi.md#numbersPrimeIsPellPrimeGet) | **GET** /numbers/prime/is-pell-prime | 
[**numbersPrimeIsPerfectGet**](PrimeApi.md#numbersPrimeIsPerfectGet) | **GET** /numbers/prime/is-perfect | 
[**numbersPrimeIsPrimeGet**](PrimeApi.md#numbersPrimeIsPrimeGet) | **GET** /numbers/prime/is-prime | 



## numbersPrimeFactorsGet

> numbersPrimeFactorsGet(opts)



Get the prime factors of a given number.

### Example

```javascript
import NumbersApi from 'numbers_api';
let defaultClient = NumbersApi.ApiClient.instance;
// Configure API key authorization: X-Mathtools-Api-Secret
let X-Mathtools-Api-Secret = defaultClient.authentications['X-Mathtools-Api-Secret'];
X-Mathtools-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Mathtools-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NumbersApi.PrimeApi();
let opts = {
  'number': 56 // Number | Number to get the factors
};
apiInstance.numbersPrimeFactorsGet(opts, (error, data, response) => {
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
 **number** | **Number**| Number to get the factors | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## numbersPrimeIsFermatPrimeGet

> numbersPrimeIsFermatPrimeGet(opts)



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

let apiInstance = new NumbersApi.PrimeApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsFermatPrimeGet(opts, (error, data, response) => {
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


## numbersPrimeIsFibonacciPrimeGet

> numbersPrimeIsFibonacciPrimeGet(opts)



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

let apiInstance = new NumbersApi.PrimeApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsFibonacciPrimeGet(opts, (error, data, response) => {
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


## numbersPrimeIsMersennePrimeGet

> numbersPrimeIsMersennePrimeGet(opts)



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

let apiInstance = new NumbersApi.PrimeApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsMersennePrimeGet(opts, (error, data, response) => {
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


## numbersPrimeIsPartitionPrimeGet

> numbersPrimeIsPartitionPrimeGet(opts)



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

let apiInstance = new NumbersApi.PrimeApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsPartitionPrimeGet(opts, (error, data, response) => {
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


## numbersPrimeIsPellPrimeGet

> numbersPrimeIsPellPrimeGet(opts)



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

let apiInstance = new NumbersApi.PrimeApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsPellPrimeGet(opts, (error, data, response) => {
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


## numbersPrimeIsPerfectGet

> numbersPrimeIsPerfectGet(opts)



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

let apiInstance = new NumbersApi.PrimeApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsPerfectGet(opts, (error, data, response) => {
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


## numbersPrimeIsPrimeGet

> numbersPrimeIsPrimeGet(opts)



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

let apiInstance = new NumbersApi.PrimeApi();
let opts = {
  'number': 56 // Number | Number to check
};
apiInstance.numbersPrimeIsPrimeGet(opts, (error, data, response) => {
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

