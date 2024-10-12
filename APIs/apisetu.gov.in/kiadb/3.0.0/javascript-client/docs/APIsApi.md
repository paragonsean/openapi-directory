# KarnatakaIndustrialAreasDevelopmentBoardKarnataka.APIsApi

All URIs are relative to *https://apisetu.gov.in/kiadb/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alltr**](APIsApi.md#alltr) | **POST** /alltr/certificate | Allotment Letter
[**bknoc**](APIsApi.md#bknoc) | **POST** /bknoc/certificate | NOC For Banks
[**bpcer**](APIsApi.md#bpcer) | **POST** /bpcer/certificate | Building Plan
[**cfltr**](APIsApi.md#cfltr) | **POST** /cfltr/certificate | Confirmatory Letter
[**lcsag**](APIsApi.md#lcsag) | **POST** /lcsag/certificate | Lease cum Sale Agreement
[**pscer**](APIsApi.md#pscer) | **POST** /pscer/certificate | Possession Certificate
[**psnoc**](APIsApi.md#psnoc) | **POST** /psnoc/certificate | NOC for New Power Supply
[**wtrbl**](APIsApi.md#wtrbl) | **POST** /wtrbl/certificate | Water Bill/ Connection



## alltr

> alltr(opts)

Allotment Letter

API to verify Allotment Letter.

### Example

```javascript
import KarnatakaIndustrialAreasDevelopmentBoardKarnataka from 'karnataka_industrial_areas_development_board_karnataka';
let defaultClient = KarnatakaIndustrialAreasDevelopmentBoardKarnataka.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.APIsApi();
let opts = {
  'alltrRequest': new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.AlltrRequest() // AlltrRequest | Request format
};
apiInstance.alltr(opts, (error, data, response) => {
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
 **alltrRequest** | [**AlltrRequest**](AlltrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## bknoc

> bknoc(opts)

NOC For Banks

API to verify NOC For Banks.

### Example

```javascript
import KarnatakaIndustrialAreasDevelopmentBoardKarnataka from 'karnataka_industrial_areas_development_board_karnataka';
let defaultClient = KarnatakaIndustrialAreasDevelopmentBoardKarnataka.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.APIsApi();
let opts = {
  'alltrRequest': new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.AlltrRequest() // AlltrRequest | Request format
};
apiInstance.bknoc(opts, (error, data, response) => {
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
 **alltrRequest** | [**AlltrRequest**](AlltrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## bpcer

> bpcer(opts)

Building Plan

API to verify Building Plan.

### Example

```javascript
import KarnatakaIndustrialAreasDevelopmentBoardKarnataka from 'karnataka_industrial_areas_development_board_karnataka';
let defaultClient = KarnatakaIndustrialAreasDevelopmentBoardKarnataka.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.APIsApi();
let opts = {
  'alltrRequest': new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.AlltrRequest() // AlltrRequest | Request format
};
apiInstance.bpcer(opts, (error, data, response) => {
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
 **alltrRequest** | [**AlltrRequest**](AlltrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## cfltr

> cfltr(opts)

Confirmatory Letter

API to verify Confirmatory Letter.

### Example

```javascript
import KarnatakaIndustrialAreasDevelopmentBoardKarnataka from 'karnataka_industrial_areas_development_board_karnataka';
let defaultClient = KarnatakaIndustrialAreasDevelopmentBoardKarnataka.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.APIsApi();
let opts = {
  'alltrRequest': new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.AlltrRequest() // AlltrRequest | Request format
};
apiInstance.cfltr(opts, (error, data, response) => {
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
 **alltrRequest** | [**AlltrRequest**](AlltrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## lcsag

> lcsag(opts)

Lease cum Sale Agreement

API to verify Lease cum Sale Agreement.

### Example

```javascript
import KarnatakaIndustrialAreasDevelopmentBoardKarnataka from 'karnataka_industrial_areas_development_board_karnataka';
let defaultClient = KarnatakaIndustrialAreasDevelopmentBoardKarnataka.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.APIsApi();
let opts = {
  'alltrRequest': new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.AlltrRequest() // AlltrRequest | Request format
};
apiInstance.lcsag(opts, (error, data, response) => {
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
 **alltrRequest** | [**AlltrRequest**](AlltrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## pscer

> pscer(opts)

Possession Certificate

API to verify Possession Certificate.

### Example

```javascript
import KarnatakaIndustrialAreasDevelopmentBoardKarnataka from 'karnataka_industrial_areas_development_board_karnataka';
let defaultClient = KarnatakaIndustrialAreasDevelopmentBoardKarnataka.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.APIsApi();
let opts = {
  'alltrRequest': new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.AlltrRequest() // AlltrRequest | Request format
};
apiInstance.pscer(opts, (error, data, response) => {
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
 **alltrRequest** | [**AlltrRequest**](AlltrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## psnoc

> psnoc(opts)

NOC for New Power Supply

API to verify NOC for New Power Supply.

### Example

```javascript
import KarnatakaIndustrialAreasDevelopmentBoardKarnataka from 'karnataka_industrial_areas_development_board_karnataka';
let defaultClient = KarnatakaIndustrialAreasDevelopmentBoardKarnataka.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.APIsApi();
let opts = {
  'alltrRequest': new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.AlltrRequest() // AlltrRequest | Request format
};
apiInstance.psnoc(opts, (error, data, response) => {
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
 **alltrRequest** | [**AlltrRequest**](AlltrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## wtrbl

> wtrbl(opts)

Water Bill/ Connection

API to verify Water Bill/ Connection.

### Example

```javascript
import KarnatakaIndustrialAreasDevelopmentBoardKarnataka from 'karnataka_industrial_areas_development_board_karnataka';
let defaultClient = KarnatakaIndustrialAreasDevelopmentBoardKarnataka.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.APIsApi();
let opts = {
  'alltrRequest': new KarnatakaIndustrialAreasDevelopmentBoardKarnataka.AlltrRequest() // AlltrRequest | Request format
};
apiInstance.wtrbl(opts, (error, data, response) => {
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
 **alltrRequest** | [**AlltrRequest**](AlltrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

