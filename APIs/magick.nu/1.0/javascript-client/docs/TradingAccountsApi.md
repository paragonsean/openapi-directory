# Tradeworks.TradingAccountsApi

All URIs are relative to *http://devui.magick.nu/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postTradingAccounts**](TradingAccountsApi.md#postTradingAccounts) | **POST** /tradingAccounts | Add a Trading Account
[**putTradingAccountsPasswordUsernameBrokerserverMt4username**](TradingAccountsApi.md#putTradingAccountsPasswordUsernameBrokerserverMt4username) | **PUT** /tradingAccounts/password/{username}/{brokerserver}/{mt4username} | Update MT4 Account Password



## postTradingAccounts

> postTradingAccounts(body)

Add a Trading Account

### Example

```javascript
import Tradeworks from 'tradeworks';

let apiInstance = new Tradeworks.TradingAccountsApi();
let body = new Tradeworks.TradingAccount(); // TradingAccount | 
apiInstance.postTradingAccounts(body, (error, data, response) => {
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
 **body** | [**TradingAccount**](TradingAccount.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putTradingAccountsPasswordUsernameBrokerserverMt4username

> putTradingAccountsPasswordUsernameBrokerserverMt4username(username, brokerserver, mt4username, body)

Update MT4 Account Password

### Example

```javascript
import Tradeworks from 'tradeworks';

let apiInstance = new Tradeworks.TradingAccountsApi();
let username = "username_example"; // String | 
let brokerserver = "brokerserver_example"; // String | 
let mt4username = "mt4username_example"; // String | 
let body = new Tradeworks.PasswordDTO(); // PasswordDTO | 
apiInstance.putTradingAccountsPasswordUsernameBrokerserverMt4username(username, brokerserver, mt4username, body, (error, data, response) => {
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
 **username** | **String**|  | 
 **brokerserver** | **String**|  | 
 **mt4username** | **String**|  | 
 **body** | [**PasswordDTO**](PasswordDTO.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

