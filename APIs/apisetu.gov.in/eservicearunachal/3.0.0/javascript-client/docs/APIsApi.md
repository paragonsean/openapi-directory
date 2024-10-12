# EServiceEDistrictArunachalPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/eservicearunachal/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chcer**](APIsApi.md#chcer) | **POST** /chcer/certificate | Character Certificate
[**dmcer**](APIsApi.md#dmcer) | **POST** /dmcer/certificate | Domicile Certificate
[**dpcer**](APIsApi.md#dpcer) | **POST** /dpcer/certificate | Dependency Certificate
[**incer**](APIsApi.md#incer) | **POST** /incer/certificate | Income Certificate
[**rscer**](APIsApi.md#rscer) | **POST** /rscer/certificate | Residence Certificate
[**shcer**](APIsApi.md#shcer) | **POST** /shcer/certificate | SC/ST  Certificate



## chcer

> chcer(opts)

Character Certificate

API to verify Character Certificate.

### Example

```javascript
import EServiceEDistrictArunachalPradesh from 'e_service__e_district_arunachal_pradesh';
let defaultClient = EServiceEDistrictArunachalPradesh.ApiClient.instance;
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

let apiInstance = new EServiceEDistrictArunachalPradesh.APIsApi();
let opts = {
  'chcerRequest': new EServiceEDistrictArunachalPradesh.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.chcer(opts, (error, data, response) => {
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
 **chcerRequest** | [**ChcerRequest**](ChcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## dmcer

> dmcer(opts)

Domicile Certificate

API to verify Domicile Certificate.

### Example

```javascript
import EServiceEDistrictArunachalPradesh from 'e_service__e_district_arunachal_pradesh';
let defaultClient = EServiceEDistrictArunachalPradesh.ApiClient.instance;
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

let apiInstance = new EServiceEDistrictArunachalPradesh.APIsApi();
let opts = {
  'chcerRequest': new EServiceEDistrictArunachalPradesh.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.dmcer(opts, (error, data, response) => {
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
 **chcerRequest** | [**ChcerRequest**](ChcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## dpcer

> dpcer(opts)

Dependency Certificate

API to verify Dependency Certificate.

### Example

```javascript
import EServiceEDistrictArunachalPradesh from 'e_service__e_district_arunachal_pradesh';
let defaultClient = EServiceEDistrictArunachalPradesh.ApiClient.instance;
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

let apiInstance = new EServiceEDistrictArunachalPradesh.APIsApi();
let opts = {
  'chcerRequest': new EServiceEDistrictArunachalPradesh.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.dpcer(opts, (error, data, response) => {
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
 **chcerRequest** | [**ChcerRequest**](ChcerRequest.md)| Request format | [optional] 

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
import EServiceEDistrictArunachalPradesh from 'e_service__e_district_arunachal_pradesh';
let defaultClient = EServiceEDistrictArunachalPradesh.ApiClient.instance;
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

let apiInstance = new EServiceEDistrictArunachalPradesh.APIsApi();
let opts = {
  'chcerRequest': new EServiceEDistrictArunachalPradesh.ChcerRequest() // ChcerRequest | Request format
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
 **chcerRequest** | [**ChcerRequest**](ChcerRequest.md)| Request format | [optional] 

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
import EServiceEDistrictArunachalPradesh from 'e_service__e_district_arunachal_pradesh';
let defaultClient = EServiceEDistrictArunachalPradesh.ApiClient.instance;
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

let apiInstance = new EServiceEDistrictArunachalPradesh.APIsApi();
let opts = {
  'chcerRequest': new EServiceEDistrictArunachalPradesh.ChcerRequest() // ChcerRequest | Request format
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
 **chcerRequest** | [**ChcerRequest**](ChcerRequest.md)| Request format | [optional] 

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
import EServiceEDistrictArunachalPradesh from 'e_service__e_district_arunachal_pradesh';
let defaultClient = EServiceEDistrictArunachalPradesh.ApiClient.instance;
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

let apiInstance = new EServiceEDistrictArunachalPradesh.APIsApi();
let opts = {
  'chcerRequest': new EServiceEDistrictArunachalPradesh.ChcerRequest() // ChcerRequest | Request format
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
 **chcerRequest** | [**ChcerRequest**](ChcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

