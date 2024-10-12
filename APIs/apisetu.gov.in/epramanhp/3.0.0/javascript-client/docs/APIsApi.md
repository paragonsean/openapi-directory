# HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/epramanhp/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agcer**](APIsApi.md#agcer) | **POST** /agcer/certificate | Agriculture/ Agriculturist Certificate
[**bacer**](APIsApi.md#bacer) | **POST** /bacer/certificate | Backward Area Certificate
[**bhcer**](APIsApi.md#bhcer) | **POST** /bhcer/certificate | Bonafide Certificate
[**chcer**](APIsApi.md#chcer) | **POST** /chcer/certificate | Character Certificate
[**dccer**](APIsApi.md#dccer) | **POST** /dccer/certificate | Dogra Class Certificate
[**ffcer**](APIsApi.md#ffcer) | **POST** /ffcer/certificate | Freedom Fighter Certificate
[**incer**](APIsApi.md#incer) | **POST** /incer/certificate | Income Certificate
[**lhcer**](APIsApi.md#lhcer) | **POST** /lhcer/certificate | Legal Heir Certificate
[**mncer**](APIsApi.md#mncer) | **POST** /mncer/certificate | Minority Certificate
[**obcer**](APIsApi.md#obcer) | **POST** /obcer/certificate | OBC Certificate
[**psprt**](APIsApi.md#psprt) | **POST** /psprt/certificate | Passport/ Passport Verification
[**racer**](APIsApi.md#racer) | **POST** /racer/certificate | Rural Area Certificate
[**rmcer**](APIsApi.md#rmcer) | **POST** /rmcer/certificate | Marriage Certificate
[**shcer**](APIsApi.md#shcer) | **POST** /shcer/certificate | SC/ST  Certificate



## agcer

> agcer(opts)

Agriculture/ Agriculturist Certificate

API to verify Agriculture/ Agriculturist Certificate.

### Example

```javascript
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
};
apiInstance.agcer(opts, (error, data, response) => {
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## bacer

> bacer(opts)

Backward Area Certificate

API to verify Backward Area Certificate.

### Example

```javascript
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
};
apiInstance.bacer(opts, (error, data, response) => {
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## bhcer

> bhcer(opts)

Bonafide Certificate

API to verify Bonafide Certificate.

### Example

```javascript
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
};
apiInstance.bhcer(opts, (error, data, response) => {
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## chcer

> chcer(opts)

Character Certificate

API to verify Character Certificate.

### Example

```javascript
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## dccer

> dccer(opts)

Dogra Class Certificate

API to verify Dogra Class Certificate.

### Example

```javascript
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
};
apiInstance.dccer(opts, (error, data, response) => {
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## ffcer

> ffcer(opts)

Freedom Fighter Certificate

API to verify Freedom Fighter Certificate.

### Example

```javascript
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
};
apiInstance.ffcer(opts, (error, data, response) => {
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

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
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

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
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

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
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

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
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## psprt

> psprt(opts)

Passport/ Passport Verification

API to verify Passport/ Passport Verification.

### Example

```javascript
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
};
apiInstance.psprt(opts, (error, data, response) => {
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

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
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

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
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

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
import HimachalPradeshDepartmentOfRevenueHimachalPradesh from 'himachal_pradesh_department_of_revenue_himachal_pradesh';
let defaultClient = HimachalPradeshDepartmentOfRevenueHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshDepartmentOfRevenueHimachalPradesh.APIsApi();
let opts = {
  'agcerRequest': new HimachalPradeshDepartmentOfRevenueHimachalPradesh.AgcerRequest() // AgcerRequest | Request format
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
 **agcerRequest** | [**AgcerRequest**](AgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

