# DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan.APIsApi

All URIs are relative to *https://apisetu.gov.in/statisticsrajasthan/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**btcer**](APIsApi.md#btcer) | **POST** /btcer/certificate | Birth Certificate
[**dtcer**](APIsApi.md#dtcer) | **POST** /dtcer/certificate | Death Certificate
[**rmcer**](APIsApi.md#rmcer) | **POST** /rmcer/certificate | Marriage Certificate



## btcer

> btcer(opts)

Birth Certificate

API to verify Birth Certificate.

### Example

```javascript
import DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan from 'directorate_of_economics_and_statistics_cum_chief_registrar_rajasthan_rajasthan';
let defaultClient = DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan.ApiClient.instance;
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

let apiInstance = new DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan.APIsApi();
let opts = {
  'btcerRequest': new DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan.BtcerRequest() // BtcerRequest | Request format
};
apiInstance.btcer(opts, (error, data, response) => {
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
 **btcerRequest** | [**BtcerRequest**](BtcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## dtcer

> dtcer(opts)

Death Certificate

API to verify Death Certificate.

### Example

```javascript
import DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan from 'directorate_of_economics_and_statistics_cum_chief_registrar_rajasthan_rajasthan';
let defaultClient = DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan.ApiClient.instance;
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

let apiInstance = new DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan.APIsApi();
let opts = {
  'dtcerRequest': new DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan.DtcerRequest() // DtcerRequest | Request format
};
apiInstance.dtcer(opts, (error, data, response) => {
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
 **dtcerRequest** | [**DtcerRequest**](DtcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## rmcer

> rmcer(opts)

Marriage Certificate

API to verify Marriage Certificate.

### Example

```javascript
import DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan from 'directorate_of_economics_and_statistics_cum_chief_registrar_rajasthan_rajasthan';
let defaultClient = DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan.ApiClient.instance;
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

let apiInstance = new DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan.APIsApi();
let opts = {
  'rmcerRequest': new DirectorateOfEconomicsAndStatisticsCumChiefRegistrarRajasthanRajasthan.RmcerRequest() // RmcerRequest | Request format
};
apiInstance.rmcer(opts, (error, data, response) => {
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
 **rmcerRequest** | [**RmcerRequest**](RmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

