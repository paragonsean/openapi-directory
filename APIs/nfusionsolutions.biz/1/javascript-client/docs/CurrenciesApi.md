# NFusionSolutionsMarketDataApi.CurrenciesApi

All URIs are relative to *https://api.nfusionsolutions.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currenciesHistoryGET**](CurrenciesApi.md#currenciesHistoryGET) | **GET** /api/v1/Currencies/history | Get historical prices for requested currency pairs
[**currenciesRateGET**](CurrenciesApi.md#currenciesRateGET) | **GET** /api/v1/Currencies/rate | Get latest mid rate for requested currency pairs
[**currenciesSummaryGET**](CurrenciesApi.md#currenciesSummaryGET) | **GET** /api/v1/Currencies/summary | Get latest Summary for requested currency pairs
[**currenciesSupportedCurrenciesHistoryGET**](CurrenciesApi.md#currenciesSupportedCurrenciesHistoryGET) | **GET** /api/v1/Currencies/history/supported | Get list of currency pairs supported by the history endpoint
[**currenciesSupportedCurrenciesRateGET**](CurrenciesApi.md#currenciesSupportedCurrenciesRateGET) | **GET** /api/v1/Currencies/rate/supported | Get list of currencies supported by the rate endpoint
[**currenciesSupportedCurrenciesSummaryGET**](CurrenciesApi.md#currenciesSupportedCurrenciesSummaryGET) | **GET** /api/v1/Currencies/summary/supported | Get list of currency pairs supported by the Summary endpoint



## currenciesHistoryGET

> [IntervalCollectionResponse] currenciesHistoryGET(pairs, start, opts)

Get historical prices for requested currency pairs

Historical OHLC data for the specified period and interval size    The combination of the interval parameter and start and end dates can result in results  being truncated to conform to result size limits. See comments on interval parameter for details on valid interval values.

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.CurrenciesApi();
let pairs = "pairs_example"; // String | comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | start date of time period. format is <i>yyyy-mm-dd</i>
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | end date of time period. format is <i>yyyy-mm-dd</i>. Default is current date.
  'interval': "interval_example", // String | aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y=year,  m=month,  w=week,  d=day,  h=hour,  mi=minute    For example, a yearly interval can be specified as \"y\" and 6 month interval as \"6m\".     If not specified the interval parameter default is 1 Day.
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.currenciesHistoryGET(pairs, start, opts, (error, data, response) => {
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
 **pairs** | **String**| comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD | 
 **start** | **Date**| start date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt; | 
 **end** | **Date**| end date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt;. Default is current date. | [optional] 
 **interval** | **String**| aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y&#x3D;year,  m&#x3D;month,  w&#x3D;week,  d&#x3D;day,  h&#x3D;hour,  mi&#x3D;minute    For example, a yearly interval can be specified as \&quot;y\&quot; and 6 month interval as \&quot;6m\&quot;.     If not specified the interval parameter default is 1 Day. | [optional] 
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 

### Return type

[**[IntervalCollectionResponse]**](IntervalCollectionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## currenciesRateGET

> [RateResponse] currenciesRateGET(pairs, opts)

Get latest mid rate for requested currency pairs

Current Mid Rate

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.CurrenciesApi();
let pairs = "pairs_example"; // String | comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD
let opts = {
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.currenciesRateGET(pairs, opts, (error, data, response) => {
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
 **pairs** | **String**| comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD | 
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 

### Return type

[**[RateResponse]**](RateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## currenciesSummaryGET

> [SummaryResponse] currenciesSummaryGET(pairs, opts)

Get latest Summary for requested currency pairs

Current and daily summary information combined into a single quote

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.CurrenciesApi();
let pairs = "pairs_example"; // String | comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD
let opts = {
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.currenciesSummaryGET(pairs, opts, (error, data, response) => {
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
 **pairs** | **String**| comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD | 
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 

### Return type

[**[SummaryResponse]**](SummaryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## currenciesSupportedCurrenciesHistoryGET

> [String] currenciesSupportedCurrenciesHistoryGET(opts)

Get list of currency pairs supported by the history endpoint

Only the currency pairs in the direction noted can be used with the history endpoint.  For example: USD/CAD is not the same as CAD/USD

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.CurrenciesApi();
let opts = {
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.currenciesSupportedCurrenciesHistoryGET(opts, (error, data, response) => {
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
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 

### Return type

**[String]**

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## currenciesSupportedCurrenciesRateGET

> [String] currenciesSupportedCurrenciesRateGET(opts)

Get list of currencies supported by the rate endpoint

Any of the currencies in this list can be paired with any other currency in this list when supplied to the Rate endpoint.  For example: USD/CAD,CAD/USD,USD/EUR,EUR/CAD

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.CurrenciesApi();
let opts = {
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.currenciesSupportedCurrenciesRateGET(opts, (error, data, response) => {
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
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 

### Return type

**[String]**

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## currenciesSupportedCurrenciesSummaryGET

> [String] currenciesSupportedCurrenciesSummaryGET(opts)

Get list of currency pairs supported by the Summary endpoint

Only the currency pairs in the direction noted can be used with the Summary endpoint.  For example: USD/CAD is not the same as CAD/USD

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.CurrenciesApi();
let opts = {
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.currenciesSupportedCurrenciesSummaryGET(opts, (error, data, response) => {
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
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 

### Return type

**[String]**

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

