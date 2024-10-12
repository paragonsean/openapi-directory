# Ibkr3rdPartyWebApi.TradesApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsAccountTradesGet**](TradesApi.md#accountsAccountTradesGet) | **GET** /accounts/{account}/trades | Returns trades in account



## accountsAccountTradesGet

> [AccountsAccountTradesGet200ResponseInner] accountsAccountTradesGet(account, opts)

Returns trades in account

Returns a list of trades for the account starting at the given &#39;since&#39; date to the current time (now()). Timezone is UTC. Any request with a future since date or going further than one week will result in an HTTP 400 bad request response. Calling /trades without since will return all trades for the past 24 hours. 

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.TradesApi();
let account = "account_example"; // String | Account Number
let opts = {
  'body': "body_example" // String | Start time specified in UTC. Allowed formats are \"yyyy-MM-dd\" or \"yyyy-MM-dd'T'HH:mm:ss\". Time is optional and is set to midnight if omitted, e.g. \"00:00:00 hh:mm:ss\". 
};
apiInstance.accountsAccountTradesGet(account, opts, (error, data, response) => {
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
 **body** | **String**| Start time specified in UTC. Allowed formats are \&quot;yyyy-MM-dd\&quot; or \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;. Time is optional and is set to midnight if omitted, e.g. \&quot;00:00:00 hh:mm:ss\&quot;.  | [optional] 

### Return type

[**[AccountsAccountTradesGet200ResponseInner]**](AccountsAccountTradesGet200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

