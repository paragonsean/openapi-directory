# NeutrinoApi.ECommerceApi

All URIs are relative to *https://neutrinoapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bINListDownload**](ECommerceApi.md#bINListDownload) | **GET** /bin-list-download | BIN List Download
[**bINLookup**](ECommerceApi.md#bINLookup) | **GET** /bin-lookup | BIN Lookup
[**convert**](ECommerceApi.md#convert) | **GET** /convert | Convert



## bINListDownload

> File bINListDownload(opts)

BIN List Download

Download our entire BIN database for direct use on your own systems

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.ECommerceApi();
let opts = {
  'includeIso3': false, // Boolean | Include ISO 3-letter country codes and ISO 3-letter currency codes in the data. These will be added to columns 10 and 11 respectively
  'include8digit': false // Boolean | Include 8-digit and higher BIN codes. This option includes all 6-digit BINs and all 8-digit and higher BINs (including some 9, 10 and 11 digit BINs where available)
};
apiInstance.bINListDownload(opts, (error, data, response) => {
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
 **includeIso3** | **Boolean**| Include ISO 3-letter country codes and ISO 3-letter currency codes in the data. These will be added to columns 10 and 11 respectively | [optional] [default to false]
 **include8digit** | **Boolean**| Include 8-digit and higher BIN codes. This option includes all 6-digit BINs and all 8-digit and higher BINs (including some 9, 10 and 11 digit BINs where available) | [optional] [default to false]

### Return type

**File**

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bINLookup

> BINLookupResponse bINLookup(binNumber, opts)

BIN Lookup

Perform a BIN (Bank Identification Number) or IIN (Issuer Identification Number) lookup

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.ECommerceApi();
let binNumber = "binNumber_example"; // String | The BIN or IIN number. This is the first 6, 8 or 10 digits of a card number, use 8 (or more) digits for the highest level of accuracy
let opts = {
  'customerIp': "customerIp_example" // String | Pass in the customers IP address and we will return some extra information about them
};
apiInstance.bINLookup(binNumber, opts, (error, data, response) => {
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
 **binNumber** | **String**| The BIN or IIN number. This is the first 6, 8 or 10 digits of a card number, use 8 (or more) digits for the highest level of accuracy | 
 **customerIp** | **String**| Pass in the customers IP address and we will return some extra information about them | [optional] 

### Return type

[**BINLookupResponse**](BINLookupResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## convert

> ConvertResponse convert(fromValue, fromType, toType)

Convert

A currency and unit conversion tool

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.ECommerceApi();
let fromValue = "fromValue_example"; // String | The value to convert from (e.g. 10.95)
let fromType = "fromType_example"; // String | The type of the value to convert from (e.g. USD)
let toType = "toType_example"; // String | The type to convert to (e.g. EUR)
apiInstance.convert(fromValue, fromType, toType, (error, data, response) => {
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
 **fromValue** | **String**| The value to convert from (e.g. 10.95) | 
 **fromType** | **String**| The type of the value to convert from (e.g. USD) | 
 **toType** | **String**| The type to convert to (e.g. EUR) | 

### Return type

[**ConvertResponse**](ConvertResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

