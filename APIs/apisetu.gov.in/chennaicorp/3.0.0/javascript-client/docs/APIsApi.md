# GreaterChennaiCorporationTamilNadu.APIsApi

All URIs are relative to *https://apisetu.gov.in/chennaicorp/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**btcer**](APIsApi.md#btcer) | **POST** /btcer/certificate | Birth Certificate
[**dtcer**](APIsApi.md#dtcer) | **POST** /dtcer/certificate | Death Certificate



## btcer

> btcer(opts)

Birth Certificate

API to verify Birth Certificate.

### Example

```javascript
import GreaterChennaiCorporationTamilNadu from 'greater_chennai_corporation_tamil_nadu';
let defaultClient = GreaterChennaiCorporationTamilNadu.ApiClient.instance;
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

let apiInstance = new GreaterChennaiCorporationTamilNadu.APIsApi();
let opts = {
  'btcerRequest': new GreaterChennaiCorporationTamilNadu.BtcerRequest() // BtcerRequest | Request format
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
import GreaterChennaiCorporationTamilNadu from 'greater_chennai_corporation_tamil_nadu';
let defaultClient = GreaterChennaiCorporationTamilNadu.ApiClient.instance;
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

let apiInstance = new GreaterChennaiCorporationTamilNadu.APIsApi();
let opts = {
  'dtcerRequest': new GreaterChennaiCorporationTamilNadu.DtcerRequest() // DtcerRequest | Request format
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

