# OpenFinTechIo.CurrenciesApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currenciesGet**](CurrenciesApi.md#currenciesGet) | **GET** /currencies | List of currencies
[**currenciesIdGet**](CurrenciesApi.md#currenciesIdGet) | **GET** /currencies/{id} | Currency by ID



## currenciesGet

> CurrenciesResponse currenciesGet(opts)

List of currencies

Returns all available currencies. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.CurrenciesApi();
let opts = {
  'pageNumber': 56, // Number | Current page number.
  'pageSize': 56, // Number | Page size.<br>*Default value: 100* 
  'filterSearch': "filterSearch_example", // String | Full text search with name, code, type, code_iso_alpha3, code_jsons_alpha, code_estandards_alpha, category.
  'filterCodeIsoAlpha3': "filterCodeIsoAlpha3_example", // String | Filtering by ISO code.
  'filterCodeIsoNumeric3': 56, // Number | Filtering by ISO number.
  'filterCodeEstandardsAlpha': "filterCodeEstandardsAlpha_example", // String | Filtering by estandards code.
  'filterCurrencyType': ["null"], // [String] | Filtration by currency type.
  'filterCategory': ["null"], // [String] | Filtration by category.
  'sort': ["null"] // [String] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | type | -type | | category | -category | | code | -code | | code_iso_alpha3 | -code_iso_alpha3 | | code_iso_numeric3 | -code_iso_numeric3 | | code_estandards_alpha | -code_estandards_alpha | 
};
apiInstance.currenciesGet(opts, (error, data, response) => {
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
 **pageNumber** | **Number**| Current page number. | [optional] 
 **pageSize** | **Number**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 
 **filterSearch** | **String**| Full text search with name, code, type, code_iso_alpha3, code_jsons_alpha, code_estandards_alpha, category. | [optional] 
 **filterCodeIsoAlpha3** | **String**| Filtering by ISO code. | [optional] 
 **filterCodeIsoNumeric3** | **Number**| Filtering by ISO number. | [optional] 
 **filterCodeEstandardsAlpha** | **String**| Filtering by estandards code. | [optional] 
 **filterCurrencyType** | [**[String]**](String.md)| Filtration by currency type. | [optional] 
 **filterCategory** | [**[String]**](String.md)| Filtration by category. | [optional] 
 **sort** | [**[String]**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | type | -type | | category | -category | | code | -code | | code_iso_alpha3 | -code_iso_alpha3 | | code_iso_numeric3 | -code_iso_numeric3 | | code_estandards_alpha | -code_estandards_alpha |  | [optional] 

### Return type

[**CurrenciesResponse**](CurrenciesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## currenciesIdGet

> CurrencyResponse currenciesIdGet(id)

Currency by ID

Returns currency with specific ID. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.CurrenciesApi();
let id = "id_example"; // String | Unique ID.
apiInstance.currenciesIdGet(id, (error, data, response) => {
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
 **id** | **String**| Unique ID. | 

### Return type

[**CurrencyResponse**](CurrencyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

