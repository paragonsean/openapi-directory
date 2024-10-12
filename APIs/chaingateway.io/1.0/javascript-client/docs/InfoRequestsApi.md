# ChaingatewayIo.InfoRequestsApi

All URIs are relative to *https://eu.eth.chaingateway.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBlock**](InfoRequestsApi.md#getBlock) | **POST** /getBlock | getBlock
[**getEthereumBalance**](InfoRequestsApi.md#getEthereumBalance) | **POST** /getEthereumBalance | getEthereumBalance
[**getExchangeRate**](InfoRequestsApi.md#getExchangeRate) | **POST** /getExchangeRate | getExchangeRate
[**getGasPrice**](InfoRequestsApi.md#getGasPrice) | **POST** /getGasPrice | getGasPrice
[**getLastBlockNumber**](InfoRequestsApi.md#getLastBlockNumber) | **POST** /getLastBlockNumber | getLastBlockNumber
[**getToken**](InfoRequestsApi.md#getToken) | **POST** /getToken | getToken
[**getTokenBalance**](InfoRequestsApi.md#getTokenBalance) | **POST** /getTokenBalance | getTokenBalance
[**getTransactions**](InfoRequestsApi.md#getTransactions) | **POST** /getTransactions | getTransactions



## getBlock

> GetBlock getBlock(authorization, getBlockRequest)

getBlock

Returns information of an ethereum block with or without transactions

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.InfoRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let getBlockRequest = {"block":"5000000"}; // GetBlockRequest | 
apiInstance.getBlock(authorization, getBlockRequest, (error, data, response) => {
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
 **authorization** | **String**| API Key | 
 **getBlockRequest** | [**GetBlockRequest**](GetBlockRequest.md)|  | 

### Return type

[**GetBlock**](GetBlock.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getEthereumBalance

> GetEthereumBalance getEthereumBalance(authorization, getEthereumBalanceRequest)

getEthereumBalance

Returns the ethereum balance of a given address.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.InfoRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let getEthereumBalanceRequest = {"ethereumaddress":"0xa1f36016221d48ce7f15cde7b826a4fbe09bacce"}; // GetEthereumBalanceRequest | 
apiInstance.getEthereumBalance(authorization, getEthereumBalanceRequest, (error, data, response) => {
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
 **authorization** | **String**| API Key | 
 **getEthereumBalanceRequest** | [**GetEthereumBalanceRequest**](GetEthereumBalanceRequest.md)|  | 

### Return type

[**GetEthereumBalance**](GetEthereumBalance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getExchangeRate

> GetExchangeRate getExchangeRate(authorization, getExchangeRateRequest)

getExchangeRate

Returns the current Ethereum price in Euro or US Dollar.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.InfoRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let getExchangeRateRequest = {"currency":"eur"}; // GetExchangeRateRequest | 
apiInstance.getExchangeRate(authorization, getExchangeRateRequest, (error, data, response) => {
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
 **authorization** | **String**| API Key | 
 **getExchangeRateRequest** | [**GetExchangeRateRequest**](GetExchangeRateRequest.md)|  | 

### Return type

[**GetExchangeRate**](GetExchangeRate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getGasPrice

> GetGasPrice getGasPrice(contentType, authorization)

getGasPrice

Returns the current gas price in GWEI.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.InfoRequestsApi();
let contentType = "application/json"; // String | 
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
apiInstance.getGasPrice(contentType, authorization, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **authorization** | **String**| API Key | 

### Return type

[**GetGasPrice**](GetGasPrice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLastBlockNumber

> GetLastBlockNumber getLastBlockNumber(contentType, authorization)

getLastBlockNumber

Returns the block number of the last mined ethereum block.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.InfoRequestsApi();
let contentType = "application/json"; // String | 
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
apiInstance.getLastBlockNumber(contentType, authorization, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **authorization** | **String**| API Key | 

### Return type

[**GetLastBlockNumber**](GetLastBlockNumber.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getToken

> GetToken getToken(authorization, getTokenRequest)

getToken

Returns information about a specific ERC20 token like name, symbol, decimal places and total supply.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.InfoRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let getTokenRequest = {"contractaddress":"0x5b86a33f0c232fe909eb4602a9d039072869d915"}; // GetTokenRequest | 
apiInstance.getToken(authorization, getTokenRequest, (error, data, response) => {
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
 **authorization** | **String**| API Key | 
 **getTokenRequest** | [**GetTokenRequest**](GetTokenRequest.md)|  | 

### Return type

[**GetToken**](GetToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTokenBalance

> GetTokenBalance getTokenBalance(authorization, getTokenBalanceRequest)

getTokenBalance

Returns the token balance of a given address.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.InfoRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let getTokenBalanceRequest = {"contractaddress":"0x5b86a33f0c232fe909eb4602a9d039072869d915","ethereumaddress":"0xa1f36016221d48ce7f15cde7b826a4fbe09bacce"}; // GetTokenBalanceRequest | 
apiInstance.getTokenBalance(authorization, getTokenBalanceRequest, (error, data, response) => {
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
 **authorization** | **String**| API Key | 
 **getTokenBalanceRequest** | [**GetTokenBalanceRequest**](GetTokenBalanceRequest.md)|  | 

### Return type

[**GetTokenBalance**](GetTokenBalance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTransactions

> GetTransactions getTransactions(authorization, getTransactionsRequest)

getTransactions

Returns information like confirmations, token contract address, amount, gas price and more of a given transaction.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.InfoRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let getTransactionsRequest = {"txid":"0x8ab5543bc103bdd908681da501d03c2c495afd7fde5ed104935ba97b1550d65b"}; // GetTransactionsRequest | 
apiInstance.getTransactions(authorization, getTransactionsRequest, (error, data, response) => {
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
 **authorization** | **String**| API Key | 
 **getTransactionsRequest** | [**GetTransactionsRequest**](GetTransactionsRequest.md)|  | 

### Return type

[**GetTransactions**](GetTransactions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

