# TransfersApi.TransfersApi

All URIs are relative to *https://balanceplatform-api-test.adyen.com/btl/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postTransfers**](TransfersApi.md#postTransfers) | **POST** /transfers | Transfer funds
[**postTransfersTransferIdReturns**](TransfersApi.md#postTransfersTransferIdReturns) | **POST** /transfers/{transferId}/returns | Return a transfer



## postTransfers

> Transfer postTransfers(opts)

Transfer funds

&gt;Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.  Starts a request to transfer funds to [balance accounts](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts), [transfer instruments](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments), or third-party bank accounts. Adyen sends the outcome of the transfer request through webhooks.  To use this endpoint, you need an additional role for your API credential and transfers must be enabled for the source balance account. Your Adyen contact will set these up for you.

### Example

```javascript
import TransfersApi from 'transfers_api';
let defaultClient = TransfersApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: clientKey
let clientKey = defaultClient.authentications['clientKey'];
clientKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientKey.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new TransfersApi.TransfersApi();
let opts = {
  'wWWAuthenticate': "SCA realm=\"Transfer\" auth-param1=\"eyJjaGFsbGVuZ2UiOiJiVlV6ZW5wek0waFNl...\"", // String | Header for authenticating through SCA
  'transferInfo': new TransfersApi.TransferInfo() // TransferInfo | 
};
apiInstance.postTransfers(opts, (error, data, response) => {
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
 **wWWAuthenticate** | **String**| Header for authenticating through SCA | [optional] 
 **transferInfo** | [**TransferInfo**](TransferInfo.md)|  | [optional] 

### Return type

[**Transfer**](Transfer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [clientKey](../README.md#clientKey), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTransfersTransferIdReturns

> ReturnTransferResponse postTransfersTransferIdReturns(transferId, opts)

Return a transfer

Returns previously transferred funds without creating a new &#x60;transferId&#x60;.

### Example

```javascript
import TransfersApi from 'transfers_api';
let defaultClient = TransfersApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: clientKey
let clientKey = defaultClient.authentications['clientKey'];
clientKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientKey.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new TransfersApi.TransfersApi();
let transferId = "transferId_example"; // String | The unique identifier of the transfer to be returned.
let opts = {
  'returnTransferRequest': new TransfersApi.ReturnTransferRequest() // ReturnTransferRequest | 
};
apiInstance.postTransfersTransferIdReturns(transferId, opts, (error, data, response) => {
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
 **transferId** | **String**| The unique identifier of the transfer to be returned. | 
 **returnTransferRequest** | [**ReturnTransferRequest**](ReturnTransferRequest.md)|  | [optional] 

### Return type

[**ReturnTransferResponse**](ReturnTransferResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [clientKey](../README.md#clientKey), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

