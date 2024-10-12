# AccountApi.PerformVerificationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderCode** | **String** | The code of the account holder to verify. | 
**accountStateType** | **String** | The state required for the account holder. &gt; Permitted values: &#x60;Processing&#x60;, &#x60;Payout&#x60;. | 
**tier** | **Number** | The tier required for the account holder. | 



## Enum: AccountStateTypeEnum


* `LimitedPayout` (value: `"LimitedPayout"`)

* `LimitedProcessing` (value: `"LimitedProcessing"`)

* `LimitlessPayout` (value: `"LimitlessPayout"`)

* `LimitlessProcessing` (value: `"LimitlessProcessing"`)

* `Payout` (value: `"Payout"`)

* `Processing` (value: `"Processing"`)




