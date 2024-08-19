# NFusionSolutionsMarketDataApi.MetalsApi

All URIs are relative to *https://api.nfusionsolutions.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metalsBenchmarkHistoryGET**](MetalsApi.md#metalsBenchmarkHistoryGET) | **GET** /api/v1/Metals/benchmark/history | Get historical benchmark prices for requested metals
[**metalsBenchmarkSummaryGET**](MetalsApi.md#metalsBenchmarkSummaryGET) | **GET** /api/v1/Metals/benchmark/summary | Get latest Benchmark prices for requested metals
[**metalsBenchmarkSupportedMetalsGET**](MetalsApi.md#metalsBenchmarkSupportedMetalsGET) | **GET** /api/v1/Metals/benchmark/supported | Get list of symbols supported by the benchmark endpoints
[**metalsSpotAnnualHistoricalPerformanceGET**](MetalsApi.md#metalsSpotAnnualHistoricalPerformanceGET) | **GET** /api/v1/Metals/spot/performance/annual | Get Historical Annual Performance for requested metals
[**metalsSpotHistoricalPerformanceGET**](MetalsApi.md#metalsSpotHistoricalPerformanceGET) | **GET** /api/v1/Metals/spot/performance | Get Historical Performance for requested metals
[**metalsSpotHistoryGET**](MetalsApi.md#metalsSpotHistoryGET) | **GET** /api/v1/Metals/spot/history | Get historical Spot prices for requested metals
[**metalsSpotRatioHistoryGET**](MetalsApi.md#metalsSpotRatioHistoryGET) | **GET** /api/v1/Metals/spot/ratio/history | Get historical Spot Ratio prices for requested metals
[**metalsSpotRatioSummaryGET**](MetalsApi.md#metalsSpotRatioSummaryGET) | **GET** /api/v1/Metals/spot/ratio/summary | Get latest Spot Summary for requested metal ratios
[**metalsSpotSummaryGET**](MetalsApi.md#metalsSpotSummaryGET) | **GET** /api/v1/Metals/spot/summary | Get latest Spot Summary for requested metals
[**metalsSpotSupportedMetalsGET**](MetalsApi.md#metalsSpotSupportedMetalsGET) | **GET** /api/v1/Metals/spot/supported | Get list of symbols supported by the spot endpoints
[**metalsSupportedCurrenciesMetalsGET**](MetalsApi.md#metalsSupportedCurrenciesMetalsGET) | **GET** /api/v1/Metals/supported/currency | Get list of currencies supported by metals endpoints for currency conversion



## metalsBenchmarkHistoryGET

> [IntervalCollectionResponse] metalsBenchmarkHistoryGET(metals, start, opts)

Get historical benchmark prices for requested metals

Historical OHLC data for the specified period and interval size    The combination of the interval parameter and start and end dates can result in results  being truncated to conform to result size limits. See comments on interval parameter for details on valid interval values.    The historicalfx flag is used to determine whether to apply today&#39;s fx rates to a historical period, or to apply the historical rates from that same time frame.

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.MetalsApi();
let metals = "metals_example"; // String | comma separated list of metals
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | start date of time period. format is <i>yyyy-mm-dd</i>
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | end date of time period. format is <i>yyyy-mm-dd</i>. Default is current date.
  'interval': "interval_example", // String | aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y=year,  m=month,  w=week,  d=day,  h=hour,  mi=minute    For example, a yearly interval can be specified as \"y\" and 6 month interval as \"6m\".     If not specified the interval parameter default is 1 Day.
  'historicalfx': true, // Boolean | if true use historical currency rates otherwise current currency rates. Defaults to true.
  'currency': "currency_example", // String | comma separated list of conversion currencies, defaults to USD
  'unitofmeasure': "unitofmeasure_example", // String | unit of meaure, defaults to troy ounces. allowed values are:  mg=milligram  g=gram  kg=kilogram  gr=grain  oz=ounce  toz=troy ounce  ct=carat  dwt=pennyweight
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.metalsBenchmarkHistoryGET(metals, start, opts, (error, data, response) => {
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
 **metals** | **String**| comma separated list of metals | 
 **start** | **Date**| start date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt; | 
 **end** | **Date**| end date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt;. Default is current date. | [optional] 
 **interval** | **String**| aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y&#x3D;year,  m&#x3D;month,  w&#x3D;week,  d&#x3D;day,  h&#x3D;hour,  mi&#x3D;minute    For example, a yearly interval can be specified as \&quot;y\&quot; and 6 month interval as \&quot;6m\&quot;.     If not specified the interval parameter default is 1 Day. | [optional] 
 **historicalfx** | **Boolean**| if true use historical currency rates otherwise current currency rates. Defaults to true. | [optional] 
 **currency** | **String**| comma separated list of conversion currencies, defaults to USD | [optional] 
 **unitofmeasure** | **String**| unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight | [optional] 
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 

### Return type

[**[IntervalCollectionResponse]**](IntervalCollectionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## metalsBenchmarkSummaryGET

> [SummaryResponse] metalsBenchmarkSummaryGET(metals, opts)

Get latest Benchmark prices for requested metals

Benchmark price information

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.MetalsApi();
let metals = "metals_example"; // String | comma separated list of metals
let opts = {
  'currency': "currency_example", // String | comma separated list of conversion currencies, defaults to USD
  'unitofmeasure': "unitofmeasure_example", // String | unit of meaure, defaults to troy ounces. allowed values are:  mg=milligram  g=gram  kg=kilogram  gr=grain  oz=ounce  toz=troy ounce  ct=carat  dwt=pennyweight
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.metalsBenchmarkSummaryGET(metals, opts, (error, data, response) => {
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
 **metals** | **String**| comma separated list of metals | 
 **currency** | **String**| comma separated list of conversion currencies, defaults to USD | [optional] 
 **unitofmeasure** | **String**| unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight | [optional] 
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 

### Return type

[**[SummaryResponse]**](SummaryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## metalsBenchmarkSupportedMetalsGET

> [String] metalsBenchmarkSupportedMetalsGET(opts)

Get list of symbols supported by the benchmark endpoints



### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.MetalsApi();
let opts = {
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.metalsBenchmarkSupportedMetalsGET(opts, (error, data, response) => {
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


## metalsSpotAnnualHistoricalPerformanceGET

> [IntervalCollectionResponse] metalsSpotAnnualHistoricalPerformanceGET(metals, opts)

Get Historical Annual Performance for requested metals

Annual Historical Performance information

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.MetalsApi();
let metals = "metals_example"; // String | comma separated list of metals
let opts = {
  'currency': "currency_example", // String | comma separated list of conversion currencies, defaults to USD
  'unitofmeasure': "unitofmeasure_example", // String | unit of meaure, defaults to troy ounces. allowed values are:  mg=milligram  g=gram  kg=kilogram  gr=grain  oz=ounce  toz=troy ounce  ct=carat  dwt=pennyweight
  'format': "format_example", // String | to override content negotiation specify a value of json or xml
  'years': 56 // Number | Number of years of history to return. Defaults to 10.
};
apiInstance.metalsSpotAnnualHistoricalPerformanceGET(metals, opts, (error, data, response) => {
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
 **metals** | **String**| comma separated list of metals | 
 **currency** | **String**| comma separated list of conversion currencies, defaults to USD | [optional] 
 **unitofmeasure** | **String**| unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight | [optional] 
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 
 **years** | **Number**| Number of years of history to return. Defaults to 10. | [optional] 

### Return type

[**[IntervalCollectionResponse]**](IntervalCollectionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## metalsSpotHistoricalPerformanceGET

> [IntervalCollectionResponse] metalsSpotHistoricalPerformanceGET(metals, opts)

Get Historical Performance for requested metals

Historical Performance information

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.MetalsApi();
let metals = "metals_example"; // String | comma separated list of metals
let opts = {
  'currency': "currency_example", // String | comma separated list of conversion currencies, defaults to USD
  'unitofmeasure': "unitofmeasure_example", // String | unit of meaure, defaults to troy ounces. allowed values are:  mg=milligram  g=gram  kg=kilogram  gr=grain  oz=ounce  toz=troy ounce  ct=carat  dwt=pennyweight
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.metalsSpotHistoricalPerformanceGET(metals, opts, (error, data, response) => {
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
 **metals** | **String**| comma separated list of metals | 
 **currency** | **String**| comma separated list of conversion currencies, defaults to USD | [optional] 
 **unitofmeasure** | **String**| unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight | [optional] 
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 

### Return type

[**[IntervalCollectionResponse]**](IntervalCollectionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## metalsSpotHistoryGET

> [IntervalCollectionResponse] metalsSpotHistoryGET(metals, start, opts)

Get historical Spot prices for requested metals

Historical OHLC data for the specified period and interval size    The combination of the interval parameter and start and end dates can result in results  being truncated to conform to result size limits. See comments on interval parameter for details on valid interval values.    The historicalfx flag is used to determine whether to apply today&#39;s fx rates to a historical period, or to apply the historical rates from that same time frame.

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.MetalsApi();
let metals = "metals_example"; // String | comma separated list of metals
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | start date of time period. format is <i>yyyy-mm-dd</i>
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | end date of time period. format is <i>yyyy-mm-dd</i>. Default is current date.
  'interval': "interval_example", // String | aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y=year,  m=month,  w=week,  d=day,  h=hour,  mi=minute    For example, a yearly interval can be specified as \"y\" and 6 month interval as \"6m\".     If not specified the interval parameter default is 1 Day.
  'historicalfx': true, // Boolean | if true use historical currency rates otherwise current currency rates. Defaults to true.
  'currency': "currency_example", // String | comma separated list of conversion currencies, defaults to USD
  'unitofmeasure': "unitofmeasure_example", // String | unit of meaure, defaults to troy ounces. allowed values are:  mg=milligram  g=gram  kg=kilogram  gr=grain  oz=ounce  toz=troy ounce  ct=carat  dwt=pennyweight
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.metalsSpotHistoryGET(metals, start, opts, (error, data, response) => {
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
 **metals** | **String**| comma separated list of metals | 
 **start** | **Date**| start date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt; | 
 **end** | **Date**| end date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt;. Default is current date. | [optional] 
 **interval** | **String**| aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y&#x3D;year,  m&#x3D;month,  w&#x3D;week,  d&#x3D;day,  h&#x3D;hour,  mi&#x3D;minute    For example, a yearly interval can be specified as \&quot;y\&quot; and 6 month interval as \&quot;6m\&quot;.     If not specified the interval parameter default is 1 Day. | [optional] 
 **historicalfx** | **Boolean**| if true use historical currency rates otherwise current currency rates. Defaults to true. | [optional] 
 **currency** | **String**| comma separated list of conversion currencies, defaults to USD | [optional] 
 **unitofmeasure** | **String**| unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight | [optional] 
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 

### Return type

[**[IntervalCollectionResponse]**](IntervalCollectionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## metalsSpotRatioHistoryGET

> [IntervalCollectionResponse] metalsSpotRatioHistoryGET(pairs, start, opts)

Get historical Spot Ratio prices for requested metals

Historical data for the specified period and interval size    The combination of the interval parameter and start and end dates can result in results  being truncated to conform to result size limits. See comments on interval parameter for details on valid interval values.

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.MetalsApi();
let pairs = "pairs_example"; // String | comma separated list of metals
let start = new Date("2013-10-20T19:20:30+01:00"); // Date | start date of time period. format is <i>yyyy-mm-dd</i>
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | end date of time period. format is <i>yyyy-mm-dd</i>. Default is current date.
  'interval': "interval_example", // String | aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y=year,  m=month,  w=week,  d=day,  h=hour,  mi=minute    For example, a yearly interval can be specified as \"y\" and 6 month interval as \"6m\".     If not specified the interval parameter default is 1 Day.
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.metalsSpotRatioHistoryGET(pairs, start, opts, (error, data, response) => {
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
 **pairs** | **String**| comma separated list of metals | 
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


## metalsSpotRatioSummaryGET

> [SummaryResponse] metalsSpotRatioSummaryGET(pairs, opts)

Get latest Spot Summary for requested metal ratios

Ratios between prices of two metals

### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.MetalsApi();
let pairs = "pairs_example"; // String | comma separated list of metal pairs. For example: gold/silver,gold/platinum,silver/palladium
let opts = {
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.metalsSpotRatioSummaryGET(pairs, opts, (error, data, response) => {
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
 **pairs** | **String**| comma separated list of metal pairs. For example: gold/silver,gold/platinum,silver/palladium | 
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 

### Return type

[**[SummaryResponse]**](SummaryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## metalsSpotSummaryGET

> [SummaryResponse] metalsSpotSummaryGET(metals, opts)

Get latest Spot Summary for requested metals

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

let apiInstance = new NFusionSolutionsMarketDataApi.MetalsApi();
let metals = "metals_example"; // String | comma separated list of metals
let opts = {
  'currency': "currency_example", // String | comma separated list of conversion currencies, defaults to USD
  'unitofmeasure': "unitofmeasure_example", // String | unit of meaure, defaults to troy ounces. allowed values are:  mg=milligram  g=gram  kg=kilogram  gr=grain  oz=ounce  toz=troy ounce  ct=carat  dwt=pennyweight
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.metalsSpotSummaryGET(metals, opts, (error, data, response) => {
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
 **metals** | **String**| comma separated list of metals | 
 **currency** | **String**| comma separated list of conversion currencies, defaults to USD | [optional] 
 **unitofmeasure** | **String**| unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight | [optional] 
 **format** | **String**| to override content negotiation specify a value of json or xml | [optional] 

### Return type

[**[SummaryResponse]**](SummaryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## metalsSpotSupportedMetalsGET

> [String] metalsSpotSupportedMetalsGET(opts)

Get list of symbols supported by the spot endpoints



### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.MetalsApi();
let opts = {
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.metalsSpotSupportedMetalsGET(opts, (error, data, response) => {
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


## metalsSupportedCurrenciesMetalsGET

> [String] metalsSupportedCurrenciesMetalsGET(opts)

Get list of currencies supported by metals endpoints for currency conversion



### Example

```javascript
import NFusionSolutionsMarketDataApi from 'n_fusion_solutions_market_data_api';
let defaultClient = NFusionSolutionsMarketDataApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new NFusionSolutionsMarketDataApi.MetalsApi();
let opts = {
  'format': "format_example" // String | to override content negotiation specify a value of json or xml
};
apiInstance.metalsSupportedCurrenciesMetalsGET(opts, (error, data, response) => {
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

