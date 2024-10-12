

# GetTransactionInfoResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockhash** | **String** | Hash of the block this transaction is in |  [optional] |
|**blockheight** | **BigDecimal** | Block height of this transaction |  [optional] |
|**blocktime** | **BigDecimal** | Block time of this transaction |  [optional] |
|**confirmations** | **BigDecimal** | Number of transaction confirmations |  [optional] |
|**fee** | **BigDecimal** | Total NEBL used as fee for this transcation in satoshis |  [optional] |
|**hex** | **String** | Transaction in raw hex |  [optional] |
|**locktime** | **BigDecimal** | Transaction locktime |  [optional] |
|**time** | **BigDecimal** | Transaction time |  [optional] |
|**totalsent** | **BigDecimal** | Total NEBL sent in this transaction in satoshis |  [optional] |
|**txid** | **String** | TXID of transaction |  [optional] |
|**version** | **BigDecimal** | Transaction version |  [optional] |
|**vin** | [**List&lt;GetTransactionInfoResponseVinInner&gt;**](GetTransactionInfoResponseVinInner.md) | Array of transaction inputs |  [optional] |
|**vout** | [**List&lt;GetTransactionInfoResponseVoutInner&gt;**](GetTransactionInfoResponseVoutInner.md) | Array of transaction outputs |  [optional] |



