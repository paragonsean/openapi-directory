# ContentApiForShopping.ShoppingAdsProgramStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**globalState** | **String** | State of the program. &#x60;ENABLED&#x60; if there are offers for at least one region. | [optional] 
**regionStatuses** | [**[ShoppingAdsProgramStatusRegionStatus]**](ShoppingAdsProgramStatusRegionStatus.md) | Status of the program in each region. Regions with the same status and review eligibility are grouped together in &#x60;regionCodes&#x60;. | [optional] 



## Enum: GlobalStateEnum


* `PROGRAM_STATE_UNSPECIFIED` (value: `"PROGRAM_STATE_UNSPECIFIED"`)

* `NOT_ENABLED` (value: `"NOT_ENABLED"`)

* `NO_OFFERS_UPLOADED` (value: `"NO_OFFERS_UPLOADED"`)

* `ENABLED` (value: `"ENABLED"`)




