# IncreaseApi.AccountTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The Account to which the transfer belongs. | 
**amount** | **Number** | The transfer amount in the minor unit of the destination account currency. For dollars, for example, this is cents. | 
**approval** | [**TransferApproval**](TransferApproval.md) |  | 
**cancellation** | [**TransferCancellation**](TransferCancellation.md) |  | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination account currency. | 
**description** | **String** | The description that will show on the transactions. | 
**destinationAccountId** | **String** | The destination account&#39;s identifier. | 
**destinationTransactionId** | **String** | The ID for the transaction receiving the transfer. | 
**id** | **String** | The account transfer&#39;s identifier. | 
**network** | **String** | The transfer&#39;s network. | 
**status** | **String** | The lifecycle status of the transfer. | 
**transactionId** | **String** | The ID for the transaction funding the transfer. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;account_transfer&#x60;. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: NetworkEnum


* `account` (value: `"account"`)





## Enum: StatusEnum


* `pending_approval` (value: `"pending_approval"`)

* `canceled` (value: `"canceled"`)

* `complete` (value: `"complete"`)





## Enum: TypeEnum


* `account_transfer` (value: `"account_transfer"`)




