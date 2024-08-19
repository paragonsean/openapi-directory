# ThePlaidApi.WalletTransactionListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextCursor** | **String** | Cursor used for fetching transactions created before the latest transaction provided in this response | [optional] 
**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**transactions** | [**[WalletTransaction]**](WalletTransaction.md) | An array of transactions of an e-wallet, associated with the given &#x60;wallet_id&#x60; | 


