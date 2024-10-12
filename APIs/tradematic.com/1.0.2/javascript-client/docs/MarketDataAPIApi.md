# TradematicCloudApi.MarketDataAPIApi

All URIs are relative to *https://api.tradematic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketdataMarketsGet**](MarketDataAPIApi.md#marketdataMarketsGet) | **GET** /marketdata/markets | Get markets list
[**marketdataMarketsMarketidGet**](MarketDataAPIApi.md#marketdataMarketsMarketidGet) | **GET** /marketdata/markets/{marketid} | Get market by ID
[**marketdataSymbolsGet**](MarketDataAPIApi.md#marketdataSymbolsGet) | **GET** /marketdata/symbols | Get symbols list
[**marketdataSymbolsSymbolidGet**](MarketDataAPIApi.md#marketdataSymbolsSymbolidGet) | **GET** /marketdata/symbols/{symbolid} | Get symbol by ID
[**marketdataSymbolsSymbolidHistdataGet**](MarketDataAPIApi.md#marketdataSymbolsSymbolidHistdataGet) | **GET** /marketdata/symbols/{symbolid}/histdata | Get historical data for instrument



## marketdataMarketsGet

> [Market] marketdataMarketsGet()

Get markets list

Get markets list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.MarketDataAPIApi();
apiInstance.marketdataMarketsGet((error, data, response) => {
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

[**[Market]**](Market.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketdataMarketsMarketidGet

> Market marketdataMarketsMarketidGet(marketid)

Get market by ID

Get market by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.MarketDataAPIApi();
let marketid = 789; // Number | 
apiInstance.marketdataMarketsMarketidGet(marketid, (error, data, response) => {
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
 **marketid** | **Number**|  | 

### Return type

[**Market**](Market.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketdataSymbolsGet

> [String] marketdataSymbolsGet(marketid, filter)

Get symbols list

Get symbols list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.MarketDataAPIApi();
let marketid = 789; // Number | 
let filter = 789; // Number | 
apiInstance.marketdataSymbolsGet(marketid, filter, (error, data, response) => {
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
 **marketid** | **Number**|  | 
 **filter** | **Number**|  | 

### Return type

**[String]**

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketdataSymbolsSymbolidGet

> String marketdataSymbolsSymbolidGet(symbolid)

Get symbol by ID

Get symbol by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.MarketDataAPIApi();
let symbolid = 789; // Number | 
apiInstance.marketdataSymbolsSymbolidGet(symbolid, (error, data, response) => {
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
 **symbolid** | **Number**|  | 

### Return type

**String**

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketdataSymbolsSymbolidHistdataGet

> MarketdataSymbolsSymbolidHistdataGet200Response marketdataSymbolsSymbolidHistdataGet(symbolid, tf, from, to)

Get historical data for instrument

Get historical data for instrument

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.MarketDataAPIApi();
let symbolid = 789; // Number | 
let tf = 789; // Number | 
let from = 789; // Number | 
let to = 789; // Number | 
apiInstance.marketdataSymbolsSymbolidHistdataGet(symbolid, tf, from, to, (error, data, response) => {
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
 **symbolid** | **Number**|  | 
 **tf** | **Number**|  | 
 **from** | **Number**|  | 
 **to** | **Number**|  | 

### Return type

[**MarketdataSymbolsSymbolidHistdataGet200Response**](MarketdataSymbolsSymbolidHistdataGet200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

