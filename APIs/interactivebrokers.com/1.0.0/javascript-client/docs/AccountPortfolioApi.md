# Ibkr3rdPartyWebApi.AccountPortfolioApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsAccountPositionsGet**](AccountPortfolioApi.md#accountsAccountPositionsGet) | **GET** /accounts/{account}/positions | Account Positions
[**accountsAccountSummaryGet**](AccountPortfolioApi.md#accountsAccountSummaryGet) | **GET** /accounts/{account}/summary | Account Values Summary
[**accountsGet**](AccountPortfolioApi.md#accountsGet) | **GET** /accounts | Brokerage Accounts



## accountsAccountPositionsGet

> [AccountsAccountPositionsGet200ResponseInner] accountsAccountPositionsGet(account)

Account Positions

Returns a list of positions for the indicated account. 

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.AccountPortfolioApi();
let account = "account_example"; // String | Account Number
apiInstance.accountsAccountPositionsGet(account, (error, data, response) => {
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
 **account** | **String**| Account Number | 

### Return type

[**[AccountsAccountPositionsGet200ResponseInner]**](AccountsAccountPositionsGet200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsAccountSummaryGet

> AccountsAccountSummaryGet200Response accountsAccountSummaryGet(account)

Account Values Summary

Returns a list of account and margin balances associated with the account passed in the URL

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.AccountPortfolioApi();
let account = "account_example"; // String | Account Number
apiInstance.accountsAccountSummaryGet(account, (error, data, response) => {
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
 **account** | **String**| Account Number | 

### Return type

[**AccountsAccountSummaryGet200Response**](AccountsAccountSummaryGet200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsGet

> AccountsGet200Response accountsGet(account)

Brokerage Accounts

Allows the caller to request a list of accounts associated with the session.

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.AccountPortfolioApi();
let account = "account_example"; // String | Account Number
apiInstance.accountsGet(account, (error, data, response) => {
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
 **account** | **String**| Account Number | 

### Return type

[**AccountsGet200Response**](AccountsGet200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

