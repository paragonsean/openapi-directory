# EDistrictOdishaServicePlusOdisha.APIsApi

All URIs are relative to *https://apisetu.gov.in/edistrictodishasp/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**egcer**](APIsApi.md#egcer) | **POST** /egcer/certificate | Economically Backward In General Caste Certificate
[**ewcer**](APIsApi.md#ewcer) | **POST** /ewcer/certificate | Economically Weaker Section Certificate
[**incer**](APIsApi.md#incer) | **POST** /incer/certificate | Income Certificate
[**lhcer**](APIsApi.md#lhcer) | **POST** /lhcer/certificate | Legal Heir Certificate
[**obcer**](APIsApi.md#obcer) | **POST** /obcer/certificate | OBC Certificate
[**rscer**](APIsApi.md#rscer) | **POST** /rscer/certificate | Residence Certificate
[**shcer**](APIsApi.md#shcer) | **POST** /shcer/certificate | SC/ST  Certificate



## egcer

> egcer(opts)

Economically Backward In General Caste Certificate

API to verify Economically Backward In General Caste Certificate.

### Example

```javascript
import EDistrictOdishaServicePlusOdisha from 'e_district_odisha_service_plus_odisha';
let defaultClient = EDistrictOdishaServicePlusOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaServicePlusOdisha.APIsApi();
let opts = {
  'egcerRequest': new EDistrictOdishaServicePlusOdisha.EgcerRequest() // EgcerRequest | Request format
};
apiInstance.egcer(opts, (error, data, response) => {
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
 **egcerRequest** | [**EgcerRequest**](EgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## ewcer

> ewcer(opts)

Economically Weaker Section Certificate

API to verify Economically Weaker Section Certificate.

### Example

```javascript
import EDistrictOdishaServicePlusOdisha from 'e_district_odisha_service_plus_odisha';
let defaultClient = EDistrictOdishaServicePlusOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaServicePlusOdisha.APIsApi();
let opts = {
  'egcerRequest': new EDistrictOdishaServicePlusOdisha.EgcerRequest() // EgcerRequest | Request format
};
apiInstance.ewcer(opts, (error, data, response) => {
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
 **egcerRequest** | [**EgcerRequest**](EgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## incer

> incer(opts)

Income Certificate

API to verify Income Certificate.

### Example

```javascript
import EDistrictOdishaServicePlusOdisha from 'e_district_odisha_service_plus_odisha';
let defaultClient = EDistrictOdishaServicePlusOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaServicePlusOdisha.APIsApi();
let opts = {
  'egcerRequest': new EDistrictOdishaServicePlusOdisha.EgcerRequest() // EgcerRequest | Request format
};
apiInstance.incer(opts, (error, data, response) => {
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
 **egcerRequest** | [**EgcerRequest**](EgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## lhcer

> lhcer(opts)

Legal Heir Certificate

API to verify Legal Heir Certificate.

### Example

```javascript
import EDistrictOdishaServicePlusOdisha from 'e_district_odisha_service_plus_odisha';
let defaultClient = EDistrictOdishaServicePlusOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaServicePlusOdisha.APIsApi();
let opts = {
  'egcerRequest': new EDistrictOdishaServicePlusOdisha.EgcerRequest() // EgcerRequest | Request format
};
apiInstance.lhcer(opts, (error, data, response) => {
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
 **egcerRequest** | [**EgcerRequest**](EgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## obcer

> obcer(opts)

OBC Certificate

API to verify OBC Certificate.

### Example

```javascript
import EDistrictOdishaServicePlusOdisha from 'e_district_odisha_service_plus_odisha';
let defaultClient = EDistrictOdishaServicePlusOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaServicePlusOdisha.APIsApi();
let opts = {
  'egcerRequest': new EDistrictOdishaServicePlusOdisha.EgcerRequest() // EgcerRequest | Request format
};
apiInstance.obcer(opts, (error, data, response) => {
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
 **egcerRequest** | [**EgcerRequest**](EgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## rscer

> rscer(opts)

Residence Certificate

API to verify Residence Certificate.

### Example

```javascript
import EDistrictOdishaServicePlusOdisha from 'e_district_odisha_service_plus_odisha';
let defaultClient = EDistrictOdishaServicePlusOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaServicePlusOdisha.APIsApi();
let opts = {
  'egcerRequest': new EDistrictOdishaServicePlusOdisha.EgcerRequest() // EgcerRequest | Request format
};
apiInstance.rscer(opts, (error, data, response) => {
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
 **egcerRequest** | [**EgcerRequest**](EgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## shcer

> shcer(opts)

SC/ST  Certificate

API to verify SC/ST  Certificate.

### Example

```javascript
import EDistrictOdishaServicePlusOdisha from 'e_district_odisha_service_plus_odisha';
let defaultClient = EDistrictOdishaServicePlusOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaServicePlusOdisha.APIsApi();
let opts = {
  'egcerRequest': new EDistrictOdishaServicePlusOdisha.EgcerRequest() // EgcerRequest | Request format
};
apiInstance.shcer(opts, (error, data, response) => {
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
 **egcerRequest** | [**EgcerRequest**](EgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

