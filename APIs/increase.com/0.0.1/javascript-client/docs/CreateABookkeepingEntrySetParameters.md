# IncreaseApi.CreateABookkeepingEntrySetParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **Date** | The date of the transaction. If &#x60;transaction_id&#x60; is provided, this must match the &#x60;created_at&#x60; field on that resource. | [optional] 
**entries** | [**[CreateABookkeepingEntrySetParametersEntriesInner]**](CreateABookkeepingEntrySetParametersEntriesInner.md) | The bookkeeping entries. | 
**transactionId** | **String** | The identifier of the Transaction related to this entry set, if any. | [optional] 


