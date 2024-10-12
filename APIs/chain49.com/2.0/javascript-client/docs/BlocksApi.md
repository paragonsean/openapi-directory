# Chain49Api.BlocksApi

All URIs are relative to *https://api.chain49.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBlockHashV2**](BlocksApi.md#getBlockHashV2) | **GET** /{blockchain}/v2/block-index/{blockHeight} | Get block hash V2
[**getBlockV2**](BlocksApi.md#getBlockV2) | **GET** /{blockchain}/v2/block/{blockHashOrHeight} | Get Block V2
[**getRawBlockV2**](BlocksApi.md#getRawBlockV2) | **GET** /{blockchain}/v2/rawblock/{blockHashOrHeight} | Get raw block data V2



## getBlockHashV2

> GetBlockHashV2200Response getBlockHashV2(blockchain, blockHeight)

Get block hash V2

Get block hash by its height  Note: Blockbook always follows the main chain of the backend it is attached to.

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

let apiInstance = new Chain49Api.BlocksApi();
let blockchain = "bitcoin"; // String | Blockchain name
let blockHeight = 15; // Number | Block height/index
apiInstance.getBlockHashV2(blockchain, blockHeight, (error, data, response) => {
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
 **blockHeight** | **Number**| Block height/index | 

### Return type

[**GetBlockHashV2200Response**](GetBlockHashV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBlockV2

> GetBlockV2200Response getBlockV2(blockchain, blockHashOrHeight, opts)

Get Block V2

Returns information about block with transactions, subject to paging.  Note: Blockbook always follows the main chain of the backend it is attached to. If there is a rollback-reorg in the backend, Blockbook will also do rollback. When you ask for block by height, you will always get the main chain block. If you ask for block by hash, you may get the block from another fork but it is not guaranteed (backend may not keep it)

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

let apiInstance = new Chain49Api.BlocksApi();
let blockchain = "bitcoin"; // String | Blockchain name
let blockHashOrHeight = "00000000000000000035835503f43c878ebb643f3b40bdfd0dfda760da74e73c"; // String | Block hash or height
let opts = {
  'page': 1, // Number | specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page.
  'pageSize': 1000 // Number | number of transactions returned by call (default and maximum 1000)
};
apiInstance.getBlockV2(blockchain, blockHashOrHeight, opts, (error, data, response) => {
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
 **blockHashOrHeight** | **String**| Block hash or height | 
 **page** | **Number**| specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. | [optional] 
 **pageSize** | **Number**| number of transactions returned by call (default and maximum 1000) | [optional] 

### Return type

[**GetBlockV2200Response**](GetBlockV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRawBlockV2

> GetRawBlockV2200Response getRawBlockV2(blockchain, blockHashOrHeight)

Get raw block data V2

Returns the raw hex-encoded block data for a given block hash or height

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

let apiInstance = new Chain49Api.BlocksApi();
let blockchain = "bitcoin"; // String | Blockchain name
let blockHashOrHeight = "00000000000000000035835503f43c878ebb643f3b40bdfd0dfda760da74e73c"; // String | Block hash or height
apiInstance.getRawBlockV2(blockchain, blockHashOrHeight, (error, data, response) => {
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
 **blockHashOrHeight** | **String**| Block hash or height | 

### Return type

[**GetRawBlockV2200Response**](GetRawBlockV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

