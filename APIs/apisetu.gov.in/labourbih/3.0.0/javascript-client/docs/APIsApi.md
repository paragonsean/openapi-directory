# LabourResourceDepartmentBihar.APIsApi

All URIs are relative to *https://apisetu.gov.in/labourbih/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alimw**](APIsApi.md#alimw) | **POST** /alimw/certificate | Application for License for Inter State Migrant Workmen
[**alsbl**](APIsApi.md#alsbl) | **POST** /alsbl/certificate | Application/ License for Boilers
[**alsfc**](APIsApi.md#alsfc) | **POST** /alsfc/certificate | Application/ License for Factory
[**apptu**](APIsApi.md#apptu) | **POST** /apptu/certificate | Application realted to Trade Unions
[**clcer**](APIsApi.md#clcer) | **POST** /clcer/certificate | Registration Certificate for Contract Labour License
[**noocl**](APIsApi.md#noocl) | **POST** /noocl/certificate | Notice of Closure
[**srcer**](APIsApi.md#srcer) | **POST** /srcer/certificate | Registration Certificate of Shops And Commercial Establishment



## alimw

> alimw(opts)

Application for License for Inter State Migrant Workmen

API to verify Application for License for Inter State Migrant Workmen.

### Example

```javascript
import LabourResourceDepartmentBihar from 'labour_resource_department_bihar';
let defaultClient = LabourResourceDepartmentBihar.ApiClient.instance;
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

let apiInstance = new LabourResourceDepartmentBihar.APIsApi();
let opts = {
  'alimwRequest': new LabourResourceDepartmentBihar.AlimwRequest() // AlimwRequest | Request format
};
apiInstance.alimw(opts, (error, data, response) => {
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
 **alimwRequest** | [**AlimwRequest**](AlimwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## alsbl

> alsbl(opts)

Application/ License for Boilers

API to verify Application/ License for Boilers.

### Example

```javascript
import LabourResourceDepartmentBihar from 'labour_resource_department_bihar';
let defaultClient = LabourResourceDepartmentBihar.ApiClient.instance;
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

let apiInstance = new LabourResourceDepartmentBihar.APIsApi();
let opts = {
  'alimwRequest': new LabourResourceDepartmentBihar.AlimwRequest() // AlimwRequest | Request format
};
apiInstance.alsbl(opts, (error, data, response) => {
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
 **alimwRequest** | [**AlimwRequest**](AlimwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## alsfc

> alsfc(opts)

Application/ License for Factory

API to verify Application/ License for Factory.

### Example

```javascript
import LabourResourceDepartmentBihar from 'labour_resource_department_bihar';
let defaultClient = LabourResourceDepartmentBihar.ApiClient.instance;
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

let apiInstance = new LabourResourceDepartmentBihar.APIsApi();
let opts = {
  'alimwRequest': new LabourResourceDepartmentBihar.AlimwRequest() // AlimwRequest | Request format
};
apiInstance.alsfc(opts, (error, data, response) => {
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
 **alimwRequest** | [**AlimwRequest**](AlimwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## apptu

> apptu(opts)

Application realted to Trade Unions

API to verify Application realted to Trade Unions.

### Example

```javascript
import LabourResourceDepartmentBihar from 'labour_resource_department_bihar';
let defaultClient = LabourResourceDepartmentBihar.ApiClient.instance;
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

let apiInstance = new LabourResourceDepartmentBihar.APIsApi();
let opts = {
  'alimwRequest': new LabourResourceDepartmentBihar.AlimwRequest() // AlimwRequest | Request format
};
apiInstance.apptu(opts, (error, data, response) => {
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
 **alimwRequest** | [**AlimwRequest**](AlimwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## clcer

> clcer(opts)

Registration Certificate for Contract Labour License

API to verify Registration Certificate for Contract Labour License.

### Example

```javascript
import LabourResourceDepartmentBihar from 'labour_resource_department_bihar';
let defaultClient = LabourResourceDepartmentBihar.ApiClient.instance;
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

let apiInstance = new LabourResourceDepartmentBihar.APIsApi();
let opts = {
  'alimwRequest': new LabourResourceDepartmentBihar.AlimwRequest() // AlimwRequest | Request format
};
apiInstance.clcer(opts, (error, data, response) => {
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
 **alimwRequest** | [**AlimwRequest**](AlimwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## noocl

> noocl(opts)

Notice of Closure

API to verify Notice of Closure.

### Example

```javascript
import LabourResourceDepartmentBihar from 'labour_resource_department_bihar';
let defaultClient = LabourResourceDepartmentBihar.ApiClient.instance;
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

let apiInstance = new LabourResourceDepartmentBihar.APIsApi();
let opts = {
  'alimwRequest': new LabourResourceDepartmentBihar.AlimwRequest() // AlimwRequest | Request format
};
apiInstance.noocl(opts, (error, data, response) => {
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
 **alimwRequest** | [**AlimwRequest**](AlimwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## srcer

> srcer(opts)

Registration Certificate of Shops And Commercial Establishment

API to verify Registration Certificate of Shops And Commercial Establishment.

### Example

```javascript
import LabourResourceDepartmentBihar from 'labour_resource_department_bihar';
let defaultClient = LabourResourceDepartmentBihar.ApiClient.instance;
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

let apiInstance = new LabourResourceDepartmentBihar.APIsApi();
let opts = {
  'alimwRequest': new LabourResourceDepartmentBihar.AlimwRequest() // AlimwRequest | Request format
};
apiInstance.srcer(opts, (error, data, response) => {
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
 **alimwRequest** | [**AlimwRequest**](AlimwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

