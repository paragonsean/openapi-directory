# Chain49Api.FeeEstimationApi

All URIs are relative to *https://api.chain49.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEstimateFeeV2**](FeeEstimationApi.md#getEstimateFeeV2) | **GET** /{blockchain}/v2/estimatefee/{confirmationTarget} | Estimate transaction fee V2



## getEstimateFeeV2

> GetEstimateFeeV2200Response getEstimateFeeV2(blockchain, confirmationTarget)

Estimate transaction fee V2

Returns an estimated transaction fee for a specific confirmation target. If you want your transaction to be included in the next block, then you give 1 as parameter. If it is not urgent, then you can wait a bit longer and get an estimation for the fifth next block.

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

let apiInstance = new Chain49Api.FeeEstimationApi();
let blockchain = "bitcoin"; // String | Blockchain name
let confirmationTarget = 1; // Number | Number of blocks in which the transaction should be confirmed
apiInstance.getEstimateFeeV2(blockchain, confirmationTarget, (error, data, response) => {
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
 **confirmationTarget** | **Number**| Number of blocks in which the transaction should be confirmed | 

### Return type

[**GetEstimateFeeV2200Response**](GetEstimateFeeV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

