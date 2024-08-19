# NamSorApiV2.IndianApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**castegroupIndianFull**](IndianApi.md#castegroupIndianFull) | **GET** /api2/json/castegroupIndianFull/{subDivisionIso31662}/{personalNameFull} | [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of a personal full name.
[**castegroupIndianFullBatch**](IndianApi.md#castegroupIndianFullBatch) | **POST** /api2/json/castegroupIndianFullBatch | [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of up to 100 personal full names. 
[**religion**](IndianApi.md#religion) | **GET** /api2/json/religionIndianFull/{subDivisionIso31662}/{personalNameFull} | [USES 10 UNITS PER NAME] Infer the likely religion of a personal Indian full name, provided the Indian state or Union territory (NB/ this can be inferred using the subclassification endpoint).
[**religionIndianFullBatch**](IndianApi.md#religionIndianFullBatch) | **POST** /api2/json/religionIndianFullBatch | [USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal full Indian names, provided the subclassification at State or Union territory level (NB/ can be inferred using the subclassification endpoint).
[**subclassificationIndian**](IndianApi.md#subclassificationIndian) | **GET** /api2/json/subclassificationIndian/{firstName}/{lastName} | [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.
[**subclassificationIndianBatch**](IndianApi.md#subclassificationIndianBatch) | **POST** /api2/json/subclassificationIndianBatch | [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.
[**subclassificationIndianFull**](IndianApi.md#subclassificationIndianFull) | **GET** /api2/json/subclassificationIndianFull/{fullName} | [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.
[**subclassificationIndianFullBatch**](IndianApi.md#subclassificationIndianFullBatch) | **POST** /api2/json/subclassificationIndianFullBatch | [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.



## castegroupIndianFull

> PersonalNameCastegroupOut castegroupIndianFull(subDivisionIso31662, personalNameFull)

[USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of a personal full name.

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.IndianApi();
let subDivisionIso31662 = "subDivisionIso31662_example"; // String | 
let personalNameFull = "personalNameFull_example"; // String | 
apiInstance.castegroupIndianFull(subDivisionIso31662, personalNameFull, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subDivisionIso31662** | **String**|  | 
 **personalNameFull** | **String**|  | 

### Return type

[**PersonalNameCastegroupOut**](PersonalNameCastegroupOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## castegroupIndianFullBatch

> BatchPersonalNameCastegroupOut castegroupIndianFullBatch(opts)

[USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of up to 100 personal full names. 

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.IndianApi();
let opts = {
  'batchPersonalNameSubdivisionIn': new NamSorApiV2.BatchPersonalNameSubdivisionIn() // BatchPersonalNameSubdivisionIn | A list of personal names
};
apiInstance.castegroupIndianFullBatch(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batchPersonalNameSubdivisionIn** | [**BatchPersonalNameSubdivisionIn**](BatchPersonalNameSubdivisionIn.md)| A list of personal names | [optional] 

### Return type

[**BatchPersonalNameCastegroupOut**](BatchPersonalNameCastegroupOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## religion

> PersonalNameReligionedOut religion(subDivisionIso31662, personalNameFull)

[USES 10 UNITS PER NAME] Infer the likely religion of a personal Indian full name, provided the Indian state or Union territory (NB/ this can be inferred using the subclassification endpoint).

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.IndianApi();
let subDivisionIso31662 = "subDivisionIso31662_example"; // String | 
let personalNameFull = "personalNameFull_example"; // String | 
apiInstance.religion(subDivisionIso31662, personalNameFull, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subDivisionIso31662** | **String**|  | 
 **personalNameFull** | **String**|  | 

### Return type

[**PersonalNameReligionedOut**](PersonalNameReligionedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## religionIndianFullBatch

> BatchPersonalNameReligionedOut religionIndianFullBatch(opts)

[USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal full Indian names, provided the subclassification at State or Union territory level (NB/ can be inferred using the subclassification endpoint).

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.IndianApi();
let opts = {
  'batchPersonalNameSubdivisionIn': new NamSorApiV2.BatchPersonalNameSubdivisionIn() // BatchPersonalNameSubdivisionIn | A list of personal names
};
apiInstance.religionIndianFullBatch(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batchPersonalNameSubdivisionIn** | [**BatchPersonalNameSubdivisionIn**](BatchPersonalNameSubdivisionIn.md)| A list of personal names | [optional] 

### Return type

[**BatchPersonalNameReligionedOut**](BatchPersonalNameReligionedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subclassificationIndian

> FirstLastNameGeoSubclassificationOut subclassificationIndian(firstName, lastName)

[USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.IndianApi();
let firstName = "firstName_example"; // String | 
let lastName = "lastName_example"; // String | 
apiInstance.subclassificationIndian(firstName, lastName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firstName** | **String**|  | 
 **lastName** | **String**|  | 

### Return type

[**FirstLastNameGeoSubclassificationOut**](FirstLastNameGeoSubclassificationOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subclassificationIndianBatch

> BatchFirstLastNameGeoSubclassificationOut subclassificationIndianBatch(opts)

[USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.IndianApi();
let opts = {
  'batchFirstLastNameGeoIn': new NamSorApiV2.BatchFirstLastNameGeoIn() // BatchFirstLastNameGeoIn | A list of personal names
};
apiInstance.subclassificationIndianBatch(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batchFirstLastNameGeoIn** | [**BatchFirstLastNameGeoIn**](BatchFirstLastNameGeoIn.md)| A list of personal names | [optional] 

### Return type

[**BatchFirstLastNameGeoSubclassificationOut**](BatchFirstLastNameGeoSubclassificationOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subclassificationIndianFull

> PersonalNameGeoSubclassificationOut subclassificationIndianFull(fullName)

[USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.IndianApi();
let fullName = "fullName_example"; // String | 
apiInstance.subclassificationIndianFull(fullName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fullName** | **String**|  | 

### Return type

[**PersonalNameGeoSubclassificationOut**](PersonalNameGeoSubclassificationOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subclassificationIndianFullBatch

> BatchPersonalNameGeoSubclassificationOut subclassificationIndianFullBatch(opts)

[USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.IndianApi();
let opts = {
  'batchPersonalNameGeoIn': new NamSorApiV2.BatchPersonalNameGeoIn() // BatchPersonalNameGeoIn | A list of personal names
};
apiInstance.subclassificationIndianFullBatch(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batchPersonalNameGeoIn** | [**BatchPersonalNameGeoIn**](BatchPersonalNameGeoIn.md)| A list of personal names | [optional] 

### Return type

[**BatchPersonalNameGeoSubclassificationOut**](BatchPersonalNameGeoSubclassificationOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

