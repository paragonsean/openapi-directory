# EDistrictHimachalPradeshHimachalPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/edistricthp/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aecmw**](APIsApi.md#aecmw) | **POST** /aecmw/certificate | Application for Renewal of Contractor Migrant Workmen license
[**aemtw**](APIsApi.md#aemtw) | **POST** /aemtw/certificate | Application for Renewal of Motor Transport Worker Registration
[**agcer**](APIsApi.md#agcer) | **POST** /agcer/certificate | Agriculture/ Agriculturist Certificate
[**alimw**](APIsApi.md#alimw) | **POST** /alimw/certificate | Application for License for Inter State Migrant Workmen
[**arcmw**](APIsApi.md#arcmw) | **POST** /arcmw/certificate | Application for Registration of Contractor Migrant Workmen license
[**armtw**](APIsApi.md#armtw) | **POST** /armtw/certificate | Application for Registration of Motor Transport Worker Registration
[**bacer**](APIsApi.md#bacer) | **POST** /bacer/certificate | Backward Area Certificate
[**bhcer**](APIsApi.md#bhcer) | **POST** /bhcer/certificate | Bonafide Certificate
[**bpcrd**](APIsApi.md#bpcrd) | **POST** /bpcrd/certificate | BPL Card
[**btcer**](APIsApi.md#btcer) | **POST** /btcer/certificate | Birth Certificate
[**cecer**](APIsApi.md#cecer) | **POST** /cecer/certificate | Renewal Certificate of Contract Labour License
[**chcer**](APIsApi.md#chcer) | **POST** /chcer/certificate | Character Certificate
[**clcer**](APIsApi.md#clcer) | **POST** /clcer/certificate | Registration Certificate for Contract Labour License
[**coprg**](APIsApi.md#coprg) | **POST** /coprg/certificate | Copy of Pariwar Register
[**dccer**](APIsApi.md#dccer) | **POST** /dccer/certificate | Dogra Class Certificate
[**dmcer**](APIsApi.md#dmcer) | **POST** /dmcer/certificate | Domicile Certificate
[**dpicr**](APIsApi.md#dpicr) | **POST** /dpicr/certificate | Disabled Person Identity Card/ Certificate
[**dtcer**](APIsApi.md#dtcer) | **POST** /dtcer/certificate | Death Certificate
[**ercer**](APIsApi.md#ercer) | **POST** /ercer/certificate | Registration Certificate of Establishment Employing Contract Labour
[**ffcer**](APIsApi.md#ffcer) | **POST** /ffcer/certificate | Freedom Fighter Certificate
[**igcer**](APIsApi.md#igcer) | **POST** /igcer/certificate | Indigent (Needy Person) Certificate
[**incer**](APIsApi.md#incer) | **POST** /incer/certificate | Income Certificate
[**lhcer**](APIsApi.md#lhcer) | **POST** /lhcer/certificate | Legal Heir Certificate
[**mncer**](APIsApi.md#mncer) | **POST** /mncer/certificate | Minority Certificate
[**mnrga**](APIsApi.md#mnrga) | **POST** /mnrga/certificate | MNREGA Job Card
[**obcer**](APIsApi.md#obcer) | **POST** /obcer/certificate | OBC Certificate
[**racer**](APIsApi.md#racer) | **POST** /racer/certificate | Rural Area Certificate
[**rmcer**](APIsApi.md#rmcer) | **POST** /rmcer/certificate | Marriage Certificate
[**secer**](APIsApi.md#secer) | **POST** /secer/certificate | Renewal Certificate of Shops And Commercial Establishment
[**shcer**](APIsApi.md#shcer) | **POST** /shcer/certificate | SC/ST  Certificate
[**sicrd**](APIsApi.md#sicrd) | **POST** /sicrd/certificate | Senior Citizen Identity Card/ Certificate
[**srcer**](APIsApi.md#srcer) | **POST** /srcer/certificate | Registration Certificate of Shops And Commercial Establishment



## aecmw

> aecmw(opts)

Application for Renewal of Contractor Migrant Workmen license

API to verify Application for Renewal of Contractor Migrant Workmen license.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
};
apiInstance.aecmw(opts, (error, data, response) => {
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## aemtw

> aemtw(opts)

Application for Renewal of Motor Transport Worker Registration

API to verify Application for Renewal of Motor Transport Worker Registration.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
};
apiInstance.aemtw(opts, (error, data, response) => {
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## agcer

> agcer(opts)

Agriculture/ Agriculturist Certificate

API to verify Agriculture/ Agriculturist Certificate.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## alimw

> alimw(opts)

Application for License for Inter State Migrant Workmen

API to verify Application for License for Inter State Migrant Workmen.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## arcmw

> arcmw(opts)

Application for Registration of Contractor Migrant Workmen license

API to verify Application for Registration of Contractor Migrant Workmen license.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
};
apiInstance.arcmw(opts, (error, data, response) => {
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## armtw

> armtw(opts)

Application for Registration of Motor Transport Worker Registration

API to verify Application for Registration of Motor Transport Worker Registration.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
};
apiInstance.armtw(opts, (error, data, response) => {
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## bpcrd

> bpcrd(opts)

BPL Card

API to verify BPL Card.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
};
apiInstance.bpcrd(opts, (error, data, response) => {
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## btcer

> btcer(opts)

Birth Certificate

API to verify Birth Certificate.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## cecer

> cecer(opts)

Renewal Certificate of Contract Labour License

API to verify Renewal Certificate of Contract Labour License.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
};
apiInstance.cecer(opts, (error, data, response) => {
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## coprg

> coprg(opts)

Copy of Pariwar Register

API to verify Copy of Pariwar Register.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
};
apiInstance.coprg(opts, (error, data, response) => {
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## dpicr

> dpicr(opts)

Disabled Person Identity Card/ Certificate

API to verify Disabled Person Identity Card/ Certificate.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
};
apiInstance.dpicr(opts, (error, data, response) => {
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## ercer

> ercer(opts)

Registration Certificate of Establishment Employing Contract Labour

API to verify Registration Certificate of Establishment Employing Contract Labour.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
};
apiInstance.ercer(opts, (error, data, response) => {
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## igcer

> igcer(opts)

Indigent (Needy Person) Certificate

API to verify Indigent (Needy Person) Certificate.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
};
apiInstance.igcer(opts, (error, data, response) => {
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## mnrga

> mnrga(opts)

MNREGA Job Card

API to verify MNREGA Job Card.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
};
apiInstance.mnrga(opts, (error, data, response) => {
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## secer

> secer(opts)

Renewal Certificate of Shops And Commercial Establishment

API to verify Renewal Certificate of Shops And Commercial Establishment.

### Example

```javascript
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
};
apiInstance.secer(opts, (error, data, response) => {
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

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
import EDistrictHimachalPradeshHimachalPradesh from 'e_district_himachal_pradesh_himachal_pradesh';
let defaultClient = EDistrictHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'aecmwRequest': new EDistrictHimachalPradeshHimachalPradesh.AecmwRequest() // AecmwRequest | Request format
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
 **aecmwRequest** | [**AecmwRequest**](AecmwRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

