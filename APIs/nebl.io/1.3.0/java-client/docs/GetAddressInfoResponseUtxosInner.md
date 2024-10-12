

# GetAddressInfoResponseUtxosInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockheight** | **BigDecimal** | Blockheight of the UTXO |  [optional] |
|**blocktime** | **BigDecimal** | Blocktime of the UTXO |  [optional] |
|**index** | **BigDecimal** | Index of the UTXO at this address |  [optional] |
|**scriptPubKey** | **Object** | Object representing the scruptPubKey of the UTXO |  [optional] |
|**tokens** | [**List&lt;GetAddressInfoResponseUtxosInnerTokensInner&gt;**](GetAddressInfoResponseUtxosInnerTokensInner.md) | Array of NTP1 tokens in this UTXO. |  [optional] |
|**txid** | **String** | Txid of this UTXO |  [optional] |
|**used** | **Boolean** | Whether the UTXO has been used |  [optional] |
|**value** | **BigDecimal** | Value of the UTXO in NEBL satoshi |  [optional] |



