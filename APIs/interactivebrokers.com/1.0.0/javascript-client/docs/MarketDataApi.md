# Ibkr3rdPartyWebApi.MarketDataApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketdataExchangeComponentsGet**](MarketDataApi.md#marketdataExchangeComponentsGet) | **GET** /marketdata/exchange_components | Exchange Components
[**marketdataSnapshotGet**](MarketDataApi.md#marketdataSnapshotGet) | **GET** /marketdata/snapshot | Market Data Snapshot



## marketdataExchangeComponentsGet

> [MarketdataExchangeComponentsGet200ResponseInner] marketdataExchangeComponentsGet()

Exchange Components

This endpoint provides a bit mapping for the bid/ask/last &#39;market&#39; values in the snapshot response. 

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.MarketDataApi();
apiInstance.marketdataExchangeComponentsGet((error, data, response) => {
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

[**[MarketdataExchangeComponentsGet200ResponseInner]**](MarketdataExchangeComponentsGet200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketdataSnapshotGet

> [MarketdataSnapshotGet200ResponseInner] marketdataSnapshotGet(marketdataSnapshotGetRequestInner)

Market Data Snapshot

This endpoint allows the consumer to request a market data snapshot for one or more trading products.  Consumers need to provide unique identifiers (conids) for the products in the IB product database (retrievable using the /secdef endpoint). The &#39;market&#39; values are integers whose bits indicate the exchange(s) making up the quote.   The mapping of bit to exchange is obtained from the marketdata/exchange_component endpoint. For example, if a bid has a &#39;market&#39; value of 5 and the exchange_component result has the map  0 &#x3D;&gt; NYSE, 1 &#x3D;&gt; ISLAND, 2 &#x3D;&gt; ARCA then the exchanges contributing to the bid size are NYSE and ARCA.   Similarly, if market&#x3D;2, then only ISLAND is contributing. 

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.MarketDataApi();
let marketdataSnapshotGetRequestInner = [new Ibkr3rdPartyWebApi.MarketdataSnapshotGetRequestInner()]; // [MarketdataSnapshotGetRequestInner] | Contract. Allowed combinations are [type and symbol and currency], or [type, symbol, exchange, and currency], or [conid].
apiInstance.marketdataSnapshotGet(marketdataSnapshotGetRequestInner, (error, data, response) => {
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
 **marketdataSnapshotGetRequestInner** | [**[MarketdataSnapshotGetRequestInner]**](MarketdataSnapshotGetRequestInner.md)| Contract. Allowed combinations are [type and symbol and currency], or [type, symbol, exchange, and currency], or [conid]. | 

### Return type

[**[MarketdataSnapshotGet200ResponseInner]**](MarketdataSnapshotGet200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

