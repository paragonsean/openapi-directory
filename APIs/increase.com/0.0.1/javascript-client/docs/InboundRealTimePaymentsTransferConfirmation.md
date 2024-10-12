# IncreaseApi.InboundRealTimePaymentsTransferConfirmation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The amount in the minor unit of the transfer&#39;s currency. For dollars, for example, this is cents. | 
**creditorName** | **String** | The name the sender of the transfer specified as the recipient of the transfer. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code of the transfer&#39;s currency. This will always be \&quot;USD\&quot; for a Real Time Payments transfer. | 
**debtorAccountNumber** | **String** | The account number of the account that sent the transfer. | 
**debtorName** | **String** | The name provided by the sender of the transfer. | 
**debtorRoutingNumber** | **String** | The routing number of the account that sent the transfer. | 
**remittanceInformation** | **String** | Additional information included with the transfer. | 
**transactionIdentification** | **String** | The Real Time Payments network identification of the transfer | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)




