# PunjabStateEGovernanceSocietyPunjab.APIsApi

All URIs are relative to *https://apisetu.gov.in/edistrictpb/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**btcer**](APIsApi.md#btcer) | **POST** /btcer/certificate | Birth Certificate
[**dtcer**](APIsApi.md#dtcer) | **POST** /dtcer/certificate | Death Certificate
[**ewcer**](APIsApi.md#ewcer) | **POST** /ewcer/certificate | Economically Weaker Section Certificate
[**obcer**](APIsApi.md#obcer) | **POST** /obcer/certificate | OBC Certificate
[**racer**](APIsApi.md#racer) | **POST** /racer/certificate | Rural Area Certificate
[**rscer**](APIsApi.md#rscer) | **POST** /rscer/certificate | Residence Certificate
[**shcer**](APIsApi.md#shcer) | **POST** /shcer/certificate | SC/ST  Certificate



## btcer

> btcer(opts)

Birth Certificate

API to verify Birth Certificate.

### Example

```javascript
import PunjabStateEGovernanceSocietyPunjab from 'punjab_state_e_governance_society_punjab';
let defaultClient = PunjabStateEGovernanceSocietyPunjab.ApiClient.instance;
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

let apiInstance = new PunjabStateEGovernanceSocietyPunjab.APIsApi();
let opts = {
  'btcerRequest': new PunjabStateEGovernanceSocietyPunjab.BtcerRequest() // BtcerRequest | Request format
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
import PunjabStateEGovernanceSocietyPunjab from 'punjab_state_e_governance_society_punjab';
let defaultClient = PunjabStateEGovernanceSocietyPunjab.ApiClient.instance;
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

let apiInstance = new PunjabStateEGovernanceSocietyPunjab.APIsApi();
let opts = {
  'btcerRequest': new PunjabStateEGovernanceSocietyPunjab.BtcerRequest() // BtcerRequest | Request format
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
 **btcerRequest** | [**BtcerRequest**](BtcerRequest.md)| Request format | [optional] 

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
import PunjabStateEGovernanceSocietyPunjab from 'punjab_state_e_governance_society_punjab';
let defaultClient = PunjabStateEGovernanceSocietyPunjab.ApiClient.instance;
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

let apiInstance = new PunjabStateEGovernanceSocietyPunjab.APIsApi();
let opts = {
  'ewcerRequest': new PunjabStateEGovernanceSocietyPunjab.EwcerRequest() // EwcerRequest | Request format
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
 **ewcerRequest** | [**EwcerRequest**](EwcerRequest.md)| Request format | [optional] 

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
import PunjabStateEGovernanceSocietyPunjab from 'punjab_state_e_governance_society_punjab';
let defaultClient = PunjabStateEGovernanceSocietyPunjab.ApiClient.instance;
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

let apiInstance = new PunjabStateEGovernanceSocietyPunjab.APIsApi();
let opts = {
  'obcerRequest': new PunjabStateEGovernanceSocietyPunjab.ObcerRequest() // ObcerRequest | Request format
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
 **obcerRequest** | [**ObcerRequest**](ObcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## racer

> racer(opts)

Rural Area Certificate

API to verify Rural Area Certificate.

### Example

```javascript
import PunjabStateEGovernanceSocietyPunjab from 'punjab_state_e_governance_society_punjab';
let defaultClient = PunjabStateEGovernanceSocietyPunjab.ApiClient.instance;
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

let apiInstance = new PunjabStateEGovernanceSocietyPunjab.APIsApi();
let opts = {
  'ewcerRequest': new PunjabStateEGovernanceSocietyPunjab.EwcerRequest() // EwcerRequest | Request format
};
apiInstance.racer(opts, (error, data, response) => {
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
 **ewcerRequest** | [**EwcerRequest**](EwcerRequest.md)| Request format | [optional] 

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
import PunjabStateEGovernanceSocietyPunjab from 'punjab_state_e_governance_society_punjab';
let defaultClient = PunjabStateEGovernanceSocietyPunjab.ApiClient.instance;
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

let apiInstance = new PunjabStateEGovernanceSocietyPunjab.APIsApi();
let opts = {
  'rscerRequest': new PunjabStateEGovernanceSocietyPunjab.RscerRequest() // RscerRequest | Request format
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
 **rscerRequest** | [**RscerRequest**](RscerRequest.md)| Request format | [optional] 

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
import PunjabStateEGovernanceSocietyPunjab from 'punjab_state_e_governance_society_punjab';
let defaultClient = PunjabStateEGovernanceSocietyPunjab.ApiClient.instance;
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

let apiInstance = new PunjabStateEGovernanceSocietyPunjab.APIsApi();
let opts = {
  'shcerRequest': new PunjabStateEGovernanceSocietyPunjab.ShcerRequest() // ShcerRequest | Request format
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
 **shcerRequest** | [**ShcerRequest**](ShcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

