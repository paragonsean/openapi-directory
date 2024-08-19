# Endpoints.DefaultApi

All URIs are relative to *https://api.tokenmetrics.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**correlation**](DefaultApi.md#correlation) | **GET** /v1/correlation | Correlation
[**indices**](DefaultApi.md#indices) | **GET** /v1/indices | Indices
[**investorGrades**](DefaultApi.md#investorGrades) | **GET** /v1/investor-grades | Investor Grades
[**marketIndicator**](DefaultApi.md#marketIndicator) | **GET** /v1/market-indicator | Market Indicator
[**price**](DefaultApi.md#price) | **GET** /v1/price | Price
[**pricePrediction**](DefaultApi.md#pricePrediction) | **GET** /v1/price-prediction | Price Prediction
[**quantmetricsTier1**](DefaultApi.md#quantmetricsTier1) | **GET** /v1/quantmetrics-tier-1 | Quantmetrics Tier 1
[**quantmetricsTier2**](DefaultApi.md#quantmetricsTier2) | **GET** /v1/quantmetrics-tier-2 | Quantmetrics Tier 2
[**resistanceSupport**](DefaultApi.md#resistanceSupport) | **GET** /v1/resistance-support | Resistance &amp; Support
[**scenarioAnalysis**](DefaultApi.md#scenarioAnalysis) | **GET** /v1/scenario-analysis | Scenario Analysis
[**sentiments**](DefaultApi.md#sentiments) | **GET** /v1/sentiments | Sentiments
[**tokens**](DefaultApi.md#tokens) | **GET** /v1/tokens | Tokens
[**traderGrades**](DefaultApi.md#traderGrades) | **GET** /v1/trader-grades | Trader Grades
[**tradingIndicator**](DefaultApi.md#tradingIndicator) | **GET** /v1/trading-indicator | Trading Indicator



## correlation

> correlation(opts)

Correlation

Correlation

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'tokens': "3375, 3306", // String | 
  'limit': "1000" // String | 
};
apiInstance.correlation(opts, (error, data, response) => {
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
 **tokens** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## indices

> indices(opts)

Indices

Indices

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'exchanges': "binance", // String | 
  'timeHorizon': "daily", // String | 
  'lowCap': "true", // String | 
  'startDate': "2023-01-10", // String | 
  'endDate': "2023-01-11", // String | 
  'limit': "1000" // String | 
};
apiInstance.indices(opts, (error, data, response) => {
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
 **exchanges** | **String**|  | [optional] 
 **timeHorizon** | **String**|  | [optional] 
 **lowCap** | **String**|  | [optional] 
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## investorGrades

> investorGrades(opts)

Investor Grades

Investor Grades

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'tokens': "3375, 3306", // String | 
  'startDate': "2023-01-10", // String | 
  'endDate': "2023-01-11", // String | 
  'limit': "1000" // String | 
};
apiInstance.investorGrades(opts, (error, data, response) => {
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
 **tokens** | **String**|  | [optional] 
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## marketIndicator

> marketIndicator(opts)

Market Indicator

Market Indicator

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'startDate': "2023-01-10", // String | 
  'endDate': "2023-01-11", // String | 
  'limit': "1000" // String | 
};
apiInstance.marketIndicator(opts, (error, data, response) => {
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
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## price

> price(opts)

Price

Price

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'tokens': "3375, 3306", // String | 
  'startDate': "2023-01-10", // String | 
  'endDate': "2023-01-11", // String | 
  'limit': "1000", // String | 
  'page': "1" // String | 
};
apiInstance.price(opts, (error, data, response) => {
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
 **tokens** | **String**|  | [optional] 
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 
 **page** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## pricePrediction

> pricePrediction(opts)

Price Prediction

Price Prediction

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'tokens': "3375, 3306", // String | 
  'date': "2023-02-01", // String | 
  'limit': "1000" // String | 
};
apiInstance.pricePrediction(opts, (error, data, response) => {
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
 **tokens** | **String**|  | [optional] 
 **date** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## quantmetricsTier1

> quantmetricsTier1(opts)

Quantmetrics Tier 1

Quantmetrics Tier 1

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'tokens': "3375, 3306", // String | 
  'date': "2023-02-01", // String | 
  'limit': "1000" // String | 
};
apiInstance.quantmetricsTier1(opts, (error, data, response) => {
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
 **tokens** | **String**|  | [optional] 
 **date** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## quantmetricsTier2

> quantmetricsTier2(opts)

Quantmetrics Tier 2

Quantmetrics Tier 2

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'tokens': "3375, 3306", // String | 
  'date': "2023-02-01", // String | 
  'limit': "1000" // String | 
};
apiInstance.quantmetricsTier2(opts, (error, data, response) => {
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
 **tokens** | **String**|  | [optional] 
 **date** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resistanceSupport

> resistanceSupport(opts)

Resistance &amp; Support

Resistance &amp; Support

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'tokens': "3375, 3306", // String | 
  'startDate': "2023-01-10", // String | 
  'endDate': "2023-01-11", // String | 
  'limit': "1000" // String | 
};
apiInstance.resistanceSupport(opts, (error, data, response) => {
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
 **tokens** | **String**|  | [optional] 
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## scenarioAnalysis

> scenarioAnalysis(opts)

Scenario Analysis

Scenario Analysis

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'tokens': "3375, 3306", // String | 
  'limit': "1000" // String | 
};
apiInstance.scenarioAnalysis(opts, (error, data, response) => {
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
 **tokens** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sentiments

> sentiments(opts)

Sentiments

Sentiments

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'tokens': "3375, 3306", // String | 
  'startDate': "2023-01-10", // String | 
  'endDate': "2023-01-11", // String | 
  'limit': "1000" // String | 
};
apiInstance.sentiments(opts, (error, data, response) => {
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
 **tokens** | **String**|  | [optional] 
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## tokens

> tokens(opts)

Tokens

Tokens

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'tokenIds': "3375, 3306", // String | 
  'tokenNames': "Hivemapper, Sei_Network, Layer_Zero, Lyra Huobi", // String | 
  'tokenSymbols': "bds, bds, btc" // String | 
};
apiInstance.tokens(opts, (error, data, response) => {
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
 **tokenIds** | **String**|  | [optional] 
 **tokenNames** | **String**|  | [optional] 
 **tokenSymbols** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## traderGrades

> traderGrades(opts)

Trader Grades

Trader Grades

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'tokens': "3375, 3306", // String | 
  'startDate': "2023-01-10", // String | 
  'endDate': "2023-01-11", // String | 
  'limit': "1000" // String | 
};
apiInstance.traderGrades(opts, (error, data, response) => {
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
 **tokens** | **String**|  | [optional] 
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## tradingIndicator

> tradingIndicator(opts)

Trading Indicator

Trading Indicator

### Example

```javascript
import Endpoints from 'endpoints';

let apiInstance = new Endpoints.DefaultApi();
let opts = {
  'tokens': "3375, 3306", // String | 
  'limit': "1000" // String | 
};
apiInstance.tradingIndicator(opts, (error, data, response) => {
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
 **tokens** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

