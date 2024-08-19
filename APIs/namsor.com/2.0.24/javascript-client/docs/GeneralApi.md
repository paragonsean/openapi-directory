# NamSorApiV2.GeneralApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nameType**](GeneralApi.md#nameType) | **GET** /api2/json/nameType/{properNoun} | Infer the likely type of a proper noun (personal name, brand name, place name etc.)
[**nameTypeBatch**](GeneralApi.md#nameTypeBatch) | **POST** /api2/json/nameTypeBatch | Infer the likely common type of up to 100 proper nouns (personal name, brand name, place name etc.)
[**nameTypeGeo**](GeneralApi.md#nameTypeGeo) | **GET** /api2/json/nameTypeGeo/{properNoun}/{countryIso2} | Infer the likely type of a proper noun (personal name, brand name, place name etc.)
[**nameTypeGeoBatch**](GeneralApi.md#nameTypeGeoBatch) | **POST** /api2/json/nameTypeGeoBatch | Infer the likely common type of up to 100 proper nouns (personal name, brand name, place name etc.)



## nameType

> ProperNounCategorizedOut nameType(properNoun)

Infer the likely type of a proper noun (personal name, brand name, place name etc.)

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.GeneralApi();
let properNoun = "properNoun_example"; // String | 
apiInstance.nameType(properNoun, (error, data, response) => {
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
 **properNoun** | **String**|  | 

### Return type

[**ProperNounCategorizedOut**](ProperNounCategorizedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nameTypeBatch

> BatchProperNounCategorizedOut nameTypeBatch(opts)

Infer the likely common type of up to 100 proper nouns (personal name, brand name, place name etc.)

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.GeneralApi();
let opts = {
  'batchNameIn': new NamSorApiV2.BatchNameIn() // BatchNameIn | A list of proper names
};
apiInstance.nameTypeBatch(opts, (error, data, response) => {
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
 **batchNameIn** | [**BatchNameIn**](BatchNameIn.md)| A list of proper names | [optional] 

### Return type

[**BatchProperNounCategorizedOut**](BatchProperNounCategorizedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## nameTypeGeo

> ProperNounCategorizedOut nameTypeGeo(properNoun, countryIso2)

Infer the likely type of a proper noun (personal name, brand name, place name etc.)

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.GeneralApi();
let properNoun = "properNoun_example"; // String | 
let countryIso2 = "countryIso2_example"; // String | 
apiInstance.nameTypeGeo(properNoun, countryIso2, (error, data, response) => {
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
 **properNoun** | **String**|  | 
 **countryIso2** | **String**|  | 

### Return type

[**ProperNounCategorizedOut**](ProperNounCategorizedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nameTypeGeoBatch

> BatchProperNounCategorizedOut nameTypeGeoBatch(opts)

Infer the likely common type of up to 100 proper nouns (personal name, brand name, place name etc.)

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.GeneralApi();
let opts = {
  'batchNameGeoIn': new NamSorApiV2.BatchNameGeoIn() // BatchNameGeoIn | A list of proper names
};
apiInstance.nameTypeGeoBatch(opts, (error, data, response) => {
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
 **batchNameGeoIn** | [**BatchNameGeoIn**](BatchNameGeoIn.md)| A list of proper names | [optional] 

### Return type

[**BatchProperNounCategorizedOut**](BatchProperNounCategorizedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

