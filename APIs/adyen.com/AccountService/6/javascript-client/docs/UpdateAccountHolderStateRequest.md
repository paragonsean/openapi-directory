# AccountApi.UpdateAccountHolderStateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderCode** | **String** | The code of the Account Holder on which to update the state. | 
**disable** | **Boolean** | If true, disable the requested state.  If false, enable the requested state. | 
**reason** | **String** | The reason that the state is being updated. &gt;Required if the state is being disabled. | [optional] 
**stateType** | **String** | The state to be updated. &gt;Permitted values are: &#x60;Processing&#x60;, &#x60;Payout&#x60; | 



## Enum: StateTypeEnum


* `LimitedPayout` (value: `"LimitedPayout"`)

* `LimitedProcessing` (value: `"LimitedProcessing"`)

* `LimitlessPayout` (value: `"LimitlessPayout"`)

* `LimitlessProcessing` (value: `"LimitlessProcessing"`)

* `Payout` (value: `"Payout"`)

* `Processing` (value: `"Processing"`)




