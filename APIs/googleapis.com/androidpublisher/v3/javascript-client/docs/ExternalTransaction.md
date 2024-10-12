# GooglePlayAndroidDeveloperApi.ExternalTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when this transaction was created. This is the time when Google was notified of the transaction. | [optional] [readonly] 
**currentPreTaxAmount** | [**Price**](Price.md) |  | [optional] 
**currentTaxAmount** | [**Price**](Price.md) |  | [optional] 
**externalTransactionId** | **String** | Output only. The id of this transaction. All transaction ids under the same package name must be unique. Set when creating the external transaction. | [optional] [readonly] 
**oneTimeTransaction** | [**OneTimeExternalTransaction**](OneTimeExternalTransaction.md) |  | [optional] 
**originalPreTaxAmount** | [**Price**](Price.md) |  | [optional] 
**originalTaxAmount** | [**Price**](Price.md) |  | [optional] 
**packageName** | **String** | Output only. The resource name of the external transaction. The package name of the application the inapp products were sold (for example, &#39;com.some.app&#39;). | [optional] [readonly] 
**recurringTransaction** | [**RecurringExternalTransaction**](RecurringExternalTransaction.md) |  | [optional] 
**testPurchase** | **Object** | Represents a transaction performed using a test account. These transactions will not be charged by Google. | [optional] 
**transactionState** | **String** | Output only. The current state of the transaction. | [optional] [readonly] 
**transactionTime** | **String** | Required. The time when the transaction was completed. | [optional] 
**userTaxAddress** | [**ExternalTransactionAddress**](ExternalTransactionAddress.md) |  | [optional] 



## Enum: TransactionStateEnum


* `STATE_UNSPECIFIED` (value: `"TRANSACTION_STATE_UNSPECIFIED"`)

* `REPORTED` (value: `"TRANSACTION_REPORTED"`)

* `CANCELED` (value: `"TRANSACTION_CANCELED"`)




