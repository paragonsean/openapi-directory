

# Transaction

<p>There are two possible types of transactions used for this data type:</p> <ul> <li> <p>A Bitcoin transaction is a movement of BTC from one address to another.</p> </li> <li> <p>An Ethereum transaction refers to an action initiated by an externally owned account, which is an account managed by a human, not a contract. For example, if Bob sends Alice 1 ETH, Bob's account must be debited and Alice's must be credited. This state-changing action occurs within a transaction.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**network** | [**QueryNetwork**](QueryNetwork.md) |  |  |
|**blockHash** | [**String**](String.md) |  |  [optional] |
|**transactionHash** | [**String**](String.md) |  |  |
|**blockNumber** | [**String**](String.md) |  |  [optional] |
|**transactionTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**transactionIndex** | [**Integer**](Integer.md) |  |  |
|**numberOfTransactions** | [**Integer**](Integer.md) |  |  |
|**status** | [**QueryTransactionStatus**](QueryTransactionStatus.md) |  |  |
|**to** | [**String**](String.md) |  |  |
|**from** | [**String**](String.md) |  |  [optional] |
|**contractAddress** | [**String**](String.md) |  |  [optional] |
|**gasUsed** | [**String**](String.md) |  |  [optional] |
|**cumulativeGasUsed** | [**String**](String.md) |  |  [optional] |
|**effectiveGasPrice** | [**String**](String.md) |  |  [optional] |
|**signatureV** | [**Integer**](Integer.md) |  |  [optional] |
|**signatureR** | [**String**](String.md) |  |  [optional] |
|**signatureS** | [**String**](String.md) |  |  [optional] |
|**transactionFee** | [**String**](String.md) |  |  [optional] |
|**transactionId** | [**String**](String.md) |  |  [optional] |



