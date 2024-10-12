# GooglePlayAndroidDeveloperApi.RecurringExternalTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**externalSubscription** | [**ExternalSubscription**](ExternalSubscription.md) |  | [optional] 
**externalTransactionToken** | **String** | Input only. Provided during the call to Create. Retrieved from the client when the alternative billing flow is launched. Required only for the initial purchase. | [optional] 
**initialExternalTransactionId** | **String** | The external transaction id of the first transaction of this recurring series of transactions. For example, for a subscription this would be the transaction id of the first payment. Required when creating recurring external transactions. | [optional] 
**migratedTransactionProgram** | **String** | Input only. Provided during the call to Create. Must only be used when migrating a subscription from manual monthly reporting to automated reporting. | [optional] 



## Enum: MigratedTransactionProgramEnum


* `EXTERNAL_TRANSACTION_PROGRAM_UNSPECIFIED` (value: `"EXTERNAL_TRANSACTION_PROGRAM_UNSPECIFIED"`)

* `USER_CHOICE_BILLING` (value: `"USER_CHOICE_BILLING"`)

* `ALTERTNATIVE_BILLING_ONLY` (value: `"ALTERTNATIVE_BILLING_ONLY"`)




