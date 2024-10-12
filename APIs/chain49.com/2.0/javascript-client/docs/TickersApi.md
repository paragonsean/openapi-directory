# Chain49Api.TickersApi

All URIs are relative to *https://api.chain49.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTickersListV2**](TickersApi.md#getTickersListV2) | **GET** /{blockchain}/v2/tickers-list/ | Get Tickers list V2
[**getTickersV2**](TickersApi.md#getTickersV2) | **GET** /{blockchain}/v2/tickers/ | Get Tickers V2



## getTickersListV2

> GetTickersListV2200Response getTickersListV2(blockchain, opts)

Get Tickers list V2

Returns a list of available currency rate tickers (secondary currencies) for the specified date, along with an actual data timestamp.  Trailing slash &#39;/&#39; is mandatory

### Example

```javascript
import Chain49Api from 'chain49_api';
let defaultClient = Chain49Api.ApiClient.instance;
// Configure API key authorization: X-RapidAPI-Host
let X-RapidAPI-Host = defaultClient.authentications['X-RapidAPI-Host'];
X-RapidAPI-Host.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-RapidAPI-Host.apiKeyPrefix = 'Token';
// Configure API key authorization: X-API-Key
let X-API-Key = defaultClient.authentications['X-API-Key'];
X-API-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-API-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-RapidAPI-Key
let X-RapidAPI-Key = defaultClient.authentications['X-RapidAPI-Key'];
X-RapidAPI-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-RapidAPI-Key.apiKeyPrefix = 'Token';

let apiInstance = new Chain49Api.TickersApi();
let blockchain = "bitcoin"; // String | Blockchain name
let opts = {
  'timestamp': "1519053802" // String | specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned.
};
apiInstance.getTickersListV2(blockchain, opts, (error, data, response) => {
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
 **blockchain** | **String**| Blockchain name | 
 **timestamp** | **String**| specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned. | [optional] 

### Return type

[**GetTickersListV2200Response**](GetTickersListV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTickersV2

> GetTickersV2200Response getTickersV2(blockchain, opts)

Get Tickers V2

Returns currency rate for the specified currency and date. If the currency is not available for that specific timestamp, the next closest rate will be returned. All responses contain an actual rate timestamp.

### Example

```javascript
import Chain49Api from 'chain49_api';
let defaultClient = Chain49Api.ApiClient.instance;
// Configure API key authorization: X-RapidAPI-Host
let X-RapidAPI-Host = defaultClient.authentications['X-RapidAPI-Host'];
X-RapidAPI-Host.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-RapidAPI-Host.apiKeyPrefix = 'Token';
// Configure API key authorization: X-API-Key
let X-API-Key = defaultClient.authentications['X-API-Key'];
X-API-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-API-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-RapidAPI-Key
let X-RapidAPI-Key = defaultClient.authentications['X-RapidAPI-Key'];
X-RapidAPI-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-RapidAPI-Key.apiKeyPrefix = 'Token';

let apiInstance = new Chain49Api.TickersApi();
let blockchain = "bitcoin"; // String | Blockchain name
let opts = {
  'timestamp': "1519053802", // String | specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned.
  'currency': "usd" // String | specifies a currency of returned rate (\"usd\", \"eur\", \"eth\"...). If not specified, all available currencies will be returned
};
apiInstance.getTickersV2(blockchain, opts, (error, data, response) => {
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
 **blockchain** | **String**| Blockchain name | 
 **timestamp** | **String**| specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned. | [optional] 
 **currency** | **String**| specifies a currency of returned rate (\&quot;usd\&quot;, \&quot;eur\&quot;, \&quot;eth\&quot;...). If not specified, all available currencies will be returned | [optional] 

### Return type

[**GetTickersV2200Response**](GetTickersV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

