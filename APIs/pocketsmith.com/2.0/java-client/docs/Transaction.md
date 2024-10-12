

# Transaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** |  |  [optional] |
|**amountInBaseCurrency** | **BigDecimal** | The amount of the transaction in the user&#39;s base currency. |  [optional] |
|**category** | [**Category**](Category.md) |  |  [optional] |
|**chequeNumber** | **String** |  |  [optional] |
|**closingBalance** | **BigDecimal** | The closing balance of the account at the transaction. |  [optional] |
|**createdAt** | **String** | When the transaction was created. |  [optional] |
|**date** | **String** | The date the transaction took place. |  [optional] |
|**id** | **Integer** | The unique identifier of the transaction. |  [optional] |
|**isTransfer** | **Boolean** | Whether the transaction is a transfer. |  [optional] |
|**labels** | **List&lt;String&gt;** |  |  [optional] |
|**memo** | **String** |  |  [optional] |
|**needsReview** | **Boolean** | Whether the transaction needs to be reviewed. |  [optional] |
|**note** | **String** |  |  [optional] |
|**originalPayee** | **String** | The payee the transaction was created with. |  [optional] |
|**payee** | **String** | The payee/merchant of the transaction. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the transaction. Pending transactions are temporary and may be superseded later by their posted counterparts, which are permanent. |  [optional] |
|**transactionAccount** | [**TransactionAccount**](TransactionAccount.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Whether the transaction is a debit or a credit |  [optional] |
|**updatedAt** | **String** | When the transaction was last updated. |  [optional] |
|**uploadSource** | **String** | Where the transaction came from. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| POSTED | &quot;posted&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DEBIT | &quot;debit&quot; |
| CREDIT | &quot;credit&quot; |



