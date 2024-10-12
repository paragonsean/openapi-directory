

# ReconciliationResponse

It conveys Information related to the Reconciliation transaction processed by the POI System. Content of the Reconciliation Response message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**poIReconciliationID** | **Integer** | Absent if ReconciliationType is AcquirerReconciliation. |  [optional] |
|**reconciliationType** | **ReconciliationType** |  |  |
|**response** | [**Response**](Response.md) |  |  |
|**transactionTotals** | [**List&lt;TransactionTotals&gt;**](TransactionTotals.md) |  |  [optional] |



