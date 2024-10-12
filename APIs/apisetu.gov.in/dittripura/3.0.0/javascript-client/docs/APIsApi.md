# DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi

All URIs are relative to *https://apisetu.gov.in/dittripura/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chcer**](APIsApi.md#chcer) | **POST** /chcer/certificate | Character Certificate
[**dncer**](APIsApi.md#dncer) | **POST** /dncer/certificate | Distance Certificate
[**dpcer**](APIsApi.md#dpcer) | **POST** /dpcer/certificate | Dependency Certificate
[**fslcs**](APIsApi.md#fslcs) | **POST** /fslcs/certificate | Food Stuff License
[**grred**](APIsApi.md#grred) | **POST** /grred/certificate | Grievance Redressal/ Registration
[**incer**](APIsApi.md#incer) | **POST** /incer/certificate | Income Certificate
[**isoal**](APIsApi.md#isoal) | **POST** /isoal/certificate | Issue of Arm Licence
[**lvcer**](APIsApi.md#lvcer) | **POST** /lvcer/certificate | Land Valuation/ Holding/ Record Certificate
[**malcs**](APIsApi.md#malcs) | **POST** /malcs/certificate | Manufacturer License
[**mpkby**](APIsApi.md#mpkby) | **POST** /mpkby/certificate | Small Savings Agent License
[**obcer**](APIsApi.md#obcer) | **POST** /obcer/certificate | OBC Certificate
[**ritin**](APIsApi.md#ritin) | **POST** /ritin/certificate | Right to Information
[**rmcer**](APIsApi.md#rmcer) | **POST** /rmcer/certificate | Marriage Certificate
[**rscer**](APIsApi.md#rscer) | **POST** /rscer/certificate | Residence Certificate
[**shcer**](APIsApi.md#shcer) | **POST** /shcer/certificate | SC/ST  Certificate
[**smcer**](APIsApi.md#smcer) | **POST** /smcer/certificate | Surviving Member Certificate
[**sslcs**](APIsApi.md#sslcs) | **POST** /sslcs/certificate | Standardized Agency Systems (SAS) Agent License
[**vrwmi**](APIsApi.md#vrwmi) | **POST** /vrwmi/certificate | License/ Verification of Weights, Measures and Instruments



## chcer

> chcer(opts)

Character Certificate

API to verify Character Certificate.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
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


## dncer

> dncer(opts)

Distance Certificate

API to verify Distance Certificate.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.dncer(opts, (error, data, response) => {
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
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
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


## fslcs

> fslcs(opts)

Food Stuff License

API to verify Food Stuff License.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.fslcs(opts, (error, data, response) => {
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


## grred

> grred(opts)

Grievance Redressal/ Registration

API to verify Grievance Redressal/ Registration.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.grred(opts, (error, data, response) => {
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
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
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


## isoal

> isoal(opts)

Issue of Arm Licence

API to verify Issue of Arm Licence.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.isoal(opts, (error, data, response) => {
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


## lvcer

> lvcer(opts)

Land Valuation/ Holding/ Record Certificate

API to verify Land Valuation/ Holding/ Record Certificate.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.lvcer(opts, (error, data, response) => {
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


## malcs

> malcs(opts)

Manufacturer License

API to verify Manufacturer License.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.malcs(opts, (error, data, response) => {
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


## mpkby

> mpkby(opts)

Small Savings Agent License

API to verify Small Savings Agent License.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.mpkby(opts, (error, data, response) => {
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


## obcer

> obcer(opts)

OBC Certificate

API to verify OBC Certificate.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
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
 **chcerRequest** | [**ChcerRequest**](ChcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## ritin

> ritin(opts)

Right to Information

API to verify Right to Information.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.ritin(opts, (error, data, response) => {
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


## rmcer

> rmcer(opts)

Marriage Certificate

API to verify Marriage Certificate.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
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
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
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
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
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


## smcer

> smcer(opts)

Surviving Member Certificate

API to verify Surviving Member Certificate.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.smcer(opts, (error, data, response) => {
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


## sslcs

> sslcs(opts)

Standardized Agency Systems (SAS) Agent License

API to verify Standardized Agency Systems (SAS) Agent License.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.sslcs(opts, (error, data, response) => {
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


## vrwmi

> vrwmi(opts)

License/ Verification of Weights, Measures and Instruments

API to verify License/ Verification of Weights, Measures and Instruments.

### Example

```javascript
import DirectorateOfInformationTechnologyGovernmentOfTripuraTripura from 'directorate_of_information_technology_government_of_tripura_tripura';
let defaultClient = DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ApiClient.instance;
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

let apiInstance = new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.APIsApi();
let opts = {
  'chcerRequest': new DirectorateOfInformationTechnologyGovernmentOfTripuraTripura.ChcerRequest() // ChcerRequest | Request format
};
apiInstance.vrwmi(opts, (error, data, response) => {
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

