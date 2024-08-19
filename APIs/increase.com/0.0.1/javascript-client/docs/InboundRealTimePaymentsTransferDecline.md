# IncreaseApi.InboundRealTimePaymentsTransferDecline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The declined amount in the minor unit of the destination account currency. For dollars, for example, this is cents. | 
**creditorName** | **String** | The name the sender of the transfer specified as the recipient of the transfer. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code of the declined transfer&#39;s currency. This will always be \&quot;USD\&quot; for a Real Time Payments transfer. | 
**debtorAccountNumber** | **String** | The account number of the account that sent the transfer. | 
**debtorName** | **String** | The name provided by the sender of the transfer. | 
**debtorRoutingNumber** | **String** | The routing number of the account that sent the transfer. | 
**reason** | **String** | Why the transfer was declined. | 
**remittanceInformation** | **String** | Additional information included with the transfer. | 
**transactionIdentification** | **String** | The Real Time Payments network identification of the declined transfer. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: ReasonEnum


* `account_number_canceled` (value: `"account_number_canceled"`)

* `account_number_disabled` (value: `"account_number_disabled"`)

* `group_locked` (value: `"group_locked"`)

* `entity_not_active` (value: `"entity_not_active"`)

* `real_time_payments_not_enabled` (value: `"real_time_payments_not_enabled"`)




