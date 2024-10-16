# NeblioRestApiSuite.NTP1Api

All URIs are relative to *https://ntp1node.nebl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**broadcastTx**](NTP1Api.md#broadcastTx) | **POST** /ntp1/broadcast | Broadcasts a signed raw transaction to the network
[**burnToken**](NTP1Api.md#burnToken) | **POST** /ntp1/burntoken | Builds a transaction that burns an NTP1 Token
[**getAddressInfo**](NTP1Api.md#getAddressInfo) | **GET** /ntp1/addressinfo/{address} | Information On a Neblio Address
[**getTokenHolders**](NTP1Api.md#getTokenHolders) | **GET** /ntp1/stakeholders/{tokenid} | Get Addresses Holding a Token
[**getTokenId**](NTP1Api.md#getTokenId) | **GET** /ntp1/tokenid/{tokensymbol} | Returns the tokenId representing a token
[**getTokenMetadata**](NTP1Api.md#getTokenMetadata) | **GET** /ntp1/tokenmetadata/{tokenid} | Get Metadata of Token
[**getTokenMetadataOfUtxo**](NTP1Api.md#getTokenMetadataOfUtxo) | **GET** /ntp1/tokenmetadata/{tokenid}/{utxo} | Get UTXO Metadata of Token
[**getTransactionInfo**](NTP1Api.md#getTransactionInfo) | **GET** /ntp1/transactioninfo/{txid} | Information On an NTP1 Transaction
[**issueToken**](NTP1Api.md#issueToken) | **POST** /ntp1/issue | Builds a transaction that issues a new NTP1 Token
[**sendToken**](NTP1Api.md#sendToken) | **POST** /ntp1/sendtoken | Builds a transaction that sends an NTP1 Token



## broadcastTx

> BroadcastTxResponse broadcastTx(broadcastTxRequest)

Broadcasts a signed raw transaction to the network

Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction. 

### Example

```javascript
import NeblioRestApiSuite from 'neblio_rest_api_suite';

let apiInstance = new NeblioRestApiSuite.NTP1Api();
let broadcastTxRequest = new NeblioRestApiSuite.BroadcastTxRequest(); // BroadcastTxRequest | Object representing a transaction to broadcast
apiInstance.broadcastTx(broadcastTxRequest, (error, data, response) => {
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
 **broadcastTxRequest** | [**BroadcastTxRequest**](BroadcastTxRequest.md)| Object representing a transaction to broadcast | 

### Return type

[**BroadcastTxResponse**](BroadcastTxResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## burnToken

> BurnTokenResponse burnToken(burnTokenRequest)

Builds a transaction that burns an NTP1 Token

Builds an unsigned raw transaction that burns an NTP1 token on the Neblio blockchain. 

### Example

```javascript
import NeblioRestApiSuite from 'neblio_rest_api_suite';

let apiInstance = new NeblioRestApiSuite.NTP1Api();
let burnTokenRequest = new NeblioRestApiSuite.BurnTokenRequest(); // BurnTokenRequest | Object representing the token to be burned
apiInstance.burnToken(burnTokenRequest, (error, data, response) => {
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
 **burnTokenRequest** | [**BurnTokenRequest**](BurnTokenRequest.md)| Object representing the token to be burned | 

### Return type

[**BurnTokenResponse**](BurnTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAddressInfo

> GetAddressInfoResponse getAddressInfo(address)

Information On a Neblio Address

Returns both NEBL and NTP1 token UTXOs held at the given address. 

### Example

```javascript
import NeblioRestApiSuite from 'neblio_rest_api_suite';

let apiInstance = new NeblioRestApiSuite.NTP1Api();
let address = "address_example"; // String | Neblio Address to get information on.
apiInstance.getAddressInfo(address, (error, data, response) => {
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
 **address** | **String**| Neblio Address to get information on. | 

### Return type

[**GetAddressInfoResponse**](GetAddressInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTokenHolders

> GetTokenHoldersResponse getTokenHolders(tokenid)

Get Addresses Holding a Token

Returns the the the addresses holding a token and how many tokens are held 

### Example

```javascript
import NeblioRestApiSuite from 'neblio_rest_api_suite';

let apiInstance = new NeblioRestApiSuite.NTP1Api();
let tokenid = "tokenid_example"; // String | TokenId to request metadata for
apiInstance.getTokenHolders(tokenid, (error, data, response) => {
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
 **tokenid** | **String**| TokenId to request metadata for | 

### Return type

[**GetTokenHoldersResponse**](GetTokenHoldersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTokenId

> GetTokenIdResponse getTokenId(tokensymbol)

Returns the tokenId representing a token

Translates a token symbol to a tokenId if a token exists with that symbol on the network 

### Example

```javascript
import NeblioRestApiSuite from 'neblio_rest_api_suite';

let apiInstance = new NeblioRestApiSuite.NTP1Api();
let tokensymbol = "tokensymbol_example"; // String | Token symbol
apiInstance.getTokenId(tokensymbol, (error, data, response) => {
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
 **tokensymbol** | **String**| Token symbol | 

### Return type

[**GetTokenIdResponse**](GetTokenIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTokenMetadata

> GetTokenMetadataResponse getTokenMetadata(tokenid, opts)

Get Metadata of Token

Returns the metadata associated with a token. 

### Example

```javascript
import NeblioRestApiSuite from 'neblio_rest_api_suite';

let apiInstance = new NeblioRestApiSuite.NTP1Api();
let tokenid = "tokenid_example"; // String | TokenId to request metadata for
let opts = {
  'verbosity': 3.4 // Number | 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses
};
apiInstance.getTokenMetadata(tokenid, opts, (error, data, response) => {
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
 **tokenid** | **String**| TokenId to request metadata for | 
 **verbosity** | **Number**| 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses | [optional] 

### Return type

[**GetTokenMetadataResponse**](GetTokenMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTokenMetadataOfUtxo

> GetTokenMetadataResponse getTokenMetadataOfUtxo(tokenid, utxo, opts)

Get UTXO Metadata of Token

Returns the metadata associated with a token for that specific utxo instead of the issuance transaction. 

### Example

```javascript
import NeblioRestApiSuite from 'neblio_rest_api_suite';

let apiInstance = new NeblioRestApiSuite.NTP1Api();
let tokenid = "tokenid_example"; // String | TokenId to request metadata for
let utxo = "utxo_example"; // String | Specific UTXO to request metadata for
let opts = {
  'verbosity': 3.4 // Number | 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses
};
apiInstance.getTokenMetadataOfUtxo(tokenid, utxo, opts, (error, data, response) => {
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
 **tokenid** | **String**| TokenId to request metadata for | 
 **utxo** | **String**| Specific UTXO to request metadata for | 
 **verbosity** | **Number**| 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses | [optional] 

### Return type

[**GetTokenMetadataResponse**](GetTokenMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionInfo

> GetTransactionInfoResponse getTransactionInfo(txid)

Information On an NTP1 Transaction

Returns detailed information regarding an NTP1 transaction. 

### Example

```javascript
import NeblioRestApiSuite from 'neblio_rest_api_suite';

let apiInstance = new NeblioRestApiSuite.NTP1Api();
let txid = "txid_example"; // String | Neblio txid to get information on.
apiInstance.getTransactionInfo(txid, (error, data, response) => {
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
 **txid** | **String**| Neblio txid to get information on. | 

### Return type

[**GetTransactionInfoResponse**](GetTransactionInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## issueToken

> IssueTokenResponse issueToken(issueTokenRequest)

Builds a transaction that issues a new NTP1 Token

Builds an unsigned raw transaction that issues a new NTP1 token on the Neblio blockchain. 

### Example

```javascript
import NeblioRestApiSuite from 'neblio_rest_api_suite';

let apiInstance = new NeblioRestApiSuite.NTP1Api();
let issueTokenRequest = new NeblioRestApiSuite.IssueTokenRequest(); // IssueTokenRequest | Object representing the token to be created
apiInstance.issueToken(issueTokenRequest, (error, data, response) => {
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
 **issueTokenRequest** | [**IssueTokenRequest**](IssueTokenRequest.md)| Object representing the token to be created | 

### Return type

[**IssueTokenResponse**](IssueTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendToken

> SendTokenResponse sendToken(sendTokenRequest)

Builds a transaction that sends an NTP1 Token

Builds an unsigned raw transaction that sends an NTP1 token on the Neblio blockchain. 

### Example

```javascript
import NeblioRestApiSuite from 'neblio_rest_api_suite';

let apiInstance = new NeblioRestApiSuite.NTP1Api();
let sendTokenRequest = new NeblioRestApiSuite.SendTokenRequest(); // SendTokenRequest | Object representing the token to be sent
apiInstance.sendToken(sendTokenRequest, (error, data, response) => {
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
 **sendTokenRequest** | [**SendTokenRequest**](SendTokenRequest.md)| Object representing the token to be sent | 

### Return type

[**SendTokenResponse**](SendTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

