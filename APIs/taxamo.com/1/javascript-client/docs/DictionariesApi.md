# Taxamo.DictionariesApi

All URIs are relative to *https://api.taxamo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCountriesDict**](DictionariesApi.md#getCountriesDict) | **GET** /api/v1/dictionaries/countries | Countries
[**getCurrenciesDict**](DictionariesApi.md#getCurrenciesDict) | **GET** /api/v1/dictionaries/currencies | Currencies
[**getProductTypesDict**](DictionariesApi.md#getProductTypesDict) | **GET** /api/v1/dictionaries/product_types | Product types



## getCountriesDict

> GetCountriesDictOut getCountriesDict(opts)

Countries

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.DictionariesApi();
let opts = {
  'taxSupported': true // Boolean | Should only countries with tax supported be listed?
};
apiInstance.getCountriesDict(opts, (error, data, response) => {
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
 **taxSupported** | **Boolean**| Should only countries with tax supported be listed? | [optional] 

### Return type

[**GetCountriesDictOut**](GetCountriesDictOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCurrenciesDict

> GetCurrenciesDictOut getCurrenciesDict()

Currencies

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.DictionariesApi();
apiInstance.getCurrenciesDict((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetCurrenciesDictOut**](GetCurrenciesDictOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductTypesDict

> GetProductTypesDictOut getProductTypesDict()

Product types

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.DictionariesApi();
apiInstance.getProductTypesDict((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetProductTypesDictOut**](GetProductTypesDictOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

