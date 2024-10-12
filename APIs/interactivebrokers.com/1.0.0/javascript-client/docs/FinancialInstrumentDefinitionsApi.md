# Ibkr3rdPartyWebApi.FinancialInstrumentDefinitionsApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secdefGet**](FinancialInstrumentDefinitionsApi.md#secdefGet) | **GET** /secdef | Get security definition



## secdefGet

> [SecdefGet200ResponseInner] secdefGet(marketdataSnapshotGetRequestInner)

Get security definition

Fields that compose security definition. Allowed combinations, (1) type and symbol and currency, or (2) type, symbol, exchange, and currency, or (3) conid 

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.FinancialInstrumentDefinitionsApi();
let marketdataSnapshotGetRequestInner = new Ibkr3rdPartyWebApi.MarketdataSnapshotGetRequestInner(); // MarketdataSnapshotGetRequestInner | Order Parameters
apiInstance.secdefGet(marketdataSnapshotGetRequestInner, (error, data, response) => {
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
 **marketdataSnapshotGetRequestInner** | [**MarketdataSnapshotGetRequestInner**](MarketdataSnapshotGetRequestInner.md)| Order Parameters | 

### Return type

[**[SecdefGet200ResponseInner]**](SecdefGet200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

