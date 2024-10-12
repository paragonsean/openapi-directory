# Ibkr3rdPartyWebApi.OrderMarginRequirementsApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsAccountOrderImpactPost**](OrderMarginRequirementsApi.md#accountsAccountOrderImpactPost) | **POST** /accounts/{account}/order_impact | Return margin impact info



## accountsAccountOrderImpactPost

> AccountsAccountOrderImpactPost200Response accountsAccountOrderImpactPost(account, accountsAccountOrderImpactPostRequest)

Return margin impact info

This endpoint allows the consumer to check the impact that an order would have on the account, including margin, NLV and estimated commission costs. To specify the contract, you provide a value for the ContractId field, OR Ticker/ListingExchange/InstrumentType&#x3D;STK for stocks OR Ticker/Currency/InstrumentType&#x3D;CASH for FX. 

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.OrderMarginRequirementsApi();
let account = "account_example"; // String | Account Number
let accountsAccountOrderImpactPostRequest = new Ibkr3rdPartyWebApi.AccountsAccountOrderImpactPostRequest(); // AccountsAccountOrderImpactPostRequest | Order Parameters
apiInstance.accountsAccountOrderImpactPost(account, accountsAccountOrderImpactPostRequest, (error, data, response) => {
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
 **accountsAccountOrderImpactPostRequest** | [**AccountsAccountOrderImpactPostRequest**](AccountsAccountOrderImpactPostRequest.md)| Order Parameters | 

### Return type

[**AccountsAccountOrderImpactPost200Response**](AccountsAccountOrderImpactPost200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

