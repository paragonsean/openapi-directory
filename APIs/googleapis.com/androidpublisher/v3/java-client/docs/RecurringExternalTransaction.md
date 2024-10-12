

# RecurringExternalTransaction

Represents a transaction that is part of a recurring series of payments. This can be a subscription or a one-time product with multiple payments (such as preorder).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalSubscription** | [**ExternalSubscription**](ExternalSubscription.md) |  |  [optional] |
|**externalTransactionToken** | **String** | Input only. Provided during the call to Create. Retrieved from the client when the alternative billing flow is launched. Required only for the initial purchase. |  [optional] |
|**initialExternalTransactionId** | **String** | The external transaction id of the first transaction of this recurring series of transactions. For example, for a subscription this would be the transaction id of the first payment. Required when creating recurring external transactions. |  [optional] |
|**migratedTransactionProgram** | [**MigratedTransactionProgramEnum**](#MigratedTransactionProgramEnum) | Input only. Provided during the call to Create. Must only be used when migrating a subscription from manual monthly reporting to automated reporting. |  [optional] |



## Enum: MigratedTransactionProgramEnum

| Name | Value |
|---- | -----|
| EXTERNAL_TRANSACTION_PROGRAM_UNSPECIFIED | &quot;EXTERNAL_TRANSACTION_PROGRAM_UNSPECIFIED&quot; |
| USER_CHOICE_BILLING | &quot;USER_CHOICE_BILLING&quot; |
| ALTERTNATIVE_BILLING_ONLY | &quot;ALTERTNATIVE_BILLING_ONLY&quot; |



