# AmazonManagedBlockchainQuery.ListTransactionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | The address (either a contract or wallet), whose transactions are being requested. | 
**network** | **String** | The blockchain network where the transactions occurred. | 
**fromBlockchainInstant** | [**GetTokenBalanceRequestAtBlockchainInstant**](GetTokenBalanceRequestAtBlockchainInstant.md) |  | [optional] 
**toBlockchainInstant** | [**GetTokenBalanceRequestAtBlockchainInstant**](GetTokenBalanceRequestAtBlockchainInstant.md) |  | [optional] 
**sort** | [**ListTransactionsRequestSort**](ListTransactionsRequestSort.md) |  | [optional] 
**nextToken** | **String** | The pagination token that indicates the next set of results to retrieve. | [optional] 
**maxResults** | **Number** | &lt;p&gt;The maximum number of transactions to list.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Even if additional results can be retrieved, the request can return less results than &lt;code&gt;maxResults&lt;/code&gt; or an empty array of results.&lt;/p&gt; &lt;p&gt;To retrieve the next set of results, make another request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. The value of &lt;code&gt;nextToken&lt;/code&gt; is &lt;code&gt;null&lt;/code&gt; when there are no more results to return&lt;/p&gt; &lt;/note&gt; | [optional] 



## Enum: NetworkEnum


* `ETHEREUM_MAINNET` (value: `"ETHEREUM_MAINNET"`)

* `BITCOIN_MAINNET` (value: `"BITCOIN_MAINNET"`)




