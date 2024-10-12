# EDistrictKeralaKerala.APIsApi

All URIs are relative to *https://apisetu.gov.in/edistrictkerala/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cmcer**](APIsApi.md#cmcer) | **POST** /cmcer/certificate | Community Certificate
[**cncer**](APIsApi.md#cncer) | **POST** /cncer/certificate | Conversion Certificate
[**ctcer**](APIsApi.md#ctcer) | **POST** /ctcer/certificate | Caste Certificate
[**dmcer**](APIsApi.md#dmcer) | **POST** /dmcer/certificate | Domicile Certificate
[**dpcer**](APIsApi.md#dpcer) | **POST** /dpcer/certificate | Dependency Certificate
[**dscer**](APIsApi.md#dscer) | **POST** /dscer/certificate | Destitute Certificate
[**fmcer**](APIsApi.md#fmcer) | **POST** /fmcer/certificate | Family Membership Certificate
[**idcer**](APIsApi.md#idcer) | **POST** /idcer/certificate | Identification Certificate
[**imcer**](APIsApi.md#imcer) | **POST** /imcer/certificate | Inter-Caste Marriage Certificate
[**incer**](APIsApi.md#incer) | **POST** /incer/certificate | Income Certificate
[**lfcer**](APIsApi.md#lfcer) | **POST** /lfcer/certificate | Life Certificate
[**lhcer**](APIsApi.md#lhcer) | **POST** /lhcer/certificate | Legal Heir Certificate
[**locer**](APIsApi.md#locer) | **POST** /locer/certificate | Location Certificate
[**mncer**](APIsApi.md#mncer) | **POST** /mncer/certificate | Minority Certificate
[**nrcer**](APIsApi.md#nrcer) | **POST** /nrcer/certificate | Non-Remarriage Certificate
[**ntcer**](APIsApi.md#ntcer) | **POST** /ntcer/certificate | Nativity Certificate
[**oscer**](APIsApi.md#oscer) | **POST** /oscer/certificate | One and the Same Certificate
[**pncer**](APIsApi.md#pncer) | **POST** /pncer/certificate | Possession and Non-Attachment Certificate
[**pscer**](APIsApi.md#pscer) | **POST** /pscer/certificate | Possession Certificate
[**rlcer**](APIsApi.md#rlcer) | **POST** /rlcer/certificate | Relationship Certificate
[**rscer**](APIsApi.md#rscer) | **POST** /rscer/certificate | Residence Certificate
[**slcer**](APIsApi.md#slcer) | **POST** /slcer/certificate | Solvency Certificate
[**vlcer**](APIsApi.md#vlcer) | **POST** /vlcer/certificate | Valuation Certificate
[**wwcer**](APIsApi.md#wwcer) | **POST** /wwcer/certificate | Widow-Widower Certificate



## cmcer

> cmcer(opts)

Community Certificate

API to verify Community Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.cmcer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## cncer

> cncer(opts)

Conversion Certificate

API to verify Conversion Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.cncer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## ctcer

> ctcer(opts)

Caste Certificate

API to verify Caste Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.ctcer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

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
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

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
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## dscer

> dscer(opts)

Destitute Certificate

API to verify Destitute Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.dscer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## fmcer

> fmcer(opts)

Family Membership Certificate

API to verify Family Membership Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.fmcer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## idcer

> idcer(opts)

Identification Certificate

API to verify Identification Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.idcer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## imcer

> imcer(opts)

Inter-Caste Marriage Certificate

API to verify Inter-Caste Marriage Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.imcer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

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
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## lfcer

> lfcer(opts)

Life Certificate

API to verify Life Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.lfcer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

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
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## locer

> locer(opts)

Location Certificate

API to verify Location Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.locer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## mncer

> mncer(opts)

Minority Certificate

API to verify Minority Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.mncer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## nrcer

> nrcer(opts)

Non-Remarriage Certificate

API to verify Non-Remarriage Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.nrcer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## ntcer

> ntcer(opts)

Nativity Certificate

API to verify Nativity Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.ntcer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## oscer

> oscer(opts)

One and the Same Certificate

API to verify One and the Same Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.oscer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## pncer

> pncer(opts)

Possession and Non-Attachment Certificate

API to verify Possession and Non-Attachment Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.pncer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

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
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## rlcer

> rlcer(opts)

Relationship Certificate

API to verify Relationship Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.rlcer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

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
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## slcer

> slcer(opts)

Solvency Certificate

API to verify Solvency Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.slcer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## vlcer

> vlcer(opts)

Valuation Certificate

API to verify Valuation Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.vlcer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## wwcer

> wwcer(opts)

Widow-Widower Certificate

API to verify Widow-Widower Certificate.

### Example

```javascript
import EDistrictKeralaKerala from 'e_district_kerala_kerala';
let defaultClient = EDistrictKeralaKerala.ApiClient.instance;
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

let apiInstance = new EDistrictKeralaKerala.APIsApi();
let opts = {
  'cmcerRequest': new EDistrictKeralaKerala.CmcerRequest() // CmcerRequest | Request format
};
apiInstance.wwcer(opts, (error, data, response) => {
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
 **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

