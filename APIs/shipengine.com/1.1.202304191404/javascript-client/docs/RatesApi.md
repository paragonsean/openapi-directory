# ShipEngineApi.RatesApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculateRates**](RatesApi.md#calculateRates) | **POST** /v1/rates | Get Shipping Rates
[**compareBulkRates**](RatesApi.md#compareBulkRates) | **POST** /v1/rates/bulk | Get Bulk Rates
[**estimateRates**](RatesApi.md#estimateRates) | **POST** /v1/rates/estimate | Estimate Rates
[**getRateById**](RatesApi.md#getRateById) | **GET** /v1/rates/{rate_id} | Get Rate By ID



## calculateRates

> CalculateRatesResponseBody calculateRates(calculateRatesRequestBody)

Get Shipping Rates

It&#39;s not uncommon that you want to give your customer the choice between whether they want to ship the fastest, cheapest, or the most trusted route. Most companies don&#39;t solely ship things using a single shipping option; so we provide functionality to show you all your options! 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.RatesApi();
let calculateRatesRequestBody = new ShipEngineApi.CalculateRatesRequestBody(); // CalculateRatesRequestBody | 
apiInstance.calculateRates(calculateRatesRequestBody, (error, data, response) => {
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
 **calculateRatesRequestBody** | [**CalculateRatesRequestBody**](CalculateRatesRequestBody.md)|  | 

### Return type

[**CalculateRatesResponseBody**](CalculateRatesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## compareBulkRates

> [BulkRate] compareBulkRates(compareBulkRatesRequestBody)

Get Bulk Rates

Get Bulk Shipment Rates

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.RatesApi();
let compareBulkRatesRequestBody = new ShipEngineApi.CompareBulkRatesRequestBody(); // CompareBulkRatesRequestBody | 
apiInstance.compareBulkRates(compareBulkRatesRequestBody, (error, data, response) => {
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
 **compareBulkRatesRequestBody** | [**CompareBulkRatesRequestBody**](CompareBulkRatesRequestBody.md)|  | 

### Return type

[**[BulkRate]**](BulkRate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## estimateRates

> [RateEstimate] estimateRates(estimateRatesRequestBody)

Estimate Rates

Get Rate Estimates

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.RatesApi();
let estimateRatesRequestBody = new ShipEngineApi.EstimateRatesRequestBody(); // EstimateRatesRequestBody | 
apiInstance.estimateRates(estimateRatesRequestBody, (error, data, response) => {
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
 **estimateRatesRequestBody** | [**EstimateRatesRequestBody**](EstimateRatesRequestBody.md)|  | 

### Return type

[**[RateEstimate]**](RateEstimate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getRateById

> GetRateByIdResponseBody getRateById(rateId)

Get Rate By ID

Retrieve a previously queried rate by its ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.RatesApi();
let rateId = "rateId_example"; // String | Rate ID
apiInstance.getRateById(rateId, (error, data, response) => {
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
 **rateId** | **String**| Rate ID | 

### Return type

[**GetRateByIdResponseBody**](GetRateByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

