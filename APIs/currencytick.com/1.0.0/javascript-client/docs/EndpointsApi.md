# CurrencytickApiDocumentation.EndpointsApi

All URIs are relative to *https://api.currencytick.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthcheck**](EndpointsApi.md#healthcheck) | **GET** /healthcheck | Healthcheck
[**historicalExchangeRate**](EndpointsApi.md#historicalExchangeRate) | **GET** /historical | Historical Exchange Rate
[**listOfSupportedCurrencies**](EndpointsApi.md#listOfSupportedCurrencies) | **GET** /supported_currencies | List of supported currencies
[**liveCurrencyExchangeRate**](EndpointsApi.md#liveCurrencyExchangeRate) | **GET** /live | Live currency exchange rate



## healthcheck

> Healthcheck200Response healthcheck()

Healthcheck

Check that the service is up. If everything is okay, you&#39;ll get a 200 OK response.  Otherwise, the request will fail with a 400 error, and a response listing the failed services.

### Example

```javascript
import CurrencytickApiDocumentation from 'currencytick_api_documentation';

let apiInstance = new CurrencytickApiDocumentation.EndpointsApi();
apiInstance.healthcheck((error, data, response) => {
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

[**Healthcheck200Response**](Healthcheck200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## historicalExchangeRate

> HistoricalExchangeRate200Response historicalExchangeRate(apikey, base, target, date)

Historical Exchange Rate

Get the exchange rate on a specific date

### Example

```javascript
import CurrencytickApiDocumentation from 'currencytick_api_documentation';
let defaultClient = CurrencytickApiDocumentation.ApiClient.instance;
// Configure API key authorization: default
let default = defaultClient.authentications['default'];
default.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//default.apiKeyPrefix = 'Token';

let apiInstance = new CurrencytickApiDocumentation.EndpointsApi();
let apikey = "YOUR_API_KEY"; // String | Authentication key.
let base = "USD"; // String | The source currency.
let target = "EUR"; // String | The target currency.
let date = "2023-04-18"; // String | The date to get the exchange rate.
apiInstance.historicalExchangeRate(apikey, base, target, date, (error, data, response) => {
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
 **apikey** | **String**| Authentication key. | 
 **base** | **String**| The source currency. | 
 **target** | **String**| The target currency. | 
 **date** | **String**| The date to get the exchange rate. | 

### Return type

[**HistoricalExchangeRate200Response**](HistoricalExchangeRate200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listOfSupportedCurrencies

> String listOfSupportedCurrencies(apikey)

List of supported currencies

Get the list of supported currencies, currently 220 currencies are supported.

### Example

```javascript
import CurrencytickApiDocumentation from 'currencytick_api_documentation';
let defaultClient = CurrencytickApiDocumentation.ApiClient.instance;
// Configure API key authorization: default
let default = defaultClient.authentications['default'];
default.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//default.apiKeyPrefix = 'Token';

let apiInstance = new CurrencytickApiDocumentation.EndpointsApi();
let apikey = "YOUR_API_KEY"; // String | Authentication key.
apiInstance.listOfSupportedCurrencies(apikey, (error, data, response) => {
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
 **apikey** | **String**| Authentication key. | 

### Return type

**String**

### Authorization

[default](../README.md#default)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## liveCurrencyExchangeRate

> HistoricalExchangeRate200Response liveCurrencyExchangeRate(apikey, base, target, opts)

Live currency exchange rate

Get the exchange rate between two currencies.

### Example

```javascript
import CurrencytickApiDocumentation from 'currencytick_api_documentation';
let defaultClient = CurrencytickApiDocumentation.ApiClient.instance;
// Configure API key authorization: default
let default = defaultClient.authentications['default'];
default.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//default.apiKeyPrefix = 'Token';

let apiInstance = new CurrencytickApiDocumentation.EndpointsApi();
let apikey = "YOUR_API_KEY"; // String | Authentication key.
let base = "USD"; // String | The source currency.
let target = "EUR"; // String | The target currency.
let opts = {
  'amount': 1 // Number | optional The amount to convert.
};
apiInstance.liveCurrencyExchangeRate(apikey, base, target, opts, (error, data, response) => {
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
 **apikey** | **String**| Authentication key. | 
 **base** | **String**| The source currency. | 
 **target** | **String**| The target currency. | 
 **amount** | **Number**| optional The amount to convert. | [optional] 

### Return type

[**HistoricalExchangeRate200Response**](HistoricalExchangeRate200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

