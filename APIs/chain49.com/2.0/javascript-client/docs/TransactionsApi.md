# Chain49Api.TransactionsApi

All URIs are relative to *https://api.chain49.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMempoolV2**](TransactionsApi.md#getMempoolV2) | **GET** /{blockchain}/v2/mempool/ | Get Mempool V2
[**getSendTxV2**](TransactionsApi.md#getSendTxV2) | **GET** /{blockchain}/v2/sendtx/{hex} | Send transaction (in URL) V2
[**getTransactionV2**](TransactionsApi.md#getTransactionV2) | **GET** /{blockchain}/v2/tx/{txId} | Get transaction V2
[**getTxSpecificV2**](TransactionsApi.md#getTxSpecificV2) | **GET** /{blockchain}/v2/tx-specific/{txId} | Get transaction (as is from Backend) V2
[**postSendTxV2**](TransactionsApi.md#postSendTxV2) | **POST** /{blockchain}/v2/sendtx/ | Send transaction (POST) V2



## getMempoolV2

> GetMempoolV2200Response getMempoolV2(blockchain, opts)

Get Mempool V2

Get a list of transaction IDs currently in the mempool of the node (meaning unconfirmed transactions not included in any block yet)  Note: this route was implemented by us and is therefore not yet supported by existing blockbook clients.

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

let apiInstance = new Chain49Api.TransactionsApi();
let blockchain = "bitcoin"; // String | Blockchain name
let opts = {
  'page': 1, // Number | specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page.
  'pageSize': 1000 // Number | number of transactions returned by call (default and maximum 1000)
};
apiInstance.getMempoolV2(blockchain, opts, (error, data, response) => {
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
 **page** | **Number**| specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. | [optional] 
 **pageSize** | **Number**| number of transactions returned by call (default and maximum 1000) | [optional] 

### Return type

[**GetMempoolV2200Response**](GetMempoolV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSendTxV2

> PostSendTxV2200Response getSendTxV2(blockchain, hex)

Send transaction (in URL) V2

Sends new transaction to backend  It is recommended to use POST for sending transactions as there is a limit on how much data can be sent in the URL itself.

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

let apiInstance = new Chain49Api.TransactionsApi();
let blockchain = "bitcoin"; // String | Blockchain name
let hex = "01000000017f9a22c9cbf54bd902400df746f138f37bcf5b4d93eb755820e974ba43ed5f42040000006a4730440220037f4ed5427cde81d55b9b6a2fd08c8a25090c2c2fff3a75c1a57625ca8a7118022076c702fe55969fa08137f71afd4851c48e31082dd3c40c919c92cdbc826758d30121029f6da5623c9f9b68a9baf9c1bc7511df88fa34c6c2f71f7c62f2f03ff48dca80feffffff019c9700000000000017a9146144d57c8aff48492c9dfb914e120b20bad72d6f8773d00700"; // String | Transaction hex data
apiInstance.getSendTxV2(blockchain, hex, (error, data, response) => {
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
 **hex** | **String**| Transaction hex data | 

### Return type

[**PostSendTxV2200Response**](PostSendTxV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionV2

> GetTransactionV2200Response getTransactionV2(blockchain, txId)

Get transaction V2

Get transaction returns \&quot;normalized\&quot; data about transaction, which has the same general structure for all supported coins. It does not return coin specific fields (for example information about Zcash shielded addresses).  A note about the blockTime field: for already mined transaction (confirmations &gt; 0), the field blockTime contains time of the block for transactions in mempool (confirmations &#x3D;&#x3D; 0), the field contains time when the running instance of Blockbook was first time notified about the transaction. This time may be different in different instances of Blockbook.

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

let apiInstance = new Chain49Api.TransactionsApi();
let blockchain = "bitcoin"; // String | Blockchain name
let txId = "cd8ec77174e426070d0a50779232bba7312b712e2c6843d82d963d7076c61366"; // String | Transaction ID
apiInstance.getTransactionV2(blockchain, txId, (error, data, response) => {
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
 **txId** | **String**| Transaction ID | 

### Return type

[**GetTransactionV2200Response**](GetTransactionV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTxSpecificV2

> Object getTxSpecificV2(blockchain, txId)

Get transaction (as is from Backend) V2

Returns transaction data in the exact format as returned by backend, including all coin specific fields

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

let apiInstance = new Chain49Api.TransactionsApi();
let blockchain = "bitcoin"; // String | Blockchain name
let txId = "cd8ec77174e426070d0a50779232bba7312b712e2c6843d82d963d7076c61366"; // String | Transaction ID
apiInstance.getTxSpecificV2(blockchain, txId, (error, data, response) => {
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
 **txId** | **String**| Transaction ID | 

### Return type

**Object**

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postSendTxV2

> PostSendTxV2200Response postSendTxV2(blockchain, opts)

Send transaction (POST) V2

Sends new transaction to backend for broadcasting  The trailing slash &#39;/&#39; at the end is mandatory 

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

let apiInstance = new Chain49Api.TransactionsApi();
let blockchain = "bitcoin"; // String | Blockchain name
let opts = {
  'body': {key: null} // Object | Transaction hex as plain text
};
apiInstance.postSendTxV2(blockchain, opts, (error, data, response) => {
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
 **body** | **Object**| Transaction hex as plain text | [optional] 

### Return type

[**PostSendTxV2200Response**](PostSendTxV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json

