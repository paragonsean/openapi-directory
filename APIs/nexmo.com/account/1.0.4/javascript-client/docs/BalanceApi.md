# AccountApi.BalanceApi

All URIs are relative to *https://api.nexmo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAccountBalance**](BalanceApi.md#getAccountBalance) | **GET** /account/get-balance | Get Account Balance
[**topUpAccountBalance**](BalanceApi.md#topUpAccountBalance) | **POST** /account/top-up | Top Up Account Balance



## getAccountBalance

> AccountBalance getAccountBalance(apiKey, apiSecret)

Get Account Balance

Retrieve the current balance of your Vonage API account

### Example

```javascript
import AccountApi from 'account_api';

let apiInstance = new AccountApi.BalanceApi();
let apiKey = "abcd1234"; // String | Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com)
let apiSecret = "ABCDEFGH01234abc"; // String | Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com)
apiInstance.getAccountBalance(apiKey, apiSecret, (error, data, response) => {
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
 **apiKey** | **String**| Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com) | 
 **apiSecret** | **String**| Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com) | 

### Return type

[**AccountBalance**](AccountBalance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## topUpAccountBalance

> Success topUpAccountBalance(apiKey, apiSecret, trx)

Top Up Account Balance

You can top up your account using this API when you have enabled auto-reload in the dashboard. The amount added by the top-up operation will be the same amount as was added in the payment when auto-reload was enabled. Your account balance is checked every 5-10 minutes and if it falls below the threshold and auto-reload is enabled, then it will be topped up automatically. Use this endpoint  if you need to top up at times when your credit may be exhausted more quickly than the auto-reload may occur.

### Example

```javascript
import AccountApi from 'account_api';

let apiInstance = new AccountApi.BalanceApi();
let apiKey = "abcd1234"; // String | Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com)
let apiSecret = "ABCDEFGH01234abc"; // String | Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com)
let trx = "trx_example"; // String | The transaction reference of the transaction when balance was added and auto-reload was enabled on your account.
apiInstance.topUpAccountBalance(apiKey, apiSecret, trx, (error, data, response) => {
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
 **apiKey** | **String**| Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com) | 
 **apiSecret** | **String**| Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com) | 
 **trx** | **String**| The transaction reference of the transaction when balance was added and auto-reload was enabled on your account. | 

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

