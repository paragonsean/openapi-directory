# SonarTrading.CurrenciesApi

All URIs are relative to *https://sonar.trading/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convertGet**](CurrenciesApi.md#convertGet) | **GET** /convert | Convert a currency amount to multiple other currencies
[**countryCurrenciesGet**](CurrenciesApi.md#countryCurrenciesGet) | **GET** /country/currencies | Return a list of all currencies of countries, available via service
[**digitalCurrenciesGet**](CurrenciesApi.md#digitalCurrenciesGet) | **GET** /digital/currencies | Return a list of all digital currencies, available via service
[**historyGet**](CurrenciesApi.md#historyGet) | **GET** /history | Return a historic rate for a currencies



## convertGet

> convertGet(from, to, opts)

Convert a currency amount to multiple other currencies

### Example

```javascript
import SonarTrading from 'sonar_trading';

let apiInstance = new SonarTrading.CurrenciesApi();
let from = "from_example"; // String | Currency you want to convert. For example, EUR
let to = "to_example"; // String | Comma separated list of currencies codes. For example, USD
let opts = {
  'amount': "amount_example", // String | This parameter can be used to specify the amount you want to convert. If an amount is not specified then 1 is assumed.
  'decimalPlaces': "decimalPlaces_example" // String | This parameter can be used to specify the number of decimal places included in the output. If an amount is not specified then 12 is assumed.
};
apiInstance.convertGet(from, to, opts, (error, data, response) => {
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
 **from** | **String**| Currency you want to convert. For example, EUR | 
 **to** | **String**| Comma separated list of currencies codes. For example, USD | 
 **amount** | **String**| This parameter can be used to specify the amount you want to convert. If an amount is not specified then 1 is assumed. | [optional] 
 **decimalPlaces** | **String**| This parameter can be used to specify the number of decimal places included in the output. If an amount is not specified then 12 is assumed. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## countryCurrenciesGet

> countryCurrenciesGet(opts)

Return a list of all currencies of countries, available via service

### Example

```javascript
import SonarTrading from 'sonar_trading';

let apiInstance = new SonarTrading.CurrenciesApi();
let opts = {
  'language': "language_example" // String | Parameter used to specify the language in which you would like the currency names to be provided. If not specified, EN is used. Now availeble only EN language.
};
apiInstance.countryCurrenciesGet(opts, (error, data, response) => {
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
 **language** | **String**| Parameter used to specify the language in which you would like the currency names to be provided. If not specified, EN is used. Now availeble only EN language. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## digitalCurrenciesGet

> digitalCurrenciesGet(opts)

Return a list of all digital currencies, available via service

### Example

```javascript
import SonarTrading from 'sonar_trading';

let apiInstance = new SonarTrading.CurrenciesApi();
let opts = {
  'language': "language_example" // String | Parameter used to specify the language in which you would like the currency names to be provided. If not specified, EN is used. Now availeble only EN language.
};
apiInstance.digitalCurrenciesGet(opts, (error, data, response) => {
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
 **language** | **String**| Parameter used to specify the language in which you would like the currency names to be provided. If not specified, EN is used. Now availeble only EN language. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## historyGet

> historyGet(from, to, date, opts)

Return a historic rate for a currencies

### Example

```javascript
import SonarTrading from 'sonar_trading';

let apiInstance = new SonarTrading.CurrenciesApi();
let from = "from_example"; // String | Currency you want to convert. For example, EUR
let to = "to_example"; // String | Comma separated list of currencies codes. For example, USD
let date = "date_example"; // String | UTC date should be in the form of YYYY-MM-DD, for example, 2018-06-20. Data available from 2018-06-19 only.
let opts = {
  'amount': "amount_example", // String | This parameter can be used to specify the amount you want to convert. If an amount is not specified then 1 is assumed.
  'decimalPlaces': "decimalPlaces_example" // String | This parameter can be used to specify the number of decimal places included in the output. If an amount is not specified then 4 is assumed.
};
apiInstance.historyGet(from, to, date, opts, (error, data, response) => {
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
 **from** | **String**| Currency you want to convert. For example, EUR | 
 **to** | **String**| Comma separated list of currencies codes. For example, USD | 
 **date** | **String**| UTC date should be in the form of YYYY-MM-DD, for example, 2018-06-20. Data available from 2018-06-19 only. | 
 **amount** | **String**| This parameter can be used to specify the amount you want to convert. If an amount is not specified then 1 is assumed. | [optional] 
 **decimalPlaces** | **String**| This parameter can be used to specify the number of decimal places included in the output. If an amount is not specified then 4 is assumed. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

