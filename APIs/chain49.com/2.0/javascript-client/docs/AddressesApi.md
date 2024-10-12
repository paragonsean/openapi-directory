# Chain49Api.AddressesApi

All URIs are relative to *https://api.chain49.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAddressV2**](AddressesApi.md#getAddressV2) | **GET** /{blockchain}/v2/address/{address} | Get address V2
[**getBalanceHistoryV2**](AddressesApi.md#getBalanceHistoryV2) | **GET** /{blockchain}/v2/balancehistory/{addressOrXpub} | Get Balance History V2
[**getUTXOV2**](AddressesApi.md#getUTXOV2) | **GET** /{blockchain}/v2/utxo/{addressOrXpub} | Get UTXO V2
[**getXpubV2**](AddressesApi.md#getXpubV2) | **GET** /{blockchain}/v2/xpub/{xpub} | Get xpub V2



## getAddressV2

> Object getAddressV2(blockchain, address, opts)

Get address V2

Returns balances and transactions of an address. The returned transactions are sorted by block height, newest blocks first.  The **details** query parameter can specify the level of details returned by the request (default: \&quot;txids\&quot;). Possible values are:  **basic**: return only xpub balances, without any derived addresses and transactions  **tokens**: basic + tokens (addresses) derived from the xpub, subject to tokens parameter  **tokenBalances**: basic + tokens (addresses) derived from the xpub with balances, subject to tokens parameter  **txids**: tokenBalances + list of txids, subject to from, to filter and paging  **txs**: tokenBalances + list of transaction with details, subject to from, to filter and paging 

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

let apiInstance = new Chain49Api.AddressesApi();
let blockchain = "bitcoin"; // String | Blockchain name
let address = "321x69Cb9HZLWwAWGiUBT1U81r1zPLnEjL"; // String | Wallet address
let opts = {
  'page': 1, // Number | specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page.
  'pageSize': 1000, // Number | number of transactions returned by call (default and maximum 1000)
  'fromBlock': 10, // Number | filter of the returned transactions from block height to block height (default no filter)
  'toBlock': 100, // Number | filter of the returned transactions from block height to block height (default no filter)
  'details': "basic", // String | specifies level of details returned by request
  'contract': "0xdAC17F958D2ee523a2206206994597C13D831ec7", // String | return only transactions which affect specified contract (applicable only to coins which support contracts)
  'secondary': "usd" // String | specifies secondary (fiat) currency in which the token and total balances are returned in addition to crypto values
};
apiInstance.getAddressV2(blockchain, address, opts, (error, data, response) => {
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
 **address** | **String**| Wallet address | 
 **page** | **Number**| specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. | [optional] 
 **pageSize** | **Number**| number of transactions returned by call (default and maximum 1000) | [optional] 
 **fromBlock** | **Number**| filter of the returned transactions from block height to block height (default no filter) | [optional] 
 **toBlock** | **Number**| filter of the returned transactions from block height to block height (default no filter) | [optional] 
 **details** | **String**| specifies level of details returned by request | [optional] [default to &#39;txids&#39;]
 **contract** | **String**| return only transactions which affect specified contract (applicable only to coins which support contracts) | [optional] 
 **secondary** | **String**| specifies secondary (fiat) currency in which the token and total balances are returned in addition to crypto values | [optional] 

### Return type

**Object**

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBalanceHistoryV2

> [GetBalanceHistoryV2200ResponseInner] getBalanceHistoryV2(blockchain, addressOrXpub, opts)

Get Balance History V2

Returns a balance history for the specified XPUB or address  The value of sentToSelf is the amount sent from the same address to the same address or within addresses of xpub.

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

let apiInstance = new Chain49Api.AddressesApi();
let blockchain = "bitcoin"; // String | Blockchain name
let addressOrXpub = "321x69Cb9HZLWwAWGiUBT1U81r1zPLnEjL"; // String | Address or XPUB
let opts = {
  'fromDate': "1578391200", // String | specifies a start date as a Unix timestamp
  'toDate': "1599053802", // String | specifies an end date as a Unix timestamp
  'fiatcurrency': "usd", // String | if specified, the response will contain secondary (fiat) rate at the time of transaction. If not, all available currencies will be returned
  'groupBy': 172800 // Number | an interval in seconds, to group results by. Default is 3600 seconds
};
apiInstance.getBalanceHistoryV2(blockchain, addressOrXpub, opts, (error, data, response) => {
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
 **addressOrXpub** | **String**| Address or XPUB | 
 **fromDate** | **String**| specifies a start date as a Unix timestamp | [optional] 
 **toDate** | **String**| specifies an end date as a Unix timestamp | [optional] 
 **fiatcurrency** | **String**| if specified, the response will contain secondary (fiat) rate at the time of transaction. If not, all available currencies will be returned | [optional] 
 **groupBy** | **Number**| an interval in seconds, to group results by. Default is 3600 seconds | [optional] [default to 3600]

### Return type

[**[GetBalanceHistoryV2200ResponseInner]**](GetBalanceHistoryV2200ResponseInner.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUTXOV2

> [Object] getUTXOV2(blockchain, addressOrXpub, opts)

Get UTXO V2

Returns array of unspent transaction outputs of address or xpub, applicable only for Bitcoin-type coins. By default, the list contains both confirmed and unconfirmed transactions. The query parameter confirmed&#x3D;true disables return of unconfirmed transactions. The returned utxos are sorted by block height, newest blocks first. For xpubs or output descriptors, the response also contains address and derivation path of the utxo.    Unconfirmed utxos do not have field height, the field confirmations has value 0 and may contain field lockTime, if not zero.  Coinbase utxos have field coinbase set to true, however due to performance reasons only up to minimum coinbase confirmations limit (100). After this limit, utxos are not detected as coinbase.

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

let apiInstance = new Chain49Api.AddressesApi();
let blockchain = "bitcoin"; // String | Blockchain name
let addressOrXpub = "321x69Cb9HZLWwAWGiUBT1U81r1zPLnEjL"; // String | Address or XPUB
let opts = {
  'confirmed': true // Boolean | confirmed=true disables return of unconfirmed transactions
};
apiInstance.getUTXOV2(blockchain, addressOrXpub, opts, (error, data, response) => {
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
 **addressOrXpub** | **String**| Address or XPUB | 
 **confirmed** | **Boolean**| confirmed&#x3D;true disables return of unconfirmed transactions | [optional] 

### Return type

**[Object]**

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getXpubV2

> GetXpubV2200Response getXpubV2(blockchain, xpub, opts)

Get xpub V2

Returns balances and transactions of an xpub or output descriptor, applicable only for Bitcoin-type coins.  Blockbook supports BIP44, BIP49, BIP84 and BIP86 (Taproot) derivation schemes, using either xpubs or output descriptors (see https://github.com/bitcoin/bitcoin/blob/master/doc/descriptors.md)  Note: usedTokens always returns total number of used addresses of xpub.  Detailed documentation found here: https://github.com/trezor/blockbook/blob/master/docs/api.md#get-xpub

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

let apiInstance = new Chain49Api.AddressesApi();
let blockchain = "bitcoin"; // String | Blockchain name
let xpub = "tpubDC88gkaZi5HvJGxGDNLADkvtdpni3mLmx6vr2KnXmWMG8zfkBRggsxHVBkUpgcwPe2KKpkyvTJCdXHb1UHEWE64vczyyPQfHr1skBcsRedN"; // String | xpub or output descriptor, applicable only for Bitcoin-type coins
let opts = {
  'page': 1, // Number | specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page.
  'pageSize': 1000, // Number | number of transactions returned by call (default and maximum 1000)
  'fromBlock': 10, // Number | filter of the returned transactions from block height to block height (default no filter)
  'toBlock': 100, // Number | filter of the returned transactions from block height to block height (default no filter)
  'details': "basic", // String | specifies level of details returned by request
  'tokens': "used", // String | specifies what tokens (xpub addresses) are returned by the request (default nonzero)
  'secondary': "usd" // String | specifies secondary (fiat) currency in which the token and total balances are returned in addition to crypto values
};
apiInstance.getXpubV2(blockchain, xpub, opts, (error, data, response) => {
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
 **xpub** | **String**| xpub or output descriptor, applicable only for Bitcoin-type coins | 
 **page** | **Number**| specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. | [optional] 
 **pageSize** | **Number**| number of transactions returned by call (default and maximum 1000) | [optional] 
 **fromBlock** | **Number**| filter of the returned transactions from block height to block height (default no filter) | [optional] 
 **toBlock** | **Number**| filter of the returned transactions from block height to block height (default no filter) | [optional] 
 **details** | **String**| specifies level of details returned by request | [optional] [default to &#39;txids&#39;]
 **tokens** | **String**| specifies what tokens (xpub addresses) are returned by the request (default nonzero) | [optional] [default to &#39;nonzero&#39;]
 **secondary** | **String**| specifies secondary (fiat) currency in which the token and total balances are returned in addition to crypto values | [optional] 

### Return type

[**GetXpubV2200Response**](GetXpubV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

