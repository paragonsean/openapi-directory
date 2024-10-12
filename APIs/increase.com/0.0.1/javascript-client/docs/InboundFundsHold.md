# IncreaseApi.InboundFundsHold

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The held amount in the minor unit of the account&#39;s currency. For dollars, for example, this is cents. | 
**automaticallyReleasesAt** | **Date** | When the hold will be released automatically. Certain conditions may cause it to be released before this time. | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the hold was created. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the hold&#39;s currency. | 
**heldTransactionId** | **String** | The ID of the Transaction for which funds were held. | 
**pendingTransactionId** | **String** | The ID of the Pending Transaction representing the held funds. | 
**releasedAt** | **Date** | When the hold was released (if it has been released). | 
**status** | **String** | The status of the hold. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: StatusEnum


* `held` (value: `"held"`)

* `complete` (value: `"complete"`)




