# Polygon.StocksApi

All URIs are relative to *https://api.polygon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CompaniesGet**](StocksApi.md#v1CompaniesGet) | **GET** /v1/companies | Available Companies
[**v1HistoricAggSizeSymbolDateGet**](StocksApi.md#v1HistoricAggSizeSymbolDateGet) | **GET** /v1/historic/agg/{size}/{symbol}/{date} | Historic Aggregates
[**v1HistoricQuotesSymbolDateGet**](StocksApi.md#v1HistoricQuotesSymbolDateGet) | **GET** /v1/historic/quotes/{symbol}/{date} | Historic Quotes
[**v1HistoricTradesSymbolDateGet**](StocksApi.md#v1HistoricTradesSymbolDateGet) | **GET** /v1/historic/trades/{symbol}/{date} | Historic Trades
[**v1LastQuoteStocksSymbolGet**](StocksApi.md#v1LastQuoteStocksSymbolGet) | **GET** /v1/last_quote/stocks/{symbol} | Last Quote for a Symbol
[**v1LastStocksSymbolGet**](StocksApi.md#v1LastStocksSymbolGet) | **GET** /v1/last/stocks/{symbol} | Last Trade for a Symbol



## v1CompaniesGet

> [Company] v1CompaniesGet(opts)

Available Companies

Get a list of the traded companies that polygon.io streams. Company includes some details about the company which we hope to add more to soon. 

### Example

```javascript
import Polygon from 'polygon';
let defaultClient = Polygon.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Polygon.StocksApi();
let opts = {
  'sort': "sort_example", // String | Which field to sort by. For desc place a `-` in front of the field name. eg `?sort=-marketcap`
  'perpage': 3.4, // Number | How many items to be on each page during pagination
  'page': 1.0 // Number | Which page of results to return
};
apiInstance.v1CompaniesGet(opts, (error, data, response) => {
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
 **sort** | **String**| Which field to sort by. For desc place a &#x60;-&#x60; in front of the field name. eg &#x60;?sort&#x3D;-marketcap&#x60; | [optional] 
 **perpage** | **Number**| How many items to be on each page during pagination | [optional] 
 **page** | **Number**| Which page of results to return | [optional] [default to 1.0]

### Return type

[**[Company]**](Company.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v1HistoricAggSizeSymbolDateGet

> V1HistoricAggSizeSymbolDateGet200Response v1HistoricAggSizeSymbolDateGet(size, symbol, date, opts)

Historic Aggregates

Get historic aggregations for a symbol. 

### Example

```javascript
import Polygon from 'polygon';
let defaultClient = Polygon.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Polygon.StocksApi();
let size = "size_example"; // String | Size of the aggregation. `second` or `minute`
let symbol = "symbol_example"; // String | Symbol of the company to retrieve
let date = new Date("2013-10-20"); // Date | Date/Day of the historic ticks to retreive
let opts = {
  'offset': 56, // Number | Timestamp offset, used for pagination
  'limit': 100 // Number | Limit the size of response, max: 10000
};
apiInstance.v1HistoricAggSizeSymbolDateGet(size, symbol, date, opts, (error, data, response) => {
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
 **size** | **String**| Size of the aggregation. &#x60;second&#x60; or &#x60;minute&#x60; | 
 **symbol** | **String**| Symbol of the company to retrieve | 
 **date** | **Date**| Date/Day of the historic ticks to retreive | 
 **offset** | **Number**| Timestamp offset, used for pagination | [optional] 
 **limit** | **Number**| Limit the size of response, max: 10000 | [optional] [default to 100]

### Return type

[**V1HistoricAggSizeSymbolDateGet200Response**](V1HistoricAggSizeSymbolDateGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v1HistoricQuotesSymbolDateGet

> V1HistoricQuotesSymbolDateGet200Response v1HistoricQuotesSymbolDateGet(symbol, date, opts)

Historic Quotes

Get historic quotes for a symbol. 

### Example

```javascript
import Polygon from 'polygon';
let defaultClient = Polygon.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Polygon.StocksApi();
let symbol = "symbol_example"; // String | Symbol of the company to retrieve
let date = new Date("2013-10-20"); // Date | Date/Day of the historic ticks to retreive
let opts = {
  'offset': 56, // Number | Timestamp offset, used for pagination
  'limit': 100 // Number | Limit the size of response, max: 10000
};
apiInstance.v1HistoricQuotesSymbolDateGet(symbol, date, opts, (error, data, response) => {
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
 **symbol** | **String**| Symbol of the company to retrieve | 
 **date** | **Date**| Date/Day of the historic ticks to retreive | 
 **offset** | **Number**| Timestamp offset, used for pagination | [optional] 
 **limit** | **Number**| Limit the size of response, max: 10000 | [optional] [default to 100]

### Return type

[**V1HistoricQuotesSymbolDateGet200Response**](V1HistoricQuotesSymbolDateGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v1HistoricTradesSymbolDateGet

> V1HistoricTradesSymbolDateGet200Response v1HistoricTradesSymbolDateGet(symbol, date, opts)

Historic Trades

Get historic trades for a symbol. 

### Example

```javascript
import Polygon from 'polygon';
let defaultClient = Polygon.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Polygon.StocksApi();
let symbol = "symbol_example"; // String | Symbol of the company to retrieve
let date = new Date("2013-10-20"); // Date | Date/Day of the historic ticks to retreive
let opts = {
  'offset': 56, // Number | Timestamp offset, used for pagination
  'limit': 100 // Number | Limit the size of response, max: 10000
};
apiInstance.v1HistoricTradesSymbolDateGet(symbol, date, opts, (error, data, response) => {
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
 **symbol** | **String**| Symbol of the company to retrieve | 
 **date** | **Date**| Date/Day of the historic ticks to retreive | 
 **offset** | **Number**| Timestamp offset, used for pagination | [optional] 
 **limit** | **Number**| Limit the size of response, max: 10000 | [optional] [default to 100]

### Return type

[**V1HistoricTradesSymbolDateGet200Response**](V1HistoricTradesSymbolDateGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v1LastQuoteStocksSymbolGet

> V1LastQuoteStocksSymbolGet200Response v1LastQuoteStocksSymbolGet(symbol)

Last Quote for a Symbol

Get the last quote tick for a given stock. 

### Example

```javascript
import Polygon from 'polygon';
let defaultClient = Polygon.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Polygon.StocksApi();
let symbol = "symbol_example"; // String | Symbol of the stock to get
apiInstance.v1LastQuoteStocksSymbolGet(symbol, (error, data, response) => {
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
 **symbol** | **String**| Symbol of the stock to get | 

### Return type

[**V1LastQuoteStocksSymbolGet200Response**](V1LastQuoteStocksSymbolGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v1LastStocksSymbolGet

> V1LastStocksSymbolGet200Response v1LastStocksSymbolGet(symbol)

Last Trade for a Symbol

Get the last trade for a given stock. 

### Example

```javascript
import Polygon from 'polygon';
let defaultClient = Polygon.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Polygon.StocksApi();
let symbol = "symbol_example"; // String | Symbol of the stock to get
apiInstance.v1LastStocksSymbolGet(symbol, (error, data, response) => {
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
 **symbol** | **String**| Symbol of the stock to get | 

### Return type

[**V1LastStocksSymbolGet200Response**](V1LastStocksSymbolGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

