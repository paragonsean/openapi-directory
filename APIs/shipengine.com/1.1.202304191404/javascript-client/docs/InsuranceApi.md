# ShipEngineApi.InsuranceApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addFundsToInsurance**](InsuranceApi.md#addFundsToInsurance) | **PATCH** /v1/insurance/shipsurance/add_funds | Add Funds To Insurance
[**connectInsurer**](InsuranceApi.md#connectInsurer) | **POST** /v1/connections/insurance/shipsurance | Connect a Shipsurance Account
[**disconnectInsurer**](InsuranceApi.md#disconnectInsurer) | **DELETE** /v1/connections/insurance/shipsurance | Disconnect a Shipsurance Account
[**getInsuranceBalance**](InsuranceApi.md#getInsuranceBalance) | **GET** /v1/insurance/shipsurance/balance | Get Insurance Funds Balance



## addFundsToInsurance

> AddFundsToInsuranceResponseBody addFundsToInsurance(addFundsToInsuranceRequestBody)

Add Funds To Insurance

You may need to auto fund your account from time to time. For example, if you don&#39;t normally ship items over $100, and may want to add funds to insurance rather than keeping the account funded. 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.InsuranceApi();
let addFundsToInsuranceRequestBody = new ShipEngineApi.AddFundsToInsuranceRequestBody(); // AddFundsToInsuranceRequestBody | 
apiInstance.addFundsToInsurance(addFundsToInsuranceRequestBody, (error, data, response) => {
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
 **addFundsToInsuranceRequestBody** | [**AddFundsToInsuranceRequestBody**](AddFundsToInsuranceRequestBody.md)|  | 

### Return type

[**AddFundsToInsuranceResponseBody**](AddFundsToInsuranceResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## connectInsurer

> Object connectInsurer(connectInsurerRequestBody)

Connect a Shipsurance Account

Connect a Shipsurance Account

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.InsuranceApi();
let connectInsurerRequestBody = new ShipEngineApi.ConnectInsurerRequestBody(); // ConnectInsurerRequestBody | 
apiInstance.connectInsurer(connectInsurerRequestBody, (error, data, response) => {
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
 **connectInsurerRequestBody** | [**ConnectInsurerRequestBody**](ConnectInsurerRequestBody.md)|  | 

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disconnectInsurer

> Object disconnectInsurer()

Disconnect a Shipsurance Account

Disconnect a Shipsurance Account

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.InsuranceApi();
apiInstance.disconnectInsurer((error, data, response) => {
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

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInsuranceBalance

> GetInsuranceBalanceResponseBody getInsuranceBalance()

Get Insurance Funds Balance

Retrieve the balance of your Shipsurance account.

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.InsuranceApi();
apiInstance.getInsuranceBalance((error, data, response) => {
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

[**GetInsuranceBalanceResponseBody**](GetInsuranceBalanceResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

