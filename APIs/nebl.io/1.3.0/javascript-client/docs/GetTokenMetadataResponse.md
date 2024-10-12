# NeblioRestApiSuite.GetTokenMetadataResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationPolicy** | **String** | Whether the tokens are aggregatable | [optional] 
**divisibility** | **Number** | Decimal places the token is divisible to | [optional] 
**firstBlock** | **Number** | Block number token was issued in | [optional] 
**initialIssuanceAmount** | **Number** | Total tokens issued in initial issuance | [optional] 
**issuanceTxid** | **String** | TXID the token was issued with | [optional] 
**issueAddress** | **String** | Address that issued the tokens | [optional] 
**lockStatus** | **Boolean** | Whether issuance of more tokens is locked | [optional] 
**metadataOfIssuance** | [**GetTokenMetadataResponseMetadataOfIssuance**](GetTokenMetadataResponseMetadataOfIssuance.md) |  | [optional] 
**metadataOfUtxo** | [**GetTokenMetadataResponseMetadataOfUtxo**](GetTokenMetadataResponseMetadataOfUtxo.md) |  | [optional] 
**numOfBurns** | **Number** | Number of times tokens have been burned | [optional] 
**numOfHolders** | **Number** | Total number of addresses this token is held at | [optional] 
**numOfIssuance** | **Number** | Total number of times this token has been issued | [optional] 
**numOfTransfers** | **Number** | Total number of transactions of this token | [optional] 
**someUtxo** | **String** | Example UTXO containing this token. | [optional] 
**tokenId** | **String** | ID of the token | [optional] 
**totalSupply** | **Number** | Total number of tokens in supply | [optional] 


