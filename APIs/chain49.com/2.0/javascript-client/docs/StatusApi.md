# Chain49Api.StatusApi

All URIs are relative to *https://api.chain49.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAvailableBlockchains**](StatusApi.md#getAvailableBlockchains) | **GET** / | List available blockchains
[**getBlockchain**](StatusApi.md#getBlockchain) | **GET** /{blockchain} | Blockchain Info Summary



## getAvailableBlockchains

> [String] getAvailableBlockchains()

List available blockchains

Get an array of active blockchains

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

let apiInstance = new Chain49Api.StatusApi();
apiInstance.getAvailableBlockchains((error, data, response) => {
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

**[String]**

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBlockchain

> GetBlockchain200Response getBlockchain(blockchain)

Blockchain Info Summary

Get basic summary of info relating to the currently selected blockchain

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

let apiInstance = new Chain49Api.StatusApi();
let blockchain = "bitcoin"; // String | Blockchain name
apiInstance.getBlockchain(blockchain, (error, data, response) => {
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

### Return type

[**GetBlockchain200Response**](GetBlockchain200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

