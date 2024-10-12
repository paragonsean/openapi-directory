# Polygon.CurrenciesApi

All URIs are relative to *https://api.polygon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CurrenciesGet**](CurrenciesApi.md#v1CurrenciesGet) | **GET** /v1/currencies | Available Currencies
[**v1HistoricForexFromToDateGet**](CurrenciesApi.md#v1HistoricForexFromToDateGet) | **GET** /v1/historic/forex/{from}/{to}/{date} | Historic Forex Ticks
[**v1LastCurrenciesFromToGet**](CurrenciesApi.md#v1LastCurrenciesFromToGet) | **GET** /v1/last/currencies/{from}/{to} | Last Trade for a Currency Pair
[**v1LastQuoteCurrenciesFromToGet**](CurrenciesApi.md#v1LastQuoteCurrenciesFromToGet) | **GET** /v1/last_quote/currencies/{from}/{to} | Last Quote for a Currency Pair



## v1CurrenciesGet

> [String] v1CurrenciesGet()

Available Currencies

Get a list of the currencies that polygon.io streams. 

### Example

```javascript
import Polygon from 'polygon';
let defaultClient = Polygon.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Polygon.CurrenciesApi();
apiInstance.v1CurrenciesGet((error, data, response) => {
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

**[String]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v1HistoricForexFromToDateGet

> V1HistoricForexFromToDateGet200Response v1HistoricForexFromToDateGet(from, to, date, opts)

Historic Forex Ticks

Get historic ticks for a currency pair. Example for **USD/JPY** the from would be **USD** and to would be **JPY**. The date formatted like **2017-6-22** 

### Example

```javascript
import Polygon from 'polygon';
let defaultClient = Polygon.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Polygon.CurrenciesApi();
let from = "from_example"; // String | From Symbol of the currency pair
let to = "to_example"; // String | To Symbol of the currency pair
let date = new Date("2013-10-20"); // Date | Date/Day of the historic ticks to retreive
let opts = {
  'offset': 56, // Number | Timestamp offset, used for pagination
  'limit': 100 // Number | Limit the size of response, max: 10000
};
apiInstance.v1HistoricForexFromToDateGet(from, to, date, opts, (error, data, response) => {
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
 **from** | **String**| From Symbol of the currency pair | 
 **to** | **String**| To Symbol of the currency pair | 
 **date** | **Date**| Date/Day of the historic ticks to retreive | 
 **offset** | **Number**| Timestamp offset, used for pagination | [optional] 
 **limit** | **Number**| Limit the size of response, max: 10000 | [optional] [default to 100]

### Return type

[**V1HistoricForexFromToDateGet200Response**](V1HistoricForexFromToDateGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v1LastCurrenciesFromToGet

> V1LastCurrenciesFromToGet200Response v1LastCurrenciesFromToGet(from, to)

Last Trade for a Currency Pair

Get Last Trade Tick for a Currency Pair. 

### Example

```javascript
import Polygon from 'polygon';
let defaultClient = Polygon.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Polygon.CurrenciesApi();
let from = "from_example"; // String | From Symbol of the pair
let to = "to_example"; // String | To Symbol of the pair
apiInstance.v1LastCurrenciesFromToGet(from, to, (error, data, response) => {
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
 **from** | **String**| From Symbol of the pair | 
 **to** | **String**| To Symbol of the pair | 

### Return type

[**V1LastCurrenciesFromToGet200Response**](V1LastCurrenciesFromToGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v1LastQuoteCurrenciesFromToGet

> V1LastQuoteCurrenciesFromToGet200Response v1LastQuoteCurrenciesFromToGet(from, to)

Last Quote for a Currency Pair

Get Last Quote Tick for a Currency Pair. 

### Example

```javascript
import Polygon from 'polygon';
let defaultClient = Polygon.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Polygon.CurrenciesApi();
let from = "from_example"; // String | From Symbol of the pair
let to = "to_example"; // String | To Symbol of the pair
apiInstance.v1LastQuoteCurrenciesFromToGet(from, to, (error, data, response) => {
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
 **from** | **String**| From Symbol of the pair | 
 **to** | **String**| To Symbol of the pair | 

### Return type

[**V1LastQuoteCurrenciesFromToGet200Response**](V1LastQuoteCurrenciesFromToGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

