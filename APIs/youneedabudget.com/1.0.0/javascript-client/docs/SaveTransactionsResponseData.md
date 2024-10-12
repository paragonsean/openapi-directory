# YnabApiEndpoints.SaveTransactionsResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duplicateImportIds** | **[String]** | If multiple transactions were specified, a list of import_ids that were not created because of an existing &#x60;import_id&#x60; found on the same account | [optional] 
**serverKnowledge** | **Number** | The knowledge of the server | 
**transaction** | [**TransactionDetail**](TransactionDetail.md) |  | [optional] 
**transactionIds** | **[String]** | The transaction ids that were saved | 
**transactions** | [**[TransactionDetail]**](TransactionDetail.md) | If multiple transactions were specified, the transactions that were saved | [optional] 


