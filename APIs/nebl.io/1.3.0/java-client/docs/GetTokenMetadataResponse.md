

# GetTokenMetadataResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationPolicy** | **String** | Whether the tokens are aggregatable |  [optional] |
|**divisibility** | **BigDecimal** | Decimal places the token is divisible to |  [optional] |
|**firstBlock** | **BigDecimal** | Block number token was issued in |  [optional] |
|**initialIssuanceAmount** | **BigDecimal** | Total tokens issued in initial issuance |  [optional] |
|**issuanceTxid** | **String** | TXID the token was issued with |  [optional] |
|**issueAddress** | **String** | Address that issued the tokens |  [optional] |
|**lockStatus** | **Boolean** | Whether issuance of more tokens is locked |  [optional] |
|**metadataOfIssuance** | [**GetTokenMetadataResponseMetadataOfIssuance**](GetTokenMetadataResponseMetadataOfIssuance.md) |  |  [optional] |
|**metadataOfUtxo** | [**GetTokenMetadataResponseMetadataOfUtxo**](GetTokenMetadataResponseMetadataOfUtxo.md) |  |  [optional] |
|**numOfBurns** | **BigDecimal** | Number of times tokens have been burned |  [optional] |
|**numOfHolders** | **BigDecimal** | Total number of addresses this token is held at |  [optional] |
|**numOfIssuance** | **BigDecimal** | Total number of times this token has been issued |  [optional] |
|**numOfTransfers** | **BigDecimal** | Total number of transactions of this token |  [optional] |
|**someUtxo** | **String** | Example UTXO containing this token. |  [optional] |
|**tokenId** | **String** | ID of the token |  [optional] |
|**totalSupply** | **BigDecimal** | Total number of tokens in supply |  [optional] |



