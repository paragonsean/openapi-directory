# TradematicCloudApi.AutofollowAPIApi

All URIs are relative to *https://api.tradematic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autofollowStrategiesGet**](AutofollowAPIApi.md#autofollowStrategiesGet) | **GET** /autofollow/strategies | Get autofollow strategies list
[**autofollowStrategiesPost**](AutofollowAPIApi.md#autofollowStrategiesPost) | **POST** /autofollow/strategies | Create new autofollow strategy
[**autofollowStrategiesStrategyidContentPut**](AutofollowAPIApi.md#autofollowStrategiesStrategyidContentPut) | **PUT** /autofollow/strategies/{strategyid}/content | Update rules for strategy that was created with strategy builder
[**autofollowStrategiesStrategyidGet**](AutofollowAPIApi.md#autofollowStrategiesStrategyidGet) | **GET** /autofollow/strategies/{strategyid} | Get autofollow strategy by ID
[**autofollowStrategiesStrategyidPositionsGet**](AutofollowAPIApi.md#autofollowStrategiesStrategyidPositionsGet) | **GET** /autofollow/strategies/{strategyid}/positions | Get positions for strategy
[**autofollowStrategiesStrategyidPut**](AutofollowAPIApi.md#autofollowStrategiesStrategyidPut) | **PUT** /autofollow/strategies/{strategyid} | Update autofollow strategy
[**autofollowStrategiesStrategyidSignalsGet**](AutofollowAPIApi.md#autofollowStrategiesStrategyidSignalsGet) | **GET** /autofollow/strategies/{strategyid}/signals | Get trading signals for strategy
[**autofollowStrategiesStrategyidSignalsPost**](AutofollowAPIApi.md#autofollowStrategiesStrategyidSignalsPost) | **POST** /autofollow/strategies/{strategyid}/signals | Send a new signal for autofollow strategy



## autofollowStrategiesGet

> [Strategy] autofollowStrategiesGet()

Get autofollow strategies list

Get autofollow strategies list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.AutofollowAPIApi();
apiInstance.autofollowStrategiesGet((error, data, response) => {
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

[**[Strategy]**](Strategy.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autofollowStrategiesPost

> AutofollowStrategiesPost200Response autofollowStrategiesPost(body)

Create new autofollow strategy

Create new autofollow strategy

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.AutofollowAPIApi();
let body = new TradematicCloudApi.AutofollowStrategiesPostRequest(); // AutofollowStrategiesPostRequest | 
apiInstance.autofollowStrategiesPost(body, (error, data, response) => {
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
 **body** | [**AutofollowStrategiesPostRequest**](AutofollowStrategiesPostRequest.md)|  | 

### Return type

[**AutofollowStrategiesPost200Response**](AutofollowStrategiesPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autofollowStrategiesStrategyidContentPut

> AutofollowStrategiesStrategyidContentPut200Response autofollowStrategiesStrategyidContentPut(strategyid, body)

Update rules for strategy that was created with strategy builder

Update rules for strategy that was created with strategy builder

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.AutofollowAPIApi();
let strategyid = 789; // Number | 
let body = new TradematicCloudApi.AutofollowStrategiesStrategyidContentPutRequest(); // AutofollowStrategiesStrategyidContentPutRequest | 
apiInstance.autofollowStrategiesStrategyidContentPut(strategyid, body, (error, data, response) => {
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
 **strategyid** | **Number**|  | 
 **body** | [**AutofollowStrategiesStrategyidContentPutRequest**](AutofollowStrategiesStrategyidContentPutRequest.md)|  | 

### Return type

[**AutofollowStrategiesStrategyidContentPut200Response**](AutofollowStrategiesStrategyidContentPut200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autofollowStrategiesStrategyidGet

> Strategy autofollowStrategiesStrategyidGet(strategyid)

Get autofollow strategy by ID

Get autofollow strategy by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.AutofollowAPIApi();
let strategyid = 789; // Number | 
apiInstance.autofollowStrategiesStrategyidGet(strategyid, (error, data, response) => {
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
 **strategyid** | **Number**|  | 

### Return type

[**Strategy**](Strategy.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autofollowStrategiesStrategyidPositionsGet

> [StrategyPosition] autofollowStrategiesStrategyidPositionsGet(strategyid)

Get positions for strategy

Get positions for strategy

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.AutofollowAPIApi();
let strategyid = 789; // Number | 
apiInstance.autofollowStrategiesStrategyidPositionsGet(strategyid, (error, data, response) => {
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
 **strategyid** | **Number**|  | 

### Return type

[**[StrategyPosition]**](StrategyPosition.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autofollowStrategiesStrategyidPut

> AutofollowStrategiesStrategyidPut200Response autofollowStrategiesStrategyidPut(strategyid, body)

Update autofollow strategy

Update autofollow strategy

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.AutofollowAPIApi();
let strategyid = 789; // Number | 
let body = new TradematicCloudApi.AutofollowStrategiesStrategyidPutRequest(); // AutofollowStrategiesStrategyidPutRequest | 
apiInstance.autofollowStrategiesStrategyidPut(strategyid, body, (error, data, response) => {
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
 **strategyid** | **Number**|  | 
 **body** | [**AutofollowStrategiesStrategyidPutRequest**](AutofollowStrategiesStrategyidPutRequest.md)|  | 

### Return type

[**AutofollowStrategiesStrategyidPut200Response**](AutofollowStrategiesStrategyidPut200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autofollowStrategiesStrategyidSignalsGet

> [Signal] autofollowStrategiesStrategyidSignalsGet(strategyid, count)

Get trading signals for strategy

Get trading signals for strategy

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.AutofollowAPIApi();
let strategyid = 789; // Number | 
let count = 789; // Number | 
apiInstance.autofollowStrategiesStrategyidSignalsGet(strategyid, count, (error, data, response) => {
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
 **strategyid** | **Number**|  | 
 **count** | **Number**|  | 

### Return type

[**[Signal]**](Signal.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autofollowStrategiesStrategyidSignalsPost

> AutofollowStrategiesStrategyidSignalsPost200Response autofollowStrategiesStrategyidSignalsPost(strategyid, body)

Send a new signal for autofollow strategy

Send a new signal for autofollow strategy

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.AutofollowAPIApi();
let strategyid = 789; // Number | 
let body = new TradematicCloudApi.AutofollowStrategiesStrategyidSignalsPostRequest(); // AutofollowStrategiesStrategyidSignalsPostRequest | 
apiInstance.autofollowStrategiesStrategyidSignalsPost(strategyid, body, (error, data, response) => {
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
 **strategyid** | **Number**|  | 
 **body** | [**AutofollowStrategiesStrategyidSignalsPostRequest**](AutofollowStrategiesStrategyidSignalsPostRequest.md)|  | 

### Return type

[**AutofollowStrategiesStrategyidSignalsPost200Response**](AutofollowStrategiesStrategyidSignalsPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

