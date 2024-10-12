# DirectorateOfMunicipalAdministrationKarnataka.APIsApi

All URIs are relative to *https://apisetu.gov.in/municipaladmin/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kecer**](APIsApi.md#kecer) | **POST** /kecer/certificate | Khatha Extract / Certificate
[**tapcn**](APIsApi.md#tapcn) | **POST** /tapcn/certificate | New Tap Connection
[**tdlcs**](APIsApi.md#tdlcs) | **POST** /tdlcs/certificate | Trade License/ Certificate
[**ugdcn**](APIsApi.md#ugdcn) | **POST** /ugdcn/certificate | Jalanidhi - New UGD Connection



## kecer

> kecer(opts)

Khatha Extract / Certificate

API to verify Khatha Extract / Certificate.

### Example

```javascript
import DirectorateOfMunicipalAdministrationKarnataka from 'directorate_of_municipal_administration_karnataka';
let defaultClient = DirectorateOfMunicipalAdministrationKarnataka.ApiClient.instance;
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

let apiInstance = new DirectorateOfMunicipalAdministrationKarnataka.APIsApi();
let opts = {
  'kecerRequest': new DirectorateOfMunicipalAdministrationKarnataka.KecerRequest() // KecerRequest | Request format
};
apiInstance.kecer(opts, (error, data, response) => {
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
 **kecerRequest** | [**KecerRequest**](KecerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## tapcn

> tapcn(opts)

New Tap Connection

API to verify New Tap Connection.

### Example

```javascript
import DirectorateOfMunicipalAdministrationKarnataka from 'directorate_of_municipal_administration_karnataka';
let defaultClient = DirectorateOfMunicipalAdministrationKarnataka.ApiClient.instance;
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

let apiInstance = new DirectorateOfMunicipalAdministrationKarnataka.APIsApi();
let opts = {
  'tapcnRequest': new DirectorateOfMunicipalAdministrationKarnataka.TapcnRequest() // TapcnRequest | Request format
};
apiInstance.tapcn(opts, (error, data, response) => {
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
 **tapcnRequest** | [**TapcnRequest**](TapcnRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## tdlcs

> tdlcs(opts)

Trade License/ Certificate

API to verify Trade License/ Certificate.

### Example

```javascript
import DirectorateOfMunicipalAdministrationKarnataka from 'directorate_of_municipal_administration_karnataka';
let defaultClient = DirectorateOfMunicipalAdministrationKarnataka.ApiClient.instance;
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

let apiInstance = new DirectorateOfMunicipalAdministrationKarnataka.APIsApi();
let opts = {
  'tdlcsRequest': new DirectorateOfMunicipalAdministrationKarnataka.TdlcsRequest() // TdlcsRequest | Request format
};
apiInstance.tdlcs(opts, (error, data, response) => {
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
 **tdlcsRequest** | [**TdlcsRequest**](TdlcsRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## ugdcn

> ugdcn(opts)

Jalanidhi - New UGD Connection

API to verify Jalanidhi - New UGD Connection.

### Example

```javascript
import DirectorateOfMunicipalAdministrationKarnataka from 'directorate_of_municipal_administration_karnataka';
let defaultClient = DirectorateOfMunicipalAdministrationKarnataka.ApiClient.instance;
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

let apiInstance = new DirectorateOfMunicipalAdministrationKarnataka.APIsApi();
let opts = {
  'tapcnRequest': new DirectorateOfMunicipalAdministrationKarnataka.TapcnRequest() // TapcnRequest | Request format
};
apiInstance.ugdcn(opts, (error, data, response) => {
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
 **tapcnRequest** | [**TapcnRequest**](TapcnRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

