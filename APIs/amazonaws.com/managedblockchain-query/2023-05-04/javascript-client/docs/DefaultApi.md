# AmazonManagedBlockchainQuery.DefaultApi

All URIs are relative to *http://managedblockchain-query.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchGetTokenBalance**](DefaultApi.md#batchGetTokenBalance) | **POST** /batch-get-token-balance | 
[**getTokenBalance**](DefaultApi.md#getTokenBalance) | **POST** /get-token-balance | 
[**getTransaction**](DefaultApi.md#getTransaction) | **POST** /get-transaction | 
[**listTokenBalances**](DefaultApi.md#listTokenBalances) | **POST** /list-token-balances | 
[**listTransactionEvents**](DefaultApi.md#listTransactionEvents) | **POST** /list-transaction-events | 
[**listTransactions**](DefaultApi.md#listTransactions) | **POST** /list-transactions | 



## batchGetTokenBalance

> BatchGetTokenBalanceOutput batchGetTokenBalance(batchGetTokenBalanceRequest, opts)



&lt;p&gt;Gets the token balance for a batch of tokens by using the &lt;code&gt;GetTokenBalance&lt;/code&gt; action for every token in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only the native tokens BTC,ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonManagedBlockchainQuery from 'amazon_managed_blockchain_query';
let defaultClient = AmazonManagedBlockchainQuery.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedBlockchainQuery.DefaultApi();
let batchGetTokenBalanceRequest = new AmazonManagedBlockchainQuery.BatchGetTokenBalanceRequest(); // BatchGetTokenBalanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchGetTokenBalance(batchGetTokenBalanceRequest, opts, (error, data, response) => {
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
 **batchGetTokenBalanceRequest** | [**BatchGetTokenBalanceRequest**](BatchGetTokenBalanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchGetTokenBalanceOutput**](BatchGetTokenBalanceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTokenBalance

> GetTokenBalanceOutput getTokenBalance(getTokenBalanceRequest, opts)



&lt;p&gt;Gets the balance of a specific token, including native tokens, for a given address (wallet or contract) on the blockchain.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only the native tokens BTC,ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonManagedBlockchainQuery from 'amazon_managed_blockchain_query';
let defaultClient = AmazonManagedBlockchainQuery.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedBlockchainQuery.DefaultApi();
let getTokenBalanceRequest = new AmazonManagedBlockchainQuery.GetTokenBalanceRequest(); // GetTokenBalanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTokenBalance(getTokenBalanceRequest, opts, (error, data, response) => {
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
 **getTokenBalanceRequest** | [**GetTokenBalanceRequest**](GetTokenBalanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTokenBalanceOutput**](GetTokenBalanceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTransaction

> GetTransactionOutput getTransaction(getTransactionRequest, opts)



Get the details of a transaction.

### Example

```javascript
import AmazonManagedBlockchainQuery from 'amazon_managed_blockchain_query';
let defaultClient = AmazonManagedBlockchainQuery.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedBlockchainQuery.DefaultApi();
let getTransactionRequest = new AmazonManagedBlockchainQuery.GetTransactionRequest(); // GetTransactionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTransaction(getTransactionRequest, opts, (error, data, response) => {
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
 **getTransactionRequest** | [**GetTransactionRequest**](GetTransactionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTransactionOutput**](GetTransactionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTokenBalances

> ListTokenBalancesOutput listTokenBalances(listTokenBalancesRequest, opts)



&lt;p&gt;This action returns the following for a given a blockchain network:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Lists all token balances owned by an address (either a contact address or a wallet address).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lists all token balances for all tokens created by a contract.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lists all token balances for a given token.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;You must always specify the network property of the &lt;code&gt;tokenFilter&lt;/code&gt; when using this operation.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonManagedBlockchainQuery from 'amazon_managed_blockchain_query';
let defaultClient = AmazonManagedBlockchainQuery.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedBlockchainQuery.DefaultApi();
let listTokenBalancesRequest = new AmazonManagedBlockchainQuery.ListTokenBalancesRequest(); // ListTokenBalancesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listTokenBalances(listTokenBalancesRequest, opts, (error, data, response) => {
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
 **listTokenBalancesRequest** | [**ListTokenBalancesRequest**](ListTokenBalancesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListTokenBalancesOutput**](ListTokenBalancesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTransactionEvents

> ListTransactionEventsOutput listTransactionEvents(listTransactionEventsRequest, opts)



An array of &lt;code&gt;TransactionEvent&lt;/code&gt; objects. Each object contains details about the transaction event.

### Example

```javascript
import AmazonManagedBlockchainQuery from 'amazon_managed_blockchain_query';
let defaultClient = AmazonManagedBlockchainQuery.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedBlockchainQuery.DefaultApi();
let listTransactionEventsRequest = new AmazonManagedBlockchainQuery.ListTransactionEventsRequest(); // ListTransactionEventsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listTransactionEvents(listTransactionEventsRequest, opts, (error, data, response) => {
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
 **listTransactionEventsRequest** | [**ListTransactionEventsRequest**](ListTransactionEventsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListTransactionEventsOutput**](ListTransactionEventsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTransactions

> ListTransactionsOutput listTransactions(listTransactionsRequest, opts)



Lists all of the transactions on a given wallet address or to a specific contract.

### Example

```javascript
import AmazonManagedBlockchainQuery from 'amazon_managed_blockchain_query';
let defaultClient = AmazonManagedBlockchainQuery.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedBlockchainQuery.DefaultApi();
let listTransactionsRequest = new AmazonManagedBlockchainQuery.ListTransactionsRequest(); // ListTransactionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listTransactions(listTransactionsRequest, opts, (error, data, response) => {
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
 **listTransactionsRequest** | [**ListTransactionsRequest**](ListTransactionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListTransactionsOutput**](ListTransactionsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

