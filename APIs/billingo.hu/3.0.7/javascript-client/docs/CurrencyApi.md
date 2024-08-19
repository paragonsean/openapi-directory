# BillingoApiV3.CurrencyApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConversionRate**](CurrencyApi.md#getConversionRate) | **GET** /currencies | Get currencies exchange rate.



## getConversionRate

> ConversationRate getConversionRate(from, to)

Get currencies exchange rate.

Return with the exchange value of given currencies.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.CurrencyApi();
let from = new BillingoApiV3.Currency(); // Currency | 
let to = new BillingoApiV3.Currency(); // Currency | 
apiInstance.getConversionRate(from, to, (error, data, response) => {
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
 **from** | [**Currency**](.md)|  | 
 **to** | [**Currency**](.md)|  | 

### Return type

[**ConversationRate**](ConversationRate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

