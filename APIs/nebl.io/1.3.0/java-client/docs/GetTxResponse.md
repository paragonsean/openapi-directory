

# GetTxResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockhash** | **String** | Hash of the block this transaction is in |  [optional] |
|**blockheight** | **BigDecimal** | Block height of this transaction |  [optional] |
|**blocktime** | **BigDecimal** | Block time of this transaction |  [optional] |
|**confirmations** | **BigDecimal** | Number of transaction confirmations |  [optional] |
|**fee** | **BigDecimal** | Total NEBL used as fee for this transcation in satoshis |  [optional] |
|**fees** | **BigDecimal** | Total NEBL used in fees for this transaction |  [optional] |
|**locktime** | **BigDecimal** | Transaction locktime |  [optional] |
|**size** | **BigDecimal** | Transcation size in bytes |  [optional] |
|**time** | **BigDecimal** | Transaction time |  [optional] |
|**totalsent** | **BigDecimal** | Total NEBL sent in this transaction in satoshis |  [optional] |
|**txid** | **String** | TXID of transaction |  [optional] |
|**valueIn** | **BigDecimal** | Total NEBL input in this transaction |  [optional] |
|**valueOut** | **BigDecimal** | Total NEBL output in this transaction |  [optional] |
|**version** | **BigDecimal** | Transaction version |  [optional] |
|**vin** | [**List&lt;GetTxResponseVinInner&gt;**](GetTxResponseVinInner.md) | Array of transaction inputs |  [optional] |
|**vout** | [**List&lt;GetTxResponseVoutInner&gt;**](GetTxResponseVoutInner.md) | Array of transaction outputs |  [optional] |



