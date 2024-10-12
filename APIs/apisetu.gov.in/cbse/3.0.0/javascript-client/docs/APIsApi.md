# CentralBoardOfSecondaryEducation.APIsApi

All URIs are relative to *https://apisetu.gov.in/cbse/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hpcer**](APIsApi.md#hpcer) | **POST** /hpcer/certificate | Class XII Passing Certificate
[**hscer**](APIsApi.md#hscer) | **POST** /hscer/certificate | Class XII Marksheet
[**hsmgr**](APIsApi.md#hsmgr) | **POST** /hsmgr/certificate | Class XII Migration Certificate
[**nchsc**](APIsApi.md#nchsc) | **POST** /nchsc/certificate | NCHMCT Skill Certificate (X)
[**nctsc**](APIsApi.md#nctsc) | **POST** /nctsc/certificate | NCHMCT Skill Certificate (XII)
[**nsesc**](APIsApi.md#nsesc) | **POST** /nsesc/certificate | NSE Skill Certificate (X)
[**nstsc**](APIsApi.md#nstsc) | **POST** /nstsc/certificate | NSE Skill Certificate (XII)
[**ntltr**](APIsApi.md#ntltr) | **POST** /ntltr/certificate | NEET Rank Letter
[**ntmks**](APIsApi.md#ntmks) | **POST** /ntmks/certificate | NEET Marksheet
[**skhsc**](APIsApi.md#skhsc) | **POST** /skhsc/certificate | Skill Certificate (X)
[**sktsc**](APIsApi.md#sktsc) | **POST** /sktsc/certificate | Skill Certificate (XII)
[**spcer**](APIsApi.md#spcer) | **POST** /spcer/certificate | Class X Passing Certificate
[**sscer**](APIsApi.md#sscer) | **POST** /sscer/certificate | Class X Marksheet
[**ssmgr**](APIsApi.md#ssmgr) | **POST** /ssmgr/certificate | Class X Migration Certificate
[**tetcr**](APIsApi.md#tetcr) | **POST** /tetcr/certificate | Teachers Eligibility Test Certificate
[**tetms**](APIsApi.md#tetms) | **POST** /tetms/certificate | Teachers Eligibility Test Mark Sheet



## hpcer

> hpcer(opts)

Class XII Passing Certificate

API to verify Class XII Passing Certificate.

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hpcerRequest': new CentralBoardOfSecondaryEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.hpcer(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## hscer

> hscer(opts)

Class XII Marksheet

API to verify Class XII Marksheet.

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hscerRequest': new CentralBoardOfSecondaryEducation.HscerRequest() // HscerRequest | Request format
};
apiInstance.hscer(opts, (error, data, response) => {
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
 **hscerRequest** | [**HscerRequest**](HscerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/xml, application/json


## hsmgr

> hsmgr(opts)

Class XII Migration Certificate

API to verify Class XII Migration Certificate.

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hpcerRequest': new CentralBoardOfSecondaryEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.hsmgr(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## nchsc

> nchsc(opts)

NCHMCT Skill Certificate (X)

API to verify NCHMCT Skill Certificate (X).

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hpcerRequest': new CentralBoardOfSecondaryEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.nchsc(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## nctsc

> nctsc(opts)

NCHMCT Skill Certificate (XII)

API to verify NCHMCT Skill Certificate (XII).

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hpcerRequest': new CentralBoardOfSecondaryEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.nctsc(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## nsesc

> nsesc(opts)

NSE Skill Certificate (X)

API to verify NSE Skill Certificate (X).

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hpcerRequest': new CentralBoardOfSecondaryEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.nsesc(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## nstsc

> nstsc(opts)

NSE Skill Certificate (XII)

API to verify NSE Skill Certificate (XII).

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hpcerRequest': new CentralBoardOfSecondaryEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.nstsc(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## ntltr

> ntltr(opts)

NEET Rank Letter

API to verify NEET Rank Letter.

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hpcerRequest': new CentralBoardOfSecondaryEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.ntltr(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## ntmks

> ntmks(opts)

NEET Marksheet

API to verify NEET Marksheet.

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hpcerRequest': new CentralBoardOfSecondaryEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.ntmks(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## skhsc

> skhsc(opts)

Skill Certificate (X)

API to verify Skill Certificate (X).

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hpcerRequest': new CentralBoardOfSecondaryEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.skhsc(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## sktsc

> sktsc(opts)

Skill Certificate (XII)

API to verify Skill Certificate (XII).

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hpcerRequest': new CentralBoardOfSecondaryEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.sktsc(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## spcer

> spcer(opts)

Class X Passing Certificate

API to verify Class X Passing Certificate.

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hpcerRequest': new CentralBoardOfSecondaryEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.spcer(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## sscer

> sscer(opts)

Class X Marksheet

API to verify Class X Marksheet.

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hscerRequest': new CentralBoardOfSecondaryEducation.HscerRequest() // HscerRequest | Request format
};
apiInstance.sscer(opts, (error, data, response) => {
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
 **hscerRequest** | [**HscerRequest**](HscerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/xml, application/json


## ssmgr

> ssmgr(opts)

Class X Migration Certificate

API to verify Class X Migration Certificate.

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'hpcerRequest': new CentralBoardOfSecondaryEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.ssmgr(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## tetcr

> tetcr(opts)

Teachers Eligibility Test Certificate

API to verify Teachers Eligibility Test Certificate.

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'tetcrRequest': new CentralBoardOfSecondaryEducation.TetcrRequest() // TetcrRequest | Request format
};
apiInstance.tetcr(opts, (error, data, response) => {
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
 **tetcrRequest** | [**TetcrRequest**](TetcrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## tetms

> tetms(opts)

Teachers Eligibility Test Mark Sheet

API to verify Teachers Eligibility Test Mark Sheet.

### Example

```javascript
import CentralBoardOfSecondaryEducation from 'central_board_of_secondary_education';
let defaultClient = CentralBoardOfSecondaryEducation.ApiClient.instance;
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

let apiInstance = new CentralBoardOfSecondaryEducation.APIsApi();
let opts = {
  'tetcrRequest': new CentralBoardOfSecondaryEducation.TetcrRequest() // TetcrRequest | Request format
};
apiInstance.tetms(opts, (error, data, response) => {
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
 **tetcrRequest** | [**TetcrRequest**](TetcrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

