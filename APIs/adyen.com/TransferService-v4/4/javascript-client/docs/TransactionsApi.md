# TransfersApi.TransactionsApi

All URIs are relative to *https://balanceplatform-api-test.adyen.com/btl/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTransactions**](TransactionsApi.md#getTransactions) | **GET** /transactions | Get all transactions
[**getTransactionsId**](TransactionsApi.md#getTransactionsId) | **GET** /transactions/{id} | Get a transaction



## getTransactions

> TransactionSearchResponse getTransactions(createdSince, createdUntil, opts)

Get all transactions

&gt;Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.  Returns all the transactions related to a balance account, account holder, or balance platform.  When making this request, you must include at least one of the following: - &#x60;balanceAccountId&#x60; - &#x60;accountHolderId&#x60; - &#x60;balancePlatform&#x60;.  This endpoint supports cursor-based pagination. The response returns the first page of results, and returns links to the next and previous pages when applicable. You can use the links to page through the results.  

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

let apiInstance = new TransfersApi.TransactionsApi();
let createdSince = new Date("2013-10-20T19:20:30+01:00"); // Date | Only include transactions that have been created on or after this point in time. The value must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
let createdUntil = new Date("2013-10-20T19:20:30+01:00"); // Date | Only include transactions that have been created on or before this point in time. The value must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
let opts = {
  'balancePlatform': "balancePlatform_example", // String | The unique identifier of the [balance platform](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id).  Required if you don't provide a `balanceAccountId` or `accountHolderId`.
  'paymentInstrumentId': "paymentInstrumentId_example", // String | The unique identifier of the [payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_).  To use this parameter, you must also provide a `balanceAccountId`, `accountHolderId`, or `balancePlatform`.  The `paymentInstrumentId` must be related to the `balanceAccountId` or `accountHolderId` that you provide.
  'accountHolderId': "accountHolderId_example", // String | The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id).  Required if you don't provide a `balanceAccountId` or `balancePlatform`.  If you provide a `balanceAccountId`, the `accountHolderId` must be related to the `balanceAccountId`.
  'balanceAccountId': "balanceAccountId_example", // String | The unique identifier of the [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id).  Required if you don't provide an `accountHolderId` or `balancePlatform`.  If you provide an `accountHolderId`, the `balanceAccountId` must be related to the `accountHolderId`.
  'cursor': "cursor_example", // String | The `cursor` returned in the links of the previous response.
  'limit': 56 // Number | The number of items returned per page, maximum of 100 items. By default, the response returns 10 items per page.
};
apiInstance.getTransactions(createdSince, createdUntil, opts, (error, data, response) => {
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
 **createdSince** | **Date**| Only include transactions that have been created on or after this point in time. The value must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**. | 
 **createdUntil** | **Date**| Only include transactions that have been created on or before this point in time. The value must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**. | 
 **balancePlatform** | **String**| The unique identifier of the [balance platform](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id).  Required if you don&#39;t provide a &#x60;balanceAccountId&#x60; or &#x60;accountHolderId&#x60;. | [optional] 
 **paymentInstrumentId** | **String**| The unique identifier of the [payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_).  To use this parameter, you must also provide a &#x60;balanceAccountId&#x60;, &#x60;accountHolderId&#x60;, or &#x60;balancePlatform&#x60;.  The &#x60;paymentInstrumentId&#x60; must be related to the &#x60;balanceAccountId&#x60; or &#x60;accountHolderId&#x60; that you provide. | [optional] 
 **accountHolderId** | **String**| The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id).  Required if you don&#39;t provide a &#x60;balanceAccountId&#x60; or &#x60;balancePlatform&#x60;.  If you provide a &#x60;balanceAccountId&#x60;, the &#x60;accountHolderId&#x60; must be related to the &#x60;balanceAccountId&#x60;. | [optional] 
 **balanceAccountId** | **String**| The unique identifier of the [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id).  Required if you don&#39;t provide an &#x60;accountHolderId&#x60; or &#x60;balancePlatform&#x60;.  If you provide an &#x60;accountHolderId&#x60;, the &#x60;balanceAccountId&#x60; must be related to the &#x60;accountHolderId&#x60;. | [optional] 
 **cursor** | **String**| The &#x60;cursor&#x60; returned in the links of the previous response. | [optional] 
 **limit** | **Number**| The number of items returned per page, maximum of 100 items. By default, the response returns 10 items per page. | [optional] 

### Return type

[**TransactionSearchResponse**](TransactionSearchResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [clientKey](../README.md#clientKey), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionsId

> Transaction getTransactionsId(id)

Get a transaction

&gt;Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.  Returns a transaction.

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

let apiInstance = new TransfersApi.TransactionsApi();
let id = "id_example"; // String | The unique identifier of the transaction.
apiInstance.getTransactionsId(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the transaction. | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [clientKey](../README.md#clientKey), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

