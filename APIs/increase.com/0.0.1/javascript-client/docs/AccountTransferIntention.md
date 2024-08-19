# IncreaseApi.AccountTransferIntention

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The pending amount in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination account currency. | 
**description** | **String** | The description you chose to give the transfer. | 
**destinationAccountId** | **String** | The identifier of the Account to where the Account Transfer was sent. | 
**sourceAccountId** | **String** | The identifier of the Account from where the Account Transfer was sent. | 
**transferId** | **String** | The identifier of the Account Transfer that led to this Pending Transaction. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)




