# EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi

All URIs are relative to *https://apisetu.gov.in/edistrictandaman/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**brlcs**](APIsApi.md#brlcs) | **POST** /brlcs/certificate | Bar License
[**dpcer**](APIsApi.md#dpcer) | **POST** /dpcer/certificate | Dependency Certificate
[**fmcer**](APIsApi.md#fmcer) | **POST** /fmcer/certificate | Family Membership Certificate
[**incer**](APIsApi.md#incer) | **POST** /incer/certificate | Income Certificate
[**lccep**](APIsApi.md#lccep) | **POST** /lccep/certificate | Local Candidate/ Status Certificate
[**ndcer**](APIsApi.md#ndcer) | **POST** /ndcer/certificate | No Dues/ Objection Certificate
[**obcer**](APIsApi.md#obcer) | **POST** /obcer/certificate | OBC Certificate
[**rmcer**](APIsApi.md#rmcer) | **POST** /rmcer/certificate | Marriage Certificate
[**rscer**](APIsApi.md#rscer) | **POST** /rscer/certificate | Residence Certificate
[**rucer**](APIsApi.md#rucer) | **POST** /rucer/certificate | Regional Language(s) Certificate
[**sicrd**](APIsApi.md#sicrd) | **POST** /sicrd/certificate | Senior Citizen Identity Card/ Certificate
[**vlcer**](APIsApi.md#vlcer) | **POST** /vlcer/certificate | Valuation Certificate



## brlcs

> brlcs(opts)

Bar License

API to verify Bar License.

### Example

```javascript
import EDistrictAndamanNicobarIslandsAndamanNicobar from 'e_district_andaman__nicobar_islands_andaman__nicobar';
let defaultClient = EDistrictAndamanNicobarIslandsAndamanNicobar.ApiClient.instance;
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

let apiInstance = new EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi();
let opts = {
  'brlcsRequest': new EDistrictAndamanNicobarIslandsAndamanNicobar.BrlcsRequest() // BrlcsRequest | Request format
};
apiInstance.brlcs(opts, (error, data, response) => {
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
 **brlcsRequest** | [**BrlcsRequest**](BrlcsRequest.md)| Request format | [optional] 

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
import EDistrictAndamanNicobarIslandsAndamanNicobar from 'e_district_andaman__nicobar_islands_andaman__nicobar';
let defaultClient = EDistrictAndamanNicobarIslandsAndamanNicobar.ApiClient.instance;
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

let apiInstance = new EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi();
let opts = {
  'brlcsRequest': new EDistrictAndamanNicobarIslandsAndamanNicobar.BrlcsRequest() // BrlcsRequest | Request format
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
 **brlcsRequest** | [**BrlcsRequest**](BrlcsRequest.md)| Request format | [optional] 

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
import EDistrictAndamanNicobarIslandsAndamanNicobar from 'e_district_andaman__nicobar_islands_andaman__nicobar';
let defaultClient = EDistrictAndamanNicobarIslandsAndamanNicobar.ApiClient.instance;
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

let apiInstance = new EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi();
let opts = {
  'brlcsRequest': new EDistrictAndamanNicobarIslandsAndamanNicobar.BrlcsRequest() // BrlcsRequest | Request format
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
 **brlcsRequest** | [**BrlcsRequest**](BrlcsRequest.md)| Request format | [optional] 

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
import EDistrictAndamanNicobarIslandsAndamanNicobar from 'e_district_andaman__nicobar_islands_andaman__nicobar';
let defaultClient = EDistrictAndamanNicobarIslandsAndamanNicobar.ApiClient.instance;
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

let apiInstance = new EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi();
let opts = {
  'brlcsRequest': new EDistrictAndamanNicobarIslandsAndamanNicobar.BrlcsRequest() // BrlcsRequest | Request format
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
 **brlcsRequest** | [**BrlcsRequest**](BrlcsRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## lccep

> lccep(opts)

Local Candidate/ Status Certificate

API to verify Local Candidate/ Status Certificate.

### Example

```javascript
import EDistrictAndamanNicobarIslandsAndamanNicobar from 'e_district_andaman__nicobar_islands_andaman__nicobar';
let defaultClient = EDistrictAndamanNicobarIslandsAndamanNicobar.ApiClient.instance;
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

let apiInstance = new EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi();
let opts = {
  'brlcsRequest': new EDistrictAndamanNicobarIslandsAndamanNicobar.BrlcsRequest() // BrlcsRequest | Request format
};
apiInstance.lccep(opts, (error, data, response) => {
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
 **brlcsRequest** | [**BrlcsRequest**](BrlcsRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## ndcer

> ndcer(opts)

No Dues/ Objection Certificate

API to verify No Dues/ Objection Certificate.

### Example

```javascript
import EDistrictAndamanNicobarIslandsAndamanNicobar from 'e_district_andaman__nicobar_islands_andaman__nicobar';
let defaultClient = EDistrictAndamanNicobarIslandsAndamanNicobar.ApiClient.instance;
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

let apiInstance = new EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi();
let opts = {
  'brlcsRequest': new EDistrictAndamanNicobarIslandsAndamanNicobar.BrlcsRequest() // BrlcsRequest | Request format
};
apiInstance.ndcer(opts, (error, data, response) => {
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
 **brlcsRequest** | [**BrlcsRequest**](BrlcsRequest.md)| Request format | [optional] 

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
import EDistrictAndamanNicobarIslandsAndamanNicobar from 'e_district_andaman__nicobar_islands_andaman__nicobar';
let defaultClient = EDistrictAndamanNicobarIslandsAndamanNicobar.ApiClient.instance;
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

let apiInstance = new EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi();
let opts = {
  'brlcsRequest': new EDistrictAndamanNicobarIslandsAndamanNicobar.BrlcsRequest() // BrlcsRequest | Request format
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
 **brlcsRequest** | [**BrlcsRequest**](BrlcsRequest.md)| Request format | [optional] 

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
import EDistrictAndamanNicobarIslandsAndamanNicobar from 'e_district_andaman__nicobar_islands_andaman__nicobar';
let defaultClient = EDistrictAndamanNicobarIslandsAndamanNicobar.ApiClient.instance;
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

let apiInstance = new EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi();
let opts = {
  'brlcsRequest': new EDistrictAndamanNicobarIslandsAndamanNicobar.BrlcsRequest() // BrlcsRequest | Request format
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
 **brlcsRequest** | [**BrlcsRequest**](BrlcsRequest.md)| Request format | [optional] 

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
import EDistrictAndamanNicobarIslandsAndamanNicobar from 'e_district_andaman__nicobar_islands_andaman__nicobar';
let defaultClient = EDistrictAndamanNicobarIslandsAndamanNicobar.ApiClient.instance;
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

let apiInstance = new EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi();
let opts = {
  'brlcsRequest': new EDistrictAndamanNicobarIslandsAndamanNicobar.BrlcsRequest() // BrlcsRequest | Request format
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
 **brlcsRequest** | [**BrlcsRequest**](BrlcsRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## rucer

> rucer(opts)

Regional Language(s) Certificate

API to verify Regional Language(s) Certificate.

### Example

```javascript
import EDistrictAndamanNicobarIslandsAndamanNicobar from 'e_district_andaman__nicobar_islands_andaman__nicobar';
let defaultClient = EDistrictAndamanNicobarIslandsAndamanNicobar.ApiClient.instance;
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

let apiInstance = new EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi();
let opts = {
  'brlcsRequest': new EDistrictAndamanNicobarIslandsAndamanNicobar.BrlcsRequest() // BrlcsRequest | Request format
};
apiInstance.rucer(opts, (error, data, response) => {
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
 **brlcsRequest** | [**BrlcsRequest**](BrlcsRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## sicrd

> sicrd(opts)

Senior Citizen Identity Card/ Certificate

API to verify Senior Citizen Identity Card/ Certificate.

### Example

```javascript
import EDistrictAndamanNicobarIslandsAndamanNicobar from 'e_district_andaman__nicobar_islands_andaman__nicobar';
let defaultClient = EDistrictAndamanNicobarIslandsAndamanNicobar.ApiClient.instance;
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

let apiInstance = new EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi();
let opts = {
  'brlcsRequest': new EDistrictAndamanNicobarIslandsAndamanNicobar.BrlcsRequest() // BrlcsRequest | Request format
};
apiInstance.sicrd(opts, (error, data, response) => {
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
 **brlcsRequest** | [**BrlcsRequest**](BrlcsRequest.md)| Request format | [optional] 

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
import EDistrictAndamanNicobarIslandsAndamanNicobar from 'e_district_andaman__nicobar_islands_andaman__nicobar';
let defaultClient = EDistrictAndamanNicobarIslandsAndamanNicobar.ApiClient.instance;
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

let apiInstance = new EDistrictAndamanNicobarIslandsAndamanNicobar.APIsApi();
let opts = {
  'brlcsRequest': new EDistrictAndamanNicobarIslandsAndamanNicobar.BrlcsRequest() // BrlcsRequest | Request format
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
 **brlcsRequest** | [**BrlcsRequest**](BrlcsRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

